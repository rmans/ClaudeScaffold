# Skills Reference

> Man-page reference for all 56 scaffold slash commands. Each entry shows synopsis, description, arguments, examples, and related skills.
>
> **When to use each skill** — see [WORKFLOW.md](WORKFLOW.md) for the step-by-step pipeline order.

---

## Quick Reference

| Skill | Arguments | What it does |
|-------|-----------|-------------|
| `/scaffold-new-design` | `[game-name]` | Fill out the design doc interactively |
| `/scaffold-new-style` | `[style-guide\|color-system\|ui-kit]` | Fill out one Rank 2 style doc |
| `/scaffold-new-system` | `[system-name]` | Create a system design with auto SYS-### ID |
| `/scaffold-new-reference` | `[authority\|interfaces\|states\|entities\|resources\|signals\|balance]` | Populate one reference doc from systems |
| `/scaffold-new-engine` | `[coding\|ui\|input\|scene-architecture\|performance]` | Fill out one engine doc interactively |
| `/scaffold-new-input` | `[action-map\|bindings-kbm\|bindings-gamepad\|ui-navigation\|input-philosophy]` | Fill out one input doc interactively |
| `/scaffold-new-roadmap` | — | Create the project roadmap |
| `/scaffold-new-phase` | `[phase-name]` | Create a phase scope gate with auto P#-### ID |
| `/scaffold-new-slice` | `[slice-name]` | Create a vertical slice with auto SLICE-### ID |
| `/scaffold-new-spec` | `[spec-name]` | Create a behavior spec with auto SPEC-### ID |
| `/scaffold-new-task` | `[task-name]` | Create an implementation task with auto TASK-### ID |
| `/scaffold-bulk-seed-style` | — | Seed all style docs from design doc |
| `/scaffold-bulk-seed-systems` | — | Seed glossary + system stubs from design doc |
| `/scaffold-bulk-seed-references` | — | Seed all 7 reference docs from systems |
| `/scaffold-bulk-seed-engine` | — | Select engine, then seed all 5 engine docs (Godot 4, Unity, Unreal 5, or custom) |
| `/scaffold-bulk-seed-input` | — | Seed all 5 input docs from design doc |
| `/scaffold-bulk-seed-slices` | — | Seed slice stubs from phases + systems + interfaces |
| `/scaffold-bulk-seed-specs` | — | Seed spec stubs from slices + systems + states |
| `/scaffold-bulk-seed-tasks` | — | Seed task stubs from specs + engine docs + signals |
| `/scaffold-review-design` | — | Audit design doc completeness and system index sync |
| `/scaffold-review-style` | `[style-guide\|color-system\|ui-kit\|glossary]` | Audit one Rank 2 doc for quality and design alignment |
| `/scaffold-review-system` | `[SYS-ID\|system-name]` | Audit one system's completeness and registration |
| `/scaffold-review-reference` | `[authority\|interfaces\|states\|entities\|resources\|signals\|balance]` | Audit one reference doc for coverage and traceability |
| `/scaffold-review-engine` | `[coding\|ui\|input\|scene-architecture\|performance]` | Audit one engine doc for quality and design consistency |
| `/scaffold-review-input` | `[action-map\|bindings-kbm\|bindings-gamepad\|ui-navigation\|input-philosophy]` | Audit one input doc for completeness and consistency |
| `/scaffold-review-roadmap` | — | Audit roadmap for phase coverage, ADR currency, vision alignment |
| `/scaffold-review-phase` | `[P#-###\|phase-name]` | Audit one phase's clarity, system alignment, ADR impact |
| `/scaffold-review-slice` | `[SLICE-###\|slice-name]` | Audit one slice's vertical coverage and spec completeness |
| `/scaffold-review-spec` | `[SPEC-###\|spec-name]` | Audit one spec's behavioral clarity and system alignment |
| `/scaffold-review-task` | `[TASK-###\|task-name]` | Audit one task's completeness, engine compliance, sizing |
| `/scaffold-bulk-review-style` | — | Audit all Rank 2 docs + cross-doc consistency |
| `/scaffold-bulk-review-systems` | — | Audit all systems + cross-system consistency |
| `/scaffold-bulk-review-references` | — | Audit all reference docs + cross-doc consistency |
| `/scaffold-bulk-review-engine` | — | Audit all engine docs + cross-doc consistency |
| `/scaffold-bulk-review-input` | — | Audit all input docs + cross-doc consistency |
| `/scaffold-bulk-review-phases` | — | Audit all phases + entry/exit chains + scope coverage |
| `/scaffold-bulk-review-slices` | — | Audit all slices + phase coverage + interface coverage |
| `/scaffold-bulk-review-specs` | — | Audit all specs + system coverage + state machine alignment |
| `/scaffold-bulk-review-tasks` | — | Audit all tasks + file conflicts + ordering sanity |
| `/scaffold-iterate` | `[document-path] [--focus "..."] [--iterations N]` | Adversarial two-loop review via external LLM |
| `/scaffold-complete` | `[document-path\|ID]` | Mark a planning doc as Complete; ripples up through parents |
| `/scaffold-update-doc` | `[doc-name\|path]` | Add, remove, or modify entries in any scaffold doc |
| `/scaffold-validate` | — | Run cross-reference validation across all scaffold docs |
| `/scaffold-playtest-log` | `[session-type]` | Log playtester observations into the feedback tracker |
| `/scaffold-playtest-review` | — | Analyze playtest feedback patterns with priority grid |
| `/scaffold-art-concept` | `[prompt or document-path]` | Generate concept art using DALL-E, informed by style guide and color system |
| `/scaffold-art-ui-mockup` | `[prompt or document-path]` | Generate UI mockup art using DALL-E, informed by UI kit, style guide, and color system |
| `/scaffold-art-character` | `[prompt or document-path]` | Generate character art using DALL-E, informed by style guide and color system |
| `/scaffold-art-environment` | `[prompt or document-path]` | Generate environment art using DALL-E, informed by style guide and color system |
| `/scaffold-art-sprite` | `[prompt or document-path]` | Generate sprite art using DALL-E, informed by style guide and color system |
| `/scaffold-art-icon` | `[prompt or document-path]` | Generate icon art using DALL-E, informed by UI kit, color system, and style guide |
| `/scaffold-art-promo` | `[prompt or document-path]` | Generate promotional art using DALL-E, informed by style guide and color system |
| `/scaffold-audio-music` | `[prompt or document-path]` | Generate music tracks using ElevenLabs, informed by style guide and design doc mood/tone |
| `/scaffold-audio-sfx` | `[prompt or document-path]` | Generate sound effects using ElevenLabs, informed by style guide and design doc game feel |
| `/scaffold-audio-ambience` | `[prompt or document-path]` | Generate ambient audio loops using ElevenLabs, informed by style guide, color system mood, and design doc world/setting |
| `/scaffold-audio-voice` | `[prompt or document-path]` | Generate voice audio using OpenAI TTS, informed by style guide and design doc characters/narrative |

---

## Create

Skills for initializing individual documents from templates. All create skills ask one section at a time, write answers immediately, and set Status to Draft.

---

### /scaffold-new-design

Fill out the design document interactively.

