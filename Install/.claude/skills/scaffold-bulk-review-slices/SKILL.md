---
name: scaffold-bulk-review-slices
description: Review all slices at once for phase coverage, spec overlap, interface coverage, and vertical completeness. Use for a full audit of all slices.
allowed-tools: Read, Grep, Glob
---

# Bulk Slice Review

Review every registered slice for completeness, quality, and cross-slice consistency.

## Steps

### 1. Gather All Slices

1. **Read the slices index** at `scaffold/slices/_index.md`.
2. **Read every slice file** in `scaffold/slices/` (Glob `scaffold/slices/SLICE-*.md`).
3. **Read all phase files** — Glob `scaffold/phases/P*-*.md`.
4. **Read the interfaces doc** at `scaffold/design/interfaces.md`.
5. **Read the systems index** at `scaffold/design/systems/_index.md`.
6. **Read the specs index** at `scaffold/specs/_index.md`.
7. **Read the tasks index** at `scaffold/tasks/_index.md`.
8. If no slices exist, report that and stop.

### 2. Per-Slice Completeness

For each slice, check all 6 sections and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Goal | One clear sentence explaining the end-to-end experience |
| Specs Included | At least 1 spec listed with description |
| Tasks | At least 1 task listed (or explicitly empty if not yet implemented) |
| Integration Points | At least 1 system-to-system connection referencing interfaces.md |
| Done Criteria | At least 1 verifiable, demonstrable condition |
| Demo Script | Step-by-step walkthrough with concrete actions and expected results |

### 3. Per-Slice Quality

For each slice, check:
- **Goal is vertical (end-to-end), not horizontal (single system).** Flag slices that only touch one system.
- **Demo script is followable** — each step says what the tester does and what they see.
- **Done criteria are testable** — observable conditions, not feelings.
- **Integration points reference real interfaces** from interfaces.md.

### 4. Cross-Slice Consistency

This is unique to bulk review — check relationships BETWEEN slices:

- **Phase coverage.** For each phase, check that its slices collectively cover all In Scope items. Flag phase scope items with no corresponding slice.
- **Spec overlap.** Check if any spec is listed in multiple slices. Some overlap is acceptable for shared behaviors, but flag specs that appear in many slices (may indicate the spec is too broad or the slice boundaries are wrong).
- **Interface coverage.** Check that every interface contract in `scaffold/design/interfaces.md` is exercised by at least one slice's Integration Points. Flag untested interfaces.
- **Vertical completeness.** For each slice, check that it crosses at least 2 system boundaries. Flag slices that test a single system in isolation — they're not vertical.
- **Demo consistency.** Check that demo scripts across slices don't contradict each other (e.g., different assumed starting states for the same system).
- **Spec coverage.** Check that every spec in `scaffold/specs/_index.md` belongs to at least one slice. Flag orphaned specs with no slice.
- **Task completeness.** For slices with tasks, check that every listed spec has at least one task. Flag specs with no implementing tasks.

### 5. Registration Check

- Every slice in `scaffold/slices/_index.md` must have a corresponding file.
- Every slice file must be registered in `scaffold/slices/_index.md`.
- Phase references in slice files must point to valid phases.

## Output Format

```
## Bulk Slice Review — X slices audited

### Overview
| ID | Slice | Phase | Sections Filled | Quality Issues | Specs | Tasks |
|----|-------|-------|-----------------|----------------|-------|-------|
| SLICE-001 | ... | P1-001 | 4/6 | 1 issue | 3 | 5 |
| SLICE-002 | ... | P1-001 | 6/6 | 0 issues | 2 | 4 |

### Per-Slice Details

#### SLICE-001 — [Name]
| Section | Status | Notes |
|---------|--------|-------|
| ... | ... | ... |

Quality Issues:
- [specific issues with quotes]

(repeat for each slice)

### Cross-Slice Consistency
- **Phase coverage:** [X/Y phase scope items covered by slices]
- **Spec overlap:** [OK / specs in multiple slices listed]
- **Interface coverage:** [X/Y interfaces exercised by slices]
- **Vertical completeness:** [OK / horizontal slices flagged]
- **Orphaned specs:** [specs with no slice]
- **Task completeness:** [specs with no implementing tasks]

### Registration
[Any mismatches between index and files]

### Recommendations (prioritized)
1. [Most impactful fix across all slices]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-slice checks are the main value** of bulk review over individual `/scaffold-review-slice` calls. Emphasize relationship issues.
- Be specific. Quote problematic text when flagging issues.
- If all slices are well-designed, say so. Don't manufacture issues.
- Prioritize recommendations by blast radius — issues that affect multiple slices rank higher than issues in a single slice.
