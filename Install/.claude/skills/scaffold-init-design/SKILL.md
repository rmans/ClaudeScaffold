---
name: scaffold-init-design
description: Initialize or update the design document. Ingests existing canon, detects gaps and contradictions, pre-fills what can be inferred, and only interviews for true missing decisions. Supports seed, fill-gaps, reconcile, and refresh modes.
argument-hint: [--mode seed|fill-gaps|reconcile|refresh] [--sections "Identity,Shape"]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Initialize Design

Initialize or update `design/design-doc.md`: **$ARGUMENTS**

This is not a blank-start questionnaire. It ingests existing project material, detects what's already decided, finds contradictions, and only asks about genuine gaps.

The design doc is the highest authority for **game intent, player experience, and non-breakable design rules**. It is not the sole container for system, reference, style, input, or engine truth. This skill captures only the design-facing truths those later docs must obey.

## Modes

| Mode | When to use | What it does |
|------|------------|-------------|
| `seed` | First time, or design doc is at template defaults | Reads existing project docs, pre-fills what can be inferred, interviews for the rest |
| `fill-gaps` | Design doc exists but has incomplete sections | Classifies each section, only asks about Missing/Partial ones |
| `reconcile` | After implementation drift or ADR changes | Detects contradictions between the design doc and other docs, resolves them |
| `refresh` | Vision has evolved, specific sections need rethinking | Re-interviews selected sections, preserving everything else |

Default mode is `seed` if the design doc is at template defaults, `fill-gaps` otherwise.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--mode` | No | auto-detect | `seed`, `fill-gaps`, `reconcile`, or `refresh` |
| `--sections` | No | all | Comma-separated section groups to focus on (e.g., `"Identity,Shape,World"`) |

## Step 1 — Read Existing Canon

Read these sources in authority order:

1. **`scaffold/doc-authority.md`** — document authority ranking, same-rank conflict resolution rules, influence map.
2. **`design/design-doc.md`** — the primary target and current canon for game intent, player experience, and design rules. Existing content remains canon unless the user explicitly refreshes it, or an accepted ADR explicitly supersedes that design decision.
3. **Other design-layer docs** — `design/systems/_index.md`, `design/architecture.md`, `design/authority.md`, `design/glossary.md` (if they exist). These may contain decisions that reveal missing or implied design intent. Do not pull detailed system ownership, interface contracts, reference tables, input bindings, or engine implementation rules upward into the design doc unless they materially affect player-facing intent or a design invariant.
4. **ADRs** — accepted ADRs may override design doc assumptions.
5. **Known issues / design debt** — constraints that affect design decisions.
6. **Engine docs** — platform and technical constraints that bound design choices.

**Do not front-load theory docs.** Read theory docs only when relevant to a specific section being discussed.

**Source precedence:**
- Design doc = highest authority for game intent (being written/updated)
- Accepted ADRs = override design doc **only when the ADR explicitly supersedes a design decision** (technical ADRs do not override game design)
- Other design-layer docs = source material (may pre-fill sections)
- Engine docs = technical constraints that bound design choices
- Theory docs = advisory only (never override canon)
- User answers in this session = newest override, but only for the section being discussed

**Design lock rule:** Sections classified as Complete are treated as locked canon. Downstream docs (systems, specs, slices, tasks) must conform to locked design sections. To change a locked section, use `--mode refresh` with explicit `--sections` targeting.

## Step 2 — Classify Sections

For each design doc section, classify as:

| Status | Meaning | Skill behavior |
|--------|---------|---------------|
| **Complete** | Section has substantive content that aligns with other docs | Skip — locked canon, do not re-interview |
| **Derived** | Section can be inferred with high confidence from existing docs | Pre-fill candidate — stage for user confirmation |
| **Partial** | Section has content but is incomplete, vague, or underspecified | Ask focused follow-up questions only about the gaps |
| **Conflicted** | Section content contradicts another doc or accepted ADR | Surface the contradiction and resolve before proceeding |
| **Missing** | Section is empty, template defaults, or TODO placeholders | Interview from scratch |

**Contradiction triggers:** Conflicts occur when two authoritative docs describe mutually exclusive mechanics, control models, progression structures, world rules, or platform commitments. Examples: direct control vs indirect control, procedural world vs authored campaign, closed economy vs player-driven economy.

Report the classification:

```
## Design Doc Section Status

| Section Group | Section | Status | Notes |
|--------------|---------|--------|-------|
| Identity | Core Fantasy | Complete | Matches existing docs |
| Identity | Elevator Pitch | Partial | Exists but vague |
| Shape | Core Loop | Conflicted | ADR-017 changes WorkAI model |
| World | Tone | Missing | Template default |
| ... | ... | ... | ... |

