---
name: scaffold-fix-roadmap
description: Review-fix loop for the roadmap — auto-fix mechanical issues (template text, vague goals, broken references, stale ADR log, terminology drift), surface strategic issues for human decision.
argument-hint: [--iterate N]
allowed-tools: Read, Edit, Grep, Glob
---

# Fix Roadmap

Iteratively review and auto-fix mechanical issues in `scaffold/phases/roadmap.md`: **$ARGUMENTS**

Reviews the roadmap, classifies issues as auto-fixable or human-required, applies safe fixes, and re-reviews until clean. This skill wraps the same checklist as `/scaffold-review-roadmap` but adds write capability for mechanical fixes.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--iterate N` | No | `10` | Maximum review-fix passes before stopping. Stops early on convergence — if a pass produces no new issues, iteration ends. |

## Step 1 — Read Context

1. Read the roadmap at `scaffold/phases/roadmap.md`.
2. Read the design doc at `scaffold/design/design-doc.md`.
3. Read the systems index at `scaffold/design/systems/_index.md`.
4. Read all ADRs with status `Accepted`.
5. Read known issues at `scaffold/decisions/known-issues.md`.
6. Read playtest feedback at `scaffold/decisions/playtest-feedback.md`.
7. Read the phases index at `scaffold/phases/_index.md`.
8. Read `scaffold/design/glossary.md` for canonical terminology.

If the roadmap is empty or at template defaults, stop: "Roadmap is at template defaults. Run `/scaffold-new-roadmap` first."

## Step 2 — Review

Run the full review checklist from `/scaffold-review-roadmap` — completeness, phase coverage, ADR feedback currency, vision alignment, and registration consistency. Do not duplicate the checklist here — refer to the review-roadmap skill for the authoritative checks.

Additionally check:
- **Phase goal quality** — each phase in the Phase Overview has an outcome-oriented goal, not a task list.
- **Milestone clarity** — each phase describes what can be demonstrated after it completes.
- **Phase ordering logic** — does each phase depend only on capabilities delivered by earlier phases? Detect dependency violations (phase requires systems introduced later) rather than enforcing a rigid sequence.
- **Capability progression** — each phase builds on the previous one's capability.
- **Terminology compliance** — glossary canonical terms used throughout.

Record all issues found.

## Step 3 — Classify Issues

### Auto-Fixable

Issues where the correct fix is unambiguous and local to the roadmap file:

| Category | Example |
|----------|---------|
| **Template text / TODOs** | `<!-- TODO: fill in -->` or template defaults still present → replace with content derived from design doc context |
| **Vision checkpoint drift** | Vision Checkpoint text doesn't match design doc Core Fantasy → update to match |
| **Stale ADR feedback log** | Accepted ADRs from completed phases missing from log → add entries |
| **Registration mismatch (in roadmap)** | Phase listed in roadmap but status doesn't match phase file → update roadmap status to match phase file (phase file is canonical). If the roadmap references a phase not present in `_index.md`, classify as human-required instead — the phase registry may be broken. |
| **Terminology drift** | Uses NOT-column glossary term → replace with canonical term |
| **Missing completed phase entries** | Phase marked Complete in overview but no entry in Completed Phases section → add stub entry with phase ID and TBD delivery notes |
| **Vague phase goal** | "Implement systems" → tighten to outcome-oriented goal derived from design doc. Auto-fix only when the intended outcome is explicitly stated in the design doc's Core Loop, Secondary Loops, or Design Pillars. If not explicitly stated → human-required. |
| **Missing phase link** | Current Phase section references a phase without a link → add link |
| **Capability ladder drift** | Phase in Phase Overview missing from Capability Ladder, or ladder capability text doesn't match phase's Capability Unlocked → sync ladder to match overview |
| **Missing phase boundary stub** | Phase lacks a Deferred section → add stub: "Deferred to later phases: TBD". Preserves structure without inventing scope. |
| **System coverage drift** | System in `systems/_index.md` not present in System Coverage Map or Deferred list → add to coverage map with "Unassigned" note. System assignment itself is human-required. |

### Human-Required

Issues that require judgment or cross-file coordination. Present using the Human Decision Presentation pattern (see WORKFLOW.md):

| Category | Why |
|----------|-----|
| **Phase coverage gap** | Design doc systems or features not assigned to any phase — planning decision |
| **Over-scoped roadmap** | Total scope exceeds design doc's Scope Reality Check — cut decision |
| **Under-scoped roadmap** | Major design doc features missing from all phases — add decision |
| **Phase ordering conflict** | Phases depend on systems not yet delivered — reorder decision |
| **Duplicate scope** | Multiple phases claim the same deliverables — dedup decision |
| **ADR contradicts roadmap** | Accepted ADR changes scope in ways the roadmap doesn't reflect — scope decision |
| **Playtest pattern conflict** | ACT NOW pattern not addressed in any phase — planning decision |
| **System-named phase** | Phase goal describes a system ("Event System", "Morale System") instead of observable behavior ("Colonists react to storms") — produces horizontal engineering slices instead of vertical gameplay slices. Reframing is a design decision. |
| **Missing phase boundaries** | Phase lacks explicit deferral list or "good enough" definition — will expand during slice generation until unfinishable |
| **Phase without demo** | Phase has no demo deliverable or demo scenario — phases without demos are usually weak milestones |
| **Phase not in index** | Roadmap references a phase not registered in `phases/_index.md` — may indicate broken phase registry |
| **System coverage assignment** | System appears in coverage map as "Unassigned" — requires planning decision about which phase introduces it |
| **Phase count concern** | Fewer than 2 or more than 12 phases may indicate roadmap is too coarse or too granular |
| **Missing Phase Transition Protocol** | Protocol section absent — template structure issue |

## Step 4 — Apply Auto-Fixes

For each auto-fixable issue:
1. Read the relevant section of the roadmap file.
2. Apply the fix using the Edit tool.
3. Record what was changed and why.

**Fix rules:**
- **Only edit the roadmap file.** Never edit phase files, indexes, design docs, or ADRs.
- Preserve the roadmap template structure.
- Fixes must be minimal — change only what's needed.
- When tightening goals, derive wording from the design doc, not invented.
- Never change what the roadmap delivers — only how clearly it expresses the plan.
- The phase file's internal Status field is canonical — if roadmap status differs, update the roadmap to match the phase file.

## Step 5 — Re-Review

After applying fixes, re-read the roadmap and run the full review checklist again.

Compare issues with the previous pass:
- **Resolved** — record as fixed.
- **New issues** — classify and fix if auto-fixable.
- **Persistent human-required** — carry forward.
- **No new issues, no remaining auto-fixable** — stop.

## Step 6 — Iterate

**Stop conditions** (any one stops iteration):
- **Clean** — no issues found.
- **Human-only** — only human-required issues remain.
- **Stable** — remaining issue set unchanged from previous pass.
- **Limit** — iteration limit reached.

## Step 7 — Output

```
## Roadmap Fix

