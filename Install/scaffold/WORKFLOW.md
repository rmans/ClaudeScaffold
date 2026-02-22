# Workflow — Step-by-Step

> **What this is:** A numbered recipe. Start at Step 1, follow in order. Each step is one skill command and one sentence of context.

---

## Design Document

### Step 1 — Create the design document

```
/scaffold-new-design [game-name]
```

Fills in `design/design-doc.md` with core vision, pillars, loops, mechanics, and scope. This is the highest-authority document — everything else flows from it.

### Step 2 — Review the design document

```
/scaffold-review-design
```

Audits completeness, system index sync, and cross-references. Fix anything it flags before moving on.

---

## Style Documents

### Step 3 — Seed style docs from design doc

```
/scaffold-bulk-seed-style
```

Reads the design doc and pre-fills `design/style-guide.md`, `design/color-system.md`, and `design/ui-kit.md`. Phases are sequential: style-guide informs color-system, which informs ui-kit.

### Step 4 — Fill in remaining style sections

For any sections the bulk seed couldn't derive, fill them interactively:

```
/scaffold-new-style style-guide
/scaffold-new-style color-system
/scaffold-new-style ui-kit
```

### Step 5 — Review all style docs

```
/scaffold-bulk-review-style
```

Audits all Rank 2 docs for completeness and cross-doc consistency (style ↔ colors ↔ UI kit ↔ glossary ↔ design doc).

---

## Systems

### Step 6 — Seed systems from design doc

```
/scaffold-bulk-seed-systems
```

Extracts terms for the glossary and creates system stubs from the design doc's Player Verbs, Core Loop, and Content Structure.

### Step 7 — Fill in each system design

Open each `design/systems/SYS-###-*.md` file and fill in all sections. To create additional systems not caught by the bulk seed:

```
/scaffold-new-system [system-name]
```

### Step 8 — Review all systems

```
/scaffold-bulk-review-systems
```

Audits all systems for completeness, quality, cross-system consistency (dependency symmetry, authority conflicts, orphan systems, glossary compliance).

---

## Reference Documents

### Step 9 — Seed reference docs from systems

```
/scaffold-bulk-seed-references
```

Reads all system designs and bulk-populates: authority table, interface contracts, state transitions, entity components, resource definitions, signal registry, and balance parameters. Works in 8 sequential phases.

### Step 10 — Review all reference docs

```
/scaffold-bulk-review-references
```

Audits all reference docs for cross-doc consistency (authority ↔ entities, interfaces ↔ signals ↔ systems, resources ↔ balance, states ↔ entities, glossary compliance).

To review a single reference doc in detail:

```
/scaffold-review-reference [authority|interfaces|states|entities|resources|signals|balance]
```

---

## Inputs

### Step 11 — Fill in input documents

Fill in the input documents manually:

- `inputs/action-map.md` — every player action with a unique name
- `inputs/default-bindings-kbm.md` — keyboard/mouse defaults
- `inputs/default-bindings-gamepad.md` — gamepad defaults
- `inputs/input-philosophy.md` — responsiveness targets, dead zones, buffering
- `inputs/ui-navigation.md` — focus flow and navigation

### Step 12 — Review all input docs

```
/scaffold-bulk-review-input
```

Audits all input docs for completeness and cross-doc consistency (action map ↔ bindings, philosophy ↔ all docs, design doc ↔ actions).

To review a single input doc in detail:

```
/scaffold-review-input [action-map|bindings-kbm|bindings-gamepad|ui-navigation|input-philosophy]
```

---

## Engine

### Step 13 — Seed engine docs

```
/scaffold-bulk-seed-engine
```

Asks which engine you're using (Godot 4, Unity, Unreal 5, etc.), then creates all 5 engine docs from templates with engine-specific conventions pre-filled. Use the **Project Overrides** table at the bottom of each doc for project-specific deviations.

### Step 14 — Fill in remaining engine sections

For any sections the bulk seed couldn't pre-fill, fill them interactively:

```
/scaffold-new-engine [coding|ui|input|scene-architecture|performance]
```

### Step 15 — Review all engine docs

```
/scaffold-bulk-review-engine
```

Audits all engine docs for completeness and cross-doc consistency (coding ↔ scene architecture, UI ↔ input, performance ↔ everything).

To review a single engine doc in detail:

```
/scaffold-review-engine [coding|ui|input|scene-architecture|performance]
```

---

## Planning

