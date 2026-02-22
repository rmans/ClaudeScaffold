# Templates — Index

> **Purpose:** Document templates for all ID'd types. Templates live here only — never in content directories.

## Available Templates

| Template | ID Format | Target Directory |
|----------|-----------|-----------------|
| [system-template.md](system-template.md) | SYS-### | [design/systems/](../design/systems/_index.md) |
| [phase-template.md](phase-template.md) | P#-### | [phases/](../phases/_index.md) |
| [spec-template.md](spec-template.md) | SPEC-### | [specs/](../specs/_index.md) |
| [task-template.md](task-template.md) | TASK-### | [tasks/](../tasks/_index.md) |
| [decision-template.md](decision-template.md) | ADR-### | [decisions/](../decisions/_index.md) |
| [slice-template.md](slice-template.md) | SLICE-### | [slices/](../slices/_index.md) |

## Usage

1. Copy the template to the target directory.
2. Rename it with the next sequential ID (e.g., `SYS-001-player-movement.md`).
3. Fill in all sections.
4. Register the new document in the target directory's `_index.md`.
