# Reviews — Index

> **Purpose:** Log of adversarial document reviews performed by `/scaffold-iterate`.

## What This Is

Reviews are adversarial audits where an external LLM (OpenAI or Anthropic) reviews a scaffold document, then Claude and the reviewer discuss issues back-and-forth until consensus. This catches blind spots that self-review misses.

## How to Run

```
/scaffold-iterate <document-path>
```

The skill auto-detects the document type from its path, selects the appropriate review tier, gathers context files, and runs the two-loop review process.

## Review Tiers

| Tier | Max Iterations | Max Exchanges | Severity Filter | Doc Types |
|------|---------------|---------------|-----------------|-----------|
| Full | 5 | 5 | All | design, style, system, roadmap, phase, spec |
| Lite | 1 | 3 | HIGH only | engine, input, slice, task |
| Lint | 1 | 2 | HIGH only + accuracy focus | reference |

## Review Log

| Date | Document | Type | Tier | Issues | Accepted | Status |
|------|----------|------|------|--------|----------|--------|
| — | — | — | — | — | — | — |

<!-- Add rows as reviews are completed. -->
