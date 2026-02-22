# Design — Index

> **Layer:** Canon — What the game is.
> **Authority:** Highest. All other layers conform to design.

## Documents

| File | Purpose |
|------|---------|
| [design-doc.md](design-doc.md) | Core vision, non-negotiables (rank 1) |
| [style-guide.md](style-guide.md) | Visual art style — art direction, tone, rendering, VFX, animation (rank 2) |
| [color-system.md](color-system.md) | Color palette, tokens, usage rules, accessibility (rank 2) |
| [ui-kit.md](ui-kit.md) | UI components, layout, typography, animation, sound, scaling (rank 2) |
| [glossary.md](glossary.md) | Canonical terminology — term, definition, NOT column (rank 2) |
| [interfaces.md](interfaces.md) | System interface contracts (rank 4) |
| [authority.md](authority.md) | Data authority — who writes what variable, readers, cadence (rank 4) |
| [state-transitions.md](state-transitions.md) | All state machines — states, transitions, triggers, authority (rank 5) |

## Systems

Individual system designs live in [systems/](systems/_index.md) using the SYS-### ID format.

## Adding Documents

- Design-layer docs define *what the game is*, never *how it's built*.
- New system designs use the [system template](../templates/system-template.md).
- Register new systems in [systems/_index.md](systems/_index.md).
