---
name: scaffold-bulk-seed-style
description: Seed style-guide, color-system, ui-kit, interaction-model, feedback-system, and audio-direction from the design doc, system designs, architecture, and engine docs. Use after the design doc is filled out. Phases are sequential — each doc informs the next.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Visual & UX Documents

Seed all 6 Step 5 docs from upstream context: **$ARGUMENTS**

Reads the design doc, system designs, architecture docs, and engine docs to pre-fill style-guide, color-system, ui-kit, interaction-model, feedback-system, and audio-direction. Each doc builds on the previous — phases are strictly sequential.

## Prerequisites

1. **Read the design doc** at `scaffold/design/design-doc.md`.
2. **Verify it's sufficiently filled out.** The following sections must have content (not just TODO markers):
   - Core Fantasy
   - Design Invariants
   - Core Loop
   - Player Control Model
   - Player Mental Model
   - Player Information Model
   - Failure Philosophy
3. If the design doc is too empty, stop and tell the user to run `/scaffold-init-design` first.
4. **Check which docs already exist and are authored.** For each of the 6 docs, if the file exists and has substantive content (not just template defaults), skip that phase. Report which docs are being skipped.

## Context Files

Read these before starting. They provide the full upstream context for Step 5. Sourced from the Document Influence Map in `scaffold/doc-authority.md`.

| Context File | Phases That Use It | Why |
|-------------|-------------------|-----|
| `scaffold/design/design-doc.md` | All | Core vision, loops, pillars, governance, player experience model, failure philosophy, target platforms |
| `scaffold/doc-authority.md` | All | Document authority ranking, same-rank conflict resolution, influence map |
| `scaffold/design/glossary.md` | All | Canonical terminology — use correct terms in all seeded content |
| `scaffold/design/systems/_index.md` | 1–6 | System list — which systems exist. Read individual SYS-### docs as needed per phase. |
| `scaffold/design/architecture.md` | 1, 3, 4 | Scene tree, UI panel pattern, data flow rules, boot order |
| `scaffold/design/authority.md` | 4 | Data ownership — what systems own what (for command model) |
| `scaffold/design/interfaces.md` | 4 | Cross-system contracts — what player-triggered interactions cross systems |
| `scaffold/design/state-transitions.md` | 2, 3, 5 | State machines — entity states map to colors (Phase 2), visual states (Phase 3), feedback triggers (Phase 5) |
| `scaffold/reference/signal-registry.md` | 5 | Signal names and levels — what events the game fires, used to build the Event-Response Table |
| `scaffold/reference/entity-components.md` | 1, 3 | Entity data shapes — what the UI needs to display, what entities need icons |
| `scaffold/reference/resource-definitions.md` | 3 | Resources — what items/resources need UI representation |
| `scaffold/engine/_index.md` | 1, 3, 4 | Engine doc list — what implementation constraints exist |
| Engine UI doc (if exists) | 1, 2, 3, 5 | UI rendering approach, theme system, layout patterns, animation approach |
| Engine input doc (if exists) | 4 | Input routing, device handling, camera control patterns |
| Engine scene-architecture doc (if exists) | 1, 3 | Scene tree patterns, lifecycle — informs rendering approach and layout |
| `scaffold/theory/` (if relevant docs exist) | 1–6 | Advisory context — game design principles, UX heuristics. Read for rationale and anti-pattern awareness. Not authoritative. |
| Accepted ADRs | All | Decisions that may affect visual/UX choices |

Only include context files that exist — skip missing ones silently.

### Per-Phase Influence Sources

Each phase reads its predecessors plus specific upstream docs. This table summarizes what each phase uniquely needs beyond the shared context above.

