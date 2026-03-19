# [Engine] — Debugging & Observability

> **Layer:** Implementation
> **Authority:** Rank 9
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Status:** Draft
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

## Purpose

<!-- Define how developers inspect, trace, and debug simulation behavior at runtime. For a simulation-heavy game, emergent bugs are miserable without observability tooling. This doc governs what is inspectable, how to trace causality, and what instrumentation exists. -->

*TODO: Define debugging and observability purpose.*

---

## Debug Overlays

<!-- What visual overlays exist for inspecting simulation state at runtime? Examples: pathfinding visualization, zone boundaries, authority ownership highlights, tick order display, entity handle validity. -->

*TODO: Define debug overlay categories and toggle mechanism.*

---

## Simulation Inspection Tools

<!-- How does a developer inspect the current state of any entity, system, or cross-system relationship at runtime? In-game inspector? Console commands? Debug panels? -->

*TODO: Define simulation state inspection tools.*

---

## Event Tracing

<!-- How does a developer trace a chain of events across systems? If a colonist starved, can you reconstruct: which need decayed → when food-seeking triggered → why the task failed → what state the colonist ended in? Define the tracing mechanism. -->

*TODO: Define cross-system event tracing approach.*

---

## State Inspection

<!-- How does a developer inspect the current value of any authoritative variable, entity field, or state machine state? Live watch? Snapshot dump? Query API? -->

*TODO: Define state inspection mechanism.*

---

## Logging Categories

<!-- What logging categories exist? How are they filtered? What severity levels are used? What format? How does logging interact with performance (is it stripped in release builds)? -->

*TODO: Define logging category hierarchy and filtering rules.*

---

## Reproduction Tooling

<!-- For emergent simulation bugs that are hard to reproduce: what tools help capture the state needed to reproduce? Save-state snapshots? Event logs? Seed recording for deterministic replay? -->

*TODO: Define reproduction capture tooling.*

---

## Diagnostics System

<!-- If the project has a runtime diagnostics/invariant checker (like diagnostics_enabled on SimulationOrchestrator), document its scope, activation, and output format here. -->

*TODO: Define runtime diagnostics system if applicable.*

---

## Project Overrides

<!-- If your project deviates from any convention above, document it here. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

---

## Rules

1. **Observability is not optional for simulation games.** Every system must be inspectable at runtime without modifying code.
2. **Tracing must cross system boundaries.** Single-system logging is not sufficient — the trace must follow causality across authority, interfaces, and signals.
3. **Debug tools must not affect simulation behavior.** Overlays and inspectors are read-only. They must never write to simulation state.
4. **Logging categories must be filterable.** A developer must be able to isolate one system's output without drowning in others.
5. **Release builds strip debug overhead.** Debug overlays, verbose logging, and diagnostics must be compile-time removable.
