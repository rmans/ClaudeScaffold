# ClaudeScaffold

A document-driven pipeline that gives Claude Code long-term memory, strict design authority, and a structured workflow for building games from concept to code.

## The Problem

LLMs forget. Over a long project, Claude Code loses track of design decisions, contradicts earlier choices, drifts from the original vision, and makes up answers when it should be reading a spec. The longer the project runs, the worse it gets.

Ad-hoc prompting doesn't scale. You can't keep saying "remember, the inventory uses slots not weight" in every conversation. And CLAUDE.md files help, but they're flat — there's no hierarchy, no conflict resolution, no pipeline.

## The Solution

ClaudeScaffold installs a structured document pipeline into your project. Instead of relying on conversation memory, Claude Code reads canonical documents that define **what** the game is, **how** it's built, and **what to do next**.

Every design decision, visual style rule, system behavior, interface contract, and implementation constraint lives in a versioned markdown file with a clear authority rank. When documents conflict, the higher-ranked document wins — automatically. Claude Code never has to guess.

**Key properties:**

- **Document authority replaces memory.** Claude reads the design doc, not yesterday's conversation. The source of truth is always a file, never a chat.
- **11-rank precedence chain.** When a system design says one thing and a task says another, the system design wins. No ambiguity.
- **Genre-agnostic design, engine-specific implementation.** The design layer works for any game. The engine layer adapts to Godot, Unity, Unreal, or anything else.
- **ADR feedback loop.** When implementation reality conflicts with the plan, Architecture Decision Records capture why and feed back into upcoming phases, specs, and tasks.
- **Draft → Review → Approved → Complete lifecycle.** Documents start as `Draft`, move to `Review` for adversarial scrutiny, are set to `Approved` by `/scaffold-iterate`, and marked `Complete` by `/scaffold-complete` when implementation is done. Completion ripples up from tasks through specs, slices, and phases. Documents can also be `Deprecated` via ADR when no longer active — they remain in place (IDs are permanent) but reviews flag references to them.
- **Token-efficient retrieval.** Index files in every directory let Claude find what it needs without loading entire folders.
- **45 skills automate the pipeline.** Create, seed, review, iterate, and edit documents with slash commands — no manual file wrangling.

## How It Works

### The Pipeline

The scaffold follows a strict pipeline from vision to code:

```
Design Doc → Style Docs → Systems → Reference Docs → Engine Docs
    ↓
Roadmap → Phases → Slices → Specs → Tasks → Code
    ↑                                         |
    └──────── ADR Feedback Loop ──────────────┘
```

1. **Design** — Define the game: vision, pillars, mechanics, loops, scope
2. **Style** — Lock in visual identity: art style, colors, UI components, terminology
3. **Systems** — Design each system as player-visible behavior (no engine code)
4. **Reference** — Extract data tables: signals, entities, resources, balance params
5. **Engine** — Define how to build it in your target engine
6. **Plan** — Create a roadmap, break it into phases, slice each phase vertically
7. **Spec** — Write atomic behavior specs for each slice
8. **Build** — Create implementation tasks, write code, file ADRs when reality diverges
9. **Feedback** — ADRs update the roadmap, re-scope upcoming phases and specs

Each step has a skill that automates it. Each document has a clear authority rank. Nothing is ad-hoc.

### Document Authority

When documents conflict, the higher-ranked document wins. Lower documents conform to higher documents. Code never "works around" higher-level intent.

| Rank | Document | What It Controls |
|------|----------|-----------------|
| 1 | Design doc | Core vision, non-negotiables |
| 2 | Style guide, color system, UI kit, glossary | Visual identity, terminology |
| 3 | Input docs | Player actions and bindings |
| 4 | Interfaces, authority table | System contracts, data ownership |
| 5 | System designs, state machines | Per-system behavior |
| 6 | Reference tables | Signals, entities, resources, balance |
| 7 | Phase gates | Scope and milestones |
| 8 | Behavior specs | Atomic testable behaviors |
| 9 | Implementation tasks | How to build each spec |
| 10 | Engine docs | Engine-specific constraints |
| 11 | Theory docs | Advisory only — no authority |

### Layer Separation

Documents are separated into layers. No document may mix layers.

| Layer | Question It Answers | Directory |
|-------|-------------------|-----------|
| Design | What is the game? | `design/` |
| Inputs | How does the player interact? | `inputs/` |
| Reference | What are the canonical data shapes? | `reference/` |
| Decisions | Why did we change the plan? | `decisions/` |
| Phases | What are we building and when? | `phases/` |
| Specs | What should this behavior do? | `specs/` |
| Tasks | How do we implement this spec? | `tasks/` |
| Slices | What proves this phase works end-to-end? | `slices/` |
| Engine | How do we build in this engine? | `engine/` |
| Theory | What do experts recommend? | `theory/` |

