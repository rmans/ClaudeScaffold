---
name: scaffold-revise-foundation
description: Detect foundation drift from implementation feedback and dispatch revision loops to affected Step 1-6 docs. On initial pass, verifies foundational doc layers completed their normal stabilization pipeline. On recheck, reads ADRs/KIs/triage/spec-task friction to identify which docs need updating, then dispatches their normal stabilization pipeline.
argument-hint: [--mode initial|recheck]
allowed-tools: Read, Grep, Glob
---

# Revise Foundation

Detect foundation drift and dispatch revision loops to affected docs: **$ARGUMENTS**

This skill is the entry point for Step 7's pipeline. It has two modes:

- **Initial mode** (`--mode initial`, default) — On first pass after Steps 1–6, there is no implementation feedback to revise from. The skill verifies that Steps 1–6 each completed their normal stabilization pipeline (create/seed → review/fix → iterate → validate), reports their status, and proceeds. This is effectively a readiness check, not a revision.

- **Recheck mode** (`--mode recheck`) — After a phase completes, reads implementation feedback to identify which foundation docs need updating, then dispatches the appropriate revision loop for each affected doc.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--mode` | No | `initial` | `initial` for first pass (readiness check), `recheck` for post-implementation. |

### Context Files

| Context File | Why |
|-------------|-----|
| `scaffold/doc-authority.md` | Document authority ranking, same-rank conflict resolution rules, deprecation protocol |

## Initial Mode

### Verify Steps 1–6 readiness

For each Step 1–6 doc layer, check the expected stabilization pipeline completed:

| Step | Doc Layer | Expected Pipeline | Validation Gate |
|------|-----------|-------------------|-----------------|
| 1 | Design | init-design → fix-design → iterate-design → validate --scope design | `validate --scope design` passes |
| 2 | Systems | bulk-seed-systems → fix-systems → iterate-systems → validate --scope systems | `validate --scope systems` passes |
| 3 | References | bulk-seed-references → fix-references → iterate-references → validate --scope refs | `validate --scope refs` passes |
| 4 | Engine | bulk-seed-engine → fix-engine → iterate-engine | fix + iterate passes |
| 5 | Visual/UX | bulk-seed-style → fix-style → iterate-style | fix + iterate passes |
| 6 | Inputs | bulk-seed-input → fix-input → iterate-input | fix + iterate passes |

For each layer, verify:
- Do the documents exist and have non-placeholder content? (not stubs or template defaults)
- Did the appropriate review/fix/iterate pass run? (check for review logs, iterate logs, or fix logs)
- Did validation pass where applicable? (Step 1: `validate --scope design`, Step 3: `validate --scope refs`)
- Are there unresolved structural issues, failed validations, or placeholder-heavy docs?

Report status per layer:

```
## Foundation Readiness

| Step | Doc Layer | Status | Pipeline | Notes |
|------|-----------|--------|----------|-------|
| 1 | Design | Ready | init → fix → iterate → validate | All 13 design checks pass |
| 2 | Systems | Partial | seed → fix → iterate | 2 systems still stubs |
| 3 | References | Ready | seed → fix → validate | Reviewed, validated |
| 4 | Engine | Ready | seed → fix → iterate | Reviewed, iterated |
| 5 | Visual/UX | Ready | seed → fix → iterate | Reviewed, iterated |
| 6 | Inputs | Ready | seed → fix | Reviewed |