**Complete:** N | **Derived:** N | **Partial:** N | **Conflicted:** N | **Missing:** N
```

In `fill-gaps` mode, only proceed with Partial/Conflicted/Missing sections.
In `reconcile` mode, only proceed with Conflicted sections.
In `refresh` mode, only proceed with sections specified in `--sections`.

## Step 3 — Pre-Fill from Existing Sources

For sections classified as Missing or Derived, attempt to infer content from existing docs before asking the user.

**Safe to pre-fill into design doc** (player-facing intent):
- Core fantasy, control model, player-facing loop structure
- Camera/presentation intent, scope/platform commitments
- Design invariants, player information assumptions
- Major mechanic categories, high-level content structure
- Philosophy/guardrail sections

**Not safe to pre-fill** (belongs in later-step docs):
- Owned variables, system authority mappings, emitted/consumed signals
- Interface shapes, save/load rules, storage models
- Input bindings, engine implementation patterns
- Glossary details (unless the term is player-facing or design-defining)
- Reference-layer IDs, data schemas, registry keys

For each pre-fill, note the source:

```
Pre-filled "Core Fantasy" from architecture.md (AI Core indirect control model).
Confirm or revise?
```

**Pre-fill rules:**
- Only pre-fill when the source is unambiguous and from an authoritative doc
- Stage all pre-fills for user confirmation before writing — never silently write inferred content as canon

Present staged pre-fills as a confirmation block:

```
## Proposed Pre-Fills

| Section | Proposed Content | Source | Status |
|---------|-----------------|--------|--------|
| Identity.CoreFantasy | Player is an AI managing a research colony | architecture.md | Derived |
| Presentation.Camera | Top-down management view | system docs consensus | Derived |

Confirm all / revise specific items / reject?
```

Only after confirmation should writing occur.

**Design drift detection (reconcile mode):** When system docs or specs imply mechanics that contradict design doc sections, flag as drift rather than silently accepting. Example: design doc says "colonists are autonomous" but system docs define `MoveColonist` commands. This is a drift signal, not an implementation detail.

## Step 4 — Interview for Gaps

For sections that remain Missing after pre-fill attempts, and for Partial sections, interview the user. Derived sections that were confirmed in Step 3 do not require interviews unless the confirmation introduced ambiguity or revealed missing detail.

**Interview rules:**
- Ask one section at a time for foundational/ambiguous sections (Core Fantasy, Core Loop, Control Philosophy)
- Batch related sections when they're clearly linked (Place + Time + Tone, Accessibility + Platforms + Performance)
- For Partial sections, show existing content first, then ask what's missing
- For Conflicted sections, present both sides and ask the user to resolve

**Write rules:**
- **Clear answers:** write into the design doc immediately
- **Fuzzy / thinking-out-loud answers:** write as provisional wording marked `<!-- PROVISIONAL: [reason] -->` — the user or fix-design will clean these up
- **Contradictions:** do not write until the user explicitly resolves the conflict
- **Answers that imply downstream changes:** write the answer, note the downstream impact as a comment

**Question style:**
- Instead of generic "What is the camera?", ask informed questions:
  "I found a strong AI-Core top-down colony-control direction in the existing docs. Is that still canon, or are you changing it?"
- Reference existing material when asking — the user shouldn't re-explain things that are already documented

## Step 5 — Resolve Contradictions

If any Conflicted sections were found:

1. Present the contradiction clearly: "Design doc says X. ADR-### says Y. Which is canon?"
2. Wait for the user's decision
3. Update the design doc to match the decision
4. If the other doc needs updating, note it as an action item (don't edit it — that's not this skill's job)

## Step 6 — Report

```
## Design Initialization: [mode]

### Design Health: N%
| Status | Count | Sections |
|--------|-------|----------|
| Complete (locked) | N | [list] |
| Derived (confirmed) | N | [list with sources] |
| Interviewed | N | [list] |
| Contradictions resolved | N | [list] |
| Still missing | N | [list] |
| Provisional | N | [list — needs user review] |

### Contradictions Found
| Section | Design Doc Says | Other Doc Says | Resolution |
|---------|----------------|---------------|------------|
| Core Loop | [X] | ADR-### says [Y] | User chose [Y] |

### Assumptions Made
[Any inferences or pre-fills that the user confirmed but should be aware of.]

### Downstream Impacts
[Actions needed in other docs based on design decisions made in this session.]

