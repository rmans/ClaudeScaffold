# ClaudeScaffold

A document-driven pipeline scaffold for game development with Claude Code. Installs into any project to give Claude Code strict document authority, token-efficient retrieval, and long-term architectural stability.

## What It Does

ClaudeScaffold provides a structured document pipeline where every design decision, implementation constraint, and behavioral spec lives in a versioned markdown file with clear authority rules. Instead of ad-hoc prompting, Claude Code reads canonical documents, follows a strict precedence chain, and operates within a defined pipeline.

The design layer is genre-agnostic — the design doc template works for any game, any genre. The engine layer is seeded from templates based on the selected engine.

## How It Works

Everything inside the `Install/` directory is the scaffold. Copy or overlay its contents into the root of your target project:

```
Install/
├── .claude/skills/       ← Claude Code skills (14 skills)
├── scaffold/             ← Document pipeline (see below)
├── CLAUDE.md             ← Install-specific instructions for Claude Code
└── README.md             ← Installation instructions
```

### Scaffold Pipeline

The scaffold separates concerns into strict layers with an 11-rank authority chain:

```
scaffold/
├── _index.md                        # Master index + retrieval protocol
├── doc-authority.md                 # Precedence rules (ranks 1–11)
├── WORKFLOW.md                      # Step-by-step pipeline recipe
│
├── design/                          # CANON: what the game is
│   ├── design-doc.md                #   Core vision, pillars, loops, mechanics (rank 1)
│   ├── style-guide.md               #   Visual art style (rank 2)
│   ├── color-system.md              #   Color palette and rules (rank 2)
│   ├── ui-kit.md                    #   UI component definitions (rank 2)
│   ├── glossary.md                  #   Canonical terminology + NOT column (rank 2)
│   ├── interfaces.md                #   System interface contracts (rank 4)
│   ├── authority.md                 #   Data ownership per variable (rank 4)
│   ├── state-transitions.md         #   All state machines (rank 5)
│   └── systems/                     #   Individual system designs (rank 5)
│
├── inputs/                          # CANON: input control definitions (rank 3)
│   ├── action-map.md                #   Canonical action IDs
│   ├── default-bindings-kbm.md      #   Keyboard/mouse defaults
│   ├── default-bindings-gamepad.md  #   Gamepad defaults
│   ├── ui-navigation.md             #   Focus flow and navigation
│   └── input-philosophy.md          #   Input design principles
│
├── reference/                       # Canonical data tables (rank 6)
│   ├── signal-registry.md           #   Cross-system signals + intents
│   ├── entity-components.md         #   Entity fields, types, cadence
│   ├── resource-definitions.md      #   Resources, tiers, production chains
│   └── balance-params.md            #   Tunable numbers, ranges, units
│
├── decisions/                       # ADRs + tracking
│   ├── known-issues.md              #   TBDs, gaps, conflicts
│   └── design-debt.md               #   Intentional compromises
│
├── phases/                          # Scope gates (rank 7)
├── specs/                           # Atomic behavior specs (rank 8)
├── tasks/                           # Implementation steps (rank 9)
├── slices/                          # Vertical slice contracts
├── engine/                          # Engine-specific constraints (rank 10, seeded from templates)
├── theory/                          # Advisory only — no authority (rank 11)
├── templates/                       # Document + engine templates
│   ├── system-template.md           #   System design template
│   ├── phase-template.md            #   Phase gate template
│   ├── spec-template.md             #   Behavior spec template
│   ├── task-template.md             #   Implementation task template
│   ├── decision-template.md         #   ADR template
│   ├── slice-template.md            #   Vertical slice template
│   ├── engine-coding-template.md    #   Engine: coding best practices
│   ├── engine-ui-template.md        #   Engine: UI best practices
│   ├── engine-input-template.md     #   Engine: input system
│   ├── engine-scene-architecture-template.md  # Engine: scene architecture
│   └── engine-performance-template.md         # Engine: performance budget
│
└── tools/                           # Scripts and utilities
```

### Document Authority

When documents conflict, the higher-ranked document wins. Lower documents must conform to higher documents. Code must never "work around" higher-level intent.

