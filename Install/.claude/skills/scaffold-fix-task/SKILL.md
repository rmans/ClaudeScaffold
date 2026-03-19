---
name: scaffold-fix-task
description: Review-fix loop for implementation tasks. Reviews, auto-fixes mechanical issues, and re-reviews until clean or max passes. Strategic issues are surfaced for human decision.
argument-hint: [TASK-### or TASK-###-TASK-###] [--iterate N]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Fix Task

Run an iterative review-fix loop on implementation tasks: **$ARGUMENTS**

Reviews the task, classifies issues as auto-fixable or human-required, applies safe fixes, and re-reviews until clean. This skill wraps the same checklist as `/scaffold-review-task` but adds write capability for mechanical fixes.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| task | No | — | Single `TASK-###`, range `TASK-###-TASK-###`, or omitted to list tasks and prompt for selection |
| `--iterate N` | No | 10 | Maximum review-fix passes per task. Stops early on convergence — if a pass produces no new issues, iteration ends. |

## Execution

**If range:**
1. Extract start and end numbers. Build ordered list.
2. For each task in order, run the full review-fix pipeline. **Parallelization:** Tasks whose `Depends on` fields are satisfied (all dependencies already processed or have no dependencies) can run in parallel. Tasks with unmet dependencies wait until those dependencies complete. See WORKFLOW.md Range Parallelization for the full pattern.
3. Between each task, output a horizontal rule (`---`).
4. Skip missing task files with a note: `**TASK-###: No file found — skipping.**`
5. After all tasks, output a summary table:

```
## Range Fix Summary: TASK-### through TASK-###

| Task | Status | Passes | Auto-Fixed | Human-Required | Final |
|------|--------|--------|------------|----------------|-------|
| TASK-### — Name | Clean | 2/3 | 4 fixes | 0 | Clean |
| TASK-### — Name | Needs human | 3/3 | 2 fixes | 1 issue | Blocked |
| TASK-### — Name | Skipped (no file) | — | — | — | — |
| TASK-### — Name | Blocked (malformed) | — | — | — | — |
```

**If single task or no argument:** Run the full review-fix pipeline for the selected task.

## Step 1 — Locate and Read Context

**Resolve the task target:**
- If a TASK-### ID is given, Glob `scaffold/tasks/TASK-###-*.md`.
- If a range is given, resolve each task in order (per Execution above).
- If no argument is provided, list registered tasks from `scaffold/tasks/_index.md` and ask the user which one to fix.
- If the task file doesn't exist, skip it (range mode) or report and stop (single mode).

**Read the task file first**, then **validate task metadata:** Verify it has an `Implements: SPEC-###` reference and recognizable section structure (Objective, Steps, Files Created, Files Modified, Verification, Deliverable, Verification Mapping). If the task is malformed enough that parent context can't be resolved, report it as `Blocked (malformed task metadata)` in the summary and skip to the next task in range mode, or stop in single mode.

**Read context** (same as `/scaffold-review-task`):

1. Read the parent spec — follow `Implements: SPEC-###`.
2. Read the parent system design.
3. Read relevant engine docs from `scaffold/engine/`.
4. Read the signal registry if the task involves signals.
5. Read ADRs referenced in the task, spec, and architecture. Skim titles for others.
6. Read `scaffold/design/architecture.md`.
7. Read `scaffold/design/glossary.md` — for terminology compliance checks.

## Step 2 — Review

Run the full review checklist (same as `/scaffold-review-task`):

- **Completeness** — check Objective, Task Type, Depends on, Steps, Files Created, Files Modified, Deliverable, Verification, Verification Mapping, Out of Scope, Risks, Notes.
- **Quality** — concrete steps, engine patterns, executable step order, realistic files (created vs modified), integration touchpoints, testable verification with negative checks, verification mapping to spec ACs, deliverable clarity, right-sized, no over-prescription.
- **Spec Alignment** — local alignment, sibling coverage awareness, verification mapping.
- **Engine Pattern Compliance** — coding conventions, scene architecture, UI, input, signals.
- **Architecture Compliance** — tick order, signal wiring, data flow, entity storage, component checklists.
- **ADR Impact** — relevant ADRs reflected in steps.
- **Prerequisites and Dependencies** — hidden prerequisites, test harness implications.
- **Terminology and Boundaries** — glossary compliance, boundary creep, verification scope mismatch.
- **Registration** — index and slice entries match.

Record all issues found.

## Step 3 — Classify Issues

For each issue, classify as:

### Auto-Fixable

Issues where the correct fix is unambiguous and local to this task file:

| Category | Example |
|----------|---------|
| **Vague Objective** | "Implement the system" → rewrite to one specific sentence based on spec |
| **Weak Verification** | "Verify it works" → rewrite with concrete checks from spec acceptance criteria |
| **Incomplete Files Created/Modified** | Steps reference files not in the Files Created or Files Modified list → add them to the correct list |
| **Extra files listed** | Files Created or Files Modified lists files no step touches → remove them |
| **File in wrong list** | File listed in Files Created but already exists (should be Files Modified), or vice versa → move to correct list |
| **Missing Deliverable** | Deliverable section absent or says "TBD" → derive from Objective and Steps |
| **Missing Verification Mapping** | Verification Mapping section absent → map existing verification steps to spec ACs |
| **Missing Out of Scope** | Out of Scope section absent → add empty Out of Scope section |
| **Missing Risks** | Risks section absent → add empty Risks section |
| **Missing Task Type** | Task Type header absent → infer from steps and files |
| **Missing Depends on** | Depends on header absent → add "None" or infer from step prerequisites |
| **Missing Notes placeholder** | Notes section absent → add empty Notes section |
| **Engine pattern wording** | Step says "connect signal in system" → fix to "wire signal in game_manager.gd" |
| **Architecture wording** | Step says "store in dictionary" → fix to "store in pre-allocated array (ADR-006)" |
| **Spec alignment wording** | Step implements spec behavior but wording doesn't match → align wording |
| **Missing ADR reference** | Step touches ADR-affected area but doesn't mention it → add ADR reference to Notes |
| **Missing test harness files** | Task adds system/signals but Files Affected doesn't list test files → add them |
| **Inconsistent terminology** | Step uses informal term instead of glossary canonical term → align wording |
| **Verification scope too broad** | Verification tests end-to-end but task only implements one piece → narrow to task scope |
| **Bad internal step order** | Steps depend on something a later step creates → reorder steps within the task |
| **Missing integration touchpoints** | Class/system created but not registered, not added to scene tree, no load path → add missing steps |
| **Verification missing negative checks** | Spec edge cases imply rejection/failure handling but verification only covers happy path → add negative checks |

### Human-Required

Issues that require judgment, cross-task coordination, or spec-level changes. Present using the Human Decision Presentation pattern (see WORKFLOW.md) — grouped by category, numbered, with concrete options (a/b/c) per issue:

| Category | Why |
|----------|-----|
| **Task too large — needs split** | Split boundaries are a design decision |
| **Spec mismatch — spec may be wrong** | Can't tell if task or spec needs changing |
| **Cross-task overlap** | Fixing requires coordinating multiple task files |
| **Cross-task reordering** | Ordering is a slice-level decision |
| **KI blocker in scope** | Strategy decision about whether to proceed |
| **Ownership ambiguity** | Which system owns this behavior is unclear |
| **Missing sibling task** | A new task may need to be created — can't do that here |
| **Hidden prerequisite unresolved** | Task assumes something no earlier task produces — ordering or new task needed |
| **Boundary creep** | Task crosses into a different concern — may need split or scope narrowing |
| **Over-prescriptive implementation** | Steps lock in design choices the spec doesn't require — judgment call on whether to loosen |
| **Registration mismatch** | Index or slice table changes need careful cross-referencing |

Before applying fixes, output a brief classification summary so the user can see what's happening:

```
Pass N: X auto-fixable, Y human-required
```

## Step 4 — Apply Auto-Fixes

For each auto-fixable issue:

1. Read the relevant section of the task file.
2. Apply the fix using the Edit tool.
3. Record what was changed and why.

**Fix rules:**
- Only edit the target task file. Never edit specs, slices, indexes, or other tasks.
- Preserve the task template structure — don't reorganize sections.
- Fixes must be minimal — change only what's needed to resolve the issue.
- When rewriting Objective or Verification, derive wording from the parent spec, not invented.
- When adding ADR references, use the format already present in the task's Notes section.

## Step 5 — Re-Review

After applying fixes, re-read the task file and run the full review checklist again on the updated content.

Compare issues with the previous pass:
- **Resolved** — issue no longer appears. Record as fixed.
- **New issues** — the fix may have exposed a deeper issue, or the fix itself introduced a problem. Classify and fix if auto-fixable.
- **Persistent human-required** — still present. Carry forward.
- **No new issues, no remaining auto-fixable issues** — stop. The task is as clean as auto-fixing can make it.

## Step 6 — Iterate

Continue the review-fix cycle until a stop condition is met.

**Stop conditions** (any one stops iteration):
- **Clean** — no issues found on a pass.
- **Human-only** — only human-required issues remain, no auto-fixable issues left.
- **Stable** — the remaining issue set is unchanged from the previous pass.
- **Limit** — iteration limit reached.

## Step 7 — Output

```
## Task Fix: TASK-### — [Name]

### Summary
| Field | Value |
|-------|-------|
| Spec | SPEC-### — [Name] |
| System | SYS-### — [Name] |
| Passes | N completed / M max [early stop: yes/no] |
| Auto-fixed | N issues |
| Human-required | N issues |
| Final status | Clean / Needs human input |

### Fixes Applied
| # | Category | What Changed | Section |
|---|----------|-------------|---------|
| 1 | Weak Verification | Added concrete checks from SPEC-### AC-1, AC-3 | Verification |
| 2 | Missing file | Added `game_manager.gd` to Files Modified | Files Modified |
| ... | ... | ... | ... |

### Human-Required Issues
| # | Category | Issue | Why Auto-Fix Cannot Resolve |
|---|----------|-------|----------------------------|
| 1 | Task too large | 12 steps, 7 files | Split boundaries need human decision |
| ... | ... | ... | ... |

### Final Review
[Brief final review status — which checklist areas are now clean, which still have issues]
```

If no issues were found on the first pass:

```
## Task Fix: TASK-### — [Name]

**Status: Clean** — no issues found. No changes made.
```

## Rules

- **Only fix mechanical, local issues.** Never make judgment calls about task scope, ordering, or spec correctness.
- **Only edit the task file.** Never edit specs, slices, indexes, engine docs, or other tasks. If a fix requires changes outside the task file, classify it as human-required.
- **Derive fixes from context, don't invent.** Rewritten Objectives come from the spec. Rewritten Verification comes from acceptance criteria. Added files come from step analysis. Never fabricate content.
- **Preserve task structure.** Don't reorganize sections, merge steps, or reformat beyond what the fix requires.
- **Stop when stable.** If the remaining issue set is unchanged from the previous pass, do not continue iterating.
- **Surface human-required issues clearly.** The user needs to know what still needs their attention and why.
- **Registration fixes are human-required.** Index and slice table edits involve cross-file coordination — flag them, don't attempt them.
- **Sizing is human-required.** Suggesting split points is fine (in the human-required table). Actually splitting the task into multiple files is not — that's `/scaffold-bulk-seed-tasks` territory.
