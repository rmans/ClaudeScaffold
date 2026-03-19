# [Engine] — Input System

> **Layer:** Implementation
> **Authority:** Rank 9
> **Conforms to:** [inputs/action-map.md](../inputs/action-map.md), [inputs/input-philosophy.md](../inputs/input-philosophy.md)
> **Status:** Draft
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

## Purpose

<!-- Why this document exists. What decisions it captures and who should read it. -->

*TODO: Describe the purpose of this input-system document and its intended audience.*

## Input Layering Model

<!-- Define the input layers (e.g., gameplay, UI, debug, cinematic). Which layers are active in which game states. How layers stack and which layer consumes input first. -->

*TODO: Define the input layering model and layer priority.*

## Input Ownership

<!-- Which systems or nodes are allowed to read input. Rules preventing multiple consumers from acting on the same input event. Ownership transfer during state changes. -->

*TODO: Define input ownership rules.*

## Intent Conversion

<!-- How raw input events are converted into game intents (e.g., "mouse click on tile" becomes "select tile" intent). Where this conversion happens in the architecture. -->

*TODO: Define intent conversion rules and where conversion lives.*

## Routing Conventions

<!-- How input flows from the engine's input system to the consuming system. Direct polling vs event propagation vs action queries. Naming conventions for actions. -->

*TODO: Define input routing conventions.*

## Device Detection and Priority

<!-- How to detect active input device (keyboard, gamepad, touch). Priority rules when multiple devices are active. UI prompt switching based on active device. -->

*TODO: Define device detection and priority rules.*

## Remapping Policy

<!-- Runtime remapping support. Which actions are remappable. Persistence of remapped bindings. UI for remapping. Conflict resolution when bindings collide. -->

*TODO: Define remapping policy and implementation approach.*

## Pause-State Behavior

<!-- Which input actions remain active during pause. How input layers change when the game is paused. Menu navigation during pause. -->

*TODO: Define pause-state input behavior.*

## Debug Input Separation

<!-- How debug-only input actions are separated from gameplay input. Ensuring debug inputs are stripped from release builds or gated behind a flag. -->

*TODO: Define debug input separation rules.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
