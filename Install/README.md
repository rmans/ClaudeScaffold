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
- `.claude/skills/` — 8 scaffold skills for design, seeding, and review
- `scaffold/` — the full document pipeline with templates and indexes
- `CLAUDE.md` — instructions that tell Claude Code how to use the scaffold

## What Gets Installed

### Skills (`.claude/skills/`)

| Skill | What it does |
|-------|-------------|
| `/scaffold-new-design` | Walk through the design doc section by section |
| `/scaffold-new-system` | Create a system — pre-fills from design doc if available |
| `/scaffold-new-reference` | Seed one reference doc from system designs |
| `/scaffold-bulk-seed-systems` | Glossary + all system stubs from design doc |
| `/scaffold-bulk-seed-references` | All companion docs from system designs |
| `/scaffold-review-design` | Audit design doc completeness |
| `/scaffold-review-system` | Audit one system's quality |
| `/scaffold-bulk-review-systems` | Audit all systems + cross-system consistency |

### Scaffold (`scaffold/`)

A structured document pipeline with 11 authority ranks. Start at `scaffold/_index.md` — it's the master entry point.

Key directories:
- **`design/`** — Canon layer: design doc, glossary, style, systems, interfaces, authority, states
- **`inputs/`** — Canon layer: action maps, bindings, navigation
- **`reference/`** — Data tables: signals, entities, resources, balance params
- **`decisions/`** — ADRs, known issues, design debt
- **`engine/`** — Godot 4 implementation constraints (replace for other engines)
- **`templates/`** — Templates for systems, specs, tasks, phases, decisions, slices

## After Installing

1. Run `/scaffold-new-design` to fill out your design doc.
2. Run `/scaffold-bulk-seed-systems` to create system stubs from your design.
3. Fill in each system design.
4. Run `/scaffold-bulk-seed-references` to populate companion docs.
5. Use `/scaffold-review-design` and `/scaffold-bulk-review-systems` to audit.

## Customization

- **Engine layer:** The `scaffold/engine/` directory ships with Godot 4 docs. Replace them with your engine's constraints.
- **Design doc:** All sections are prompts with TODO markers. Fill in what applies, skip what doesn't.
- **Templates:** Edit `scaffold/templates/` to match your project's conventions.

## Troubleshooting

- Ensure Git is installed and available on your PATH.
- Ensure Claude Code CLI is installed and authenticated.
- Skills require the `scaffold/` directory to exist at the project root.
