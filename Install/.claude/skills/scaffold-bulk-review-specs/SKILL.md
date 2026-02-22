---
name: scaffold-bulk-review-specs
description: Review all specs at once for slice coverage, system coverage, layer boundary compliance, state machine alignment, and precondition chains. Use for a full audit of all specs.
allowed-tools: Read, Grep, Glob
---

# Bulk Spec Review

Review every registered spec for completeness, quality, and cross-spec consistency.

## Steps

### 1. Gather All Specs

1. **Read the specs index** at `scaffold/specs/_index.md`.
2. **Read every spec file** in `scaffold/specs/` (Glob `scaffold/specs/SPEC-*.md`).
3. **Read all system designs** from `scaffold/design/systems/`.
4. **Read the slices index** at `scaffold/slices/_index.md` and all slice files.
5. **Read state transitions** at `scaffold/design/state-transitions.md`.
6. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.
7. **Read the glossary** at `scaffold/design/glossary.md`.
8. If no specs exist, report that and stop.

### 2. Per-Spec Completeness

For each spec, check all 6 sections and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Summary | One clear sentence explaining what behavior this spec defines |
| Preconditions | At least 1 concrete, verifiable condition |
| Behavior | Numbered steps — each step is testable and describes one observable action or result |
| Postconditions | At least 1 concrete, observable state change |
| Edge Cases | At least 2 real boundary conditions with expected outcomes |
| Acceptance Criteria | At least 2 concrete, verifiable tests or checks |

### 3. Per-Spec Quality

For each spec, check:
- **No implementation leaks.** Flag any mention of signals, methods, nodes, classes, functions, variable names, or engine constructs. Specs describe BEHAVIOR, not IMPLEMENTATION.
- **Steps are precise and testable.** Each step should describe one observable action or result.
- **Preconditions are verifiable** — "Player has 10 wood" not "Player is ready."
- **Edge cases are real** — things a player would actually try, not hypotheticals.
- **Acceptance criteria are concrete** — each is a test you could run or manually verify.

### 4. Cross-Spec Consistency

This is unique to bulk review — check relationships BETWEEN specs:

- **Slice coverage.** For each slice, check that its Specs Included table matches the actual spec files that reference that slice. Flag one-sided references.
- **System coverage.** For each system in `scaffold/design/systems/_index.md`, check how many specs cover it. Flag systems with no specs (may be expected if not yet planned) and systems where specs don't cover the full Player Actions section.
- **Layer boundary.** Check ALL specs for implementation leaks in a single pass. This is more efficient than checking one at a time because patterns (like using a specific engine term) often repeat across specs.
- **State machine alignment.** For specs that involve state changes, check that the transitions match `scaffold/design/state-transitions.md`. Flag specs that imply transitions not in the state machine, or state machines with transitions no spec covers.
- **Precondition chains.** Check if any spec's postconditions are another spec's preconditions. Map these chains. Flag broken chains where a precondition isn't satisfied by any other spec's postcondition (unless it's an initial condition).
- **Glossary compliance.** If `scaffold/design/glossary.md` has entries, check all specs for NOT-column terms. Flag terminology violations.
- **ADR currency.** Check that ADRs affecting system behavior are reflected in the specs that cover those systems. Flag stale specs that haven't absorbed relevant ADRs.
- **Acceptance criteria overlap.** Flag specs with identical or near-identical acceptance criteria — may indicate duplicated specs or poorly split behaviors.

### 5. Registration Check

- Every spec in `scaffold/specs/_index.md` must have a corresponding file.
- Every spec file must be registered in `scaffold/specs/_index.md`.
- System references and slice references must point to valid documents.

## Output Format

```
## Bulk Spec Review — X specs audited

### Overview
| ID | Spec | System | Slice | Sections Filled | Quality Issues |
|----|------|--------|-------|-----------------|----------------|
| SPEC-001 | ... | SYS-001 | SLICE-001 | 5/6 | 1 issue |
| SPEC-002 | ... | SYS-002 | SLICE-001 | 6/6 | 0 issues |

### Per-Spec Details

#### SPEC-001 — [Name]
| Section | Status | Notes |
|---------|--------|-------|
| ... | ... | ... |

Quality Issues:
- [specific issues with quotes]

(repeat for each spec)

### Cross-Spec Consistency
- **Slice coverage:** [OK / one-sided references]
- **System coverage:** [X/Y systems have specs]
- **Layer boundary:** [X implementation leaks across Y specs]
- **State machine alignment:** [OK / mismatches]
- **Precondition chains:** [X chains found, Y broken links]
- **Glossary compliance:** [OK / X violations]
- **ADR currency:** [OK / X stale specs]

### Registration
[Any mismatches between index and files]

### Recommendations (prioritized)
1. [Most impactful fix across all specs]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-spec checks are the main value** of bulk review over individual `/scaffold-review-spec` calls. Emphasize relationship issues.
- Be specific. Quote problematic text when flagging issues.
- Implementation leaks are the most common spec issue — flag every instance, but group them for readability.
- If all specs are well-written, say so. Don't manufacture issues.
- Prioritize recommendations by blast radius — issues that affect multiple specs rank higher than issues in a single spec.
