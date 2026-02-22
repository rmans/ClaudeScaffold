# Entity Components

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Status:** Draft

---

## Purpose

Master registry of every entity in the game and its fields, grouped by component. Defines the data shape for each entity type — what fields it has, their types, which system owns them, and how often they update.

## Relationship to Authority Table

The Authority column in entity tables is a **convenience reference** derived from [design/authority.md](../design/authority.md). That document is the canonical source for data ownership (Rank 4). If the Authority column here conflicts with authority.md, **authority.md wins** — update this document to match.

## Entities

<!-- Add entities as they are designed. One section per entity type. -->

*None yet.*

<!-- Example entry:

### Colonist

| Component | Field | Type | Authority | Cadence | Notes |
|-----------|-------|------|-----------|---------|-------|
| Identity | name | string | Static | Once | Set at creation |
| Identity | age | int | Static | Once | Set at creation |
| Health | current_hp | float | SYS-003 Health | Per tick | Clamped 0–max_hp |
| Health | max_hp | float | SYS-003 Health | On change | Modified by traits, equipment |
| Health | bleed_rate | float | SYS-003 Health | On damage | 0 when not bleeding |
| Needs | hunger | float | SYS-002 Needs | Per tick | 0 = full, 1 = starving |
| Needs | rest | float | SYS-002 Needs | Per tick | 0 = rested, 1 = exhausted |
| Needs | mood | float | SYS-002 Needs | Per tick | Derived from need satisfaction |
| Movement | position | vec2 | SYS-006 Pathfinding | Per frame | World coordinates |
| Movement | speed | float | SYS-006 Pathfinding | On change | Modified by terrain, health |
| Work | current_task | ref | SYS-005 Job Queue | On assignment | null when idle |
| Work | skill_levels | dict | SYS-005 Job Queue | On completion | Skill → level mapping |

-->

## Template

Use this format for each entity:

```markdown
### [Entity Name]

| Component | Field | Type | Authority | Cadence | Notes |
|-----------|-------|------|-----------|---------|-------|
| ... | ... | ... | ... | ... | ... |
```

## Rules

1. **Every field has one authority.** Cross-reference with [authority.md](../design/authority.md) — they must agree.
2. **Types are logical, not engine-specific.** Use `string`, `int`, `float`, `bool`, `vec2`, `ref`, `dict`, `enum` — not engine class names.
3. **Cadence must be explicit.** "Per tick", "per frame", "on change", "on event", "once" — never leave it ambiguous.
4. **Static fields are immutable after creation.** If a "static" field turns out to need updates, change its authority and cadence.
