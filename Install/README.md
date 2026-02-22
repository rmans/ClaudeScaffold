# Installation

## Prerequisites

- [Git](https://git-scm.com/)
- [Claude Code CLI](https://claude.ai/code)

## Install

Copy the contents of this directory into the root of your target project:

```bash
# From the ClaudeScaffold repo
cp -r Install/.claude /path/to/your/project/
cp -r Install/scaffold /path/to/your/project/
cp Install/CLAUDE.md /path/to/your/project/
```

This gives your project:
- `.claude/skills/` — 18 scaffold skills for design, seeding, and review
- `scaffold/` — the full document pipeline with templates and indexes
- `CLAUDE.md` — instructions that tell Claude Code how to use the scaffold

## What Gets Installed

### Skills (`.claude/skills/`)

| Skill | What it does |
|-------|-------------|
| `/scaffold-new-design` | Walk through the design doc section by section |
| `/scaffold-new-style` | Fill out a style doc interactively (style-guide, color-system, or ui-kit) |
| `/scaffold-new-system` | Create a system — pre-fills from design doc if available |
| `/scaffold-new-reference` | Seed one reference doc from system designs |
| `/scaffold-new-engine` | Fill out one engine doc interactively |
| `/scaffold-bulk-seed-style` | Seed style-guide, color-system, and ui-kit from design doc |
| `/scaffold-bulk-seed-systems` | Glossary + all system stubs from design doc |
| `/scaffold-bulk-seed-references` | All companion docs from system designs |
| `/scaffold-bulk-seed-engine` | Select engine, then seed all 5 engine docs from templates |
| `/scaffold-review-design` | Audit design doc completeness |
| `/scaffold-review-style` | Audit one Rank 2 style doc for completeness and quality |
| `/scaffold-review-system` | Audit one system's quality |
| `/scaffold-review-reference` | Audit one reference doc against system designs |
| `/scaffold-review-engine` | Audit one engine doc for completeness and quality |
| `/scaffold-bulk-review-style` | Audit all Rank 2 docs + cross-doc consistency |
| `/scaffold-bulk-review-systems` | Audit all systems + cross-system consistency |
| `/scaffold-bulk-review-references` | Audit all reference docs + cross-doc consistency |
| `/scaffold-bulk-review-engine` | Audit all engine docs + cross-doc consistency |

### Scaffold (`scaffold/`)

A structured document pipeline with 11 authority ranks. Start at `scaffold/_index.md` — it's the master entry point.

Key directories:
- **`design/`** — Canon layer: design doc, style-guide, color-system, ui-kit, glossary, systems, interfaces, authority, states
- **`inputs/`** — Canon layer: action maps, bindings, navigation
- **`reference/`** — Data tables: signals, entities, resources, balance params
- **`decisions/`** — ADRs, known issues, design debt
- **`engine/`** — Engine-specific implementation constraints (seeded from templates)
- **`templates/`** — Templates for systems, specs, tasks, phases, decisions, slices, and engine docs

## After Installing

1. Run `/scaffold-new-design` to fill out your design doc.
2. Run `/scaffold-bulk-seed-style` to seed style-guide, color-system, and ui-kit.
3. Run `/scaffold-bulk-seed-systems` to create system stubs from your design.
4. Fill in each system design.
5. Run `/scaffold-bulk-seed-references` to populate companion docs.
6. Run `/scaffold-bulk-seed-engine` to select your engine and seed engine docs.
7. Use review skills to audit everything.

## Customization

- **Engine layer:** The `scaffold/engine/` directory is seeded from templates based on your selected engine.
- **Design doc:** All sections are prompts with TODO markers. Fill in what applies, skip what doesn't.
- **Templates:** Edit `scaffold/templates/` to match your project's conventions. Engine templates are seeded by skill based on your selected engine.

## Troubleshooting

- Ensure Git is installed and available on your PATH.
- Ensure Claude Code CLI is installed and authenticated.
- Skills require the `scaffold/` directory to exist at the project root.
