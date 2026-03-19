---
name: scaffold-fix-references
description: Mechanical cleanup pass for Step 3 docs (architecture, authority, interfaces, state-transitions, entity-components, resource-definitions, signal-registry, balance-params, enums-and-statuses). Auto-fixes structural issues, cross-doc inconsistencies, and terminology drift. Detects design signals for adversarial review. Supports --target for single-doc focus.
argument-hint: [--target doc.md] [--iterate N]
allowed-tools: Read, Edit, Grep, Glob
---

# Fix References

Mechanical cleanup and signal detection for Step 3 reference and architecture docs: **$ARGUMENTS**

This skill is the **formatter and linter** for Step 3 docs — not the design reviewer. It normalizes structure, repairs mechanical inconsistencies across the 9 Step 3 docs, and detects design signals. It does not interpret or resolve design issues — that is the job of `iterate-references` (adversarial review) which runs immediately after this skill.

**What fix-references does:** normalize docs so adversarial review doesn't waste time on trivial issues.
**What fix-references does NOT do:** evaluate whether the architecture is good, resolve ownership conflicts, or make foundation decisions.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--target` | No | all | Target a single doc by filename (e.g., `--target architecture.md`, `--target authority.md`, `--target signal-registry.md`). When omitted, processes all 9 Step 3 docs. |
| `--iterate N` | No | `10` | Maximum review-fix passes before stopping. Stops early on convergence. |

### Valid --target values

| Target | Doc Path |
|--------|----------|
| `architecture.md` | `design/architecture.md` |
| `authority.md` | `design/authority.md` |
| `interfaces.md` | `design/interfaces.md` |
| `state-transitions.md` | `design/state-transitions.md` |
| `entity-components.md` | `reference/entity-components.md` |
| `resource-definitions.md` | `reference/resource-definitions.md` |
| `signal-registry.md` | `reference/signal-registry.md` |
| `balance-params.md` | `reference/balance-params.md` |
| `enums-and-statuses.md` | `reference/enums-and-statuses.md` |

When `--target` is specified, cross-doc checks still run (reading other docs for consistency) but only the targeted doc is edited. This is the expected mode when called from `revise-foundation` after a specific doc was revised.

## Step 1 — Gather Context

Always read (regardless of `--target`):
1. `scaffold/design/design-doc.md` — Design Invariants, governance, glossary references.
2. `scaffold/design/glossary.md` — canonical terminology.
3. `scaffold/doc-authority.md` — document authority ranking, same-rank conflict resolution rules, deprecation protocol.
4. `scaffold/design/systems/_index.md` — registered system IDs and names.
5. All accepted ADRs in `scaffold/decisions/`.
6. `scaffold/decisions/known-issues.md`.

Read the target doc(s) and their templates:
7. Each target doc from `scaffold/design/` or `scaffold/reference/`.
8. Corresponding template from `scaffold/templates/` — defines expected section structure.

Read cross-reference docs (for consistency checks, not editing):
9. All 9 Step 3 docs (even when targeting one — cross-doc consistency requires reading neighbors).
10. System designs that are referenced by authority/interface/signal entries.

## Step 2 — Per-Doc Checks

### architecture.md

#### Section Structure
Compare against the architecture template. Required sections:
- Purpose
- Scene Tree Layout (with System Representation subsection)
- System Dependency Graph (with tier purpose clarification)
- Tick Processing Order (with Simulation Update Semantics subsection)
- Signal Wiring Map (Behavioral + Logging)
- Data Flow Rules (positive rules + Forbidden Patterns)
- Initialization & Boot Order
- Entity Identity & References (Runtime, Persistent, Content, How Systems Reference)
- Failure & Recovery Patterns
- Code Patterns
- Rules

#### Mechanical Checks
- **Scene tree completeness** — every system registered in `systems/_index.md` appears in the scene tree. Missing systems flagged.
- **Dependency graph consistency** — tier assignments don't violate stated tier rules. No upward dependencies.
- **Tick order completeness** — every ticked system in the scene tree has a tick position.
- **Signal wiring coverage** — signals in the wiring map exist in `signal-registry.md`. Signals in the registry with Gameplay classification appear in the behavioral wiring table.
- **Simulation Update Semantics present** — subsection exists under Tick Processing Order, even if contents are TBD. Missing section entirely is a structural failure, not just a design signal.
- **Data flow rule count** — positive rules section is not empty or template-only.
- **Forbidden patterns present** — all 7 template forbidden patterns exist.
- **Identity section populated** — not all TBD/placeholder. If engine docs exist and identity is still all TBD, escalate as design signal.
- **Boot order populated** — not template-only. If engine docs exist, boot sequence table should have concrete entries. If engine docs don't exist, TBD is acceptable.
- **Failure/Recovery patterns populated** — at least template categories present (missing dependency, stale reference, invalid state, data corruption). If system designs or known-issues mention recovery behavior, doc should reflect that.
- **Terminology compliance** — glossary canonical terms throughout.
- **Template text / TODOs** — no remaining placeholder content in populated sections.

#### Design Signals
- **Dependency cycle detected** — signal for iterate-references.
- **Tick order ambiguity** — systems with unclear ordering justification.
- **Missing simulation update semantics** — timing decisions still TBD after engine docs exist.

---

### authority.md

#### Section Structure
Required: Purpose, Ownership Model, Domain grouping sections with authority tables, Conflict/TBD section, Rules.

#### Mechanical Checks
- **Table columns complete** — every row has: Variable/Property, Owning System, Write Mode, Authority Type, Persistence Owner, Readers, Update Cadence, Notes.
- **System ID resolution** — every SYS-### in the table exists in `systems/_index.md`.
- **Domain grouping** — entries organized by domain, not flat.
- **Derived/Cache consistency** — entries marked Derived or Cache have Persistence Owner = "—".
- **Entity-components alignment** — Authority column in `entity-components.md` matches ownership claims here. Flag mismatches. **authority.md wins on conflict.**
- **System Owned State alignment** — for each system in range, every variable in the system's Owned State section has a corresponding authority.md entry. Flag missing entries.
- **No duplicate variables** — same Variable/Property name doesn't appear in multiple domain sections.
- **Terminology compliance.**
- **Conflict/TBD section populated** — any unresolved ownership disputes are tracked here.

#### Design Signals
- **Ownership conflict** — two systems appear to write the same variable (from system Owned State cross-check).
- **Authority type mismatch** — a variable marked Authoritative has no Persistence Owner, or a Derived variable has one.
- **Stale system reference** — references a system that no longer exists or was renamed.

---

### interfaces.md

#### Section Structure
Required: Purpose, Relationship to Other Documents, Domain grouping sections with interface tables, Missing/TBD Contracts section, Rules.

#### Mechanical Checks
- **Table columns complete** — every row has: Source System, Target System, Data Exchanged, Direction, Realization Path, Timing, Failure Guarantee, Notes.
- **System ID resolution** — both Source and Target exist in `systems/_index.md`.
- **Direction values valid** — Push / Pull / Request / TBD only.
- **Realization Path values valid** — signal / intent / query API / direct sanctioned interface call / TBD only.
- **Timing values valid** — immediate / deferred / next tick / TBD only.
- **Failure Guarantee values valid** — can fail / no-op / queue / retry / TBD only.
- **Signal registry alignment** — interfaces realized via signal have a corresponding entry in `signal-registry.md`. Flag missing signals.
- **Bidirectional coverage** — if System A → B exists, check whether B → A is needed (from system dependency tables). Flag potential missing reverse contracts.
- **Authority alignment** — interface data exchanged is consistent with who owns what in `authority.md`. A system cannot Push data it doesn't own.
- **No duplicate contracts** — same Source + Target + Data Exchanged doesn't appear twice.
- **Terminology compliance.**
- **Missing/TBD section populated** — known gaps are tracked.

#### Design Signals
- **Unresolved direction** — Direction: TBD entries that should have been resolved by now.
- **Missing realization path** — contract has no signal, intent, or API to implement it.
- **Authority violation** — interface implies a system sending data it doesn't own per authority.md.

---

### state-transitions.md

#### Section Structure
Required: Purpose, numbered state machine sections each with: Authority, Entity, transition table (with Timing column), Entry Conditions, Exit Conditions, Illegal Transitions, Cross-System Readers, Invariants.

#### Mechanical Checks
- **Authority resolution** — every Authority system exists in `systems/_index.md`.
- **Timing column present** — every transition row has a Timing value.
- **Timing values valid** — immediate / queued / end-of-tick / TBD only.
- **Terminal states marked** — `*(terminal)*` in Transitions To column for states with no outgoing transitions.
- **Invariants present** — every state machine has at least "entity is in exactly one state" and "only authority triggers transitions."
- **State name consistency** — state names match `enums-and-statuses.md` for cross-system states. Flag drift.
- **Entity-components alignment** — entity types in state machines exist in `entity-components.md` with corresponding enum fields.
- **No orphan state machines** — every state machine's authority system exists and claims the relevant state in Owned State.
- **Sequential numbering** — state machines are numbered 1, 2, 3... without gaps.
- **Terminology compliance.**

#### Design Signals
- **Missing illegal transitions** — section is empty for complex state machines (5+ states).
- **No cross-system readers** — state machine with cross-system enum has no readers listed.
- **Continuous value modeled as discrete** — state names suggest thresholded continuous values without explicit band definitions.

---

### entity-components.md

#### Section Structure
Required: Purpose, Entity Reference Convention, Content Identity Convention, Reference Type Conventions, Singleton Conventions, Derived/Cache Field Policy, entity sections with component tables, Rules.

#### Mechanical Checks
- **Convention sections populated** — Entity Reference Convention, Content Identity Convention, Reference Type Conventions, Singleton Conventions, and Derived/Cache Field Policy sections exist and are not template-only. If identity decisions are TBD (pre-Step 7), TBD is acceptable but section must exist.
- **Table columns complete** — every row has: Component, Field, Type, Authority, Cadence, Persistence, Notes.
- **Authority alignment** — Authority column (owning system) matches `authority.md`. Flag mismatches. **authority.md wins.** The Authority column in entity-components always means the owning SYS-### system, never a type classification.
- **Type concreteness** — no vague types ("data", "info", "stuff"). Must be string, int, float, bool, enum, list, dict, ref, Vector2i, etc.
- **Persistence consistency** — Persistence column determines saved/derived/transient status. Fields with Persistence = "Derived" should have their source documented in Notes. Fields with Persistence = "Saved" must have a real Authority system (not "Derived" or "Cache" in the Authority column). The Derived/Cache Field Policy section governs these conventions.
- **Singleton marker** — singleton entities (Colony, World, PowerGrid) have Singleton in Component column.
- **Handle convention used** — `ref` type fields reference the stated Entity Reference Convention.
- **State fields match state-transitions.md** — enum fields corresponding to state machines use the same state names.
- **No orphan entities** — every entity traces back to at least one system's Owned State.
- **Terminology compliance.**

#### Design Signals
- **Authority mismatch** — Authority column doesn't match authority.md.
- **Missing persistence** — Persistence column empty for fields that clearly affect gameplay.
- **Over-entityfication** — entity has fewer than 3 fields and no lifecycle — may not warrant entity status.

---

### resource-definitions.md

#### Section Structure
Required: Purpose, Tier Definitions, Storage Types, Resource Categories summary, per-category sections, Resource State Variants, Production Chains, Production Stations (if applicable), Rules.

#### Mechanical Checks
- **Table columns complete** — every row has: Resource, Tier, Source, Storage, Fungibility, Physical/Abstract, Transportability, Notes.
- **Tier values valid** — 1, 2, 3, or 4 only.
- **Category summary count matches** — total in summary table equals sum of per-category entries.
- **Production chain completeness** — every Tier 2+ resource has a production chain entry tracing back to Tier 1 sources, unless Source explicitly marks it as imported / scavenged / event-only / expedition-only.
- **Station registry** — every station mentioned in production chains appears in the station table.
- **Fungibility values valid** — fungible / unique / TBD only.
- **Physical/Abstract values valid** — Physical / Abstract / TBD only.
- **Transportability values valid** — hauled / piped / instant / immovable / TBD only.
- **No duplicate resources** — same Resource name doesn't appear in multiple categories.
- **Terminology compliance.**

#### Design Signals
- **Fungible/unique ambiguity** — resource marked fungible but entity-components has a corresponding item entity (or vice versa).
- **Missing production chain** — Tier 2+ resource with no chain.
- **Orphan station** — station in registry not referenced by any chain.

---

### signal-registry.md

#### Section Structure
Required: Purpose, Signal vs Intent Conventions, Signals table, Intent Objects table, Dispatch Timing Conventions, Payload Schema Conventions, Rules.

#### Mechanical Checks
- **Signal table columns complete** — every row has: Signal Name, Level, Payload, Emitter, Consumer(s), Delivery Expectation, Gameplay/Logging, Notes.
- **Intent table columns complete** — every row has: Intent Object, Payload, Requester, Handler, Delivery Expectation, Notes.
- **System ID resolution** — every Emitter, Consumer, Requester, Handler exists in `systems/_index.md`. "UI" is valid shorthand.
- **Level values valid** — Entity / Room / System / Colony / Global only.
- **Delivery Expectation values valid** — fire-and-forget / reliable / deduped / queued / TBD only.
- **Gameplay/Logging values valid** — Gameplay / Logging / Both only.
- **Signal naming convention** — past tense with underscores (structure_completed, not completeStructure).
- **Intent naming convention** — noun form with underscores (hauling_request, not haul).
- **Interface alignment** — every Push interface in `interfaces.md` realized via signal has a corresponding signal here. Flag gaps.
- **No duplicate signals** — same Signal Name doesn't appear twice.
- **Payload field concreteness** — no vague payloads ("data", "info"). Must list specific fields.
- **Terminology compliance.**

#### Design Signals
- **Missing consumers** — signal with Gameplay classification but empty/single consumer list.
- **Orphan signal** — signal not referenced by any interface contract.
- **Logging-only with gameplay consumers** — signal marked Logging but consumed by gameplay systems. Signals marked Both are not flagged — they intentionally serve dual purposes.

---

### balance-params.md

#### Section Structure
Required: Purpose, Parameter naming/unit conventions, per-system sections, TBD/Unresolved Tuning section, Rules.

#### Mechanical Checks
- **Table columns complete** — every row has: Parameter, Value, Unit, Type, Range, System, Dependency Notes, Notes.
- **Type values valid** — threshold / rate / duration / capacity / multiplier / TBD only.
- **System ID resolution** — every System exists in `systems/_index.md`.
- **Range present** — every parameter has a min–max range (TBD range is acceptable but flagged).
- **Convention sections populated** — Parameter naming/unit conventions section exists and is not template-only.
- **Unit concreteness** — no vague units. Must be specific (hp, per hour, multiplier, seconds, etc.).
- **System grouping** — organized by system subsection in ascending SYS-### order.
- **No duplicate parameters** — same Parameter name + System doesn't appear twice.
- **TBD section populated** — unresolved tuning items tracked.
- **Terminology compliance.**

#### Design Signals
- **Orphan parameter** — parameter references a system that doesn't exist.
- **Missing dependency notes** — parameter is clearly a multiplier for another parameter but Dependency Notes is empty.
- **TBD clustering** — 50%+ of a system's parameters are TBD — system may be under-designed.

---

### enums-and-statuses.md

#### Section Structure
Required: Purpose, Canonical vocabulary rules, category sections with enum tables, Rules.

#### Mechanical Checks
- **Table columns complete** — every row has: State, Meaning, Used By, Owning Authority/System, Source of Truth, Deprecated Synonyms.
- **Used By has 2+ systems** — single-system enums don't belong here.
- **System ID resolution** — every system in Used By and Owning Authority exists in `systems/_index.md`.
- **State-transitions alignment** — state values that appear in state-transitions.md use identical names here.
- **Glossary alignment** — terms don't conflict with glossary.md (simulation-facing here, player-facing in glossary).
- **No duplicate states** — same State value doesn't appear in multiple categories.
- **Source of Truth values valid** — state-transition / authority / interface / UI only.
- **Source of Truth populated** — every entry has a value, not empty.
- **Terminology compliance.**

#### Design Signals
- **Terminology drift** — enum value differs from state-transitions.md name.
- **Missing owning authority** — shared state with no clear authority system.
- **Single-system leak** — enum only used by one system — should move to system doc.

---

## Step 3 — Classify Issues

### Auto-Fixable (apply immediately)

| Category | Fix | Condition |
|----------|-----|-----------|
| **Missing sections** | Add section heading with template content | Section required by template and genuinely absent |
| **Missing table columns** | Add column headers to existing tables | Template has columns the doc doesn't |
| **Template text / TODOs** | Remove placeholder text in populated sections | Section has authored content beyond template markers |
| **Terminology drift** | Replace NOT-column terms with canonical terms | Used as authoritative terminology, not in examples/quotes |
| **Registration gaps** | Add missing system to `_index.md` cross-reference | System referenced in Step 3 doc but missing from index |
| **Duplicate entries** | Merge duplicate rows, keeping the more complete version | Same equivalence key (see bulk-seed-references rules) appears twice |
| **Stale ADR references** | Update to current ADR status | ADR status changed since doc was last edited |
| **Stale system references** | Update system name to match current `_index.md` | System was renamed |
| **Missing reciprocal entries** | Add stub entry in counterpart doc | Only when the canonical doc explicitly implies a counterpart artifact (Push interface → signal stub, Request interface → intent stub). Do not add reciprocal stubs when the relationship itself is uncertain or marked TBD. Stub only — content is human-required. |
| **Missing convention section** | Add section heading from template | Convention section required by template and genuinely absent (entity-components conventions, signal/intent conventions, parameter naming conventions, canonical vocabulary rules) |
| **Authority-entity alignment** | Update entity-components Authority column to match authority.md | authority.md is canonical; entity-components derives from it |

### Mechanically Detected, User-Confirmed

| Category | Action |
|----------|--------|
| **Template defaults remaining** | Section still at template/default level. Report for human completion. |
| **Authority conflict** | Two systems claim same variable. Report with both sources for human resolution. |
| **Missing realization path** | Interface contract has no signal/intent/API. Report for human decision. |
| **Fungible/unique ambiguity** | Resource exists in both resource-definitions and entity-components. Report for modeling decision. |
| **TBD entries after engine docs exist** | Timing/identity decisions still TBD when engine docs are populated. Report for human resolution. |

### Design Signals (for adversarial review)

These feed into `iterate-references`. Detected and reported, not resolved.

| Signal | Context |
|--------|---------|
| Dependency cycle | Systems form a cycle in the dependency graph |
| Authority mismatch | Owned State vs authority.md vs entity-components disagree |
| Interface without realization | Contract exists but no signal/intent/API implements it |
| Orphan signal | Signal not referenced by any interface |
| State-transitions drift | State names don't match enums-and-statuses |
| Over-entityfication | Entity with <3 fields and no lifecycle |
| TBD clustering | 50%+ of a doc section is TBD |
| Missing forbidden pattern | Architecture.md missing one of the 7 template forbidden patterns |
| Canonical section underpopulated | A required section in any doc is still mostly template/TBD when its upstream inputs exist (e.g., architecture identity still TBD after engine docs exist, authority Conflict/TBD growing instead of shrinking, interfaces with many Direction:TBD, signal-registry with vague payloads, balance-params 50%+ TBD for a system) |

## Step 4 — Apply Auto-Fixes

**Safety rules:**
- **When `--target` is set, only edit the targeted doc.** Cross-doc mismatches are flagged but counterpart docs are not edited.
- **When `--target` is not set, edit all 9 docs.** Cross-doc fixes (authority-entity alignment, signal-interface stubs) apply to both sides.
- **Never edit system designs, design-doc, engine docs, or planning docs.** Only edit Step 3 docs.
- **Never change architectural decisions.** Only fix how clearly they're expressed and how consistently they're reflected.
- **Derive fixes from existing doc content, not invented.** Consistency fixes come from authoritative sources.
- **Authority.md is canonical for ownership.** On mismatch with entity-components, fix entity-components.
- **Interfaces.md is canonical for contracts.** On mismatch with signal-registry, fix signal-registry.
- **State-transitions.md is canonical for state names.** On mismatch with enums-and-statuses, fix enums-and-statuses.
- **No speculative fixes.** When multiple plausible interpretations exist, report instead of auto-fixing.

## Step 5 — Cross-Doc Pass

After all per-doc checks and fixes, run one cross-doc consistency pass:

1. **Authority → Entity-Components** — every authority.md variable has a corresponding entity-components field. Flag gaps.
2. **Interfaces → Signal Registry** — every Push interface has a signal. Every Request interface has an intent. Every signal has a consuming interface. Flag orphans.
3. **State-Transitions → Entity-Components** — every state machine's entity has corresponding enum fields. State names match.
4. **State-Transitions → Enums-and-Statuses** — cross-system states appear in enums. Names match exactly.
5. **Authority → Interfaces** — a system cannot Push data it doesn't own. Flag authority violations in interface contracts.
6. **Architecture → All** — scene tree systems match _index.md. Tick order systems are complete. Signal wiring entries exist in signal-registry.
7. **Resource-Definitions → Entity-Components** — fungible resources and unique item entities are not duplicated across both docs.
8. **Balance-Params → Systems** — every balance param references an existing system. Systems with gameplay behavior have at least some parameters registered.

Cross-doc pass results are:
- Auto-fixable alignment issues → applied (respecting `--target` scope)
- Design signals → reported for iterate-references

## Step 6 — Re-review and Iterate

After applying fixes, re-review. Continue iterating until:
- **Clean** — no issues remain.
- **Human-only** — only human-required issues and design signals remain.
- **Stable** — same issues persist across two consecutive passes.
- **Limit** — `--iterate N` reached.

## Step 7 — Report

```
## Fix-References Summary

