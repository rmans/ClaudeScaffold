# Interaction Model

> **Authority:** Rank 2
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md), [style-guide.md](style-guide.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

This document defines **how the player interacts with the game** — what inputs mean, how selection works, how commands are issued, and how layers are navigated. It is engine-agnostic and describes player intent and behavior, not implementation mechanics.

<!-- This doc bridges the gap between what the player wants to do (design-doc.md) and how the engine handles it (engine input-system docs). It governs what input docs implement and what UI presents. -->

---

## Selection Model

<!-- How does the player select things? What can be selected? What happens to selection across mode changes? -->

### Selectable Entities

<!-- What entity types can the player select? Colonists, structures, items, terrain tiles, zones? Are there things that are visible but NOT selectable? -->

### Selection Mechanics

<!-- Single click to select? Drag to multi-select? Modifier keys for add-to-selection? What deselects (click empty space, press Escape, switch modes)? -->

### Selection Persistence

<!-- Does selection survive mode switches (e.g., switching from normal view to build mode)? When is selection forcibly cleared? -->

## Command Model

<!-- How does the player issue commands to the game? -->

### Direct Commands

<!-- Actions that happen immediately: place a structure, designate a zone, set a priority. What triggers them (click, hotkey, menu)? -->

### Queued Commands

<!-- Commands that enter a queue for colonists/systems to execute. How does the player know a command was accepted vs executed? -->

### Command Cancellation

<!-- How does the player cancel a pending or in-progress command? Right-click? Escape? Undo? What's cancellable and what isn't? -->

### Priority Commands

<!-- Can the player override normal task priority? How (force-assign, priority slider, emergency flag)? What are the limits? -->

## Secondary Actions

<!-- Actions beyond primary click/select/command. -->

### Right-Click / Context Menu

<!-- What does right-click do? Context menu with options? Quick-cancel? Depends on what's selected? -->

### Modifier Keys

<!-- Shift-click, Ctrl-click, Alt-click — what do they do? Are these consistent across all modes? -->

### Double-Click

<!-- Does double-click do anything (e.g., select all of type, open detail panel)? -->

## Drag Behaviors

<!-- What happens when the player clicks and drags? -->

### Drag-to-Select

<!-- Box selection: how does it work? Does it select everything in the box or only specific entity types? -->

### Drag-to-Place

<!-- Placing structures, painting zones, drawing walls. How does the drag preview work? Snap-to-grid? -->

### Drag-to-Assign

<!-- Drag items to stockpiles, drag colonists to tasks? Or is this not supported? -->

### Drag Thresholds

<!-- How many pixels of movement before a click becomes a drag? What prevents accidental drags? -->

## Interaction Patterns

<!-- Common sequences the player performs repeatedly. Define the canonical flow for each. -->

### Select Entity → Inspect

<!-- Click colonist → panel opens showing details. Click structure → panel opens. What info is shown? -->

### Select Entity → Issue Command

<!-- Select colonist → right-click target → command issued. Or: select structure → click action button. -->

### Navigate Layers

<!-- How does the player switch between game layers (normal view, build mode, zone mode, overlay mode)? Hotkeys? Toolbar? What changes visually? What persists across switches? -->

### Cancel Action

<!-- The universal "stop what I'm doing" flow. Escape? Right-click? How does the player know they cancelled successfully? -->

## Modal vs Non-Modal Interaction

<!-- When is the player in a "mode" (build mode, zone painting) vs free interaction? How do they enter/exit modes? Can they inspect entities while in build mode? -->

## Input Feedback

<!-- How does the UI respond to direct input gestures (hover, select, click)? This covers the immediate input→visual response. For system-level feedback (action confirmation, failure messages, alerts, state change notifications), see [feedback-system.md](feedback-system.md). -->

### Hover Feedback

<!-- What happens on mouseover? Highlight? Tooltip? Name label? Is this consistent for all entity types? -->

### Selection Highlight

<!-- How is the selected entity visually distinguished? Outline? Glow? Color change? What about multi-selection? -->

### Confirmation Prompts

<!-- Which actions require confirmation before executing? Demolish? Exile colonist? What's the confirmation UI? This defines WHICH actions need confirmation — the visual/audio response for the confirmation dialog itself is in feedback-system.md. -->

## Camera Interaction

<!-- How does the player control the camera? -->

### Pan

<!-- WASD? Edge scroll? Middle-click drag? -->

### Zoom

<!-- Scroll wheel? +/- keys? How many zoom levels? What changes at each level (detail, labels, overlays)? -->

### Follow / Center

<!-- Can the player follow a colonist? Double-click to center on entity? Hotkey to jump to alert source? -->

## Accessibility Considerations

<!-- Input accessibility requirements. -->

<!-- One-handed play support? Rebindable keys? Mouse-only mode? Keyboard-only mode? Gamepad support? Screen reader hints? -->

## Rules

<!-- Enforceable rules that govern interaction design decisions. -->

1. <!-- Every player action must produce visible feedback within 100ms. -->
2. <!-- Selection is never silently cleared — the player always knows why selection changed. -->
3. <!-- Modal states (build mode, zone mode) are always visually distinct from free interaction. -->
4. <!-- Right-click is always safe — it either cancels or opens context, never executes a destructive action. -->
5. <!-- Drag thresholds prevent accidental drags — a click is not a drag until N pixels of movement. -->
