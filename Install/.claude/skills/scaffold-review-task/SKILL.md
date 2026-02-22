---
name: scaffold-review-task
description: Review an implementation task for completeness, spec alignment, engine pattern compliance, and sizing. Use to audit a single task.
argument-hint: [TASK-### or task-name]
allowed-tools: Read, Grep, Glob
---

# Task Review

Review the implementation task for: **$ARGUMENTS**

## Locate the Task

1. If the argument is a TASK-### ID, look for the matching file in `scaffold/tasks/`.
2. If the argument is a name, search `scaffold/tasks/_index.md` for a matching entry and find the file.
3. If no argument is provided, list all registered tasks and ask the user which one to review.
4. If the task file doesn't exist, report that and stop.

## Read Context

1. **Read the task file.**
2. **Read the parent spec** — follow the Implements reference in the task header.
3. **Read the parent system design** that the spec belongs to.
4. **Read relevant engine docs** from `scaffold/engine/` — especially coding best practices, scene architecture, and any engine doc relevant to the task's domain.
5. **Read the signal registry** at `scaffold/reference/signal-registry.md` if the task involves system communication.
6. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.

## Review Checklist

### Completeness

Check each section and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Objective | One clear sentence explaining what this task produces |
| Steps | At least 2 numbered, concrete implementation steps — each step is verifiable |
| Files Affected | At least 1 file listed (created or modified) |
| Verification | At least 1 concrete check or test to confirm the task is done |
| Notes | Either has implementation notes or is explicitly empty (both are valid) |

### Quality

- **Steps are concrete and actionable.** "Create a PlayerInventory class with add_item() and remove_item() methods" is good. "Implement the inventory" is too vague. Each step should be doable without guessing.
- **Steps use correct engine patterns.** Cross-reference with engine docs. Flag steps that contradict coding conventions, scene architecture, or performance guidelines.
- **Files Affected is realistic.** Flag if the file list seems incomplete for the steps described, or if it lists files that the steps don't actually touch.
- **Verification is testable.** "Run the scene and place 3 walls" is good. "Verify it works" is not. Verification should reference specific acceptance criteria from the parent spec.
- **Task is right-sized.** A task should be completable in one session. Flag tasks that seem too large (more than ~8 steps or touching more than ~5 files) and suggest splitting.

### Spec Alignment

- Every behavior in the parent spec should be covered by this task (or by other tasks that share the same spec). Flag spec behaviors with no corresponding task step.
- The task should not introduce behaviors beyond what the spec defines. Flag task steps that implement functionality not in the spec.
- Verification should map to the spec's Acceptance Criteria. Flag acceptance criteria with no corresponding verification step.

### Engine Pattern Compliance

- Check steps against `scaffold/engine/coding-best-practices.md` for naming, structure, and pattern compliance.
- Check steps against `scaffold/engine/scene-architecture.md` for scene organization.
- If the task involves UI, check against `scaffold/engine/ui.md`.
- If the task involves input, check against `scaffold/engine/input.md`.
- If the task involves signals, check that signal names match `scaffold/reference/signal-registry.md`.
- Flag any step that contradicts an engine doc.

### ADR Impact

- Check if any ADRs affect this task's implementation approach.
- Flag ADRs that change engine patterns, system behavior, or interfaces relevant to this task but aren't reflected in the task steps.

### Registration

- Verify the task is registered in `scaffold/tasks/_index.md`.
- Verify the task appears in its parent slice's Tasks table.
- Check that the ID, name, spec reference, and phase reference match across all locations.

## Output Format

```
## Task Review: TASK-### — [Name]

### Section Completeness: X/5 complete
| Section | Status | Notes |
|---------|--------|-------|
| ...     | ...    | ...   |

### Quality Issues
- [List any issues found, with specific quotes from the doc]

### Spec Alignment: [OK / Issues found]
- [Coverage of spec behaviors]
- [Extra behaviors not in spec]

### Engine Compliance: [OK / Issues found]
- [Pattern violations listed]

### ADR Impact: [No ADRs / X ADRs affect this task]
- [Relevant ADRs and their impact]

### Sizing: [OK / Too large — suggest split]

### Registration: [OK / Issues found]
- [Status of index and slice entries]

### Recommendations
1. [Most important thing to fix]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific. Quote the problematic text when flagging issues.
- Engine pattern compliance is critical — tasks that ignore engine docs cause inconsistent codebases.
- Sizing matters. Oversized tasks lead to incomplete sessions and lost context. Suggest concrete splits when flagging.
- If the task is well-written, say so. Don't manufacture issues.
