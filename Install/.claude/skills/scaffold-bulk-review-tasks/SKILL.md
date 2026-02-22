---
name: scaffold-bulk-review-tasks
description: Review all tasks at once for spec coverage, engine consistency, file conflicts, ordering sanity, and sizing. Use for a full audit of all tasks.
allowed-tools: Read, Grep, Glob
---

# Bulk Task Review

Review every registered task for completeness, quality, and cross-task consistency.

## Steps

### 1. Gather All Tasks

1. **Read the tasks index** at `scaffold/tasks/_index.md`.
2. **Read every task file** in `scaffold/tasks/` (Glob `scaffold/tasks/TASK-*.md`).
3. **Read all spec files** from `scaffold/specs/`.
4. **Read all slice files** from `scaffold/slices/`.
5. **Read engine docs** from `scaffold/engine/` — at minimum, coding best practices and scene architecture.
6. **Read the signal registry** at `scaffold/reference/signal-registry.md`.
7. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.
8. If no tasks exist, report that and stop.

### 2. Per-Task Completeness

For each task, check all 5 sections and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Objective | One clear sentence explaining what this task produces |
| Steps | At least 2 numbered, concrete implementation steps |
| Files Affected | At least 1 file listed |
| Verification | At least 1 concrete check or test |
| Notes | Either has implementation notes or is explicitly empty (both are valid) |

### 3. Per-Task Quality

For each task, check:
- **Steps are concrete and actionable** — doable without guessing.
- **Steps use correct engine patterns** from engine docs.
- **Files Affected is realistic** for the described steps.
- **Verification is testable** — references specific checks, not just "verify it works."
- **Task is right-sized** — flag tasks with more than ~8 steps or ~5 files.

### 4. Cross-Task Consistency

This is unique to bulk review — check relationships BETWEEN tasks:

- **Spec coverage.** For each spec, check that at least one task implements it. Flag specs with no tasks. Flag tasks that claim to implement a spec but don't cover its key behaviors.
- **Engine consistency.** Check all tasks for consistent use of engine patterns. Flag tasks that use different patterns for the same type of operation (e.g., one task uses signal A for communication while another task uses a different pattern for the same interface).
- **File conflicts.** Build a map of files affected by each task. Flag files that are created by multiple tasks (who creates it first?) or files modified by many tasks (potential merge conflicts). If tasks share files, check that their modifications are compatible.
- **Ordering sanity.** Within each slice, check the task order in the Tasks table. Flag ordering issues where:
  - A task modifies a file that a later task creates
  - A task depends on a signal or interface that a later task implements
  - A task references a class or scene that a later task creates
- **Sizing distribution.** Report the size distribution (steps per task, files per task). Flag outliers — tasks much larger or smaller than the median may need splitting or merging.
- **Signal alignment.** Check that every signal referenced in task steps exists in `scaffold/reference/signal-registry.md`. Flag unregistered signals.
- **ADR currency.** Check that ADRs affecting implementation patterns are reflected in relevant tasks. Flag tasks that use patterns overridden by an ADR.

### 5. Registration Check

- Every task in `scaffold/tasks/_index.md` must have a corresponding file.
- Every task file must be registered in `scaffold/tasks/_index.md`.
- Spec references and phase references must point to valid documents.
- Every task should appear in its parent slice's Tasks table.

## Output Format

```
## Bulk Task Review — X tasks audited

### Overview
| ID | Task | Spec | Slice | Sections Filled | Quality Issues | Steps | Files |
|----|------|------|-------|-----------------|----------------|-------|-------|
| TASK-001 | ... | SPEC-001 | SLICE-001 | 4/5 | 1 issue | 5 | 3 |
| TASK-002 | ... | SPEC-002 | SLICE-001 | 5/5 | 0 issues | 3 | 2 |

### Per-Task Details

#### TASK-001 — [Name]
| Section | Status | Notes |
|---------|--------|-------|
| ... | ... | ... |

Quality Issues:
- [specific issues with quotes]

(repeat for each task)

### Cross-Task Consistency
- **Spec coverage:** [X/Y specs have implementing tasks]
- **Engine consistency:** [OK / pattern conflicts found]
- **File conflicts:** [X files touched by multiple tasks]
- **Ordering sanity:** [OK / ordering issues in N slices]
- **Sizing distribution:** [min/median/max steps per task]
- **Signal alignment:** [OK / X unregistered signals]
- **ADR currency:** [OK / X stale tasks]

### Registration
[Any mismatches between index, files, and slice tables]

### Recommendations (prioritized)
1. [Most impactful fix across all tasks]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-task checks are the main value** of bulk review over individual `/scaffold-review-task` calls. Emphasize relationship issues.
- Be specific. Quote problematic text when flagging issues.
- File conflicts and ordering issues are the most impactful cross-task problems — weight them heavily.
- If all tasks are well-written, say so. Don't manufacture issues.
- Prioritize recommendations by blast radius — issues that affect multiple tasks rank higher than issues in a single task.
