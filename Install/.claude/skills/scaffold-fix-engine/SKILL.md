---
name: scaffold-fix-engine
description: Mechanical cleanup pass for engine docs — auto-fix structural issues (template text, missing sections, terminology drift, stale markers), detect design signals (architecture contradictions, Step 3 alignment gaps, layer breaches) for adversarial review. Supports single doc or all. Individual fix loops run in parallel.
argument-hint: [--target doc-stem] [--iterate N]
allowed-tools: Read, Edit, Grep, Glob
---

# Fix Engine

Mechanical cleanup and signal detection for engine docs: **$ARGUMENTS**

This skill is the **formatter and linter** for engine docs — not the design reviewer. It normalizes structure, repairs mechanical inconsistencies, and detects signals where engine docs may contradict Step 3 architecture or reference docs. It does not interpret or resolve design issues — that is the job of `iterate-engine` (adversarial review) which runs immediately after this skill.

**What fix-engine does:** normalize docs so adversarial review doesn't waste time on trivial issues.
**What fix-engine does NOT do:** evaluate whether the engine approach is good, resolve architecture conflicts, or make design decisions.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--target` | No | all | Target a single doc by stem (e.g., `--target simulation-runtime`, `--target coding-best-practices`). When omitted, processes all engine docs. |
| `--iterate N` | No | `10` | Maximum review-fix passes. Stops early on convergence. |

## Parallelization

Individual fix loops are local to each engine doc — all docs can run their fix loops in parallel. The cross-doc pass (Step 5) runs after all individual loops complete.

## Step 1 — Gather Context

1. **Glob** `scaffold/engine/*` to find all engine docs.
2. If `--target` is set, filter to only the matching doc. If no match, stop.
3. For each engine doc, read the **canonical template** from `scaffold/templates/` — defines expected section structure.
4. Read upstream context (always, regardless of `--target`):
   - `design/architecture.md` — tick order, data flow rules, forbidden patterns, identity model, boot order, simulation update semantics
   - `design/authority.md` — ownership rules
   - `design/interfaces.md` — cross-system contracts, timing, realization paths
   - `design/state-transitions.md` — state machine timing
   - `reference/entity-components.md` — entity data shapes, persistence model
   - `reference/signal-registry.md` — signal dispatch timing, delivery expectations
   - `design/glossary.md` — canonical terminology
   - `scaffold/doc-authority.md` — document authority ranking, same-rank conflict resolution rules, deprecation protocol
   - `design/style-guide.md` — rendering approach (for UI, post-processing docs)
   - `scaffold/engine/_index.md` — registration
   - Accepted ADRs that reference engine docs
   - `decisions/known-issues.md`

## Step 2 — Per-Doc Checks

For each engine doc, run two categories of checks: **mechanical checks** (structure, formatting, registration) and **alignment signal detection** (Step 3 contradictions, layer breaches).

### Mechanical Checks

#### Header & Metadata Block
- **Status field exists and is valid** — blockquote header contains `> **Status:**` with a valid value (`Draft | Review | Approved | Complete | Deprecated`).
- **Required metadata fields present** — `Layer:`, `Authority:`, `Conforms to:`, and `Status:` exist in the header blockquote.
- **Title matches doc type** — the H1 title contains the correct engine name and doc-type label (e.g., `Godot 4 — Simulation Runtime`, not `[Engine] — Simulation Runtime`).
- **Engine prefix in title is correct** — title references the active engine, not a template placeholder or different engine.

#### Section Structure
- All sections from the canonical template are present.
- **Template mapping sanity** — doc contains all required sections from the expected template for its doc stem (e.g., `simulation-runtime` seeded from `engine-simulation-runtime-template.md`). Additional project-specific sections are allowed, but required template sections must not be missing or replaced. Flag docs whose required sections match the wrong template.
- **Duplicate section detection** — no repeated headings, repeated Rules sections, repeated Project Overrides tables, or repeated template scaffolding blocks. Duplicates can appear after multiple seed/fix passes. Auto-fixable if obviously redundant (identical content); user-confirmed if both copies have distinct authored content.
- `<!-- SEEDED -->` or `*TODO:*` markers on sections that now have authored content — marker should be removed.
- `<!-- Constrained: ... -->` markers are still accurate (the referenced Step 3 decision may now be resolved).

#### Terminology & Registration
- **Glossary compliance** — engine doc does not use NOT-column terms as authoritative technical terminology.
- **Index registration** — engine doc is listed in `scaffold/engine/_index.md`.
- **Engine prefix consistency** — all engine-prefixed docs use the same prefix. Exclude `implementation-patterns.md` and `_index.md` (these are not engine-prefixed by design).

#### Structural Quality
- **Purpose is present and scannable** — Purpose section exists with authored content, not buried in multi-paragraph prose.
- **Rules section exists and is meaningful** — every engine doc needs binding rules at the bottom. If the Rules section exists but contains only template filler or empty numbered list, flag as user-confirmed (section present but not useful).
- **Project Overrides table exists** — even if empty.
- **Template-default content** — section still contains scaffold instruction text (`<!-- Define... -->`), bracket prompts (`[Engine]`, `[describe...]`), example filler (`ExampleSystem`, `PlayerCharacter`, `TODO_SIGNAL_NAME`), or near-empty boilerplate with no project-specific content. A section can exist, have the right heading, have no TODO marker, and still be useless template sludge. Classify as user-confirmed pending, not auto-fixable.
- **Placeholder examples left unchanged** — template placeholder names (`ExampleSystem`, `SomeNode`, `TODO_SIGNAL_NAME`, `[prefix]-example`) still present in authored sections. Auto-fixable only if the surrounding content makes the correct replacement unambiguous; otherwise user-confirmed.
- **No authority-layer or intent-layer overrides** — engine docs may reference gameplay concepts (colonist, reservation, task, room, state transition) as implementation targets, but must not redefine player-facing intent, canonical ownership, contract semantics, state definitions, or other decisions owned by higher-ranked docs (Rank 1-8). Flag content that establishes new design authority rather than implementing existing authority.

#### Engine Identity & Stack
- **Engine identity drift in body text** — body content references a different engine than the active one (e.g., "In Unity…", "Use Blueprint…", "Unreal's GC…" in a Godot project). Catches copy-paste contamination from wrong-engine sources. Auto-fixable only if the correct engine term is unambiguous; otherwise user-confirmed.
- **Implementation stack consistency** — all engine docs assume the same implementation stack. Flag if one doc assumes GDScript-only while another assumes GDScript + C++ GDExtension, or if build docs reference C# project files in a GDScript project. Detected per-doc, reported as cross-doc signal if multiple docs disagree.

#### Upstream Anchor Drift
- **Stale upstream references** — section names, table terms, signal names, interface names, or canonical labels cited from Step 3 docs no longer match their upstream source. Auto-fixable when the old→new mapping is unambiguous.

#### Engine Internal Cross-References
- **Engine internal reference drift** — engine docs referencing other engine docs or sections by stale names (e.g., coding-best-practices references a simulation-runtime section that was renamed, build-and-test-workflow references an old performance-budget section title, debugging-and-observability references a doc stem that changed). Auto-fixable when the old→new mapping is unambiguous within the engine doc set.

#### File Inventory
- **Filename/stem validation** — only expected engine docs exist for the active prefix. The valid set is the 15 doc stems from `scaffold-bulk-seed-engine` plus `_index.md` and `implementation-patterns.md`. Flag unexpected extra prefixed files, malformed filenames, or files that don't match any known engine doc stem.

#### Index ↔ File Bidirectional Consistency
- **Missing docs in _index.md** — engine doc files exist on disk but aren't listed in the index. Auto-fixable: add registration.
- **Stale index rows** — _index.md lists docs that don't exist on disk. Auto-fixable: remove the row.
- **Duplicate index rows** — same doc listed more than once. Auto-fixable: remove duplicates.
- **Wrong descriptions** — _index.md description doesn't match the doc it points to (e.g., description for coding-best-practices on the row for simulation-runtime). Auto-fixable when the correct doc exists and has an authored Purpose.
- **Stale template descriptions** — _index.md descriptions are still template-default when the doc has authored content. Auto-fixable: update the description to reflect the doc's actual Purpose section.
- **Template-default _index.md** — if `_index.md` exists but its content is still scaffold template boilerplate (no authored descriptions, no real entries), flag as user-confirmed mechanical issue.
- **Stale prefix entries** — index contains entries from a different engine prefix unless intentionally preserved.
- **Wrong prefix in index rows** — index row references a doc with a different engine prefix than the active one.

#### ADR Supersession & Deprecation
- **Deprecation drift** — engine doc or section remains active after an accepted ADR superseded or deprecated it. If the ADR explicitly deprecates a doc or section, flag for status update. User-confirmed pending unless the supersession is explicit enough to auto-mark as Deprecated.
- **Active content contradicting accepted ADR** — engine doc describes a convention or pattern that an accepted ADR explicitly reversed. Auto-fixable when the ADR decision is unambiguous; otherwise flag as alignment signal.

#### Constrained TODO Currency
- **Unblocked sections** — if a `<!-- Constrained: depends on [X] -->` marker references a Step 3 decision that is now resolved (not TBD), flag for update. The section can now be promoted from Constrained TODO to authored content.
- **Stale TBDs** — if engine content was written but the TODO marker was left, flag for cleanup.
- **Stale constrained references** — if a `<!-- Constrained: depends on [X] -->` marker names a decision, section, or doc that no longer exists or was renamed upstream, flag as stale constrained reference. Auto-fixable if the rename mapping is unambiguous; otherwise report for human resolution.
- **Orphan constrained marker** — `<!-- Constrained -->` or `<!-- Constrained: ... -->` exists but does not clearly reference a real, traceable Step 3 decision. The marker is present but the dependency is vague or unnamed. User-confirmed — the section needs a concrete dependency or should be converted to an Open TODO.

### Alignment Signal Detection

These are **detected and reported**, not resolved. The adversarial review skill interprets them.

#### Architecture Alignment
- **Tick model contradiction** — engine simulation-runtime describes a different timing model than architecture.md Simulation Update Semantics.
- **Data flow violation** — engine doc describes a communication pattern that violates architecture.md Forbidden Patterns.
- **Identity model mismatch** — engine coding/save-load describes handle semantics that don't match architecture.md Entity Identity section.
- **Boot order mismatch** — engine scene-architecture describes initialization that conflicts with architecture.md Boot Order.

#### Authority/Contract Alignment
- **Ownership assumption** — engine doc assumes a system owns something that authority.md assigns differently.
- **Interface timing mismatch** — engine doc describes signal dispatch timing that conflicts with interfaces.md Timing column or signal-registry.md Dispatch Timing Conventions.
- **Contract realization mismatch** — engine doc describes a cross-system interaction pattern that doesn't match the realization path in interfaces.md.

#### Layer Boundary
- **Engine doc overriding higher-ranked authority** — engine doc redefines, constrains, or contradicts decisions owned by higher-ranked docs (Rank 1-8) — whether player-facing intent, canonical ownership, contract semantics, state definitions, or architectural rules — rather than implementing them. Includes both explicit redefinition and implicit constraint (a technical decision that effectively narrows a design decision without acknowledging it).

#### False Certainty
- **Unresolved dependency masked as certainty** — engine doc contains concrete implementation wording in a section that should still be constrained by unresolved Step 3 decisions. The `<!-- Constrained -->` marker may be missing or was never added.
- **Engine internal convention conflict** — one engine doc establishes a convention (naming, pattern, timing, error handling) that another engine doc violates.

## Step 3 — Classify Issues

### Auto-Fixable (apply immediately)

| Category | Fix | Condition |
|----------|-----|-----------|
| **Missing sections** | Add section heading with template content | Section required by template and genuinely absent |
| **Stale SEEDED/TODO markers** | Remove marker from sections with authored content | Section has substantive content beyond the marker |
| **Unblocked constrained section** | Remove stale `<!-- Constrained: depends on [X] -->` comment. Replace with plain `*TODO: [X] is now resolved — author this section*` if no draft content exists. Report as "now unblocked and ready for authoring." | Referenced Step 3 decision is no longer TBD. Does NOT invent content — only cleans the marker and flags for human authoring. |
| **Stale upstream naming** | Update old signal/interface/section/term names to current upstream canonical names | Mapping is unambiguous (old name → new name traceable in upstream doc) |
| **Terminology drift** | Replace NOT-column terms with canonical terms | Used as authoritative terminology, not in examples/quotes |
| **Registration gaps** | Add to `scaffold/engine/_index.md` | Engine doc missing from index |
| **Stale ADR reference** | Update to current ADR status | ADR status changed |
| **Missing Rules section** | Add Rules section heading from template | Doc has no Rules section |
| **Missing Project Overrides** | Add empty Project Overrides table from template | Doc has no overrides section |
| **Stale constrained reference** | Update `<!-- Constrained: depends on [X] -->` to use current upstream name | Referenced decision/section/doc was renamed and mapping is unambiguous |
| **Duplicate sections** | Remove obviously redundant duplicate (identical content) | Same heading appears twice with identical content after seed/fix pass |
| **Stale index rows** | Remove _index.md rows pointing to nonexistent files | File does not exist on disk |
| **Duplicate index rows** | Remove duplicate _index.md entries for the same doc | Same doc listed more than once |
| **Engine internal reference drift** | Update stale cross-references between engine docs | Old doc stem or section name → new name, mapping unambiguous |
| **Header metadata missing** | Add missing required blockquote fields from template | `Status:`, `Layer:`, `Authority:`, or `Conforms to:` absent |
| **Template placeholder in title** | Replace `[Engine]` with actual engine name in H1 title | Title still contains `[Engine]` placeholder |
| **ADR-reversed convention** | Update engine content to match accepted ADR decision | ADR explicitly reversed a convention and the mapping is unambiguous |

### Mechanically Detected, User-Confirmed

| Category | Action |
|----------|--------|
| **Template defaults remaining** | Section still at template/default level. Report for human completion. |
| **Template-default content** | Section exists with correct heading and no TODO marker, but body is scaffold filler (`<!-- Define... -->`, bracket prompts, example placeholders, near-empty boilerplate). Not the same as "missing" — the heading is present but the content is useless. |
| **Placeholder examples** | Template placeholder names (`ExampleSystem`, `SomeNode`, `TODO_SIGNAL_NAME`, `[prefix]-example`) survive in authored sections. Report unless replacement is unambiguous. |
| **Section exists but unauthored after fix** | Fix pass added a missing section from template — section now exists but is an empty shell. Report explicitly so the summary reflects true authoring state. |
| **Design content in engine doc** | Flag content that reads like design-layer intent. User decides whether to move it or keep it. |
| **Engine prefix mismatch** | Flag if one doc uses a different prefix than the rest. |
| **Template-default _index.md** | Engine index exists but has no authored descriptions or real entries — still scaffold boilerplate. |
| **Engine identity drift** | Body text references a different engine than the active one (e.g., Unity terms in a Godot project). Report unless auto-fix replacement is unambiguous. |
| **Unexpected files in engine dir** | Files in `scaffold/engine/` that don't match any known engine doc stem for the active prefix. |
| **Duplicate sections with distinct content** | Same heading appears twice with different authored content. User must decide which to keep. |
| **Deprecation drift** | Engine doc or section still active after an accepted ADR superseded or deprecated it. |
| **Orphan constrained marker** | Constrained TODO exists but does not name a traceable Step 3 decision. Needs concrete dependency or conversion to Open TODO. |
| **Empty Rules section** | Rules section exists but contains only template filler or empty numbered list — not meaningful. |

### Alignment Signals (for adversarial review)

Tag each signal with a severity to help iterate-engine prioritize:

| Signal | Context | Severity |
|--------|---------|----------|
| Tick model contradiction | simulation-runtime timing ≠ architecture.md | **HIGH** (correctness-breaking) |
| Data flow violation | Engine doc describes forbidden pattern | **HIGH** (correctness-breaking) |
| Ownership assumption | Engine doc assumes ownership ≠ authority.md | **HIGH** (correctness-breaking) |
| Contract realization mismatch | Interaction pattern ≠ interfaces.md realization path | **HIGH** (correctness-breaking) |
| Identity model mismatch | Handle semantics ≠ architecture.md | **HIGH** (correctness-breaking) |
| Layer breach | Engine doc redefines, constrains, or contradicts higher-ranked authority (Rank 1-8) | **HIGH** (correctness-breaking) |
| Boot order mismatch | Init sequence ≠ architecture.md | **MEDIUM** (architectural risk) |
| Interface timing mismatch | Signal timing ≠ interfaces.md/signal-registry | **MEDIUM** (architectural risk) |
| Unresolved dependency masked as certainty | Concrete wording where Constrained TODO should be | **MEDIUM** (architectural risk) |
| Engine internal convention conflict | One engine doc's convention contradicts another's | **MEDIUM** (architectural risk) |
| Stack assumption inconsistency | Engine docs assume different implementation stacks | **MEDIUM** (architectural risk) |
| Maturity imbalance | Simulation-critical docs mostly TODO while general docs populated | **LOW** (completeness/quality) |
| Architecture coverage gap | Architecture decision not addressed by any engine doc | **LOW** (completeness/quality) |
| Constrained TODO clustering | Multiple docs blocked on same unresolved Step 3 decision | **LOW** (completeness/quality) |

## Step 4 — Apply Auto-Fixes

For each auto-fixable issue:
1. Apply the fix to the engine doc using Edit.
2. Record what was changed and why.

**Safety rules:**
- **Never silently resolve substantive architecture contradictions.** If an engine doc contradicts Step 3 and the mismatch appears intentional, architectural, or judgment-heavy, flag it as an alignment signal. If the mismatch is clearly stale mechanical drift from a locked higher-ranked decision (stale terminology, outdated timing wording, stale ownership assumption, outdated signal name), auto-fix the engine doc to conform.
- **Never add new engine constraints.** Only clarify or restructure what's already there.
- **Never infer missing implementation decisions.** When multiple plausible approaches exist, report instead of auto-fixing.
- **Never edit upstream docs.** Don't edit architecture.md, authority.md, interfaces.md, system designs, or any Rank 1-8 docs.
- **No speculative fixes.** If resolving an issue requires guessing the intended implementation approach, report instead.
- **When `--target` is set, only edit the targeted doc.** Flag cross-doc implications.

## Step 5 — Cross-Doc Pass

After all individual engine docs have been fixed, run one cross-doc pass:

- **Consistency across engine docs** — do all engine docs agree on fundamental conventions? (e.g., does coding-best-practices describe a signal pattern that scene-architecture contradicts?)
- **Architecture alignment coverage** — for each architecture.md decision (tick model, identity, data flow, boot order), verify at least one engine doc addresses it. Flag gaps.
- **Simulation-specific doc maturity** — are simulation-runtime, save-load, and ai-task-execution still mostly TODO while engine-general docs are populated? Flag as maturity imbalance.
- **Constrained TODO clustering** — are multiple docs waiting on the same unresolved Step 3 decision? Flag the blocking decision.
- **Implementation stack contradiction** — do engine docs assume different stacks? (e.g., coding doc says GDScript + C++, performance doc assumes GDScript-only, build doc references C# project files). Not just a convention conflict — a fundamental stack disagreement.
- **Engine identity contamination** — do any engine docs reference a different engine in body text? (e.g., Unity/Unreal terms in a Godot project). Catches copy-paste drift across the doc set.

Cross-doc pass results are reported as signals, not auto-fixed.

## Step 6 — Re-review and Iterate

After applying fixes, re-review. Continue iterating until:
- **Clean** — no issues remain.
- **Human-only** — only human-required issues and alignment signals remain.
- **Stable** — same issues persist across two consecutive passes.
- **Limit** — `--iterate N` reached.

## Step 7 — Report

For a single doc:
```
## Fix-Engine Summary: [doc-stem]

| Metric | Value |
|--------|-------|
| Passes | N |
| Auto-fixed | N issues |
| User-confirmed pending | N issues |
| Alignment signals | N issues |
| Unblocked sections | N (formerly constrained by Step 3, now ready for authoring) |
| Final status | Clean / Human-only / Stable / Limit |

### Auto-Fixes Applied
| # | Category | What Changed |
|---|----------|-------------|
| 1 | Stale TODO | Removed TODO marker from Purpose (now authored) |
| 2 | Terminology | Replaced "worker" with "colonist" |
| ... | ... | ... |

### User-Confirmed Actions Pending
| # | Category | Action Required |
|---|----------|----------------|
| 1 | Template defaults | Queued Work Draining section needs authored content |
| ... | ... | ... |

### Alignment Signals (for iterate-engine)
| # | Signal | Detail |
|---|--------|--------|
| 1 | Tick model contradiction | simulation-runtime says variable step, architecture.md says fixed |
| 2 | Interface timing mismatch | Signal dispatch described as immediate, but signal-registry says queued |
| ... | ... | ... |
```

For all docs:
```
### Engine Doc Summary
| Doc | Auto-fixed | User-pending | Signals | Unblocked Sections | Status |
|-----|-----------|-------------|---------|---------------------|--------|
| coding-best-practices | 3 | 1 | 0 | 0 | Clean |
| simulation-runtime | 1 | 4 | 2 | 1 | Human-only |
| ... | ... | ... | ... | ... | ... |

### Cross-Doc Signals
| # | Signal | Docs Involved | Detail |
|---|--------|--------------|--------|
| 1 | Convention conflict | coding, scene-architecture | Signal wiring pattern differs |
| 2 | Maturity imbalance | simulation-runtime, save-load | Mostly TODO while general docs are populated |
| 3 | Blocking constraint | simulation-runtime, ai-task | Both waiting on architecture.md timing resolution |
| ... | ... | ... | ... |
```

## Rules

- **This skill is a formatter and linter, not a design reviewer.** It normalizes docs and detects signals. Design evaluation belongs to iterate-engine.
- **No authority-layer or intent-layer overrides.** Engine docs may reference gameplay concepts as implementation targets, but must not redefine player-facing intent, canonical ownership, contract semantics, or state definitions owned by higher-ranked docs.
- **Never silently resolve substantive architecture contradictions.** If an engine doc conflicts with Step 3 in a way that appears intentional, architectural, or judgment-heavy, flag it as a signal. If the mismatch is clearly stale mechanical drift from a locked higher-ranked decision, auto-fix it. The contradiction may be in either direction — don't assume the engine doc is wrong.
- **Never infer missing implementation decisions.** When multiple plausible approaches exist, report — do not auto-fix.
- **No speculative fixes.** If resolving an issue requires guessing the intended approach, report instead.
- **Alignment signals are detected, not resolved.** Architecture, authority, and contract alignment signals are reported for iterate-engine — not acted on by this skill.
- **Terminology fixes respect context.** Only replace NOT-column terms when used as authoritative terminology.
- **Constrained TODO resolution is a promotion, not an invention.** When a constraint is resolved, the skill flags the section for authoring — it does not invent the content.
- **All individual fix loops run in parallel.** Cross-doc signals are caught in the post-loop cross-doc pass.
- **Cross-doc pass results are signals, not fixes.** Nothing in Step 5 is auto-applied.
