---
name: scaffold-sync-reference-docs
description: Update scaffold reference and architecture documents to match actual implemented code.
argument-hint: TASK-### --files <file...>
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Sync Reference Docs

Update scaffold reference and architecture documents to reflect what was actually implemented.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| task | Yes | — | TASK-### ID — used to read the task file for intended scope |
| --files | Yes | — | Implementation files created or modified (passed by parent skill) |

## Step 1 — Determine Actual Documentation Impact

Use the provided file list as the authoritative set of implementation changes. Read those files and determine whether they introduce or change:

- Public signals or signal payloads
- Entity/component fields or data structures
- System-owned authoritative variables
- Scene-tree nodes (systems, UI panels, renderers)
- Tick order participation
- Dependency graph relationships
- Cross-system signal wiring
- State machines or transitions

Read the task file for intended scope context, but **use the implementation as the source of truth** — tasks can be stale or drifted.

If none of these changed, report `No scaffold docs needed updating.` and exit.

## Step 2 — Update Reference Documents

For each category that applies:

### signal-registry.md
Add or update signal entries with correct emitter, payload format, and subscribers. Match what the code actually emits, not what the task said it would emit.

### entity-components.md
Add or update entity fields with type, default, and owning system.

### authority.md
Add or update rows for system-owned variables whose Variable, Owning System, Readers, or Cadence changed.

## Step 3 — Update Architecture Document

Only if implementation added or changed one of the following:

### New C++ System
- Section 1 (Scene Tree) — add node under SimulationLayer
- Section 2 (Dependency Graph) — add to correct tier
- Section 3 (Tick Processing Order) — insert at correct position, renumber subsequent
- Section 4 (Signal Wiring Map) — add behavioral and/or logging connections
- Section 5 (C++ Signal Registry) — add signal block with parameter signatures
- Update system counts and Last Updated date

### New UI Panel
- Section 1 (Scene Tree) — add under UILayer

### New Renderer
- Section 1 (Scene Tree) — add under WorldLayer

### Modified Signal Wiring
- Section 4 (Signal Wiring Map) — add/update connections
- Section 5 (C++ Signal Registry) — update signatures if changed

## Step 4 — Update State Transitions

If the implementation introduces new state machines or modifies existing ones:
- Update `scaffold/design/state-transitions.md` with the relevant state machine block.

## Output

Report what was updated:

```
Docs updated:
- signal-registry.md: added [signal_name] signal
- architecture.md: added SystemName to §1, §2, §3, §4, §5
- entity-components.md: no changes
- authority.md: no changes
- state-transitions.md: no changes
```

Or: `No scaffold docs needed updating.`

## Rules

- **Implementation is the source of truth.** Update docs based on actual implemented behavior, not task wording.
- **Do not update speculatively.** Only reflect nodes, tick order, dependencies, and signal wiring that were actually implemented. Never invent architectural future state.
- **Filter the file list.** If `--files` includes non-implementation artifacts (test files, scaffold docs, build artifacts), ignore them. Only use implementation source files as documentation evidence.
- **Read before editing.** For each impacted category, read the current target document before making any edits.
- Only update documents where the implementation requires it.
- Don't update for internal-only changes that don't affect documented architecture.
- Match existing format and style in each document.
- When adding to tick order (§3), renumber ALL subsequent positions and update ordering constraint chains.
