---
name: scaffold-bulk-seed-tasks
description: Read specs, engine docs, and the signal registry to bulk-create implementation task stubs with engine-specific steps. Use after specs are defined.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Tasks from Specs

Read all specs, engine docs, and the signal registry to bulk-create implementation task stubs.

## Prerequisites

1. **Read `scaffold/specs/_index.md`** to get the list of registered specs.
2. **Read every spec file** in `scaffold/specs/` (Glob `scaffold/specs/SPEC-*.md`).
3. **Read the slices index** at `scaffold/slices/_index.md` and all slice files — tasks are ordered within slices.
4. **Read all engine docs** from `scaffold/engine/`:
   - `scaffold/engine/coding-best-practices.md` — naming, patterns, structure
   - `scaffold/engine/scene-architecture.md` — scene organization, node hierarchy
   - `scaffold/engine/ui.md` — UI patterns (if specs involve UI)
   - `scaffold/engine/input.md` — input handling (if specs involve input)
   - `scaffold/engine/performance.md` — performance patterns (if specs involve heavy systems)
5. **Read the signal registry** at `scaffold/reference/signal-registry.md`.
6. **Read entity components** at `scaffold/reference/entity-components.md`.
7. **Read the task template** at `scaffold/templates/task-template.md`.
8. **Read the tasks index** at `scaffold/tasks/_index.md` to find the next available ID and avoid duplicates.
9. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md` — ADRs may have changed implementation patterns.
10. **If fewer than 1 spec is defined**, stop and tell the user to create specs first.
11. **If no engine docs are filled out**, warn the user that task steps will lack engine-specific guidance. Suggest running `/scaffold-bulk-seed-engine` first.

## Phase 1 — Translate Specs to Tasks

For each spec, translate its behavior into implementation:

1. **Map behavior steps to implementation steps.** Each spec Behavior step becomes one or more implementation steps using engine patterns:
   - Reference coding conventions from engine docs for naming and structure
   - Reference scene architecture for file organization
   - Reference signal registry for cross-system communication
   - Reference entity components for data structures
2. **Determine files affected.** Based on engine scene architecture and the systems involved:
   - New files to create (scenes, scripts, resources)
   - Existing files to modify
3. **Draft verification steps.** Translate spec Acceptance Criteria into concrete engine-specific tests or checks.
4. **Determine task granularity.** If a spec requires more than ~8 implementation steps or ~5 files, split into multiple tasks with clear boundaries.
5. **For each task**, draft:
   - **Objective** — what this task produces (one sentence)
   - **Steps** — numbered implementation steps with engine patterns
   - **Files Affected** — specific file paths based on engine conventions
   - **Verification** — concrete checks derived from acceptance criteria
   - **Notes** — engine quirks, gotchas, references to engine docs

## Phase 2 — Determine Ordering

Within each slice, order tasks based on dependencies:

1. Tasks that create foundational files (data structures, base classes) come first.
2. Tasks that implement core logic come next.
3. Tasks that wire up signals and interfaces come after core logic.
4. Tasks that implement UI or feedback come last.

Flag any circular dependencies between tasks.

## Phase 3 — ADR Impact Check

For each task candidate, check all ADRs:
- Did an ADR change the implementation approach for this system?
- Did an ADR add engine constraints or change patterns?

If ADRs affect a task, annotate the draft with the ADR reference and adjust the implementation steps.

## Phase 4 — Present for Confirmation

Present all candidate tasks to the user, organized by slice with ordering:

```
### Slice: SLICE-### — [Name]

Task 1 (order 1): TASK-### — [name]
- Spec: SPEC-###
- Objective: [one sentence]
- Steps: [numbered list]
- Files: [file list]
- ADR impacts: [if any]

Task 2 (order 2): TASK-### — [name]
...
```

Ask the user to confirm, modify, reorder, merge, split, or remove tasks. Flag:
- Specs with no implementing tasks
- Tasks that seem too large (suggest splitting)
- Potential file conflicts between tasks

## Phase 5 — Create Task Files

For each confirmed task:

1. **Assign the next sequential TASK-### ID** from `scaffold/tasks/_index.md`.
2. **Create** `scaffold/tasks/TASK-###-<name>.md` using the task template:
   - Fill in Objective, Steps, Files Affected, Verification, and Notes from the confirmed drafts.
   - Set the Implements reference to the parent spec ID.
   - Set the Phase reference from the slice's parent phase.
3. **Register** the task in `scaffold/tasks/_index.md` with the spec reference.
4. **Update** the parent slice's Tasks table with the new task ID, description, and order number.

## Phase 6 — Report

Summarize what was seeded:
- Tasks created: X total, across Y slices
- Per slice: task count and implementation order
- Per spec: how many tasks implement each spec
- Engine patterns used: [list of engine doc patterns referenced]

Flag any gaps:
- Specs with no implementing tasks
- Signals referenced in tasks but not in signal registry
- Entity fields referenced but not in entity-components
- Engine doc sections that should exist but are empty (limiting task quality)
- ADRs that affect tasks (annotated in the task files)

Remind the user of next steps:
- Review each task and refine steps, file lists, and verification
- Run `/scaffold-bulk-review-tasks` to audit all tasks for cross-task consistency
- Run `/scaffold-review-task` on individual tasks for detailed review
- Begin implementation by working through tasks in slice order
- File ADRs when implementation conflicts with the plan

## Rules

- **Never write without confirmation.** Present all proposed tasks before creating files.
- **Tasks describe IMPLEMENTATION, not BEHAVIOR.** This is where engine constructs, class names, signals, file paths, and method names belong. Translate spec behavior into engine-specific implementation.
- **Engine docs are the pattern source.** Every implementation step should follow patterns from engine docs. If engine docs are empty, note which sections would improve task quality.
- **Pre-filled content is a starting point.** Always present for user confirmation.
- **Preserve existing tasks.** If tasks already exist, add to them — don't overwrite or duplicate.
- **IDs are sequential and permanent** — never skip or reuse.
- **Each task should be right-sized** — completable in one session (~3-8 steps, ~1-5 files). Split larger tasks.
- **Flag conflicts, don't resolve them.** If file ownership is unclear or tasks would conflict, present the conflict to the user.
- **Ordering matters.** Tasks within a slice must be ordered so each task can build on the previous ones.
