# Document Authority

> **Rule:** When documents conflict, the higher-ranked document wins. Lower documents must conform to higher documents. Code must never "work around" higher-level intent.

## Precedence Chain (highest wins)

| Rank | Document | Layer |
|------|----------|-------|
| 1 | [design/design-doc.md](design/design-doc.md) | Canon — core vision, non-negotiables |
| 2 | [design/style-guide.md](design/style-guide.md) | Canon — visual and code style |
| 2 | [design/color-system.md](design/color-system.md) | Canon — color palette and rules |
| 2 | [design/ui-kit.md](design/ui-kit.md) | Canon — UI component definitions |
| 2 | [design/glossary.md](design/glossary.md) | Canon — canonical terminology |
| 3 | [inputs/action-map.md](inputs/action-map.md) | Canon — canonical action IDs |
| 3 | [inputs/default-bindings-kbm.md](inputs/default-bindings-kbm.md) | Canon — keyboard/mouse bindings |
| 3 | [inputs/default-bindings-gamepad.md](inputs/default-bindings-gamepad.md) | Canon — gamepad bindings |
| 4 | [design/interfaces.md](design/interfaces.md) | Canon — system interface contracts |
| 4 | [design/authority.md](design/authority.md) | Canon — data authority table |
| 5 | design/systems/SYS-### | Canon — individual system designs |
| 5 | [design/state-transitions.md](design/state-transitions.md) | Canon — state machine definitions |
| 6 | reference/* | Reference — canonical data tables |
| 7 | phases/P#-### | Scope — phase gates |
| 8 | specs/SPEC-### | Behavior — atomic specs |
| 9 | tasks/TASK-### | Execution — implementation steps |
| 10 | engine/* | Implementation — Godot 4 constraints |
| 11 | theory/* | Reference only — never canonical |

## Rules

1. **No work-arounds.** If code would violate a higher-authority document, the code is wrong, not the document. Raise a decision (ADR) to change the document instead.
2. **No implicit overrides.** A lower document cannot silently redefine something from a higher document. Conflicts must be resolved explicitly via an ADR.
3. **Engine adapts to design.** The `engine/` layer describes *how* to implement, never *what* to implement. If an engine constraint conflicts with design intent, file an ADR.
4. **Theory is advisory.** Documents in `theory/` inform decisions but never dictate them. They carry no authority.
5. **IDs are stable.** Renaming a document does not change its authority rank — the rank is determined by its directory and type, not its filename.
