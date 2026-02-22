---
name: scaffold-review-phase
description: Review a specific phase scope gate for clarity, specificity, system alignment, entry/exit criteria, and ADR impact. Use to audit a single phase.
argument-hint: [P#-### or phase-name]
allowed-tools: Read, Grep, Glob
---

# Phase Review

Review the phase scope gate for: **$ARGUMENTS**

## Locate the Phase

1. If the argument is a P#-### ID, look for the matching file in `scaffold/phases/`.
2. If the argument is a name, search `scaffold/phases/_index.md` for a matching entry and find the file.
3. If no argument is provided, list all registered phases and ask the user which one to review.
4. If the phase file doesn't exist, report that and stop.

## Read Context

1. **Read the phase file.**
2. **Read the roadmap** at `scaffold/phases/roadmap.md` — find this phase in the Phase Overview.
3. **Read the design doc** at `scaffold/design/design-doc.md` for scope alignment.
4. **Read the systems index** at `scaffold/design/systems/_index.md`.
5. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.
6. **Read known issues** at `scaffold/decisions/known-issues.md`.
7. **Read the slices index** at `scaffold/slices/_index.md` to check downstream coverage.

## Review Checklist

### Completeness

Check each section and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Goal | One clear sentence explaining what this phase delivers |
| Entry Criteria | At least 1 concrete condition with specific IDs (phase IDs or system IDs), not vague |
| In Scope | At least 2 specific items (systems, features, or slices) — not vague categories |
| Out of Scope | At least 1 explicit deferral |
| Deliverables | At least 1 concrete output that can be demonstrated or tested |
| Exit Criteria | At least 1 verifiable condition — not just "done" or "complete" |
| Dependencies | Lists specific phases, systems, or decisions — or explicitly states none |

### Quality

- **Entry criteria reference specific IDs.** Flag vague conditions like "when the design is ready" — they should say "P1-001 complete" or "SYS-003 designed."
- **In Scope items are specific.** "Build inventory system" is good. "Build some systems" is too vague.
- **Out of Scope draws clear lines.** Items should prevent the most likely scope creep for this phase.
- **Exit criteria are verifiable.** "Core loop playable" is good. "Phase feels done" is not.
- **Deliverables are demonstrable.** Something you can show, play, or test.
- **Goal is outcome-oriented.** "Prove the core loop works" is good. "Implement 5 systems" is task-oriented.

### System Alignment

- Check that every system listed in the phase's In Scope section exists in `scaffold/design/systems/_index.md`. Flag references to non-existent systems.
- Check that systems in scope for this phase aren't already fully delivered by a prior completed phase (unless intentionally extending).

### ADR Impact

- **Check all ADRs for impacts on this phase.** Flag any ADR that:
  - Explicitly defers work into this phase
  - Changes a system that's in scope for this phase
  - Adds constraints that affect this phase's deliverables
- **If ADRs affect this phase but aren't reflected in its scope**, flag the disconnect.
- If no ADRs exist, note that explicitly.

### Registration

- Verify the phase is registered in `scaffold/phases/_index.md`.
- Verify the phase appears in the roadmap's Phase Overview table.
- Check that the ID, name, and status match across the file, index, and roadmap.

### Downstream Coverage

- If slices exist for this phase, check that they collectively cover the phase's In Scope items. Flag scope items with no corresponding slice.
- If no slices exist yet, note that as expected if the phase hasn't started.

## Output Format

```
## Phase Review: P#-### — [Name]

### Section Completeness: X/7 complete
| Section | Status | Notes |
|---------|--------|-------|
| ...     | ...    | ...   |

### Quality Issues
- [List any issues found, with specific quotes from the doc]

### System Alignment: [OK / Issues found]
- [Status of system references]

### ADR Impact: [No ADRs / X ADRs affect this phase]
- [ADR impacts and whether they're reflected in scope]

### Registration: [OK / Issues found]
- [Status of index and roadmap entries]

### Downstream Coverage: [X/Y scope items have slices]
- [Uncovered items listed]

### Recommendations
1. [Most important thing to fix]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific. Quote the problematic text when flagging issues.
- Distinguish between "empty" (needs writing) and "bad" (needs rewriting).
- If the phase is well-scoped, say so. Don't manufacture issues.
- ADR impact analysis is critical — phases that ignore ADRs will drift from reality.
