---
name: scaffold-bulk-review-references
description: Review all reference docs at once for completeness and cross-doc consistency. Use for a full audit of the reference layer.
allowed-tools: Read, Grep, Glob
---

# Bulk Reference Review

Review every reference and companion doc for completeness, accuracy, and cross-doc consistency.

## Documents Audited

| Doc | File |
|-----|------|
| Authority table | `scaffold/design/authority.md` |
| Interface contracts | `scaffold/design/interfaces.md` |
| State transitions | `scaffold/design/state-transitions.md` |
| Entity components | `scaffold/reference/entity-components.md` |
| Resource definitions | `scaffold/reference/resource-definitions.md` |
| Signal registry | `scaffold/reference/signal-registry.md` |
| Balance parameters | `scaffold/reference/balance-params.md` |
| Glossary | `scaffold/design/glossary.md` |
| Known issues | `scaffold/decisions/known-issues.md` |
| Design debt | `scaffold/decisions/design-debt.md` |

## Steps

### 1. Read Everything

1. Read all 10 documents listed above.
2. Read all system designs from `scaffold/design/systems/`.
3. Read the design doc at `scaffold/design/design-doc.md` for high-level cross-reference.

### 2. Per-Doc Completeness

For each document, assess:
- **Entry count** — how many entries exist?
- **Coverage** — what percentage of system-referenced items are registered?
- **Empty sections** — any sections still at template defaults?

Categorize each doc as: **Complete**, **Partial**, or **Empty**.

### 3. Cross-Doc Consistency

This is the main value of bulk review — checking relationships BETWEEN reference docs:

- **Authority ↔ Entity Components.** Every Authority column in entity-components must match the owning system in authority.md. Flag mismatches.
- **Authority ↔ Systems.** Every variable in authority.md should trace back to a system's responsibilities. Flag orphaned authority entries.
- **Signals ↔ System Outputs.** Every signal in signal-registry should correspond to a system Outputs table entry. Every system output should have a registered signal. Flag one-sided entries.
- **Interfaces ↔ Systems.** Every system-to-system communication in system Inputs/Outputs should have an interface contract. Flag system pairs that communicate but have no interface defined.
- **Interfaces ↔ Authority.** Data exchanged in interfaces should respect authority ownership — the owning system should be the source for push interfaces. Flag interfaces where a non-owner pushes data it doesn't own.
- **Signals ↔ Interfaces.** Every signal in signal-registry should implement an interface contract. Flag signals that don't have an interface contract and interface contracts that don't have a corresponding signal.
- **Resources ↔ Systems.** Every resource should be produced and consumed by at least one system. Flag resources with no producer or no consumer.
- **Resources ↔ Balance Params.** Resource-related numbers (stack limits, production rates, storage capacities) should appear in balance-params. Flag missing params.
- **Balance Params ↔ Systems.** Every parameter should reference a valid owning system. Flag orphaned params.
- **State Transitions ↔ Systems.** Every state machine's owning system should exist. Every entity with states should have a state machine. Flag gaps.
- **State Transitions ↔ Entity Components.** Entities with state machines should have a corresponding state/status field in entity-components. Flag missing fields.
- **Glossary ↔ Everything.** If the glossary has entries, check all reference docs for NOT-column terms. Flag terminology violations.

### 4. Gap Analysis

Identify what's missing by reading system designs and checking which data should exist but doesn't:

- Systems that don't contribute to ANY reference doc (underdesigned or reference docs not seeded)
- Entities mentioned in systems but not in entity-components
- Variables written in systems but not in authority table
- Resources consumed/produced but not in resource-definitions
- Numbers referenced but not in balance-params
- State changes implied but no state machine defined

### 5. Tracking Doc Check

For known-issues.md and design-debt.md:
- Are any resolved issues still in the Open section?
- Do any Open issues reference systems or docs that no longer exist?
- Are design debt items still relevant, or have they been silently resolved?

## Output Format

```
## Bulk Reference Review — X docs audited

### Overview
| Doc | Status | Entries | Coverage | Issues |
|-----|--------|---------|----------|--------|
| Authority | Partial | 12 | 80% | 3 |
| Entities | Complete | 5 | 100% | 0 |
| ... | ... | ... | ... | ... |

### Cross-Doc Consistency
- **Authority ↔ Entities:** [X matches, Y mismatches]
- **Signals ↔ Systems:** [X matched, Y orphaned signals, Z missing signals]
- **Resources ↔ Systems:** [status]
- **Balance ↔ Systems:** [status]
- **States ↔ Entities:** [status]
- **Glossary compliance:** [X violations found]

### Gap Analysis
[List of data that should exist but doesn't, organized by source system]

### Tracking Docs
- Known issues: X open, Y resolved
- Design debt: X active, Y paid off
- [Any stale entries]

### Recommendations (prioritized)
1. [Highest-impact fix across all docs]
2. [Second priority]
3. ...
```

## Rules

- This skill is read-only. Do not modify any files.
- **Cross-doc consistency is the main value.** Individual completeness is what `/scaffold-review-reference` does — bulk review focuses on relationships.
- Be specific. Name the exact entries and docs involved in every mismatch.
- If everything is consistent, say so. Don't manufacture issues.
- Prioritize by blast radius — issues affecting multiple docs rank higher.
