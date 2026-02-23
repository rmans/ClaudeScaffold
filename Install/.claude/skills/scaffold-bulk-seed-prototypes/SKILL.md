---
name: scaffold-bulk-seed-prototypes
description: Scan pipeline documents to identify prototype-worthy questions. Proposes prototype candidates from systems, engine docs, slices, and known issues.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Prototype Candidates

Scan the pipeline for questions that would benefit from a throwaway code spike.

## Steps

### 1. Read Context

1. **Read the prototypes index** at `scaffold/prototypes/_index.md` to find existing prototypes and the next available PROTO-### ID.
2. **Read the prototype template** at `scaffold/templates/prototype-template.md`.
3. **Read the design doc** at `scaffold/design/design-doc.md`.
4. **Read all system designs** — Glob `scaffold/design/systems/SYS-*.md`.
5. **Read the systems index** at `scaffold/design/systems/_index.md`.
6. **Read all engine docs** from `scaffold/engine/`.
7. **Read all slice files** — Glob `scaffold/slices/SLICE-*.md`.
8. **Read all spec files** — Glob `scaffold/specs/SPEC-*.md`.
9. **Read known issues** at `scaffold/decisions/known-issues.md`.
10. **Read design debt** at `scaffold/decisions/design-debt.md`.
11. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md`.
12. **Read the interfaces doc** at `scaffold/design/interfaces.md`.
13. **Read the state transitions** at `scaffold/design/state-transitions.md`.

### 2. Identify Prototype Candidates

Scan for uncertainty signals across the pipeline. Look for:

**From System Designs:**
- Open Questions sections with unresolved items
- System interactions where authority is unclear
- Performance-sensitive operations flagged in system docs
- Edge cases that question fundamental assumptions

**From Engine Docs:**
- Performance targets without evidence they're achievable
- Engine API usage patterns that haven't been validated
- Architecture patterns with uncertain scalability

**From Slices:**
- Integration points between systems that haven't been tested together
- Slices that depend on untested engine capabilities
- Complex state interactions across system boundaries

**From Specs:**
- Behavior descriptions with "if the engine supports..." qualifiers
- Edge cases that depend on timing or performance characteristics
- Acceptance criteria that reference measurable thresholds

**From Known Issues / Design Debt:**
- Open issues that need investigation before resolution
- Debt items that question whether current approach will scale
- Deferred decisions that need evidence to resolve

**From ADRs:**
- Accepted ADRs with open follow-up questions
- ADRs that deferred investigation to a later phase

### 3. Filter and Deduplicate

For each candidate:
- **Check existing prototypes** — skip if already covered by an existing PROTO-###.
- **Check ADRs** — skip if already resolved by an ADR.
- **Verify it requires building** — skip if the question can be answered by reading docs.
- **Verify it's specific** — skip or refine if the question is too broad.

### 4. Present Candidates

Present all candidates to the user, organized by source:

```
### From Systems
1. PROTO-### — [name]
   Question: [specific question]
   Source: SYS-### [section] — "[quote that raised the question]"
   Priority: [High / Medium / Low] — [why]

### From Engine
2. PROTO-### — [name]
   ...

### From Slices
3. PROTO-### — [name]
   ...

### From Known Issues / Debt
4. PROTO-### — [name]
   ...
```

Ask the user to confirm, modify, or remove candidates. Also ask if they want to add any prototypes not identified by the scan.

### 5. Create Prototype Files

For each confirmed candidate:

1. **Assign the next sequential PROTO-### ID.**
2. **Create** `scaffold/prototypes/PROTO-###-<name>.md` using the prototype template:
   - Fill in Question from the candidate.
   - Fill in Related Documents with the source reference.
   - Leave Hypothesis, Scope: Build, Scope: Skip, and Approach as TODO markers for the user to fill.
   - Leave all post-spike sections as TODO markers.
   - Set Status to Draft.
3. **Register** the prototype in `scaffold/prototypes/_index.md`.

### 6. Report

Summarize what was seeded:
- Prototypes created: X total
- By source: systems (N), engine (N), slices (N), known issues (N)
- Candidates filtered out: N (already covered, already decided, or too broad)

Remind the user:
- Fill in Hypothesis, Scope: Build, Scope: Skip, and Approach for each prototype
- Run `/scaffold-review-prototype` on each before starting the spike
- Use `/scaffold-prototype-log` after completing each spike

## Rules

- **Never write without confirmation.** Present all candidates before creating files.
- **Quality over quantity.** 3 well-scoped prototypes are worth more than 10 vague ones.
- **Each prototype answers ONE question.** If a candidate has multiple questions, split it.
- **Preserve existing prototypes.** If prototypes already exist, add to them — don't overwrite or duplicate.
- **IDs are sequential and permanent** — never skip or reuse.
- **Only fill Question and Related Documents** in seeded files. Leave Hypothesis, Scope, and Approach for the user — these require domain knowledge the scan can't provide.
- **Created documents start with Status: Draft.**
