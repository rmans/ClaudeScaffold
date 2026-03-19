# Feedback System

> **Authority:** Rank 2
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md), [style-guide.md](style-guide.md), [color-system.md](color-system.md), [ui-kit.md](ui-kit.md), [audio-direction.md](audio-direction.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

This document defines **how the game responds to events and player actions** — the coordinated visual, audio, and UI response that creates game feel. It bridges the gap between interaction-model.md (what the player does) and the presentation docs (style-guide, ui-kit, audio-direction) by defining *when* and *how* feedback fires across all channels simultaneously.

<!-- This doc answers: "When X happens, what does the player see, hear, and read — and in what order?" Component-level feedback (what a button looks like when pressed) stays in ui-kit.md. Sound categories stay in audio-direction.md. This doc defines the coordination between them. -->

---

## Feedback Types

<!-- Define the categories of feedback the game produces. Each type has a different purpose, urgency, and presentation style. -->

### Action Confirmation

<!-- Player did something, system acknowledges it. Examples: structure placed, zone designated, task queued. What's the coordinated response? Visual + audio + UI status. How does the player know the action was received AND accepted? -->

### Action Failure

<!-- Player tried something that can't be done. Examples: not enough resources, invalid placement, colonist busy. What's the coordinated response? What specific information is shown (not just "failed" but why)? -->

### State Change Notification

<!-- Something changed in the simulation without direct player input. Examples: construction complete, colonist arrived, research finished. When does the player need to know? How prominent is the notification? -->

### Warning / Escalation

<!-- Something is going wrong and the player should act. Examples: food running low, colonist injured, power failing. How does warning escalate over time? What's the Pre-Failure Warning Contract (from design-doc)? -->

### Critical Alert

<!-- Something requires immediate attention. Examples: containment breach, colonist death, fire. What overrides what? Does the game auto-pause? What's the visual + audio + UI response? -->

### Selection / Hover

<!-- Player is inspecting the world. Examples: hovering over a colonist, selecting a structure, mousing over a zone. What feedback appears and how quickly? -->

### Sustained State

<!-- Ongoing conditions that persist over time. Examples: low food overlay, power outage visual, contamination warning. How do sustained states differ from transient events? Do they stack visually? -->

## Timing Rules

<!-- When does feedback appear relative to the triggering event? -->

### Instant vs Delayed

<!-- Which feedback types fire immediately (selection highlight, button press) vs which wait for simulation confirmation (structure placement, task assignment)? What's the maximum acceptable delay before the player thinks the game is broken? -->

### Sustained vs Transient

<!-- How long does feedback last? Transient = appears and fades (alert banner, placement sound). Sustained = persists until condition changes (low food icon, power warning overlay). What are the durations for transient feedback? -->

### Queued vs Immediate

<!-- When multiple feedback events fire on the same tick, do they all play simultaneously or queue? Which types queue (alerts) vs play immediately (action confirmation)? -->

## Priority & Stacking

<!-- When multiple feedback sources compete for the player's attention, which wins? -->

### Priority Hierarchy

<!-- Define the priority stack from highest to lowest. Example:
1. Critical alerts (containment breach, death)
2. Warning escalation (hunger, injury, power)
3. Action failure (can't place, can't build)
4. Action confirmation (placed, queued, assigned)
5. State change notification (built, arrived, researched)
6. Selection / hover feedback
7. Sustained state indicators
-->

### Visual Stacking

<!-- Can multiple visual feedback states coexist? Can a colonist show both "selected" and "injured" simultaneously? What happens when overlay colors conflict? -->

### Audio Stacking

<!-- Defined primarily in audio-direction.md — reference the priority ordering here. How many simultaneous feedback sounds? What gets ducked? -->

### Modal Interaction

<!-- How does feedback behave during modal states (build mode, zone painting, panel open)? Is non-modal feedback suppressed, dimmed, or unchanged? -->

## Cross-Modal Coordination

<!-- The core of this document: how visual + audio + UI work together. -->

### Coordination Rules

<!-- For each major event type, define what fires across all channels simultaneously. Example:
- Structure placed: placement sound (audio) + brief flash at position (visual) + "Built" status text (UI) — all within the same frame.
- Colonist death: death sting (audio) + screen flash (visual) + critical alert banner (UI) + auto-pause (game state) — all immediate.
-->

### Channel Responsibilities

<!-- Which channel carries which information?
- Audio: urgency, confirmation, ambient awareness
- Visual: location, state, identity
- UI: detail, numbers, actionable information
No channel should carry information that another channel doesn't at least reinforce. -->

### Redundancy Principle

<!-- Every critical piece of information must be conveyed through at least two channels (visual + audio, visual + UI, etc.). No single-channel-only information for gameplay-critical feedback. This is both a feel principle and an accessibility requirement. -->

## Event-Response Table

<!-- The practical reference table. For each major game event, define the complete coordinated response. -->

| Event | Visual | Audio | UI | Timing | Priority |
|-------|--------|-------|-----|--------|----------|
<!-- | Structure placed | Brief highlight at position | Placement sound | — | Instant | 4 |
| Construction complete | Structure sprite swap | Completion chime | Status notification | Instant | 5 |
| Colonist hungry | Hunger icon over head | — | Warning alert if below threshold | Sustained | 6 (icon) / 2 (alert) |
| Containment breach | Screen flash + alarm overlay | Breach siren | Critical alert banner + auto-pause | Instant | 1 |
-->

## Rules

1. <!-- No silent events — every player-visible state change produces feedback through at least one channel. -->
2. <!-- Critical alerts override all other feedback — visual, audio, and UI. -->
3. <!-- Action failures are specific — "Not enough Steel (need 4, have 2)" not "Cannot build." -->
4. <!-- Feedback timing matches player expectation — instant for direct actions, brief delay acceptable for simulation-confirmed results. -->
5. <!-- Sustained feedback never blocks transient feedback — ongoing indicators coexist with momentary events. -->
6. <!-- Two-channel minimum for gameplay-critical information — no single-channel-only feedback for things the player must know. -->
7. <!-- Feedback priority is absolute — a Priority 1 event always takes precedence, regardless of what else is happening. -->
