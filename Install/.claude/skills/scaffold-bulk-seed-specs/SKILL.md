---
name: scaffold-bulk-seed-specs
description: Read slices, system designs, and state transitions to bulk-create behavior spec stubs. Slice goals drive candidate selection; system designs flesh out behavior. Use after slices are defined.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Specs from Slices

Read all slices, system designs, and state transitions to bulk-create behavior spec stubs. Slice goals are the primary driver — system designs and state transitions flesh out behavior, but only for what the slice needs to prove.

## Prerequisites

1. **Read `scaffold/slices/_index.md`** to get the list of registered slices.
2. **Read every slice file** in `scaffold/slices/` (Glob `scaffold/slices/SLICE-*.md`).
3. **Read the systems index** at `scaffold/design/systems/_index.md`.
4. **Read every system design** in `scaffold/design/systems/`.
5. **Read state transitions** at `scaffold/design/state-transitions.md`.
6. **Read interfaces** at `scaffold/design/interfaces.md` for cross-system contracts.
7. **Read authority** at `scaffold/design/authority.md` for data ownership boundaries.
8. **Read doc-authority** at `scaffold/doc-authority.md` for the document authority ranking and influence map — understand which documents inform specs and how.
9. **Read entity-components** at `scaffold/reference/entity-components.md` — entity data shapes that specs can reference.
10. **Read signal-registry** at `scaffold/reference/signal-registry.md` — signals that specs can trigger or consume.
11. **Read balance-params** at `scaffold/reference/balance-params.md` — tunable parameters that specs can reference.
12. **Read resource-definitions** at `scaffold/reference/resource-definitions.md` — resources that specs may involve.
13. **Read the spec template** at `scaffold/templates/spec-template.md`.
14. **Read the specs index** at `scaffold/specs/_index.md` to find the next available ID and check existing specs.
15. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md` — ADRs may have changed system behavior.
16. **Read known issues** at `scaffold/decisions/known-issues.md` — known issues often represent missing behaviors, edge cases, or constraints that specs must account for.
17. **If fewer than 1 slice is defined**, stop and tell the user to create slices first.

## Phase 1 — Derive Behavior Candidates from Slice Goals

For each slice, the **slice goal** is the primary driver. System designs are supporting evidence, not the starting point.

### 1a. Identify what the slice must prove

Read the slice's Goal, Scope, "Systems Covered" sections, and `> **Depends on:**` field. If the slice depends on earlier slices, read those dependency slices to understand what behaviors are already proven — specs should not re-prove what dependency slices already cover, but may build on those proven behaviors as preconditions.

Answer:
- What end-to-end behaviors must this slice demonstrate?
- What must the player be able to do and observe by the end of this slice?
- What cross-system interactions does the slice need to prove work together?

### 1b. Decompose into behavior candidates

For each end-to-end behavior the slice must prove:
1. Use **Player Actions** from the relevant system designs to identify the concrete player-visible steps.
2. Use **System Resolution** sections to understand causal behavior and observable consequences. Do not copy internal implementation detail into the spec — extract only what the player or a test can observe.
3. Use **state transitions** to identify entry/exit conditions where relevant to the slice.
4. Use **Edge Cases** from system designs, but only those relevant to the slice's proof goal.

**Do not seed specs for system behaviors unrelated to the slice's proof goal.** A system may have 10 Player Actions, but if the slice only needs 3 of them, only those 3 generate spec candidates.

### 1c. Cluster related behaviors

Before splitting into atomic specs, group related behaviors into clusters:

- A single player action may produce one spec or several, depending on complexity.
- Example: "Place wall" might cluster into: valid placement, invalid placement rejection, resource consumption, room recalculation trigger. Each cluster member may become its own atomic spec.
- Some behaviors are tightly coupled and belong in one spec. Others are distinct and should be separate.

Present clusters to the user before splitting into atomic spec units.

### 1d. Split clusters into atomic spec units

For each cluster, produce atomic spec candidates. An atomic spec has:
- One testable behavior with a clear pass/fail outcome.
- Preconditions that can be set up independently.
- Acceptance criteria that can be verified without testing other specs.
- **Atomicity test:** A spec is atomic when it can fail for one primary reason and be validated independently of unrelated behavior branches. If a spec contains multiple distinct rejection paths, lifecycle stages, or player intents, consider splitting it. Example: "Construction lifecycle" is too broad — split into placement validation, job creation, work progress, completion, cancellation.

If a cluster can't be split cleanly, it's probably one atomic spec. Don't force splitting.

### 1e. Identify cross-system behaviors

Some spec candidates span multiple systems. For each:
- Assign the **primary owning system** (the system whose Player Action initiates the behavior).
- Note **secondary systems** that participate (consume signals, react to state changes, update their own data).
- Flag the spec as **cross-system** in the draft so downstream review checks authority compliance.

Cross-reference `scaffold/design/interfaces.md` for defined contracts and `scaffold/design/authority.md` for data ownership boundaries.

### 1f. Draft each spec candidate

For each atomic spec candidate, draft:
- **Summary** — one sentence describing the behavior from the player's perspective.
- **Proof Intent** — what this spec proves within its parent slice.
- **Trigger** — the initiating player action or system event.
- **Preconditions** — verifiable conditions that must be true before the behavior can occur.
- **Behavior** — numbered steps of player-visible actions with observable outcomes.
- **Observable Outcome** — what can be seen when the behavior succeeds.
- **Failure Outcome** — expected visible behavior when the action is rejected or fails.
- **Postconditions** — the world state after behavior completes.
- **Edge Cases** — boundary conditions, error states, and interactions with other systems.
- **Secondary Effects** — cross-system propagation triggered by this behavior, or "None."
- **Acceptance Criteria** — testable pass/fail checks derived from behavior steps.
- **Asset Requirements** — scan existing `assets/` directories for assets that match the spec's visual and audio needs (derived from Behavior, Observable Outcome, Failure Outcome sections). For each visual or audio element implied by the behavior, add a row: Requirement, Type, Description, Source Section, Satisfied By (existing asset path if reusable, or "—"), Status (Ready if reusable, Needed if must be produced). If no assets are needed, write "No art or audio assets required."
- **Out of Scope** — what this spec intentionally does not cover.
- **System** — primary owning system ID.
- **Cross-system** — secondary system IDs if applicable, or "None."

### 1g. Behavior path completeness check

For each drafted candidate, verify:
- **Success path** — is the happy-path behavior fully described?
- **Rejection/invalid path** — if the player can attempt this action in an invalid or blocked state, does the spec either cover the rejection path explicitly or defer it to a separate spec? If the action has no invalid state (purely informational), note "N/A."
- **Authority trace** — for every postcondition that changes state, identify which system owns that state change. If a postcondition mutates state and the owning system is unclear, flag it for resolution before creation.

If a candidate is missing its rejection path and the action can be attempted invalidly, either add the rejection behavior or split into separate success/rejection specs.

## Phase 2 — ADR Impact Check

For each spec candidate, check all accepted ADRs:
- Did an ADR change the system behavior this spec covers?
- Did an ADR add constraints or remove features relevant to this spec?
- Did an ADR affect cross-system contracts that this spec depends on?

If ADRs affect a spec, annotate the draft with the ADR reference and its impact. Use the post-ADR behavior, not the original.

## Phase 2b — Known Issue Impact Check

For each spec candidate, check `scaffold/decisions/known-issues.md`:
- Does an open known issue constrain or affect the behavior this spec covers?
- Does a known issue represent an edge case the spec should account for?
- Does a known issue suggest a performance or architectural limitation relevant to this spec?

If known issues affect a spec, annotate the draft with the KI reference and its constraint. Known issue impacts are shown alongside ADR impacts in Phase 4.

## Phase 3 — Check Against Existing Specs

Before presenting candidates, compare against existing specs in `scaffold/specs/`:

Overlap candidates are presented **without consuming SPEC-### IDs**. Only confirmed new specs get IDs in Phase 5.

For each candidate:
1. Check if an existing spec **substantially overlaps** (covers the same behavior or acceptance criteria).
2. If overlap is found, present it as a decision:
   - **(a) Merge** — fold the candidate's behavior into the existing spec.
   - **(b) Split** — the existing spec is too broad; split it and absorb the candidate into one piece.
   - **(c) Keep separate** — the behaviors are distinct enough to warrant separate specs.
   - **(d) Skip** — the existing spec already covers this adequately.
   - **(e) Defer** — valid behavior, but not worth specifying in this slice yet. Record as a gap for future slices.
3. Do not silently create near-duplicates.

## Phase 4 — Present for Confirmation

Present all candidate specs to the user, organized by slice:

```
### Slice: SLICE-### — [Name]
**Slice goal:** [the end-to-end proof this slice demonstrates]

