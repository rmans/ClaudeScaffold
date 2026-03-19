---
name: scaffold-fix-foundation
description: Review-fix loop for foundation architecture docs — auto-fix mechanical issues (template text, missing sections, authority conflicts, interface gaps, inconsistent ownership), surface architectural decisions for human resolution. Operates on architecture.md, authority.md, interfaces.md, and reference docs.
argument-hint: [--iterate N] [--mode initial|recheck]
allowed-tools: Read, Edit, Grep, Glob
---

# Fix Foundation

Iteratively review and auto-fix mechanical issues in foundation architecture documents: **$ARGUMENTS**

Reviews `design/architecture.md`, `design/authority.md`, `design/interfaces.md`, and reference docs for mechanical inconsistencies across the 6 foundation areas. Classifies issues as auto-fixable or human-required, applies safe fixes, and re-reviews until clean.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--iterate N` | No | `10` | Maximum review-fix passes before stopping. Stops early on convergence — if a pass produces no new issues, iteration ends. |
| `--mode` | No | `initial` | `initial` for pre-planning gate, `recheck` for post-implementation. Recheck mode focuses on areas where ADRs/KIs suggest drift. |

## Step 1 — Read Context

1. Read `scaffold/design/architecture.md`.
2. Read `scaffold/design/authority.md`.
3. Read `scaffold/design/interfaces.md`.
4. Read `scaffold/design/state-transitions.md`.
5. Read `scaffold/reference/entity-components.md`.
6. Read `scaffold/reference/signal-registry.md`.
7. Read `scaffold/design/systems/_index.md` and skim system files for ownership/dependency claims.
8. Read all ADRs with status `Accepted`.
9. Read `scaffold/decisions/known-issues.md`.
10. Read `scaffold/engine/godot4-coding.md` (or equivalent) for engine-level constraints.
11. Read `scaffold/design/glossary.md` for canonical terminology.
12. Read `scaffold/doc-authority.md` for document authority ranking, same-rank conflict resolution rules, deprecation protocol.

In `--mode recheck`, also read:
- Triage logs from completed slices/phases
- Revision logs from revise-phases/revise-roadmap
- Prototype findings

## Step 2 — Review

Check each foundation area for mechanical issues:

| Foundation Area | What to check |
|----------------|---------------|
| Identity / handle model | Handle type defined in architecture.md? Destroy/reuse semantics documented? Entity-components.md handle column consistent? |
| Content-definition model | Enum vs registry boundary documented? ID/namespacing policy explicit? |
| Entity / storage model | Storage approach documented? Iteration/reuse rules explicit? Stale-reference policy defined? |
| Save/load architecture | Schema philosophy documented? Validation pipeline described? Versioning/migration policy explicit? |
| Map / spatial model | Dimensions documented? Tile indexing convention explicit? Layer rules defined? |
| Core API boundary rules | Tick ordering documented? Ownership rules in authority.md match architecture.md? Interface contracts align? |

Additionally check:
- **Cross-doc consistency** — authority.md ownership matches system design claims.
- **Interface completeness** — systems that interact have contracts in interfaces.md.
- **Signal consistency** — signals referenced in architecture.md exist in signal-registry.md.
- **Terminology compliance** — glossary canonical terms used throughout.
- **Template text** — no TODOs or placeholder content in foundation sections.

## Step 3 — Classify Issues

### Auto-Fixable

| Category | Example |
|----------|---------|
| **Template text / TODOs** | Architecture.md foundation section still has placeholder → replace with content derived from system designs |
| **Terminology drift** | Uses NOT-column glossary term → replace with canonical term |
| **Missing known-issue entry** | Foundation area is Partial but not tracked in known-issues.md → add entry |
| **Authority-architecture mismatch** | Authority.md says system A owns variable X, architecture.md says system B → auto-fix only when one doc clearly derives from the other. Otherwise human-required. |
| **Missing interface contract** | Two systems interact per architecture.md but no contract in interfaces.md → add stub contract. Content is human-required. |
| **Signal registry gap** | Signal referenced in architecture.md not in registry → add stub entry |
| **Stale ADR reference** | Architecture.md references deprecated ADR → update reference |

### Human-Required

| Category | Why |
|----------|-----|
| **Foundation area Undefined** | Requires architectural decision — cannot be inferred |
| **Ownership conflict** | Multiple systems claim the same data — design decision |
| **Storage model choice** | ECS vs arrays vs pools — engineering decision with broad downstream impact |
| **Save/load philosophy** | Schema approach, validation pipeline — affects all persistence |
| **Handle model design** | Identity semantics affect every system — cannot auto-resolve |
| **API boundary dispute** | Who owns what, who queries what — authority decision |
| **ADR contradicts architecture** | Accepted ADR changes a foundation assumption — scope decision |
| **Engine constraint conflict** | Engine limitation affects a foundation decision — viability decision |

Present human-required issues using the Human Decision Presentation pattern (see WORKFLOW.md).

## Step 4 — Apply Auto-Fixes

**Fix rules:**
- **Edit only architecture docs and reference docs.** Never edit system designs, phase files, or engine docs.
- Fixes must be minimal — change only what's needed.
- Derive fixes from existing document content, not invented.
- Never change a foundation decision — only fix how clearly it's expressed or how consistently it's reflected across docs.
- Authority.md is canonical for ownership. Architecture.md is canonical for cross-cutting rules.

## Step 5 — Re-Review and Iterate

Same stop conditions as other fix skills:
- **Clean** — no issues found.
- **Human-only** — only human-required issues remain.
- **Stable** — remaining issue set unchanged from previous pass.
- **Limit** — iteration limit reached.

## Step 6 — Output

```
## Foundation Fix [initial / recheck]

### Summary
| Field | Value |
|-------|-------|
| Mode | initial / recheck |
| Foundation areas checked | 6 |
| Passes | N completed / M max [early stop: yes/no] |
| Auto-fixed | N issues |
| Human-required | N issues |
| Final status | Clean / Needs human input |

### Foundation Area Status
| Area | Status | Issues |
|------|--------|--------|
| Identity / handle model | Locked / Partial / Undefined | N |
| Content-definition model | Locked / Partial / Undefined | N |
| Entity / storage model | Locked / Partial / Undefined | N |
| Save/load architecture | Locked / Partial / Undefined | N |
| Map / spatial model | Locked / Partial / Undefined | N |
| Core API boundary rules | Locked / Partial / Undefined | N |

### Fixes Applied
| # | Category | What Changed | Document |
|---|----------|-------------|----------|
| 1 | Template text | Replaced TODO in identity section | architecture.md |
| ... | ... | ... | ... |

### Human-Required Issues
| # | Category | Issue | Why Auto-Fix Cannot Resolve |
|---|----------|-------|----------------------------|
| 1 | Storage model choice | ECS vs slot arrays undecided | Engineering decision with broad impact |
| ... | ... | ... | ... |
```

## Rules

- **Only fix mechanical, local issues.** Never make architectural decisions.
- **Architecture.md is canonical for cross-cutting rules.** Authority.md is canonical for ownership.
- **Human decisions drive foundation choices.** This skill surfaces options; the user decides.
- **Derive fixes from context, don't invent.** Consistency fixes come from existing doc content.
- **Stop when stable.** If remaining issues are unchanged, stop iterating.
- **In recheck mode, focus on drift areas.** Don't re-audit stable areas unless evidence suggests drift.
