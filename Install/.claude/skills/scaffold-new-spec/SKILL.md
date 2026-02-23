---
name: scaffold-new-spec
description: Create an atomic behavior spec for a slice. Reads system designs and ADRs to define testable behavior. Use after slices are defined.
argument-hint: [spec-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# New Behavior Spec

Create a new behavior spec for: **$ARGUMENTS**

## Steps

### 1. Read Context

1. **Read the spec template** at `scaffold/templates/spec-template.md`.
2. **Read the specs index** at `scaffold/specs/_index.md` to find the next available SPEC-### ID.
3. **Read the slices index** at `scaffold/slices/_index.md` to identify which slice this spec serves.
4. **Read the parent slice document** to understand the context this spec operates within.
5. **Read the system design(s)** this spec is derived from (`scaffold/design/systems/SYS-###-*.md`).
6. **Read state transitions** at `scaffold/design/state-transitions.md` for relevant state machines.
7. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`. ADRs may have changed system behavior that affects this spec.
8. **Read playtest feedback** at `scaffold/decisions/playtest-feedback.md` — filter for entries matching this spec's system. Playtest patterns may inform behavior requirements.

### 2. ADR Impact Check

Check if any ADRs affect this spec's domain:

- Did an ADR change a system's behavior or interface?
- Did an ADR add constraints or remove features?
- Did an ADR from a previous task change how this behavior should work?

If ADRs apply, present them to the user before defining the spec. Summarize the relevant ADR decisions and explain how they influence this spec.

Also check playtest feedback for this system: Are there Pattern-status entries or high-severity observations that should inform this spec's behavior, edge cases, or acceptance criteria? Present relevant playtest feedback alongside ADR impacts.

### 3. Assign to System and Slice

1. Ask which system this spec belongs to (or infer from the argument/context).
2. Ask which slice this spec is part of (or infer from context).

If both can be confidently inferred from the argument and the documents read in step 1, present the inferred assignment for user confirmation instead of asking open-ended questions.

### 4. Define the Spec

Walk the user through the spec template, pre-filling from the system design where possible. Ask one section at a time and write answers into the spec doc immediately after each confirmation.

1. **Summary** — Ask: *"In one sentence, what behavior does this spec define?"*
2. **Preconditions** — Ask: *"What must be true before this behavior can occur?"* Pre-fill from system design's Player Actions prerequisites if available.
3. **Behavior** — Ask: *"Step by step, what happens? Be precise — each step should be testable."* Pre-fill from system design's Player Actions and System Resolution.
4. **Postconditions** — Ask: *"What must be true after this behavior completes?"*
5. **Edge Cases** — Ask: *"What unusual inputs or boundary conditions exist?"* Pre-fill from system design's Edge Cases section.
6. **Acceptance Criteria** — Ask: *"How do you verify this is correctly implemented? What tests would you run?"*

Pre-filled content is a starting point. Always present pre-filled content for user confirmation — never treat it as final.

### 5. Create the Spec File

Create `scaffold/specs/SPEC-###-<name>.md` where `<name>` is a lowercase-kebab-case version of the spec name.

- Replace `SPEC-###` in the title with the actual ID.
- Replace any placeholder names with the provided spec name.
- Populate all sections with the user's confirmed answers.

### 6. Register

1. Add a row to `scaffold/specs/_index.md` with the system reference and slice reference.
2. Add the spec to the parent slice's Specs Included table.

### 7. Report

Show the user:

- The file path and assigned ID
- ADRs that influenced the spec (if any)
- Suggest creating tasks for this spec with `/scaffold-new-task`

## Rules

- **Ask one section at a time.** Do not dump all questions at once.
- **Write answers into the spec doc immediately** after each section is confirmed.
- **ADR check is mandatory** — never skip it, even if no ADRs exist yet (report that none were found).
- **Pre-fill from system designs where possible**, but always present pre-filled content for user confirmation.
- **Specs describe BEHAVIOR, not IMPLEMENTATION.** No code, no engine constructs, no class names, no signals, no methods, no nodes.
- **Each spec should be atomic** — one testable behavior. If the scope is too large, suggest splitting into multiple specs.
- **If no argument is provided**, ask the user for a spec name before proceeding.
- **IDs are sequential and permanent** — never skip or reuse.
- **Never overwrite an existing spec file.**
- **Keep index tables in sync** — `scaffold/specs/_index.md` and the parent slice document must always match.
- **Created documents start with Status: Draft.**
