---
name: scaffold-iterate
description: Adversarial two-loop document review using an external LLM. The reviewer raises issues; Claude discusses, pushes back, or accepts. Use to catch blind spots self-review misses.
argument-hint: [document-path] [--focus "section or concern"] [--iterations N]
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# Adversarial Document Review

Run an adversarial two-loop review of a scaffold document using an external LLM reviewer.

## Architecture

```
OUTER LOOP (iterations — fresh review of updated doc)
├─ Iteration 1
│   ├─ Python script sends doc to external LLM → gets structured issues JSON
│   ├─ INNER LOOP (exchanges — back-and-forth conversation)
│   │   ├─ Claude evaluates each issue (agree / pushback / partial)
│   │   ├─ If pushback → Python script sends Claude's response to reviewer
│   │   ├─ Reviewer counter-responds → Claude re-evaluates
│   │   └─ ... until consensus or max exchanges
│   ├─ Apply agreed changes to document
│   └─ Log iteration in review log
├─ Iteration 2 (fresh review of updated doc)
└─ ... up to max_iterations or until no issues found
```

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `document-path` | Yes | — | Path or document ID (e.g., `SYS-001`, `SPEC-003`) |
| `--focus` | No | — | Focus the review on a specific section or concern. The reviewer will concentrate on this area and only flag issues outside it if HIGH severity. Example: `--focus "authority compliance"`, `--focus "Core Loop section"` |
| `--iterations` | No | Tier default | Override the number of outer loop iterations. Tier defaults: Full=5, Lite=1, Lint=1. Use to run more passes on critical docs or limit passes when time is short. |

## Steps

### 1. Resolve Target and Parse Options

Parse the user's arguments. Extract:
- **document-path** (required) — the file path or document ID
- **--focus** (optional) — if present, pass to the Python script via `--focus`
- **--iterations** (optional) — if present, use this instead of the tier default for the outer loop count

Resolve the document path:
- If a path is given, verify the file exists.
- If a document ID is given (e.g., `SYS-001`, `SPEC-003`, `TASK-012`), find the matching file:
  - `SYS-###` → `scaffold/design/systems/SYS-###-*.md`
  - `SPEC-###` → `scaffold/specs/SPEC-###-*.md`
  - `TASK-###` → `scaffold/tasks/TASK-###-*.md`
  - `SLICE-###` → `scaffold/slices/SLICE-###-*.md`
  - `P#-###` → `scaffold/phases/P#-###-*.md`
  - `ADR-###` → `scaffold/decisions/ADR-###-*.md`

### 2. Detect Type and Tier

The Python script auto-detects the document type from its path. The type determines the review tier:

| Tier | Max Iter | Max Exchanges | Severity | Doc Types |
|------|----------|---------------|----------|-----------|
| Full | 5 | 5 | All | design, style, system, roadmap, phase, spec |
| Lite | 1 | 3 | HIGH only | engine, input, slice, task |
| Lint | 1 | 2 | HIGH only + accuracy | reference |

### 3. Gather Context Files

Based on the document type, read these context files and pass them to the reviewer via `--context-files`:

| Type | Context Files |
|------|---------------|
| design | `scaffold/doc-authority.md`, `scaffold/design/systems/_index.md` |
| style | `scaffold/design/design-doc.md`, `scaffold/design/glossary.md` |
| system | `scaffold/design/design-doc.md`, `scaffold/doc-authority.md`, `scaffold/design/interfaces.md`, `scaffold/design/glossary.md` |
| reference | `scaffold/design/systems/_index.md`, relevant system files |
| engine | `scaffold/design/design-doc.md` |
| input | `scaffold/design/design-doc.md`, `scaffold/design/glossary.md` |
| roadmap | `scaffold/design/design-doc.md`, `scaffold/design/systems/_index.md`, `scaffold/decisions/known-issues.md` |
| phase | `scaffold/phases/roadmap.md`, `scaffold/design/design-doc.md`, all ADRs, `scaffold/decisions/known-issues.md` |
| slice | parent phase file, `scaffold/design/interfaces.md`, `scaffold/design/systems/_index.md` |
| spec | parent system file, parent slice file, `scaffold/design/state-transitions.md`, all ADRs |
| task | parent spec file, engine docs, `scaffold/reference/signal-registry.md` |