#### Behavior Cluster: [cluster name]

Candidate 1: [name]
- System: SYS-### (primary), SYS-### (secondary)
- Cross-system: Yes/No
- Summary: [one sentence]
- Behavior: [numbered steps]
- Acceptance Criteria: [testable checks]
- ADR impacts: [if any — ADR-### references and how they constrain behavior]
- Known issue impacts: [if any — KI-### references and constraints]
- Existing spec overlap: [if any — with merge/split/keep/skip/defer options]

Candidate 2: [name]
...

#### Coverage Assessment

✓ Slice goal behaviors covered: [list]
⚠ Slice goal behaviors NOT covered: [list — these need specs or explicit deferral]
⚠ State transitions touched by slice but not covered: [list]
⚠ Cross-system handoffs implied by slice but not covered: [list]
⚠ Observable player outcomes in slice goal without a spec: [list]
```

Present decisions using the Human Decision Presentation pattern (see WORKFLOW.md). Each overlap gets numbered options (merge/split/keep/skip/defer). Each candidate gets confirm/modify/remove. Wait for the user's decisions on each issue before proceeding.

## Phase 5 — Create Spec Files

For each confirmed spec:

1. **Assign the next sequential SPEC-### ID** from `scaffold/specs/_index.md`.
2. **Create** `scaffold/specs/SPEC-###-<name>_draft.md` using the spec template. Write substantive content for ALL sections — remove template HTML comments and replace with authored prose. No section should be left at template defaults.

   | Section | What to write | Minimum content |
   |---------|--------------|-----------------|
   | **Summary** | One sentence describing what behavior this spec defines | Complete sentence, not a fragment |
   | **Proof Intent** | What this spec proves within its parent slice — connects spec to slice proof chain | 1 sentence with concrete proof (e.g., "proves valid placement path") |
   | **Trigger** | What causes this behavior to start — player action or system event | 1 sentence naming the specific initiating event |
   | **Preconditions** | What must be true before this behavior can occur | At least 2 bullet points |
   | **Behavior** | Step-by-step description of the behavior — precise and testable | At least 3 numbered steps, each describing one observable action or result |
   | **Observable Outcome** | What can be observed when the behavior succeeds — player-visible or test-observable | At least 2 bullet points |
   | **Failure Outcome** | What happens when the behavior is rejected or fails — expected visible failure | At least 1 failure scenario with observable result |
   | **Postconditions** | What must be true after this behavior completes | At least 2 bullet points |
   | **Edge Cases** | Unusual inputs, boundary conditions, error states | At least 2 edge cases |
   | **Secondary Effects** | Follow-on effects in other systems triggered by this behavior | At least 1 effect, or explicit "No secondary effects — behavior is self-contained" |
   | **Acceptance Criteria** | Concrete pass/fail checks for verifying correct implementation | At least 3 testable criteria |
   | **Asset Requirements** | Table of art/audio assets needed — scan existing assets/ before listing as Needed | Table with entries, or explicit "No art or audio assets required for this behavior" |
   | **Out of Scope** | What this spec intentionally does not cover | At least 1 exclusion |
   | **Notes** | ADR constraints, KI references, design debt, or other context | At least 1 note, or explicit "No additional constraints" |

   - Set the System reference to the primary system ID.
   - If the spec is cross-system, add secondary system IDs as **header metadata** (e.g., `> **Secondary Systems:** SYS-###, SYS-###`), not as narrative in the behavior body. Cross-system is a structural property, not a behavior step.
   - Set the Conforms to reference.
3. **Register** the spec in `scaffold/specs/_index.md` with the system reference and slice reference.
4. **Update** the parent slice's Specs Included table with the new spec ID and description.

## Phase 6 — Report

Summarize what was seeded:
- Specs created: X total, across Y slices
- Per slice: how many specs and what behaviors they cover
- Per system: how many specs reference each system
- Cross-system specs: X total

Flag any remaining gaps:
- Slice goal behaviors not fully covered by specs
- Observable player outcomes in slice goals without a spec
- State transitions touched by slices but with no spec
- Cross-system handoffs implied by slices but with no spec
- ADRs that affect specs (annotated in the spec files)

Remind the user of next steps. Seeded specs go through a stabilization loop before task generation:
- Run `/scaffold-fix-spec SPEC-###-SPEC-###` to auto-fix mechanical issues
- Run `/scaffold-iterate` on specs for adversarial review
- Run `/scaffold-triage-specs SLICE-###` to resolve human-required issues
- Repeat fix → iterate → triage until stable
- Run `/scaffold-validate` to check planning-pipeline integrity
- Run `/scaffold-approve-specs SLICE-###` to mark specs as Approved
- Then run `/scaffold-bulk-seed-tasks SLICE-###` to generate implementation tasks from approved specs

## Rules

- **Seeded files must contain substantive content, not template placeholders.** Every section (Summary, Trigger, Preconditions, Behavior, Acceptance Criteria, Asset Requirements, etc.) must have real authored prose derived from system designs and slice goals. Do not leave sections as TODO, HTML comment prompts, or single generic sentences. Remove template HTML comments from sections that receive authored content — replace them with actual behavioral descriptions and testable criteria. A spec file where Behavior is "TBD" or Acceptance Criteria is the template's HTML comment has failed the seed.
- **Slice goals drive spec selection.** Derive candidates from what the slice must prove end-to-end, not from exhaustive system behavior enumeration. System designs flesh out behavior; they don't determine which specs exist.
- **Never write without confirmation.** Present all proposed specs before creating files.
- **Specs describe BEHAVIOR, not IMPLEMENTATION.** No signals, methods, nodes, classes, functions, or engine constructs in spec content. Translate Player Actions and System Resolution into behavior language.
- **Cluster before splitting.** Group related behaviors, then split into atomic units. Don't jump from system action to spec without considering whether behaviors cluster.
- **Cross-system specs must be explicit.** Assign a primary owning system and note secondary systems. Do not flatten cross-system behavior into a single-system spec without acknowledging the dependency.
- **Handle existing spec overlaps explicitly.** Present merge/split/keep/skip options for every overlap. Never silently create near-duplicates.
- **Pre-filled content is a starting point.** Always present pre-filled content for user confirmation — never treat it as final.
- **IDs are sequential and permanent** — never skip or reuse.
- **Each spec should be atomic** — one testable behavior. If a behavior cluster can't be split cleanly, keep it as one spec.
- **Flag conflicts, don't resolve them.** If system designs disagree about a behavior, present the conflict to the user.
- **ADR impacts must be noted.** If an ADR changes a system behavior, the spec must reflect the post-ADR behavior, not the original.
- **Created documents start with Status: Draft.**
