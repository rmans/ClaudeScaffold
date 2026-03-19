---
name: scaffold-bulk-seed-input
description: Seed all 5 input docs from the design doc and interaction model. Action-map and philosophy derive from design canon in parallel; bindings derive from action-map; navigation derives from action-map + philosophy + ui-kit.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Input Documents from Design Doc

Read the completed design doc and interaction model to pre-fill action-map, input-philosophy, keyboard/mouse bindings, gamepad bindings, and UI navigation.

## Prerequisites

1. **Read the design doc** at `scaffold/design/design-doc.md`.
2. **Read the interaction model** at `scaffold/design/interaction-model.md`. This is the Rank 2 canon document that defines how the player interacts with the game — action-map, bindings, and navigation all derive from it. If this file does not exist, stop and tell the user to create it first (via `/scaffold-bulk-seed-style` or the interaction-model template).
3. **If present, read the engine input doc** — Glob `scaffold/engine/*-input-system.md`. Use only as an implementation constraint reference — do not let engine details override Rank 2/3 canon. If the engine input doc does not exist, proceed without it.
4. **If present, read `scaffold/doc-authority.md`** to confirm parent/child influence boundaries. If absent, proceed using standard scaffold authority rules (Rank 2 interaction-model governs Rank 3 input docs).
5. **Verify the design doc is sufficiently filled out:**
   - **Required:** Player Verbs and Core Loop must have substantive content (not just TODO markers). If either is missing, stop and tell the user to run `/scaffold-init-design` first.
   - **Optional:** If Input Feel exists, it must contain substantive content (not TODO). If it does not exist, continue without blocking — derive philosophy from the interaction model and other accessibility/input sections.

## Dependency Chain

The 5 phases are not strictly sequential. The real dependency structure is:

```
interaction-model + design doc → action-map (Phase 1)
interaction-model + design doc → input-philosophy (Phase 2)
action-map → KBM bindings (Phase 3)
action-map → gamepad bindings (Phase 4)
action-map + philosophy + ui-kit → UI navigation (Phase 5)
```

Phases 1 and 2 are independent — both derive from design canon, not from each other. Phases 3–4 depend on Phase 1. Phase 5 depends on Phases 1 and 2.

## Phase 1 — Seed Action Map

1. **Read** `scaffold/inputs/action-map.md`.
2. **Extract player verbs** from the design doc's Player Verbs, Core Loop, and Content Structure sections. Also extract from the interaction model's action definitions.
3. **Propose action IDs** with namespaces (`player_`, `ui_`, `camera_`, `debug_`). Verify each proposed ID follows the naming convention: lowercase, underscore-separated, stable semantic name, correct namespace prefix. Include a Source column for each action tracing it to a specific design artifact (e.g., `design-doc: Player Verbs`, `interaction-model: Selection Model`).
4. **Add to proposal package** (do not present yet — see Phase 6).

## Phase 2 — Seed Input Philosophy

1. **Read** `scaffold/inputs/input-philosophy.md`.
2. **Read advisory theory docs** for context (if present):
   - `scaffold/theory/ux-heuristics.md` — accessibility principles
   - `scaffold/theory/game-design-principles.md` — agency and feedback
3. **Extract principles** from the design doc's Input Feel, Accessibility Philosophy, and Accessibility Targets sections. Also extract from the interaction model's input principles.
4. **Propose input philosophy content:** principles, responsiveness targets, accessibility features, and constraints.
5. **Add to proposal package.**

## Phase 3 — Seed KBM Bindings

1. **Read** `scaffold/inputs/default-bindings-kbm.md`.
2. **Read the action-map** — use the Phase 1 proposal output as the authoritative action list. If the action-map file already contains substantive authored content beyond what Phase 1 proposed, include those existing rows as well.
3. **Propose default keyboard/mouse bindings** for every action, grouped by namespace.
4. **Check for suspicious binding collisions.** Flag duplicate assignments that appear ambiguous within the same active input context. Do not flag overlaps that are clearly separated by namespace, screen, or mode (e.g., `debug_` and `player_` actions may share keys if they are never active simultaneously).
5. **Add to proposal package.**

## Phase 4 — Seed Gamepad Bindings

1. **Read** `scaffold/inputs/default-bindings-gamepad.md`.
2. **Read the action-map** — use the Phase 1 proposal output as the authoritative action list, plus any existing authored rows.
3. **Propose default gamepad bindings** for every action, grouped by namespace.
4. **Check for suspicious binding collisions** using the same context-aware rules as Phase 3.
5. **Add to proposal package.**

## Phase 5 — Seed UI Navigation

