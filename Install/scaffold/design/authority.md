# Data Authority Table

> **Authority:** Rank 4
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md)
> **Status:** Draft

---

## Purpose

Defines who **writes** each piece of game data at runtime. Every variable, property, or state has exactly one owning system. Other systems may read it, but only the owner may change it. This prevents silent conflicts where two systems fight over the same value.

## Relationship to Entity Components

This document tracks **cross-system ownership** — which system is the single writer for each shared variable. For the full per-field data shape of each entity (types, components, all fields), see [reference/entity-components.md](../reference/entity-components.md). The Authority column in entity-components is derived from this table. **On conflict, this document wins.**

## Authority Table

<!-- Add entries as systems are designed. One row per variable or property. -->

| Variable / Property | Owning System | Readers | Update Cadence | Notes |
|---------------------|---------------|---------|----------------|-------|
| *None yet* | — | — | — | — |

<!-- Example entries:
| colonist.mood          | SYS-002 Needs & Mood | UI, AI Behavior     | Per tick        | Derived from need satisfaction |
| tile.building          | SYS-001 Construction | Pathfinding, Room   | On build/remove | null when empty               |
| resource.stone.count   | SYS-004 Resources    | UI, Construction    | On change       | Clamped to storage capacity    |
| colonist.current_task  | SYS-005 Job Queue    | AI Behavior, UI     | On assignment   | null when idle                 |
-->

## Rules

1. **Single writer.** Every variable has exactly one owning system. If two systems need to write the same value, resolve it with an ADR.
2. **Readers are unlimited.** Any system may read any variable, but must not cache stale values across frames without a clear invalidation strategy.
3. **Cadence matters.** A variable updated "per tick" has different reliability guarantees than one updated "on change." Readers must respect the cadence.
4. **New variables must be registered here** before they are implemented. If a variable isn't in this table, it doesn't officially exist.

## Conflict Resolution

If you find two systems writing to the same variable:

1. Check if one is actually a derived value (should be read-only + recalculated).
2. If both genuinely need write access, file an ADR to split the variable or designate a mediator system.
3. Never resolve it by having both systems write and "hoping for the best."
