---
name: scaffold-add-regression-tests
description: Add regression tests to the full regression test suite for a task's implementation. Uses implementation files as source of truth.
argument-hint: TASK-### --files <file...>
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# Add Regression Tests

Add regression tests to the full regression test suite for a task's implementation.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| task | Yes | — | TASK-### ID — used to read the task file for intended coverage |
| --files | Yes | — | Implementation files created or modified (passed by parent skill) |

## Step 1 — Read Context

Read these files to understand current state and determine coverage targets. If `test_full_regression.gd` or `test_full_regression.tscn` is missing, stop and report the error — the regression harness must exist before tests can be added.

1. `game/scripts/test/test_full_regression.gd` — focus on:
   - Signal tracking variables (top of file)
   - Section registration area (in `_ready()`)
   - `_reset_signals()` function
   - Existing sections for the same system (to follow patterns)
2. `game/scenes/test/test_full_regression.tscn`
3. The task file — for its Regression Tests / Verification section (guidance, not source of truth)
4. The provided `--files` implementation files — **source of truth** for what APIs, signals, and state actually need coverage

Use the implementation files to determine:
- What public APIs were added or changed
- What signals are emitted
- What state machines or transitions exist
- What cross-system interactions occur

The task file provides intended coverage guidance, but if the implementation diverged, test what was actually built.

## Step 2 — Add Infrastructure

For each system or signal the implementation requires the regression harness to reference or observe:

### System Reference Variable
```gdscript
var system_name: Node = null
```

### Signal Tracking Variables
```gdscript
var signal_fired: bool = false
var signal_param: Type = default
```

### System Node Resolution
In the setup section:
```gdscript
system_name = get_node_or_null("../SystemName")
```
Add null check.

### Signal Wiring
In the signal wiring section (STEP 2b area):
```gdscript
system_name.signal_name.connect(_on_signal_name)
```

### Signal Reset
In `_reset_signals()`:
```gdscript
signal_fired = false
signal_param = default
```

### Signal Handlers
```gdscript
func _on_signal_name(params) -> void:
    signal_fired = true
    signal_param = params
```

When infrastructure already exists, verify it is complete and consistent — reference variable, node resolution, signal wiring, reset entry, and handler must all be present. Add any missing pieces rather than duplicating existing ones. Skip only when all pieces are already in place.

## Step 3 — Write Test Section

### Register the Section

Add in the section registration area, after existing sections, in logical order:

```gdscript
_run_section("TAG", "Description (TASK-###)", "_section_tag_name")
```

### Write the Section Function

```gdscript
func _section_tag_name() -> void:
```

Design the section across the 6-layer model. Cover every applicable layer for this task. If a layer is not meaningfully applicable to this implementation, omit it rather than inventing filler coverage.

| Layer | What to Test | When to Omit |
|-------|-------------|--------------|
| 1 — Core | Happy path: call each API, verify returned values and/or resulting state changes, check signals | Never — always applicable |
| 2 — Edge Cases | Boundary values, invalid IDs, wrong-state operations, duplicates | Never — always applicable |
| 3 — Invariants | Data range rules, ownership rules, structural consistency | Omit if task has no data constraints |
| 4 — State Transitions | Valid transitions, full lifecycle, invalid transition rejection | Omit if task has no state machine |
| 5 — Integration | Cross-system reads/writes, signal chains, data consistency | Omit if task is single-system only |
| 6 — Stress | Rapid repeats, many entities, destroy-and-verify cleanup | Omit if task has no entity/resource management |

### Naming Convention

`TAG#` — short uppercase tag (e.g., FIRE, SPREAD, EMRG) with sequential number.

## Step 4 — Update Test Scene

If the implementation added a new node type required by the regression harness, add it to `game/scenes/test/test_full_regression.tscn`:

```
[node name="SystemName" type="SystemName" parent="."]
```

Add only the nodes required for the regression section being added and any `_ready()` dependencies they need. Do not add implementation nodes that the tests don't reference. Insert in correct position relative to other systems.

## Output

Report what was added:

```
Regression tests updated:
- Section: TAG — Description (TASK-###)
- Signal tracking vars added: [list or "none"]
- Signal handlers added: [list or "none"]
- System references added: [list or "none"]
- Test scene updated: yes/no
- Layers covered: 1, 2, 3, 5 (4 and 6 omitted — no state machine, no entity management)
- New assertions: N
```

## Rules

- **Implementation is the source of truth.** Test what was actually built, not what the task file said would be built.
- **Filter the file list.** Ignore non-implementation artifacts in `--files` (test files, scaffold docs, build artifacts). Only inspect implementation source files when determining coverage targets.
- Never call APIs that trigger `push_error()` or `push_warning()` in test code — these count as failures. Verify state before/after instead.
- **Test tag must be unique.** Before choosing a tag, inspect existing section tags in the file. Choose the next available sequence number for that tag family. Never duplicate an existing tag.
- Every task gets tests. No exceptions.
- Follow existing patterns in the file — match style, spacing, comment format.
- Do not modify existing test sections unless fixing a bug introduced by this task.
- **Scope: regression harness only.** This skill operates on `test_full_regression.gd` and `test_full_regression.tscn` only. GUT unit tests for GDScript logic are handled separately in the parent workflow.
