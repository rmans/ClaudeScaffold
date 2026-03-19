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
| 2 | `design/style-guide.md`, `color-system.md`, `ui-kit.md`, `glossary.md`, `interaction-model.md`, `feedback-system.md`, `audio-direction.md` | Canon — visual identity, terminology, interaction, feedback, audio |
| 3 | `inputs/*` | Canon — input actions and bindings |
| 4 | `design/architecture.md`, `design/interfaces.md`, `design/authority.md` | Canon — engineering conventions, contracts, data ownership |
| 5 | `design/systems/SYS-###`, `design/state-transitions.md` | Canon — systems, states |
| 6 | `reference/*` | Reference — data tables |
| 7 | `phases/roadmap.md`, `phases/P#-###` | Scope — roadmap and phase gates |
| 8 | `slices/SLICE-###` | Integration — vertical slice contracts |
| 9 | `specs/SPEC-###` | Behavior — atomic specs |
| 10 | `engine/*` | Implementation — engine constraints |
| 11 | `tasks/TASK-###` | Execution — implementation steps |
| — | `theory/*` | Advisory only — no authority |
| — | `decisions/*` | Pipeline influence — drives changes to ranked docs (see `scaffold/doc-authority.md` Decision Influence Model) |

## Key Directories

- `scaffold/design/` — What the game is: vision, style, colors, UI, glossary, systems, interfaces, authority, states
- `scaffold/inputs/` — Player input definitions: action maps, bindings, navigation, input philosophy
- `scaffold/reference/` — Canonical data tables: signals, entities, resources, balance
- `scaffold/decisions/` — ADRs, known issues, design debt, playtest feedback
- `scaffold/phases/` — Roadmap and phase scope gates
- `scaffold/specs/` — Atomic behavior specs tied to slices
- `scaffold/tasks/` — Implementation tasks tied to specs
- `scaffold/slices/` — Vertical slice contracts within phases
- `scaffold/engine/` — Engine-specific constraints (seeded from templates)
- `scaffold/theory/` — Advisory reference: game design, UX, architecture patterns (no authority)
- `scaffold/decisions/review/` — Adversarial review logs from `/scaffold-iterate`
- `scaffold/audio/` — Generated audio from audio skills (music, SFX, ambience, voice)
- `scaffold/templates/` — Templates for all document types and engine docs

## When Creating or Modifying Systems

- Use the template at `scaffold/templates/system-template.md`.
- Assign sequential SYS-### IDs — never skip or reuse.
- Register in both `scaffold/design/systems/_index.md` AND the System Design Index in `scaffold/design/design-doc.md`.
- Write in player-visible behavior only. Technical contracts belong in `scaffold/design/interfaces.md` and `scaffold/reference/signal-registry.md`.

## When Planning (Phases, Slices, Specs, Tasks)

- Follow the order: Roadmap → Phases → Slices → Specs → Tasks.
- Before creating a phase, spec, or task, read all ADRs filed during prior work. ADRs may change scope.
- Before creating a phase, read `scaffold/decisions/playtest-feedback.md` for Pattern-status entries. Playtest patterns may affect phase scope alongside ADRs.
- Slices define vertical end-to-end chunks within a phase. Specs define behavior within a slice. Tasks implement specs.
- Specs describe BEHAVIOR (what it does). Tasks describe IMPLEMENTATION (how to build it in the engine).
- After completing a phase, follow the Phase Transition Protocol in `scaffold/phases/roadmap.md` to update the roadmap.

## Document Status

Every scaffold document carries a `> **Status:**` field in its blockquote header. Values: `Draft | Review | Approved | Complete | Deprecated`.

- **Draft** — set automatically when a document is created (via templates and create/seed skills).
- **Review** — set manually by the user when the document is ready for adversarial review.
- **Approved** — set automatically by `/scaffold-iterate` after a successful adversarial review (consensus reached, no unresolved HIGH issues).
- **Complete** — set by `/scaffold-complete` when implementation is done and verified. Applies to planning-layer docs only (phases, slices, specs, tasks). Ripples upward: when all tasks for a spec are Complete, the spec becomes Complete, and so on through slices and phases.
- **Deprecated** — set via ADR when a document is no longer active. The document remains in its directory (IDs are permanent) but reviews flag references to it.

ADRs use their own status lifecycle (`Proposed | Accepted | Deprecated | Superseded`) and are not part of this system.

### Document Date Tracking

Every scaffold document carries `> **Created:**`, `> **Last Updated:**`, and `> **Changelog:**` fields in its blockquote header (ADRs use `> **Date:**` instead of `> **Created:**`).

**When creating a document** (seed, new, init skills): set `Created` and `Last Updated` to today's date. Add an initial Changelog entry: `- YYYY-MM-DD: Created.`

**When editing a document** (fix, revise, iterate, triage, approve, complete, update-doc, implement-task, code-review skills): update `Last Updated` to today's date. Append a Changelog entry describing what changed and **which decision doc triggered the change**: `- YYYY-MM-DD: [brief description] ([decision doc reference]).` Keep entries concise — one line per change, not per line edited. The decision doc reference closes the traceability loop: decision docs point to which ranked docs changed, ranked docs point back to which decision doc caused the change.

**Changelog entry examples:**
- `- 2026-03-18: Created.`
- `- 2026-03-19: Fixed authority.md alignment — added NeedsSystem as mood reader (REVISION-references-2026-03-19).`
- `- 2026-03-20: Status → Approved after iterate-spec pass (ITERATE-spec-SPEC-042-2026-03-20).`
- `- 2026-03-21: Resolved constrained TODO — tick model locked in architecture.md (ADR-004).`
- `- 2026-03-22: Added save format versioning section (KI-011 resolution).`
- `- 2026-03-23: Narrowed scope — removed expedition system (DD-005 payoff, TRIAGE-SLICE-009-2026-03-23).`

**Do not back-fill dates on existing docs.** Documents created before this rule will gain these fields naturally when next edited by a skill. Skills should add the fields if they're missing during any edit pass.

### Document Influence Map

Before creating or revising any scaffold document, check the **Document Influence Map** in `scaffold/doc-authority.md` to identify what upstream docs should be read as context. The map defines "Influenced By" (what to read) and "Influences" (what reads this doc) for every document type. Skills with explicit Context Files tables may be a subset — the influence map is the complete reference. When in doubt, read the map.

## Workflow

Follow the step-by-step recipe in `scaffold/WORKFLOW.md` for the full 24-step pipeline from design doc to implementation.

## When Resolving Conflicts

- Higher-ranked document always wins.
- File an ADR in `scaffold/decisions/` to change a higher-authority document.
- Log unresolved questions in `scaffold/decisions/known-issues.md`.
- Log intentional compromises in `scaffold/decisions/design-debt.md`.
