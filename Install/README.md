# ClaudeScaffold — Installation

This is the installable overlay. Copy its contents into any game project to give Claude Code a structured document pipeline, strict design authority, and 39 skills that automate the workflow from concept to code.

## What Gets Installed

```
your-project/
├── .claude/skills/       ← 39 slash commands (create, seed, review, iterate, edit)
├── scaffold/             ← Document pipeline with indexes and templates
└── CLAUDE.md             ← Rules that tell Claude Code how to use the scaffold
```

**`CLAUDE.md`** — Teaches Claude Code the scaffold rules: document authority, layer separation, retrieval protocol, and conflict resolution. This is what makes Claude follow the pipeline instead of guessing.

**`scaffold/`** — A structured document hierarchy with 11 authority ranks. Every design decision, style rule, system behavior, interface contract, and implementation constraint has a home. Start at `scaffold/_index.md` — it's the master entry point.

**`.claude/skills/`** — 39 slash commands that automate document creation, bulk seeding, review audits, adversarial iteration, and editing. Skills read higher-authority documents to pre-fill lower ones, check ADRs before scoping new work, and cross-reference everything.

## Prerequisites

- [Claude Code CLI](https://claude.ai/code)
- A game project (new or existing)

## Install

```bash
# From the ClaudeScaffold repo
cp -r Install/.claude /path/to/your/project/
cp -r Install/scaffold /path/to/your/project/
cp Install/CLAUDE.md /path/to/your/project/
```

## After Installing

Follow the pipeline in order. Each step builds on the last.

### Phase 1 — Define the game

```
/scaffold-new-design              ← core vision, pillars, mechanics, loops, scope
/scaffold-bulk-seed-style         ← seed style-guide, color-system, ui-kit from design doc
/scaffold-bulk-seed-systems       ← glossary + system stubs from design doc
```

Fill in each system design manually, then:

```
/scaffold-bulk-seed-references    ← extract signals, entities, resources, balance params
/scaffold-bulk-seed-engine        ← select your engine, seed all 5 engine docs
```

### Phase 2 — Review everything

```
/scaffold-review-design           ← audit the design doc
/scaffold-bulk-review-style       ← audit all style docs + cross-consistency
/scaffold-bulk-review-systems     ← audit all systems + cross-consistency
/scaffold-bulk-review-references  ← audit all reference docs + cross-consistency
/scaffold-bulk-review-engine      ← audit all engine docs + cross-consistency
/scaffold-bulk-review-input       ← audit all input docs + cross-consistency
```

For deeper adversarial review using an external LLM:

```
/scaffold-iterate <document-path>
```

Fix anything the reviews flag before moving on.

### Phase 3 — Plan and build

```
/scaffold-new-roadmap             ← define phases from start to ship
/scaffold-new-phase [name]        ← create a phase scope gate (checks ADRs)
/scaffold-new-slice [name]        ← define a vertical slice within the phase
/scaffold-new-spec [name]         ← write an atomic behavior spec for the slice
/scaffold-new-task [name]         ← create an implementation task tied to the spec
```

Or bulk-seed planning docs from higher-level documents:

```
/scaffold-bulk-seed-slices        ← seed slice stubs from phases + interfaces
/scaffold-bulk-seed-specs         ← seed spec stubs from slices + system designs
/scaffold-bulk-seed-tasks         ← seed task stubs from specs + engine docs
```

Review planning docs for completeness and cross-doc consistency:

```
/scaffold-review-roadmap          ← audit roadmap completeness and ADR currency
/scaffold-bulk-review-phases      ← audit all phases + entry/exit chains
/scaffold-bulk-review-slices      ← audit all slices + phase/interface coverage
/scaffold-bulk-review-specs       ← audit all specs + system/state alignment
/scaffold-bulk-review-tasks       ← audit all tasks + file conflicts + ordering
```

Build. When implementation conflicts with the plan, file an ADR. After completing a phase, ADRs feed back into the roadmap and re-scope upcoming work.

See `scaffold/WORKFLOW.md` for the full 24-step recipe.

## All 39 Skills

| Category | Skills |
|----------|--------|
| **Create** | `new-design`, `new-style`, `new-system`, `new-reference`, `new-engine`, `new-roadmap`, `new-phase`, `new-slice`, `new-spec`, `new-task` |
| **Bulk seed** | `bulk-seed-style`, `bulk-seed-systems`, `bulk-seed-references`, `bulk-seed-engine`, `bulk-seed-slices`, `bulk-seed-specs`, `bulk-seed-tasks` |
| **Review** | `review-design`, `review-style`, `review-system`, `review-reference`, `review-engine`, `review-input`, `review-roadmap`, `review-phase`, `review-slice`, `review-spec`, `review-task` |
| **Bulk review** | `bulk-review-style`, `bulk-review-systems`, `bulk-review-references`, `bulk-review-engine`, `bulk-review-input`, `bulk-review-phases`, `bulk-review-slices`, `bulk-review-specs`, `bulk-review-tasks` |
| **Iterate** | `iterate` |
| **Edit** | `update-doc` |

All skill names are prefixed with `/scaffold-` (e.g., `/scaffold-new-design`).

## Key Directories

| Directory | Layer | What Goes Here |
|-----------|-------|---------------|
| `design/` | Canon (ranks 1–5) | Vision, style, colors, UI, glossary, systems, interfaces, authority, states |
| `inputs/` | Canon (rank 3) | Action map, key bindings, gamepad bindings, navigation, input philosophy |
| `reference/` | Reference (rank 6) | Signals, entities, resources, balance params |
| `decisions/` | History | ADRs, known issues, design debt |
| `phases/` | Scope (rank 7) | Roadmap, phase scope gates |
| `specs/` | Behavior (rank 8) | Atomic behavior specs |
| `tasks/` | Execution (rank 9) | Implementation tasks |
| `slices/` | Integration | Vertical slice contracts |
| `engine/` | Implementation (rank 10) | Engine-specific best practices and constraints |
| `theory/` | Advisory (rank 11) | 16 docs on game design, UX, architecture — no authority |
| `templates/` | Meta | Templates for all document types |

## Customization

- **Engine layer:** Seeded from templates based on your selected engine. Works with Godot, Unity, Unreal, or any other engine.
- **Design doc:** All sections are prompts with TODO markers. Fill in what applies, skip what doesn't.
- **Templates:** Edit `scaffold/templates/` to match your project's conventions.
- **Theory:** Add your own theory docs to `scaffold/theory/` for domain-specific advisory context.

## Troubleshooting

- Skills require the `scaffold/` directory to exist at the project root.
- If Claude ignores the pipeline, check that `CLAUDE.md` was copied to the project root.
- If documents conflict, the higher-ranked document always wins — see `scaffold/doc-authority.md`.
