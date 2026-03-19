# Enums & Statuses — Canonical Reference

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** System designs and state-transitions.md
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft

---

## Purpose

Canonical shared vocabulary for all status, state, and enum values used across multiple systems. Prevents terminology fragmentation — when two systems refer to the same concept, they must use the same term from this document.

Single-system enums that are never referenced externally may remain in their system doc's State Lifecycle section. This document captures only **shared** vocabulary.

---

## How to Use This Document

- When a system doc references a state or status value, it must match an entry here if the value is cross-system.
- When a spec references a precondition or postcondition involving state, the state name must match this document.
- When adding a new shared enum, register it here first — don't invent terms in individual system docs.
- The glossary captures player-facing terms. This document captures simulation-facing state vocabulary.

---

## Job / Task States

<!-- States that describe work assignments, task lifecycle, and job processing across any system that manages tasks or work. -->
<!-- Cross-ref: See state-transitions.md for the full transition graph of task/job state machines. -->

| State | Meaning | Used By | Owning Authority / System | Source of Truth | Deprecated Synonyms |
|-------|---------|---------|---------------------------|-----------------|----------------------|
| ... | ... | SYS-### | SYS-### SystemName | state-transition / authority / interface / UI | Former names no longer valid |

<!-- Column definitions for all enum tables:
  - Owning Authority / System: The system that is the single writer for this state value (must match authority.md).
  - Source of Truth: Which document/mechanism defines the valid values and transitions for this enum:
    - state-transition: Defined in state-transitions.md with a full transition graph.
    - authority: Defined in authority.md as a data ownership entry.
    - interface: Defined in interfaces.md as part of a cross-system contract.
    - UI: Defined by UI requirements (display-only, no simulation authority).
  - Deprecated Synonyms: Previous names for this state that may appear in old docs or code. Listed so reviewers can catch stale references.
-->

---

## Construction States

<!-- States that describe the lifecycle of a structure from planned to complete/destroyed. -->
<!-- Cross-ref: See state-transitions.md for the full construction state machine. -->

| State | Meaning | Used By | Owning Authority / System | Source of Truth | Deprecated Synonyms |
|-------|---------|---------|---------------------------|-----------------|----------------------|
| ... | ... | SYS-### | SYS-### SystemName | state-transition / authority / interface / UI | ... |

---

## Colonist Activity States

<!-- States that describe what a colonist is currently doing. -->
<!-- Cross-ref: See state-transitions.md for the colonist activity state machine. -->

| State | Meaning | Used By | Owning Authority / System | Source of Truth | Deprecated Synonyms |
|-------|---------|---------|---------------------------|-----------------|----------------------|
| ... | ... | SYS-### | SYS-### SystemName | state-transition / authority / interface / UI | ... |

---

## Need / Vital States

<!-- States that describe colonist need levels, satisfaction, and vital status. -->

| State | Meaning | Used By | Owning Authority / System | Source of Truth | Deprecated Synonyms |
|-------|---------|---------|---------------------------|-----------------|----------------------|
| ... | ... | SYS-### | SYS-### SystemName | state-transition / authority / interface / UI | ... |

---

## Alert / Severity Levels

<!-- Severity or priority levels used by alert, event, or notification systems. -->

| Level | Meaning | Used By | Owning Authority / System | Source of Truth | Deprecated Synonyms |
|-------|---------|---------|---------------------------|-----------------|----------------------|
| ... | ... | SYS-### | SYS-### SystemName | state-transition / authority / interface / UI | ... |

---

## Resource States

<!-- States that describe resource availability, reservation, or consumption status. -->

| State | Meaning | Used By | Owning Authority / System | Source of Truth | Deprecated Synonyms |
|-------|---------|---------|---------------------------|-----------------|----------------------|
| ... | ... | SYS-### | SYS-### SystemName | state-transition / authority / interface / UI | ... |

---

## Damage / Health States

<!-- States that describe damage levels, structural integrity, or health for entities or structures. -->

| State | Meaning | Used By | Owning Authority / System | Source of Truth | Deprecated Synonyms |
|-------|---------|---------|---------------------------|-----------------|----------------------|
| ... | ... | SYS-### | SYS-### SystemName | state-transition / authority / interface / UI | ... |

---

## Ownership / Control States

<!-- States that describe who controls or owns an entity, zone, or resource. -->

| State | Meaning | Used By | Owning Authority / System | Source of Truth | Deprecated Synonyms |
|-------|---------|---------|---------------------------|-----------------|----------------------|
| ... | ... | SYS-### | SYS-### SystemName | state-transition / authority / interface / UI | ... |

---

## Custom Enums

<!-- Add additional enum categories as the project discovers shared vocabulary needs. Each category should have a clear scope heading, a table with State/Meaning/Used By columns, and a comment explaining what this category covers. -->

---

## Rules

1. **Shared vocabulary only.** Single-system enums stay in their system doc.
2. **Canonical terms.** If two systems use different names for the same concept, reconcile here — one canonical term, the other goes in the NOT column.
3. **Used By is mandatory.** Every entry must list which systems reference it. If only one system uses a term, it probably doesn't belong here.
4. **State transitions reference this document.** `design/state-transitions.md` state names must match entries here for cross-system states.
5. **Glossary is player-facing. This doc is simulation-facing.** Player-visible terms go in `design/glossary.md`. Internal simulation state vocabulary goes here.
