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
├── README.md
├── .gitignore
└── .gitattributes
```
