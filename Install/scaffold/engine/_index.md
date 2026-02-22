# Engine — Index

> **Layer:** Implementation — How we build in the target engine.
> **Authority:** Rank 10. Engine docs adapt to design, never the reverse.

## Documents

Engine docs are seeded by a skill based on the selected engine. Once seeded, this directory contains:

| File | Topic |
|------|-------|
| `[engine]-coding-best-practices.md` | Language conventions, code organization |
| `[engine]-ui-best-practices.md` | UI implementation patterns |
| `[engine]-input-system.md` | Input system configuration, action handling |
| `[engine]-scene-architecture.md` | Scene tree design, object patterns |
| `[engine]-performance-budget.md` | Frame budget, optimization targets |

## Templates

Engine templates live in [templates/](../templates/_index.md):

| Template | Seeds |
|----------|-------|
| `engine-coding-template.md` | Coding best practices |
| `engine-ui-template.md` | UI best practices |
| `engine-input-template.md` | Input system |
| `engine-scene-architecture-template.md` | Scene architecture |
| `engine-performance-template.md` | Performance budget |

## Rules

- Engine docs describe *how* to implement, never *what* to implement.
- If an engine constraint conflicts with design intent, file an ADR — do not silently work around the design.
- Each doc has a **Project Overrides** section at the bottom for project-specific deviations from engine defaults.