| Rank | Document | Role |
|------|----------|------|
| 1 | `design/design-doc.md` | Core vision, non-negotiables |
| 2 | `style-guide`, `color-system`, `ui-kit`, `glossary` | Visual style, colors, UI, terminology |
| 3 | `inputs/*` | Canonical input actions and bindings |
| 4 | `interfaces.md`, `authority.md` | System contracts, data ownership |
| 5 | `systems/SYS-###`, `state-transitions.md` | System designs, state machines |
| 6 | `reference/*` | Data tables (signals, entities, resources, balance) |
| 7 | `phases/P#-###` | Phase scope gates |
| 8 | `specs/SPEC-###` | Atomic behavior specs |
| 9 | `tasks/TASK-###` | Implementation steps |
| 10 | `engine/*` | Engine constraints |
| 11 | `theory/*` | Reference only |

### Skills

The scaffold includes 27 Claude Code skills organized by workflow:

**Create:**

| Skill | Purpose |
|-------|---------|
| `/scaffold-new-design` | Fill out the design doc interactively, section by section |
| `/scaffold-new-style` | Fill out a style doc interactively (style-guide, color-system, or ui-kit) |
| `/scaffold-new-system` | Create a system — pre-fills from design doc if available, blank template if not |
| `/scaffold-new-reference` | Seed one reference doc from system designs |
| `/scaffold-new-engine` | Fill out one engine doc interactively |
| `/scaffold-new-roadmap` | Create the project roadmap with phases from start to ship |
| `/scaffold-new-phase` | Create a phase scope gate, consuming ADRs from prior work |
| `/scaffold-new-slice` | Define a vertical slice within a phase |
| `/scaffold-new-spec` | Create an atomic behavior spec for a slice |
| `/scaffold-new-task` | Create an implementation task tied to a spec |

**Bulk create:**

| Skill | Purpose |
|-------|---------|
| `/scaffold-bulk-seed-style` | Seed style-guide, color-system, and ui-kit from design doc |
| `/scaffold-bulk-seed-systems` | Glossary + all system stubs from design doc |
| `/scaffold-bulk-seed-references` | All companion docs from system designs |
| `/scaffold-bulk-seed-engine` | Select engine, then seed all 5 engine docs from templates |

**Review:**

| Skill | Purpose |
|-------|---------|
| `/scaffold-review-design` | Audit design doc completeness and index consistency |
| `/scaffold-review-style` | Audit one Rank 2 style doc for completeness and quality |
| `/scaffold-review-system` | Audit one system's completeness and quality |
| `/scaffold-review-reference` | Audit one reference doc against system designs |
| `/scaffold-review-engine` | Audit one engine doc for completeness and quality |
| `/scaffold-review-input` | Audit one input doc for completeness and quality |
| `/scaffold-bulk-review-style` | Audit all Rank 2 docs + cross-doc consistency |
| `/scaffold-bulk-review-systems` | Audit all systems + cross-system consistency |
| `/scaffold-bulk-review-references` | Audit all reference docs + cross-doc consistency |
| `/scaffold-bulk-review-engine` | Audit all engine docs + cross-doc consistency |
| `/scaffold-bulk-review-input` | Audit all input docs + cross-doc consistency |

**Edit:**

| Skill | Purpose |
|-------|---------|
| `/scaffold-update-doc` | Add, remove, or modify entries in any scaffold doc with automatic cross-reference updates |

**Recommended workflow:**

1. `/scaffold-new-design` — fill out the design doc
2. `/scaffold-bulk-seed-style` — seed style-guide, color-system, ui-kit from design doc
3. `/scaffold-bulk-seed-systems` — glossary + system stubs from design doc
4. Fill in each system design manually
5. `/scaffold-bulk-seed-references` — populate all companion docs
6. `/scaffold-bulk-seed-engine` — select engine and seed engine docs
7. Review skills — audit everything

### Token-Efficient Retrieval

Every growable directory has an `_index.md`. Claude Code follows a simple protocol:

1. Start at `scaffold/_index.md` to locate the correct directory.
2. Open that directory's `_index.md` to find the specific document.
3. Read only the document(s) needed — never load entire directories.

### Layer Separation

| Layer | Purpose | Directory |
|-------|---------|-----------|
| Design | What the game is | `design/` |
| Inputs | Player input definitions | `inputs/` |
| Reference | Canonical data tables | `reference/` |
| Decisions | ADRs, issues, debt tracking | `decisions/` |
| Phases | Scope gates and milestones | `phases/` |
| Specs | Atomic behavior definitions | `specs/` |
| Tasks | Executable implementation steps | `tasks/` |
| Engine | How we implement in the target engine | `engine/` |
| Theory | Advisory reference only | `theory/` |

No document may mix layers.

## Getting Started

See [Install/README.md](Install/README.md) for installation instructions.

## License

<!-- Add your license here. -->
