---
name: scaffold-new-input
description: Interactively fill out an input document. Pick which doc to create: action-map, bindings-kbm, bindings-gamepad, ui-navigation, or input-philosophy.
argument-hint: [action-map|bindings-kbm|bindings-gamepad|ui-navigation|input-philosophy]
allowed-tools: Read, Edit, Grep, Glob
---

# New Input Document

Guide the user through filling out an input document: **$ARGUMENTS**

## Supported Documents

| Argument | File |
|----------|------|
| `action-map` | `scaffold/inputs/action-map.md` |
| `bindings-kbm` | `scaffold/inputs/default-bindings-kbm.md` |
| `bindings-gamepad` | `scaffold/inputs/default-bindings-gamepad.md` |
| `ui-navigation` | `scaffold/inputs/ui-navigation.md` |
| `input-philosophy` | `scaffold/inputs/input-philosophy.md` |

## Before Starting

1. **Match the argument** to a supported document above. If no argument or unrecognized, list the options and ask the user which doc to fill out.
2. **Read the design doc** at `scaffold/design/design-doc.md` for context — especially Player Verbs, Core Loop, Input Feel, and Accessibility Philosophy sections.
3. **Read advisory theory docs** for context (informs suggestions but carries no authority):
   - `scaffold/theory/ux-heuristics.md` — UX principles, especially accessibility
   - `scaffold/theory/game-design-principles.md` — agency and feedback principles
4. **Read `scaffold/inputs/input-philosophy.md`** for input design principles context (if filling a different doc).
5. **Read the target doc** and identify which sections are already filled (have content beyond `*TODO:*` markers) and which are empty.
6. **Skip sections that are already complete.** Only walk the user through unfilled or partial sections.

## Walkthrough: action-map

Work through `scaffold/inputs/action-map.md` section by section:

1. **Namespacing** — Ask: *"What namespace prefixes does your game use for actions? Common choices: `player_`, `ui_`, `camera_`, `debug_`. List the namespaces and what each covers."*
2. **Player Actions** — Ask: *"List all `player_` actions — these are gameplay verbs the player performs. For each, give the action ID, a brief description, and whether it's a press, hold, or axis."*
3. **UI Actions** — Ask: *"List all `ui_` actions — menu navigation, inventory interaction, dialog advance, etc. For each, give the action ID, description, and input type."*
4. **Camera Actions** — Ask: *"List all `camera_` actions — zoom, rotate, pan, lock-on, etc. For each, give the action ID, description, and input type."*
5. **Debug Actions** — Ask: *"List any `debug_` actions — toggle console, frame stats, teleport, etc. These are stripped from release builds."*
6. **Rules** — Ask: *"What rules govern action naming and organization? For example: 'all actions use snake_case', 'no action belongs to two namespaces', 'every action must have exactly one canonical binding'."*

## Walkthrough: bindings-kbm

Work through `scaffold/inputs/default-bindings-kbm.md` section by section:

1. **Read the action-map** at `scaffold/inputs/action-map.md` for the full list of actions.
2. **For each namespace**, propose default keyboard/mouse bindings one namespace at a time:
   - **Player actions** — Ask: *"Here are the player actions. I'll propose default keyboard/mouse bindings for each. Confirm, change, or skip each one."* Present a table of action → proposed key.
   - **UI actions** — Same pattern.
   - **Camera actions** — Same pattern.
   - **Debug actions** — Same pattern.
3. **Check for conflicts** — After all bindings are proposed, scan for duplicate key assignments and flag them.
4. **Modifier keys** — Ask: *"Which modifier combinations are used? (e.g., Shift+Click for bulk select, Ctrl+S for quicksave). List any modifier rules."*

## Walkthrough: bindings-gamepad

Work through `scaffold/inputs/default-bindings-gamepad.md` section by section:

1. **Read the action-map** at `scaffold/inputs/action-map.md` for the full list of actions.
2. **For each namespace**, propose default gamepad bindings one namespace at a time:
   - **Player actions** — Ask: *"Here are the player actions. I'll propose default gamepad bindings. Confirm, change, or skip each one."* Present a table of action → proposed button/stick.
   - **UI actions** — Same pattern.
   - **Camera actions** — Same pattern.
   - **Debug actions** — Same pattern (often mapped to D-pad combos or shoulder+select).
3. **Check for conflicts** — After all bindings are proposed, scan for duplicate button assignments and flag them.
4. **Stick behavior** — Ask: *"How do analog sticks behave? Dead zones, response curves, inversion options?"*

## Walkthrough: ui-navigation

Work through `scaffold/inputs/ui-navigation.md` section by section:

1. **Navigation Model** — Ask: *"How does the player navigate menus and UI? Options: spatial (D-pad/arrow keys move between elements), tab-order (Tab/Shift+Tab cycles through elements), hybrid (spatial + tab). Which model?"*
2. **Focus Flow** — Ask: *"Describe the focus flow for each major screen: main menu, pause menu, inventory, settings, etc. Which element gets focus first? Where does focus wrap?"*
3. **Navigation Actions** — Ask: *"Which actions from the action-map control UI navigation? Map them: navigate_up, navigate_down, navigate_left, navigate_right, confirm, cancel, tab_next, tab_prev."*
4. **Mouse Behavior** — Ask: *"How does the mouse interact with UI? Does hovering move focus? Does clicking bypass the focus system? Is there a cursor mode vs. gamepad mode?"*

## Walkthrough: input-philosophy

Work through `scaffold/inputs/input-philosophy.md` section by section:

1. **Principles** — Ask: *"What are the core input design principles? Examples: 'every action has immediate visual feedback', 'no input should feel laggy', 'accessibility is not optional'. List 3–5 principles."*
2. **Responsiveness** — Ask: *"What are the responsiveness targets? Input latency budget (e.g., <100ms from press to feedback), animation canceling rules, input buffering window."*
3. **Accessibility** — Ask: *"What accessibility features does the input system support? Rebindable keys, one-handed mode, hold-vs-toggle options, colorblind input cues, subtitle support for audio cues."*
4. **Constraints** — Ask: *"What input constraints exist? Maximum simultaneous inputs, forbidden key combinations, platform-specific restrictions (e.g., no right-click on web, no keyboard on console)."*

## Rules

- **Ask one section at a time.** Do not dump all questions at once.
- **Write answers into the target doc immediately** after the user responds. Replace the `*TODO:*` marker with their answer.
- **Use the user's voice.** Capture their intent faithfully — don't rewrite into generic design language.
- **Reference the design doc.** If the design doc has relevant info (e.g., Player Verbs for action-map, Input Feel for philosophy), mention it to the user as context before asking.
- **Use theory docs as advisory context.** Reference UX heuristics and game design principles when relevant, but never impose them.
- **If the user says "skip" or "later"**, leave the TODO marker and move on.
- **If the user gives a short answer**, that's fine. Short and clear beats long and vague.
- **After completing all sections**, report how many sections are filled vs. remaining TODOs.
- **Remind the user** to run `/scaffold-review-input` when done to audit completeness.
- **Created documents start with Status: Draft.**
