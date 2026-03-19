---
name: scaffold-fix-spec
description: Review-fix loop for specs — auto-fix mechanical issues (vague ACs, missing sections, terminology drift, system misalignment), surface strategic issues for human decision. Supports single spec or range.
argument-hint: SPEC-### or SPEC-###-SPEC-###
allowed-tools: Read, Edit, Grep, Glob
---

# Fix Spec

Iteratively review and auto-fix mechanical issues in: **$ARGUMENTS**

This skill is the mechanical cleanup pass for specs. It finds issues that have clear, safe fixes and applies them automatically. Issues that require human judgment are collected and reported for triage.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `SPEC-###` or `SPEC-###-SPEC-###` | Yes | — | Single spec or range. Range processes all specs with IDs in the numeric range. |
| `--iterate N` | No | `10` | Maximum review-fix passes before stopping. Stops early on convergence — if a pass produces no new issues, iteration ends. |

## Step 1 — Gather Context

**Parallelization:** Specs within a slice are independent — range processing can run all items in parallel. See WORKFLOW.md Range Parallelization.

For each spec:
1. Locate the spec file: glob `scaffold/specs/SPEC-###-*.md`.
2. Read the spec file.
3. Read `scaffold/doc-authority.md` — document authority ranking, same-rank conflict resolution rules, influence map.
4. Read `scaffold/design/design-doc.md` — design invariants and core vision context for spec validation.
5. Read the parent system design: extract system reference from spec, read `scaffold/design/systems/SYS-###-*.md`.
6. Read the parent slice: grep `scaffold/slices/SLICE-*.md` for this spec ID.
7. Read `scaffold/design/state-transitions.md` for relevant state machines.
8. Read `scaffold/design/glossary.md` for canonical terminology.
9. Read all ADRs with status `Accepted` that reference this spec's system or ID.
10. Read `scaffold/design/interfaces.md` and `scaffold/design/authority.md` for cross-system contracts.
11. Read `scaffold/decisions/known-issues.md` — known issues may represent constraints or edge cases the spec should address.

## Step 2 — Review

Run the full review checklist from `/scaffold-review-spec` — completeness, quality (behavior language, determinism, actor/trigger/sequence clarity, observability, failure paths, internal consistency, atomicity, terminology), slice alignment, system alignment, state machine alignment, ADR impact, known issue impact, and registration. Do not duplicate the checklist here — refer to the review-spec skill for the authoritative checks.

Record all issues found.

## Step 3 — Classify Issues

For each issue found, classify as:

### Auto-Fixable (apply immediately)
- **Missing sections** — add empty section with `<!-- TODO: fill in -->` placeholder. Required sections: Summary, Proof Intent, Trigger, Preconditions, Behavior, Observable Outcome, Failure Outcome, Postconditions, Edge Cases, Secondary Effects, Acceptance Criteria, Out of Scope, Notes.
- **Missing Secondary Systems header** — add `> **Secondary Systems:** —` to the header block if absent.
- **Vague ACs** — tighten wording to be testable (e.g., "works correctly" → specific observable outcome from the Observable Outcome or Behavior section).
- **Implementation leaks** — replace engine constructs with behavior language (e.g., "emit signal" → "notify the system", "node" → "entity").
- **Terminology drift** — replace NOT-column terms with canonical terms.
- **Missing ADR reflection** — add edge case or AC noting the ADR's impact.
- **Registration gaps** — add to `_index.md` or slice table.
- **Vague preconditions/postconditions** — tighten to verifiable conditions using context from system design.
- **Vague Observable/Failure Outcome** — tighten to concrete player-visible or test-observable results.
- **Empty Out of Scope** — add at least one explicit exclusion based on spec boundary and related specs.

### Human-Required (collect for triage)

Present using the Human Decision Presentation pattern (see WORKFLOW.md) — grouped by category, numbered, with concrete options (a/b/c) per issue.

- **System scope mismatch** — spec describes behavior outside its system's defined scope.
- **Authority violation** — spec implies cross-system data writes not defined in authority.md.
- **State machine conflict** — spec's transitions don't match state-transitions.md and it's unclear which is right.
- **Spec overlap** — two specs define the same behavior (detected during range processing).
- **Missing coverage** — slice goals suggest behavior that no spec covers.
- **Contradictory ACs** — acceptance criteria within the spec conflict with each other.
- **Cross-spec dependency** — spec assumes behavior from another spec that doesn't define it.

## Step 4 — Apply Auto-Fixes

For each auto-fixable issue:
1. Apply the fix to the spec file using Edit.
2. Record what was changed and why.

**Safety rules:**
- Never change the meaning of behavior — only tighten wording, add missing structure, or fix terminology.
- Never add new behavior. Only clarify or restructure what's already there.
- Never modify ACs in a way that changes what they test — only make them more precise.
- Never edit other files besides the spec and its index/slice registrations.

## Step 5 — Re-review and Iterate

After applying fixes, re-review the spec. Continue iterating until one of:
- **Clean** — no issues remain.
- **Human-only** — only human-required issues remain.
- **Stable** — same issues persist across two consecutive passes (fixes aren't helping).
- **Iteration limit** — `--iterate N` reached.

## Step 6 — Report

For a single spec:
```
## Fix-Spec Summary: SPEC-### — [Name]

| Metric | Value |
|--------|-------|
| Passes | N |
| Auto-fixed | N issues |
| Human-required | N issues |
| Final status | Clean / Human-only / Stable / Limit |

### Auto-Fixes Applied
| # | Category | What Changed |
|---|----------|-------------|
| 1 | Terminology | Replaced "creature" with "colonist" |
| 2 | Vague AC | AC-3 tightened from "works" to "HP decreases by damage amount" |
| ... | ... | ... |

### Human-Required Issues
| # | Category | Description | Suggested Resolution |
|---|----------|-------------|---------------------|
| 1 | System scope | Spec describes UI behavior but parent system is HealthSystem | Move to UISystem spec or split |
| 2 | Authority | Spec implies NeedSystem writes temperature data | Clarify in authority.md or redesign |
| ... | ... | ... | ... |
```

For a range, add a summary table:
```
### Range Summary
| Spec | Auto-fixed | Human-required | Status |
|------|-----------|----------------|--------|
| SPEC-### | 3 | 1 | Human-only |
| SPEC-### | 0 | 0 | Clean |
| ... | ... | ... | ... |
```

## Rules

- **Never change behavior meaning.** Auto-fixes tighten wording and fix structure. They never alter what the spec defines.
- **Specs describe BEHAVIOR, not IMPLEMENTATION.** If a fix would introduce engine constructs, it's wrong. Go the other direction — replace implementation language with behavior language.
- **Human-required issues go to triage.** Do not attempt to resolve system scope, authority, or state machine conflicts automatically.
- **Registration fixes are safe.** Adding a spec to an index or slice table is always auto-fixable.
- **Range processing detects cross-spec issues.** Overlap and dependency issues only surface when reviewing multiple specs together.
