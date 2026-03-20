---
name: scaffold-bulk-seed-tasks
description: Seed implementation task stubs for a specific slice. Reads the slice's specs, relevant architecture/engine/reference docs, and existing tasks to generate scoped candidates. Use after specs are defined.
argument-hint: SLICE-###
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Tasks for Slice

Generate implementation task stubs for a single slice: **$ARGUMENTS**

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `SLICE-###` | Yes | — | The slice to seed tasks for. All generated tasks are scoped to this slice's specs. |

## Step 1 — Read Target Slice and Specs

Read the slice and its included specs — these are the source of truth for what tasks must exist.

1. **Resolve the slice file** — Glob `scaffold/slices/SLICE-###-*.md`. If not found, report the error and stop.
2. **Read the slice** — extract the Specs Included table, Phase reference, and `> **Depends on:**` field. If the slice declares dependencies, read the dependency slices' tasks to understand what code and infrastructure already exists — task generation should build on that foundation rather than re-implement it.
3. **Read each spec** listed in the slice's Specs Included table. For each spec, extract:
   - Summary, Preconditions, Behavior steps, Postconditions, Edge Cases, Acceptance Criteria
   - The parent system reference
   - **Asset Requirements** — if the spec has an Asset Requirements table, extract it. Tasks that implement visual or audio behavior should reference the specific asset paths from the spec's Satisfied By column (for Ready assets) or note that production is pending (for Needed/In Production assets). This tells the task exactly what files to wire.
4. **If the slice has zero specs**, stop and tell the user to create specs first.

Do NOT read specs outside this slice. Task generation is scoped to the target slice only.

## Step 2 — Read Supporting Context

Read documents that shape how tasks are written — architecture, engine patterns, reference data, and existing constraints.

| Document | Why | Need |
|----------|-----|------|
| `scaffold/design/design-doc.md` | Core vision context for implementation decisions | Hard required |
| `scaffold/design/authority.md` | Data ownership boundaries for each implementation step | Hard required |
| `scaffold/design/interfaces.md` | Cross-system contracts each step must respect | Hard required |
| `scaffold/design/architecture.md` | Tick order, signal wiring, data flow rules, code patterns, component checklists | Hard required |
| `scaffold/reference/enums-and-statuses.md` | Shared state vocabulary for state handling in implementation | Hard required |
| `scaffold/doc-authority.md` | Document authority ranking and influence map | Hard required |
| `scaffold/templates/task-template.md` | Template structure for generated task files | Hard required |
| `scaffold/tasks/_index.md` | Next available TASK-### ID, existing tasks to avoid duplication | Hard required |
| System design docs for each spec's parent system (Glob `scaffold/design/systems/SYS-*{system}*.md`) | System-level behavior context | Hard required — for each unique system |
| `scaffold/engine/godot4-coding-best-practices.md` | Naming, patterns, structure | Strongly recommended |
| `scaffold/engine/godot4-scene-architecture.md` | Scene organization, node hierarchy | Strongly recommended |
| `scaffold/decisions/design-debt.md` | Intentional compromises — tasks must not "fix" these; annotate tasks that touch DD areas | Strongly recommended |
| `scaffold/decisions/known-issues.md` | Unresolved gaps and blockers — flag tasks that touch KI areas, especially KIs that block this slice | Strongly recommended |
| `scaffold/reference/signal-registry.md` | Signal names, payloads, emitters | Conditional — if any spec involves signals |
| `scaffold/reference/entity-components.md` | Entity data structures | Conditional — if any spec creates/modifies entities |
| `scaffold/engine/ui.md` | UI patterns | Conditional — if any spec involves UI |
| `scaffold/engine/input.md` | Input handling | Conditional — if any spec involves input |
| ADRs affecting this slice's systems — Grep `scaffold/decisions/ADR-*.md` for system IDs | Implementation constraints from prior decisions | Conditional — if any exist |

If a hard-required document is missing, stop and report the error — task generation cannot produce useful results without it. Skip missing conditional/recommended documents silently, but warn that task steps will lack that context.

## Step 3 — Detect Existing Coverage

Before generating candidates, check what tasks already exist for this slice's specs.

