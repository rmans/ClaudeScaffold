# Workflow — Step-by-Step

> **What this is:** A numbered recipe. Start at Step 1, follow in order. Each step is one command and one sentence of context.

---

## Design

### Step 1 — Create the design document

```
/create-design
```

Fills in `design/design-doc.md` with core vision, pillars, and non-negotiables. This is the highest-authority document — everything else flows from it.

### Step 2 — Iterate on the design document

```
/iterate-design design/design-doc.md
```

Refine through AI-assisted conversation until you're satisfied.

### Step 3 — Auto-review the design document

```
/auto-review scaffold/design/design-doc.md --iterations 3
```

Runs the two-loop Claude+OpenAI review (`doc-review.py`). Fix anything it flags, then move on.

### Step 4 — Create the style guide

```
/create-design style-guide
```

Fills in `design/style-guide.md` — visual identity, tone, art direction.

### Step 5 — Create the color system

```
/create-design color-system
```

Fills in `design/color-system.md` — palette, usage rules, accessibility.

### Step 6 — Create the UI kit

```
/create-design ui-kit
```

Fills in `design/ui-kit.md` — components, layout rules, interaction patterns.

### Step 7 — Iterate and review each design document

Repeat the iterate → review cycle for each document created in Steps 4–6:

```
/iterate-design design/<document>.md
/auto-review scaffold/design/<document>.md --iterations 3
```

---

## Inputs

### Step 8 — Create the action map

```
/create-design action-map
```

Fills in `inputs/action-map.md` — every player action with a unique name.

### Step 9 — Create the default bindings

```
/create-design bindings
```

Fills in `inputs/default-bindings-kbm.md` and `inputs/default-bindings-gamepad.md`.

### Step 10 — Create the input philosophy

```
/create-design input-philosophy
```

Fills in `inputs/input-philosophy.md` — responsiveness targets, dead zones, buffering.

### Step 11 — Iterate and review input documents

```
/iterate-design inputs/<document>.md
/auto-review scaffold/inputs/<document>.md --iterations 3
```

---

## Interfaces & Systems

### Step 12 — Create the interfaces document

```
/create-design interfaces
```

Fills in `design/interfaces.md` — system boundaries, signals, data contracts.

### Step 13 — Create system documents

For each system in your game, create a system design doc:

```
/create-design system
```

Each run creates a new `design/systems/SYS-###.md` with that system's responsibilities, interfaces, and constraints.

### Step 14 — Iterate and review interfaces and systems

```
/iterate-design design/interfaces.md
/iterate-design design/systems/SYS-###.md
/auto-review scaffold/design/interfaces.md --iterations 3
/auto-review scaffold/design/systems/SYS-###.md --iterations 3
```

---

## Engine

### Step 15 — Review engine best practices

Read the documents in `engine/` and update them for your project's needs:

```
/iterate-design engine/godot4-coding-best-practices.md
/iterate-design engine/godot4-scene-architecture.md
```

These constrain *how* code gets written — review them before implementation begins.

---

## Planning

### Step 16 — Define phases

```
/create-design phase
```

Creates `phases/P#-###.md` — scope gates and milestones for your project.

### Step 17 — Write specs

```
/create-design spec
```

Creates `specs/SPEC-###.md` — atomic behavior definitions derived from system designs.

### Step 18 — Write tasks

```
/create-design task
```

Creates `tasks/TASK-###.md` — executable implementation steps, each tied to a spec.

### Step 19 — Define slices

```
/create-design slice
```

Creates `slices/SLICE-###.md` — vertical slice contracts that bundle related tasks.

### Step 20 — Iterate and review planning documents

```
/iterate-design <document>.md
/auto-review scaffold/<document>.md --iterations 3
```

---

## Building

### Step 21 — Implement a task

```
/implement TASK-###
```

Builds the code for one task. The skill reads the task, its linked spec, relevant system docs, and engine constraints, then writes code.

### Step 22 — Record decisions

When a conflict or ambiguity arises during implementation:

```
/write-adr
```

Creates `decisions/ADR-###.md` — captures the decision, alternatives considered, and rationale. ADRs are permanent records.

### Step 23 — Repeat

Continue the implement → ADR cycle (`Steps 21–22`) for each task until the slice is complete. Then move to the next slice.

---

## Reference

| Command | What it does |
|---------|-------------|
| `/create-design` | Create or fill in a design document |
| `/iterate-design <path>` | Refine a document through conversation |
| `/auto-review <path>` | Run two-loop AI review (doc-review.py) |
| `/implement TASK-###` | Build code for a task |
| `/write-adr` | Record an architecture decision |
