# Roadmap

> **Authority:** Rank 7
> **Layer:** Scope
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)

---

## Purpose

Living document that tracks the full project arc from start to ship. Phases, slices, specs, and tasks all derive from this roadmap. Updated after every phase completion and whenever ADRs from implementation change the plan.

## Vision Checkpoint

<!-- One line from the design doc's Core Fantasy. Keep this visible as a constant reminder of what we're building toward. -->

*TODO: Copy the Core Fantasy from the design doc.*

## Phase Overview

<!-- Master view of all phases. Update Status as phases progress. -->

| Phase | Goal | Status | Key Deliverable |
|-------|------|--------|-----------------|
| *None yet* | — | — | — |

<!-- Example entries:
| P1 — Foundation | Prove the core loop works | Complete | Playable core loop prototype |
| P2 — Systems | Build all primary systems | In Progress | All SYS designs implemented |
| P3 — Content | Populate the game world | Planned | First playable level |
| P4 — Polish | Juice, UX, accessibility | Planned | Release candidate |
-->

## Current Phase

<!-- What we're building right now. Link to the phase doc. -->

*TODO: Set when the first phase is created.*

## ADR Feedback Log

<!-- After completing each phase (or significant task), review ADRs filed during that work and record their impact on the roadmap here. This is the feedback loop that keeps the plan honest. -->

| ADR | Impact | Affected Phases/Slices/Specs |
|-----|--------|------------------------------|
| *None yet* | — | — |

<!-- Example entries:
| ADR-001 | Pathfinding too expensive for real-time → switched to turn-based movement | P2 scope reduced, SPEC-005 rewritten |
| ADR-003 | Inventory system needs crafting support not originally planned | P2 extended, new SLICE-004 added |
| ADR-007 | Touch controls infeasible for this game → mobile platform cut | P4 scope reduced, input docs updated |
-->

## Completed Phases

<!-- Move phases here when they're done. Record what was delivered, what ADRs were filed, and what changed from the original plan. -->

*None yet.*

<!-- Example entry:

### P1 — Foundation (Complete)

**Delivered:** Playable core loop — player can move, interact with objects, and trigger the primary mechanic.
**ADRs filed:** ADR-001 (pathfinding change), ADR-002 (camera angle)
**Scope changes:** Camera switched from isometric to top-down per ADR-002.
**Lessons learned:** Physics system was the bottleneck, not rendering. Budget more time for physics in P2.

-->

## Upcoming Phases

<!-- Tentative — these WILL change based on ADRs and lessons from completed phases. Don't over-plan. -->

*TODO: Define upcoming phases after the first phase is created.*

## Phase Transition Protocol

When a phase completes:

1. **Review all ADRs** filed during the phase. For each ADR:
   - Does it affect any upcoming phase's scope? → Update the Phase Overview table.
   - Does it invalidate any existing specs? → Flag for rewrite.
   - Does it require new slices or tasks? → Add them to the affected phase.
2. **Update the ADR Feedback Log** with a summary of each ADR's impact.
3. **Move the phase to Completed Phases** with delivery notes and lessons learned.
4. **Re-scope the next phase** based on:
   - ADR impacts
   - What was learned during implementation
   - Any scope that was deferred from the completed phase
5. **Update the Phase Overview table** with new statuses.
6. **Set Current Phase** to the next phase.

## Rules

1. **This is a living document.** It changes after every phase and whenever ADRs shift the plan.
2. **Upcoming phases are tentative.** Don't treat them as commitments — they will change.
3. **ADRs are the feedback mechanism.** Implementation reality feeds back into planning through ADRs. Never ignore ADRs when planning the next phase.
4. **Vision Checkpoint is constant.** The core fantasy doesn't change unless the design doc changes (which requires its own ADR). Everything else flexes around it.
5. **Scope cuts are recorded, not hidden.** If something is cut, note what was cut and why in the completed phase entry.