| Phase | Doc Being Seeded | Key Upstream (beyond design-doc + glossary) | Reads Prior Step 5 Docs |
|-------|-----------------|---------------------------------------------|------------------------|
| 1 | style-guide | architecture (scene tree), engine UI doc, engine scene-architecture, entity-components | — |
| 2 | color-system | state-transitions (state→color mapping) | style-guide |
| 3 | ui-kit | system designs (info to surface), architecture (UI panel pattern), engine UI doc, entity-components, resource-definitions | style-guide, color-system |
| 4 | interaction-model | system designs (player-interactive entities), architecture (query API rules), interfaces (cross-system triggers), authority (ownership), engine input doc | style-guide, color-system, ui-kit |
| 5 | feedback-system | system designs (events per system), signal-registry (gameplay signals), state-transitions (state changes), engine UI doc | style-guide, color-system, ui-kit, interaction-model |
| 6 | audio-direction | feedback-system (priority hierarchy, sound categories) | style-guide, feedback-system |

## Phase 1 — Seed Style Guide

1. **Read** `scaffold/design/style-guide.md`. If already authored, skip to Phase 2.
2. **If file doesn't exist**, create from `scaffold/templates/style-guide-template.md` (if a template exists) or create with the standard Rank 2 header.
3. **Extract visual identity cues** from upstream context:
   - **Art Direction** ← Design doc: Aesthetic Pillars + Genre & Reference Points
   - **Visual Tone** ← Design doc: Tone section + Failure Philosophy (how mood shifts with game state)
   - **Rendering Approach** ← Design doc: Camera/Perspective + Architecture: scene tree layout + Engine UI doc: rendering approach
   - **Character & Entity Style** ← Design doc: entity descriptions + Entity-components: what entities exist
   - **Environment Style** ← Design doc: Place & Time + Rules of the World
   - **Lighting Model** ← Design doc: atmosphere + Tone section
   - **Animation Style** ← Design doc: Input Feel + Aesthetic Pillars
   - **Iconography Style** ← Design doc: Player Information Model (what info must be visible at a glance)
4. **Present proposed content** for each section to the user as a draft.
5. **Ask the user to confirm, edit, or reject** each section.
6. **Write confirmed content**, set Created/Last Updated dates, add Changelog entry.

## Phase 2 — Seed Color System

1. **Read** `scaffold/design/color-system.md`. If already authored, skip to Phase 3.
2. **Read the style-guide** (just seeded in Phase 1) for visual identity context.
3. **Extract color cues** from upstream context:
   - **Palette** ← Style-guide: Art Direction + Visual Tone (colors that match the mood)
   - **Color Tokens** ← Design doc: game mechanics + State-transitions: entity states (map states to semantic colors)
   - **Usage Rules** ← Style-guide: Visual Tone + Design doc: Player Information Model (readability rules)
   - **UI vs World Colors** ← Style-guide: Rendering Approach + Engine UI doc: theme system
   - **Accessibility** ← Design doc: Accessibility Philosophy and targets
   - **Theme Variants** ← Design doc: factions, biomes, modes, escalation states
4. **Present proposed content** for each section.
5. **Ask the user to confirm, edit, or reject.**
6. **Write confirmed content**, set dates, add Changelog entry.

## Phase 3 — Seed UI Kit

1. **Read** `scaffold/design/ui-kit.md`. If already authored, skip to Phase 4.
2. **Read the style-guide and color-system** (just seeded) for context.
3. **Read system designs that surface player-visible information.** Scan `scaffold/design/systems/_index.md` and read the Purpose + Player Actions + Visibility to Player sections of systems that directly affect what the UI must show (e.g., NeedsSystem surfaces hunger/fatigue bars, HealthSystem surfaces wound indicators, MoraleSystem surfaces mood).
4. **Extract UI cues** from upstream context:
   - **Component Definitions** ← Design doc: Player Verbs + Core Loop + Player Control Model (what UI does the player need?) + System designs: what info each system surfaces to the player + Architecture: UI Panel Pattern + Resource-definitions: what items/resources need UI representation
   - **Layout Rules** ← Design doc: Camera/Perspective + Architecture: scene tree UI layers + Engine UI doc: layout system
   - **Typography** ← Style-guide: Visual Tone + Design doc: Player Information Model (data density needs)
   - **Iconography** ← Style-guide: Iconography Style + Entity-components: entity types needing icons
   - **Component States** ← Color-system: color tokens (hover = accent, disabled = muted, error = danger) + State-transitions: entity states needing visual representation
   - **Animation & Transitions** ← Style-guide: Animation Style + Engine UI doc: animation approach
   - **Sound Feedback** ← Design doc: Audio Identity (basic per-component sounds — detailed coordination is in feedback-system)
   - **Responsive & Resolution Scaling** ← Design doc: Target Platforms + Engine UI doc: responsive design approach
