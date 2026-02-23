# CLAUDE.md

This project uses ClaudeScaffold — a document-driven pipeline for game development. Every design decision, system behavior, and implementation constraint lives in `scaffold/` as a versioned markdown file with a clear authority rank.

## Rules

1. **Document authority is law.** When documents conflict, the higher-ranked document wins. Code must never "work around" higher-level intent. If an implementation would violate a design document, the implementation is wrong — file an ADR to change the document instead.
2. **Design defines WHAT, engine defines HOW.** Documents in `scaffold/design/` describe what the game is. Documents in `scaffold/engine/` describe how to build it. Never mix layers.
3. **Single writer per variable.** Every piece of game data has exactly one owning system defined in `scaffold/design/authority.md`. No system may write to another system's data without an ADR.
4. **Use canonical terminology.** Terms defined in `scaffold/design/glossary.md` are mandatory. Use the exact term — never synonyms from the NOT column.
5. **Systems are behavior, not implementation.** System designs in `scaffold/design/systems/` describe player-visible behavior. No signals, methods, nodes, or class names in system docs.
6. **Theory informs, never dictates.** Documents in `scaffold/theory/` provide advisory context. Read them when creating or reviewing, but they carry no authority.
7. **ADRs are the feedback mechanism.** When implementation conflicts with design, file an ADR. ADRs feed back into upcoming phases, specs, and tasks. Never silently deviate from the plan.

## Retrieval Protocol

Never load entire directories. Follow this protocol:

1. Start at `scaffold/_index.md` to locate the correct directory.
2. Open the directory's `_index.md` to find the specific document.
3. Read only the document(s) you need.
4. If two documents conflict, the higher-authority document wins (see `scaffold/doc-authority.md`).

## Authority Chain (highest wins)

| Rank | Document | Layer |
|------|----------|-------|
| 1 | `design/design-doc.md` | Canon — core vision |
| 2 | `design/style-guide.md`, `color-system.md`, `ui-kit.md`, `glossary.md` | Canon — visual style, colors, UI, terminology |
| 3 | `inputs/*` | Canon — input actions and bindings |
| 4 | `design/interfaces.md`, `design/authority.md` | Canon — contracts, data ownership |
| 5 | `design/systems/SYS-###`, `design/state-transitions.md` | Canon — systems, states |
| 6 | `reference/*` | Reference — data tables |
| 7 | `phases/P#-###` | Scope — phase gates |
| 8 | `specs/SPEC-###` | Behavior — atomic specs |
| 9 | `tasks/TASK-###` | Execution — implementation steps |
| 10 | `engine/*` | Implementation — engine constraints |
| 11 | `theory/*` | Advisory only — no authority |

## Key Directories

- `scaffold/design/` — What the game is: vision, style, colors, UI, glossary, systems, interfaces, authority, states
- `scaffold/inputs/` — Player input definitions: action maps, bindings, navigation, input philosophy
- `scaffold/reference/` — Canonical data tables: signals, entities, resources, balance
- `scaffold/decisions/` — ADRs, known issues, design debt
- `scaffold/phases/` — Roadmap and phase scope gates
- `scaffold/specs/` — Atomic behavior specs tied to slices
- `scaffold/tasks/` — Implementation tasks tied to specs
- `scaffold/slices/` — Vertical slice contracts within phases
- `scaffold/engine/` — Engine-specific constraints (seeded from templates)
- `scaffold/theory/` — Advisory reference: game design, UX, architecture patterns (no authority)
- `scaffold/reviews/` — Adversarial review logs from `/scaffold-iterate`
- `scaffold/templates/` — Templates for all document types and engine docs

## When Creating or Modifying Systems

- Use the template at `scaffold/templates/system-template.md`.
- Assign sequential SYS-### IDs — never skip or reuse.
- Register in both `scaffold/design/systems/_index.md` AND the System Design Index in `scaffold/design/design-doc.md`.
- Write in player-visible behavior only. Technical contracts belong in `scaffold/design/interfaces.md` and `scaffold/reference/signal-registry.md`.

## When Planning (Phases, Slices, Specs, Tasks)

- Follow the order: Roadmap → Phases → Slices → Specs → Tasks.
- Before creating a phase, spec, or task, read all ADRs filed during prior work. ADRs may change scope.
- Slices define vertical end-to-end chunks within a phase. Specs define behavior within a slice. Tasks implement specs.
- Specs describe BEHAVIOR (what it does). Tasks describe IMPLEMENTATION (how to build it in the engine).
- After completing a phase, follow the Phase Transition Protocol in `scaffold/phases/roadmap.md` to update the roadmap.

## Document Status

Every scaffold document carries a `> **Status:**` field in its blockquote header. Values: `Draft | Review | Approved | Complete`.

- **Draft** — set automatically when a document is created (via templates and create/seed skills).
- **Review** — set manually by the user when the document is ready for adversarial review.
- **Approved** — set automatically by `/scaffold-iterate` after a successful adversarial review (consensus reached, no unresolved HIGH issues).
- **Complete** — set by `/scaffold-complete` when implementation is done and verified. Applies to planning-layer docs only (phases, slices, specs, tasks). Ripples upward: when all tasks for a spec are Complete, the spec becomes Complete, and so on through slices and phases.

ADRs use their own status lifecycle (`Proposed | Accepted | Deprecated | Superseded`) and are not part of this system.

## Workflow

Follow the step-by-step recipe in `scaffold/WORKFLOW.md` for the full 24-step pipeline from design doc to implementation.

## When Resolving Conflicts

- Higher-ranked document always wins.
- File an ADR in `scaffold/decisions/` to change a higher-authority document.
- Log unresolved questions in `scaffold/decisions/known-issues.md`.
- Log intentional compromises in `scaffold/decisions/design-debt.md`.