### Next Steps
- Run `/scaffold-review-design` to audit completeness
- Run `/scaffold-iterate design/design-doc.md` for adversarial review
- Proceed to Step 2 (Visual & UX Definition) when review passes
```

## Design Doc Sections

Organized into groups for interview batching:

| Group | Sections |
|-------|----------|
| **Identity** | Core Fantasy, **Design Invariants**, Elevator Pitch, Core Pillars, **Core Design Tension**, Unique Selling Points |
| **Shape** | Core Loop, Secondary Loops, Session Shape, Progression Arc, **Player Goals** (short/mid/long-term), **Decision Types**, **Decision Density** |
| **Control** | **Player Control Model** (direct/indirect/none), Control Philosophy, Player Verbs, **Player Mental Model**, Feedback Loops |
| **World** | Place & Time, Tone, Narrative Wrapper, Factions/Forces |
| **Presentation** | Camera, Aesthetic Pillars, Audio Direction, **Player Information Model** (visible/partial/hidden) |
| **Content** | Content Structure, Content Categories, Procedural vs Authored, **Replayability Model** |
| **System Domains** | **Major System Domains** (high-level, not full ownership map), Major Mechanics, **System Interaction Philosophy**, **Simulation Depth Target** |
| **Philosophy** | **Failure Philosophy** (traceable causes), **Risk/Reward Philosophy**, **Simulation Transparency Policy** (how understandable is the sim?), **Information Clarity Principle** (can the player understand consequences before acting?), **Decision Anchors** (3–5 tie-breaker rules: "X over Y"), **Design Pressure Tests** (3–6 stress scenarios that validate the design), **Design Gravity** (3–4 directions the game deepens over time), **Design Boundaries** (what this game is NOT), **Learning Curve Strategy** |
| **Scope** | Scope Reality Check, Target Platforms, Accessibility Goals, Performance Targets |

**Design Invariants** are the most critical addition. Each invariant follows a consistent format for downstream referencing:

```
Invariant: <ShortName>
Rule: <single sentence non-breakable rule>
Reason: <why this rule exists>
Implication: <high-level design impact>
```

Downstream docs cite them using `Invariant: <ShortName>` when justifying mechanics or constraints. If a feature breaks an invariant, the feature is wrong.

**Decision Anchors** are kept to 3–5 rules to remain actionable. They express preferred tradeoffs ("X over Y") and resolve ambiguous design choices without debate.

**Design Pressure Tests** follow a consistent format:

```
Pressure Test: <name>
Scenario: <extreme condition applied to the game>
Expectation: <what must remain true if the design is correct>
Failure Signal: <what indicates the design is breaking>
```

Keep to 3–6 tests that stress the core design philosophy.

**Design Gravity** defines 3–4 directions the game should deepen over time. Core Pillars define what the game fundamentally *is*. Design Gravity defines the direction the game should deepen as it *evolves*. Pillars = identity. Gravity = evolution.

## Rules

- **Ingest before interviewing.** Never ask a question whose answer already exists in the project.
- **Show your work on pre-fills.** Always cite the source doc when pre-filling a section.
- **Contradictions block writes.** Do not write content that contradicts an accepted ADR or higher-authority doc until the user resolves it.
- **Provisional wording is explicitly marked.** Fuzzy answers get `<!-- PROVISIONAL -->` comments, not silent canon status.
- **Design doc is the target, not the source.** This skill writes into design-doc.md. It reads from other docs but never edits them.
- **Theory docs are advisory.** Read them when relevant to a section, but never pre-fill from them or treat them as authority.
- **Use the user's voice.** Capture intent faithfully — don't rewrite their vision into generic project-management language.
- **Phases should be outcome-oriented** if the user discusses phases during design. "Prove the core loop works" not "implement 5 systems."
- **Do not upscope into later-step truth.** If a discovered fact belongs primarily to systems, references, inputs, style, engine, or foundation architecture, record only the design-facing implication in the design doc and leave full detail to the appropriate later-step document.
- **Constraint conflicts are not silent rewrites.** If engine or technical docs conflict with desired design intent, preserve the design intent here, flag the feasibility issue, and defer resolution to Step 6 or Step 7.
- **Invariant violations escalate.** Any pre-fill, derived assumption, or downstream implication that violates a Design Invariant must be surfaced as a contradiction/drift issue, not written as normal content.
- **Design drift signals must not be silently reconciled.** When downstream docs (systems, specs, slices) imply mechanics that violate a Design Invariant, Decision Anchor, or Pressure Test, the issue must be surfaced as drift and resolved by the user or through reconcile mode.
- **Design decision escalation.** If a downstream document introduces a new player-facing mechanic, rule, resource, or interaction not already described in the design doc, the change must be escalated to the design doc before implementation proceeds. Design defines the game; systems implement the game — not the reverse.
- **Content sections define player-facing categories only.** Detailed schemas, IDs, registries, and reference tables belong in later-step docs.
- **Created documents start with Status: Draft.**
