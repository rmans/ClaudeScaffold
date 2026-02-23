# Prototypes — Index

> **Purpose:** Registry of throwaway code spikes. Each prototype answers ONE specific question and feeds findings back through ADRs. The document is the real output — not the code.

## When to Prototype

Prototype when you face a **specific technical or design uncertainty** that reading docs alone can't resolve. Good prototype triggers:

- "Will this system interaction actually work at scale?"
- "Is the engine API fast enough for our use case?"
- "Can these two systems share state without authority conflicts?"
- "Does this UI pattern feel right with our input model?"

**Don't prototype** when the question can be answered by reading engine docs, reference tables, or existing system designs. Don't prototype for exploration without a specific question — that's research, not validation.

## Lifecycle

```
Question → Hypothesis → Scoped Spike → Answer → ADR (if design impact) → Dispose
```

1. **Create** — `/scaffold-new-prototype` — define the question, hypothesis, scope, and approach.
2. **Build** — Execute the spike. Stay within scope. If you discover a bigger question, file a separate prototype.
3. **Log** — `/scaffold-prototype-log` — capture findings, evidence, surprises, and file ADR stubs.
4. **Dispose** — Mark disposition: Discarded (deleted), Archived (kept for reference), or Absorbed (code merged into real implementation via a task).

## Disposition Guide

| Disposition | When | What Happens |
|-------------|------|-------------|
| Discarded | Default. The spike answered the question. | Code is deleted. Only the document remains. |
| Archived | The code is useful reference but not production-ready. | Code stays in a `prototypes/spikes/` directory, clearly marked non-production. |
| Absorbed | Findings led to a task that reuses spike code. | Code is refactored into the real codebase via a TASK-###. Prototype doc references the task. |

## Prototype Registry

| ID | Name | Question (short) | Status | Disposition | ADRs Filed |
|----|------|-------------------|--------|-------------|------------|
| — | — | — | — | — | — |

<!-- Add rows as prototypes are created. Status: Draft | In Progress | Complete -->

## Related Skills

| Skill | What it does |
|-------|-------------|
| `/scaffold-new-prototype` | Create a new prototype document |
| `/scaffold-review-prototype` | Audit one prototype for quality |
| `/scaffold-bulk-seed-prototypes` | Identify prototype candidates from pipeline docs |
| `/scaffold-bulk-review-prototypes` | Audit all prototypes for consistency |
| `/scaffold-prototype-log` | Log findings from a completed spike |
