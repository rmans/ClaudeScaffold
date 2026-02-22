---
name: scaffold-bulk-seed-engine
description: Ask which engine the project uses, then seed all 5 engine docs from templates with engine-specific conventions. Use at project setup.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Engine Documents

Ask the user which engine they're using, then create all 5 engine docs from templates with engine-specific conventions pre-filled.

## Phase 1 — Select Engine

1. **Ask the user:** *"Which engine is this project using?"*
   - Offer common options: Godot 4, Unity, Unreal Engine 5, custom/other
   - If custom, ask for a short name to use in filenames (e.g., `custom`, `bevy`, `monogame`)
2. **Derive the filename prefix** from the engine choice:
   - Godot 4 → `godot4`
   - Unity → `unity`
   - Unreal Engine 5 → `unreal5`
   - Custom → whatever the user provides (lowercase, hyphenated)

## Phase 2 — Check for Existing Engine Docs

1. **Glob** `scaffold/engine/*` to see if engine docs already exist.
2. If engine docs exist, warn the user and ask if they want to overwrite or skip.
3. If skipping, stop and report what already exists.

## Phase 3 — Read Context

1. **Read the design doc** at `scaffold/design/design-doc.md` for context — especially Target Platforms, Input Feel, and Camera/Perspective.
2. **Read the style-guide** at `scaffold/design/style-guide.md` for visual style context.
3. **Read the ui-kit** at `scaffold/design/ui-kit.md` for UI implementation context.

## Phase 4 — Create Engine Docs

For each of the 5 engine templates:

1. **Read the template** from `scaffold/templates/`:
   - `engine-coding-template.md`
   - `engine-ui-template.md`
   - `engine-input-template.md`
   - `engine-scene-architecture-template.md`
   - `engine-performance-template.md`

2. **Create the file** in `scaffold/engine/` with the engine prefix:
   - `[engine]-coding-best-practices.md`
   - `[engine]-ui-best-practices.md`
   - `[engine]-input-system.md`
   - `[engine]-scene-architecture.md`
   - `[engine]-performance-budget.md`

3. **Replace `[Engine]`** in the title and any references with the actual engine name.

4. **Pre-fill engine-specific conventions** where possible. Use well-known conventions for the selected engine:

   **For Godot 4:**
   - Language Conventions → GDScript typing, snake_case, static typing preferred
   - Event Patterns → Signals for decoupling, direct calls for parent-child
   - Globals → Autoloads for managers, avoid excessive autoloads
   - UI Framework → Control nodes, Theme resources
   - Input System → InputMap, _unhandled_input for gameplay, _input for UI
   - Scene Architecture → Scene tree, packed scenes, node composition
   - Performance → 60fps target, monitor with Profiler and Monitor panels

   **For Unity:**
   - Language Conventions → C#, PascalCase methods, camelCase fields, [SerializeField]
   - Event Patterns → UnityEvents, C# events, delegates
   - Globals → ScriptableObject singletons, avoid static managers
   - UI Framework → UI Toolkit or UGUI, USS stylesheets
   - Input System → New Input System, PlayerInput component
   - Scene Architecture → Prefabs, ScriptableObjects, additive scene loading
   - Performance → 60fps target, Profiler window, frame debugger

   **For Unreal Engine 5:**
   - Language Conventions → C++ and Blueprints, UE naming conventions (F, U, A prefixes)
   - Event Patterns → Delegates, multicast delegates, Blueprint events
   - Globals → Game Instance, Subsystems
   - UI Framework → UMG (Unreal Motion Graphics), Slate for C++
   - Input System → Enhanced Input System, Input Mapping Contexts
   - Scene Architecture → Levels, sublevels, world partition, actor components
   - Performance → 60fps target, Unreal Insights, stat commands

   **For other engines:** Leave sections as TODO with engine name in the title. The user will fill them in with `/scaffold-new-engine`.

5. **Present proposed pre-fill content** to the user for each doc before writing.
6. **Ask the user to confirm, edit, or reject** each doc's content.

## Phase 5 — Update Engine Index

1. **Update** `scaffold/engine/_index.md` to list the newly created docs with the correct engine prefix and descriptions.

## Phase 6 — Report

Summarize what was created:
- Engine selected
- Number of docs created
- Number of sections pre-filled vs. left as TODO
- Remind the user of next steps: fill in remaining TODOs with `/scaffold-new-engine`, then run `/scaffold-bulk-review-engine` to audit

## Rules

- **Never write without confirmation.** Present proposed content before writing each doc.
- **Be engine-specific.** Pre-filled content should use the engine's actual API names, patterns, and terminology — this is the implementation layer.
- **If unsure about an engine's conventions**, leave the section as TODO rather than guessing wrong.
- **Preserve any existing engine docs.** If some docs already exist, only create the missing ones (unless user explicitly wants to overwrite).
- **Pre-filled content is a starting point.** Tell the user to review and refine — engine conventions evolve.
- **Update the engine index** to reflect the actual files created.
