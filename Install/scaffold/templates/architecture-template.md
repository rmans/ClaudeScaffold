# Software Architecture

> **Status:** Draft
> **Authority:** Rank 2 — Canon (alongside style-guide, color-system, ui-kit, glossary)
> **Layer:** Design — Engineering conventions
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Changelog:**
> - YYYY-MM-DD: Initial creation.

## Purpose

This document defines **project-level engineering conventions**: the scene tree layout, system dependency graph, tick processing order, signal wiring map, data flow rules, entity identity model, simulation update semantics, and recurring code patterns. Every implementation task should reference this document to understand how systems connect and how to build new components.

Style guide = "how things look." Glossary = "what to call things." **Architecture = "how systems connect and how to build new ones."**

---

## 1. Scene Tree Layout

The game scene uses a three-layer architecture under a root node. Each layer has a strict responsibility boundary.

```
Main (Node) — orchestrates init, behavioral signal wiring, HUD, input
│
├── ConsoleLogger (Node) — logging-only signal observation
│
├── SimulationLayer (Node)
│   ├── SimulationOrchestrator    — tick driver, calls process_tick() on all systems
│   ├── ...                       — registered systems in tick order
│
├── WorldLayer (Node2D/Node3D) — camera-relative visual renderers
│   ├── ...                       — renderers, overlays, effects
│
└── UILayer (CanvasLayer) — screen-space HUD and panels
    ├── ...                       — HUD elements, panels, overlays
```

**Layer boundaries:**
- **SimulationLayer** — pure data and logic. No rendering, no UI, no input handling.
- **WorldLayer** — reads simulation data, renders to screen. No simulation writes.
- **UILayer** — reads simulation data, presents to player. Sends commands via intent objects.

### System Representation

<!-- Explicitly state how systems exist at runtime. Are they:
  - Scene tree nodes (children of SimulationLayer)?
  - Pure C++/script objects owned by the orchestrator?
  - Autoloads?
  - Hybrids (node in tree but logic in a separate object)?

This affects lifecycle, dependency access, signal wiring, and testing. Be explicit. -->

Systems are [nodes / objects / autoloads / hybrids] — describe the concrete representation and why.

---

## 2. System Dependency Graph

Systems are organized into tiers. A system may only depend on systems in the same or lower tier. No upward dependencies.

### Tier Definitions

| Tier | Meaning |
|------|---------|
| 0 | Data stores — no tick, no dependencies |
| 1 | Primary producers — tick independently |
| 2 | Consumers of Tier 0–1 data |
| 3 | Higher-order consumers |
| ... | Continue as needed |

**What tiering governs:**
- **Dependency direction** — a system may only depend on systems in the same or lower tier.
- **Data consumption** — higher-tier systems consume data produced by lower tiers.

**What tiering does NOT govern:**
- **Tick order** — systems in the same tier may still require explicit ordering if they share freshness constraints. Tick order is defined separately in Section 3.
- **Authority** — tiering does not imply ownership. A Tier 0 data store may be written by a Tier 2 system if authority.md says so.

### Dependencies

| System | Tier | Depends On | Notes |
|--------|------|------------|-------|
| ... | ... | ... | ... |

---

## 3. Tick Processing Order

Systems are ticked in a fixed order by SimulationOrchestrator. Order determines data freshness — earlier systems see stale data from later systems (one-tick delay).

| Position | System | Justification |
|----------|--------|---------------|
| 1 | ... | ... |

**Ordering principles:**
- Time/clock first — everything else depends on elapsed time.
- State producers before consumers.
- Need satisfaction before task assignment.
- Emergency detection after all state updates.

### Simulation Update Semantics

<!-- This section defines the timing model for the simulation. These decisions affect every system and are among the most important architectural choices. Fill all of these. -->

