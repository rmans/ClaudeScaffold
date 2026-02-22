---
name: scaffold-review-input
description: Review a single input doc for completeness, quality, and consistency with design docs and other input docs.
argument-hint: [action-map|bindings-kbm|bindings-gamepad|ui-navigation|input-philosophy]
allowed-tools: Read, Grep, Glob
---

# Input Document Review

Review a single Rank 3 document: **$ARGUMENTS**

## Supported Documents

| Argument | File |
|----------|------|
| `action-map` | `scaffold/inputs/action-map.md` |
| `bindings-kbm` | `scaffold/inputs/default-bindings-kbm.md` |
| `bindings-gamepad` | `scaffold/inputs/default-bindings-gamepad.md` |
| `ui-navigation` | `scaffold/inputs/ui-navigation.md` |
| `input-philosophy` | `scaffold/inputs/input-philosophy.md` |

## Steps

### 1. Identify Target

1. Match the argument to a supported document above.
2. If no argument or unrecognized argument, list the options and ask the user which doc to review.
3. Confirm the file exists before proceeding.

### 2. Read the Target Doc

Read the target doc and assess its overall state — empty, partially filled, or populated.

### 3. Read Context Docs for Cross-Reference

Read the documents most relevant to the target:

- **action-map** ← `scaffold/design/design-doc.md` (player verbs, core loop), `scaffold/inputs/input-philosophy.md`
- **bindings-kbm** ← `scaffold/inputs/action-map.md` (must cover every action)
- **bindings-gamepad** ← `scaffold/inputs/action-map.md` (must cover every action)
- **ui-navigation** ← `scaffold/design/ui-kit.md` (components, layout), `scaffold/inputs/action-map.md` (ui_ actions)
- **input-philosophy** ← `scaffold/design/design-doc.md` (genre, feel, platforms)

### 4. Completeness Check

**action-map** —
- Namespaces should be defined (e.g., gameplay, ui, menu).
- Every namespace should list its actions with descriptions.
- A rules section should be filled covering action priority, conflict resolution, and context switching.
- Flag sections that are empty or say "TBD" without detail.

**bindings-kbm** —
- Every action in the action-map should have a keyboard/mouse binding.
- No key conflicts within the same context/namespace.
- Modifier usage (Shift, Ctrl, Alt) should be reasonable — not overloaded.
- Flag any actions from the action-map that are missing bindings.

**bindings-gamepad** —
- Every action in the action-map should have a gamepad binding.
- Generic button names should be used (e.g., "South Face Button" not "A button") for cross-platform support.
- No button conflicts within the same context/namespace.
- Flag any actions from the action-map that are missing bindings.

**ui-navigation** —
- A navigation model should be defined (cursor-based, focus-based, hybrid, etc.).
- Focus flow rules should describe how focus moves between UI elements.
- Navigation actions should map to actions defined in the action-map.
- Mouse/pointer behavior should be defined alongside keyboard/gamepad navigation.
- Flag sections that are empty or say "TBD" without detail.

**input-philosophy** —
- Core input principles should be defined (e.g., responsiveness, discoverability, consistency).
- Responsiveness targets should be set (e.g., max input latency, buffering rules).
- Accessibility requirements should be listed (e.g., rebinding support, one-handed play, hold-vs-toggle).
- Input constraints should be defined (e.g., simultaneous input limits, input priority rules).
- Flag sections that are empty or say "TBD" without detail.

### 5. Quality Check

For all input docs:

- **Design-layer only.** Input docs describe WHAT actions exist and how they map, not HOW the engine implements them. Flag any engine-specific content (node names, class names, API calls, signal names).
- **Action coverage.** Every action in the action-map should be referenced by at least one system design or binding doc. Flag orphaned actions that nothing references.
- **Naming consistency.** All action IDs should follow `snake_case` with a namespace prefix (e.g., `gameplay_jump`, `ui_confirm`). Flag deviations.
- **Cross-input consistency.** Binding docs should reference the same action IDs as the action-map. Flag mismatches — typos, renamed actions, or IDs that appear in bindings but not in the action-map (or vice versa).

## Output Format

```
## Input Review: [Doc Name]

### Completeness: X/Y sections filled
[List each section with status: Complete, Partial, or Empty]

### Quality Issues
- [Specific issues with quotes]

### Cross-Input Consistency
- [How well this doc aligns with other input docs]

### Design Doc Alignment
- [How well the input design supports the game design]

### Recommendations
1. [Most important fix]
2. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific — quote the exact text when flagging issues.
- If the doc is empty, don't just say "empty" — list what SHOULD be in it based on the design doc and other input docs.
- If no design docs are filled, review the doc on its own merits and note that design alignment cannot be checked.
