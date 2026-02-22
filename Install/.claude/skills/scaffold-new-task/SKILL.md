---
name: scaffold-new-task
description: Create an implementation task tied to a spec. Reads engine docs and ADRs to define concrete steps. Use after specs are defined.
argument-hint: [task-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# scaffold-new-task

Create a new implementation task tied to a spec, consuming ADRs.

## 1. Read Context

1. Read `scaffold/templates/task-template.md`.
2. Read `scaffold/tasks/_index.md` to find the next available TASK-### ID.
3. Read `scaffold/specs/_index.md` to identify available specs.
4. Read the parent spec document to understand what behavior to implement.
5. Read the system design that the spec belongs to.
6. Read relevant engine docs from `scaffold/engine/` — especially coding best practices and any engine doc relevant to the task's domain (UI, input, scene architecture, performance).
7. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`. ADRs may have changed implementation approach.
8. Read `scaffold/design/interfaces.md` and `scaffold/reference/signal-registry.md` if the task involves system communication.

## 2. ADR Impact Check

Check if any ADRs affect this task:

- Did an ADR change the implementation approach for this system?
- Did an ADR from a prior task in the same slice change something this task depends on?
- Did an ADR add engine constraints or change patterns?

If ADRs apply, present them to the user before defining the task.

## 3. Assign to Spec and Phase

1. Ask which spec this task implements (or infer from argument/context).
2. Determine the phase from the spec's slice.

## 4. Define the Task

Walk the user through the task template:

1. **Objective** — Ask: *"In one sentence, what does this task produce?"*
2. **Steps** — Ask: *"What are the concrete implementation steps? Each step should be verifiable."* Pre-fill from the spec's Behavior section, translating behavior into implementation using engine doc patterns.
3. **Files Affected** — Ask: *"What files will be created or modified?"* Suggest based on engine scene architecture and coding conventions.
4. **Verification** — Ask: *"How do you confirm this task is done? What tests or checks?"* Pre-fill from the spec's Acceptance Criteria.
5. **Notes** — Ask: *"Any implementation gotchas, engine quirks, or references?"* Pre-fill from relevant engine docs.

## 5. Create the Task File

Create `scaffold/tasks/TASK-###-<name>.md` with the user's answers.

## 6. Register

1. Add a row to `scaffold/tasks/_index.md` with the spec reference.
2. Add the task to the parent slice's Tasks table (with order number).

## 7. Report

Show the user:

- The file path and assigned ID
- ADRs that influenced the task (if any)
- The parent spec and slice
- Remind the user: if conflicts or ambiguities arise during implementation, file an ADR with `/scaffold-update-doc`

## Rules

- Ask one section at a time.
- Write answers into the task doc immediately.
- ADR check is mandatory — never skip it.
- Tasks describe IMPLEMENTATION, not BEHAVIOR. This is where engine constructs, class names, and file paths belong.
- Steps should be concrete enough for a developer to follow without guessing.
- Reference engine docs for patterns and conventions — don't contradict them.
- If no argument is provided, ask the user for a task name.
- IDs are sequential and permanent.
- Each task should be small enough to complete in one session. If it's too big, suggest splitting into multiple tasks.
- **Created documents start with Status: Draft.**
