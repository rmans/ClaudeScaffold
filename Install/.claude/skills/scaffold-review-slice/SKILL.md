---
name: scaffold-review-slice
description: Review a vertical slice for coverage, spec completeness, demo script quality, and integration points. Use to audit a single slice.
argument-hint: [SLICE-### or slice-name]
allowed-tools: Read, Grep, Glob
---

# Slice Review

Review the vertical slice for: **$ARGUMENTS**

## Locate the Slice

1. If the argument is a SLICE-### ID, look for the matching file in `scaffold/slices/`.
2. If the argument is a name, search `scaffold/slices/_index.md` for a matching entry and find the file.
3. If no argument is provided, list all registered slices and ask the user which one to review.
4. If the slice file doesn't exist, report that and stop.

## Read Context

1. **Read the slice file.**
2. **Read the parent phase** — follow the Phase reference in the slice header.
3. **Read the interfaces doc** at `scaffold/design/interfaces.md`.
4. **Read the systems index** at `scaffold/design/systems/_index.md`.
5. **Read the specs index** at `scaffold/specs/_index.md` to check spec coverage.
6. **Read the tasks index** at `scaffold/tasks/_index.md` to check task coverage.
7. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.

## Review Checklist

### Completeness

Check each section and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Goal | One clear sentence explaining the end-to-end experience this slice delivers |
| Specs Included | At least 1 spec listed with description — table is populated, not template defaults |
| Tasks | At least 1 task listed (or explicitly empty if specs aren't yet implemented) |
| Integration Points | At least 1 system-to-system connection described, referencing interfaces.md |
| Done Criteria | At least 1 verifiable condition — something demonstrable |
| Demo Script | Step-by-step walkthrough with concrete actions and expected results |

### Quality

- **Goal is vertical, not horizontal.** The slice should cross system boundaries — not just "implement one system." Flag slices that only touch a single system.
- **Specs cover the goal.** Every part of the slice's goal should map to at least one spec. Flag gaps where the goal promises something no spec covers.
- **Integration points reference real interfaces.** Cross-check against `scaffold/design/interfaces.md`. Flag interfaces mentioned in the slice that don't exist in interfaces.md.
- **Done criteria are testable.** "Player can complete the loop" is good. "Slice feels done" is not.
- **Demo script is followable.** Each step should say what the tester does and what they should see. Flag steps that are vague ("test the system") or missing expected results.
- **Demo script covers the full slice.** The demo should exercise every spec and every integration point. Flag specs or integration points not touched by the demo.

### Phase Alignment

- Verify the slice belongs to a valid phase.
- Check that the slice's scope fits within the parent phase's In Scope items.
- Flag slices that cover functionality outside the parent phase's scope.

### Spec Completeness

- Every spec listed in the Specs Included table should have a corresponding file in `scaffold/specs/`.
- Every spec file that references this slice should appear in the table.
- Flag one-sided references (spec references slice but isn't in the table, or table lists spec that doesn't reference the slice).

### Task Coverage

- If tasks exist, verify each task references a spec from this slice.
- Check task ordering — do tasks build logically? Flag ordering issues where a later task depends on an earlier one that isn't listed first.

## Output Format

```
## Slice Review: SLICE-### — [Name]

### Section Completeness: X/6 complete
| Section | Status | Notes |
|---------|--------|-------|
| ...     | ...    | ...   |

### Quality Issues
- [List any issues found, with specific quotes from the doc]

### Phase Alignment: [OK / Issues found]
- [Status]

### Spec Completeness: [X specs listed, Y exist as files]
- [Mismatches listed]

### Task Coverage: [X tasks listed, covering Y/Z specs]
- [Gaps listed]

### Recommendations
1. [Most important thing to fix]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific. Quote the problematic text when flagging issues.
- Vertical coverage is the key value of slices — weight horizontality issues heavily.
- If the slice is well-designed, say so. Don't manufacture issues.
- If specs or tasks don't exist yet, flag that as expected early state, not as an error.
