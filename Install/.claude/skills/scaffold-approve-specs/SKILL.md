---
name: scaffold-approve-specs
description: Mark all Draft specs in a slice as Approved after the spec stabilization loop confirms the spec set is clean. Renames files, updates indexes, and syncs the slice table.
argument-hint: SLICE-###
allowed-tools: Read, Edit, Grep, Glob, Bash
---

# Approve Specs

Approve all review-ready specs in: **$ARGUMENTS**

This skill is the gate between spec planning and task seeding. It marks Draft specs as Approved, renames files to match the status convention, and updates all indexes. Run this only after the spec stabilization loop produces no new issues and `/scaffold-validate --scope specs` passes.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `SLICE-###` | Yes | — | The slice whose specs should be approved. |

## Preconditions

Before approving, verify all three conditions. If any fails, stop and report.

### 1. Spec graph validation passes

Run `/scaffold-validate --scope specs`. Approval cannot proceed if validation fails. Validate covers structural integrity (index sync, file existence, system resolution, status sync, slice membership).

Additionally, check content readiness: no `<!-- TODO -->` markers in Summary, Proof Intent, Trigger, Preconditions, Behavior, Observable Outcome, Failure Outcome, Postconditions, Edge Cases, Secondary Effects, Acceptance Criteria, or Out of Scope sections. This is a content-quality check that validate does not cover.

If validation fails, stop and suggest running `/scaffold-fix-spec` or `/scaffold-triage-specs` first.

### 2. No pending upstream actions that affect spec behavior

Read `scaffold/decisions/triage-logs/TRIAGE-SPECS-SLICE-###.md` if it exists. If any upstream action with status **Pending** affects behavior-defining architecture, **stop**. This includes actions that change:
- System ownership (which system owns a behavior)
- Authority rules (cross-system data writes)
- State transitions (state-machine meaning)
- Interfaces/contracts (cross-system behavioral contracts)
- Persistence assumptions (what gets saved/loaded)
- ADR outcomes that alter spec behavior semantics

Report the affected specs and require the user to resolve the upstream action or explicitly confirm approval against current architecture. The user must explicitly state approval — do not infer override intent from vague confirmation. Ask specifically: "Approve these N specs against current architecture despite pending upstream action #X?"

Upstream actions that don't affect behavior semantics (e.g., documentation clarifications, glossary additions) do not block approval.

### 3. Slice membership is consistent

Read the slice's Specs table. Verify:
- Every listed SPEC-### has an existing file.
- Every spec assigned to this slice in `scaffold/specs/_index.md` appears in the slice's Specs table.

If a file is missing or an assigned spec is not in the table, report the inconsistency and stop — suggest rerunning `/scaffold-triage-specs` to resync. (This should already be caught by `/scaffold-validate --scope specs`, but checking here provides a safety net.)

## Step 1 — Identify Specs to Approve

1. Read the slice's Specs table.
2. For each spec in the table, read the actual spec file. If a file doesn't exist, report the inconsistency and stop.
3. Categorize:

| Category | Condition | Action |
|----------|-----------|--------|
| **To approve** | Status is `Draft`, no blocker notes, all required sections filled | Approve in Step 2 |
| **Blocked** | Notes contain `> **Blocked by:**` | Skip — stays Draft, report separately |
| **Deferred** | Triage log has a Defer decision matching this spec's ID | Skip — stays Draft, report separately |
| **Already approved** | Status is `Approved` | Skip |
| **Already complete** | Status is `Complete` | Skip — verify slice table also shows Complete |

Specs with unresolved blockers remain Draft. Other specs may still be approved — blocked specs do not prevent approval of the rest of the slice's specs.

## Step 2 — Approve Each Spec

For each spec to approve:

1. Update the spec file's `> **Status:**` line from `Draft` to `Approved`.
2. Rename the file: `SPEC-###-name_draft.md` → `SPEC-###-name_approved.md` using `git mv`.
3. Update `scaffold/specs/_index.md` — change the filename reference to the new name.
4. Update the slice's Specs table — set the Status column to `Approved`.

Note: The slice's Specs table stores status, not filenames. Filename references live only in `scaffold/specs/_index.md`.

## Step 3 — Report

```
## Approval Complete: SLICE-### — [Name]

### Most Dangerous Blocking Issue
[If any specs were blocked or deferred, state the single issue most likely to cause downstream problems. If none, write "No blocking issues."]

| Metric | Value |
|--------|-------|
| Specs approved | N |
| Already approved | N (skipped) |
| Already complete | N (skipped) |
| Blocked/deferred | N (skipped — stays Draft) |
| Total in slice | N |

### Approved Specs
| ID | Name | System |
|----|------|--------|
| SPEC-### | [Name] | SYS-### |
| ... | ... | ... |

### Blocked/Deferred Specs
[List specs that were skipped with reason. If none, write "None."]

### Next Steps
- Run `/scaffold-bulk-seed-tasks SLICE-###` to generate implementation tasks from the approved specs
- If blocked specs need resolving, address their blockers then re-run `/scaffold-approve-specs`
```

## Rules

- **Only approve Draft specs.** Never re-approve Approved or Complete specs.
- **Validation is a prerequisite.** `/scaffold-validate --scope specs` must pass before approval. Structural integrity is validate's job — approval only adds the TODO content-readiness check on top.
- **Blocked specs stay Draft but don't block others.** Specs with blocker notes remain Draft. Other eligible specs in the slice may still be approved.
- **Incomplete specs stay Draft.** Specs with TODO placeholders in required sections are not approved.
- **Complete specs must be consistent.** If a spec has status Complete in the file, verify the slice table also shows Complete. Flag mismatches.
- **File renames use git mv.** Always use `git mv` so git tracks the rename.
- **Index updates are mandatory.** `scaffold/specs/_index.md` stores filename references. The slice's Specs table stores status. Both must be updated.
- **Architecture-impacting upstream actions are a hard stop.** If a pending upstream action would change ownership, authority, state transitions, interfaces, persistence, or behavior semantics that specs depend on, stop and require resolution or explicit override.

**Why approval is a separate skill:** The stabilization loop (fix → iterate → triage) is about getting spec content right. Approval is a lifecycle transition that signals "these specs are ready for task generation." Keeping them separate means the loop can run multiple times without side effects.
