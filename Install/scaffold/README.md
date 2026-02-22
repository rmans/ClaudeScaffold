# Scaffold Usage Guide

This scaffold provides a document-driven pipeline for building a game. Every design decision, implementation constraint, and behavioral spec lives in a structured document with clear authority rules.

## Quick Start

1. Read [_index.md](_index.md) — master index and retrieval protocol.
2. Read [doc-authority.md](doc-authority.md) — understand which documents take precedence.
3. Follow [WORKFLOW.md](WORKFLOW.md) — step-by-step recipe from design through implementation.
4. Use templates from `templates/` to create new documents in their respective directories.

## Principles

- **Document authority is strict.** Higher-ranked documents always win. See [doc-authority.md](doc-authority.md).
- **Layers don't mix.** Design docs describe *what*. Engine docs describe *how*. Theory docs are reference only. Never combine layers in a single document.
- **IDs are permanent.** Once assigned, an ID (SYS-001, SPEC-003, etc.) never changes, even if the document is renamed.
- **Token-efficient retrieval.** Start at `_index.md`, drill into the directory you need, read only the files you need. Avoid loading entire directories.

## Creating New Documents

1. Pick the correct template from [templates/](templates/_index.md).
2. Assign the next sequential ID for that type.
3. Create the file in the correct directory (not in `templates/`).
4. Register it in the directory's `_index.md`.

## Directory Overview

| Directory | What goes here |
|-----------|---------------|
| `design/` | Game vision, style, colors, UI kit, interfaces, system designs |
| `engine/` | Engine-specific best practices and implementation constraints |
| `inputs/` | Action map, key bindings, input philosophy |
| `theory/` | Reference material (never canonical) |
| `phases/` | Phase scope gates and milestones |
| `specs/` | Atomic behavior definitions |
| `tasks/` | Executable implementation steps |
| `decisions/` | Architecture Decision Records (ADRs) |
| `slices/` | Vertical slice contracts |
| `templates/` | Document templates (never content) |
