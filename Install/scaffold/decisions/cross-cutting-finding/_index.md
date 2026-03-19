# Cross-Cutting Findings — Index

> **Purpose:** Persistent log of cross-document integrity issues found by `/scaffold-validate --scope all` (Section 2l checks). Each finding gets its own file. The validator reads this index to avoid re-reporting known findings.

## Active Findings

| ID | Category | Downstream Doc | Severity | Status |
|----|----------|---------------|----------|--------|
<!-- Rows appended by /scaffold-validate --scope all. -->

## Resolution Protocol

| Status | Meaning | Validator Behavior |
|--------|---------|-------------------|
| **Open** | Finding is active and unresolved | Reports as FAIL/WARN per original severity |
| **Acknowledged** | User reviewed and accepts the risk (reason required) | Downgraded to INFO |
| **Resolved** | Issue fixed | Validator confirms on next run; removes if clean |
| **Deferred** | Tracked in KI-### or ADR-### (cross-reference required) | Downgraded to INFO |

## Categories

| Category | What It Covers |
|----------|---------------|
| `decision-closure` | Unresolved TODO/TBD/Open Questions in Approved/Complete docs |
| `workflow` | Missing pipeline prerequisites for current doc status |
| `staleness` | Upstream doc modified after downstream doc was stabilized |
