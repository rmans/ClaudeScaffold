---
name: scaffold-bulk-seed-specs
description: Read slices, system designs, and state transitions to bulk-create behavior spec stubs with pre-filled behavior from systems. Use after slices are defined.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Specs from Slices

Read all slices, system designs, and state transitions to bulk-create behavior spec stubs.

## Prerequisites

1. **Read `scaffold/slices/_index.md`** to get the list of registered slices.
2. **Read every slice file** in `scaffold/slices/` (Glob `scaffold/slices/SLICE-*.md`).
3. **Read the systems index** at `scaffold/design/systems/_index.md`.
4. **Read every system design** in `scaffold/design/systems/`.
5. **Read state transitions** at `scaffold/design/state-transitions.md`.
6. **Read the spec template** at `scaffold/templates/spec-template.md`.
7. **Read the specs index** at `scaffold/specs/_index.md` to find the next available ID and avoid duplicates.
8. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md` — ADRs may have changed system behavior.
9. **If fewer than 1 slice is defined**, stop and tell the user to create slices first.

## Phase 1 — Extract Spec Candidates

For each slice, read its Specs Included table and Goal to identify specs:

1. **If the slice already lists spec names**, use those as starting points.
2. **Cross-reference with system designs.** For each system involved in the slice:
   - Each distinct behavior in Player Actions is a spec candidate
   - Each state transition trigger is a spec candidate
   - Each failure state is a spec candidate (or edge case within a broader spec)
3. **Name each spec** with a behavior-focused name (e.g., "place-wall-on-empty-tile" not "wall-placement-system").
4. **For each candidate**, draft:
   - **Summary** — one sentence from the system design's relevant section
   - **Preconditions** — derived from the system's Player Actions prerequisites
   - **Behavior** — numbered steps from Player Actions and System Resolution
   - **Postconditions** — observable results from System Resolution
   - **Edge Cases** — from the system's Edge Cases section
   - **Acceptance Criteria** — derived from behavior steps (each step becomes a verifiable check)

## Phase 2 — ADR Impact Check

For each spec candidate, check all ADRs:
- Did an ADR change the system behavior this spec covers?
- Did an ADR add constraints or remove features relevant to this spec?

If ADRs affect a spec, annotate the draft with the ADR reference and its impact.

## Phase 3 — Present for Confirmation

Present all candidate specs to the user, organized by slice:

```
### Slice: SLICE-### — [Name]

Spec 1: SPEC-### — [name]
- System: SYS-###
- Summary: [one sentence]
- Behavior: [numbered steps from system design]
- ADR impacts: [if any]

Spec 2: SPEC-### — [name]
...
```

Ask the user to confirm, modify, merge, split, or remove specs. Flag:
- Slice goal areas not covered by any proposed spec
- System behaviors not covered by any spec
- Specs that seem too broad (suggest splitting)

## Phase 4 — Create Spec Files

For each confirmed spec:

1. **Assign the next sequential SPEC-### ID** from `scaffold/specs/_index.md`.
2. **Create** `scaffold/specs/SPEC-###-<name>.md` using the spec template:
   - Fill in Summary, Preconditions, Behavior, Postconditions, Edge Cases, and Acceptance Criteria from the confirmed drafts.
   - Set the System reference to the parent system ID.
   - Set the Conforms to reference.
3. **Register** the spec in `scaffold/specs/_index.md` with the system reference and slice reference.
4. **Update** the parent slice's Specs Included table with the new spec ID and description.

## Phase 5 — Report

Summarize what was seeded:
- Specs created: X total, across Y slices
- Per slice: how many specs and what behaviors they cover
- Per system: how many specs reference each system

Flag any gaps:
- Slice goals not fully covered by specs
- System behaviors (Player Actions) with no spec
- State transitions with no spec
- ADRs that affect specs (annotated in the spec files)

Remind the user of next steps:
- Review each spec and refine behavior steps, edge cases, and acceptance criteria
- Run `/scaffold-bulk-review-specs` to audit all specs for cross-spec consistency
- Run `/scaffold-review-spec` on individual specs for detailed review
- Run `/scaffold-bulk-seed-tasks` to seed task stubs from the spec definitions
- Or run `/scaffold-new-task` to create tasks one at a time

## Rules

- **Never write without confirmation.** Present all proposed specs before creating files.
- **Specs describe BEHAVIOR, not IMPLEMENTATION.** No signals, methods, nodes, classes, functions, or engine constructs in spec content. System designs are the source — translate Player Actions and System Resolution into spec language.
- **Pre-filled content is a starting point.** Always present pre-filled content for user confirmation — never treat it as final.
- **Preserve existing specs.** If specs already exist, add to them — don't overwrite or duplicate.
- **IDs are sequential and permanent** — never skip or reuse.
- **Each spec should be atomic** — one testable behavior. If a system behavior is complex, suggest splitting into multiple specs.
- **Flag conflicts, don't resolve them.** If system designs disagree about a behavior, present the conflict to the user.
- **ADR impacts must be noted.** If an ADR changes a system behavior, the spec must reflect the post-ADR behavior, not the original.
- **Created documents start with Status: Draft.**