1. **Grep `scaffold/tasks/TASK-*.md` for each spec ID** (e.g., `Implements: SPEC-###`).
2. **Read each existing task's Objective and Files Affected** to understand what it covers.
3. **Read the spec's Behavior steps and Acceptance Criteria** to identify the full implementation surface.
4. For each spec, categorize coverage by comparing existing tasks against the spec:
   - **Fully covered** — existing tasks collectively map to all major behavior clusters (groups of related Behavior steps) and all Acceptance Criteria in the spec. Skip this spec.
   - **Partially covered** — some behavior clusters or acceptance criteria have corresponding tasks, but others do not. Generate tasks for uncovered behavior only.
   - **Uncovered** — no existing task's Objective meaningfully maps to the spec's implementation surface. Generate full task set.
5. Record the next available TASK-### ID from the tasks index.

## Step 4 — Generate Task Candidates

For each uncovered or partially covered spec, translate behavior into implementation:

### 4a. Map Behavior to Implementation Steps

Each spec Behavior step becomes one or more implementation steps:
- Reference architecture.md for tick order placement, signal wiring conventions, data flow rules, and code pattern templates
- Reference engine docs for naming conventions, file organization, and patterns
- Reference signal registry for cross-system communication
- Reference entity components for data structures

### 4b. Determine Files Affected

Based on architecture and engine conventions:
- New files to create (`.h`, `.cpp`, `.gd`, scenes, resources)
- Existing files to modify (orchestrator, registration, wiring, test harness)

### 4c. Draft Verification

Translate spec Acceptance Criteria into concrete engine-specific checks.

### 4d. Check Task Granularity

If a spec requires more than ~8 implementation steps or ~5 files, split into multiple tasks with clear boundaries. Each task should be completable in one `/scaffold-implement-task` session.

### 4e. Constraint Check — ADRs, Design Debt, Known Issues

For each task candidate, check all three constraint sources:

**ADRs:**
- Did an ADR change the implementation approach for this system?
- Did an ADR add engine constraints or patterns?
- If so, annotate the draft with the ADR reference and adjust the steps.

