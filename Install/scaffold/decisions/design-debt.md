# Design Debt

> **Authority:** Rank 6
> **Layer:** Reference

---

## Purpose

Intentional design compromises — things we know are wrong or incomplete but are shipping anyway, at least for now. Unlike known issues (which are unresolved questions), design debt is a conscious decision to accept a less-than-ideal solution with a plan to revisit it.

## Active Debt

<!-- Add entries when a compromise is made. Remove when the debt is paid off. -->

| ID | Area | Compromise | Why | Payoff Plan | Priority |
|----|------|-----------|-----|-------------|----------|
| *None yet* | — | — | — | — | — |

<!-- Example entries:
| DD-001 | Combat    | Damage is flat, no armor calculation       | Armor system not designed yet        | Implement after SYS-003 v2  | Medium |
| DD-002 | Building  | No structural integrity — floating roofs OK | Structural sim too complex for alpha | Revisit in beta if time     | Low    |
| DD-003 | AI        | Colonists don't avoid danger zones         | Threat mapping not implemented       | Required before combat slice | High   |
| DD-004 | Balance   | All resources weigh the same               | Weight system deferred               | Phase 3                     | Low    |
-->

## Paid Off

<!-- Move here when the debt is resolved. -->

| ID | Area | Compromise | Resolution | Resolved In |
|----|------|-----------|------------|-------------|
| *None yet* | — | — | — | — |

## Rules

1. **Debt is intentional.** If you didn't know it was a compromise, it's a known issue, not debt. Log it in [known-issues.md](known-issues.md).
2. **Every debt needs a payoff plan.** "We'll fix it later" is not a plan. "Revisit after SYS-003 is complete" is.
3. **Priority reflects risk, not effort.** High priority = this will cause real problems if left too long.
4. **Debt accumulates interest.** Review this list each phase. If something has been "Low priority" for three phases, either pay it off or accept it as permanent.
