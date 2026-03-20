---
name: scaffold-implement-task
description: Implement one or more tasks end-to-end — code, tests, verification, code review, doc sync, and mark complete. Supports single task or range.
argument-hint: [TASK-### or TASK-###-TASK-###] [--CRI N]
allowed-tools: Read, Edit, Write, Grep, Glob, Bash, Skill, Agent
---

# Implement Task

Implement task(s) end-to-end: **$ARGUMENTS**

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| task | Yes | — | Single TASK-### or range TASK-###-TASK-### |
| --CRI N | No | 10 | Maximum code review passes passed to /scaffold-code-review --iterations N. Review may stop early if no new issues are found. |

## Range Behavior

If the argument contains a hyphen between two TASK-### IDs:
1. Extract start and end numbers. Build ordered list.
2. Execute the full pipeline (Steps 1–9) for each task sequentially. **Parallelization:** Tasks whose `Depends on` fields are satisfied (all dependencies already processed or have no dependencies) can run in parallel. Tasks with unmet dependencies wait until those dependencies complete. See WORKFLOW.md Range Parallelization for the full pattern.
3. Between tasks: `---` separator and `## Implementing: TASK-### — [Name] ([N of M])` header.
4. Skip missing task files with a note.
5. **Stop on failure.** Do NOT proceed to next task — later tasks may depend on the failed one.
6. After all tasks (or pipeline stop), output summary table:

```
## Implementation Summary: TASK-### through TASK-###

| Task | Status | Tests Added | Build | Tests | Completed |
|------|--------|-------------|-------|-------|-----------|
| TASK-### — Name | Implemented | N tests | Pass | Pass | Yes |
| TASK-### — Name | Failed (build) | — | FAIL | — | No |
| TASK-### — Name | Skipped (dependency) | — | — | — | No |
```

## Step 1 — Read Context

Read all context needed to implement:

1. The task file — Objective, Task Type, Depends on, Steps, Files Created, Files Modified, Deliverable, Verification, Verification Mapping, Out of Scope, Risks, Regression Tests.
2. Parent spec — follow `Implements: SPEC-###`. Understand the behavior. If the spec has an Asset Requirements table, check that all assets this task needs are Status: Ready with valid Satisfied By paths. If any required assets are Needed or In Production, warn: "Asset [requirement] is not yet Ready. Implementation may need placeholder assets or must wait for asset production."
3. Parent system design — follow the spec's system reference.
4. `scaffold/design/architecture.md` — tick order, signal wiring, data flow, code patterns.
5. `scaffold/design/interfaces.md` — cross-system contracts (if task involves system communication).
6. `scaffold/reference/signal-registry.md` — signal names and payloads (if task uses signals).
7. `scaffold/reference/entity-components.md` — entity data structures (if task creates/modifies entities).
8. Relevant engine docs from `scaffold/engine/`.
9. `scaffold/doc-authority.md` — document authority ranking, same-rank conflict resolution rules, deprecation protocol.
10. All ADRs affecting this task's system — Glob `scaffold/decisions/ADR-*.md`.
11. Existing system code — if modifying an existing system, read the `.h` and `.cpp` files.
12. `game/scripts/test/test_full_regression.gd` — signal tracking vars, section registration, existing sections for same system.
13. `game/scenes/test/test_full_regression.tscn`.

**Do NOT start coding until all context is read.**

## Step 2 — Plan

Output a brief implementation plan (5–10 lines):

- Files to create or modify
- Tick order position (architecture.md §3)
- Signals to register
- Sibling pointers needed
- Signal wiring for game_manager.gd
- Data table changes (CSVs per ADR-019/020/021/022/027)
- Regression test layers to cover
- Existing patterns to follow

## Step 3 — Implement

Write the code following the task's Steps section in order. Follow the Coding Rules below.

**Track all implementation files created or modified during this step.** This list is passed to child skills in Steps 4 through 8. Only include implementation files — not test files, scaffold docs, or build artifacts.

## Step 4 — Add Tests

Delegate to `/scaffold-add-regression-tests TASK-### --files <changed_files>`.

Pass the implementation file list from Step 3.

## Step 5 — Build and Test

Delegate to `/scaffold-build-and-test --files <changed_files>`.

Pass the implementation file list from Step 3. Pass `--skip-gut` and/or `--skip-lint` if this is a C++-only task with no GDScript changes.

If the verdict is FAIL:
1. Read the failure details from the output.
2. Fix the code or tests.
3. Re-invoke `/scaffold-build-and-test` with the same arguments.
4. Repeat until the verdict is PASS.

Do not proceed until the verdict is PASS.

## Step 6 — Code Review

1. From the tracked file list, identify which systems were affected.
2. Review each changed code file individually:
   - `/scaffold-code-review <file-path> --iterations N`
   - N comes from `--CRI` flag (default: 10). Review stops early if a pass produces no code changes.
   - File scope is the default — reviews topics 1 (Correctness), 3 (Engine), 4 (Performance), 6 (Maintainability), 7 (Organization). Topic 2 (Architecture) included only for boundary-relevant files (orchestrators, registration, wiring). Topic 5 (Domain Design) included only for files with meaningful behavior logic.
   - The paired file (.h ↔ .cpp) is loaded as read-only context. Files without a natural pair (e.g., `register_types.cpp`, `game_manager.gd`) are reviewed with context files only.
   - Edit boundary: accepted fixes apply only to the target file. Changes to the paired file or any other file are logged, not applied.
3. After all file reviews complete, optionally run one lightweight system-level pass if:
   - Multiple files in the same system changed, OR
   - Interfaces, signals, or state ownership changed.
   - `/scaffold-code-review <system-name> --scope system --focus "cross-file coherence"`
   - System scope reviews all 7 topics but edits are bounded to the resolved file set for that system.

If code review modifies any files, add them to the tracked implementation file list before proceeding to Step 7.

## Step 7 — Rebuild and Retest

If any code changed during Step 6, delegate to `/scaffold-build-and-test --files <changed_files>` again with the updated file list.

If the verdict is FAIL:
1. Read the failure details from the output.
2. Fix the code or tests.
3. Re-invoke `/scaffold-build-and-test` with the same arguments.
4. Repeat until the verdict is PASS.

Skip if review applied zero changes.

## Step 8 — Sync Reference Docs

Delegate to `/scaffold-sync-reference-docs TASK-### --files <changed_files>`.

Pass the final tracked implementation file list from Steps 3 and 6. This happens after review so docs reflect final stabilized code, not provisional implementation.

## Step 9 — Complete and Report

Delegate to `/scaffold-complete TASK-###`.

Output summary:

```
### TASK-### — [Name]: COMPLETE
- Files created/modified: [list]
- Tests added: N new tests (total: X passed, Y failed)
- Scaffold docs updated: [list or "none"]
- Code review: [X topics, Y issues, Z accepted — score N/10 — iterations completed/max, early stop: yes/no]
- Ripple: [what was marked Complete]
```

If range, continue to next task. After all tasks, output summary table.

## Coding Rules

- **Over-comment everything.** Every class, function, and non-trivial block gets a comment explaining what, why, and how it fits.
- **GDCLASS macro** for C++ systems. Register in `register_types.cpp`.
- **Add to SimulationOrchestrator** if tickable — update both `.h` and `.cpp`.
- **Add node to game.tscn** in correct tick order position.
- **Signal wiring in game_manager.gd only** for cross-system signals.
- **`tr()` for all player-visible strings.** Add keys to `strings.csv` first.
- **ADR-006 arrays** for entity storage, not dynamic containers.
- **Sibling resolution** via `get_parent()->get_node_or_null()`, never by path from root.
- **`[DIAG]` warnings** at decision points where unexpected values indicate a bug.
- **No hardcoded balance values** — use CSVs (ADR-027).
- **GridUtils/SlotUtils** for shared utilities (ADR-028).
- **GDScript conventions:** static typing, snake_case, `@export`/`@onready`.

## Child Skills

| Skill | Step | Receives | Purpose |
|-------|------|----------|---------|
| `/scaffold-add-regression-tests` | 4 | TASK-### + file list | Add regression tests using 6-layer model and update test scene |
| `/scaffold-build-and-test` | 5, 7 | file list + flags | Pure verification gate — build, lint, regression, GUT |
| `/scaffold-code-review` | 6 | file path + `--iterations N` | File-scope review per changed file (correctness, engine, performance, maintainability, organization — plus architecture/domain conditionally), optional system-scope coherence pass (all 7). Early stop on stability. |
| `/scaffold-sync-reference-docs` | 8 | TASK-### + file list | Update signal-registry, entity-components, authority, architecture, state-transitions |
| `/scaffold-complete` | 9 | TASK-### | Mark task Complete, ripple upward through hierarchy |

## Rules

- **Read before coding.** Incomplete context causes bugs.
- **Follow the task's Steps section.** Don't add features not in the task.
- **Track changed files.** Maintain the implementation file list through Steps 3–8. Only implementation files — not tests, docs, or artifacts.
- **Stop on failure.** Don't skip to next task in a range.
- **One task at a time.** Complete each task fully before starting the next.
- **Don't modify the task file.** Implementation goes in code files, not back into the task doc.
- **Clean up** temporary files created during implementation.
