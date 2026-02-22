# Inputs — Index

> **Layer:** Canon — Input control definitions.
> **Authority:** Rank 3 (action-map and bindings).

## Documents

| File | Purpose |
|------|---------|
| [action-map.md](action-map.md) | Canonical action IDs — stable, namespaced |
| [default-bindings-kbm.md](default-bindings-kbm.md) | Default keyboard + mouse bindings |
| [default-bindings-gamepad.md](default-bindings-gamepad.md) | Default gamepad bindings |
| [ui-navigation.md](ui-navigation.md) | UI navigation rules and focus flow |
| [input-philosophy.md](input-philosophy.md) | Input design principles |

## Rules

- Action IDs in [action-map.md](action-map.md) are canonical and stable.
- Binding docs define *defaults* — players may remap at runtime.
- Implementation details live in the engine input system doc (`engine/[engine]-input-system.md`).
