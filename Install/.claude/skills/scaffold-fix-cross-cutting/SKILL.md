---
name: scaffold-fix-cross-cutting
description: Resolve cross-document integrity findings from validate. Reads cross-cutting-findings.md, dispatches fix actions per category (decision closure, workflow integrity, upstream staleness), and updates finding status. Interactive — presents options for judgment calls.
argument-hint: [--category decision-closure|workflow|staleness] [--id XC-###]
allowed-tools: Read, Edit, Write, Bash, Grep, Glob
---

# Fix Cross-Cutting Findings

Resolve cross-document integrity findings: **$ARGUMENTS**

This skill reads `scaffold/decisions/cross-cutting-findings.md`, processes Open findings, and dispatches the appropriate fix action for each. Some fixes are mechanical (auto-applied). Others require human judgment (presented as options).

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--category` | No | all | Filter to one category: `decision-closure`, `workflow`, `staleness`. |
| `--id` | No | all | Fix a single finding by ID (e.g., `XC-003`). |

## Context Files

Read these before processing findings:

| Context File | Why |
|-------------|-----|
| `scaffold/decisions/cross-cutting-findings.md` | Primary input — the findings to resolve |
| `scaffold/doc-authority.md` | Authority ranking for conflict resolution |
| `scaffold/decisions/known-issues.md` | Check if findings are already tracked here |
| `scaffold/decisions/design-debt.md` | Check if findings are already tracked here |
| ADRs with status `Accepted` | Check if findings are already resolved by ADRs |

## Preflight

1. Read `scaffold/decisions/cross-cutting-findings.md`.
2. Parse the Active Findings table.
3. Filter to Open findings only (skip Acknowledged, Resolved, Deferred).
4. If `--category` is set, filter to that category.
5. If `--id` is set, filter to that single finding.
6. If no Open findings match, report "No open findings to resolve" and stop.
7. Group findings by category for presentation.

## Fix Actions by Category

### Decision Closure Findings

These indicate Approved/Complete docs with unresolved TODO/TBD/Open Questions.

**For each finding:**

1. Read the downstream doc cited in the finding.
2. Locate the unresolved marker (TODO, TBD, Open Questions section).
3. Classify the marker:
   - **Resolvable now** — the information exists elsewhere in the scaffold (upstream doc, ADR, system design). Auto-fill the answer and remove the marker.
   - **Needs user decision** — the marker represents a genuine open question. Present options:
     - (a) **Resolve** — user provides the answer, skill writes it and removes the marker.
     - (b) **Defer** — file in known-issues.md or reference an existing ADR. Mark finding as Deferred with tracking reference.
     - (c) **Downgrade status** — revert the doc from Approved back to Draft (rename file with `git mv`, update `_index.md`). Mark finding as Resolved (the closure requirement no longer applies at Draft).
   - **Constrained TODO (engine docs only)** — the marker is legitimately blocked on an upstream Step 3 decision. Verify the blocking decision is still unresolved. If so, mark finding as Acknowledged with reason "blocked on [upstream doc]". If the blocking decision was resolved, auto-fill and remove the marker.

4. After resolving, update the finding's Status in cross-cutting-findings.md.

### Workflow Integrity Findings

These indicate missing pipeline prerequisites for the doc's current status.

**For each finding, dispatch the missing step:**

| Finding | Auto-Fix | Dispatch Action |
|---------|----------|----------------|
| Slice missing iterate log | No | "Run `/scaffold-iterate-slice SLICE-###` to create the missing review. Or revert to Draft if the slice was approved prematurely." |
| Phase missing iterate log | No | "Run `/scaffold-iterate-phase P#-###` to create the missing review. Or revert to Draft." |
| Tasks approved before reorder | No | "Run `/scaffold-reorder-tasks SLICE-###` to fix ordering. Then re-run `/scaffold-approve-tasks SLICE-###`." |
| Phase approved before predecessor Complete | No | "Complete P#-### first, or revert P#-### to Draft. Entry criteria require it." |
| Complete phase missing from roadmap | Partial | Read the phase file and draft a Completed Phases entry. Present to user for confirmation. Run `/scaffold-revise-roadmap` if approved. |
| Validate appears stale | No | "Run `/scaffold-validate --scope [relevant]` to refresh. This is advisory — no structural change needed." |

**Workflow findings cannot be auto-fixed** because they represent missing process steps that need to actually run, not just files to edit. The skill dispatches the user to the right command.

### Staleness Findings

These indicate upstream docs changed after downstream docs were stabilized.

**For each finding:**

1. Read both the upstream doc and the downstream doc.
2. Identify what changed in the upstream doc (diff against the downstream doc's stabilization date if possible, or read the upstream doc's recent changelog/revision history section).
3. Classify the change:
   - **No impact** — the upstream change doesn't affect the downstream doc's content. Mark finding as Resolved with reason "upstream change does not affect [downstream doc]: [brief explanation]".
   - **Minor impact** — the downstream doc needs a small update (terminology, reference, section name). Auto-apply the edit. Mark finding as Resolved.
   - **Major impact** — the downstream doc needs restabilization. Present options:
     - (a) **Restabilize** — dispatch the appropriate fix/iterate skill for the downstream doc type. Mark finding as "Resolved — restabilization dispatched".
     - (b) **Defer** — the downstream doc is still usable as-is despite upstream drift. Add to known-issues.md with the staleness note. Mark finding as Deferred.
     - (c) **Escalate** — the upstream change implies a broader architecture shift. File an ADR stub. Mark finding as Deferred with ADR reference.

4. After resolving, update the finding's Status in cross-cutting-findings.md.

**Staleness dispatch table:**

| Downstream Type | Restabilization Command |
|----------------|------------------------|
| Spec | `/scaffold-fix-spec SPEC-###` then `/scaffold-iterate-spec SPEC-###` |
| Task | `/scaffold-fix-task TASK-###` then `/scaffold-iterate-task TASK-###` |
| Engine doc | `/scaffold-fix-engine --target [stem]` then `/scaffold-iterate-engine --target [stem]` |
| Roadmap | `/scaffold-fix-roadmap` then `/scaffold-iterate-roadmap` |
| Slice | `/scaffold-fix-slice SLICE-###` then `/scaffold-iterate-slice SLICE-###` |

## Execution Flow

```
1. Preflight (read findings, filter)
2. Group by category
3. Present summary:
   "Found N open findings: X decision-closure, Y workflow, Z staleness"
4. Process each category:
   a. Decision closure — attempt auto-resolve, present options for judgment calls
   b. Workflow — present dispatch commands, user runs them
   c. Staleness — classify impact, auto-fix minor, present options for major
5. After all findings processed:
   a. Update cross-cutting-findings.md with new statuses
   b. Report summary
```

## Report

```
## Cross-Cutting Fix Complete

### Summary
| Category | Open Before | Resolved | Acknowledged | Deferred | Still Open |
|----------|------------|----------|--------------|----------|-----------|
| Decision Closure | N | N | N | N | N |
| Workflow | N | N | N | N | N |
| Staleness | N | N | N | N | N |

### Actions Taken
- XC-001: Resolved — auto-filled TODO from architecture.md section [X]
- XC-002: Deferred — tracked in KI-### (genuine open question)
- XC-003: Dispatched — user needs to run `/scaffold-iterate-slice SLICE-009`

### Recommended Next Steps
- [List any dispatched commands the user needs to run]
- [Any ADR stubs that need completion]
- [Suggest re-running validate to confirm resolutions]
```

## Rules

- **Read-then-act.** Always read both the finding and the cited docs before deciding on an action. Never assume the finding is still valid — the issue may have been fixed since the last validate run.
- **Never auto-fix workflow findings.** Workflow findings represent missing process steps. The skill tells the user what to run — it doesn't fake the pipeline step.
- **Auto-fix only when certain.** Decision closure and staleness findings can be auto-fixed only when the correct answer is unambiguous from existing scaffold docs. When in doubt, present options.
- **Update findings doc after every action.** Don't batch updates — write each status change immediately so progress is not lost if the skill is interrupted.
- **Acknowledge requires a reason.** "Acknowledged" without an explanation is rejected. The reason must explain why the risk is acceptable.
- **Defer requires a tracking reference.** "Deferred" without a KI-### or ADR-### reference is rejected. Bare deferrals are not allowed.
- **Never edit upstream docs.** This skill fixes downstream docs or dispatches restabilization. If the upstream doc is wrong, that's an ADR, not a cross-cutting fix.
- **Respect document authority.** When resolving conflicts between findings, `scaffold/doc-authority.md` determines which doc is correct.
- **Present decisions grouped.** Don't interleave categories — process all decision-closure findings, then all workflow, then all staleness. This lets the user batch similar decisions.
- **One finding, one action.** Each finding gets exactly one outcome: Resolved, Acknowledged, Deferred, or Still Open. No partial resolutions.
