# Scaffold

This is the document pipeline for your game. Every design decision, style rule, system behavior, interface contract, and implementation constraint lives here as a versioned markdown file with a clear authority rank.

## How to Use This

**If you're starting fresh**, follow [WORKFLOW.md](WORKFLOW.md) — it's a 24-step recipe from design doc to code, with a skill command for each step.

**If you're mid-project**, use [_index.md](_index.md) to find the document you need. Every directory has its own `_index.md` — drill down, read only what you need, never load entire directories.

**If two documents conflict**, the higher-ranked document wins. See [doc-authority.md](doc-authority.md) for the full precedence chain.

## Key Files

| File | What It Does |
|------|-------------|
| [_index.md](_index.md) | Master entry point — directory map, ID system, retrieval protocol |
| [doc-authority.md](doc-authority.md) | Precedence rules — which document wins when they conflict |
| [WORKFLOW.md](WORKFLOW.md) | Step-by-step recipe — 24 steps from design through implementation |
| [SKILLS.md](SKILLS.md) | Man-page reference — all 45 skills with arguments, descriptions, and examples |

## The Pipeline

```
Design Doc → Style Docs → Systems → Reference Docs → Engine Docs
    ↓
Roadmap → Phases → Slices → Specs → Tasks → Code
    ↑                                         |
    └──────── ADR Feedback Loop ──────────────┘
```

The top row defines the game. The bottom row builds it. ADRs close the loop — when implementation reality conflicts with the plan, decisions feed back into upcoming phases, specs, and tasks.

## Document Authority (highest wins)

| Rank | Document | What It Controls |
|------|----------|-----------------|
| 1 | `design/design-doc.md` | Core vision, non-negotiables |
| 2 | `design/style-guide.md`, `color-system.md`, `ui-kit.md`, `glossary.md` | Visual identity, terminology |
| 3 | `inputs/*` | Player actions and bindings |
| 4 | `design/interfaces.md`, `authority.md` | System contracts, data ownership |
| 5 | `design/systems/SYS-###`, `state-transitions.md` | Per-system behavior, state machines |
| 6 | `reference/*` | Signals, entities, resources, balance |
| 7 | `phases/P#-###` | Scope and milestones |
| 8 | `specs/SPEC-###` | Atomic testable behaviors |
| 9 | `tasks/TASK-###` | Implementation steps |
| 10 | `engine/*` | Engine-specific constraints |
| 11 | `theory/*` | Advisory only — never authoritative |

## Directory Overview

| Directory | Layer | Rank | What Goes Here |
|-----------|-------|------|---------------|
| `design/` | Canon | 1–5 | Vision, style, colors, UI, glossary, systems, interfaces, authority, state machines |
| `inputs/` | Canon | 3 | Action map, keyboard/mouse bindings, gamepad bindings, navigation, input philosophy |
| `reference/` | Reference | 6 | Signal registry, entity components, resource definitions, balance params |
| `decisions/` | History | — | ADRs, known issues, design debt |
| `phases/` | Scope | 7 | Roadmap, phase scope gates |
| `specs/` | Behavior | 8 | Atomic behavior specs tied to slices |
| `tasks/` | Execution | 9 | Implementation tasks tied to specs |
| `slices/` | Integration | — | Vertical slice contracts within phases |
| `engine/` | Implementation | 10 | Engine-specific best practices and constraints |
| `theory/` | Advisory | 11 | Game design principles, UX heuristics, architecture patterns — no authority |
| `templates/` | Meta | — | Templates for all document types and engine docs |
| `tools/` | Tooling | — | Scripts and utilities |

## Rules

1. **Authority is law.** Higher-ranked documents always win. Code never "works around" higher-level intent. To change a higher document, file an ADR.
2. **Layers don't mix.** Design docs describe *what*. Engine docs describe *how*. Theory docs advise. A single document never crosses layers.
3. **IDs are permanent.** Once assigned, an ID (`SYS-001`, `SPEC-003`, `TASK-012`) never changes, even if the document is renamed or moved.
4. **Single writer per variable.** Every piece of game data has exactly one owning system defined in `design/authority.md`. No system writes to another system's data without an ADR.
5. **ADRs are the feedback mechanism.** When implementation conflicts with design, file an ADR. ADRs feed back into the roadmap, re-scope phases, and update specs. Never silently deviate.
6. **Theory informs, never dictates.** Documents in `theory/` provide advisory context. Skills read them when creating and reviewing documents, but they carry no authority.

## Creating Documents

Use the skill commands — they pre-fill from higher-authority documents and register in the correct `_index.md` automatically.

To create manually:

1. Pick the template from [templates/](templates/_index.md).
2. Assign the next sequential ID for that type.
3. Create the file in the correct directory (not in `templates/`).
4. Register it in the directory's `_index.md`.

## Retrieval Protocol

Never load entire directories. Follow this protocol:

1. Start at [_index.md](_index.md) to find the correct directory.
2. Open the directory's `_index.md` to find the specific document.
3. Read only the document(s) you need.
4. If two documents conflict, the higher-authority document wins.
