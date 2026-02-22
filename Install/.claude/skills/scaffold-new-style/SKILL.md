---
name: scaffold-new-style
description: Interactively fill out a Rank 2 style document. Pick which doc to create: style-guide, color-system, or ui-kit.
argument-hint: [style-guide|color-system|ui-kit]
allowed-tools: Read, Edit, Grep, Glob
---

# New Style Document

Guide the user through filling out a Rank 2 style document: **$ARGUMENTS**

## Supported Documents

| Argument | File |
|----------|------|
| `style-guide` | `scaffold/design/style-guide.md` |
| `color-system` | `scaffold/design/color-system.md` |
| `ui-kit` | `scaffold/design/ui-kit.md` |

## Before Starting

1. **Match the argument** to a supported document above. If no argument or unrecognized, list the options and ask the user which doc to fill out.
2. **Read the design doc** at `scaffold/design/design-doc.md` for context — especially Tone, Aesthetic Pillars, Camera/Perspective, and Audio Identity sections.
3. **Read advisory theory doc** for context (informs suggestions but carries no authority):
   - `scaffold/theory/ux-heuristics.md` — UX principles to guide style decisions
   - `scaffold/theory/audio-design.md` — audio principles for sound feedback sections
4. **Read the target doc** and identify which sections are already filled (have content beyond `*TODO:*` markers) and which are empty.
5. **Skip sections that are already complete.** Only walk the user through unfilled or partial sections.

## Walkthrough: style-guide

Work through `scaffold/design/style-guide.md` section by section:

1. **Art Direction** — Ask: *"What does this game look like at a glance? Describe the overall visual identity — influences, mood boards, reference points."*
2. **Visual Tone** — Ask: *"How should the visuals make the player feel? Dark and gritty? Bright and whimsical? Clean and minimalist? Nostalgic?"*
3. **Rendering Approach** — Ask: *"2D or 3D? Pixel art, hand-drawn, low-poly, realistic? What's the perspective — top-down, isometric, side-scroll, free camera?"*
4. **Character & Entity Style** — Ask: *"How do characters, creatures, and objects look? What are the proportions? How do you tell entities apart at a glance?"*
5. **Environment Style** — Ask: *"How does the world look? Biome palettes, architectural style, terrain approach, lighting mood?"*
6. **VFX & Particles** — Ask: *"What do explosions, magic, weather, and hit feedback look like? How flashy or subtle?"*
7. **Animation Style** — Ask: *"Should animations feel snappy or weighty? What's the idle behavior? How do transitions feel?"*

## Walkthrough: color-system

Work through `scaffold/design/color-system.md` section by section:

1. **Palette** — Ask: *"What are your core colors? List them with hex values if you have them, or describe them (e.g. 'muted earth tones', 'neon cyberpunk'). Group by role: primary, secondary, accent, neutral."*
2. **Color Tokens** — Ask: *"What semantic color names does the game use? Examples: color-health, color-danger, color-xp, color-bg-panel. These are what the game references — not raw hex values."*
3. **Usage Rules** — Ask: *"What rules govern color usage? For example: 'red is only for danger/health', 'accent color is only for interactive elements', 'neutral backgrounds only'."*
4. **UI vs World Colors** — Ask: *"How do colors differ between UI and the game world? UI is typically flat and readable. World colors follow lighting and environment. Where's the boundary?"*
5. **Accessibility** — Ask: *"What are your contrast requirements? How do colorblind players distinguish important elements? Do you use shape/icon in addition to color?"*
6. **Theme Variants** — Ask: *"Are there alternate color schemes? Light/dark mode, faction colors, seasonal themes, biome palettes? If none, say so."*

## Walkthrough: ui-kit

Work through `scaffold/design/ui-kit.md` section by section:

1. **Component Definitions** — Ask: *"What reusable UI components does the game need? List them — buttons, panels, tooltips, health bars, inventory slots, dialog boxes, menus, sliders, progress bars, etc."*
2. **Layout Rules** — Ask: *"What's the spacing and layout philosophy? Grid system, margin scale, safe zones? Where does the HUD live — corners, edges, center?"*
3. **Typography** — Ask: *"What fonts does the game use? Define the hierarchy: title text, heading text, body text, label text. Sizes, weights, line heights."*
4. **Iconography** — Ask: *"What's the icon style — outline, filled, pixel? Standard sizes? Custom-drawn or from a pack? How do icons relate to the art direction?"*
5. **Component States** — Ask: *"How do components look in each state: default, hover, pressed, focused, disabled, selected, error? What's the visual language — color shifts, scale, glow?"*
6. **Animation & Transitions** — Ask: *"How do UI elements enter, exit, and transition? Panel slides, fades, pops? What are the timing curves — snappy, eased, bouncy?"*
7. **Sound Feedback** — Ask: *"Which UI interactions get audio feedback? Button press, tab switch, error, success? Describe the feel — 'soft click', 'crisp snap' — not filenames."*
8. **Responsive & Resolution Scaling** — Ask: *"How does the UI adapt to different screen sizes? What's the minimum resolution? Scaling approach — stretch, letterbox, anchor-based? Touch targets if applicable?"*

## Rules

- **Ask one section at a time.** Do not dump all questions at once.
- **Write answers into the target doc immediately** after the user responds. Replace the `*TODO:*` marker with their answer.
- **Use the user's voice.** Capture their intent faithfully — don't rewrite into generic design language.
- **Reference the design doc.** If the design doc has relevant info (e.g. Aesthetic Pillars for style-guide, or Tone for color-system), mention it to the user as context before asking.
- **Use theory docs as advisory context.** Reference UX heuristics when relevant to help the user think through style decisions, but never impose them. Theory informs — it doesn't dictate.
- **If the user says "skip" or "later"**, leave the TODO marker and move on.
- **If the user gives a short answer**, that's fine. Short and clear beats long and vague.
- **After completing all sections**, report how many sections are filled vs. remaining TODOs.
- **Remind the user** to run `/scaffold-review-style` when done to audit completeness.
