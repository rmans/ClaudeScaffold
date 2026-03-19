# System Interfaces

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

Defines the contracts between game systems — what data flows between them, in what direction, and under what guarantees. This is the design-layer view of system communication: it describes WHAT systems exchange, not HOW (signals, methods, and payloads are registered in [reference/signal-registry.md](../reference/signal-registry.md)).

## Relationship to Other Documents

- **This document** defines the contracts: who talks to whom, what data is exchanged, and what guarantees hold.
- **[reference/signal-registry.md](../reference/signal-registry.md)** (Rank 6) registers the actual signal names, payloads, and intent objects that implement these contracts. Signal-registry conforms to this document.
- **[authority.md](authority.md)** (Rank 4) defines who WRITES each variable. Interfaces define who READS and what they can assume about it.
- **System designs** (`systems/SYS-###`) list their own Upstream Dependencies and Downstream Consequences. This document is the cross-system view — it resolves conflicts between individual system claims.

## Interface Summary

### [Domain Name] Interfaces

<!-- Group interfaces by domain (Time & Calendar, Colonist Lifecycle, Needs & Morale, Health & Injury, Tasks & Production, Map & Structures, Power & Environment, Storage & Zones, etc.). Each domain gets its own subsection and table. -->

| Source System | Target System | Data Exchanged | Direction | Realization Path | Timing | Failure Guarantee | Notes |
|---------------|---------------|----------------|-----------|------------------|--------|-------------------|-------|
| SYS-### Name | SYS-### Name | Description of data | Push / Pull / Request | signal / intent / query API / direct sanctioned interface call | immediate / deferred / next tick | can fail / no-op / queue / retry | Guarantees, conditions |

<!-- Realization Path values:
  - signal: Past-tense notification via signal bus. See signal-registry.md.
  - intent: Noun-form request object. Receiving system decides whether to act.
  - query API: Target exposes a read-only query that source calls synchronously.
  - direct sanctioned interface call: Source calls a method on the target through a documented interface. Use sparingly.

Timing values:
  - immediate: Processed in the same tick/frame the data is sent.
  - deferred: Queued and processed later in the same tick (e.g., end-of-tick batch).
  - next tick: Queued and processed in the following simulation tick.

Failure Guarantee values:
  - can fail: The operation may fail and the caller must handle failure.
  - no-op: On failure, nothing happens — silently ignored.
  - queue: On failure, the request is queued for retry.
  - retry: The system retries automatically until success or timeout.
-->

<!-- Direction types:
  - Push: Source sends data/signal to target when something happens.
  - Pull: Target reads data from source when it needs it.
  - Request: Source sends an intent/request to target; target decides whether to act.
-->

<!-- Repeat for each domain. -->

---

## Missing / TBD Contracts

<!-- Track interfaces that are known to be needed but not yet fully defined. Each entry represents a system interaction gap discovered during design or implementation. Resolve each before the relevant spec is Approved. -->

| Source System | Target System | Expected Data | Blocker | Resolution |
|---------------|---------------|---------------|---------|------------|
| SYS-### Name | SYS-### Name | Description of expected data flow | Why this contract is incomplete | Pending spec / ADR-### / TBD |

---

## Rules

1. **This document describes WHAT flows between systems.** Signal names, payloads, and methods belong in signal-registry.md. Implementation details belong in engine docs.
2. **Every interface must have both systems registered** in `design/systems/`. If a system doesn't exist yet, the interface is speculative — mark it as such.
3. **Direction is explicit.** Push, Pull, or Request. No ambiguous "bidirectional" without specifying which direction for which data.
4. **Contracts resolve conflicts.** When a system design claims an input/output that conflicts with another system's claims, this document is the tiebreaker.
5. **New cross-system data flows must be registered here** before implementation. If a task introduces a new system interaction, add it to this table first.
