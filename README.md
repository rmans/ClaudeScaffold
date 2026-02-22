# ClaudeScaffold

A document-driven pipeline scaffold for building a Godot 4 game with Claude Code. Installs into any project to give Claude Code strict document authority, token-efficient retrieval, and long-term architectural stability.

## What It Does

ClaudeScaffold provides a structured document pipeline where every design decision, implementation constraint, and behavioral spec lives in a versioned markdown file with clear authority rules. Instead of ad-hoc prompting, Claude Code reads canonical documents, follows a strict precedence chain, and operates within a defined pipeline.

## How It Works

Everything inside the `Install/` directory is the scaffold. Copy or overlay its contents into the root of your target project:

```
Install/
├── .claude/skills/       ← Claude Code skills
├── scaffold/             ← Document pipeline (see below)
├── CLAUDE.md             ← Install-specific instructions for Claude Code
└── README.md             ← Installation instructions
```

### Scaffold Pipeline

The scaffold separates concerns into strict layers with a 10-rank authority chain:

```
scaffold/
├── _index.md                 # Master index + retrieval protocol
├── doc-authority.md          # Precedence rules (ranks 1–10)
│
├── design/                   # CANON: what the game is
│   ├── design-doc.md         #   Core vision, non-negotiables (rank 1)
│   ├── style-guide.md        #   Visual/code style (rank 2)
│   ├── color-system.md       #   Color palette and rules (rank 2)
│   ├── ui-kit.md             #   UI component definitions (rank 2)
│   ├── interfaces.md         #   System interface contracts (rank 4)
│   └── systems/              #   Individual system designs (rank 5)
│
├── inputs/                   # CANON: input control definitions
│   ├── action-map.md         #   Canonical action IDs (rank 3)
│   ├── default-bindings-*    #   KBM and gamepad defaults (rank 3)
│   ├── ui-navigation.md      #   Focus flow and navigation (rank 3)
│   └── input-philosophy.md   #   Input design principles (rank 3)
│
├── engine/                   # HOW: Godot 4 implementation constraints (rank 9)
├── theory/                   # Reference only — never canonical (rank 10)
│
├── phases/                   # Scope gates (P#-###, rank 6)
├── specs/                    # Atomic behavior definitions (SPEC-###, rank 7)
├── tasks/                    # Executable steps (TASK-###, rank 8)
├── decisions/                # Architecture Decision Records (ADR-###)
├── slices/                   # Vertical slice contracts (SLICE-###)
├── templates/                # Document templates for all ID'd types
└── tools/                    # Scripts and utilities for the pipeline
```

### Document Authority

When documents conflict, the higher-ranked document wins. Lower documents must conform to higher documents. Code must never "work around" higher-level intent.

| Rank | Document | Role |
|------|----------|------|
| 1 | `design/design-doc.md` | Core vision, non-negotiables |
| 2 | `style-guide`, `color-system`, `ui-kit` | Visual and code style |
| 3 | `inputs/action-map` + bindings | Canonical input actions |
| 4 | `design/interfaces.md` | System interface contracts |
| 5 | `design/systems/SYS-###` | Individual system designs |
| 6 | `phases/P#-###` | Phase scope gates |
| 7 | `specs/SPEC-###` | Atomic behavior specs |
| 8 | `tasks/TASK-###` | Implementation steps |
| 9 | `engine/*` | Godot 4 constraints |
| 10 | `theory/*` | Reference only |

### Token-Efficient Retrieval

Every growable directory has an `_index.md`. Claude Code follows a simple protocol:

1. Start at `scaffold/_index.md` to locate the correct directory.
2. Open that directory's `_index.md` to find the specific document.
3. Read only the document(s) needed — never load entire directories.

### Layer Separation

| Layer | Purpose | Directory |
|-------|---------|-----------|
| Design | What the game is | `design/` |
| Engine | How we implement in Godot 4 | `engine/` |
| Theory | Reference only | `theory/` |
| Specs | Atomic behavior definitions | `specs/` |
| Tasks | Executable steps | `tasks/` |
| Decisions | Architectural history | `decisions/` |

No document may mix layers.

### Tools

The `tools/` directory contains scripts that support the pipeline:

- **`doc-review.py`** — Two-loop AI document review process. Claude and OpenAI discuss a document, reach agreement on changes, and apply them. Runs 1 outer-loop iteration by default; use `--iterations N` for more.

```
python doc-review.py <document-path>
python doc-review.py <document-path> --iterations 3
```

## Getting Started

See [Install/README.md](Install/README.md) for installation instructions.

## License

<!-- Add your license here. -->