**Synopsis**

    /scaffold-new-design [game-name]

**Description**

Walks through the core design document in 7 passes: Identity, Shape, World, Depth, Narrative, Practical, Accessibility & Scope. Reads design principles, common pitfalls, and genre conventions from `theory/` as advisory context. Writes answers into the document immediately, replacing TODO markers. Reports sections filled vs remaining TODOs at the end.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `game-name` | No | Pre-fills the game title. |

**Examples**

    /scaffold-new-design Verdant
    /scaffold-new-design

**See Also**

`/scaffold-review-design`, `/scaffold-bulk-seed-style`

---

### /scaffold-new-style

Fill out one Rank 2 style document interactively.

**Synopsis**

    /scaffold-new-style [style-guide|color-system|ui-kit]

**Description**

Interactively fills one Rank 2 style document by reading the design doc for context (Tone, Aesthetic Pillars, Camera/Perspective) and theory docs (UX heuristics, color theory, visual design). Asks one section at a time and writes answers immediately. Reports completion and reminds user to run `/scaffold-review-style` when done.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `style-guide\|color-system\|ui-kit` | No | Which style doc to fill. If omitted, asks interactively. |

**Examples**

    /scaffold-new-style style-guide
    /scaffold-new-style color-system
    /scaffold-new-style ui-kit
    /scaffold-new-style

**See Also**

`/scaffold-bulk-seed-style`, `/scaffold-review-style`, `/scaffold-bulk-review-style`

---

### /scaffold-new-system

Create a system design with automatic ID assignment.

**Synopsis**

    /scaffold-new-system [system-name]

**Description**

Creates a system design file at `design/systems/SYS-###-<name>.md` with automatic sequential ID assignment. Reads the design doc to pre-fill Purpose and Player Intent when context exists. Seeds the glossary with candidate terms if the system introduces new terminology. Registers in both `design/systems/_index.md` and the design doc's System Design Index.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `system-name` | No | Name for the system. If omitted, asks interactively. |

**Examples**

    /scaffold-new-system combat
    /scaffold-new-system inventory-management
    /scaffold-new-system

**See Also**

`/scaffold-bulk-seed-systems`, `/scaffold-review-system`, `/scaffold-bulk-review-systems`

---

### /scaffold-new-reference

Populate a single reference document from system designs.

**Synopsis**

    /scaffold-new-reference [authority|interfaces|states|entities|resources|signals|balance]

**Description**

Reads all system designs and proposes entries for the chosen reference document. Extracts candidates based on the document type (e.g., authority from data ownership, signals from system inputs/outputs). Presents all proposed entries as a table for user confirmation. Writes confirmed entries only, preserving existing content.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `authority\|interfaces\|states\|entities\|resources\|signals\|balance` | No | Which reference doc to populate. If omitted, asks interactively. |

**Examples**

    /scaffold-new-reference authority
    /scaffold-new-reference signals
    /scaffold-new-reference

**See Also**

`/scaffold-bulk-seed-references`, `/scaffold-review-reference`, `/scaffold-bulk-review-references`

---

### /scaffold-new-engine

Fill out one engine document interactively.

**Synopsis**

    /scaffold-new-engine [coding|ui|input|scene-architecture|performance]

**Description**

Guides user through filling one engine doc by reading the design doc for scope, style docs for visual/UI context, and input docs for input philosophy. Maps sections to engine-specific patterns. Asks one section at a time and writes answers immediately. Reports sections filled vs remaining TODOs.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `coding\|ui\|input\|scene-architecture\|performance` | No | Which engine doc to fill. If omitted, asks interactively. |

**Examples**

    /scaffold-new-engine coding
    /scaffold-new-engine scene-architecture
    /scaffold-new-engine

**See Also**

`/scaffold-bulk-seed-engine`, `/scaffold-review-engine`, `/scaffold-bulk-review-engine`

---

### /scaffold-new-input

Fill out one input document interactively.

**Synopsis**

    /scaffold-new-input [action-map|bindings-kbm|bindings-gamepad|ui-navigation|input-philosophy]

**Description**

Interactively fills one input document by reading the design doc for context (Player Verbs, Core Loop, Input Feel) and theory docs (UX heuristics for accessibility, game design principles for agency). Asks one section at a time and writes answers immediately. For action-map: walks through namespaces then actions per namespace. For bindings: reads the action-map and proposes defaults, checking for conflicts. For ui-navigation: walks through navigation model, focus flow, and mouse behavior. For input-philosophy: walks through principles, responsiveness targets, accessibility, and constraints.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `action-map\|bindings-kbm\|bindings-gamepad\|ui-navigation\|input-philosophy` | No | Which input doc to fill. If omitted, asks interactively. |

**Examples**

    /scaffold-new-input action-map
    /scaffold-new-input bindings-kbm
    /scaffold-new-input bindings-gamepad
    /scaffold-new-input ui-navigation
    /scaffold-new-input input-philosophy
    /scaffold-new-input

**See Also**

`/scaffold-bulk-seed-input`, `/scaffold-review-input`, `/scaffold-bulk-review-input`

---

### /scaffold-new-roadmap

Create the project roadmap.

**Synopsis**

    /scaffold-new-roadmap

**Description**

Creates the project roadmap by copying Core Fantasy from the design doc as the Vision Checkpoint, then walking through phase definition. Asks about goals, deliverables, and outcome orientation for each phase. Typical progression: Foundation → Systems → Content → Polish → Ship. Reports the completed roadmap overview.

**Examples**

    /scaffold-new-roadmap

**See Also**

`/scaffold-review-roadmap`, `/scaffold-new-phase`

---

### /scaffold-new-phase

Create a phase scope gate with automatic ID assignment.

**Synopsis**

    /scaffold-new-phase [phase-name]

**Description**

Creates a phase scope gate at `phases/P#-###-<name>.md` with automatic sequential ID assignment. Reads the roadmap, design doc, all systems, and all ADRs for impact analysis before defining the phase. Walks through Goal, Entry Criteria (with specific IDs), In Scope, Out of Scope, Deliverables, Exit Criteria, and Dependencies. Registers in `phases/_index.md`.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `phase-name` | No | Name for the phase. If omitted, asks interactively. |

**Examples**

    /scaffold-new-phase foundation
    /scaffold-new-phase content-pipeline
    /scaffold-new-phase

**See Also**

`/scaffold-review-phase`, `/scaffold-bulk-review-phases`, `/scaffold-new-slice`

---

### /scaffold-new-slice

Create a vertical slice with automatic ID assignment.

**Synopsis**

    /scaffold-new-slice [slice-name]

**Description**

Creates a vertical slice at `slices/SLICE-###-<name>.md` with automatic sequential ID assignment. Reads the slice template, slices index, phase files, systems, and interfaces. Asks which phase the slice belongs to (or infers from context). Walks through Goal, Specs Included (marked TBD), Integration Points (referencing `interfaces.md`), Done Criteria, and Demo Script. Registers in `slices/_index.md`.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `slice-name` | No | Name for the slice. If omitted, asks interactively. |

**Examples**

    /scaffold-new-slice core-combat-loop
    /scaffold-new-slice inventory-ui
    /scaffold-new-slice

**See Also**