### Configuration
| Field | Value |
|-------|-------|
| Target | [all / specific doc] |
| Passes | N completed / M max [early stop: yes/no] |
| Auto-fixed | N issues |
| User-confirmed pending | N issues |
| Design signals | N issues |
| Final status | Clean / Human-only / Stable / Limit |

### Per-Doc Status
| Document | Auto-fixed | User-pending | Design Signals | Status |
|----------|-----------|-------------|----------------|--------|
| architecture.md | N | N | N | Clean / Human-only |
| authority.md | N | N | N | Clean / Human-only |
| interfaces.md | N | N | N | Clean / Human-only |
| state-transitions.md | N | N | N | Clean / Human-only |
| entity-components.md | N | N | N | Clean / Human-only |
| resource-definitions.md | N | N | N | Clean / Human-only |
| signal-registry.md | N | N | N | Clean / Human-only |
| balance-params.md | N | N | N | Clean / Human-only |
| enums-and-statuses.md | N | N | N | Clean / Human-only |

### Auto-Fixes Applied
| # | Document | Category | What Changed |
|---|----------|----------|-------------|
| 1 | authority.md | Terminology | Replaced "worker" with "colonist" |
| 2 | entity-components.md | Authority alignment | Updated Authority column for colonist.mood to match authority.md |
| ... | ... | ... | ... |

