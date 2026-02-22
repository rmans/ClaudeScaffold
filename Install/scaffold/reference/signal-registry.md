# Signal Registry

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** [design/interfaces.md](../design/interfaces.md)

---

## Purpose

Master registry of all cross-system signals and intent objects. Every signal that crosses a system boundary is registered here with its name, payload, emitter, and consumers. Implementation code must match these definitions exactly.

## Signals

<!-- Add signals as systems are designed. One row per signal. -->

| Signal Name | Payload | Emitter | Consumer(s) | Notes |
|-------------|---------|---------|-------------|-------|
| *None yet* | — | — | — | — |

<!-- Example entries:
| building_placed       | { position, building_type, priority } | SYS-001 Construction | Pathfinding, Room Detection | Fired when player places a blueprint       |
| resource_changed      | { resource_type, old_amount, new_amount } | SYS-004 Resources | UI, Construction, Trading | Fired on any resource count change          |
| colonist_mood_changed | { colonist_id, old_mood, new_mood } | SYS-002 Needs & Mood | AI Behavior, UI | Fired when mood crosses a threshold         |
| colonist_downed       | { colonist_id, cause } | SYS-003 Health | Job Queue, AI Behavior | Fired when health reaches 0                 |
-->

## Intent Objects

<!-- Intent objects are requests that one system sends to another. Unlike signals (which are notifications), intents request action. -->

| Intent Name | Payload | Sender | Receiver | Notes |
|-------------|---------|--------|----------|-------|
| *None yet* | — | — | — | — |

<!-- Example entries:
| haul_request   | { item, from, to, priority }  | SYS-001 Construction | SYS-005 Job Queue | Request to move materials to a blueprint |
| rescue_request | { colonist_id, location }     | SYS-003 Health       | SYS-005 Job Queue | Request to rescue a downed colonist      |
-->

## Rules

1. **Every cross-system signal must be registered here.** No undocumented signals.
2. **Payloads are contracts.** Changing a payload shape requires updating all consumers and filing an ADR.
3. **Signals are notifications, intents are requests.** Signals say "this happened." Intents say "please do this." Don't conflate them.
4. **Naming convention:** `snake_case`, verb in past tense for signals (`building_placed`), noun for intents (`haul_request`).
