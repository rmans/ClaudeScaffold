---
name: scaffold-bulk-seed-slices
description: Read phases, systems, and interfaces to bulk-create vertical slice stubs with goals and integration points. Use after phases are defined.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Slices from Phases

Read all phases, system designs, and interface contracts to bulk-create vertical slice stubs.

## Prerequisites

1. **Read `scaffold/phases/_index.md`** to get the list of registered phases.
2. **Read every phase file** in `scaffold/phases/` (Glob `scaffold/phases/P*-*.md`).
3. **Read the roadmap** at `scaffold/phases/roadmap.md` to understand phase ordering.
4. **Read the systems index** at `scaffold/design/systems/_index.md`.
5. **Read relevant system designs** from `scaffold/design/systems/`.
6. **Read the interfaces doc** at `scaffold/design/interfaces.md`.
7. **Read the slice template** at `scaffold/templates/slice-template.md`.
8. **Read the slices index** at `scaffold/slices/_index.md` to find the next available ID and avoid duplicates.
9. **If fewer than 1 phase is defined**, stop and tell the user to create phases first.

## Phase 1 — Identify Slice Candidates

For each phase, analyze its In Scope items to identify natural vertical slices:

1. **Group In Scope items by end-to-end experience.** A vertical slice proves that multiple systems work together. Look for:
   - System clusters that share interfaces (from interfaces.md)
   - Features that require crossing system boundaries
   - The smallest demonstrable chunks of the phase's deliverables
2. **Name each candidate slice** with a clear, action-oriented name (e.g., "player-places-wall" not "building-system").
3. **For each candidate**, draft:
   - **Goal** — one sentence describing the end-to-end experience
   - **Systems involved** — which systems from the phase's scope participate
   - **Integration Points** — which interfaces from interfaces.md are exercised
   - **Suggested specs** — what behaviors need to work (these become spec candidates)

## Phase 2 — Present for Confirmation

Present all candidate slices to the user, organized by phase:

```
### Phase: P#-### — [Name]

Slice 1: [name]
- Goal: [one sentence]
- Systems: SYS-001, SYS-003, SYS-007
- Interfaces: [list from interfaces.md]
- Suggested specs: [behavior list]

Slice 2: [name]
...
```

Ask the user to confirm, modify, or remove slices. Flag any phase scope items that aren't covered by any proposed slice.

## Phase 3 — Create Slice Files

For each confirmed slice:

1. **Assign the next sequential SLICE-### ID** from `scaffold/slices/_index.md`.
2. **Create** `scaffold/slices/SLICE-###-<name>.md` using the slice template:
   - Fill in Goal from the confirmed description.
   - Fill in Integration Points from interfaces.md references.
   - Populate the Specs Included table with suggested spec names (marked as "TBD — create with `/scaffold-new-spec`").
   - Leave the Tasks table empty.
   - Fill in Done Criteria based on the goal.
   - Draft a basic Demo Script skeleton based on the integration points.
3. **Register** the slice in `scaffold/slices/_index.md` with the phase reference.

## Phase 4 — Report

Summarize what was seeded:
- Slices created: X total, across Y phases
- Per phase: how many slices and which scope items they cover
- Specs suggested: X behavior specs to create next

Flag any gaps:
- Phase scope items not covered by any slice
- Systems in scope but not exercised by any slice
- Interfaces not tested by any slice

Remind the user of next steps:
- Review each slice and refine goals, done criteria, and demo scripts
- Run `/scaffold-bulk-review-slices` to audit all slices for cross-slice consistency
- Run `/scaffold-review-slice` on individual slices for detailed review
- Run `/scaffold-bulk-seed-specs` to seed spec stubs from the slice definitions
- Or run `/scaffold-new-spec` to create specs one at a time

## Rules

- **Never write without confirmation.** Present all proposed slices before creating files.
- **Slices must be vertical.** Every slice must cross at least 2 system boundaries. If a scope item maps to a single system, combine it with related items to form a vertical slice.
- **Preserve existing slices.** If slices already exist, add to them — don't overwrite or duplicate.
- **IDs are sequential and permanent** — never skip or reuse.
- **Integration points must reference real interfaces** from interfaces.md. Don't invent interfaces that don't exist.
- **Flag conflicts, don't resolve them.** If phase scope items can't be cleanly divided into slices, present the conflict to the user.
- **One slice per end-to-end experience.** Don't create overlapping slices that prove the same thing.