1. **Read** `scaffold/inputs/ui-navigation.md`.
2. **Read the action-map** — use the Phase 1 proposal output as the authoritative action list, plus any existing authored rows.
3. **Read `scaffold/design/ui-kit.md`** if present for component and screen context. If ui-kit does not exist, derive navigation from the interaction model, existing UI references in the design doc, and genre conventions. Leave any screen-specific flows that cannot be determined as TODO.
4. **Read the input philosophy** (proposed in Phase 2) for accessibility and responsiveness constraints that affect navigation.
5. **Propose navigation model** (spatial, tab-order, or hybrid) based on game genre and input philosophy.
6. **Propose focus flow** for major screens based on available UI context. Navigation is the phase most likely to have partial authored content — preserve existing authored screen flows, only propose flows for unfilled screens/sections, and do not replace a substantive navigation model.
7. **Add to proposal package.**

## Phase 6 — Present and Confirm

Present all five proposals as a single review package:

```
## Input Seed — Review Package

### Phase 1: Action Map
[proposed actions table]

### Phase 2: Input Philosophy
[proposed principles, responsiveness, accessibility, constraints]

### Phase 3: KBM Bindings
[proposed bindings table]
[collision warnings if any]

### Phase 4: Gamepad Bindings
[proposed bindings table]
[collision warnings if any]

### Phase 5: UI Navigation
[proposed navigation model, focus flow]

**Options:**
- Approve all → write all five docs
- Edit Phase # → revise specific phase before writing
- Reject Phase # → skip that phase, leave as TODO
```

Wait for user approval before writing any content. The user can approve the entire package at once or request edits to specific phases. Only write after approval.

## Phase 7 — Write Confirmed Content

For each approved phase, write the confirmed content into the corresponding input doc:
- Replace TODO markers and template instructions with confirmed content.
- Preserve any substantive existing content (see fill-level rules below).
- Update `Last Updated` to today's date.
- Add Changelog entry: `- YYYY-MM-DD: Seeded/expanded from design doc and interaction model (scaffold-bulk-seed-input).`

## Phase 8 — Report

```
## Input Docs Seeded

### Summary
| Doc | Sections filled | Sections left as TODO | Status |
|-----|----------------|----------------------|--------|
| action-map.md | N | N | Draft |
| input-philosophy.md | N | N | Draft |
| default-bindings-kbm.md | N | N | Draft |
| default-bindings-gamepad.md | N | N | Draft |
| ui-navigation.md | N | N | Draft |

### Actions Registered
| Namespace | Count |
|-----------|-------|
| player_ | N |
| ui_ | N |
| camera_ | N |
| debug_ | N |

### Flagged Same-Context Collisions
[List any ambiguous binding overlaps within the same active input context, or "None detected"]

### Next Steps
- Run `/scaffold-sync-glossary --scope input` to register new domain terms (action names, input concepts) in the glossary
- Review each doc and fill in remaining TODOs
- Run `/scaffold-fix-style --target interaction-model.md` if input seeding revealed interaction model gaps
- Run `/scaffold-validate --scope all` to check cross-references when ready to stabilize
```

## Rules

- **Never write content the user hasn't confirmed.** Generate all proposals first, present as a single review package, write only after approval.
- **Phases follow the dependency chain, not a strict sequence.** Action-map and philosophy are independent (both derive from design canon). Bindings depend on action-map. Navigation depends on action-map, philosophy, and optionally ui-kit.
- **Be specific, not generic.** Proposed content should reference the actual game described in the design doc, not boilerplate.
- **If a section can't be derived**, say so and leave it as TODO. Don't force content where the design doc doesn't provide enough context.
- **Fill-level rules for existing content:**
  - Sections containing only TODOs, placeholder notes, or template instructions → treat as unfilled, propose replacement.
  - Sections with substantive authored content → treat as filled, skip entirely.
  - Sections with partial content (some authored rows, some empty) → preserve authored content, only propose additions for empty rows/fields.
  - Never replace substantive content unless the user explicitly asks for revision.
- **Seeded docs remain Status: Draft** unless they already have a different user-set status. Do not change an existing status.
- **Do not import implementation detail into design canon.** The engine input doc is a constraint reference only. Use it to avoid contradictions, not to pull implementation mechanics upward into Rank 3 docs. If the engine doc suggests a binding limitation or input routing constraint, note it as a constraint — do not describe the implementation.
- **Action IDs must follow naming conventions.** Lowercase, underscore-separated, stable semantic names, correct namespace prefix. Verify every proposed ID before presenting.
- **Binding collision checks are context-aware.** Not all duplicate key assignments are conflicts. Actions in different namespaces, mutually exclusive contexts, or debug-only layers may legitimately share bindings. Only flag ambiguous overlaps within the same active input context.
- **ui-kit is optional for navigation.** If ui-kit does not exist, derive what you can from the interaction model and genre conventions. Leave screen-specific flows as TODO rather than blocking the entire phase.
- **Every action must trace to design canon.** Do not invent actions solely to make bindings or navigation look complete. Every proposed action must trace back to a player verb, UI need, camera need, or explicit debug need found in the design doc or interaction model. If an action has no traceable source, do not propose it.