**Design Debt (DD-###):**
- Does this task touch an area with active design debt?
- If so, annotate the task's Notes section with the DD-### reference so the implementer knows the compromise exists and does not try to "fix" it.
- If the task would directly conflict with a DD entry (e.g., implementing something the DD explicitly defers), flag it for the user.

**Known Issues (KI-###):**
- Does this task touch an area with an open known issue?
- If a KI is marked as **blocking** this slice (check KI's Blocking column), flag it prominently — the task may not be implementable until the KI is resolved.
- If a KI describes instability in an area the task touches (e.g., KI-009 medical pipeline, KI-011 array limits), annotate the task's Notes section so the implementer is aware.

### 4f. Draft Each Task

For each task candidate, draft:
- **Objective** — what this task produces (one sentence)
- **Deliverable** — what should concretely exist when done (more specific than Objective)
- **Depends on** — TASK-### IDs this task requires, or "—". Derived from step ordering and file dependencies.
- **Task Type** — foundation / behavior / integration / UI / verification / wiring
- **Steps** — numbered implementation steps with engine-specific constructs
- **Files Created** — new files this task introduces
- **Files Modified** — existing files this task changes
- **Verification** — concrete checks derived from acceptance criteria
- **Verification Mapping** — maps parent spec ACs to verification steps (e.g., "AC-1 → Verification step 3")
- **Out of Scope** — what this task intentionally does not implement
- **Risks** — task-local execution risks (central tick flow, signal ordering, stale handles, etc.)
- **Notes** — engine quirks, ADR references, DD references, KI warnings, gotchas

## Step 5 — Order Tasks

Order task candidates within the slice based on dependencies:

1. Tasks that create foundational files (data structures, base classes, CSVs) come first.
2. Tasks that implement core logic come next.
3. Tasks that wire up signals and interfaces come after core logic.
4. Tasks that implement UI or feedback come last.

Flag any circular dependencies between tasks.

## Step 6 — Present for Confirmation

Present all candidate tasks grouped by spec within the slice:

```
## Task Candidates for SLICE-### — [Name]

### SPEC-### — [Name] [coverage: uncovered / partially covered]

Task (order N): TASK-### — [name]
- Objective: [one sentence]
- Steps: [count] steps
- Files: [file list]
- Constraints: [ADR-###, DD-###, KI-### references or "none"]
- Size: [OK / large — suggest split]

Task (order N+1): TASK-### — [name]
...

### SPEC-### — [Name] [coverage: fully covered — skipped]

---

### Flags
- Specs with no implementing tasks: [list or "none"]
- Tasks that seem too large: [list with split suggestions]
- File conflicts between tasks: [list or "none"]
- Overlap with existing tasks: [list or "none"]
- Design debt in scope: [DD-### entries touching this slice's systems — tasks must work around these]
- Known issue blockers: [KI-### entries that block this slice — must be resolved before affected tasks]
- Known issue warnings: [KI-### entries in affected areas — tasks annotated but not blocked]
```

Present decisions using the Human Decision Presentation pattern (see WORKFLOW.md). Each overlap, size issue, and candidate gets numbered options. Wait for the user's decisions on each issue before proceeding.

## Step 7 — Create Task Files

For each confirmed task:

1. **Assign the next sequential TASK-### ID** from `scaffold/tasks/_index.md`.
2. **Create** `scaffold/tasks/TASK-###-<name>_draft.md` using the task template:
   - Fill in Objective, Steps, Files Affected, Verification, and Notes from the confirmed drafts.
   - Set the `Implements` reference to the parent spec ID.
   - Set the `Phase` reference from the slice's parent phase.
3. **Register** the task in `scaffold/tasks/_index.md` with the spec reference.
4. **Update** the parent slice's Tasks table with the new task ID, description, and order number. If the Tasks table is missing or malformed in the slice file, stop and report the error — do not attempt to guess the table format or insert into the wrong location.

## Step 8 — Report

```
## Tasks Seeded for SLICE-### — [Name]

| Spec | Coverage | Tasks Created | Existing Tasks |
|------|----------|---------------|----------------|
| SPEC-### — Name | Full | N new | M existing |
| SPEC-### — Name | Partial | N new | M existing |
| SPEC-### — Name | Skipped | 0 | M existing (fully covered) |

**Total:** N new tasks created (IDs TASK-### through TASK-###)
**Implementation order:** [ordered list]
**Constraints:** [N ADR impacts, N DD annotations, N KI warnings, N KI blockers — or "none"]

### Next Steps
- Run `/scaffold-review-task TASK-###-TASK-###` to audit all new tasks
- Run `/scaffold-bulk-review-tasks` for cross-task consistency
- Begin implementation with `/scaffold-implement-task TASK-###` (first in order)
```

## Rules

- **Slice-scoped only.** This skill generates tasks for one slice at a time. To seed multiple slices, invoke once per slice.
- **Never write without confirmation.** Present all proposed tasks before creating files.
- **Tasks describe IMPLEMENTATION, not BEHAVIOR.** Engine constructs, class names, signals, file paths, and method names belong here. Translate spec behavior into engine-specific implementation.
- **Specs are the source of truth.** The slice's included specs define what tasks must exist. Don't generate tasks for specs outside the target slice.
- **Detect existing coverage first.** Before generating, check what tasks already exist. Never duplicate an existing task's objective or file set. If overlap is ambiguous, flag it for the user instead of guessing.
- **Architecture and engine docs shape the how.** These inform implementation steps but don't define what tasks exist — that comes from specs.
- **ADRs modify approach.** Check ADRs for constraints on each task's system. Annotate affected tasks with ADR references.
- **Design debt is not a task target.** If a DD entry covers something a task would touch, annotate the task to work around it — don't generate tasks that "fix" design debt unless the user explicitly asks.
- **Known issue blockers stop task generation.** If a KI is marked as blocking this slice, flag it prominently. Tasks affected by KI blockers may not be implementable until the KI is resolved.
- **Each task should be right-sized** — completable in one session (~3-8 steps, ~1-5 files). Split larger tasks.
- **Flag conflicts, don't resolve them.** If file ownership is unclear or tasks would conflict, present the conflict to the user.
- **Ordering matters.** Tasks within the slice must be ordered so each task can build on previous ones.
- **IDs are sequential and permanent** — never skip or reuse.
- **Created documents start with Status: Draft.**
