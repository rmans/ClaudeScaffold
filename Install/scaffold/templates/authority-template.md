# Data Authority Table

> **Authority:** Rank 4
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft
> **Changelog:**
> - YYYY-MM-DD: Initial creation.

---

## Purpose

Defines who **writes** each piece of game data at runtime. Every variable, property, or state has exactly one owning system. Other systems may read it, but only the owner may change it. This prevents silent conflicts where two systems fight over the same value.

## Relationship to Entity Components

This document tracks **cross-system ownership** — which system is the single writer for each shared variable. For the full per-field data shape of each entity (types, components, all fields), see [reference/entity-components.md](../reference/entity-components.md). The Authority column in entity-components is derived from this table. **On conflict, this document wins.**

## Authority Table

### [Domain Name]

<!-- Group variables by domain (Time & Calendar, Colonist — Lifecycle, Colonist — Needs, Health & Injury, Map & Terrain, Structures, etc.). Each domain gets its own subsection and table. -->

| Variable / Property | Owning System | Write Mode | Authority Type | Persistence Owner | Readers | Update Cadence | Notes |
|---------------------|---------------|------------|----------------|-------------------|---------|----------------|-------|
| ... | SYS-### SystemName | direct owner write / delegated setter / event-driven update | Authoritative / Derived / Cache | SYS-### or SaveSystem | SYS-###, SYS-###, UI | Per tick / On event / On change / Once | ... |

<!-- Write Mode values:
  - direct owner write: The owning system writes the value directly during its tick or event handler.
  - delegated setter: Another system calls into the owner through a sanctioned setter interface. Owner still validates.
  - event-driven update: The value updates in response to a signal/event, not a direct call.

Authority Type values:
  - Authoritative: This is the source-of-truth value. Saved and loaded.
  - Derived: Computed from other authoritative values. Not saved — recomputed on load.
  - Cache: A performance copy of data owned elsewhere. Invalidated when source changes. Not saved.

Persistence Owner: The system responsible for serializing/deserializing this value during save/load.
  For Derived/Cache values, enter "—" (not persisted).
-->

<!-- Repeat for each domain. -->

---

## Conflict / TBD

<!-- Track unresolved authority questions here. Any variable where ownership is disputed, unclear, or deferred goes in this table. Resolve each entry via ADR before implementation. -->

| Variable / Property | Contending Systems | Issue | Resolution |
|---------------------|--------------------|-------|------------|
| ... | SYS-### vs SYS-### | TBD — describe the ownership conflict or ambiguity | Pending ADR / ADR-### |

---

## Rules

1. **Single writer per variable.** If two systems need to write the same variable, one is wrong — resolve via ADR.
2. **Readers are listed explicitly.** "All systems" is acceptable only for truly global values (game_speed, simulation_paused). Otherwise, list specific system IDs.
3. **Update Cadence values:** `Per tick` (every simulation tick), `On event` (when triggered), `On change` (when value changes), `Once` (set at creation, never changes).
4. **New variables must be registered here** before implementation. If a task introduces a new shared variable, add it to this table first.
5. **On conflict with entity-components.md, this document wins.** Entity-components derives its Authority column from this table.