4. **Present proposed content** for each section.
5. **Ask the user to confirm, edit, or reject.**
6. **Write confirmed content**, set dates, add Changelog entry.

## Phase 4 — Seed Interaction Model

1. **Read** `scaffold/design/interaction-model.md`. If file doesn't exist, create from `scaffold/templates/interaction-model-template.md`.
2. **Read style-guide, color-system, and ui-kit** (just seeded) for context.
3. **Read system designs for player-interactive entities.** Scan system designs and read Purpose + Player Actions sections to identify: what entities the player can select, what commands each system exposes, what modes exist (build, zone, inspect), what information the player queries.
4. **Extract interaction cues** from upstream context:
   - **Selection Model** ← Design doc: Player Control Model + System designs: what entities are player-interactive + Architecture: UI reads via query APIs rule
   - **Command Model** ← Design doc: Core Loop + Player Verbs + System designs: what actions each system exposes to the player
   - **Secondary Actions** ← Design doc: Player Control Model + Interfaces: what cross-system interactions the player triggers
   - **Drag Behaviors** ← Design doc: zone/build/placement mechanics + Engine input doc: input routing
   - **Interaction Patterns** ← Design doc: Core Loop (the canonical sequence of actions per game cycle)
   - **Modal vs Non-Modal** ← Design doc: layer/mode descriptions + UI kit: layout rules (what screen regions change per mode)
   - **Input Feedback** ← Color-system: hover/selection colors + Style-guide: animation for hover/press
   - **Camera Interaction** ← Design doc: Camera/Perspective + Engine input doc: camera control patterns
   - **Accessibility** ← Design doc: Accessibility Philosophy
4. **Present proposed content** for each section.
5. **Ask the user to confirm, edit, or reject.**
6. **Write confirmed content**, set dates, add Changelog entry.

## Phase 5 — Seed Feedback System

1. **Read** `scaffold/design/feedback-system.md`. If file doesn't exist, create from `scaffold/templates/feedback-system-template.md`.
2. **Read all prior Step 5 docs** (style-guide, color-system, ui-kit, interaction-model) for context.
3. **Read system designs for events and state changes.** Scan system designs and read Purpose + Downstream Consequences + State Lifecycle sections to identify: what events each system produces, what state changes the player should be notified about, what failure/warning conditions exist per system.
4. **Extract feedback cues** from upstream context:
   - **Feedback Types** ← Design doc: Failure Philosophy (Pre-Failure Warning Contract, no silent failures) + System designs: what events each system produces + Signal-registry: gameplay-facing signals
   - **Timing Rules** ← Interaction-model: input timing expectations + Design doc: simulation tick model awareness (instant UI vs tick-confirmed simulation)
   - **Priority & Stacking** ← Design doc: alert escalation model + UI kit: Alert Feed severity levels + Signal-registry: signal levels (Entity/Room/System/Colony/Global)
   - **Cross-Modal Coordination** ← UI kit: component states + Sound Feedback section + Color-system: semantic color meanings + Style-guide: animation timing
   - **Event-Response Table** ← System designs: major events per system + State-transitions: state change triggers + Signal-registry: gameplay signals. Map each to visual + audio + UI response.
4. **Present proposed content** for each section. The Event-Response Table is the most critical — present it as a draft table with the top 15-20 most common game events.
5. **Ask the user to confirm, edit, or reject.**
6. **Write confirmed content**, set dates, add Changelog entry.

## Phase 6 — Seed Audio Direction

