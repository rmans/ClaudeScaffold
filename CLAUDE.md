# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

ClaudeScaffold is an installable overlay that helps Claude Code self-document and operate under a structured workflow/pipeline. Everything inside `Install/` is a scaffold that can be copied into any project to give Claude Code the context, conventions, and skills it needs to work effectively.

## Project Structure

```
/
├── Install/
│   ├── .claude/skills/   ← Claude Code skills
│   ├── scaffold/         ← Templates, conventions, tools
│   ├── CLAUDE.md         ← Install-specific instructions
│   └── README.md         ← Installation instructions
├── CLAUDE.md
├── claudescaffold.py      ← Installer script (contains VERSION)
├── README.md
├── .gitignore
└── .gitattributes
```

## Versioning

The project version lives in `claudescaffold.py` line 16 as `VERSION = "X.Y.Z"`. After making changes to any files under `Install/` (skills, templates, scaffold docs, tools), bump the version before committing:

- **Patch** (X.Y.**Z**) — bug fixes, wording tweaks, minor corrections
- **Minor** (X.**Y**.0) — new checks, new skill features, new templates, behavioral changes
- **Major** (**X**.0.0) — breaking changes to scaffold structure or skill contracts
