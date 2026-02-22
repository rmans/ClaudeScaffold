# UX Heuristics

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

General UX principles for games. This document is a reference for reviewing design docs and systems. It informs decisions but never dictates them — cite specific heuristics in ADRs when they influence a choice.

## Onboarding

- Teach through play, not text. The player should learn by doing, not by reading paragraphs.
- Introduce one mechanic at a time. Let the player internalize each concept before layering the next one on top.
- Provide a safe space to practice. Early encounters should be forgiving enough that failure teaches rather than punishes.
- Ramp complexity progressively. Each new challenge should build on something the player already understands.
- Do not front-load information. Deliver knowledge at the moment the player needs it, not before.
- Assume the player will skip or ignore any text longer than one sentence.

## Tutorialization

- Show, don't tell. A visual demonstration or guided action is worth more than an explanation.
- Use contextual prompts over menu tutorials. Teach the player in the moment, in the environment where the skill is used.
- Let players fail safely. A failed attempt with clear feedback teaches better than a forced success.
- Repeat critical lessons in new contexts. If a mechanic is important, reinforce it in varied situations so the player generalizes the skill.
- Make tutorials skippable for returning players. Forced tutorials on replay breed resentment.
- Gate progression on demonstrated understanding, not on reading a tooltip.

## UI Clarity

- Give the most screen space to the most important information. If health matters most, it should be the most visible element.
- Use consistent iconography. The same icon should always mean the same thing across every screen.
- Design for the target viewing distance. Text and icons legible on a monitor at arm's length may be unreadable on a TV across a room or a mobile device in hand.
- Minimize the number of clicks or steps required to reach common actions. Frequent tasks should be fast; rare tasks can afford more steps.
- Avoid clutter. Every element on screen competes for attention. If an element does not help the player right now, consider hiding it or reducing its prominence.

## Feedback and Communication

- Every player action should produce visible or audible feedback. If the player presses a button and nothing happens, the game feels broken.
- Distinguish between "action succeeded," "action failed," and "action not available." Each state needs a distinct response.
- Error states should explain what went wrong and what the player can do about it. "Invalid" is not helpful; "Not enough gold (need 50, have 30)" is.
- Make progress visible. If the player is working toward a goal, show how far they have come and how far they have to go.
- State changes should be obvious. When the game mode shifts (combat to exploration, gameplay to menu), signal it clearly through visual, audio, or both.

## Navigation and Wayfinding

- The player should always know where to go next, or know that freeform exploration is the intended experience. Ambiguity should be deliberate, not accidental.
- Provide multiple wayfinding tools: landmarks, maps, minimaps, breadcrumbs, objective markers. Let the player choose their preferred level of guidance.
- Minimize backtracking that serves no gameplay purpose. If the player must retrace their steps, give them something new to encounter along the way.
- Make the critical path visually distinct from optional paths. Players should be able to distinguish "I must go here" from "I can explore here" at a glance.
- Ensure the player can always return to known safe territory without getting permanently lost.

## Accessibility

- Support colorblind modes. Never rely on color alone to convey critical information — pair color with shape, pattern, or text.
- Provide subtitle options: adjustable size, optional background for readability, and speaker labels for multi-character dialogue.
- Allow full control remapping. Every gameplay action should be rebindable. Avoid requiring simultaneous button presses (chords) without an alternative.
- Offer meaningful difficulty options. Adjustable difficulty respects the broadest range of players without diminishing the experience for any of them.
- Support screen readers for menus and non-time-critical UI. Alt text on icons and buttons costs little and enables a lot.
- Consider one-handed play options where the game design permits it. Toggle alternatives for hold actions, auto-run, and simplified control schemes widen the audience.

## Settings and Options

- Expose graphics, audio, and control settings. Players expect to adjust resolution, volume channels, and keybinds at minimum.
- Respect system-level preferences where relevant: OS language, dark mode, system volume.
- Save settings changes immediately or on focus loss. Never force the player to find and click a "Save" button for preferences.
- Preview changes before applying where possible. Let the player see what a graphics or audio change does before committing.
- Provide sensible defaults. The game should be playable and pleasant on first launch without any settings changes.

## Error Prevention

- Confirm destructive actions. Deleting a save file, quitting without saving, and spending rare resources should require explicit confirmation.
- Support undo where feasible. If the player can accidentally ruin something, let them reverse it.
- Auto-save at regular intervals and at critical moments (before boss fights, after major progress). Never rely on the player remembering to save.
- Never allow softlocks. If the player can reach a state where progress is impossible and they cannot reload or escape, the game has a critical bug.
- Handle disconnects and crashes gracefully. Recover as much state as possible and communicate clearly what was lost.

## Consistency

- The same button should perform the same action in every context. If "A" confirms in menus, it should confirm everywhere.
- The same color should convey the same meaning throughout the game. If red means damage, do not use red for positive effects elsewhere.
- The same icon should represent the same concept on every screen. Do not reuse icons for unrelated purposes.
- Break consistency only when there is a strong gameplay reason, and signal the break clearly. Inconsistency should feel intentional, not like an oversight.
- Apply consistent spatial conventions. If health is top-left, keep it top-left. If inventory opens from the right, always open from the right.

## Cognitive Load

- Limit simultaneous demands on player attention. Avoid requiring the player to read text, track enemies, and manage a timer all at once unless that pressure is the intended design.
- Group related information together. Stats near stats, actions near actions, lore near lore.
- Use chunking: present information in groups of 3 to 5 items. Long flat lists are harder to scan and remember than structured clusters.
- Offload memory to the UI. Quest logs, inventories, maps, bestiaries, and combo lists exist so the player does not have to memorize them.
- Reveal complexity gradually. A system with 20 interacting variables is fine if the player learns them 2 or 3 at a time over hours, not all at once in a menu.
- Provide summaries and reminders. If the player returns after a break, help them remember where they were and what they were doing.