**Proceed to fix-foundation (7b):** Yes / No — [reason if no]
```

If any doc layer is not ready (missing, all stubs, never reviewed), stop and direct back to the appropriate step.

## Recheck Mode

### Step 1 — Gather implementation feedback

Read:
- ADRs filed during implementation (created/accepted since last foundation gate pass)
- `known-issues.md` deltas
- Triage logs and upstream actions
- Prototype findings
- Phase/roadmap revision notes and revision logs
- Playtest feedback patterns
- Implementation friction signals
- Code review findings that suggest foundation drift
- Spec/task friction signals (repeated triage, blocked tasks, recurring spec conflicts that suggest underlying architecture misalignment)

### Step 2 — Identify affected foundation areas

For each of the 6 foundation areas, check whether any feedback item implies drift:

| Area | Drift signal examples |
|------|----------------------|
| Identity/handles | ADR changes entity lifecycle, KI about stale handles, code review found handle misuse |
| Content-definition | ADR changes enum→registry boundary, new content type added without ID policy |
| Storage | ADR changes container type, performance issue with iteration, KI about stale references |
| Save/load | ADR changes serialization, KI about migration |
| Spatial | ADR changes tile convention, KI about map size, system added spatial queries differently |
| API boundaries | ADR changes ownership, triage moved authority, code review found cross-system mutation |

**A single drift signal may affect multiple foundation areas.** For example, an ADR that changes handle lifecycle may affect identity, storage, and save/load simultaneously. Map each signal to all areas it touches.

### Step 3 — Identify affected docs

Map affected foundation areas to the Step 1–6 docs that need revision:

| Affected doc layer | When to revise | Dispatch skill | Stabilization loop |
|-------------------|----------------|----------------|-------------------|
| Design doc (Step 1) | Vision, core loop, governance, or player-facing assumptions changed | `/scaffold-revise-design --source foundation-recheck --signals [signals]` | revise-design → fix-design → iterate-design → validate --scope design |
| Systems (Step 2) | Ownership, dependencies, or interfaces changed | Step 2 bulk-review → fix loop | bulk-review-systems → iterate |
| References (Step 3) | Authority, signals, entities, or states changed | Step 3 review → validate loop | bulk-review-references → validate --scope refs |
| Engine (Step 4) | Engine constraints or viability assumptions changed | Step 4 bulk-review → fix loop | bulk-review-engine → iterate |
| Visual/UX (Step 5) | UI architecture, presentation rules, or interaction model changed | Step 5 bulk-review → fix loop | bulk-review-style → iterate |
| Inputs (Step 6) | Input architecture or action model changed | Step 6 bulk-review → fix loop | bulk-review-input → iterate |

### Step 4 — Dispatch revision loops

**Dispatch in dependency order.** Revise upstream conceptual docs before downstream derivative docs. When multiple layers need revision, process them in authority order (design → systems → references → engine → visual/UX → inputs). This prevents stale-content loops — a system revision that depends on an updated design doc must wait for the design revision to complete first.

Only dispatch to layers that are actually affected by detected drift — don't re-run all Steps 1–6.

For each affected layer, run the following skills in sequence. Wait for each skill to complete before running the next. If any skill surfaces issues requiring user decisions, resolve those before continuing.

#### Step 1 — Design doc (if affected)

**Why:** Vision, core loop, governance, or player-facing assumptions changed. The design doc is the highest-authority document — if it needs updating, it must be revised first so all downstream layers revise against current design intent.

**Skills to run:**

1. `/scaffold-revise-design --source foundation-recheck --signals [signals]`
   - **What:** Reads only the specific drift signals passed via `--signals`. Classifies each as design-led vs implementation-led. Auto-updates safe mechanical changes. Dispatches to `init-design --mode reconcile/refresh` for design decisions. Escalates governance impacts.
   - **Why:** Targeted revision — doesn't re-scan the universe, just processes signals this skill identified.
2. `/scaffold-fix-design`
   - **What:** Auto-fixes template text, governance format normalization, terminology drift, system index mismatches. Surfaces contradictions, drift, and layer violations.
   - **Why:** Revise-design may have changed sections — fix catches mechanical issues introduced by those changes.
3. `/scaffold-iterate-design --sections "[changed groups]"`
   - **What:** Adversarial review scoped to only the topics relevant to the changed sections, with early convergence stopping. Uses the `--sections` argument from revise-design's report (e.g., if revise-design changed Shape and Philosophy, iterate runs Topics 1, 2, 4, 5 — not all 5 topics). Section-to-topic mapping is defined in iterate-design's `--sections` argument. Default max 10 iterations, but stops early when no new issues are found.
   - **Why:** Revise + fix may have shifted section content. Scoped iterate catches coherence issues in the changed areas without re-reviewing untouched sections.
   - **When to skip:** If revise-design made no changes (only auto-updated references or found no drift), skip iterate to save cost.
4. `/scaffold-validate --scope design`
   - **What:** 13 deterministic structural checks: section health, governance format, glossary compliance, ADR consistency, review freshness.
   - **Why:** Final gate confirming the design doc is structurally ready to govern downstream work again.

#### Step 2 — Systems (if affected)

**Why:** Ownership, dependencies, or system interfaces changed.

**Skills to run:**

1. `/scaffold-revise-systems --source foundation-recheck --signals [signals]`
   - **What:** Reads only the specific drift signals passed via `--signals`. Classifies each as design-led vs implementation-led. Auto-updates safe changes (dependency entries, edge cases). Escalates ownership shifts and authority violations.
   - **Why:** Targeted revision — doesn't re-scan everything, just processes signals this skill identified.
2. `/scaffold-fix-systems SYS-###-SYS-###`
   - **What:** Mechanical cleanup pass on affected systems. Normalizes structure, detects design signals.
   - **Why:** Revise-systems may have changed sections — fix catches mechanical issues introduced by those changes.
