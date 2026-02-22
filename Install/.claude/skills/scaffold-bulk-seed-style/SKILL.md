---
name: scaffold-bulk-seed-style
description: Seed style-guide, color-system, and ui-kit from the design doc. Use after the design doc is filled out.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Style Documents from Design Doc

Read the completed design doc and use it to pre-fill the style-guide, color-system, and ui-kit.

## Prerequisites

1. **Read the design doc** at `scaffold/design/design-doc.md`.
2. **Verify it's sufficiently filled out.** The following sections must have content (not just TODO markers):
   - Core Fantasy
   - Tone
   - Aesthetic Pillars
   - Camera / Perspective
3. If the design doc is too empty, stop and tell the user to run `/scaffold-new-design` first.

## Phase 1 — Seed Style Guide

1. **Read** `scaffold/design/style-guide.md`.
2. **Extract visual identity cues** from the design doc:
   - **Art Direction** ← Aesthetic Pillars + Genre & Reference Points
   - **Visual Tone** ← Tone section
   - **Rendering Approach** ← Camera / Perspective + any rendering mentions
   - **Character & Entity Style** ← Player Character + any entity descriptions
   - **Environment Style** ← Place & Time + Rules of the World
   - **VFX & Particles** ← Input Feel + any feedback descriptions
   - **Animation Style** ← Input Feel + Aesthetic Pillars
3. **Present proposed content** for each section to the user as a draft.
4. **Ask the user to confirm, edit, or reject** each section.
5. **Write confirmed content** into the style-guide, replacing TODO markers.

## Phase 2 — Seed Color System

1. **Read** `scaffold/design/color-system.md`.
2. **Read the style-guide** (just seeded in Phase 1) for visual identity context.
3. **Extract color cues** from the design doc and style-guide:
   - **Palette** ← Aesthetic Pillars + Visual Tone (propose colors that match the mood)
   - **Color Tokens** ← Derive semantic names from game mechanics (health, mana, XP, danger, etc.)
   - **Usage Rules** ← Propose rules based on the visual tone and game mechanics
   - **UI vs World Colors** ← Derive from the rendering approach and visual tone
   - **Accessibility** ← Accessibility Philosophy and Accessibility Targets from design doc
   - **Theme Variants** ← Any mentions of factions, biomes, modes in the design doc
4. **Present proposed content** for each section to the user as a draft.
5. **Ask the user to confirm, edit, or reject** each section.
6. **Write confirmed content** into the color-system, replacing TODO markers.

## Phase 3 — Seed UI Kit

1. **Read** `scaffold/design/ui-kit.md`.
2. **Read the style-guide and color-system** (just seeded) for context.
3. **Extract UI cues** from the design doc, style-guide, and color-system:
   - **Component Definitions** ← Player Verbs + Core Loop (what UI does the player interact with?)
   - **Layout Rules** ← Camera / Perspective + any HUD mentions
   - **Typography** ← Visual Tone + Aesthetic Pillars (propose font style that fits)
   - **Iconography** ← Art Direction (icons should match the visual style)
   - **Component States** ← Derive from color tokens (hover = accent, disabled = muted, error = danger)
   - **Animation & Transitions** ← Animation Style from style-guide + Input Feel
   - **Sound Feedback** ← Audio Identity from design doc
   - **Responsive & Resolution Scaling** ← Target Platforms from design doc
4. **Present proposed content** for each section to the user as a draft.
5. **Ask the user to confirm, edit, or reject** each section.
6. **Write confirmed content** into the ui-kit, replacing TODO markers.

## Phase 4 — Report

Summarize what was seeded:
- Number of sections filled in each doc
- Number of sections left as TODO
- Remind the user of next steps: review each doc with `/scaffold-review-style`, then fill in remaining TODOs with `/scaffold-new-style`

## Rules

- **Never write content the user hasn't confirmed.** Always present the proposal first.
- **Phases are sequential.** Style-guide informs color-system, which informs ui-kit. Do not skip ahead.
- **Be specific, not generic.** Proposed content should reference the actual game described in the design doc, not boilerplate.
- **If a section can't be derived**, say so and leave it as TODO. Don't force content where the design doc doesn't provide enough context.
- **Preserve any existing content.** If a section is already filled, skip it — don't overwrite.
