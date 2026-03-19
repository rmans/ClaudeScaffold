# SYS-### — [System Name]

> **Authority:** Rank 5
> **Layer:** Canon
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft
> **Changelog:**

---

## Purpose

<!-- One sentence: what player-visible behavior does this system own? Not implementation — what the player experiences because this system exists. -->

## Simulation Responsibility

<!-- What state does this system uniquely own and update? This is the system's reason for existing — if no other system can own this state, this system must. -->

## Player Intent

<!-- What is the player trying to accomplish when they engage with this system? Bullet list. -->

## Design Constraints

<!-- Which Design Invariants, Decision Anchors, Design Boundaries, or Control Model rules constrain this system? Reference by name.

Example:
- Invariant: IndirectControl — colonists cannot be directly commanded
- Boundary: no micromanagement of individual colonist needs
- Control Model: player influences through policy, not direct orders -->

## Visibility to Player

<!-- What parts of this system are visible, partially visible, or hidden from the player? What must the player understand to make good decisions? Connects to the Player Information Model in the design doc.

| State/Behavior | Visibility | Why |
|---------------|-----------|-----|
| ... | Visible / Partial / Hidden | ... | -->

## Player Actions

<!-- Step by step, what does the player actually do? Write this as a numbered sequence of observable actions. No implementation details — only what the player sees and does. -->

1. ...
2. ...
3. ...

## System Resolution

<!-- What happens after the player acts? How does the game world respond? Describe the chain of visible consequences. -->

1. ...
2. ...
3. ...

## State Lifecycle

<!-- What are the major states this system can be in, and how does it move between them from the player's perspective? Not implementation state machines — player-observable phases.

Example: Planned → Under Construction → Active → Damaged → Destroyed
Example: Idle → Triggered → Recovering → Resolved -->

## Failure / Friction States

<!-- What can go wrong? What does the player see when things stall, break, or fail? How does the game communicate the problem? -->

- ...

## Owned State

<!-- What gameplay/runtime state does this system exclusively own? Only this system may write to these. Other systems may read them. List gameplay state only — not caches, scene nodes, engine objects, service locators, or data-structure choices.

| State | Description | Persistence |
|-------|-------------|-------------|
| ... | ... | Runtime / Saved / Derived | -->

## Upstream Dependencies

<!-- What other systems does this one require to function? Describe at the design level (not signals/methods — those belong in interfaces.md and signal-registry.md). -->

| Source System | What It Provides |
|---------------|------------------|
| ... | ... |

## Downstream Consequences

<!-- What does this system feed OUT to other systems? What ripple effects does it create? -->

| Target System | What It Receives |
|---------------|------------------|
| ... | ... |

## Non-Responsibilities

<!-- What this system explicitly does NOT own. Prevents scope creep. Be specific — name the system that DOES own it if possible. -->

- ...

## Edge Cases & Ambiguity Killers

<!-- Questions a player or implementer would naturally ask. Answer them here so the design is unambiguous. Include exceptions and boundary conditions. -->

- *Can I...?*
- *What happens if...?*

## Feel & Feedback

<!-- How should this system feel to use? What's the feedback language? What makes it satisfying? Describe only system-specific feel requirements. Detailed visual/audio style belongs to Step 4 docs (style-guide, audio-direction). -->

- ...

## Open Questions

<!-- Unresolved design questions. Remove entries as they are resolved. -->

- ...