3. `/scaffold-iterate-systems --topics "[affected topics]" SYS-###-SYS-###`
   - **What:** Adversarial review scoped to affected topics and systems, with early convergence.
   - **Why:** Revise + fix may have shifted system content. Scoped iterate catches design issues in changed areas.
   - **When to skip:** If revise-systems made no changes (only found no drift), skip iterate.
4. `/scaffold-validate --scope systems --range SYS-###-SYS-###`
   - **What:** 16 deterministic structural checks on affected systems.
   - **Why:** Final gate confirming system docs are structurally ready.

#### Step 3 — References (if affected)

**Why:** Authority, signals, entities, or state transitions changed.

**Skills to run:**

1. `/scaffold-revise-references --source foundation-recheck --signals [signals]`
   - **What:** Reads only the specific drift signals passed via `--signals`. Classifies each as design-led vs implementation-led. Auto-updates safe changes (missing registrations, stale references, column updates). Escalates authority changes, architecture changes, contract changes, and state machine changes.
   - **Why:** Targeted revision — doesn't re-scan everything, just processes signals this skill identified. Respects canonical direction (authority→entity, interfaces→signals, states→enums).
2. `/scaffold-fix-references --target [affected-doc.md]`
   - **What:** Mechanical cleanup targeted at the specific doc(s) that were revised. Per-doc structural checks plus cross-doc consistency against all 9 Step 3 docs. Auto-fixes alignment issues. Detects design signals.
   - **Why:** Revise may have changed authority entries, interface contracts, or state names — fix-references catches mechanical inconsistencies introduced by those changes and propagates alignment fixes.
   - **Target selection:** If drift affected authority.md, target authority.md. If multiple docs affected, run without `--target` to fix all.
3. `/scaffold-iterate-references --target [affected-doc.md] --topics "[affected topics]"`
   - **What:** Adversarial review scoped to the affected doc and relevant topics. Uses `--target` to auto-select topics.
   - **Why:** Fix-references catches mechanical issues; iterate-references catches conceptual drift, cross-doc contradictions, and design quality issues.
   - **When to skip:** If revise-references and fix-references found no issues and no design signals, skip iterate.
4. `/scaffold-validate --scope refs`
   - **What:** Deterministic validation — Python script (9 checks) plus expanded checks (33+ checks covering structure, values, cross-doc consistency).
   - **Why:** Programmatic gate — reference docs must be structurally consistent before foundation integration runs.

#### Step 4 — Engine (if affected)

**Why:** Engine constraints, viability assumptions, or platform rules changed. Step 3 docs were revised and engine docs must catch up.

**Skills to run:**

1. `/scaffold-revise-engine --source foundation-recheck --signals [signals]`
   - **What:** Detects engine doc drift from Step 3 changes, ADRs, code review findings, and implementation friction. Auto-applies safe updates (stale references, Step 3 alignment, constrained TODO resolution). Escalates convention changes and performance budget revisions.
   - **Why:** Engine docs are Rank 9 — they implement Step 3 decisions. When Step 3 changes, engine docs must follow. revise-engine classifies drift and applies safe changes directly.
2. `/scaffold-fix-engine` (if revise-engine made changes)
   - **What:** Mechanical cleanup after revision — cross-engine consistency, template structure, terminology.
   - **When to skip:** If revise-engine made no changes (only found no drift), skip fix.
3. `/scaffold-iterate-engine --target [affected-doc] --topics "1,2"` (for specifically affected engine docs)
   - **What:** Adversarial review focused on architecture implementation fidelity and authority compliance for the revised doc(s).
   - **When to skip:** If revise-engine and fix-engine found no issues and no design signals, skip iterate.

#### Step 5 — Visual/UX (if affected)

**Why:** UI architecture, presentation rules, interaction model, or visual identity assumptions changed.

**Skills to run:**

1. `/scaffold-revise-style --source foundation-recheck --signals [signals]`
   - **What:** Reads only the specific drift signals passed via `--signals`. Classifies each as design-led, playtest-led, or implementation-led. Auto-updates safe changes (missing tokens, stale references, new feedback entries, cross-doc alignment). Escalates aesthetic direction changes, interaction model changes, priority hierarchy changes, accessibility changes, and component removals.
   - **Why:** Targeted revision — doesn't re-scan everything, just processes signals this skill identified. Respects Step 5 authority flow (style-guide → color-system → ui-kit; feedback-system → audio-direction).
