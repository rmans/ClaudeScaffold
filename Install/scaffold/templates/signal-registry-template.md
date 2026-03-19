# Signal Registry

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** [design/interfaces.md](../design/interfaces.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft

---

## Purpose

Master registry of all cross-system signals and intent objects. Every signal that crosses a system boundary is registered here with its name, payload, emitter, and consumers. Implementation code must match these definitions exactly.

## Signals

<!-- Signals are past-tense notifications: they report what already happened. Emitters fire them after completing an action. Consumers react to them.

Level column classifies the signal's scope:
  - Entity: Affects a single entity (colonist, structure, item)
  - Room: Affects a room or spatial region
  - System: Affects an entire system's state
  - Colony: Affects colony-wide state
  - Global: Affects world/game-level state
-->

| Signal Name | Level | Payload | Emitter | Consumer(s) | Delivery Expectation | Gameplay / Logging | Notes |
|-------------|-------|---------|---------|-------------|----------------------|--------------------| ------|
| ... | Entity / Room / System / Colony / Global | { field, field, ... } | SYS-### SystemName | SYS-###, SYS-###, UI | fire-and-forget / reliable / deduped / queued | Gameplay / Logging / Both | When it fires, why it matters |

<!-- Delivery Expectation values:
  - fire-and-forget: Signal is emitted once. If no consumer is connected, it is lost. No retry.
  - reliable: Signal must be delivered to all registered consumers. Framework guarantees delivery.
  - deduped: Multiple emissions within the same tick are collapsed into one delivery.
  - queued: Signal is placed in a queue and processed in order during the consumer's next processing pass.

Gameplay / Logging values:
  - Gameplay: This signal drives simulation behavior — a consumer makes gameplay decisions based on it.
  - Logging: This signal exists for telemetry, debug output, or analytics only. No gameplay consequences.
  - Both: Used for both gameplay decisions and logging/telemetry.
-->

---

## Intent Objects

<!-- Intent objects are noun-form requests: they describe what a system WANTS to happen. The receiving system decides whether and how to act on the request. Intent objects are not signals — they flow through method calls or queues, not through the signal bus. -->

| Intent Object | Payload | Requester | Handler | Delivery Expectation | Notes |
|---------------|---------|-----------|---------|----------------------|-------|
| ... | { field, field, ... } | SYS-### SystemName | SYS-### SystemName | fire-and-forget / reliable / deduped / queued | When it's created, what it requests |

---

## Dispatch Timing Conventions

<!-- Define when signals are dispatched relative to the simulation tick. This section establishes project-wide conventions so that individual signal entries don't need to repeat timing rationale. -->

| Timing Slot | When It Fires | Use For |
|-------------|---------------|---------|
| During tick | Inline, as the emitting system processes its tick | State changes that consumers need to react to within the same tick |
| End of tick | After all systems have processed, during the post-tick phase | Aggregate notifications, batch updates, UI refresh triggers |
| Deferred | Queued and dispatched at the start of the next tick | Cross-system requests that must not interrupt the current tick's processing |

<!-- Adjust these slots to match your engine's tick architecture. Reference engine/godot4-tick-order.md or equivalent. -->

---

## Payload Schema Conventions

<!-- Define project-wide conventions for signal and intent payloads to ensure consistency. -->

- **Field naming:** snake_case, matching the field names in entity-components.md where applicable.
- **Entity references:** Use the project's entity handle type (e.g., `EntityHandle`, `int entity_id`). Never pass raw pointers.
- **Positions:** Use `Vector2i` for grid positions, `Vector2` for world positions. Never mix coordinate spaces without documenting the transform.
- **Enums:** Use enum values from enums-and-statuses.md. Never pass raw integers for enum-typed fields.
- **Optional fields:** Mark nullable fields explicitly in the payload definition. Consumers must null-check these fields.
- **Payload size:** Keep payloads minimal. Pass entity IDs and let consumers query for additional data, rather than duplicating large data structures in the payload.

---

## Rules

1. **Every cross-system signal must be registered here.** If code emits a signal that another system consumes, it must appear in this document.
2. **Signals are past-tense.** Name signals as events that already happened: `structure_completed`, not `complete_structure`. Use `_changed`, `_created`, `_destroyed`, `_crossed`, etc.
3. **Intent objects are noun-form.** Name intents as requests: `sleep_request`, `hauling_request`. Not verbs, not past-tense.
4. **Payload fields must be concrete.** Use specific field names and types, not vague descriptions.
5. **Consumer list must be exhaustive.** Every system that connects to a signal must be listed. "UI" is an acceptable shorthand for all UI consumers.
6. **Conforms to interfaces.md.** If interfaces.md defines a data flow, the signal implementing it must be registered here. On conflict, interfaces.md wins (Rank 4 > Rank 6).
7. **Level classification is mandatory.** Every signal must have a Level indicating its scope.
