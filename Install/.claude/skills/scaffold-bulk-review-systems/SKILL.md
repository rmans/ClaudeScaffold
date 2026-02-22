---
name: scaffold-bulk-review-systems
description: Review all system designs at once for completeness, quality, and cross-system consistency. Use for a full audit of all systems.
allowed-tools: Read, Grep, Glob
---

# Bulk System Design Review

Review every registered system design for completeness, quality, and cross-system consistency.

## Steps

### 1. Gather All Systems

1. **Read** `scaffold/design/systems/_index.md` to get the list of registered systems.
2. **Read every system file** in `scaffold/design/systems/`.
3. If no systems exist, report that and stop.

### 2. Per-System Completeness

For each system, check all 11 sections and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Purpose | One clear sentence explaining why this system exists |
| Player Intent | At least 2 concrete goals the player has |
| Player Actions | Numbered steps describing observable player behavior — no implementation details |
| System Resolution | Numbered steps describing what happens after the player acts — visible consequences only |
| Failure / Friction States | At least 2 failure modes with what the player sees for each |
| Inputs & Dependencies | Every source system listed with what it provides |
| Outputs & Consequences | Every target system listed with what it receives |
| Non-Responsibilities | At least 1 explicit boundary |
| Edge Cases & Player Questions | At least 3 real questions a player would ask, answered |
| Feel & Feedback | Describes the sensory experience — visual, audio, or haptic cues |
| Open Questions | Either has unresolved questions or is explicitly empty (both are valid) |

### 3. Per-System Quality

For each system, check:
- **Player language, not code language.** Flag mentions of signals, methods, nodes, classes, functions, variable names.
- **Concrete, not vague.** "The player places a wall" is good. "The player interacts with the building system" is too vague.
- **Failure states include player-visible feedback.** Not just "it fails."
- **Non-Responsibilities draw clear lines** against the most likely scope creep for this system.
- **Edge cases answer real questions** a player would actually try or wonder about.

### 4. Cross-System Consistency

This is unique to bulk review — check relationships BETWEEN systems:

- **Dependency symmetry.** If System A lists System B in its Inputs, System B should list System A in its Outputs (and vice versa). Flag one-sided dependencies.
- **Orphan systems.** Systems with no Inputs from and no Outputs to other systems. Are they genuinely standalone, or are dependencies missing?
- **Authority conflicts.** If two systems' Player Actions or System Resolution describe writing to the same variable/state, flag the conflict. Reference `scaffold/design/authority.md` if it exists.
- **State coverage.** If `scaffold/design/state-transitions.md` defines state machines, check that every system referencing an entity's state aligns with the defined transitions.
- **Glossary compliance.** If `scaffold/design/glossary.md` has entries, check that system files use canonical terms and not the NOT-column alternatives.
- **Signal alignment.** If `scaffold/reference/signal-registry.md` has entries, check that system Inputs/Outputs match registered signals.

### 5. Registration Check

- Every system in `scaffold/design/systems/_index.md` must have a corresponding file.
- Every system file must be registered in `scaffold/design/systems/_index.md`.
- Every system must appear in the System Design Index in `scaffold/design/design-doc.md`.
- IDs, names, and status values must match across all three locations.

## Output Format

```
## Bulk System Review — X systems audited

### Overview
| ID | System | Sections Filled | Quality Issues | Status |
|----|--------|-----------------|----------------|--------|
| SYS-001 | ... | 8/11 | 2 issues | ... |
| SYS-002 | ... | 11/11 | 0 issues | ... |

### Per-System Details

#### SYS-001 — [Name]
| Section | Status | Notes |
|---------|--------|-------|
| ... | ... | ... |

Quality Issues:
- [specific issues with quotes]

(repeat for each system)

### Cross-System Consistency
- **Dependency gaps:** [one-sided dependencies]
- **Authority conflicts:** [two systems writing same data]
- **Orphan systems:** [systems with no connections]
- **Glossary violations:** [wrong terminology used]
- **Signal mismatches:** [unregistered signals referenced]

### Registration
[Any mismatches between indexes and files]

### Recommendations (prioritized)
1. [Most impactful fix across all systems]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-system checks are the main value** of bulk review over individual `/scaffold-review-system` calls. Emphasize relationship issues.
- Be specific. Quote problematic text when flagging issues.
- If all systems are well-designed, say so. Don't manufacture issues.
- Prioritize recommendations by blast radius — issues that affect multiple systems rank higher than issues in a single system.
