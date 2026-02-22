---
name: scaffold-review-reference
description: Review a single reference doc for completeness, accuracy, and consistency with system designs. Pick which doc to audit.
argument-hint: [doc-name]
allowed-tools: Read, Grep, Glob
---

# Reference Doc Review

Review a single reference document: **$ARGUMENTS**

## Supported Documents

| Argument | File |
|----------|------|
| `authority` | `scaffold/design/authority.md` |
| `states` | `scaffold/design/state-transitions.md` |
| `entities` | `scaffold/reference/entity-components.md` |
| `resources` | `scaffold/reference/resource-definitions.md` |
| `signals` | `scaffold/reference/signal-registry.md` |
| `balance` | `scaffold/reference/balance-params.md` |

## Steps

### 1. Identify Target

1. Match the argument to a supported document above.
2. If no argument or unrecognized argument, list the options and ask the user which doc to review.

### 2. Read the Target Doc

Read the reference doc and assess its overall state — empty, partially filled, or populated.

### 3. Read System Designs for Cross-Reference

1. Read `scaffold/design/systems/_index.md` to get registered systems.
2. Read every system file in `scaffold/design/systems/`.

### 4. Completeness Check

Depending on the target:

**Authority** —
- Every variable referenced in system Inputs/Outputs should have an authority entry.
- Every entry should have: Variable, Owning System, Readers, Update Cadence.
- Flag variables mentioned in systems but missing from the authority table.

**States** —
- Every entity with lifecycle states in system designs should have a state machine.
- Every state machine should have: states, transitions, triggers, invariants.
- Flag entities with implied states (idle, active, dead, etc.) but no state machine.

**Entities** —
- Every entity referenced in system designs should have a component table.
- Every field should have: Component, Field, Type, Authority, Cadence.
- Authority column should match `scaffold/design/authority.md`.
- Flag entities mentioned in systems but not defined here.

**Resources** —
- Every resource consumed/produced in system designs should be registered.
- Every resource should have: Category, Tier, Produced By, Consumed By, Storage Type.
- Production chains should be acyclic.
- Flag resources mentioned in systems but not defined here.

**Signals** —
- Every cross-system output in system Outputs tables should map to a signal or intent.
- Every signal should have: Name, Payload, Emitter, Consumer(s).
- Naming convention: snake_case, past tense for signals, noun for intents.
- Flag system outputs that don't have a registered signal.
- Cross-reference with `scaffold/design/interfaces.md` for contract alignment.

**Balance** —
- Every tunable number mentioned in system designs should be registered.
- Every parameter should have: Name, Value (or TBD), Unit, Range, System.
- Units must be explicit — no ambiguous numbers.
- Flag numbers in system designs that aren't registered here.

### 5. Quality Check

For all reference docs:
- **No stale entries.** Every entry should trace back to a current system. Flag orphaned entries that reference deleted or renamed systems.
- **Consistent naming.** Check against `scaffold/design/glossary.md` if it has entries.
- **No duplicates.** Flag entries that appear more than once.
- **Formatting.** Tables should be well-formed with no missing columns.

## Output Format

```
## Reference Review: [Doc Name]

### Completeness: X entries, Y gaps
[List of registered entries and missing entries]

### Quality Issues
- [Specific issues with quotes]

### Cross-Reference Gaps
- [Systems that should contribute but don't]
- [Entries that reference non-existent systems]

### Recommendations
1. [Most important fix]
2. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific — name the system and the missing entry when flagging gaps.
- If the doc is empty, don't just say "empty" — list what SHOULD be in it based on current system designs.
- If no systems are designed yet, report that and suggest filling in systems first.
