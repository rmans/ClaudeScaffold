# Decisions — Index

> **Layer:** History — Architecture Decision Records, tracking, and design debt.
> **Authority:** ADRs do not carry authority themselves; they document *why* a decision was made and which authoritative document was updated as a result. Tracking docs record what's unresolved or compromised.

## Directories

| Directory | ID Format | Purpose | Template |
|-----------|-----------|---------|----------|
| [architecture-decision-record/](architecture-decision-record/_index.md) | ADR-### | Why decisions were made and what docs changed | [decision-template.md](../templates/decision-template.md) |
| [known-issues/](known-issues/_index.md) | KI-### | TBDs, gaps, conflicts, ambiguities | [known-issue-entry-template.md](../templates/known-issue-entry-template.md) |
| [design-debt/](design-debt/_index.md) | DD-### | Intentional design compromises with payoff plans | [design-debt-entry-template.md](../templates/design-debt-entry-template.md) |
| [playtest-feedback/](playtest-feedback/_index.md) | PF-### | Playtester observations and patterns | [playtest-feedback-entry-template.md](../templates/playtest-feedback-entry-template.md) |
| [cross-cutting-finding/](cross-cutting-finding/_index.md) | XC-### | Cross-document integrity issues from validate | [cross-cutting-finding-entry-template.md](../templates/cross-cutting-finding-entry-template.md) |
| [code-review/](code-review/_index.md) | CR-### | Adversarial code review logs | [code-review-log-template.md](../templates/code-review-log-template.md) |
| [revision-log/](revision-log/_index.md) | REVISION-[layer]-YYYY-MM-DD | Drift detection and update records | [revision-log-template.md](../templates/revision-log-template.md) |
| [triage-log/](triage-log/_index.md) | TRIAGE-[type]-SLICE-### | Spec/task triage decision records | [triage-log-template.md](../templates/triage-log-template.md) |
| [review/](review/_index.md) | ITERATE/FIX/REVIEW-* | Adversarial document review logs | [review-template.md](review/review-template.md) |

## Adding a Decision

1. Use the [decision template](../templates/decision-template.md).
2. Assign the next ADR-### ID.
3. Save the file in `architecture-decision-record/` as `ADR-###-title.md`.
4. Register it in [architecture-decision-record/_index.md](architecture-decision-record/_index.md).

## When to Write an ADR

- When an engine constraint conflicts with a design document.
- When changing a system interface contract.
- When deprecating or replacing an input action ID.
- When any lower-authority document needs to deviate from a higher-authority document.
- When implementation friction reveals a design gap that requires a decision.
