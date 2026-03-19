---
name: scaffold-fix-input
description: Mechanical cleanup pass for Step 6 input docs (action-map, input-philosophy, default-bindings-kbm, default-bindings-gamepad, ui-navigation). Auto-fixes structural issues, naming convention violations, binding collisions, cross-doc inconsistencies, and terminology drift. Detects design signals for adversarial review. Supports --target for single-doc focus.
argument-hint: [--target doc.md] [--iterate N]
allowed-tools: Read, Edit, Grep, Glob
---

# Fix Input

Mechanical cleanup and signal detection for Step 6 input docs: **$ARGUMENTS**

This skill is the **formatter and linter** for input docs — not the design reviewer. It normalizes structure, repairs mechanical inconsistencies across the 5 input docs and their upstream canon, and detects design signals. It does not interpret or resolve input design issues — that is the job of `iterate-input` (adversarial review) which runs immediately after this skill.

**What fix-input does:** normalize docs so adversarial review doesn't waste time on trivial issues.
**What fix-input does NOT do:** evaluate whether the input scheme is good, resolve binding philosophy disputes, or make UX decisions.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--target` | No | all | Target a single doc by filename (e.g., `--target action-map.md`, `--target ui-navigation.md`). When omitted, processes all 5 input docs. |
| `--iterate N` | No | `10` | Maximum review-fix passes before stopping. Stops early on convergence. |

### Valid --target values

| Target | Doc Path |
|--------|----------|
| `action-map.md` | `inputs/action-map.md` |
| `input-philosophy.md` | `inputs/input-philosophy.md` |
| `default-bindings-kbm.md` | `inputs/default-bindings-kbm.md` |
| `default-bindings-gamepad.md` | `inputs/default-bindings-gamepad.md` |
| `ui-navigation.md` | `inputs/ui-navigation.md` |

When `--target` is specified, cross-doc checks still run (reading other docs for consistency) but only the targeted doc is edited.

## Missing Doc Handling

If a target input doc does not exist, report it as **missing** in the per-doc status and do not attempt to create or edit it. Missing input docs are seeded by `/scaffold-bulk-seed-input`, not fix-input. Continue processing any remaining docs.

## Step 1 — Gather Context

Always read (regardless of `--target`):
1. `scaffold/design/design-doc.md` — Player Verbs, Core Loop, Input Feel, Accessibility targets.
2. `scaffold/design/interaction-model.md` — Rank 2 canon: what the player does. This is the primary upstream authority for input docs.
3. `scaffold/design/glossary.md` — canonical terminology.
4. `scaffold/doc-authority.md` — if present, for authority ranking. Proceed with standard rules if absent.
5. `scaffold/design/ui-kit.md` — if present, for component and screen references needed by ui-navigation.
6. `scaffold/design/feedback-system.md` — if present, for input-feedback alignment.
7. Accepted ADRs that reference input, actions, bindings, or navigation.
8. `scaffold/decisions/known-issues.md` — if present, for constraints affecting input.

Read the engine input doc as a constraint reference only:
9. Glob `scaffold/engine/*-input-system.md` — if present, for implementation constraints (context/layer model, remapping policy, pause behavior). Do not let engine details override Rank 2/3 canon.

Read all 5 input docs (even when targeting one — cross-doc consistency requires reading neighbors):
10. All files in `scaffold/inputs/` (excluding `_index.md`).

## Section Health Classification

For each section in each doc, classify its health:

| Health | Criteria |
|--------|---------|
| **Complete** | Substantive authored content — specific to this project, not template text |
| **Partial** | Some authored content but TODOs, placeholders, or template text remain |
| **Empty** | Only template/default text, or section heading with no content |

Report per-doc health as weighted percentage: Complete = 1.0, Partial = 0.5, Empty = 0. Health = `(sum of weights / total required sections) × 100`.

## Step 2 — Per-Doc Checks

### action-map.md

#### Section Structure
Required sections: Namespacing, Actions (with at least one namespace group), Rules.

#### Mechanical Checks
- **Namespace groups present** — at least `player_` and `ui_` groups defined. `camera_` and `debug_` recommended but not required.
- **Action ID naming convention** — every action ID uses lowercase `snake_case` with correct namespace prefix. Flag violations: camelCase, missing prefix, inconsistent separators.
- **Action ID uniqueness** — no duplicate action IDs across all namespaces.
- **Action descriptions present** — every action row has a non-empty Description column.
- **Design doc coverage** — every player verb from the design doc's Player Verbs section has a corresponding action. Flag missing verbs.
- **Interaction model coverage** — every player action described in the interaction model has a corresponding action ID. Flag gaps.
- **Traceability present** — every action has a traceable source: a design doc player verb, interaction model action, UI need, camera need, or debug need. Flag actions with no traceable source. This is the mechanical enforcement of the seed skill's "every action must trace to design canon" rule.
- **Traceability structure** — every action row must include a Source column referencing a specific design artifact in the format `doc-name: section/concept` (e.g., `design-doc: Player Verbs`, `interaction-model: Selection Model`). Flag rows with missing, empty, or inconsistently formatted Source fields. The Source column must exist in the table header — if missing, add it as an auto-fix.
- **Binding coverage** — every non-excluded action ID appears in at least one binding doc (KBM or gamepad). Exclusions (e.g., debug-only actions not mapped to gamepad, UI-only actions without KBM bindings) must be explicitly documented in the bindings doc or input-philosophy. Flag silently unbound actions.
- **Stale deprecated actions** — actions marked as deprecated still have binding entries (should be removed from bindings).
- **Terminology compliance** — glossary canonical terms used in descriptions.
- **Template text / TODOs** — no remaining placeholder content in populated sections.

#### Design Signals
- **Missing player verb** — design doc or interaction model describes a verb with no action ID.
- **Namespace confusion** — actions that appear to be in the wrong namespace (e.g., a camera action in `player_`, a UI action in `debug_`).
- **Action bloat** — action IDs that don't trace to any player verb, UI need, camera need, or debug need in design canon.

---

### input-philosophy.md

#### Section Structure
Required sections: Principles, Responsiveness, Accessibility, Constraints.

#### Mechanical Checks
- **Principles populated** — at least 3 concrete principles, not template text.
- **Responsiveness targets concrete** — at least one numeric target stated (latency, buffering window, etc.), not just "fast."
- **Accessibility section populated** — at least 3 concrete accessibility requirements, not template text.
- **Constraints section populated** — at least 1 hard constraint stated.
- **Design doc alignment** — principles trace to design doc Input Feel and Accessibility sections. Flag contradictions.
- **Interaction model alignment** — philosophy principles are consistent with interaction model's approach (e.g., if interaction model uses drag-select, philosophy shouldn't say "no hold actions").
- **Engine constraint awareness** — if the engine input doc exists, philosophy doesn't promise features the engine doc says aren't feasible. Flag contradictions as design signals, not auto-fixes.
- **Terminology compliance.**
- **Template text / TODOs.**

#### Design Signals
- **Philosophy-interaction mismatch** — philosophy states a principle that contradicts interaction model behavior.
- **Accessibility gap** — interaction model uses hold/drag/chord patterns but philosophy doesn't address toggle alternatives.
- **Engine constraint conflict** — philosophy promises input behavior the engine doc flags as problematic.

---

### default-bindings-kbm.md

#### Section Structure
Required sections: Bindings (with at least one namespace group), Rules.

#### Mechanical Checks
- **Complete action coverage** — every action in action-map.md has a KBM binding. Flag missing bindings.
- **No orphan bindings** — every binding references an action ID that exists in action-map.md. Flag orphan bindings.
- **Context-aware collision detection** — flag duplicate key assignments that are ambiguous within the same active input context. Do not flag overlaps that are clearly separated by namespace, screen, or mode (e.g., `debug_` and `player_` may share keys if mutually exclusive).
- **Modifier discipline** — flag if a majority of actions within a namespace require multi-key modifiers, or if core gameplay actions (`player_`) require modifiers without strong justification. Ctrl+Shift+Alt triple-modifiers are always flagged regardless of count.
- **Namespace grouping** — bindings are grouped by namespace, matching action-map grouping.
- **Key names standardized** — consistent key naming (e.g., "Space" not "Spacebar", "Ctrl" not "Control").
- **Terminology compliance.**
- **Template text / TODOs.**

#### Design Signals
- **Heavy modifier usage** — many actions require modifiers, suggesting the action space may be too large for available keys.
- **Accessibility concern** — bindings require simultaneous key presses but input-philosophy says "no chords."
- **Missing one-handed support** — if philosophy mentions one-handed play, check that core actions are reachable with one hand.

---

### default-bindings-gamepad.md

#### Section Structure
Required sections: Bindings (with at least one namespace group), Rules.

#### Mechanical Checks
- **Complete action coverage** — every action in action-map.md that is gamepad-relevant has a binding. UI-only or debug-only actions may be excluded if input-philosophy says gamepad doesn't need them — but this must be explicit, not silent.
- **No orphan bindings** — every binding references an action ID that exists in action-map.md.
- **Context-aware collision detection** — same rules as KBM: flag ambiguous same-context duplicates, allow cross-context sharing.
- **Button naming standardized** — consistent button naming (e.g., "A/Cross" or "RB/R1" using a clear convention).
- **Namespace grouping** — matches action-map.
- **Terminology compliance.**
- **Template text / TODOs.**

#### Design Signals
- **Missing gamepad coverage** — philosophy says "device-agnostic" but some player actions have no gamepad binding.
- **Button exhaustion** — more actions assigned than available buttons, suggesting context-switching or combined inputs are needed but not documented.

---

### ui-navigation.md

#### Section Structure
Required sections: Navigation Model, Focus Flow, Navigation Actions, Mouse Behavior.

#### Mechanical Checks
- **Navigation model stated** — spatial, tab-order, or hybrid explicitly chosen, not "TBD."
- **Focus flow rules present** — at least 1 concrete rule about initial focus and focus movement.
- **Navigation actions reference action-map** — `ui_` actions used in navigation are defined in action-map.md. Flag missing action IDs.
- **Navigation action completeness** — all `ui_` navigation actions defined in action-map (e.g., `ui_confirm`, `ui_cancel`, `ui_navigate_*`) are used or referenced in ui-navigation.md. Flag unused navigation actions.
- **UI-kit alignment** — if ui-kit exists, navigation references components that exist in ui-kit. Flag references to undefined components.
- **Interaction model alignment** — navigation model is consistent with interaction model's selection/command model. Flag contradictions.
- **Mouse behavior defined** — at least hover, click, and cursor visibility addressed.
- **Accessibility considerations** — navigation supports keyboard-only and gamepad-only traversal if input-philosophy requires it.
- **Terminology compliance.**
- **Template text / TODOs.**

#### Design Signals
- **Navigation model conflict** — ui-navigation says "spatial" but interaction model implies tab-order, or vice versa.
- **Component gap** — navigation references screens or panels not defined in ui-kit.
- **Gamepad navigation gap** — navigation model doesn't address gamepad at all but philosophy says "device-agnostic."

---

## Step 3 — Classify Issues

### Auto-Fixable (apply immediately)

| Category | Fix | Condition |
|----------|-----|-----------|
| **Template text / TODOs** | Remove placeholder text in populated sections | Section has authored content beyond template markers |
| **Terminology drift** | Replace NOT-column terms with canonical terms | Used as authoritative terminology, not in examples/quotes |
| **Action ID normalization** | Fix casing/separator violations in action IDs | ID doesn't match `lowercase_snake_case` convention |
| **Key/button name normalization** | Standardize key and button names to consistent format | Inconsistent naming within same doc |
| **Namespace grouping** | Reorder binding tables to match action-map namespace groups | Bindings not grouped by namespace |
| **Orphan binding removal** | Remove binding rows that reference non-existent action IDs | Action ID not in action-map |
| **Stale deprecated cleanup** | Remove bindings for deprecated actions | Action marked deprecated in action-map |
| **Missing table columns** | Add column headers to match expected format | Table missing required columns |
| **Table structure normalization** | Align row structure to match header schema without altering authored values | Table rows have missing or extra columns vs header |
| **Index sync** | Update `inputs/_index.md` if doc list is stale | Index doesn't match existing docs |

Auto-fix may **not** invent:
- New action IDs, bindings, navigation flows, or philosophy principles
- Content for Empty sections — those are user-pending
- Bindings for actions that have no binding (flag as missing, don't invent keys)

### Mechanically Detected, User-Confirmed

| Category | Action |
|----------|--------|
| **Missing action coverage** | Player verb or interaction model action has no action ID. Report for human decision. |
| **Missing binding** | Action ID has no binding in one or both binding docs. Report for human decision. |
| **Binding collision** | Same-context duplicate assignment. Report with context analysis. |
| **Missing doc** | An input doc does not exist. Report for seeding via bulk-seed-input. |
| **Engine constraint conflict** | Philosophy promises something engine doc says isn't feasible. Report for human resolution. |

### Design Signals (for adversarial review)

These feed into `iterate-input`. Detected and reported, not resolved.

| Signal | Context |
|--------|---------|
| Missing player verb | Design doc verb has no action ID |
| Namespace confusion | Action appears to be in wrong namespace |
| Action bloat | Action doesn't trace to design canon |
| Philosophy-interaction mismatch | Philosophy contradicts interaction model |
| Accessibility gap | Hold/drag/chord used without toggle alternative |
| Heavy modifier usage | Excessive multi-key combinations |
| Button exhaustion | More gamepad actions than available buttons |
| Navigation model conflict | ui-navigation and interaction model disagree |
| Gamepad navigation gap | Navigation ignores gamepad despite "device-agnostic" philosophy |
| Component gap | Navigation references undefined UI components |

## Step 4 — Apply Auto-Fixes

**Safety rules:**
- **When `--target` is set, only edit the targeted doc.** Cross-doc mismatches are flagged but other docs are not edited.
- **When `--target` is not set, edit all 5 docs.** Cross-doc auto-fixes are limited to normalization only.
- **Never edit Step 1–5 docs.** Input docs never auto-edit design-doc, interaction-model, ui-kit, feedback-system, style docs, system designs, reference docs, or engine docs. Flag mismatches for human resolution.
- **Never change design decisions.** Only fix how clearly they're expressed and how consistently they're reflected.
- **Never invent actions or bindings.** Auto-fix normalizes what exists. Flag gaps for human decision.
- **No speculative fixes.** When multiple plausible interpretations exist, report instead of auto-fixing.
- **Authority flows from canon.** design-doc and interaction-model (Rank 2) → input docs (Rank 3). Engine docs are constraints, not authority. On mismatch between Rank 2 and Rank 3, the Rank 2 doc is canonical.

## Step 5 — Cross-Doc Pass

After all per-doc checks and fixes, run one cross-doc consistency pass:

1. **Action-map → KBM bindings** — every action has a KBM binding. No orphan bindings.
2. **Action-map → Gamepad bindings** — every gamepad-relevant action has a binding. Explicitly excluded actions are documented.
3. **Action-map → UI navigation** — `ui_` actions used in navigation exist in action-map.
4. **Action-map ↔ Interaction model** — action IDs cover all interaction model player actions. No action IDs lack an interaction model source (possible bloat).
5. **Action-map ↔ Design doc** — action IDs cover all player verbs. No player verbs lack an action ID.
6. **Input philosophy → Bindings** — philosophy constraints (e.g., "no chords", "one-handed play") are not violated by actual bindings.
7. **Input philosophy → UI navigation** — philosophy accessibility requirements (e.g., "keyboard-only navigation") are reflected in navigation model.
8. **Input philosophy ↔ Interaction model** — philosophy principles are consistent with interaction model behavior.
9. **UI navigation → UI-kit** — if ui-kit exists, navigation references components that are defined. Flag missing components.
10. **Bindings ↔ Engine input doc** — if engine input doc exists, only flag contradictions where input behavior explicitly depends on stated engine capabilities (simultaneous contexts, remapping limits, device support). Do not infer constraints not stated in the engine doc.

Cross-doc pass results:
- Auto-fixable alignment issues → applied (respecting `--target` scope)
- Design signals → reported for iterate-input

## Step 6 — Re-review and Iterate

After applying fixes, re-review. Continue iterating until:
- **Clean** — no issues remain.
- **Human-only** — only human-required issues and design signals remain.
- **Stable** — same issues persist across two consecutive passes (same doc, category, section).
- **Limit** — `--iterate N` reached.

## Step 7 — Report

```
## Fix-Input Summary

### Configuration
| Field | Value |
|-------|-------|
| Target | [all / specific doc] |
| Passes | N completed / M max [early stop: yes/no] |
| Auto-fixed | N issues |
| User-confirmed pending | N issues |
| Design signals | N issues |
| Final status | Clean / Human-only / Stable / Limit |

### Per-Doc Status
| Document | Health | Auto-fixed | User-pending | Design Signals | Status |
|----------|--------|-----------|-------------|----------------|--------|
| action-map.md | N% | N | N | N | Clean / Human-only / Missing |
| input-philosophy.md | N% | N | N | N | Clean / Human-only / Missing |
| default-bindings-kbm.md | N% | N | N | N | Clean / Human-only / Missing |
| default-bindings-gamepad.md | N% | N | N | N | Clean / Human-only / Missing |
| ui-navigation.md | N% | N | N | N | Clean / Human-only / Missing |

### Action Coverage
| Source | Actions in source | Actions in action-map | Gap |
|--------|------------------|----------------------|-----|
| Design doc Player Verbs | N | N | N missing |
| Interaction model actions | N | N | N missing |

### Binding Coverage
| Namespace | Actions | KBM bound | Gamepad bound | Unbound |
|-----------|---------|-----------|---------------|---------|
| player_ | N | N | N | N |
| ui_ | N | N | N | N |
| camera_ | N | N | N | N |
| debug_ | N | N | N | N |

### Flagged Same-Context Collisions
| Doc | Key/Button | Actions | Context | Resolution |
|-----|-----------|---------|---------|-----------|
[List collisions, or "None detected"]

### Auto-Fixes Applied
| # | Document | Category | What Changed |
|---|----------|----------|-------------|
| 1 | action-map.md | ID normalization | Renamed `playerJump` to `player_jump` |
| ... | ... | ... | ... |

### User-Confirmed Actions Pending
| # | Document | Category | Action Required |
|---|----------|----------|----------------|
| 1 | action-map.md | Missing verb | Design doc verb "assign" has no action ID |
| ... | ... | ... | ... |

### Design Signals (for iterate-input)
| # | Documents | Signal | Detail |
|---|----------|--------|--------|
| 1 | action-map, interaction-model | Action bloat | `player_whistle` has no interaction model source |
| ... | ... | ... | ... |

### Cross-Doc Consistency
| Check | Result | Issues |
|-------|--------|--------|
| Action-map → KBM | N issues | ... |
| Action-map → Gamepad | N issues | ... |
| Action-map ↔ Interaction model | N gaps | ... |
| Action-map ↔ Design doc | N gaps | ... |
| Philosophy → Bindings | N violations | ... |
| Philosophy → Navigation | N gaps | ... |
| Navigation → UI-kit | N gaps | ... |
```

Update each edited doc's `Last Updated` date and add **one** Changelog entry per doc per run: `- YYYY-MM-DD: Mechanical cleanup (fix-input).`

## Rules

- **This skill is a formatter and linter, not a design reviewer.** It normalizes docs and detects signals. Input design evaluation belongs to iterate-input.
- **Authority flows from design canon.** design-doc and interaction-model (Rank 2) govern input docs (Rank 3). On mismatch, the Rank 2 doc is canonical.
- **Engine docs are constraints, not authority.** Read the engine input doc to avoid contradictions, but never pull implementation detail upward into Rank 3 docs. Flag constraint conflicts as design signals.
- **--target restricts edits, not reads.** When targeting one doc, all 5 input docs and upstream docs are still read for cross-doc checks, but only the target is edited.
- **Never change design decisions.** Auto-fixes clarify expression and fix consistency. They never alter what the input scheme says.
- **Never edit Step 1–5 docs.** Input docs never auto-edit design-doc, interaction-model, ui-kit, feedback-system, style docs, system designs, reference docs, or engine docs.
- **Never invent actions or bindings.** Auto-fix normalizes what exists. Missing actions and bindings are flagged for human decision, not fabricated.
- **Missing docs are reported, not created.** If an input doc doesn't exist, report it and skip. Creation belongs to bulk-seed-input.
- **No speculative fixes.** When multiple plausible interpretations exist, report — do not auto-fix.
- **Binding collision checks are context-aware.** Not all duplicate assignments are conflicts. Actions in different namespaces, mutually exclusive contexts, or debug-only layers may legitimately share keys/buttons.
- **Action ID convention is enforced.** `lowercase_snake_case` with correct namespace prefix. Violations are auto-fixed.
- **Design signals are detected, not resolved.** Philosophy mismatches, coverage gaps, and bloat signals are reported for iterate-input.
- **Terminology fixes respect context.** Only replace NOT-column terms when used as authoritative terminology. Do not normalize terminology inside code blocks, examples, quoted text, or external references.
- **One changelog entry per doc per run.** Multiple passes that edit the same doc collapse into a single changelog entry.
