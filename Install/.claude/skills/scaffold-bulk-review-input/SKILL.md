---
name: scaffold-bulk-review-input
description: Review all input docs at once for completeness and cross-doc consistency. Use for a full audit of the input layer.
allowed-tools: Read, Grep, Glob
---

# Bulk Input Review

Review all Rank 3 input documents for completeness, accuracy, and cross-doc consistency.

## Documents Audited

| Doc | File |
|-----|------|
| Action Map | `scaffold/inputs/action-map.md` |
| Default Bindings KBM | `scaffold/inputs/default-bindings-kbm.md` |
| Default Bindings Gamepad | `scaffold/inputs/default-bindings-gamepad.md` |
| UI Navigation | `scaffold/inputs/ui-navigation.md` |
| Input Philosophy | `scaffold/inputs/input-philosophy.md` |

## Steps

### 1. Read Everything

1. Read all 5 documents listed above from `scaffold/inputs/`.
2. Read `scaffold/design/design-doc.md` for player verbs, core loop, and platform targets.
3. Read `scaffold/design/ui-kit.md` for UI component context.
4. Read `scaffold/design/systems/_index.md` to check system-action coverage.
5. If no input docs exist, report that and stop.

### 2. Per-Doc Completeness

For each document, assess:
- **Section count** — how many sections exist?
- **Filled sections** — how many have content beyond TODO markers?
- **Empty sections** — any sections still at template defaults?

Categorize each doc as: **Complete**, **Partial**, or **Empty**.

### 3. Cross-Doc Consistency

This is the main value of bulk review — checking relationships BETWEEN input docs:

- **Action Map <> Bindings KBM.** Every action in the action map must have a KBM binding. Flag actions without bindings and bindings referencing unknown actions.
- **Action Map <> Bindings Gamepad.** Same check for gamepad. Flag actions without bindings and bindings referencing unknown actions.
- **Action Map <> UI Navigation.** Actions with a `ui_` namespace should align with navigation actions defined in ui-navigation.md. Flag ui_ actions with no navigation rule and navigation rules referencing unknown actions.
- **Bindings KBM <> Bindings Gamepad.** Both should cover the same set of actions. Flag actions bound in one but not the other.
- **Input Philosophy <> All Docs.** Principles in input-philosophy should be reflected in the action map structure and binding choices. Flag contradictions (e.g., philosophy says "device-agnostic" but gamepad bindings are missing; philosophy says "no modifier combos" but KBM bindings use Ctrl+Shift chords).
- **Design Doc <> Action Map.** Player verbs and core loop actions in the design doc should have corresponding actions in the action map. Flag design doc actions with no input mapping.

### 4. Gap Analysis

Identify what's missing by cross-referencing all sources:

- Actions in the design doc with no action-map entry
- Actions in the action-map with no binding in either binding doc
- UI components in ui-kit.md with no navigation rules in ui-navigation.md
- Systems in `scaffold/design/systems/_index.md` that imply player input but have no corresponding actions
- Accessibility requirements in input-philosophy with no implementation path

### 5. Layer Boundary Check

Input docs must stay in their lane. Flag content that crosses layer boundaries:

- **Engine layer leaks** — content that describes HOW the engine handles input (InputEvent processing, action strength curves, dead zones as implementation values). These belong in `scaffold/engine/`.
- **Design/systems layer leaks** — content that defines game mechanics or behavior triggered by input (damage calculations, state machine transitions, ability cooldowns). These belong in `scaffold/design/systems/`.
- **Correct scope** — input docs define WHAT actions exist and how they map to physical controls. They may name the action and its context but must not describe what happens after the engine receives the action.

## Output Format

```
## Bulk Input Review — X docs audited

### Overview
| Doc | Status | Sections | Filled | Issues |
|-----|--------|----------|--------|--------|
| Action Map | Complete | 4 | 4 | 1 |
| Default Bindings KBM | Partial | 3 | 2 | 2 |
| ... | ... | ... | ... | ... |

### Cross-Doc Consistency
- **Action Map <> Bindings KBM:** [status — matches and mismatches]
- **Action Map <> Bindings Gamepad:** [status — matches and mismatches]
- **Action Map <> UI Navigation:** [status]
- **KBM <> Gamepad coverage:** [status — actions in one but not the other]
- **Philosophy <> All Docs:** [status — contradictions or alignment]
- **Design Doc <> Action Map:** [status — unmapped verbs]

### Gap Analysis
[List of missing coverage, organized by source]

### Layer Boundary Issues
[Any content that belongs in a different layer]

### Recommendations (prioritized)
1. [Highest-impact fix across all docs]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-doc consistency is the main value.** Individual completeness is what `/scaffold-review-input` does — bulk review focuses on relationships.
- Be specific. Name the exact sections and docs involved in every mismatch.
- If everything is consistent, say so. Don't manufacture issues.
- Prioritize by blast radius — issues affecting multiple docs rank higher.
- **Layer boundary enforcement is critical.** Input docs define actions and bindings, nothing more.