For types that reference "parent" files or "all ADRs", resolve dynamically:
- Read the document to find parent references (e.g., a spec's linked system or slice).
- Use Glob to find all `scaffold/decisions/ADR-*.md` files.
- Only include context files that exist — skip missing ones silently.

### 4. Outer Loop — Iterations

Determine the iteration count: use `--iterations` if the user provided it, otherwise use the tier's `max_iterations`.

For each iteration (up to that limit):

#### 4a. Request Review

Run:
```
python scaffold/tools/doc-review.py review <path> --iteration N --context-files <file1> <file2> ...
```

If the type wasn't auto-detected, add `--type <type>`.
If the user provided `--focus`, add `--focus "<value>"` to the command.

Parse the JSON output. If `"error"` key exists, report the error and stop.

#### 4b. Filter Issues by Tier

- **Full tier:** Keep all issues (HIGH, MEDIUM, LOW).
- **Lite tier:** Keep only HIGH severity issues.
- **Lint tier:** Keep only HIGH severity issues.

If no issues remain after filtering, skip the inner loop — the document passed review.

#### 4c. Inner Loop — Evaluate Each Issue

For each issue, read the relevant section of the document and any context files. Evaluate:

- **AGREE** — The issue is valid. Note the change to make.
- **PUSHBACK** — The issue is wrong or out of scope. Explain why with reference to project documents (authority chain, design doc, glossary, etc.).
- **PARTIAL** — The issue has merit but the suggested fix isn't right. Propose an alternative.

Compose Claude's response as a single message covering all issues, then send it:

```
python scaffold/tools/doc-review.py respond <path> --iteration N --message-file <temp-file>
```

Write Claude's response to a temporary file and pass it via `--message-file`.

Parse the reviewer's counter-response. For any issues where the reviewer pushes back on Claude's pushback, re-evaluate. Continue exchanges up to the tier's `max_exchanges`.

**Key rule:** Claude is the authority on this codebase. When the reviewer raises something that conflicts with project documents, Claude wins. Ties go to Claude.

#### 4d. Request Consensus

After the inner loop completes (agreement reached or max exchanges hit):

```
python scaffold/tools/doc-review.py consensus <path> --iteration N
```

Parse the consensus JSON.

#### 4e. Apply Changes

For each change in `changes_to_apply` from the consensus:
- Read the relevant section of the document.
- Apply the change using the Edit tool.
- Never apply changes that violate document authority (higher-rank docs win).

#### 4f. Log Iteration

Record the iteration results for the review log (issues raised, resolutions, changes applied, rejected issues).

#### 4g. Reappearing Issue Check

If the same issue (same location + same problem) appears across 2 or more iterations, escalate to the user. The reviewer and Claude cannot agree — the user must arbitrate.

### 5. Create Review Log

After all iterations complete, create a review log in `scaffold/reviews/`:
- Use the template at `scaffold/reviews/TEMPLATE-review.md`.
- Name it: `REVIEW-<doc-name>-<YYYY-MM-DD>.md`
- Fill in all sections from the iteration data.
- Update the Review Log table in `scaffold/reviews/_index.md` with a new row.

### 6. Update Document Status

If the review completed successfully (consensus reached, no unresolved HIGH issues), update the document's `> **Status:**` line from whatever it currently is to `Approved` using the Edit tool. If the review ended with unresolved HIGH issues or required user arbitration, leave the status unchanged.

### 7. Report

Present a summary to the user:
- Document reviewed, type, tier
- Total issues found vs. accepted vs. rejected
- Key changes made
- Any reappearing issues that need arbitration
- Link to the review log file

## Rules

- **Claude is the authority on this codebase.** Ties go to Claude. The reviewer is an outsider with no project context beyond what's provided.
- **Never apply changes that violate document authority.** If the reviewer suggests something that contradicts a higher-ranked document, reject it and explain why.
- **Never blindly accept.** Every issue gets evaluated against project context and the authority chain.
- **Pushback is expected and healthy.** The value of adversarial review is the discussion, not automatic acceptance.
- **Reappearing issues escalate to the user.** If the same issue persists across 2+ iterations, Claude and the reviewer cannot agree — the user decides.
- **If the Python script fails, report the error and stop.** Do not attempt to work around script errors.
- **Do not modify the Python script or config during a review.** If they need changes, report that separately.
- **Clean up temporary files** (message files used for `--message-file`) after use.
