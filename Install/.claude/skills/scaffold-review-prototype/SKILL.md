---
name: scaffold-review-prototype
description: Review a prototype document for question clarity, scope discipline, findings quality, and ADR follow-through. Use to audit a single prototype.
argument-hint: [PROTO-### or prototype-name]
allowed-tools: Read, Grep, Glob
---

# Prototype Review

Review the prototype for: **$ARGUMENTS**

## Locate the Prototype

1. If the argument is a PROTO-### ID, look for the matching file in `scaffold/prototypes/`.
2. If the argument is a name, search `scaffold/prototypes/_index.md` for a matching entry and find the file.
3. If no argument is provided, list all registered prototypes and ask the user which one to review.
4. If the prototype file doesn't exist, report that and stop.

## Read Context

1. **Read the prototype file.**
2. **Read the prototypes index** at `scaffold/prototypes/_index.md`.
3. **Read the design doc** at `scaffold/design/design-doc.md` for project context.
4. **Read the systems index** at `scaffold/design/systems/_index.md` for valid system references.
5. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md` — to check ADR follow-through.
6. **Read related documents** listed in the prototype's Related Documents section.

## Review Checklist

### Pre-Spike Sections

Check each section and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Question | ONE specific, answerable question — not compound, not vague |
| Hypothesis | Expected answer WITH reasoning — not just a guess |
| Scope: Build | Numbered list of minimum steps, <=5 items ideally |
| Scope: Skip | At least 2 explicit exclusions — discipline boundary is clear |
| Approach | Numbered steps for execution, optionally time-boxed |
| Related Documents | At least 1 valid scaffold doc reference |

### Question Quality

- **Specific:** Can this be answered with a yes/no or a measurable result?
- **Singular:** Is this ONE question, not a compound question?
- **Requires building:** Can't be answered by reading existing docs?
- **Not already decided:** No existing ADR covers this question?

### Scope Discipline

- **Build scope is minimal:** Could anything in Build be removed while still answering the question?
- **Skip scope is explicit:** Are exclusions specific enough to prevent scope creep?
- **Build + Skip are complementary:** Do they together define a clear boundary?
- **Right-sized:** Is Build scope achievable in one spike session?

### Post-Spike Sections (if Status is Complete)

If the prototype has been completed, also check:

| Section | What "Complete" Means |
|---------|----------------------|
| Answer | Direct answer to the Question — one paragraph, clear |
| Evidence | Specific measurements or observations — not vague impressions |
| Surprises | Either has unexpected findings or explicitly states "None" |
| Design Impact | Table of affected documents with specific changes needed |
| ADRs Filed | Every Design Impact entry has a corresponding ADR-### |
| Disposition | One of: Discarded / Archived / Absorbed — with reason |

### ADR Follow-Through

- Every entry in Design Impact should have a corresponding ADR in ADRs Filed.
- Every ADR referenced in ADRs Filed should exist as an actual ADR file.
- If Disposition is "Absorbed", a TASK-### should be referenced.

### Registration

- Verify the prototype is registered in `scaffold/prototypes/_index.md`.
- Check that the ID, name, status, and disposition match between the file and the registry.

## Output Format

```
## Prototype Review: PROTO-### — [Name]

### Pre-Spike Completeness: X/6 complete
| Section | Status | Notes |
|---------|--------|-------|
| ...     | ...    | ...   |

### Question Quality
- Specific: [Yes / No — why]
- Singular: [Yes / No — compound questions found]
- Requires building: [Yes / No — could be answered by reading docs]
- Not already decided: [Yes / No — ADR-### already covers this]

### Scope Discipline
- Build scope minimal: [Yes / No — what could be removed]
- Skip scope explicit: [Yes / No — what's missing]
- Right-sized: [Yes / No — too large, suggest split]

### Post-Spike Completeness: X/6 complete (if applicable)
| Section | Status | Notes |
|---------|--------|-------|
| ...     | ...    | ...   |

### ADR Follow-Through: [OK / Issues found]
- [Missing ADRs, unresolved design impacts]

### Registration: [OK / Issues found]

### Recommendations
1. [Most important fix]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Question quality is the most important check.** A bad question produces a worthless prototype.
- **Scope discipline is the second most important check.** Unbounded prototypes become mini-projects.
- Be specific. Quote problematic text when flagging issues.
- If the prototype is well-written, say so. Don't manufacture issues.
- For Draft prototypes, only review pre-spike sections. For Complete prototypes, review everything.
