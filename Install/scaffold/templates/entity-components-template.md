# Entity Components

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft
> **Changelog:**
> - YYYY-MM-DD: Initial creation.

---

## Purpose

Master registry of every entity in the game and its fields, grouped by component. Defines the data shape for each entity type — what fields it has, their types, which system owns them, and how often they update.

## Relationship to Authority Table

The Authority column in entity tables is a **convenience reference** derived from [design/authority.md](../design/authority.md). That document is the canonical source for data ownership (Rank 4). If the Authority column here conflicts with authority.md, **authority.md wins** — update this document to match.

## Entity Reference Convention

<!-- Define how entities reference each other. Example: EntityHandle {int32_t index, uint32_t generation} for generational handles, or bare int IDs, or string keys. The `ref` type in tables below means this reference type. -->

All entity references use `ref` type — define the concrete reference mechanism here.

## Content Identity Convention

<!-- Define how game content types (items, structures, recipes, traits) are identified. Example: namespaced string IDs via ContentRegistry, or enum values, or integer keys. -->

Game content types use string/enum IDs — define the concrete identity mechanism here.

## Reference Type Conventions

<!-- Define the standard reference types used across all entity tables. Every field typed as a reference must use one of these conventions. -->

| Reference Type | Description | Nullability | Example |
|----------------|-------------|-------------|---------|
| Entity Ref | Reference to a runtime entity instance (e.g., colonist, structure, item). Uses the project's entity handle mechanism. | Nullable — must handle invalid/destroyed refs | `colonist_ref`, `task_ref` |
| Content Ref | Reference to a content definition (e.g., item type, structure type, recipe). Uses the project's content identity mechanism. | Non-null — content definitions are static and always valid | `item_type_id`, `recipe_id` |
| World Ref | Reference to a spatial location or world feature (e.g., tile coordinate, room ID, zone ID). | Nullable — location may become invalid (destroyed room, etc.) | `tile_pos`, `room_ref` |

<!-- Update these conventions to match your project's identity mechanisms (generational handles, integer IDs, string keys, etc.). -->

## Singleton Conventions

<!-- Define how singleton entities (one-per-game instances) are handled. Singletons don't use entity handles — they are accessed directly. -->

- Singleton entities are listed with `Singleton` in the Component column of their entity table.
- Singletons are not referenced by handle — systems access them directly through the owning system's API.
- Examples: Colony, World, PowerGrid, Calendar.
- Singletons must still register all fields in the entity table below.

## Derived / Cache Field Policy

<!-- Define the rules for fields that are computed from other fields rather than stored as authoritative data. -->

- **Derived fields** are recomputed from authoritative data. They are NOT saved — they are rebuilt on load. Mark with `Derived` in the Authority column.
- **Cache fields** are performance copies of data owned by another system. Mark with `Cache` in the Authority column. They must document their invalidation trigger in Notes.
- Derived and Cache fields must list their source fields or source system in the Notes column.
- On conflict between a Derived/Cache value and its authoritative source, the authoritative source wins — the Derived/Cache field has a bug.

---

## Entities

### [Entity Name]

<!-- Group fields by component (Identity, Lifecycle, Needs, Health, Skills, Work, etc.). Each entity gets its own subsection. -->

| Component | Field | Type | Authority | Cadence | Persistence | Notes |
|-----------|-------|------|-----------|---------|-------------|-------|
| Identity | name | string | Static | Once | Saved | Set at creation |
| ... | ... | ... | SYS-### SystemName | Per tick / On event / On change / Once | Saved / Derived / Transient | ... |

<!-- Persistence values:
  - Saved: This field is serialized to the save file and restored on load. Authoritative data.
  - Derived: This field is NOT saved — it is recomputed from other Saved fields on load. List source in Notes.
  - Transient: This field is NOT saved — it is reset to a default on load (e.g., UI state, animation state).
-->

<!-- Type values: string, int, float, bool, enum, list, dict, ref (entity reference), Vector2i (grid position), etc.
     Authority values: Static (never changes after creation), or SYS-### SystemName (owning system).
     Cadence values: Once (set at creation), Per tick, On event, On change. -->

---

<!-- Repeat for each entity. Entities include:
  - Gameplay entities: Colonist, Task, Structure, Room, Item, etc.
  - Sub-entities: Wound, TraitProfile, ProductionJob, etc.
  - Singletons: PowerGrid, Colony, World, etc.

  Each entity section should list ALL fields grouped by component.
-->

<!-- Template for adding a new entity:

### [Entity Name]

| Component | Field | Type | Authority | Cadence | Persistence | Notes |
|-----------|-------|------|-----------|---------|-------------|-------|
| Identity | id | int | Static | Once | Saved | Unique entity ID |
| ... | ... | ... | ... | ... | Saved / Derived / Transient | ... |

-->

---

## Rules

1. **Every entity field must be registered here.** If code adds a new field to an entity, it must appear in this document.
2. **Authority column must match authority.md.** This is a convenience copy — authority.md is the source of truth.
3. **Component grouping is semantic.** Group fields by what aspect of the entity they describe (Identity, Lifecycle, Health, Skills, etc.), not by implementation.
4. **Types must be concrete.** Use specific types (float, enum, list of ref), not vague descriptions.
5. **Cadence must be accurate.** Per tick means it changes every tick. On event means it changes in response to specific triggers. Don't over-report cadence.
