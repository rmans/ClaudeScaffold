---
name: scaffold-review-design
description: Review the design document for completeness and consistency. Use to audit unfilled sections, check system index sync, and validate cross-references.
allowed-tools: Read, Grep, Glob
---

# Design Document Review

Audit the design document and system designs for completeness and consistency.

## Steps

### 0. Read Advisory Context

Read theory docs for advisory context (these inform observations but never cause hard failures):
- `scaffold/theory/common-design-pitfalls.md` — flag patterns that match known anti-patterns
- `scaffold/theory/genre-conventions.md` — check alignment with genre expectations (if genre is stated)
- `scaffold/theory/narrative-design.md` — check narrative sections against storytelling principles
- `scaffold/theory/balance-principles.md` — check difficulty and pacing against balance principles

### 1. Design Doc Completeness

Read `scaffold/design/design-doc.md` and check every section for:
- **Unfilled TODOs** — count how many `*TODO:` markers remain.
- **Empty sections** — sections that have no content beyond the HTML comment prompt.
- **Placeholder text** — generic text that hasn't been customized to the actual game.

Categorize each section as: **Complete**, **Partial**, or **Empty**.

### 2. System Index Consistency

Read both index tables:
- `scaffold/design/design-doc.md` — the System Design Index table
- `scaffold/design/systems/_index.md` — the Registered Systems table

Check that:
- Every system in one table exists in the other (both directions).
- IDs match between the two tables.
- Names match between the two tables.
- Status values match between the two tables.

Flag any mismatches.

### 3. System File Existence

For every system registered in the index tables:
- Verify the corresponding `scaffold/design/systems/SYS-###-*.md` file actually exists.
- Flag any registered systems that are missing their file, or any system files that aren't registered.

### 4. System Design Completeness

For each system file found in `scaffold/design/systems/`:
- Check how many sections are filled in vs. still at template defaults.
- Flag systems that have unfilled critical sections (Purpose, Player Actions, System Resolution).

### 5. Cross-Reference Validation

Check that:
- Systems referencing other systems in their Inputs/Outputs tables reference systems that actually exist.
- No circular "blockers" exist (System A depends on System B which depends on System A with no resolution).

## Output Format

Present the review as a structured report:

```
## Design Doc Review

### Completeness: X/Y sections filled
[Table of sections with status]

### System Index: [In Sync / X mismatches found]
[List any mismatches]

### System Files: X registered, Y files found
[List any missing or unregistered files]

### System Completeness
[Per-system breakdown of filled vs. empty sections]

### Cross-References
[Any broken references or issues]

### Advisory Observations
[Patterns from theory docs — pitfalls or genre mismatches worth considering. Clearly labeled as advisory, not hard failures.]

### Recommendations
[Prioritized list of what to fill in next]
```

## Rules

- This skill is read-only. Do not modify any files.
- Be specific about what's missing — don't just say "incomplete", say which sections need attention.
- Prioritize recommendations by impact: Vision and Core Loop matter more than Business & Lifecycle early in development.
- **Theory observations are advisory only.** Present them as "worth considering" — never as errors or required fixes. Theory docs carry no authority.
