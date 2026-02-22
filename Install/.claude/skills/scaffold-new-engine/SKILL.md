---
name: scaffold-new-engine
description: Interactively fill out one engine doc. Pick which doc to work on: coding, ui, input, scene-architecture, or performance.
argument-hint: [coding|ui|input|scene-architecture|performance]
allowed-tools: Read, Edit, Grep, Glob
---

# New Engine Document

Guide the user through filling out an engine document: **$ARGUMENTS**

## Supported Documents

| Argument | File Pattern |
|----------|-------------|
| `coding` | `scaffold/engine/[engine]-coding-best-practices.md` |
| `ui` | `scaffold/engine/[engine]-ui-best-practices.md` |
| `input` | `scaffold/engine/[engine]-input-system.md` |
| `scene-architecture` | `scaffold/engine/[engine]-scene-architecture.md` |
| `performance` | `scaffold/engine/[engine]-performance-budget.md` |

## Before Starting

1. **Match the argument** to a supported document above. If no argument or unrecognized, list the options and ask the user which doc to fill out.
2. **Find the target file** by globbing `scaffold/engine/*` to identify the engine prefix (e.g., `godot4`, `unity`, `unreal5`). If no engine docs exist, tell the user to run `/scaffold-bulk-seed-engine` first.
3. **Read the target doc** and identify which sections are already filled (have content beyond `*TODO:*` markers) and which are empty.
4. **Read the design doc** at `scaffold/design/design-doc.md` for context on what the game needs.
5. **Skip sections that are already complete.** Only walk the user through unfilled or partial sections.

## Walkthrough: coding

Work through the coding best practices doc section by section:

1. **Language Conventions** — Ask: *"What are your coding conventions? Typing strictness, formatting rules, naming patterns (snake_case, PascalCase), file naming?"*
2. **Event / Message Patterns** — Ask: *"When do you use the engine's event system vs direct calls? What's the naming convention for events/signals?"*
3. **Globals / Singletons** — Ask: *"What goes into global scope — managers, services, autoloads? What should never be global?"*
4. **Asset / Resource Management** — Ask: *"How do you load assets? Preload vs lazy load? Caching strategy? Streaming for large assets?"*
5. **Error Handling** — Ask: *"How do you handle errors? Assertions in debug, logging levels, error reporting conventions?"*
6. **Testing** — Ask: *"What's the testing approach? Unit tests, integration tests, what framework, what coverage expectations?"*

## Walkthrough: ui

Work through the UI best practices doc section by section:

1. **UI Framework Components** — Ask: *"Which UI components or widgets does the engine provide that you'll use? Any third-party UI libraries?"*
2. **Theme / Styling System** — Ask: *"How do you implement the design's style guide and color system in this engine? Theme resources, CSS, style sheets?"*
3. **Layout System** — Ask: *"What layout containers or systems does the engine provide? How do you handle spacing, margins, alignment?"*
4. **Focus and Navigation** — Ask: *"How do you implement keyboard/gamepad navigation? Focus modes, focus neighbors, tab order?"*
5. **Responsive Design** — Ask: *"How do you handle different resolutions and aspect ratios? Anchors, stretch modes, scaling?"*
6. **UI Performance** — Ask: *"What UI-specific performance concerns does this engine have? Draw calls, overdraw, batching?"*

## Walkthrough: input

Work through the input system doc section by section:

1. **Input System Configuration** — Ask: *"How does the canonical action-map.md translate to this engine's input system? Configuration approach?"*
2. **Action Handling Patterns** — Ask: *"How and where do you poll or listen for input actions? Event-driven, polling, or both?"*
3. **Input Buffering** — Ask: *"Do you need input buffering for responsiveness? If so, how is it implemented in this engine?"*
4. **Device Detection** — Ask: *"How do you detect and switch between input devices — keyboard, gamepad, touch?"*
5. **Remapping** — Ask: *"How do you support runtime key remapping? Engine-native or custom solution?"*

## Walkthrough: scene-architecture

Work through the scene architecture doc section by section:

1. **Scene / Level Structure** — Ask: *"How is the top-level scene organized? Main scene, world scene, UI layer? How are levels structured?"*
2. **Entity / Object Patterns** — Ask: *"How do you compose game objects? Prefabs, scenes, blueprints, components? When to use which?"*
3. **Scene Transitions** — Ask: *"How are scenes loaded, switched, and freed? Loading screens, async loading, streaming?"*
4. **Composition vs Inheritance** — Ask: *"When do you use composition (child objects, components) vs inheritance (subclasses)? What's the default?"*
5. **Dependency Management** — Ask: *"How do objects find and communicate with dependencies? Service locators, dependency injection, direct references?"*

## Walkthrough: performance

Work through the performance budget doc section by section:

1. **Target Specs** — Ask: *"What's the minimum hardware? Target framerate? Target resolution?"*
2. **Frame Budget** — Ask: *"How is the frame time budget allocated? Physics, rendering, scripts, AI — what gets how many milliseconds?"*
3. **Memory Budget** — Ask: *"What are the RAM/VRAM limits? Asset size guidelines? Streaming thresholds?"*
4. **Rendering Budget** — Ask: *"What's the draw call limit? Batching strategy? LOD policy?"*
5. **Profiling** — Ask: *"When and how do you profile? Which tools? What's the performance regression process?"*

## Rules

- **Ask one section at a time.** Do not dump all questions at once.
- **Write answers into the target doc immediately** after the user responds. Replace the `*TODO:*` marker with their answer.
- **Be engine-specific.** Use the engine's actual terminology (nodes, prefabs, blueprints, etc.) — this is the implementation layer, not design.
- **Reference the design doc.** If the design doc has relevant constraints (e.g., Target Platforms for performance), mention them as context.
- **If the user says "skip" or "later"**, leave the TODO marker and move on.
- **If the user gives a short answer**, that's fine. Short and clear beats long and vague.
- **After completing all sections**, report how many sections are filled vs. remaining TODOs.
- **Remind the user** to run `/scaffold-review-engine` when done to audit completeness.
- **Created documents start with Status: Draft.**
