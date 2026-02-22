---
name: scaffold-review-engine
description: Review a single engine doc for completeness, quality, and consistency with design docs. Pick which doc to audit.
argument-hint: [coding|ui|input|scene-architecture|performance]
allowed-tools: Read, Grep, Glob
---

# Engine Document Review

Review a single engine document: **$ARGUMENTS**

## Supported Documents

| Argument | File Pattern |
|----------|-------------|
| `coding` | `scaffold/engine/[engine]-coding-best-practices.md` |
| `ui` | `scaffold/engine/[engine]-ui-best-practices.md` |
| `input` | `scaffold/engine/[engine]-input-system.md` |
| `scene-architecture` | `scaffold/engine/[engine]-scene-architecture.md` |
| `performance` | `scaffold/engine/[engine]-performance-budget.md` |

## Steps

### 1. Identify Target

1. Match the argument to a supported document above.
2. If no argument or unrecognized argument, list the options and ask the user which doc to review.
3. Glob `scaffold/engine/*` to find the actual file with the engine prefix.
4. If no engine docs exist, tell the user to run `/scaffold-bulk-seed-engine` first.

### 2. Read the Target Doc

Read the engine doc and assess its overall state — empty, partially filled, or populated.

### 3. Read Design Docs for Cross-Reference

Read the design docs relevant to the target:

- **coding** ← `design/design-doc.md` (overall architecture needs)
- **ui** ← `design/ui-kit.md` (component definitions, states, animation), `design/style-guide.md` (visual style), `design/color-system.md` (color tokens)
- **input** ← `inputs/action-map.md` (canonical actions), `inputs/input-philosophy.md` (responsiveness targets)
- **scene-architecture** ← `design/design-doc.md` (content structure, world design)
- **performance** ← `design/design-doc.md` (target platforms, scope)

### 4. Completeness Check

**coding** —
- Every section should have content beyond the TODO marker.
- Language Conventions should define naming, typing, and formatting rules.
- Event Patterns should define when to use events vs direct calls.
- Globals policy should be explicit about what is and isn't allowed in global scope.
- Project Overrides table should either have entries or be explicitly empty.

**ui** —
- UI Framework Components should map to the components defined in `design/ui-kit.md`.
- Theme/Styling should explain how to implement the color system and style guide.
- Layout System should support the layout rules in `design/ui-kit.md`.
- Focus and Navigation should implement the navigation rules in `inputs/ui-navigation.md`.
- Responsive Design should match the scaling approach in `design/ui-kit.md`.

**input** —
- Input System Configuration should map every action in `inputs/action-map.md` to engine constructs.
- Action Handling Patterns should be consistent with `inputs/input-philosophy.md`.
- Device Detection should cover all platforms listed in the design doc.
- Remapping should support the input philosophy's remapping requirements.

**scene-architecture** —
- Scene/Level Structure should support the content structure described in the design doc.
- Entity/Object Patterns should support the entities defined in system designs.
- Scene Transitions should handle all navigation patterns in the game.

**performance** —
- Target Specs should match the platforms listed in the design doc.
- Frame Budget should account for all systems (physics, rendering, scripts, AI).
- Memory Budget should be realistic for the target platform.
- Profiling should name specific tools available for the engine.

### 5. Quality Check

For all engine docs:
- **Engine-specific.** Content should use the engine's actual API names, classes, and patterns. Flag vague content that doesn't reference engine constructs.
- **No design-layer content.** Engine docs describe HOW, not WHAT. Flag any content that belongs in the design layer (player behavior, visual identity, game mechanics).
- **Project Overrides are justified.** Every override should have a rationale. Flag overrides without explanation.
- **Consistency with design docs.** Implementation approach should support — not contradict — the design intent.

## Output Format

```
## Engine Review: [Doc Name]

### Completeness: X/Y sections filled
[List each section with status: Complete, Partial, or Empty]

### Quality Issues
- [Specific issues with quotes]

### Design Doc Alignment
- [How well the implementation approach supports the design intent]

### Recommendations
1. [Most important fix]
2. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific — quote the exact text when flagging issues.
- If the doc is empty, don't just say "empty" — list what SHOULD be in it based on the engine and design docs.
- If no design docs are filled, review the engine doc on its own merits and note that design alignment can't be checked yet.