### Step 16 — Create the roadmap

```
/scaffold-new-roadmap
```

Reads the design doc, systems, and known issues to define the full project arc from start to ship. Creates the living roadmap in `phases/roadmap.md` with phases, goals, and key deliverables. This roadmap is updated after every phase completion.

### Step 17 — Create phases

```
/scaffold-new-phase [phase-name]
```

Creates a phase scope gate in `phases/P#-###-name.md`. Reads the roadmap, all existing ADRs, and known issues. Each phase has a mandatory ADR impact analysis — no phase is created without checking what prior decisions affect its scope.

### Step 18 — Define slices

```
/scaffold-new-slice [slice-name]
```

Defines a vertical slice within a phase — a playable end-to-end chunk that proves systems work together. Reads interfaces and ADRs to scope what the slice must demonstrate. Slices determine the order of implementation.

### Step 19 — Write specs

```
/scaffold-new-spec [spec-name]
```

Creates an atomic behavior spec for a slice. Pre-fills from system designs. Describes BEHAVIOR, not implementation — no engine constructs. Each spec checks ADRs for impacts on the behavior being defined.

### Step 20 — Write tasks

```
/scaffold-new-task [task-name]
```

Creates an implementation task tied to a spec. Reads engine docs and ADRs. This is where engine constructs belong — tasks describe HOW to implement the spec's behavior in the target engine.

---

## Building

### Step 21 — Implement tasks

For each task, read the task doc, its linked spec, relevant system designs, and engine constraints, then write code.

### Step 22 — Record decisions

When a conflict or ambiguity arises during implementation, create `decisions/ADR-###.md` using `templates/decision-template.md`. ADRs are permanent records that feed back into upcoming phases, specs, and tasks.

### Step 23 — Update the roadmap

After completing a phase, follow the Phase Transition Protocol in `phases/roadmap.md`:

1. Review all ADRs filed during the phase.
2. Update the ADR Feedback Log with each ADR's impact.
3. Move the phase to Completed Phases with delivery notes.
4. Re-scope the next phase based on ADR impacts and lessons learned.
5. Update the Phase Overview and set the new Current Phase.

### Step 24 — Repeat

Continue the implement → ADR → update cycle for each task until the slice is complete. Then move to the next slice. After completing all slices in a phase, run the Phase Transition Protocol (Step 23) before starting the next phase.

---

## Quick Reference

| Skill | What it does |
|-------|-------------|
| `/scaffold-new-design` | Fill out the design doc interactively |
| `/scaffold-new-style` | Fill out a style doc (style-guide, color-system, or ui-kit) |
| `/scaffold-new-system` | Create a system design |
| `/scaffold-new-reference` | Seed one reference doc from system designs |
| `/scaffold-new-engine` | Fill out one engine doc interactively |
| `/scaffold-bulk-seed-style` | Seed all style docs from design doc |
| `/scaffold-bulk-seed-systems` | Glossary + all system stubs from design doc |
| `/scaffold-bulk-seed-references` | All reference docs from system designs |
| `/scaffold-bulk-seed-engine` | Select engine, then seed all 5 engine docs |
| `/scaffold-review-design` | Audit design doc completeness |
| `/scaffold-review-style` | Audit one Rank 2 style doc |
| `/scaffold-review-system` | Audit one system's quality |
| `/scaffold-review-reference` | Audit one reference doc |
| `/scaffold-review-engine` | Audit one engine doc |
| `/scaffold-review-input` | Audit one input doc |
| `/scaffold-bulk-review-style` | Audit all Rank 2 docs + cross-doc consistency |
| `/scaffold-bulk-review-systems` | Audit all systems + cross-system consistency |
| `/scaffold-bulk-review-references` | Audit all reference docs + cross-doc consistency |
| `/scaffold-bulk-review-engine` | Audit all engine docs + cross-doc consistency |
| `/scaffold-bulk-review-input` | Audit all input docs + cross-doc consistency |
| `/scaffold-new-roadmap` | Create the project roadmap with phases from start to ship |
| `/scaffold-new-phase` | Create a phase scope gate with ADR impact analysis |
| `/scaffold-new-slice` | Define a vertical slice within a phase |
| `/scaffold-new-spec` | Create an atomic behavior spec for a slice |
| `/scaffold-new-task` | Create an implementation task tied to a spec |
| `/scaffold-update-doc` | Add, remove, or modify entries in any scaffold doc |
