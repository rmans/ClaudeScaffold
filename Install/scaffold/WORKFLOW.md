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

Reads all system designs and bulk-populates: authority table, state transitions, entity components, resource definitions, signal registry, and balance parameters. Works in 6 sequential phases.

### Step 10 — Review all reference docs

```
/scaffold-bulk-review-references
```

Audits all reference docs for cross-doc consistency (authority ↔ entities, signals ↔ systems, resources ↔ balance, states ↔ entities, glossary compliance).

To review a single reference doc in detail:

```
/scaffold-review-reference [authority|states|entities|resources|signals|balance]
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

---

## Engine

### Step 12 — Seed engine docs

Seed engine-specific docs from the templates in `templates/`. Replace `[Engine]` with your engine name and fill in engine-specific conventions:

- `engine/[engine]-coding-best-practices.md`
- `engine/[engine]-ui-best-practices.md`
- `engine/[engine]-input-system.md`
- `engine/[engine]-scene-architecture.md`
- `engine/[engine]-performance-budget.md`

Use the **Project Overrides** table at the bottom of each doc for project-specific deviations.

---

## Planning

### Step 13 — Define phases

Create `phases/P#-###.md` files using `templates/phase-template.md` — scope gates and milestones.

### Step 14 — Write specs

Create `specs/SPEC-###.md` files using `templates/spec-template.md` — atomic behavior definitions derived from system designs.

### Step 15 — Write tasks

Create `tasks/TASK-###.md` files using `templates/task-template.md` — executable implementation steps, each tied to a spec.

### Step 16 — Define slices

Create `slices/SLICE-###.md` files using `templates/slice-template.md` — vertical slice contracts that bundle related tasks.

---

## Building

### Step 17 — Implement tasks

For each task, read the task doc, its linked spec, relevant system designs, and engine constraints, then write code.

### Step 18 — Record decisions

When a conflict or ambiguity arises during implementation, create `decisions/ADR-###.md` using `templates/decision-template.md`. ADRs are permanent records.

### Step 19 — Repeat

Continue the implement → ADR cycle for each task until the slice is complete. Then move to the next slice.

---

## Quick Reference

| Skill | What it does |
|-------|-------------|
| `/scaffold-new-design` | Fill out the design doc interactively |
| `/scaffold-new-style` | Fill out a style doc (style-guide, color-system, or ui-kit) |
| `/scaffold-new-system` | Create a system design |
| `/scaffold-new-reference` | Seed one reference doc from system designs |
| `/scaffold-bulk-seed-style` | Seed all style docs from design doc |
| `/scaffold-bulk-seed-systems` | Glossary + all system stubs from design doc |
| `/scaffold-bulk-seed-references` | All reference docs from system designs |
| `/scaffold-review-design` | Audit design doc completeness |
| `/scaffold-review-style` | Audit one Rank 2 style doc |
| `/scaffold-review-system` | Audit one system's quality |
| `/scaffold-review-reference` | Audit one reference doc |
| `/scaffold-bulk-review-style` | Audit all Rank 2 docs + cross-doc consistency |
| `/scaffold-bulk-review-systems` | Audit all systems + cross-system consistency |
| `/scaffold-bulk-review-references` | Audit all reference docs + cross-doc consistency |
