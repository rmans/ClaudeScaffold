---
name: scaffold-bulk-review-phases
description: Review all phases at once for roadmap alignment, entry/exit chains, scope coverage, ADR absorption, and dependency graph. Use for a full audit of all phases.
allowed-tools: Read, Grep, Glob
---

# Bulk Phase Review

Review every registered phase for completeness, quality, and cross-phase consistency.

## Steps

### 1. Gather All Phases

1. **Read the roadmap** at `scaffold/phases/roadmap.md`.
2. **Read the phases index** at `scaffold/phases/_index.md`.
3. **Read every phase file** in `scaffold/phases/` (Glob `scaffold/phases/P*-*.md`).
4. **Read the design doc** at `scaffold/design/design-doc.md`.
5. **Read the systems index** at `scaffold/design/systems/_index.md`.
6. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.
7. **Read the slices index** at `scaffold/slices/_index.md`.
8. If no phases exist, report that and stop.

### 2. Per-Phase Completeness

For each phase, check all 7 sections and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Goal | One clear sentence explaining what this phase delivers |
| Entry Criteria | At least 1 concrete condition with specific IDs |
| In Scope | At least 2 specific items |
| Out of Scope | At least 1 explicit deferral |
| Deliverables | At least 1 concrete, demonstrable output |
| Exit Criteria | At least 1 verifiable condition |
| Dependencies | Lists specific references or explicitly states none |

### 3. Per-Phase Quality

For each phase, check:
- **Entry criteria reference specific IDs** (phase IDs, system IDs), not vague conditions.
- **In Scope items are specific** — named systems, features, or slices.
- **Goals are outcome-oriented** — "prove the core loop" not "implement 5 systems."
- **Exit criteria are verifiable** — observable, testable conditions.

### 4. Cross-Phase Consistency

This is unique to bulk review — check relationships BETWEEN phases:

- **Roadmap alignment.** Every phase in the roadmap's Phase Overview should have a phase file. Every phase file should appear in the roadmap. Flag mismatches.
- **Entry/exit chains.** Phase N's exit criteria should satisfy Phase N+1's entry criteria. Flag broken chains where a later phase requires something no prior phase delivers.
- **Scope coverage.** The union of all phases' In Scope items should cover every system in the systems index and every major feature in the design doc. Flag uncovered systems or features.
- **Scope overlap.** Check for systems or features claimed by multiple phases. Overlap is acceptable for iterative development (e.g., "basic inventory" in P1, "crafting extension" in P2) but flag exact duplicates.
- **ADR absorption.** Every ADR that defers work to a specific phase should be reflected in that phase's scope. Cross-reference ADR files with phase In Scope sections. Flag ADRs whose deferred work isn't absorbed.
- **Dependency graph.** Build a dependency graph from each phase's Dependencies section. Flag cycles (Phase A depends on Phase B depends on Phase A). Flag unresolvable dependencies (depends on a phase that doesn't exist).
- **Status consistency.** Phase statuses in the roadmap, the index, and the phase files themselves should match. Flag disagreements.
- **Out of Scope hand-offs.** Items in Phase N's Out of Scope should appear in a later phase's In Scope. Flag items that are deferred but never picked up.

### 5. Registration Check

- Every phase in `scaffold/phases/_index.md` must have a corresponding file.
- Every phase file must be registered in `scaffold/phases/_index.md`.
- Every phase must appear in the roadmap's Phase Overview.
- IDs, names, and statuses must match across all three locations.

## Output Format

```
## Bulk Phase Review — X phases audited

### Overview
| ID | Phase | Sections Filled | Quality Issues | Status |
|----|-------|-----------------|----------------|--------|
| P1-001 | ... | 5/7 | 2 issues | ... |
| P2-002 | ... | 7/7 | 0 issues | ... |

### Per-Phase Details

#### P1-001 — [Name]
| Section | Status | Notes |
|---------|--------|-------|
| ... | ... | ... |

Quality Issues:
- [specific issues with quotes]

(repeat for each phase)

### Cross-Phase Consistency
- **Roadmap alignment:** [OK / mismatches]
- **Entry/exit chains:** [OK / broken links]
- **Scope coverage:** [X/Y systems covered, Z/W features covered]
- **Scope overlap:** [OK / duplicates found]
- **ADR absorption:** [X/Y ADRs reflected in phases]
- **Dependency graph:** [OK / cycles / unresolvable]
- **Out of Scope hand-offs:** [X/Y deferred items picked up]

### Registration
[Any mismatches between roadmap, index, and files]

### Recommendations (prioritized)
1. [Most impactful fix across all phases]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-phase checks are the main value** of bulk review over individual `/scaffold-review-phase` calls. Emphasize relationship issues.
- Be specific. Quote problematic text when flagging issues.
- If all phases are well-designed, say so. Don't manufacture issues.
- Prioritize recommendations by blast radius — issues that affect multiple phases rank higher than issues in a single phase.