1. **Read** `scaffold/design/audio-direction.md`. If file doesn't exist, create from `scaffold/templates/audio-direction-template.md`.
2. **Read all prior Step 5 docs** (especially feedback-system for priority coordination) for context.
3. **Extract audio cues** from upstream context:
   - **Audio Philosophy** ← Design doc: Tone + Core Fantasy + Aesthetic Pillars (clinical? oppressive? calm?) + Style-guide: Visual Tone registers (how audio mirrors visual escalation)
   - **Sound Categories** ← Feedback-system: feedback types (each type needs a sound category) + UI kit: Sound Feedback (component-level sounds already defined)
   - **Music Direction** ← Design doc: Tone + pacing references + Style-guide: Visual Tone registers (music follows same escalation model?)
   - **Silence & Space** ← Design doc: atmosphere + Failure Philosophy (does silence mean danger?)
   - **Feedback Hierarchy** ← Feedback-system: priority hierarchy (audio stacking aligns with cross-modal priority)
   - **Asset Style Rules** ← Style-guide: Art Direction (audio aesthetic should match visual aesthetic) + Design doc: Target Platforms (audio format constraints)
   - **Accessibility** ← Design doc: Accessibility Philosophy + Feedback-system: redundancy principle (no audio-only information)
4. **Present proposed content** for each section.
5. **Ask the user to confirm, edit, or reject.**
6. **Write confirmed content**, set dates, add Changelog entry.

## Phase 7 — Report

```
## Step 5 Seed Complete

### Documents Seeded
| Document | Sections Filled | Sections TODO | Status |
|----------|----------------|--------------|--------|
| style-guide.md | N | N | Draft / Skipped (already authored) |
| color-system.md | N | N | Draft / Skipped |
| ui-kit.md | N | N | Draft / Skipped |
| interaction-model.md | N | N | Draft / Skipped |
| feedback-system.md | N | N | Draft / Skipped |
| audio-direction.md | N | N | Draft / Skipped |

### Cross-Doc Consistency Notes
[Any inconsistencies noticed between the 6 docs during seeding]

### Recommended Next Steps
- Fill remaining TODO sections interactively with `/scaffold-new-style [doc-name]`
- Run `/scaffold-fix-style` (when available) for mechanical cleanup
- Run `/scaffold-iterate-style` (when available) for adversarial review
- Run `/scaffold-validate --scope all` to check cross-references
```

## Rules

- **Never write content the user hasn't confirmed.** Always present the proposal first.
- **Phases are strictly sequential.** Style-guide → color-system → ui-kit → interaction-model → feedback-system → audio-direction. Each doc reads the previous ones as context. Do not skip ahead.
- **Be specific, not generic.** Proposed content should reference the actual game described in the design doc, not boilerplate. Use system names, entity types, and mechanics from the project.
- **Use canonical terminology.** All proposed content must use terms from `scaffold/design/glossary.md`. Never use NOT-column synonyms.
- **If a section can't be derived**, say so and leave it as TODO. Don't force content where upstream docs don't provide enough context. Note what's missing so the user can fill it manually.
- **Preserve any existing content.** If a section is already filled, skip it — don't overwrite.
- **Created documents start with Status: Draft.** Set Created and Last Updated to today's date. Add initial Changelog entry referencing this skill as trigger.
- **Engine-aware, not engine-bound.** Step 5 docs define what must exist, how it behaves, and how it feels. They may reference engine capabilities (e.g., "the engine uses Control nodes for UI") for context, but must not prescribe specific node hierarchies, signal wiring, or Godot patterns. Those belong in Step 4 engine docs.
- **Feedback-system is the coordination layer.** UI kit defines component-level feedback (what a button looks like pressed). Audio-direction defines sound character. Feedback-system defines when and how they fire together. Don't duplicate — cross-reference.
- **Interaction-model owns input, feedback-system owns response.** Interaction-model defines what the player does (select, command, drag, cancel). Feedback-system defines what the system does back (confirm, warn, alert). Don't mix these.
- **Read theory docs for advisory context.** If `scaffold/theory/` contains docs on UX design, visual design, audio design, or game feel — read them for rationale and anti-pattern awareness. Theory never overrides design-doc decisions, but it provides useful framing. Note in proposals when a suggestion is informed by theory.
