# State Transitions

> **Authority:** Rank 5
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md)

---

## Purpose

Master registry of all state machines in the game. Every entity or system that has discrete states (idle, active, dead, paused, etc.) is defined here with its valid transitions, triggers, and owning authority.

## State Machines

<!-- Add state machines as entities/systems are designed. One section per state machine. -->

*None yet.*

<!-- Example entry:

### Colonist Lifecycle

**Authority:** SYS-002 Needs & Mood
**Entity:** Colonist

| State | Transitions To | Trigger | Notes |
|-------|---------------|---------|-------|
| Idle | Working | Job assigned by Job Queue | |
| Idle | Sleeping | Rest need critical | |
| Working | Idle | Job complete or cancelled | |
| Working | Downed | Health reaches 0 | Drops current job |
| Sleeping | Idle | Rest need satisfied | |
| Downed | Recovering | Rescued + medical treatment | |
| Downed | Dead | Bleed-out timer expires | |
| Recovering | Idle | Health above threshold | |
| Dead | (terminal) | — | Entity removed or converted to corpse |

**Invariants:**
- A colonist can only be in one state at a time.
- Only the owning system may trigger transitions.
- Dead is terminal — no transitions out.

-->

## Template

Use this format for each state machine:

```markdown
### [State Machine Name]

**Authority:** [Owning system]
**Entity:** [What entity/object this applies to]

| State | Transitions To | Trigger | Notes |
|-------|---------------|---------|-------|
| ... | ... | ... | ... |

**Invariants:**
- [Rules that must always hold for this state machine]
```

## Rules

1. **Every state machine has one authority.** The owning system is the only one that may trigger transitions.
2. **All transitions are explicit.** If a transition isn't in the table, it's not allowed — no implicit state changes.
3. **Terminal states are marked.** If a state has no outgoing transitions, mark it `(terminal)`.
4. **Invariants are enforced, not aspirational.** If an invariant says "only one state at a time," the implementation must guarantee it.
