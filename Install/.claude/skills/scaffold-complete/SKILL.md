---
name: scaffold-complete
description: Mark a planning-layer document (task, spec, slice, or phase) as Complete. Automatically ripples upward through the planning hierarchy when all children are done.
argument-hint: [document-path or ID]
allowed-tools: Read, Edit, Grep, Glob
---

# Mark Document Complete

Mark a planning-layer document as `Complete` and ripple the status upward through the hierarchy: **$ARGUMENTS**

## Scope

This skill applies only to **planning-layer documents** — tasks, specs, slices, and phases. Design docs, style docs, reference docs, engine docs, and theory docs use `Approved` as their terminal status and are not eligible for `Complete`.

## Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `document-path` | Yes | File path or document ID (e.g., `TASK-001`, `SPEC-003`, `SLICE-002`, `P1-001`) |

## Steps

### 1. Resolve Target

Resolve the document path:
- If a path is given, verify the file exists.
- If a document ID is given, find the matching file:
  - `TASK-###` → `scaffold/tasks/TASK-###-*.md`
  - `SPEC-###` → `scaffold/specs/SPEC-###-*.md`
  - `SLICE-###` → `scaffold/slices/SLICE-###-*.md`
  - `P#-###` → `scaffold/phases/P#-###-*.md`

If the document is not a planning-layer type (task, spec, slice, or phase), report the error and stop. Only planning-layer docs can be marked Complete.

### 2. Read the Document

Read the target document. Extract:
- Its current `> **Status:**` value.
- Its type (task, spec, slice, or phase) from the path or ID prefix.
- Its parent linkage fields (see Linkage Fields below).

### 3. Check Eligibility

**For tasks:** Tasks can be marked Complete from any status (Draft, Review, or Approved). No child check needed — tasks are leaf nodes.

**For specs, slices, and phases:** Before marking Complete, verify that **all children** are already Complete:
- **Spec:** Find all tasks that implement it (grep `scaffold/tasks/TASK-*.md` for `Implements: SPEC-###`). All must have `Status: Complete`.
- **Slice:** Read the slice's "Specs Included" table. Every listed spec must have `Status: Complete`.
- **Phase:** Find all slices in this phase (grep `scaffold/slices/SLICE-*.md` for `Phase: P#-###`). All must have `Status: Complete`.

If any children are not Complete, report what's still pending and stop. Do not mark the document Complete.

### 4. Set Status to Complete

Update the document's `> **Status:**` line to `Complete` using the Edit tool.

### 5. Ripple Upward

After marking the target Complete, check whether the target's parent can now also be marked Complete. Follow the ripple chain:

**Task → Spec:**
1. Read the task's `Implements: SPEC-###` field to find the parent spec.
2. Find the parent spec file (`scaffold/specs/SPEC-###-*.md`).
3. Find all tasks that implement this spec (grep `scaffold/tasks/TASK-*.md` for `Implements: SPEC-###`).
4. If ALL tasks for this spec are now Complete, set the spec's status to Complete.
5. If the spec was marked Complete, continue rippling to its slice.

**Spec → Slice:**
1. Find which slice includes this spec. Grep `scaffold/slices/SLICE-*.md` for the spec ID (e.g., `SPEC-###`).
2. Read the slice's "Specs Included" table to get all its specs.
3. If ALL specs in the slice are now Complete, set the slice's status to Complete.
4. If the slice was marked Complete, continue rippling to its phase.

**Slice → Phase:**
1. Read the slice's `Phase: P#-###` field to find the parent phase.
2. Find all slices in this phase (grep `scaffold/slices/SLICE-*.md` for `Phase: P#-###`).
3. If ALL slices for this phase are now Complete, set the phase's status to Complete.

At each ripple level, if not all children are Complete, stop rippling. The parent stays at its current status.

### 6. Report

Present a summary to the user:

- **Marked Complete:** List every document whose status was changed to Complete (the target + any parents that rippled).
- **Ripple stopped at:** If ripple stopped before reaching the top, state which parent still has pending children and list them.
- **Already Complete:** If the target was already Complete, report that and skip all steps.

## Linkage Fields

| Doc Type | Parent Link Field | How to Find Children |
|----------|------------------|---------------------|
| Task | `Implements: SPEC-###` | (leaf node — no children) |
| Spec | (found via slice's "Specs Included" table) | Grep `scaffold/tasks/TASK-*.md` for `Implements: SPEC-###` |
| Slice | `Phase: P#-###` | Read "Specs Included" table in the slice |
| Phase | (top of hierarchy) | Grep `scaffold/slices/SLICE-*.md` for `Phase: P#-###` |

## Rules

- **Planning-layer only.** Never mark design, style, reference, engine, or theory docs as Complete. Report an error if attempted.
- **No strict prerequisite for tasks.** A task can go from Draft, Review, or Approved directly to Complete.
- **Children must be Complete first.** Specs, slices, and phases cannot be marked Complete unless all their children are already Complete.
- **Ripple is automatic.** After marking a document Complete, always check parents. Never skip the ripple check.
- **Stop rippling on failure.** If a parent has incomplete children, stop. Don't continue checking grandparents.
- **Idempotent.** If the target is already Complete, report it and do nothing.
- **Read before writing.** Always read a document's current status before attempting to change it.
