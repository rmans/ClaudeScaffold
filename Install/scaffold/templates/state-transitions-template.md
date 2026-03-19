# State Transitions

> **Authority:** Rank 5
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft

---

## Purpose

Master registry of all state machines in the game. Every entity or system that has discrete states (idle, active, dead, paused, etc.) is defined here with its valid transitions, triggers, and owning authority.

## State Machines

### 1. [State Machine Name]

**Authority:** SYS-### SystemName
**Entity:** EntityName

| State | Transitions To | Trigger | Timing | Notes |
|-------|---------------|---------|--------|-------|
| ... | ... | ... | immediate / queued / end-of-tick | ... |

<!-- Timing values:
  - immediate: Transition happens synchronously when the trigger fires.
  - queued: Transition is queued and applied during the owning system's next processing pass.
  - end-of-tick: Transition is batched and applied at the end of the current simulation tick.
-->

**Entry Conditions:**
<!-- Conditions that must be true for an entity to enter this state machine (e.g., entity must be fully initialized, must have a valid owner, etc.). -->
- ...

**Exit Conditions:**
<!-- Conditions that must be true for an entity to leave this state machine entirely (e.g., entity is destroyed, archived, or transferred to another system). -->
- ...

**Illegal Transitions:**
<!-- Explicitly list state pairs that must NEVER occur, even if a code path could technically trigger them. These are invariant violations if observed. -->
| From | To | Reason |
|------|----|--------|
| ... | ... | Why this transition is forbidden |

**Cross-System Readers:**
<!-- Systems other than the authority that read this state machine's current value. Important for understanding who depends on state changes. Omit if no external readers. -->
| Reader System | Why It Reads | Reaction |
|---------------|-------------|----------|
| SYS-### Name | ... | What the reader does when state changes |

**Invariants:**
- An entity is in exactly one state at a time.
- Only the authority system triggers transitions.
- [Terminal state] is terminal — no transitions out.
- ...

---

<!-- Repeat for each state machine. Number sequentially (1, 2, 3...). Each state machine must have:
  - A descriptive name
  - Authority (owning system)
  - Entity (what has this state)
  - Transition table (State → Transitions To → Trigger → Notes)
  - Invariants (rules that must always hold)
-->

<!-- Template for adding a new state machine:

### N. [State Machine Name]

**Authority:** SYS-### SystemName
**Entity:** EntityName

| State | Transitions To | Trigger | Timing | Notes |
|-------|---------------|---------|--------|-------|
| StateA | StateB | Condition that causes transition | immediate / queued / end-of-tick | |
| StateB | StateA | Condition that causes transition | immediate / queued / end-of-tick | |
| StateB | StateC | Condition that causes transition | immediate / queued / end-of-tick | |
| StateC | *(terminal)* | — | — | Entity removed or archived |

**Entry Conditions:**
- ...

**Exit Conditions:**
- ...

**Illegal Transitions:**
| From | To | Reason |
|------|----|--------|
| ... | ... | ... |

**Cross-System Readers:**
| Reader System | Why It Reads | Reaction |
|---------------|-------------|----------|
| SYS-### Name | ... | ... |

**Invariants:**
- ...

-->

---

## Rules

1. **Every discrete state in the game must be registered here.** If code uses a state enum, it must appear in this document.
2. **Authority is mandatory.** Every state machine must name the single system that owns transitions. No shared ownership.
3. **Transitions are exhaustive.** If a state can reach another state, it must be in the table. Unlisted transitions are bugs.
4. **Invariants are testable.** Each invariant should be something code can verify at runtime.
5. **State names must match enums-and-statuses.md** for cross-system states. Single-system states may use local names but must still be registered here.
6. **Terminal states must be explicitly marked** with `*(terminal)*` in the Transitions To column.
