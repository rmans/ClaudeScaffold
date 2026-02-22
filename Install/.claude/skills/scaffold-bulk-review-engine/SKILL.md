---
name: scaffold-bulk-review-engine
description: Review all engine docs at once for completeness and cross-doc consistency. Use for a full audit of the engine layer.
allowed-tools: Read, Grep, Glob
---

# Bulk Engine Review

Review all engine documents for completeness, accuracy, and cross-doc consistency.

## Documents Audited

Glob `scaffold/engine/*` to find all engine docs (excluding `_index.md`). Expected docs:

| Doc | File Pattern |
|-----|-------------|
| Coding best practices | `[engine]-coding-best-practices.md` |
| UI best practices | `[engine]-ui-best-practices.md` |
| Input system | `[engine]-input-system.md` |
| Scene architecture | `[engine]-scene-architecture.md` |
| Performance budget | `[engine]-performance-budget.md` |

## Steps

### 1. Read Everything

1. Read all engine docs from `scaffold/engine/`.
2. Read the design doc at `scaffold/design/design-doc.md`.
3. Read `scaffold/design/style-guide.md`, `scaffold/design/color-system.md`, and `scaffold/design/ui-kit.md` for style context.
4. Read `scaffold/inputs/action-map.md` and `scaffold/inputs/input-philosophy.md` for input context.
5. If no engine docs exist, report that and tell the user to run `/scaffold-bulk-seed-engine` first.

### 2. Per-Doc Completeness

For each engine document, assess:
- **Section count** — how many sections exist?
- **Filled sections** — how many have content beyond TODO markers?
- **Empty sections** — any sections still at template defaults?
- **Project Overrides** — any overrides defined?

Categorize each doc as: **Complete**, **Partial**, or **Empty**.

### 3. Cross-Doc Consistency

This is the main value of bulk review — checking relationships BETWEEN engine docs:

- **Coding ↔ Scene Architecture.** Naming conventions in coding should match how scenes, nodes, and scripts are named in scene architecture. Composition vs inheritance guidelines should align.
- **Coding ↔ UI.** Event/message patterns should be consistent between gameplay code and UI code. Error handling should apply to UI as well.
- **UI ↔ Input.** Focus and navigation implementation should use the input patterns defined in the input system doc. Device detection in the input doc should inform UI responsive behavior.
- **UI ↔ Performance.** UI performance guidelines should be consistent with the overall frame budget. Draw call limits should account for UI overhead.
- **Input ↔ Performance.** Input buffering and polling approaches should be compatible with the frame budget.
- **Scene Architecture ↔ Performance.** Scene loading strategies should respect memory budgets. Entity/object patterns should support the rendering budget.
- **All Docs ↔ Design.** Every engine doc should support the design intent without contradicting it. Flag implementation approaches that would make design goals difficult or impossible.

### 4. Gap Analysis

Identify what's missing:

- Engine docs that don't exist (only some of the 5 were created)
- Sections that reference engine features not covered in other engine docs
- Design doc requirements that aren't addressed by any engine doc
- Input actions defined in `inputs/action-map.md` with no implementation guidance in the input system doc
- UI components defined in `design/ui-kit.md` with no implementation guidance in the UI doc
- Performance targets in the design doc with no budget allocation in the performance doc

### 5. Layer Boundary Check

Engine docs must stay in their lane:
- Flag any content that describes WHAT the game does (belongs in design layer)
- Flag any content that defines player-visible behavior (belongs in system designs)
- Flag any content that specifies data formats (belongs in reference layer)
- Engine docs should only describe HOW to implement

## Output Format

```
## Bulk Engine Review — X docs audited

### Overview
| Doc | Status | Sections | Filled | Overrides | Issues |
|-----|--------|----------|--------|-----------|--------|
| Coding | Complete | 7 | 7 | 2 | 1 |
| UI | Partial | 7 | 4 | 0 | 3 |
| ... | ... | ... | ... | ... | ... |

### Cross-Doc Consistency
- **Coding ↔ Scene Architecture:** [status]
- **Coding ↔ UI:** [status]
- **UI ↔ Input:** [status]
- **UI ↔ Performance:** [status]
- **Input ↔ Performance:** [status]
- **Scene ↔ Performance:** [status]
- **Design alignment:** [status]

### Gap Analysis
[List of missing coverage, organized by source]

### Layer Boundary Issues
[Any content that belongs in a different layer]

### Recommendations (prioritized)
1. [Highest-impact fix across all docs]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-doc consistency is the main value.** Individual completeness is what `/scaffold-review-engine` does — bulk review focuses on relationships.
- Be specific. Name the exact sections and docs involved in every mismatch.
- If everything is consistent, say so. Don't manufacture issues.
- Prioritize by blast radius — issues affecting multiple docs rank higher.
- **Layer boundary enforcement is critical.** Engine docs that leak into design territory undermine the scaffold's authority chain.
