# System Interfaces

> **Authority:** Rank 4
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md)

---

## Purpose

Defines the contracts between game systems — what data flows between them, in what direction, and under what guarantees. This is the design-layer view of system communication: it describes WHAT systems exchange, not HOW (signals, methods, and payloads are registered in [reference/signal-registry.md](../reference/signal-registry.md)).

## Relationship to Other Documents

- **This document** defines the contracts: who talks to whom, what data is exchanged, and what guarantees hold.
- **[reference/signal-registry.md](../reference/signal-registry.md)** (Rank 6) registers the actual signal names, payloads, and intent objects that implement these contracts. Signal-registry conforms to this document.
- **[authority.md](authority.md)** (Rank 4) defines who WRITES each variable. Interfaces define who READS and what they can assume about it.
- **System designs** (`systems/SYS-###`) list their own Inputs & Dependencies and Outputs & Consequences. This document is the cross-system view — it resolves conflicts between individual system claims.

## Interface Summary

<!-- Quick-reference table of all system-to-system interfaces. One row per interface. -->

| Source System | Target System | Data Exchanged | Direction | Notes |
|---------------|---------------|----------------|-----------|-------|
| *None yet* | — | — | — | — |

<!-- Example entries:
| SYS-001 Construction | Pathfinding       | building footprint, walkability changes | Push (signal) | Pathfinding rebuilds on change |
| SYS-001 Construction | SYS-004 Resources | material requirements, refund amounts    | Pull (query)  | Construction reads resource counts |
| SYS-002 Needs & Mood | UI                | mood level, need satisfaction bars       | Push (signal) | UI subscribes to mood changes |
| SYS-005 Job Queue    | SYS-002 Needs     | job assignment, job completion           | Push (signal) | Needs system tracks work satisfaction |
-->

## Interface Contracts

<!-- Detailed contracts grouped by domain. Each contract describes what the source provides, what the target can assume, and what invariants hold. -->

*TODO: Define interface contracts as systems are designed.*

<!-- Example contract:

### Construction → Pathfinding

**Data exchanged:** Building footprint (position, size, walkability mask)
**Direction:** Push — Construction notifies Pathfinding when buildings are placed or removed.
**Source guarantees:**
- Footprint data is valid and within world bounds.
- Signal fires after the building is committed, never during preview/ghost placement.
- Removal signal fires before the building entity is destroyed.
**Target guarantees:**
- Pathfinding rebuilds affected navmesh within one frame.
- If rebuild fails, Pathfinding logs an error but does not block Construction.
**Failure mode:** If Pathfinding is unavailable, Construction proceeds — entities may path through buildings until the next rebuild.

### Construction ← Resources (Pull)

**Data exchanged:** Resource counts, storage capacity
**Direction:** Pull — Construction reads current resource levels before starting a build.
**Source guarantees:**
- Resource counts are accurate as of the current frame.
- Counts are never negative.
**Target guarantees:**
- Construction does not cache resource values across frames.
- Construction deducts resources through the Resources system's API, never by direct write.
**Failure mode:** If resources are insufficient, Construction shows a "not enough materials" indicator.

-->

## Communication Patterns

Interfaces use one of these patterns. Each interface in the summary table should specify which:

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Push (signal)** | Source emits a notification. Targets subscribe and react. | Source doesn't need a response. Multiple targets may care. |
| **Pull (query)** | Target reads data from the source on demand. | Target needs data at its own pace. Source doesn't need to know who's reading. |
| **Request (intent)** | Source sends a request. Target decides whether and how to fulfill it. | Source needs something done but doesn't own the capability. |

## Rules

1. **Systems communicate only through interfaces defined here.** No system may reach into another system's internals.
2. **Every interface has a direction.** Push, pull, or request — never ambiguous.
3. **Guarantees are contracts, not hopes.** If a guarantee says "within one frame," the implementation must enforce it.
4. **Interface changes require an ADR** (see [decisions/](../decisions/_index.md)). Changing an interface affects every system on both sides.
5. **No undocumented interfaces.** If two systems communicate and it's not in this document, it's a bug.
6. **This document resolves conflicts.** If two system designs disagree about what data flows between them, this document is the tiebreaker.
