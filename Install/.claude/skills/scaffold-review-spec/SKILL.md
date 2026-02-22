---
name: scaffold-review-spec
description: Review a behavior spec for clarity, completeness, acceptance criteria, and system alignment. Use to audit a single spec.
argument-hint: [SPEC-### or spec-name]
allowed-tools: Read, Grep, Glob
---

# Spec Review

Review the behavior spec for: **$ARGUMENTS**

## Locate the Spec

1. If the argument is a SPEC-### ID, look for the matching file in `scaffold/specs/`.
2. If the argument is a name, search `scaffold/specs/_index.md` for a matching entry and find the file.
3. If no argument is provided, list all registered specs and ask the user which one to review.
4. If the spec file doesn't exist, report that and stop.

## Read Context

1. **Read the spec file.**
2. **Read the parent system design** — follow the System reference in the spec header.
3. **Read the parent slice** — find which slice this spec belongs to via `scaffold/slices/_index.md` or `scaffold/specs/_index.md`.
4. **Read state transitions** at `scaffold/design/state-transitions.md` for relevant state machines.
5. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.

## Review Checklist

### Completeness

Check each section and categorize as **Complete**, **Partial**, or **Empty**:

| Section | What "Complete" Means |
|---------|----------------------|
| Summary | One clear sentence explaining what behavior this spec defines |
| Preconditions | At least 1 concrete condition that must be true before the behavior occurs |
| Behavior | Numbered steps describing the behavior — each step is testable |
| Postconditions | At least 1 concrete condition that must be true after the behavior completes |
| Edge Cases | At least 2 boundary conditions or unusual inputs with expected outcomes |
| Acceptance Criteria | At least 2 concrete, verifiable tests or checks |

### Quality

- **Behavior describes WHAT, not HOW.** Flag any mention of signals, methods, nodes, classes, functions, variable names, engine constructs, or implementation details. Specs are behavior-level, not implementation.
- **Steps are precise and testable.** "The player places a wall on an empty tile" is good. "The building behavior happens" is too vague. Each step should describe one observable action or result.
- **Preconditions are verifiable.** "Player has at least 10 wood" is good. "Player is ready" is not.
- **Postconditions describe observable state changes.** "The wall appears on the tile" is good. "The system state updates" is too abstract.
- **Edge cases cover real scenarios.** What happens at the boundary? What if the player interrupts? What if resources are insufficient? Flag hypothetical edge cases that could never actually occur.
- **Acceptance criteria are concrete.** Each criterion should be a test you could actually run or manually verify. "Verify it works" is not a criterion.

### System Alignment

- Check that the spec's behavior aligns with the parent system design's Player Actions and System Resolution sections.
- Flag behaviors in the spec that contradict the system design.
- Flag behaviors in the system design that this spec claims to cover but actually doesn't.
- If the spec references state transitions, verify they match `scaffold/design/state-transitions.md`.

### ADR Impact

- Check if any ADRs affect this spec's domain.
- Flag ADRs that change system behavior covered by this spec but aren't reflected in the spec.

### Registration

- Verify the spec is registered in `scaffold/specs/_index.md`.
- Verify the spec appears in its parent slice's Specs Included table.
- Check that the ID, name, system reference, and slice reference match across all locations.

## Output Format

```
## Spec Review: SPEC-### — [Name]

### Section Completeness: X/6 complete
| Section | Status | Notes |
|---------|--------|-------|
| ...     | ...    | ...   |

### Quality Issues
- [List any issues found, with specific quotes from the doc]

### System Alignment: [OK / Issues found]
- [Alignment status with parent system design]

### ADR Impact: [No ADRs / X ADRs affect this spec]
- [Relevant ADRs and their impact]

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
- Implementation leaks are the #1 issue in specs — weight them heavily. Specs describe BEHAVIOR, not IMPLEMENTATION.
- Distinguish between "empty" (needs writing) and "bad" (needs rewriting).
- If the spec is well-written, say so. Don't manufacture issues.
