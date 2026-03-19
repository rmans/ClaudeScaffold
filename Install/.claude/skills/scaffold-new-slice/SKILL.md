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
7. **Read known issues** at `scaffold/decisions/known-issues.md` — known issues may affect slice scope or suggest behaviors the slice should validate.

### 2. Assign to Phase

Ask which phase this slice belongs to. If only one phase exists, assign automatically. Show the phase's scope to confirm the slice fits.

If no phases exist, stop and tell the user to run `/scaffold-new-phase` first. A slice must belong to a phase.

### 3. Define the Slice

Walk the user through the slice template, one section at a time. Write answers into the slice doc immediately after each response.

1. **Goal** — Ask: *"In one sentence, what end-to-end experience does this slice deliver? What does it prove?"*
1b. **Dependencies** — Ask: *"Does this slice depend on any earlier slices being Complete first? If so, which SLICE-### IDs?"* Show the list of existing slices in the same phase for reference. If the user says none, set `> **Depends on:** —`. Otherwise set `> **Depends on:** SLICE-###, SLICE-###`.
2. **Proof Value** — Ask: *"What uncertainty does this slice reduce? What important thing will you know after this slice passes that you don't know now?"*
3. **Assumptions** — Ask: *"What does this slice assume already works? What infrastructure, systems, or behaviors must exist before this slice can succeed?"*
4. **Starting Conditions** — Ask: *"What must be true before the demo begins? What state must the game be in?"*
5. **Specs Included** — Ask: *"What behaviors need to work for this slice? We'll create specs for these next."* List candidate specs based on the systems in scope. The user confirms or adjusts.
6. **Integration Points** — Ask: *"Which systems connect in this slice? What interfaces are exercised?"* Cross-reference with `design/interfaces.md`.
7. **Done Criteria** — Ask: *"What must be true for this slice to be considered complete? What can you demonstrate?"*
8. **Failure Modes** — Ask: *"What kinds of breakage should be visible if this slice fails? What bugs would this slice expose?"*
9. **Visible Proof** — Ask: *"What should the tester visibly see if the slice works? Not logs or internal state — player-visible results."*
10. **Demo Script** — Ask: *"Walk me through the step-by-step demo. What does the tester do, and what should they see?"*

Leave the Tasks table empty — tasks are created after specs.

### 4. Create the Slice File

Create `scaffold/slices/SLICE-###-<name>_draft.md` using the template with the user's answers. Replace `<name>` with a lowercase-kebab-case version of the slice name.

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