### User-Confirmed Actions Pending
| # | Document | Category | Action Required |
|---|----------|----------|----------------|
| 1 | architecture.md | Template defaults | Simulation Update Semantics still TBD |
| 2 | authority.md | Authority conflict | colonist.mood claimed by SYS-004 and SYS-009 |
| ... | ... | ... | ... |

### Design Signals (for iterate-references)
| # | Documents | Signal | Detail |
|---|----------|--------|--------|
| 1 | authority.md, entity-components.md | Authority mismatch | 3 fields disagree between docs |
| 2 | interfaces.md, signal-registry.md | Missing realization | 2 contracts have no signal/intent |
| ... | ... | ... | ... |

### Cross-Doc Consistency
| Check | Result | Issues |
|-------|--------|--------|
| Authority → Entity-Components | N gaps | ... |
| Interfaces → Signal Registry | N orphans | ... |
| State-Transitions → Enums | N drift | ... |
| Architecture → Scene Tree | N missing | ... |
| Resource-Defs → Entity-Components | N duplicates | ... |
```

## Rules

- **This skill is a formatter and linter, not a design reviewer.** It normalizes docs and detects signals. Design evaluation belongs to iterate-references.
- **Authority hierarchy governs fix direction.** authority.md → entity-components. interfaces.md → signal-registry. state-transitions.md → enums-and-statuses. Higher-rank doc is canonical; lower-rank doc gets fixed.
- **--target restricts edits, not reads.** When targeting one doc, all 9 docs are still read for cross-doc checks, but only the target is edited. Mismatches in other docs are flagged, not fixed.
- **Never change architectural decisions.** Auto-fixes clarify expression and fix consistency. They never alter what the architecture says.
- **Never edit upstream docs.** Step 3 docs never auto-edit system designs, design-doc, engine docs, or planning docs. Flag mismatches for human resolution.
- **No speculative fixes.** When multiple plausible interpretations exist, report — do not auto-fix.
- **Design signals are detected, not resolved.** Architectural, ownership, and consistency signals are reported for iterate-references — not acted on by this skill.
- **Terminology fixes respect context.** Only replace NOT-column terms when used as authoritative design terminology.
- **Duplicate detection uses equivalence keys.** Same Variable/Property (authority), same Source+Target+Data (interfaces), same Signal Name (signals), same Resource name (resources), same State value (enums), same Entity+Component+Field (entity-components), same Parameter+System (balance).
- **Stub entries are minimal.** When adding a missing reciprocal entry (signal for an interface, or interface for a signal), add a stub row with TBD fields. Content is human-required.
- **Cross-doc pass runs after per-doc fixes.** Individual doc fixes may resolve issues that the cross-doc pass would otherwise flag.
