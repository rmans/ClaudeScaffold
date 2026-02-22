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

| Action ID | Description |
|-----------|-------------|
| `player_move_left` | Move left |
| `player_move_right` | Move right |
| `player_jump` | Jump |

-->

*TODO: Define canonical action IDs.*

## Rules

1. Action IDs use `snake_case` with a namespace prefix.
2. IDs are permanent — never rename, only deprecate and add new.
3. Every action must appear in at least one binding doc.
4. See [input-philosophy.md](input-philosophy.md) for design rationale.