### Theory as Advisory Context

The `theory/` directory contains 16 documents covering game design principles, common pitfalls, genre conventions, UX heuristics, color theory, architecture patterns, and more. These are Rank 11 — they carry **no authority**. Skills read them for context when creating and reviewing documents, but they never dictate design decisions. Theory informs; it doesn't override.

## Installation

Download and run the installer — no need to clone the repo:

```bash
# Download install.py (once)
curl -O https://raw.githubusercontent.com/rmans/ClaudeScaffold/main/install.py

# Install into your project
python install.py /path/to/your/project
```

Options:
- `--branch <name>` — download a specific branch or tag (default: `main`)
- `--dry-run` — preview what would be copied without making changes
- `--force` — overwrite an existing `scaffold/` directory
- `--verbose` — list every file as it's copied

**Manual alternative** (requires cloning the repo):

```bash
git clone https://github.com/rmans/ClaudeScaffold.git
cp -r ClaudeScaffold/Install/.claude /path/to/your/project/
cp -r ClaudeScaffold/Install/scaffold /path/to/your/project/
cp ClaudeScaffold/Install/CLAUDE.md /path/to/your/project/
```

This gives your project:

```
.claude/skills/       ← 45 Claude Code skills
scaffold/             ← Document pipeline with templates and indexes
CLAUDE.md             ← Instructions that tell Claude Code how to use the scaffold
```

See [Install/README.md](Install/README.md) for full installation details.

## Skills

45 slash commands organized by workflow:

**Create (11):** `/scaffold-new-design`, `/scaffold-new-style`, `/scaffold-new-system`, `/scaffold-new-reference`, `/scaffold-new-engine`, `/scaffold-new-input`, `/scaffold-new-roadmap`, `/scaffold-new-phase`, `/scaffold-new-slice`, `/scaffold-new-spec`, `/scaffold-new-task`

**Bulk seed (8):** `/scaffold-bulk-seed-style`, `/scaffold-bulk-seed-systems`, `/scaffold-bulk-seed-references`, `/scaffold-bulk-seed-engine`, `/scaffold-bulk-seed-input`, `/scaffold-bulk-seed-slices`, `/scaffold-bulk-seed-specs`, `/scaffold-bulk-seed-tasks`

**Review (20):** `/scaffold-review-design`, `/scaffold-review-style`, `/scaffold-review-system`, `/scaffold-review-reference`, `/scaffold-review-engine`, `/scaffold-review-input`, `/scaffold-review-roadmap`, `/scaffold-review-phase`, `/scaffold-review-slice`, `/scaffold-review-spec`, `/scaffold-review-task`, `/scaffold-bulk-review-style`, `/scaffold-bulk-review-systems`, `/scaffold-bulk-review-references`, `/scaffold-bulk-review-engine`, `/scaffold-bulk-review-input`, `/scaffold-bulk-review-phases`, `/scaffold-bulk-review-slices`, `/scaffold-bulk-review-specs`, `/scaffold-bulk-review-tasks`

**Iterate (1):** `/scaffold-iterate`

**Complete (1):** `/scaffold-complete`

**Edit (1):** `/scaffold-update-doc`

**Validate (1):** `/scaffold-validate`

**Playtest (2):** `/scaffold-playtest-log`, `/scaffold-playtest-review`

### Recommended Workflow

```
1.  /scaffold-new-design              ← fill out the design doc
2.  /scaffold-bulk-seed-style         ← seed style, color, and UI docs
3.  /scaffold-bulk-seed-systems       ← glossary + system stubs
4.  Fill in each system design
5.  /scaffold-bulk-seed-references    ← populate reference docs
6.  /scaffold-bulk-seed-engine        ← select engine, seed engine docs
7.  Review skills                     ← audit everything
8.  /scaffold-new-roadmap             ← create the project roadmap
9.  /scaffold-new-phase → /scaffold-new-slice → /scaffold-new-spec → /scaffold-new-task
```

See `scaffold/WORKFLOW.md` for the full 24-step recipe.

## Scaffold Structure

```
scaffold/
├── _index.md                        # Master index + retrieval protocol
├── doc-authority.md                 # Precedence rules (ranks 1–11)
├── WORKFLOW.md                      # Step-by-step pipeline recipe (24 steps)
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
├── engine/                          # Engine-specific constraints (rank 10)
├── theory/                          # Advisory only — no authority (rank 11)
├── reviews/                         # Adversarial review logs from /scaffold-iterate
├── templates/                       # Document + engine templates
└── tools/                           # Scripts and utilities
```

## License

<!-- Add your license here. -->
