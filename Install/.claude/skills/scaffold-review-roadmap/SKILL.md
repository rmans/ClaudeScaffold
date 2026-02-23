---
name: scaffold-review-roadmap
description: Review the project roadmap for completeness, phase coverage, ADR feedback currency, and vision alignment. Use to audit the roadmap.
allowed-tools: Read, Grep, Glob
---

# Roadmap Review

Review the project roadmap for completeness, currency, and alignment with the design doc.

## Steps

### 1. Read Context

1. **Read the roadmap** at `scaffold/phases/roadmap.md`.
2. **Read the design doc** at `scaffold/design/design-doc.md` — especially Core Fantasy, Scope Reality Check, and Content Structure.
3. **Read the phases index** at `scaffold/phases/_index.md` to see all registered phases.
4. **Read all phase files** in `scaffold/phases/` (Glob `scaffold/phases/P*-*.md`).
5. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.
6. **Read known issues** at `scaffold/decisions/known-issues.md`.
7. **Read design debt** at `scaffold/decisions/design-debt.md`.
8. **Read playtest feedback** at `scaffold/decisions/playtest-feedback.md` — check for Pattern-status entries that may affect phase planning.
9. If the roadmap is empty or at template defaults, report that and stop.

### 2. Completeness Check

Check each section and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Vision Checkpoint | Core Fantasy copied from design doc — matches current design doc text |
| Phase Overview | At least 2 phases listed with goals and statuses |
| Current Phase | Set to a valid phase with a link to the phase doc |
| ADR Feedback Log | Every ADR from completed phases has an entry (or explicitly empty if no ADRs filed) |
| Completed Phases | Every phase marked "Complete" in the overview has an entry with delivery notes |
| Upcoming Phases | At least one upcoming phase described (unless all phases are complete) |
| Phase Transition Protocol | Present and unmodified from template (or intentionally customized) |

### 3. Phase Coverage

Cross-reference the roadmap against the design doc:

- **System coverage.** Every system in `scaffold/design/systems/_index.md` should be in scope for at least one phase. Flag systems with no phase assignment.
- **Feature coverage.** Major features from the design doc's Core Loop, Secondary Loops, and Content Structure should map to at least one phase. Flag uncovered features.
- **Phase progression.** Phases should build logically — foundation before systems, systems before content. Flag ordering issues.
- **Scope alignment.** The total scope of all phases should roughly match the design doc's Scope Reality Check. Flag if the roadmap promises significantly more or less than the design doc scopes.

### 4. ADR Feedback Currency

- **Every completed phase's ADRs must appear in the ADR Feedback Log.** Cross-reference ADR files with the log. Flag any ADRs filed during a completed phase that aren't logged.
- **ADR impacts must be reflected in phase scopes.** If an ADR says "defer X to P3," check that P3's scope includes X. Flag disconnects.
- **No stale ADR references.** If an ADR references a phase, slice, or spec that no longer exists, flag it.

### 5. Vision Alignment

- Compare the Vision Checkpoint text against the design doc's Core Fantasy. Flag if they don't match.
- Check that every phase's goal contributes toward the core fantasy. Flag phases that seem disconnected from the vision.

### 6. Registration Consistency

- Every phase listed in the roadmap's Phase Overview should have a corresponding file in `scaffold/phases/`.
- Every phase file in `scaffold/phases/` should appear in the roadmap's Phase Overview.
- Every phase file should be registered in `scaffold/phases/_index.md`.
- IDs and statuses should match across all three locations.

## Output Format

```
## Roadmap Review

### Section Completeness: X/7 complete
| Section | Status | Notes |
|---------|--------|-------|
| ...     | ...    | ...   |

### Phase Coverage
- **Systems covered:** X/Y systems assigned to phases
- **Features covered:** [status]
- **Ordering:** [OK / issues]
- **Scope alignment:** [OK / over-scoped / under-scoped]

### ADR Feedback Currency
- **ADRs logged:** X/Y from completed phases
- **Impact reflected:** [OK / gaps found]
- [Specific gaps listed]

### Vision Alignment: [Aligned / Drifted]
- [Specific observations]

### Registration: [OK / Issues found]
- [Mismatches listed]

### Recommendations
1. [Most important fix]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific. Quote problematic text when flagging issues.
- ADR feedback currency is critical — the feedback loop is what keeps the roadmap honest. Weight ADR gaps heavily.
- If the roadmap is well-maintained, say so. Don't manufacture issues.
- If no phases exist yet, report that the roadmap is at template defaults and suggest running `/scaffold-new-roadmap`.