`/scaffold-bulk-seed-slices`, `/scaffold-review-slice`, `/scaffold-bulk-review-slices`, `/scaffold-new-spec`

---

### /scaffold-new-spec

Create a behavior spec with automatic ID assignment.

**Synopsis**

    /scaffold-new-spec [spec-name]

**Description**

Creates a behavior spec at `specs/SPEC-###-<name>.md` with automatic sequential ID assignment. Reads the spec template, parent slice, parent system design, state transitions, and all ADRs for impact check. Pre-fills from system design where possible (Behavior from Player Actions, Edge Cases from system Edge Cases). Walks through Summary, Preconditions, Behavior, Postconditions, Edge Cases, and Acceptance Criteria. Registers in `specs/_index.md` and parent slice's table.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `spec-name` | No | Name for the spec. If omitted, asks interactively. |

**Examples**

    /scaffold-new-spec player-attack
    /scaffold-new-spec item-pickup
    /scaffold-new-spec

**See Also**

`/scaffold-bulk-seed-specs`, `/scaffold-review-spec`, `/scaffold-bulk-review-specs`, `/scaffold-new-task`

---

### /scaffold-new-task

Create an implementation task with automatic ID assignment.

**Synopsis**

    /scaffold-new-task [task-name]

**Description**

Creates an implementation task at `tasks/TASK-###-<name>.md` with automatic sequential ID assignment. Reads the task template, parent spec, parent system, engine docs, signal registry, entity components, and all ADRs for impact check. Pre-fills implementation steps from spec Behavior, translating to engine patterns. Walks through Objective, Steps, Files Affected, Verification, and Notes. Registers in `tasks/_index.md` and parent slice's Tasks table.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `task-name` | No | Name for the task. If omitted, asks interactively. |

**Examples**

    /scaffold-new-task implement-attack-resolution
    /scaffold-new-task wire-inventory-ui
    /scaffold-new-task

**See Also**

`/scaffold-bulk-seed-tasks`, `/scaffold-review-task`, `/scaffold-bulk-review-tasks`, `/scaffold-complete`

---

## Bulk Seed

Skills for bulk-populating multiple documents from source documents. All bulk seed skills present proposed content for user confirmation and set Status to Draft.

---

### /scaffold-bulk-seed-style

Seed all style docs from the design doc.

**Synopsis**

    /scaffold-bulk-seed-style

**Description**

Reads the completed design doc and bulk-seeds `style-guide.md`, `color-system.md`, and `ui-kit.md` in 3 sequential phases. Phase 1 extracts visual identity and proposes style-guide content. Phase 2 proposes color-system from Aesthetic Pillars and Visual Tone. Phase 3 proposes ui-kit from Player Verbs and Core Loop. Presents each section to user for confirmation; writes confirmed content only.

**Examples**

    /scaffold-bulk-seed-style

**See Also**

`/scaffold-new-style`, `/scaffold-bulk-review-style`

---

### /scaffold-bulk-seed-systems

Seed glossary and system stubs from the design doc.

**Synopsis**

    /scaffold-bulk-seed-systems

**Description**

Reads the completed design doc and bulk-seeds the glossary and system design stubs. Phase 1 extracts candidate glossary terms. Phase 2 identifies systems from Player Verbs, Core Loop, Meta Loop, and Failure States. Phase 3 bulk-creates system files with SYS-### IDs, pre-filling Purpose and Player Intent. Registers in both system index and design doc.

**Examples**

    /scaffold-bulk-seed-systems

**See Also**

`/scaffold-new-system`, `/scaffold-bulk-review-systems`

---

### /scaffold-bulk-seed-references

Seed all 7 reference docs from system designs.

**Synopsis**

    /scaffold-bulk-seed-references

**Description**

