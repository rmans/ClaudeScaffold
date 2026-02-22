---
name: scaffold-new-reference
description: Add entries to a reference doc. Pre-fills from system designs if available, or add entries manually. Pick which doc — entity-components, resource-definitions, signal-registry, or balance-params.
argument-hint: [doc-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Single Reference Doc

Populate a single reference document from system designs: **$ARGUMENTS**

## Supported Documents

| Argument | File | What gets seeded |
|----------|------|------------------|
| `authority` | `scaffold/design/authority.md` | Variable ownership extracted from system Inputs/Outputs |
| `interfaces` | `scaffold/design/interfaces.md` | Interface contracts extracted from system Inputs/Outputs |
| `states` | `scaffold/design/state-transitions.md` | State machines extracted from entity lifecycles |
| `entities` | `scaffold/reference/entity-components.md` | Entity fields from system descriptions |
| `resources` | `scaffold/reference/resource-definitions.md` | Resources from system production/consumption |
| `signals` | `scaffold/reference/signal-registry.md` | Signals/intents from system Outputs tables |
| `balance` | `scaffold/reference/balance-params.md` | Tunable numbers from system designs |

## Steps

### 1. Identify Target

1. Match the argument to a supported document above.
2. If no argument or unrecognized argument, list the options and ask the user which doc to seed.

### 2. Read System Designs

1. **Read** `scaffold/design/systems/_index.md` to get the list of registered systems.
2. **Read every system file** in `scaffold/design/systems/`.
3. If no systems are filled out, stop and tell the user to design systems first.

### 3. Read Existing Content

1. **Read the target reference doc** to see what's already there.
2. **Preserve existing entries** — only add new ones.

### 4. Extract and Propose

Depending on the target document:

**Authority** — For each system, find variables it writes to in Player Actions and System Resolution. Propose ownership entries with readers derived from other systems' Inputs tables.

**Interfaces** — For each pair of systems that communicate (one system's Outputs reference another system's Inputs), draft an interface contract. Identify the data exchanged, direction (push/pull/request), and what guarantees each side provides. Cross-reference with `scaffold/design/authority.md` for data ownership.

**States** — For each entity referenced in systems, look for lifecycle states (idle, active, dead, etc.) or mode changes. Draft state tables with transitions and triggers.

**Entities** — For each noun that systems create, modify, or destroy, draft a component table with fields, types, authority (from authority.md if already seeded), and cadence.

**Resources** — For anything consumed, produced, stored, or traded in system descriptions, draft resource entries with category, tier, and production chains.

**Signals** — For every row in system Outputs tables, draft a signal (notification) or intent (request). Cross-reference with `scaffold/design/interfaces.md`.

**Balance** — For every number mentioned in system designs (rates, thresholds, capacities, timings), draft a parameter entry with suggested unit and range.

### 5. Confirm with User

Present all proposed entries as a table. The user can:
- Confirm all
- Confirm selectively
- Edit entries before writing
- Reject and start over

### 6. Write

Write confirmed entries into the target doc, preserving existing content and formatting.

### 7. Report

Show what was added and flag any gaps (systems that didn't contribute entries, orphaned references). Remind the user to run `/scaffold-review-reference` to audit the doc's completeness.

## Rules

- **Never write without confirmation.**
- **Preserve existing content** — add, don't overwrite.
- **One doc at a time.** For bulk seeding of all docs, use `/scaffold-bulk-seed-references`.
- **Flag conflicts** (e.g., two systems writing the same variable) — don't silently resolve them.
- **"TBD" is valid** for balance param values. Register the parameter even without a number.