- **Timestep model:** [Fixed timestep / Variable timestep / Fixed with interpolation]. Describe how simulation time advances relative to real time.
- **Signal dispatch timing:** [Immediate / Deferred / Queued]. When a system emits a signal, does the consumer execute immediately (within the emitter's tick), or is the signal queued for a later phase?
- **Same-tick cascading:** [Allowed / Forbidden]. Can a signal triggered during System A's tick cause System B to run logic before System B's own tick position? If allowed, what are the limits?
- **Intent/command processing:** [Within tick / Separate phase / Next tick]. When does the simulation process player commands and intent objects?
- **Data freshness rule:** A system ticked at position N sees position N-1's data from this tick, but position N+1's data from the previous tick. [Confirm or override this default.]
- **Deferred work:** [Supported / Not supported]. Can systems request work to be executed after all ticks complete (post-tick phase)?

---

## 4. Signal Wiring Map

Two categories of signal wiring exist:

### Behavioral Signals (game_manager)

Behavioral signals trigger gameplay-relevant side effects. Wired in the designated orchestrator.

| Signal | Source | Target | Purpose |
|--------|--------|--------|---------|
| ... | ... | ... | ... |

### Logging Signals (console_logger)

Logging signals are observe-only. Wired in the designated logger. No simulation effect.

| Signal | Source | Purpose |
|--------|--------|---------|
| ... | ... | ... |

---

## 5. Data Flow Rules

These rules govern how data moves through the system. Violating these rules creates hidden coupling and bugs.

<!-- Fill these with project-specific positive rules. Each rule should explain WHAT to do and WHY. The numbered rules below are common starting points — adapt or replace as needed. -->

### Rule 1: Systems publish state through query APIs

Systems expose their owned state through read-only query methods. Other systems and UI call these methods to access data. No direct field access across system boundaries.

### Rule 2: Commands enter simulation as intent objects or sanctioned setter APIs

External input (player commands, UI actions) enters the simulation layer through published setter APIs or intent objects defined in interfaces.md. No system accepts commands through ad hoc channels.

### Rule 3: Signals communicate occurrence, not ownership

Signals report that something happened (past tense). They do not transfer ownership of data. The emitter remains the authority. Consumers react to the event but do not cache the payload as a source of truth.

### Rule 4: Query APIs are read-only and side-effect free

A `get_*()` method must not modify state, emit signals, or trigger transitions. It returns the current value and nothing else.

### Rule 5: Cached or derived views must be reconstructible from authoritative state

Any cache, index, or derived data structure must be rebuildable from the authoritative source at any time. If a cache diverges, the cache is wrong — not the authority.

### Rule 6: Single writer per variable

Per authority.md, every piece of game data has exactly one owning system. No system may write to another system's data without an ADR. Readers are documented in the authority table.

### Rule 7: Signal wiring in designated locations only

Cross-system behavioral signal connections happen in the designated orchestrator. Logging-only signal connections happen in the designated logger. Systems may connect to their own required dependency's signals in their own initialization. No other wiring locations are permitted.

### Forbidden Patterns

These are the red-line violations of the rules above. Each is the negative-space counterpart of a positive rule. If code does any of these, it is an architecture bug — not a style preference.

1. **No cross-system state mutation.** A system must not directly write to another system's owned state. All cross-system effects flow through signals, intent objects, or sanctioned query/setter APIs defined by interfaces.md.
2. **No undeclared second authority.** Derived or cached state must not become an independent source of truth. If a cache diverges from the authoritative system, the cache is wrong. Every piece of mutable state has exactly one writer (authority.md).
3. **No ad hoc direct calls bypassing interfaces/signals.** Systems must not form private communication channels outside the registered signal and interface contracts.
4. **No hidden bidirectional write loops.** If System A writes to System B's state and System B writes to System A's state, that is a dependency cycle. One direction must be converted to a signal or the ownership consolidated.
5. **No implicit state transitions.** Every discrete state change must be declared in state-transitions.md with its trigger and authority.
6. **No UI writes to simulation state.** UI may read through query APIs and request changes through setter APIs or intent objects. UI must never directly mutate simulation data.
7. **No signal wiring outside designated locations.** Behavioral signals are wired in their designated orchestrator. Logging signals are wired in their designated logger. No other wiring locations are permitted.

---

## 6. Initialization & Boot Order

<!-- Define the startup sequence: who initializes first, who wires signals, when systems become live and ready to process ticks. This prevents hidden initialization races. -->

### Boot Sequence

| Phase | What Happens | Who Runs It |
|-------|-------------|-------------|
| 1 | ... | ... |

<!-- Common phases: scene tree construction → system _ready() calls → signal wiring → data loading → first tick. Define the concrete order for your project. -->

### Initialization Rules

- Systems must not call other systems during their own `_ready()` unless the dependency is guaranteed to be initialized first (lower scene tree position).
- Signal wiring happens [in orchestrator _ready() / after all systems _ready() / in a dedicated init phase].
- Systems must not emit signals during initialization — the first tick is the earliest safe point.
- [Add project-specific init rules as they emerge.]

---

## 7. Entity Identity & References

<!-- This section defines how entities are identified, referenced, and validated at runtime and across save/load boundaries. This is one of the most important architecture topics in simulation games — get it wrong and stale references corrupt the entire simulation. -->

### Runtime Identity

- **Handle format:** [Describe the concrete reference type — e.g., `EntityHandle {index, generation}`, bare integer ID, UUID, etc.]
- **Uniqueness scope:** [Globally unique / Per-entity-type / Map-local]
- **Handle invalidation:** [How stale references are detected — e.g., generation mismatch, null check, validity flag]
- **Reuse policy:** [Are slot indices reused after entity destruction? If so, how is stale reference detection guaranteed?]

### Persistent Identity

- **Save format:** [How entity references are serialized — e.g., `{index, generation}` pairs, string IDs, UUIDs]
- **Load validation:** [How references are validated on load — e.g., generation check, existence check, migration]
- **Cross-reference survival:** [What happens when a referenced entity doesn't exist on load — e.g., null out, reconstruct, fail]

### Content Identity

- **Content ID format:** [How game content types (items, structures, recipes, traits) are identified — e.g., namespaced string IDs `core:iron_ore`, enum values, integer keys]
- **Runtime resolution:** [How string/external IDs map to compact runtime IDs for performance]
- **Mod extensibility:** [Whether the ID scheme supports external content additions]

### How Systems Reference Entities

- Systems hold [handles / IDs / direct pointers] to entities they interact with.
- References are validated [every access / once per tick / on use] via [generation check / validity query / etc.].
- Stale references are handled by [returning null/invalid / logging warning / auto-cleanup].

---

## 8. Failure & Recovery Patterns

<!-- Define what happens when things go wrong at the architecture level. This section prevents ad hoc error handling that creates hidden coupling. -->

### Missing Dependency

- If a required system dependency is null at tick time: [skip tick with warning / crash / degrade gracefully].
- If an optional system dependency is null: [skip that integration path / use default values].

### Stale Reference

- If a system holds a reference to a destroyed entity: [detected by generation mismatch / null check / validity query].
- Recovery: [null out the reference / remove from tracking list / log warning and continue].

### Invalid State

- If a system detects an entity in an impossible state (not in state-transitions.md): [log diagnostic warning / force to safe state / crash in debug].
- If a state invariant is violated: [emit diagnostic / attempt self-heal / escalate to emergency system].

### Data Corruption on Load

- If a saved reference points to a non-existent entity: [null out / reconstruct / fail load].
- If a saved enum has an unrecognized value: [use default / skip entity / fail load].

<!-- Add project-specific failure patterns as they emerge. Each pattern should describe: the failure, detection mechanism, recovery action, and whether it's silent or logged. -->

---

## 9. Code Patterns

Recurring implementation patterns used across the codebase.

### Pattern: [Name]

**When to use:** ...
**Structure:** ...
**Example:** ...

<!-- Add patterns as they emerge. Each pattern should have: name, when to use, structure/template, and a concrete example. Common patterns include:
  - Entity Storage Pattern (pool/array/ECS with handle validation)
  - Content Registry Pattern (string ID → runtime ID mapping)
  - Serialization Pattern (save/load pipeline)
  - UI Panel Pattern (how panels connect to simulation data)
  - Task Pattern (how task types are defined and processed)
-->

---

## Rules

1. **This document describes HOW systems connect.** What systems do is in `design/systems/SYS-###`. What data they own is in `design/authority.md`. What signals they use is in `reference/signal-registry.md`.
2. **Tick order is canonical.** If code processes systems in a different order than this document, the code is wrong.
3. **Dependency direction is downward only.** Higher-tier systems depend on lower tiers. Never the reverse.
4. **Signal categories are strict.** Behavioral signals in their orchestrator, logging signals in their logger. No mixing.
5. **New systems must be registered** in the Scene Tree Layout, Dependency Graph, Tick Order (if ticked), and Signal Wiring sections before implementation begins.
6. **Forbidden Patterns are absolute.** The Forbidden Patterns section defines architecture bugs, not style preferences. Code that matches a forbidden pattern must be fixed regardless of whether it "works."
7. **Simulation Update Semantics are binding.** The timing model (signal dispatch, cascading, freshness) governs all system implementations. If code assumes different timing, the code is wrong.
