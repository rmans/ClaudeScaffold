---
name: scaffold-fix-design
description: Review-fix loop for the design document — auto-fix mechanical issues (template text, incomplete sections, terminology drift, missing invariant format), surface strategic issues (contradictions, drift, scope creep) for human decision.
argument-hint: [--iterate N] [--sections "Identity,Shape"]
allowed-tools: Read, Edit, Grep, Glob
---

# Fix Design

Iteratively review and auto-fix mechanical issues in `design/design-doc.md`: **$ARGUMENTS**

Reviews the design doc against the section structure defined by `init-design`, classifies issues as auto-fixable or human-required, applies safe fixes, and re-reviews until clean. This skill wraps the same checklist as `/scaffold-review-design` but adds write capability for mechanical fixes.

The design doc is the highest authority for player-facing intent and non-breakable design rules. This skill fixes how clearly the doc expresses that intent — it never changes what the game is.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--iterate N` | No | `10` | Maximum review-fix passes before stopping. Stops early on convergence — if a pass produces no new issues, iteration ends. |
| `--sections` | No | all | Comma-separated section groups to focus on (e.g., `"Identity,Philosophy"`) |

## Step 1 — Read Context

1. Read `design/design-doc.md`.
2. Read `design/glossary.md` for canonical terminology.
3. Read `design/systems/_index.md` to check System Design Index references.
4. Read accepted ADRs that may affect design decisions.
5. Read `decisions/known-issues.md` for constraints affecting design.

If the design doc is empty or at template defaults, stop: "Design doc is at template defaults. Run `/scaffold-init-design` first."

## Step 2 — Review

Run the full review checklist from `/scaffold-review-design` — completeness, quality, cross-references, and consistency. Do not duplicate the checklist here — refer to the review-design skill for the authoritative checks.

Additionally check against the `init-design` section structure:

### Section completeness (9 groups, ~40–50 sections depending on optional items)

For each section group (Identity, Shape, Control, World, Presentation, Content, System Domains, Philosophy, Scope), verify:
- Section exists (not structurally absent)
- Section has non-placeholder content (not TODO or template default)
- Section is internally consistent (doesn't contradict itself)
- **Shadow section detection** — detect sections that describe the same primary design concept under different names (e.g., "Core Loop" vs "Gameplay Flow"). Only flag when sections appear to define the same mechanic or player interaction model — related but distinct sections (Core Loop vs Session Shape) are not shadows.

### Governance structure

- **Design Invariants** — each follows the format: `Invariant: <ShortName>`, `Rule:`, `Reason:`, `Implication:`. Missing fields are auto-fixable if the rule text is clear enough to derive them.
- **Decision Anchors** — 3–5 items, each in "X over Y" format.
- **Design Pressure Tests** — each follows: `Pressure Test: <name>`, `Scenario:`, `Expectation:`, `Failure Signal:`.
- **Design Gravity** — 3–4 directional statements.

### Cross-reference consistency

- System Design Index matches `systems/_index.md`
- Terminology matches `glossary.md` canonical terms
- No contradictions with accepted ADRs

### Design governance checks

- **Invariant violations from downstream** — do any existing system docs, specs, or slices imply mechanics that violate a Design Invariant? When detected, classify the signal:
  - **Speculative** — concept or proposal not yet implemented (informational only)
  - **Implementation drift** — implemented system contradicts design (actionable)
  - **Design evolution** — project direction changed but design doc not updated (actionable)
  Only Implementation drift and Design evolution are treated as actionable issues. Speculative signals are logged but don't block.
  **Drift detection sources:** system design documents, gameplay specs, vertical slices, implemented task documentation. Concept notes or experimental proposals are treated as Speculative.
- **Unescalated new mechanics** — do downstream docs introduce player-facing mechanics not described in the design doc? (Design decision escalation rule)
- **Anchor coverage** — do Decision Anchors actually resolve the ambiguous design choices visible in the project?

Record all issues found.

## Step 3 — Classify Issues

### Auto-Fixable

Issues where the correct fix is unambiguous and local to the design doc:

| Category | Example |
|----------|---------|
| **Template text / TODOs** | `<!-- TODO: fill in -->` still present → replace with content derived from existing sections or other docs |
| **Incomplete invariant format** | Invariant has Rule but missing Reason/Implication → derive from context if unambiguous |
| **Incomplete pressure test format** | Missing Scenario/Expectation/Failure Signal fields → derive from test name if unambiguous |
| **Terminology drift** | Uses NOT-column glossary term → replace with canonical term |
| **System index mismatch** | System Design Index doesn't match `systems/_index.md` → sync to match index |
| **Missing section stub** | Required section from init-design structure is absent → add empty stub with section heading |
| **Stale ADR reference** | References deprecated ADR → update reference |
| **Provisional marker cleanup** | `<!-- PROVISIONAL -->` markers on sections that are now substantive → remove marker |

### Human-Required

Issues that require judgment or design decisions. Present using the Human Decision Presentation pattern (see WORKFLOW.md):

| Category | Why |
|----------|-----|
| **Contradictory sections** | Two sections describe mutually exclusive mechanics — design decision |
| **Invariant violation from downstream** | System/spec/slice implies mechanic breaking an invariant — reconcile or update invariant |
| **Unescalated mechanic** | Downstream doc introduces player-facing mechanic not in design doc — design decision |
| **Vague invariant** | Invariant rule is too broad to be testable — needs sharpening |
| **Missing invariant** | Project behavior suggests an undocumented invariant should exist — design decision |
| **Anchor conflict** | Two Decision Anchors contradict in a real scenario — needs resolution |
| **Pressure test failure** | A current feature would fail a defined pressure test — design decision |
| **Philosophy drift** | Philosophy section wording no longer matches actual project direction — needs refresh |
| **Scope creep signal** | Design doc describes features beyond the roadmap's scope — cut or roadmap decision |
| **Design gravity violation** | Recent additions deepen the game in a direction not listed in Design Gravity — needs evaluation |
| **Layer violation** | Design doc contains system-layer truth (ownership, schemas, signals, bindings) that belongs in later-step docs |

## Step 4 — Apply Auto-Fixes

For each auto-fixable issue:
1. Read the relevant section of the design doc.
2. Apply the fix using the Edit tool.
3. Record what was changed and why.

**Fix rules:**
- **Only edit the design doc.** Never edit system designs, reference docs, engine docs, or other downstream documents.
- Preserve the design doc's section structure — don't reorganize.
- Fixes must be minimal — change only what's needed.
- When filling stubs, derive wording from existing sections or other authoritative docs, not invented.
- Never change what the game is — only fix how clearly the doc expresses it.
- Invariant format fixes must preserve the original rule meaning exactly.
- Do not remove `<!-- PROVISIONAL -->` markers unless the section now has substantive, confirmed content.

## Step 5 — Re-Review

After applying fixes, re-read the design doc and run the full review checklist again.

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
## Design Fix

### Summary
| Field | Value |
|-------|-------|
| Sections checked | N / total defined |
| Passes | N completed / M max [early stop: yes/no] |
| Issues per pass | [e.g., 12 → 5 → 1 (healthy) or 12 → 11 → 11 (stuck)] |
| Auto-fixed | N issues |
| Human-required | N issues |
| Final status | Clean / Needs human input |

### Design Health: N%
| Status | Count |
|--------|-------|
| Complete | N |
| Partial | N |
| Missing | N |
| Template default | N |

### Governance Status
| Mechanism | Status |
|-----------|--------|
| Design Invariants | N defined, N properly formatted |
| Decision Anchors | N defined (target: 3-5) |
| Pressure Tests | N defined, N properly formatted |
| Design Gravity | N defined (target: 3-4) |

### Fixes Applied
| # | Category | What Changed | Section |
|---|----------|-------------|---------|
| 1 | Template text | Replaced TODO in Player Goals | Shape |
| 2 | Invariant format | Added Reason/Implication to AutonomousAgents | Identity |
| ... | ... | ... | ... |

### Human-Required Issues
| # | Category | Issue | Why Auto-Fix Cannot Resolve |
|---|----------|-------|----------------------------|
| 1 | Invariant violation | SYS-015 implies direct colonist commands | Design decision needed |
| 2 | Layer violation | Design doc contains signal registry details | Move to reference docs |
| ... | ... | ... | ... |
```

If no issues found:
```
## Design Fix

**Status: Clean** — no issues found. No changes made.
```

## Rules

- **Only fix mechanical, local issues.** Never make design decisions — those are human-required.
- **Only edit the design doc.** Never edit system designs, reference docs, glossary, engine docs, or downstream documents.
- **Derive fixes from context, don't invent.** Tightened wording comes from existing sections or other authoritative docs.
- **Preserve design doc structure.** Don't reorganize sections or merge groups.
- **Stop when stable.** If remaining issues are unchanged, stop iterating.
- **Governance mechanisms are format-checked, not content-judged.** This skill verifies invariants have the right format — it does not evaluate whether the invariant itself is a good rule.
- **Layer violations are always human-required.** If the design doc contains system-layer truth (ownership tables, signal registries, interface contracts, data schemas), flag it for removal but don't delete it — the user decides where it goes.
- **Design intent is sacred.** Auto-fixes may tighten wording but never change what the game delivers or how the player experiences it.
- **Design decision escalation.** If a downstream document introduces a player-facing mechanic, rule, resource, or interaction not described in the design doc, the change must be escalated to the design doc before implementation proceeds. Design defines the game; systems implement it.
