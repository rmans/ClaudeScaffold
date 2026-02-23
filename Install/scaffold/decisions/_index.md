# Decisions — Index

> **Layer:** History — Architecture Decision Records, tracking, and design debt.
> **Authority:** ADRs do not carry authority themselves; they document *why* a decision was made and which authoritative document was updated as a result. Tracking docs record what's unresolved or compromised.

## Registered Decisions

<!-- Add ADRs as they are created. -->

| ID | Title | Status | Date |
|----|-------|--------|------|
| *None yet* | — | — | — |

## Tracking Documents

| File | Purpose |
|------|---------|
| [known-issues.md](known-issues.md) | TBDs, gaps, conflicts found during design or extraction |
| [design-debt.md](design-debt.md) | Intentional design compromises — deferred mechanics, tuning hacks |
| [playtest-feedback.md](playtest-feedback.md) | Playtester observations, patterns, and actions taken |

## Adding a Decision

1. Use the [decision template](../templates/decision-template.md).
2. Assign the next ADR-### ID.
3. Save the file in this directory as `ADR-###-title.md`.
4. Register it in the table above.

## When to Write an ADR

- When an engine constraint conflicts with a design document.
- When changing a system interface contract.
- When deprecating or replacing an input action ID.
- When any lower-authority document needs to deviate from a higher-authority document.
