# Action Map

> **Authority:** Rank 3
> **Layer:** Canon
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Status:** Draft

## Purpose

Canonical list of all input actions. These IDs are stable — code references them directly. Renaming an action ID is a breaking change that requires an ADR.

## Namespacing

Actions are namespaced by context: `player_`, `ui_`, `camera_`, `debug_`, etc.

## Actions

<!-- Define actions using this format:

### player_ (Player Actions)

| Action ID | Description | Source |
|-----------|-------------|--------|
| `player_move_left` | Move left | design-doc: Player Verbs |
| `player_move_right` | Move right | design-doc: Player Verbs |
| `player_jump` | Jump | interaction-model: Movement |

Source column traces each action to a specific design artifact (doc + section or concept).
Valid sources: design-doc (section), interaction-model (section), ui-kit (component), debug need, camera need.

-->

*TODO: Define canonical action IDs.*

## Rules

1. Action IDs use `snake_case` with a namespace prefix.
2. IDs are permanent — never rename, only deprecate and add new.
3. Every action must appear in at least one binding doc.
4. Every action must have a Source tracing it to a specific design artifact.
5. See [input-philosophy.md](input-philosophy.md) for design rationale.
