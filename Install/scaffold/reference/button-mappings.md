# Button Mappings

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** [inputs/action-map.md](../inputs/action-map.md)

---

## Purpose

Input mappings that connect physical buttons/keys to game actions. This is a stub until UI specs exist — once the game's interface is designed, this document maps every input to its action, context, and priority.

See also:
- [inputs/action-map.md](../inputs/action-map.md) — canonical action IDs
- [inputs/default-bindings-kbm.md](../inputs/default-bindings-kbm.md) — keyboard/mouse defaults
- [inputs/default-bindings-gamepad.md](../inputs/default-bindings-gamepad.md) — gamepad defaults

## Context-Sensitive Mappings

<!-- Input meaning changes based on context (e.g., "E" means "interact" in the world but "confirm" in a menu). Define those contexts here. -->

| Context | Description | Active When |
|---------|-------------|-------------|
| *None yet* | — | — |

<!-- Example:
| Gameplay  | Normal play — moving, interacting, building | Default context    |
| Menu      | Any menu is open                             | Menu overlay open  |
| Build     | Building mode — placing blueprints           | Build tool active  |
| Combat    | Direct combat control                        | Colonist drafted   |
-->

## Mappings

<!-- One table per context. -->

*None yet — stub until UI specs exist.*

<!-- Example:

### Gameplay Context

| Action | Keyboard/Mouse | Gamepad | Notes |
|--------|---------------|---------|-------|
| Select | Left click | A | Select entity under cursor |
| Move camera | WASD / Edge scroll | Left stick | |
| Zoom | Scroll wheel | Right trigger/bumper | |
| Open build menu | B | Y | Switches to Build context |
| Pause | Space | Start | Toggle pause |
| Speed 1x | 1 | D-pad left | |
| Speed 2x | 2 | D-pad up | |
| Speed 3x | 3 | D-pad right | |

-->

## Rules

1. **Every action must have both KBM and gamepad mappings** (if gamepad is supported).
2. **No input collisions within the same context.** The same button can mean different things in different contexts, but never two things in the same context.
3. **Canonical action IDs come from [inputs/action-map.md](../inputs/action-map.md).** This document maps buttons to those actions — it doesn't define new actions.