### Summary
| Field | Value |
|-------|-------|
| Phases in roadmap | N |
| Passes | N completed / M max [early stop: yes/no] |
| Issues per pass | [e.g., 7 → 3 → 0 (healthy) or 7 → 6 → 6 (stuck)] |
| Auto-fixed | N issues |
| Human-required | N issues |
| Final status | Clean / Needs human input |

### Fixes Applied
| # | Category | What Changed | Section |
|---|----------|-------------|---------|
| 1 | Vision drift | Updated Vision Checkpoint to match design doc | Vision Checkpoint |
| 2 | Stale ADR log | Added ADR-007 entry for P1-001 | ADR Feedback Log |
| ... | ... | ... | ... |

### Human-Required Issues
| # | Category | Issue | Why Auto-Fix Cannot Resolve |
|---|----------|-------|----------------------------|
| 1 | Coverage gap | SYS-015 not in any phase | Requires planning decision |
| ... | ... | ... | ... |
```

If no issues found:
```
## Roadmap Fix

**Status: Clean** — no issues found. No changes made.
```

## Rules

- **Only fix mechanical, local issues.** Never make judgment calls about phase scope, ordering, or roadmap strategy.
- **Only edit the roadmap file.** Never edit phase files, indexes, design docs, or ADRs.
- **Derive fixes from context, don't invent.** Tightened goals come from the design doc.
- **Preserve roadmap structure.** Don't reorganize sections.
- **Stop when stable.** If remaining issues are unchanged, stop iterating.
- **Phase file status is canonical.** When the roadmap disagrees with a phase file's Status, the phase file wins.
