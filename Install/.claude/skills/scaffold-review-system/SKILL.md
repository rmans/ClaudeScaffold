---
name: scaffold-review-system
description: Review a specific system design for completeness and quality. Use to audit a single system's design file.
argument-hint: [SYS-ID or system-name]
allowed-tools: Read, Grep, Glob
---

# System Design Review

Review the system design for: **$ARGUMENTS**

## Locate the System

1. If the argument is a SYS-### ID, look for the matching file in `scaffold/design/systems/`.
2. If the argument is a name, search `scaffold/design/systems/_index.md` for a matching entry and find the file.
3. If no argument is provided, list all registered systems and ask the user which one to review.
4. If the system file doesn't exist, report that and stop.

## Review Checklist

Read the system file and evaluate each section:

### Completeness

Check each section and categorize as **Complete**, **Partial**, or **Empty**:

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

### Quality

For sections that are filled in, check:

- **Player Actions use player language, not code language.** Flag any mention of signals, methods, nodes, classes, functions, or variable names. The system design is behavior-level, not implementation.
- **Steps are concrete, not vague.** "The player places a wall" is good. "The player interacts with the building system" is too vague.
- **Failure states include what the player sees.** Not just "it fails" — what visual/audio feedback communicates the problem?
- **Dependencies reference real systems.** Check that every system named in Inputs/Outputs actually exists in `scaffold/design/systems/_index.md`. Flag any that don't.
- **Non-Responsibilities draw clear lines.** They should prevent the most likely scope creep for this system.
- **Edge cases answer real questions.** Not hypotheticals — things a player would actually try or wonder about.

### Registration

- Verify the system is registered in `scaffold/design/systems/_index.md`.
- Verify the system is registered in the System Design Index in `scaffold/design/design-doc.md`.
- Check that the ID, name, and status match across both tables and the file itself.

## Output Format

```
## System Review: SYS-### — [Name]

### Section Completeness: X/11 complete
| Section | Status | Notes |
|---------|--------|-------|
| ...     | ...    | ...   |

### Quality Issues
- [List any issues found, with specific quotes from the doc]

### Registration: [OK / Issues found]
- [Status of both index entries]

### Recommendations
1. [Most important thing to fix or fill in]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific. Quote the problematic text when flagging issues.
- Distinguish between "empty" (needs writing) and "bad" (needs rewriting). Both need action but for different reasons.
- If the system is well-designed, say so. Don't manufacture issues.
