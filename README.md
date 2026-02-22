# ClaudeScaffold

A scaffold that can be installed or overlayed on top of any project to help Claude Code self-document and operate under a structured workflow/pipeline.

## What It Does

ClaudeScaffold provides a ready-made set of templates, conventions, and skills that give Claude Code the context it needs to work effectively in your project. Instead of starting from scratch each time, drop the scaffold into your repo and Claude Code immediately understands your structure, follows your conventions, and operates within a defined pipeline.

## How It Works

Everything inside the `Install/` directory is the scaffold. Copy or overlay its contents into the root of your target project:

```
Install/
├── .claude/skills/   ← Claude Code skills
├── scaffold/         ← Templates, conventions, and tools
├── CLAUDE.md         ← Install-specific instructions for Claude Code
└── README.md         ← Installation instructions
```

Once installed, Claude Code will:

- Follow project-specific conventions defined in the scaffold
- Use predefined skills for common tasks
- Self-document as it works within your project
- Operate under a consistent workflow/pipeline

## Getting Started

See [Install/README.md](Install/README.md) for installation instructions.

## License

<!-- Add your license here. -->