2. `/scaffold-fix-style --target [affected-doc.md]`
   - **What:** Mechanical cleanup targeted at the specific doc(s) that were revised. Per-doc structural checks plus cross-doc consistency across all 6 Step 5 docs. Auto-fixes alignment issues. Detects design signals.
   - **Why:** Revise may have added tokens, feedback entries, or interaction mappings — fix-style catches mechanical inconsistencies introduced by those changes and propagates alignment fixes.
   - **Target selection:** If drift affected a single doc, target it. If multiple docs affected, run without `--target` to fix all.
3. `/scaffold-iterate-style --target [affected-doc.md] --topics "[affected topics]"`
   - **What:** Adversarial review focused on the revised areas of the affected Step 5 doc(s).
   - **Why:** Revise and fix catch mechanical issues; iterate catches conceptual drift in aesthetic direction, interaction design, and feedback coherence.
   - **When to skip:** If revise-style and fix-style found no issues and no design signals, skip iterate.

#### Step 6 — Inputs (if affected)

**Why:** Input architecture, action model, or binding assumptions changed.

**Skills to run:**

1. `/scaffold-bulk-review-input`
   - **What:** Audits all input docs for completeness and cross-doc consistency (action map ↔ bindings ↔ navigation ↔ philosophy ↔ design doc ↔ interaction model).
   - **Why:** Detects misalignment between input docs and the (potentially revised) design doc control model and interaction model.
2. `/scaffold-iterate inputs/[affected-doc].md` (for specifically affected input docs)
   - **What:** Adversarial review of the affected input doc(s).
   - **When to skip:** If bulk-review found no issues.

#### After all dispatched revisions complete

Proceed to Step 7b (`fix-foundation`) for cross-doc integration verification. Individual layer revisions may have introduced new cross-layer contradictions that only the foundation-level integration check can catch.

### Step 5 — Report

```
## Foundation Revision: Post-Implementation

**Mode:** Recheck
**Foundation areas checked:** 6
**Areas with drift:** N
**Docs revised:** N
**Feedback sources:** N ADRs, N KIs, N triage actions, N spec/task friction signals

### Drift Detected
| Foundation Area | Drift Signal | Affected Docs |
|----------------|-------------|---------------|
| Identity | ADR-### changed handle semantics | systems, references |
| API boundaries | Triage moved ownership of X | authority, systems |

### Revisions Dispatched
| Doc Layer | Dispatch Command | Signals Passed | Status |
|-----------|-----------------|----------------|--------|
| Design (Step 1) | revise-design --source foundation-recheck --signals ADR-015,KI:colonist-autonomy | ADR-015, KI:colonist-autonomy | Complete |
| Systems (Step 2) | Step 2 bulk-review → iterate | — (full layer review) | Complete |
| References (Step 3) | Step 3 bulk-review → validate --scope refs | — (full layer review) | Complete |

### No Drift
| Foundation Area |
|----------------|
| Content-definition |
| Storage |
| Save/load |
| Spatial |

**Proceed to fix-foundation (7b):** Yes — dispatched revisions complete
```

If no drift is detected in any area:
```
## Foundation Revision: Post-Implementation

**Mode:** Recheck
**Foundation areas checked:** 6
**Areas with drift:** 0
**Drift detected:** None

No foundation docs require revision. Proceed directly to fix-foundation (7b) for cross-doc integration verification.
```

## Rules

- **This skill never edits docs directly.** It dispatches revision loops to the appropriate Step 1–6 pipelines.
- **Only revise affected docs.** Don't re-run the full Steps 1–6 pipeline on every recheck.
- **Dispatch in dependency order.** Revise upstream conceptual docs before downstream derivative docs, using the project's document authority and dependency chain (design → systems → references → engine → visual/UX → inputs) to prevent stale-content loops.
- **Initial mode is a readiness check, not a revision.** If Steps 1–6 aren't ready, stop — don't try to compensate.
- **Recheck mode prioritizes concrete signals** (ADRs, KIs, triage logs, review notes, spec/task friction) when detecting drift.
- **A single signal may affect multiple areas.** Map each signal to all foundation areas it touches, not just the most obvious one.
- **After dispatched revisions complete, the cross-doc integration loop (7b fix-foundation → 7c validate) must run.** Individual doc revisions may introduce new cross-doc contradictions.
