---
name: scaffold-new-slice
description: Define a vertical slice within a phase — an end-to-end playable chunk that proves something works. Use after phases are defined.
argument-hint: [slice-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# New Vertical Slice

Create a new vertical slice for: **$ARGUMENTS**

## Steps

### 1. Read Context

1. **Read the slice template** at `scaffold/templates/slice-template.md`.
2. **Read the slices index** at `scaffold/slices/_index.md` to find the next available SLICE-### ID.
3. **Read phase context** — read `scaffold/phases/_index.md` and `scaffold/phases/roadmap.md` to identify available phases.
4. **Read the systems index** at `scaffold/design/systems/_index.md` to see available systems.
5. **Read the interfaces doc** at `scaffold/design/interfaces.md` to understand system-to-system communication.
6. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md` and read each one. ADRs may affect slice scope.

### 2. Assign to Phase

Ask which phase this slice belongs to. If only one phase exists, assign automatically. Show the phase's scope to confirm the slice fits.

If no phases exist, stop and tell the user to run `/scaffold-new-phase` first. A slice must belong to a phase.

### 3. Define the Slice

Walk the user through the slice template, one section at a time. Write answers into the slice doc immediately after each response.

1. **Goal** — Ask: *"In one sentence, what end-to-end experience does this slice deliver? What does it prove?"*
2. **Specs Included** — Ask: *"What behaviors need to work for this slice? We'll create specs for these next."* List candidate specs based on the systems in scope. The user confirms or adjusts.
3. **Integration Points** — Ask: *"Which systems connect in this slice? What interfaces are exercised?"* Cross-reference with `design/interfaces.md`.
4. **Done Criteria** — Ask: *"What must be true for this slice to be considered complete? What can you demonstrate?"*
5. **Demo Script** — Ask: *"Walk me through the step-by-step demo. What does the tester do, and what should they see?"*

Leave the Tasks table empty — tasks are created after specs.

### 4. Create the Slice File

Create `scaffold/slices/SLICE-###-<name>.md` using the template with the user's answers. Replace `<name>` with a lowercase-kebab-case version of the slice name.

### 5. Register

Add a row to `scaffold/slices/_index.md` with the phase reference.

### 6. Report

Show the user:
- The file path and assigned ID
- The specs that need to be created for this slice
- Suggest running `/scaffold-new-spec` to create each spec

## Rules

- **Ask one section at a time.** Do not dump all questions at once.
- **Write answers into the slice doc immediately** after the user responds.
- **A slice must belong to a phase.** If no phases exist, tell the user to run `/scaffold-new-phase` first.
- **Slices should be vertical (end-to-end across systems), not horizontal (one system in isolation).** If the user describes a slice that only touches one system, flag it and suggest broadening or reframing.
- **The demo script should be concrete enough** for someone unfamiliar with the project to follow.
- **If no argument is provided**, ask the user for a slice name before proceeding.
- **IDs are sequential and permanent** — never skip or reuse.
- **Created documents start with Status: Draft.**
