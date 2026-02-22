---
name: scaffold-bulk-seed-references
description: Read all system designs and bulk-populate reference docs, state transitions, and the authority table. Use after system designs are filled out.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed References from System Designs

Read all completed system designs and use them to bulk-populate the companion docs.

## Prerequisites

1. **Read** `scaffold/design/systems/_index.md` to get the list of registered systems.
2. **Read every system file** in `scaffold/design/systems/`.
3. **Verify systems are sufficiently filled out.** Each system should have content (not just template defaults) in at least:
   - Purpose
   - Player Actions
   - System Resolution
   - Inputs & Dependencies
   - Outputs & Consequences
4. If fewer than 2 systems are filled out, stop and tell the user to design more systems first.

## Phase 1 — Authority Table

1. **Read** `scaffold/design/authority.md`.
2. **Extract ownership claims** from every system's Player Actions, System Resolution, and Inputs/Outputs tables. Look for:
   - Variables or properties a system writes to (that system is the owner)
   - Variables a system reads from another system (that system is a reader)
3. **Propose entries** for the authority table:
   ```
   | Variable / Property | Owning System | Readers | Update Cadence | Notes |
   ```
4. **Present to the user for confirmation.** Flag any conflicts where two systems appear to write the same variable.
5. **Write confirmed entries** into `scaffold/design/authority.md`.

## Phase 2 — State Transitions

1. **Read** `scaffold/design/state-transitions.md`.
2. **Extract state machines** from system designs. Look for:
   - Entities that have lifecycle states (idle, active, dead, etc.)
   - Entities that change mode (building → built, raw → refined)
   - Any mention of "state", "status", "phase", "mode" in system designs
3. **For each proposed state machine**, draft:
   - Name and owning system
   - State table (State → Transitions To → Trigger)
   - Invariants
4. **Present to the user for confirmation.**
5. **Write confirmed state machines** into `scaffold/design/state-transitions.md`.

## Phase 3 — Entity Components

1. **Read** `scaffold/reference/entity-components.md`.
2. **Extract entities** from system designs. Any noun that a system creates, modifies, moves, or destroys is likely an entity. Look for:
   - Entities named in Player Actions and System Resolution
   - Entities implied by state machines (Phase 2)
   - Entities implied by the authority table (Phase 1)
3. **For each entity**, draft a component table:
   - Group fields by component (logical grouping: Identity, Health, Movement, etc.)
   - Assign types (string, int, float, bool, vec2, ref, dict, enum)
   - Set Authority from the authority table (Phase 1)
   - Set Cadence (per tick, per frame, on change, on event, once)
4. **Present to the user for confirmation.**
5. **Write confirmed entities** into `scaffold/reference/entity-components.md`.

## Phase 4 — Resource Definitions

1. **Read** `scaffold/reference/resource-definitions.md`.
2. **Extract resources** from system designs. Look for:
   - Anything consumed, produced, stored, or traded in system descriptions
   - Materials mentioned in Player Actions (e.g., "player selects stone")
   - Items in Inputs/Outputs tables
3. **For each resource**, draft:
   - Category, tier, production chain, storage type
4. **Present to the user for confirmation.**
5. **Write confirmed resources** into `scaffold/reference/resource-definitions.md`.
6. **Draft production chains** if multi-step resource transformations exist.

## Phase 5 — Signal Registry

1. **Read** `scaffold/reference/signal-registry.md`.
2. **Extract signals** from system Inputs/Outputs tables. Every row in an Outputs table is a candidate signal or intent:
   - If a system **notifies** others that something happened → Signal (past tense: `building_placed`)
   - If a system **requests** another system to act → Intent (noun: `haul_request`)
3. **For each proposed signal/intent**, draft:
   - Name (snake_case), payload, emitter, consumer(s)
4. **Cross-reference with** `scaffold/design/interfaces.md` — signals should align with interface contracts.
5. **Present to the user for confirmation.**
6. **Write confirmed signals** into the Signals table and intents into the Intent Objects table.

## Phase 6 — Balance Parameters

1. **Read** `scaffold/reference/balance-params.md`.
2. **Extract tunable numbers** from system designs. Look for:
   - Any number mentioned in Player Actions, System Resolution, or Failure States
   - Rates (speed, decay, regeneration)
   - Thresholds (health at which X happens, mood below which Y triggers)
   - Capacities (stack limits, storage sizes, population caps)
   - Timings (cooldowns, durations, intervals)
3. **For each parameter**, draft:
   - Name, initial value (or "TBD"), unit, suggested range, owning system
4. **Present to the user for confirmation.** Values can be approximate — tuning comes later.
5. **Write confirmed parameters** into `scaffold/reference/balance-params.md`, grouped by system.

## Phase 7 — Report

Summarize what was seeded:
- Authority table: X entries
- State machines: X defined
- Entities: X with Y total fields
- Resources: X defined, Y production chains
- Signals: X signals, Y intents
- Balance parameters: X registered

Flag any gaps:
- Systems that didn't contribute to any reference doc (may be underdesigned)
- Variables with no clear owner
- Entities referenced but not fully defined

Remind the user of next steps:
- Review and refine each reference doc
- Run `/scaffold-bulk-review-references` to audit all reference docs for cross-doc consistency
- Run `/scaffold-review-reference` on individual docs for detailed review
- Run `/scaffold-review-design` to check overall design consistency

## Rules

- **Never write without confirmation.** Every phase presents proposals before writing.
- **Work phase by phase.** Complete one phase before starting the next — later phases build on earlier ones.
- **Authority table comes first** because entity-components and balance-params reference it.
- **Preserve existing content.** If a reference doc already has entries, add to them — don't overwrite.
- **Flag conflicts, don't resolve them.** If two systems claim the same variable or entity field, present the conflict to the user. Don't guess.
- **"TBD" is a valid value.** For balance params where no number exists yet, use TBD. The point is to register the parameter, not to tune it.
- **Cross-reference everything.** Every entity should trace back to a system. Every signal should trace back to an Outputs table. Every authority entry should trace back to a system's responsibilities. If something is orphaned, flag it.