Reads all completed system designs and bulk-populates 7 companion docs in order: authority table, interface contracts, state transitions, entity components, resource definitions, signal registry, and balance parameters. Each phase presents proposed entries to user for confirmation. Reports what was added and flags any gaps (systems that didn't contribute, orphaned references).

**Examples**

    /scaffold-bulk-seed-references

**See Also**

`/scaffold-new-reference`, `/scaffold-bulk-review-references`

---

### /scaffold-bulk-seed-engine

Select engine, then seed all 5 engine docs.

**Synopsis**

    /scaffold-bulk-seed-engine

**Description**

Asks which engine the project uses (Godot 4, Unity, Unreal 5, or custom), then creates all 5 engine docs from templates with engine-specific pre-filled conventions. Reads design, style, and UI docs for context. Creates `[engine]-coding`, `-ui`, `-input`, `-scene-architecture`, and `-performance` docs. Updates the engine index.

**Examples**

    /scaffold-bulk-seed-engine

**See Also**

`/scaffold-new-engine`, `/scaffold-bulk-review-engine`

---

### /scaffold-bulk-seed-input

Seed all 5 input docs from the design doc.

**Synopsis**

    /scaffold-bulk-seed-input

**Description**

Reads the completed design doc and bulk-seeds all 5 input documents in 5 sequential phases. Phase 1 extracts player verbs and proposes action-map entries with namespaces. Phase 2 derives input philosophy from the design doc's Input Feel and Accessibility sections. Phase 3 proposes default keyboard/mouse bindings from the action-map. Phase 4 proposes default gamepad bindings. Phase 5 proposes UI navigation model and focus flow from the action-map and UI kit. Presents each phase to user for confirmation; writes confirmed content only.

**Examples**

    /scaffold-bulk-seed-input

**See Also**

`/scaffold-new-input`, `/scaffold-bulk-review-input`

---

### /scaffold-bulk-seed-slices

Seed slice stubs from phases, systems, and interfaces.

**Synopsis**

    /scaffold-bulk-seed-slices

**Description**

Reads all phases, system designs, and interface contracts to bulk-create vertical slice stubs. Identifies slice candidates by grouping In Scope items into end-to-end experiences. Presents all candidates to user for confirmation. Creates SLICE-### files with pre-filled Goals, Integration Points from `interfaces.md`, and suggested specs. Registers in `slices/_index.md`.

**Examples**

    /scaffold-bulk-seed-slices

**See Also**

`/scaffold-new-slice`, `/scaffold-bulk-review-slices`

---

### /scaffold-bulk-seed-specs

Seed spec stubs from slices, systems, and state transitions.

**Synopsis**

    /scaffold-bulk-seed-specs

**Description**

Reads all slices, system designs, and state transitions to bulk-create behavior spec stubs. Extracts spec candidates from slice Specs Included tables and system Player Actions. Checks ADRs for behavior changes. Presents all candidates to user for confirmation. Creates SPEC-### files with pre-filled Summary, Behavior, Edge Cases, and Acceptance Criteria. Registers in `specs/_index.md` and slice tables.

**Examples**

    /scaffold-bulk-seed-specs

**See Also**

`/scaffold-new-spec`, `/scaffold-bulk-review-specs`

---

### /scaffold-bulk-seed-tasks

Seed task stubs from specs, engine docs, and signal registry.

**Synopsis**

    /scaffold-bulk-seed-tasks

**Description**

Reads all specs, engine docs, and signal registry to bulk-create implementation task stubs. Translates each spec to implementation tasks using engine patterns. Determines task ordering within slices (foundational files → core logic → wiring → UI/feedback). Checks ADRs for implementation approach changes. Presents all candidates to user for confirmation. Creates TASK-### files with pre-filled Objective, Steps, and Files Affected. Registers in `tasks/_index.md` and slice Tasks tables.

**Examples**

    /scaffold-bulk-seed-tasks

**See Also**

`/scaffold-new-task`, `/scaffold-bulk-review-tasks`

---

## Review

Skills for auditing individual documents. All review skills are read-only and report completeness, quality, alignment, and prioritized recommendations.

---

### /scaffold-review-design

Audit the design doc for completeness and system index sync.

**Synopsis**

    /scaffold-review-design

**Description**

Reads the design doc and all system designs to audit completeness and consistency. Checks design doc sections (Complete/Partial/Empty), System Index sync between `design-doc.md` and `systems/_index.md`, system file existence, per-system completeness (Purpose, Player Actions, System Resolution as critical sections), and cross-references. Flags unresolved references and issues. Advisory observations from theory docs. Reports recommendations prioritized by impact.

**Examples**

    /scaffold-review-design

**See Also**

`/scaffold-new-design`, `/scaffold-iterate`

---

### /scaffold-review-style

Audit one Rank 2 style doc for quality and design alignment.

**Synopsis**

    /scaffold-review-style [style-guide|color-system|ui-kit|glossary]

**Description**

Reviews a single Rank 2 document for completeness, quality, and consistency with the design doc. Checks each section status (Complete/Partial/Empty), specificity (implementable vs vague), internal consistency (sections agree with each other), and design alignment (visual identity, tone, pillars match). Reads theory docs for advisory UX heuristics, color theory, and visual design context. Reports completeness, quality issues, design alignment, and recommendations.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `style-guide\|color-system\|ui-kit\|glossary` | No | Which style doc to review. If omitted, asks interactively. |

**Examples**

    /scaffold-review-style style-guide
    /scaffold-review-style glossary
    /scaffold-review-style

**See Also**

`/scaffold-new-style`, `/scaffold-bulk-review-style`, `/scaffold-iterate`

---

### /scaffold-review-system

Audit one system's completeness and registration.

**Synopsis**

    /scaffold-review-system [SYS-ID|system-name]

**Description**

Reviews a single system design for completeness, quality, and registration. Checks all 11 sections (Purpose, Player Intent, Player Actions, System Resolution, Failure States, Inputs/Outputs, Non-Responsibilities, Edge Cases, Feel/Feedback, Open Questions) for Complete/Partial/Empty status. Flags implementation leaks, vague content, missing dependencies, and unregistered systems. Verifies registration in both index tables. Advisory observations from theory docs. Reports recommendations.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `SYS-ID\|system-name` | No | System to review (e.g., `SYS-001` or `combat`). If omitted, asks interactively. |

**Examples**

    /scaffold-review-system SYS-001
    /scaffold-review-system combat
    /scaffold-review-system

**See Also**

`/scaffold-new-system`, `/scaffold-bulk-review-systems`, `/scaffold-iterate`

---

### /scaffold-review-reference

Audit one reference doc for coverage and traceability.

**Synopsis**

    /scaffold-review-reference [authority|interfaces|states|entities|resources|signals|balance]

**Description**

Reviews a single reference doc for completeness and cross-system consistency. Checks entry coverage (every system-referenced item registered), traceability (entries link back to systems), and consistency (no duplicates, proper formatting). Flags stale orphaned entries and broken references. Reports entries vs gaps, quality issues, cross-reference gaps, and recommendations.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `authority\|interfaces\|states\|entities\|resources\|signals\|balance` | No | Which reference doc to review. If omitted, asks interactively. |

**Examples**

    /scaffold-review-reference authority
    /scaffold-review-reference signals
    /scaffold-review-reference

**See Also**

`/scaffold-new-reference`, `/scaffold-bulk-review-references`, `/scaffold-iterate`

---

### /scaffold-review-engine

Audit one engine doc for quality and design consistency.

**Synopsis**

    /scaffold-review-engine [coding|ui|input|scene-architecture|performance]

**Description**

Reviews a single engine doc for completeness, quality, and design consistency. Checks section status (Complete/Partial/Empty), engine-specificity (uses engine API names), and no design-layer leaks. Verifies design alignment (implementation approach supports design intent). Flags vague or missing sections and contradictions. Reports completeness, quality issues, design alignment, and recommendations.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `coding\|ui\|input\|scene-architecture\|performance` | No | Which engine doc to review. If omitted, asks interactively. |

**Examples**

    /scaffold-review-engine coding
    /scaffold-review-engine performance
    /scaffold-review-engine

**See Also**

`/scaffold-new-engine`, `/scaffold-bulk-review-engine`, `/scaffold-iterate`

---

### /scaffold-review-input

Audit one input doc for completeness and consistency.

**Synopsis**

    /scaffold-review-input [action-map|bindings-kbm|bindings-gamepad|ui-navigation|input-philosophy]

**Description**

Reviews a single input doc for completeness, quality, and consistency with other input docs. For action-map: checks namespaces, actions, rules. For bindings: verifies every action has a binding, no conflicts, reasonable modifiers. For ui-navigation: checks focus flow, navigation model, mouse behavior. For input-philosophy: checks principles, responsiveness targets, accessibility, constraints. Flags missing bindings and cross-input mismatches.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `action-map\|bindings-kbm\|bindings-gamepad\|ui-navigation\|input-philosophy` | No | Which input doc to review. If omitted, asks interactively. |

**Examples**

    /scaffold-review-input action-map
    /scaffold-review-input bindings-kbm
    /scaffold-review-input

**See Also**

`/scaffold-bulk-review-input`, `/scaffold-iterate`

---

### /scaffold-review-roadmap

Audit the roadmap for phase coverage, ADR currency, and vision alignment.

**Synopsis**

    /scaffold-review-roadmap

**Description**

Reviews the roadmap for completeness, currency, and alignment with the design doc. Checks Vision Checkpoint (matches Core Fantasy), Phase Overview (at least 2 phases with goals), Current Phase, ADR Feedback Log, Completed Phases, and Upcoming Phases. Verifies system and feature coverage (every system in at least one phase), phase progression, scope alignment, and ADR feedback currency (every completed phase's ADRs logged). Reports section completeness, phase coverage, ADR currency, vision alignment, and recommendations.

**Examples**

    /scaffold-review-roadmap

**See Also**

`/scaffold-new-roadmap`, `/scaffold-review-phase`, `/scaffold-bulk-review-phases`

---

### /scaffold-review-phase

Audit one phase's clarity, system alignment, and ADR impact.

**Synopsis**

    /scaffold-review-phase [P#-###|phase-name]

**Description**

Reviews a single phase for clarity, specificity, system alignment, and ADR impact. Checks all 7 sections (Goal, Entry Criteria, In Scope, Out of Scope, Deliverables, Exit Criteria, Dependencies) for Complete/Partial/Empty. Verifies entry criteria use specific IDs (not vague), In Scope items are specific, Goals are outcome-oriented, and Exit Criteria are verifiable. Checks system references exist and ADR impacts are reflected in scope. Verifies registration and downstream slice coverage.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `P#-###\|phase-name` | No | Phase to review (e.g., `P1-001` or `foundation`). If omitted, asks interactively. |

**Examples**

    /scaffold-review-phase P1-001
    /scaffold-review-phase foundation
    /scaffold-review-phase

**See Also**

`/scaffold-new-phase`, `/scaffold-bulk-review-phases`, `/scaffold-iterate`

---

### /scaffold-review-slice

Audit one slice's vertical coverage and spec completeness.

**Synopsis**

    /scaffold-review-slice [SLICE-###|slice-name]

**Description**

Reviews a single slice for coverage, spec completeness, demo script quality, and integration points. Checks all 6 sections (Goal, Specs Included, Tasks, Integration Points, Done Criteria, Demo Script) for Complete/Partial/Empty. Verifies Goal is vertical (crosses system boundaries), Specs cover the goal, Integration Points reference real interfaces from `interfaces.md`, Done Criteria are testable, and Demo Script is followable and exercises all specs/integration points. Verifies spec/task coverage and cross-references.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `SLICE-###\|slice-name` | No | Slice to review (e.g., `SLICE-001` or `core-combat-loop`). If omitted, asks interactively. |

**Examples**

    /scaffold-review-slice SLICE-001
    /scaffold-review-slice core-combat-loop
    /scaffold-review-slice

**See Also**

`/scaffold-new-slice`, `/scaffold-bulk-review-slices`, `/scaffold-iterate`

---

### /scaffold-review-spec

Audit one spec's behavioral clarity and system alignment.

**Synopsis**

    /scaffold-review-spec [SPEC-###|spec-name]

**Description**

Reviews a behavior spec for clarity, completeness, acceptance criteria, and system alignment. Checks all 6 sections (Summary, Preconditions, Behavior, Postconditions, Edge Cases, Acceptance Criteria) for Complete/Partial/Empty. Flags implementation leaks (signals, methods, nodes, classes), vague steps, and non-verifiable preconditions/postconditions. Verifies behavior aligns with parent system design's Player Actions/System Resolution. Checks ADR impacts and registration.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `SPEC-###\|spec-name` | No | Spec to review (e.g., `SPEC-001` or `player-attack`). If omitted, asks interactively. |

**Examples**

    /scaffold-review-spec SPEC-001
    /scaffold-review-spec player-attack
    /scaffold-review-spec

**See Also**

`/scaffold-new-spec`, `/scaffold-bulk-review-specs`, `/scaffold-iterate`

---

### /scaffold-review-task

Audit one task's completeness, engine compliance, and sizing.

**Synopsis**

    /scaffold-review-task [TASK-###|task-name]

**Description**

Reviews an implementation task for completeness, spec alignment, engine pattern compliance, and sizing. Checks all 5 sections (Objective, Steps, Files Affected, Verification, Notes) for Complete/Partial/Empty. Verifies steps are concrete/actionable, use correct engine patterns, files list is realistic, and verification is testable. Flags oversized tasks (>8 steps or >5 files). Checks spec coverage, engine compliance, ADR impacts, and registration.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `TASK-###\|task-name` | No | Task to review (e.g., `TASK-001` or `implement-attack-resolution`). If omitted, asks interactively. |

**Examples**

    /scaffold-review-task TASK-001
    /scaffold-review-task implement-attack-resolution
    /scaffold-review-task

**See Also**

`/scaffold-new-task`, `/scaffold-bulk-review-tasks`, `/scaffold-iterate`, `/scaffold-complete`

---

## Bulk Review

Skills for auditing all documents in a category at once. Bulk reviews check cross-document consistency — the main value over individual reviews.

---

### /scaffold-bulk-review-style

Audit all Rank 2 docs and cross-doc consistency.

**Synopsis**

    /scaffold-bulk-review-style

**Description**

Reviews all 4 Rank 2 docs (style-guide, color-system, ui-kit, glossary) at once for consistency. Per-doc: checks section completeness. Cross-doc checks: Style ↔ Colors (mood alignment), Style ↔ UI Kit (art direction → icon style), Colors ↔ UI Kit (tokens cover states, contrast achievable), Glossary ↔ All (no NOT-column violations), Design Doc ↔ All (Pillars/Tone/Perspective align). Gap analysis and specificity audit. Reports per-doc status, cross-doc consistency, gaps, and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-style

**See Also**

`/scaffold-review-style`, `/scaffold-bulk-seed-style`

---

### /scaffold-bulk-review-systems

Audit all systems and cross-system consistency.

**Synopsis**

    /scaffold-bulk-review-systems

**Description**

Reviews all registered systems at once for completeness and cross-system consistency. Per-system: checks all 11 sections. Cross-system checks: dependency symmetry (if A depends on B, B should output to A), orphan systems (no inputs/outputs), authority conflicts (two systems writing same variable), state coverage (specs align with state machines), glossary compliance, and signal alignment (Inputs/Outputs match signal-registry). Reports per-system details, cross-system consistency, and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-systems

**See Also**

`/scaffold-review-system`, `/scaffold-bulk-seed-systems`

---

### /scaffold-bulk-review-references

Audit all reference docs and cross-doc consistency.

**Synopsis**

    /scaffold-bulk-review-references

**Description**

Reviews all 10 reference docs (authority, interfaces, states, entities, resources, signals, balance, glossary, known-issues, design-debt) at once for consistency. Cross-doc checks: Authority ↔ Entities (ownership matches), Signals ↔ System Outputs (complete correspondence), Interfaces ↔ Authority (non-owners don't push owned data), Resources ↔ Balance Params (related numbers registered), State Transitions ↔ Entities (state machines have fields), Glossary ↔ Everything (terminology correct). Gap analysis and stale entry detection. Reports per-doc status, cross-doc consistency, gaps, and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-references

**See Also**

`/scaffold-review-reference`, `/scaffold-bulk-seed-references`

---

### /scaffold-bulk-review-engine

Audit all engine docs and cross-doc consistency.

**Synopsis**

    /scaffold-bulk-review-engine

**Description**

Reviews all 5 engine docs at once for consistency. Cross-doc checks: Coding ↔ Scene Architecture (naming consistency), Coding ↔ UI (event patterns consistent), UI ↔ Input (focus implementation uses input patterns), UI ↔ Performance (frame budget accounts for UI), Input ↔ Performance (buffering compatible with budget), Scene Architecture ↔ Performance (memory budgets respected), All Docs ↔ Design (implementation supports design intent). Gap analysis and layer boundary check (no design-layer leaks). Reports per-doc status, cross-doc consistency, gaps, and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-engine

**See Also**

`/scaffold-review-engine`, `/scaffold-bulk-seed-engine`

---

### /scaffold-bulk-review-input

Audit all input docs and cross-doc consistency.

**Synopsis**

    /scaffold-bulk-review-input

**Description**

Reviews all 5 input docs at once for consistency. Cross-doc checks: Action Map ↔ Bindings KBM (every action bound), Action Map ↔ Bindings Gamepad (every action bound), Action Map ↔ UI Navigation (ui_ actions have navigation rules), KBM ↔ Gamepad (same actions covered), Input Philosophy ↔ All Docs (principles reflected in bindings), Design Doc ↔ Action Map (player verbs mapped). Gap analysis for unmapped design actions, unbound actions, and missing navigation rules. Layer boundary check. Reports per-doc status, cross-doc consistency, gaps, and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-input

**See Also**

`/scaffold-review-input`

---

### /scaffold-bulk-review-phases

Audit all phases, entry/exit chains, and scope coverage.

**Synopsis**

    /scaffold-bulk-review-phases

**Description**

Reviews all phases at once for roadmap alignment, entry/exit chains, scope coverage, ADR absorption, and dependency graph. Cross-phase checks: Roadmap alignment (every phase in file and roadmap), entry/exit chains (phase N's exit → phase N+1's entry), scope coverage (all systems and features covered), scope overlap (flagging exact duplicates), ADR absorption (deferred work reflected in phases), dependency graph (no cycles), status consistency, and out-of-scope hand-offs (deferred items picked up later). Reports per-phase details, cross-phase consistency, and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-phases

**See Also**

`/scaffold-review-phase`, `/scaffold-review-roadmap`

---

### /scaffold-bulk-review-slices

Audit all slices, phase coverage, and interface coverage.

**Synopsis**

    /scaffold-bulk-review-slices

**Description**

Reviews all slices at once for phase coverage, spec overlap, interface coverage, and vertical completeness. Cross-slice checks: Phase coverage (scope items have slices), spec overlap (specs in multiple slices flagged), interface coverage (every interface exercised), vertical completeness (at least 2 system boundaries per slice), demo consistency (no contradictory assumptions), spec coverage (every spec in a slice), and task completeness (every spec has implementing tasks). Reports per-slice details, cross-slice consistency, and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-slices

**See Also**

`/scaffold-review-slice`, `/scaffold-bulk-seed-slices`

---

### /scaffold-bulk-review-specs

Audit all specs, system coverage, and state machine alignment.

**Synopsis**

    /scaffold-bulk-review-specs

**Description**

Reviews all specs at once for slice coverage, system coverage, layer boundary compliance, state machine alignment, and precondition chains. Cross-spec checks: Slice coverage (spec references match slice tables), system coverage (every system has specs, full Player Actions covered), layer boundary (implementation leaks scanned across all specs), state machine alignment (spec transitions match `state-transitions.md`), precondition chains (postconditions → next spec's preconditions), glossary compliance, ADR currency, and acceptance criteria overlap. Reports per-spec details, cross-spec consistency, implementation leak count, and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-specs

**See Also**

`/scaffold-review-spec`, `/scaffold-bulk-seed-specs`

---

### /scaffold-bulk-review-tasks

Audit all tasks, file conflicts, and ordering sanity.

**Synopsis**

    /scaffold-bulk-review-tasks

**Description**

Reviews all tasks at once for spec coverage, engine consistency, file conflicts, ordering sanity, and sizing. Cross-task checks: Spec coverage (every spec has implementing tasks), engine consistency (consistent patterns across tasks), file conflicts (files created/modified by multiple tasks), ordering sanity (dependencies resolve in order), sizing distribution (median steps/files, flagging outliers), signal alignment (all signals in registry), and ADR currency. Reports per-task details, cross-task consistency, sizing distribution (min/median/max), and recommendations prioritized by blast radius.

**Examples**

    /scaffold-bulk-review-tasks

**See Also**

`/scaffold-review-task`, `/scaffold-bulk-seed-tasks`

---

## Iterate

Adversarial review using an external LLM.

---

### /scaffold-iterate

Run adversarial two-loop review on any scaffold document.

**Synopsis**

    /scaffold-iterate [document-path] [--focus "section or concern"] [--iterations N]

**Description**

Runs adversarial two-loop review using an external LLM. The outer loop (1–5 iterations) requests a fresh review, applies changes, and logs the iteration. The inner loop (up to 5 exchanges per iteration) follows a pattern: reviewer raises issues, Claude evaluates each (AGREE/PUSHBACK/PARTIAL) with project context, reviewer counter-responds, continuing until consensus or max exchanges.

Auto-detects doc type to select a review tier: **Full tier** (5 iterations, all severity) for design, style, system, roadmap, phase, and spec docs; **Lite tier** (1 iteration, HIGH only) for engine, input, slice, and task docs; **Lint tier** (1 iteration, HIGH + accuracy) for reference docs. Gathers context files by type. Applies consensus changes. Updates doc status to Approved if no unresolved HIGH issues remain. Creates a review log in `reviews/`.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `document-path` | No | Path to the document to review. If omitted, asks interactively. |
| `--focus` | No | Narrow the review to a specific section or concern. |
| `--iterations` | No | Override the default iteration count (1–5). |

**Examples**

    /scaffold-iterate design/design-doc.md
    /scaffold-iterate design/systems/SYS-001-combat.md --focus "Failure States"
    /scaffold-iterate specs/SPEC-003-item-pickup.md --iterations 3
    /scaffold-iterate

**See Also**

`/scaffold-review-design`, `/scaffold-review-system`, `/scaffold-review-spec`

---

## Complete

Mark planning-layer documents as Complete with automatic upward rippling.

---

### /scaffold-complete

Mark a planning doc as Complete; ripple status upward through parents.

**Synopsis**

    /scaffold-complete [document-path|ID]

**Description**

Marks planning-layer documents (tasks, specs, slices, phases) as Complete with automatic upward rippling. Applies only to the planning layer — design, style, reference, engine, and theory docs use Approved status and are not eligible.

For tasks: direct Complete (leaf nodes, no children check). For specs, slices, and phases: verifies all children are Complete first (specs check tasks, slices check specs, phases check slices). Sets document status to Complete, then ripples upward — if the target's parent now has all children Complete, auto-marks the parent Complete and continues up the hierarchy. Stops rippling when a parent still has incomplete children. Idempotent: already-Complete docs report status and do nothing.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `document-path\|ID` | No | Document to complete (e.g., `TASK-001`, `SPEC-003`, or file path). If omitted, asks interactively. |

**Examples**

    /scaffold-complete TASK-001
    /scaffold-complete SPEC-003
    /scaffold-complete phases/P1-001-foundation.md
    /scaffold-complete

**See Also**

`/scaffold-review-task`, `/scaffold-review-spec`

---

## Edit

Targeted edits to any scaffold document with automatic cross-reference updates.

---

### /scaffold-update-doc

Add, remove, or modify entries in any scaffold document.

**Synopsis**

    /scaffold-update-doc [doc-name|path]

**Description**

Makes targeted edits to any scaffold document (add, remove, or modify entries or sections). Identifies the target by doc-name, SYS-### ID, or file path. Asks for the action (Add/Remove/Modify) if not specified. For table docs: validates format, maintains ordering (alphabetical for glossary, grouped for balance params). For section docs: replaces TODOs with content. For state machines: manages blocks. Handles complex edits (issue tracking, state machines).

Updates cross-references automatically: glossary term renames propagate, system add/remove/rename updates both indexes, signal/entity/resource changes check related docs. Confirms proposed edit before writing. Reports what changed and any cross-references flagged for manual attention. Never silently breaks references.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `doc-name\|path` | No | Target document (e.g., `glossary`, `SYS-001`, or file path). If omitted, asks interactively. |

**Examples**

    /scaffold-update-doc glossary
    /scaffold-update-doc SYS-001
    /scaffold-update-doc reference/signal-registry.md
    /scaffold-update-doc

---

## Validate

Cross-reference validation across the entire scaffold.

---

### /scaffold-validate

Run cross-reference validation across all scaffold documents.

**Synopsis**

    /scaffold-validate

**Description**

Runs `validate-refs.py` to check referential integrity across all scaffold documents. Reports broken references, missing registrations, glossary NOT-column violations, and orphaned entries. Checks: system IDs registered in `systems/_index.md`, authority ↔ entity ownership, signal emitters/consumers, interface sources/targets, state machine authorities, glossary NOT-column usage, bidirectional system registration (index ↔ design doc), spec ↔ slice coverage, and task ↔ spec links.

Presents results as a summary table with PASS/FAIL per check and lists each failing issue with file, line, and message. Suggests specific fixes for each issue. Read-only — does not modify any files.

**Examples**

    /scaffold-validate

**See Also**

`/scaffold-review-design`, `/scaffold-bulk-review-references`, `/scaffold-update-doc`

---

## Playtest

Skills for capturing and analyzing playtester feedback. Observations are logged with `/scaffold-playtest-log` and analyzed with `/scaffold-playtest-review`.

---

### /scaffold-playtest-log

Log playtester observations into the feedback tracker.

**Synopsis**

    /scaffold-playtest-log [session-type]

**Description**

Captures playtester observations into `decisions/playtest-feedback.md`. Creates or identifies a playtest session, then walks through observations one at a time — Type, Observation, System/Spec, Severity, Frequency. Checks for duplicates before adding (aggregates frequency if the same issue is already logged). After all observations are entered, scans for entries with 3+ reports and prompts to promote them to Patterns per the Rule of Three. Reports entries logged, duplicates merged, and patterns promoted.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `session-type` | No | Session type hint (e.g., `in-person`, `remote`, `self-play`). If omitted, asks interactively. |

**Examples**

    /scaffold-playtest-log in-person
    /scaffold-playtest-log remote
    /scaffold-playtest-log

**See Also**

`/scaffold-playtest-review`, `/scaffold-update-doc`

---

### /scaffold-playtest-review

Analyze playtest feedback patterns with severity x frequency grid.

**Synopsis**

    /scaffold-playtest-review

**Description**

Read-only analysis of `decisions/playtest-feedback.md`. Groups feedback by system to identify hot spots, classifies entries into a severity x frequency priority grid (ACT NOW / WATCH CLOSELY / MONITOR / NOTE & MOVE ON), recommends actions for high-priority entries, cross-references with known issues, design debt, and ADRs for overlaps, checks for stale entries, and produces a delight inventory of positive observations to protect. Does not modify any files.

**Examples**

    /scaffold-playtest-review

**See Also**

`/scaffold-playtest-log`, `/scaffold-review-roadmap`, `/scaffold-new-phase`

---

## Art

Skills for generating visual assets informed by the project's style guide and color system.

---

### /scaffold-art-concept

Generate concept art using DALL-E, informed by the project's style guide and color system.

**Synopsis**

    /scaffold-art-concept [prompt or document-path]

**Description**

Generates concept art using DALL-E, grounded in the project's visual identity. Reads `design/style-guide.md` and `design/color-system.md` to build a style context, then combines it with the user's prompt or a document's visual elements. Supports two modes: freeform (text prompt) and document-driven (reads a scaffold doc and extracts visual elements). Shows the composed prompt for user confirmation before calling the API. Saves images to `art/concept-art/` with kebab-case timestamped filenames and updates the art index.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-art-concept a misty pixel-art village at dawn
    /scaffold-art-concept scaffold/design/systems/SYS-001-combat.md
    /scaffold-art-concept

**See Also**

`/scaffold-new-style`, `/scaffold-review-style`, `/scaffold-art-ui-mockup`, `/scaffold-art-character`, `/scaffold-art-environment`, `/scaffold-art-sprite`, `/scaffold-art-icon`, `/scaffold-art-promo`

---

### /scaffold-art-ui-mockup

Generate UI mockup art using DALL-E, informed by the project's UI kit, style guide, and color system.

**Synopsis**

    /scaffold-art-ui-mockup [prompt or document-path]

**Description**

Generates UI mockup art using DALL-E, grounded in the project's visual identity. Reads `design/ui-kit.md`, `design/style-guide.md`, and `design/color-system.md` to build a style context focused on screen composition, HUD layout, menu flows, and readability. Supports freeform (text prompt) and document-driven (reads a scaffold doc and extracts UI elements) modes. Shows the composed prompt for user confirmation before calling the API. Saves images to `art/ui-mockups/` with kebab-case timestamped filenames. Default size: 1792x1024.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-art-ui-mockup main HUD with health bar, minimap, and hotbar
    /scaffold-art-ui-mockup scaffold/design/ui-kit.md
    /scaffold-art-ui-mockup

**See Also**

`/scaffold-art-concept`, `/scaffold-art-icon`, `/scaffold-new-style`

---

### /scaffold-art-character

Generate character art using DALL-E, informed by the project's style guide and color system.

**Synopsis**

    /scaffold-art-character [prompt or document-path]

**Description**

Generates character art using DALL-E, grounded in the project's visual identity. Reads `design/style-guide.md` and `design/color-system.md` to build a style context, plus checks the design doc for character descriptions. Focuses on silhouette readability, proportions, color identity, expression, and costume design. Supports freeform (text prompt) and document-driven (reads a scaffold doc and extracts character descriptions) modes. Shows the composed prompt for user confirmation before calling the API. Saves images to `art/character-art/` with kebab-case timestamped filenames. Default size: 1024x1024.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-art-character a rogue archer with dark cloak and glowing arrows
    /scaffold-art-character scaffold/design/design-doc.md
    /scaffold-art-character

**See Also**

`/scaffold-art-concept`, `/scaffold-art-sprite`, `/scaffold-new-style`

---

### /scaffold-art-environment

Generate environment art using DALL-E, informed by the project's style guide and color system.

**Synopsis**

    /scaffold-art-environment [prompt or document-path]

**Description**

Generates environment art using DALL-E, grounded in the project's visual identity. Reads `design/style-guide.md` and `design/color-system.md` to build a style context, plus checks the design doc for world/setting descriptions. Focuses on depth, atmosphere, lighting, scale, and walkable vs decorative space. Supports freeform (text prompt) and document-driven (reads a scaffold doc and extracts environment descriptions) modes. Shows the composed prompt for user confirmation before calling the API. Saves images to `art/environment-art/` with kebab-case timestamped filenames. Default size: 1792x1024.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-art-environment a misty forest clearing with ancient ruins
    /scaffold-art-environment scaffold/design/systems/SYS-003-exploration.md
    /scaffold-art-environment

**See Also**

`/scaffold-art-concept`, `/scaffold-art-promo`, `/scaffold-new-style`

---

### /scaffold-art-sprite

Generate sprite art using DALL-E, informed by the project's style guide and color system.

**Synopsis**

    /scaffold-art-sprite [prompt or document-path]

**Description**

Generates sprite art using DALL-E, grounded in the project's visual identity. Reads `design/style-guide.md` and `design/color-system.md` to build a style context focused on pixel art style, limited palette, clean edges, and small-size readability. Supports freeform (text prompt) and document-driven (reads a scaffold doc and extracts sprite subjects) modes. Shows the composed prompt for user confirmation before calling the API. Saves images to `art/sprite-art/` with kebab-case timestamped filenames. Default size: 1024x1024.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-art-sprite warrior idle animation frame, 16-color palette
    /scaffold-art-sprite scaffold/design/systems/SYS-001-combat.md
    /scaffold-art-sprite

**See Also**

`/scaffold-art-concept`, `/scaffold-art-character`, `/scaffold-new-style`

---

### /scaffold-art-icon

Generate icon art using DALL-E, informed by the project's UI kit, color system, and style guide.

**Synopsis**

    /scaffold-art-icon [prompt or document-path]

**Description**

Generates icon art using DALL-E, grounded in the project's visual identity. Reads `design/ui-kit.md`, `design/color-system.md`, and `design/style-guide.md` to build a style context focused on square format, simple silhouette, high contrast, and icon-size readability. Supports freeform (text prompt) and document-driven (reads a scaffold doc and extracts icon subjects) modes. Shows the composed prompt for user confirmation before calling the API. Saves images to `art/icon-art/` with kebab-case timestamped filenames. Default size: 1024x1024.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-art-icon health potion icon, red liquid in glass vial
    /scaffold-art-icon scaffold/reference/entity-components.md
    /scaffold-art-icon

**See Also**

`/scaffold-art-ui-mockup`, `/scaffold-art-concept`, `/scaffold-new-style`

---

### /scaffold-art-promo

Generate promotional art using DALL-E, informed by the project's style guide and color system.

**Synopsis**

    /scaffold-art-promo [prompt or document-path]

**Description**

Generates promotional art using DALL-E, grounded in the project's visual identity. Reads `design/style-guide.md` and `design/color-system.md` to build a style context, plus checks the design doc for identity and vision. Focuses on dramatic composition, marketing appeal, text-safe space for title/logo overlay, and landscape orientation. Supports freeform (text prompt) and document-driven (reads a scaffold doc and extracts visual themes) modes. Shows the composed prompt for user confirmation before calling the API. Saves images to `art/promo-art/` with kebab-case timestamped filenames. Default size: 1792x1024.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-art-promo epic hero banner with dark forest background, text-safe left third
    /scaffold-art-promo scaffold/design/design-doc.md
    /scaffold-art-promo

**See Also**

`/scaffold-art-concept`, `/scaffold-art-environment`, `/scaffold-new-style`

---

## Audio

Skills for generating audio assets informed by the project's style guide, color system, and design doc.

---

### /scaffold-audio-music

Generate music tracks using ElevenLabs, informed by the project's style guide and design doc mood/tone.

**Synopsis**

    /scaffold-audio-music [prompt or document-path]

**Description**

Generates music tracks using ElevenLabs, grounded in the project's tonal identity. Reads `design/style-guide.md` and `design/design-doc.md` to build a musical direction (genre, tempo, mood, instrumentation). Supports two modes: freeform (text prompt) and document-driven (reads a scaffold doc and extracts musical elements). Shows the composed prompt for user confirmation before calling the API. Saves audio to `audio/music/` with kebab-case timestamped filenames. Output format: `.mp3`.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-audio-music upbeat chiptune battle theme, loopable, 120 BPM
    /scaffold-audio-music scaffold/design/design-doc.md
    /scaffold-audio-music

**See Also**

`/scaffold-audio-sfx`, `/scaffold-audio-ambience`, `/scaffold-audio-voice`

---

### /scaffold-audio-sfx

Generate sound effects using ElevenLabs, informed by the project's style guide and design doc game feel.

**Synopsis**

    /scaffold-audio-sfx [prompt or document-path]

**Description**

Generates sound effects using ElevenLabs, grounded in the project's tonal identity. Reads `design/style-guide.md` and `design/design-doc.md` to build a sound design direction (intensity, style, audio character). Focuses on clarity, impact, timing, and game-appropriate intensity. Supports freeform (text prompt) and document-driven (reads a scaffold doc and extracts sound-worthy events) modes. Shows the composed prompt for user confirmation before calling the API. Saves audio to `audio/sfx/` with kebab-case timestamped filenames. Output format: `.mp3`.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-audio-sfx sword slash impact, metallic ring, medium weight
    /scaffold-audio-sfx scaffold/design/systems/SYS-001-combat.md
    /scaffold-audio-sfx

**See Also**

`/scaffold-audio-music`, `/scaffold-audio-ambience`, `/scaffold-audio-voice`

---

### /scaffold-audio-ambience

Generate ambient audio loops using ElevenLabs, informed by the project's style guide, color system mood, and design doc world/setting.

**Synopsis**

    /scaffold-audio-ambience [prompt or document-path]

**Description**

Generates ambient audio loops using ElevenLabs, grounded in the project's world and atmosphere. Reads `design/style-guide.md`, `design/color-system.md`, and `design/design-doc.md` to build an atmospheric direction (environment type, mood, depth, spatial character). Uses the `sfx` subcommand with `--loop` for seamless looping. Focuses on atmosphere, depth, layering, and loop seamlessness. Supports freeform (text prompt) and document-driven (reads a scaffold doc and extracts environment descriptions) modes. Shows the composed prompt for user confirmation before calling the API. Saves audio to `audio/ambience/` with kebab-case timestamped filenames. Output format: `.mp3`.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text prompt, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-audio-ambience misty forest clearing with distant birdsong and gentle wind
    /scaffold-audio-ambience scaffold/design/systems/SYS-003-exploration.md
    /scaffold-audio-ambience

**See Also**

`/scaffold-audio-music`, `/scaffold-audio-sfx`, `/scaffold-audio-voice`

---

### /scaffold-audio-voice

Generate voice audio using OpenAI TTS, informed by the project's style guide and design doc characters/narrative.

**Synopsis**

    /scaffold-audio-voice [prompt or document-path]

**Description**

Generates voice audio using OpenAI TTS, grounded in the project's narrative identity. Reads `design/style-guide.md` and `design/design-doc.md` to build a voice direction (vocal register, energy, pacing, emotional range). Supports selecting from OpenAI TTS voices (alloy, echo, fable, onyx, nova, shimmer) based on character personality. Supports freeform (text to speak) and document-driven (reads a scaffold doc and extracts dialogue/narration) modes. Shows the text and voice parameters for user confirmation before calling the API. Saves audio to `audio/voice/` with kebab-case timestamped filenames. Output format: `.mp3`.

**Arguments**

| Argument | Required | Description |
|----------|----------|-------------|
| `prompt or document-path` | No | Freeform text to speak, or a path to a scaffold doc for document-driven mode. If omitted, asks interactively. |

**Examples**

    /scaffold-audio-voice "The ancient forest holds secrets older than memory."
    /scaffold-audio-voice scaffold/design/design-doc.md
    /scaffold-audio-voice

**See Also**

`/scaffold-audio-music`, `/scaffold-audio-sfx`, `/scaffold-audio-ambience`
