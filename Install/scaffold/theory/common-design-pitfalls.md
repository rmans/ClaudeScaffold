# Common Design Pitfalls

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

---

## Purpose

A reference catalog of recurring game design anti-patterns. Each entry describes the pitfall, how to recognize it early, and practical mitigations. Consult this when evaluating feature proposals, reviewing system designs, or conducting design retrospectives.

This document carries no authority. It informs decisions but never dictates them. If a pitfall identified here influences a design change, that change should be captured in an ADR, which is what carries the actual authority.

---

## 1. Feature Creep

Adding features that do not serve the core loop.

- **What it is.** Features accumulate because they sound interesting in isolation, not because they reinforce what the game is about. The phrase "wouldn't it be cool if..." is the usual entry point.
- **How to recognize it.** A proposed feature cannot be traced back to a design pillar. The feature list grows between milestones without corresponding cuts. Systems exist that no other system depends on or interacts with meaningfully.
- **How to avoid it.** Every feature must trace to a design pillar defined in the design doc. If it does not connect, it does not ship. Maintain a cut list alongside the feature list — moving something to the cut list is a decision, not a failure.

## 2. Scope Blindness

Underestimating the total work a feature requires.

- **What it is.** The visible part of a feature (the core mechanic) represents a fraction of the real work. The iceberg below the surface includes UI, edge cases, save/load integration, accessibility, polish, and testing. Teams plan for the tip and discover the rest mid-implementation.
- **How to recognize it.** Estimates consistently miss by 2x or more. Features are "almost done" for weeks. Edge cases surface late and cause cascading rework.
- **How to avoid it.** Prototype the hardest part first, not the most visible part. Break features into vertical slices that include UI and integration from the start. When estimating, explicitly list the non-obvious work: error states, data persistence, input edge cases, undo behavior.

## 3. Complexity Debt

Systems that interact in ways nobody can predict or debug.

- **What it is.** Every new system multiplies the number of potential interactions. Two systems have one interaction path. Five systems have ten. Ten systems have forty-five. When interactions are implicit rather than explicit, the game develops emergent bugs that no single system owner can diagnose.
- **How to recognize it.** Bugs require investigating three or more systems to understand. Changes to one system produce unexpected behavior in unrelated systems. Developers are afraid to modify existing systems.
- **How to avoid it.** Define explicit interfaces between systems (see `design/interfaces.md`). Enforce strict data authority — one writer per variable (see `design/authority.md`). Prefer systems that communicate through well-defined signals over systems that read each other's internal state.

## 4. Tutorial Crutch

Designing unintuitive systems and then explaining them with tutorials instead of fixing the design.

- **What it is.** When a mechanic is confusing, the instinct is to add a tutorial popup, tooltip, or walkthrough. This treats the symptom (player confusion) rather than the cause (unclear design). Players skip tutorials, forget tutorials, and resent tutorials.
- **How to recognize it.** Playtesters consistently misunderstand a mechanic despite tutorials being present. The tutorial for a single system requires multiple steps or screens. Removing the tutorial would make the feature unusable.
- **How to avoid it.** Design for discoverability first. Use progressive disclosure — introduce one concept at a time through gameplay, not text. If a mechanic needs a paragraph of explanation, simplify the mechanic. Reserve tutorials for genuinely complex strategic depth, not for basic interactions.

## 5. False Choice

Presenting options where one is obviously better or the choice does not matter.

- **What it is.** The player is offered a decision, but the decision is meaningless. Either one option dominates (no real trade-off), the options are cosmetically different but functionally identical, or the "wrong" choice is a trap that punishes the player for not reading a wiki.
- **How to recognize it.** Playtesters always pick the same option. Players feel no tension when choosing. Online guides have a single "correct" build or path. Options differ in magnitude but not in kind (e.g., +10% damage vs. +5% damage).
- **How to avoid it.** Every option should involve a genuine trade-off — gaining something valuable while giving up something else that is also valuable. Test choices by asking: "Can I construct a scenario where each option is the best pick?" If not, the choice is false.

## 6. Kitchen Sink Design

Trying to appeal to every player type simultaneously.

- **What it is.** The game attempts to include combat, crafting, base building, story, multiplayer, and exploration — all at equal depth — because each feature might attract a different audience. The result is a game that does many things adequately and nothing memorably.
- **How to recognize it.** The elevator pitch requires more than two sentences. Features compete for development time with no clear priority. Playtesters enjoy different parts of the game but nobody loves the whole thing.
- **How to avoid it.** Pick your audience and commit. Define the core loop first and treat everything else as support for that loop. It is better to be a sharp knife than a dull Swiss Army knife. If a feature does not make the core loop better, it is a candidate for the cut list.

## 7. Premature Balance

Tuning numbers before the underlying mechanics are fun.

- **What it is.** Time is spent adjusting damage values, cooldown timers, and resource costs while the mechanics themselves are still in flux. When the mechanics change (and they will), all the balance work is invalidated. Worse, balanced-but-unfun mechanics feel "done" and resist redesign.
- **How to recognize it.** Spreadsheets exist for systems that have not been playtested. Balance discussions dominate meetings for features that are not yet fun in their simplest form. Designers resist mechanical changes because "the numbers are already tuned."
- **How to avoid it.** Get the feel right first. Use placeholder values that are intentionally extreme — make things too powerful, too fast, too cheap — so the mechanical interactions are visible and testable. Balance is a polish activity, not a design activity. Record balance parameters in `reference/balance-params.md` only after the mechanics are stable.

## 8. Content Treadmill

Relying on raw content volume instead of systemic depth to create variety.

- **What it is.** Each hour of gameplay requires a proportional amount of hand-authored content — unique levels, scripted encounters, one-off dialogue. Production scales linearly with game length, which is unsustainable. When the content runs out, the game ends abruptly.
- **How to recognize it.** Extending the game by 20% requires 20% more production work. Playtesters exhaust content faster than the team can produce it. Replayability is low because encounters play out identically each time.
- **How to avoid it.** Invest in systems that generate variety through interaction rather than authorship. Combine a smaller set of well-designed components (enemies, items, terrain, modifiers) that produce different outcomes in different combinations. Hand-authored content should set the stage; systemic depth should fill it.

## 9. Invisible Walls

Arbitrary restrictions that break the player's mental model of the world.

- **What it is.** The player encounters a limitation that has no in-world justification: a waist-high fence that cannot be climbed, a locked door with no explanation, a powerful ability that inexplicably fails in a specific context. These moments shatter immersion and erode trust in the game's rules.
- **How to recognize it.** Playtesters ask "why can't I do this?" and the honest answer is "because we didn't implement it" or "because it would break the level." Restrictions feel punitive rather than natural. Players attempt workarounds that feel like they should succeed but do not.
- **How to avoid it.** Make constraints consistent with the world's internal logic. If the player cannot go somewhere, give a visible, believable reason. If an ability has limitations, communicate them through the fiction, not through an error message. When a restriction is purely mechanical, at minimum acknowledge it in the game's own language rather than silently blocking the action.

## 10. Second System Effect

The sequel or v2 that tries to fix everything and add everything, losing what worked.

- **What it is.** After a successful first version, the next version attempts to address every criticism, add every deferred feature, and rearchitect every system. The result is bloated, unfocused, and often worse than the original because the qualities that made the original work were implicit and unprotected.
- **How to recognize it.** The v2 feature list is dramatically larger than v1's. Core systems from v1 are being rewritten without a clear problem statement. The team cannot articulate which specific qualities of v1 must be preserved. Design discussions focus on what to add rather than what to protect.
- **How to avoid it.** Before starting v2, explicitly identify what works in v1 and mark it as protected. Separate "fix what is broken" from "add what is missing" — these are different workstreams with different risk profiles. Apply the same scope discipline to v2 that made v1 succeed. New features must still trace to design pillars, not to a wishlist.
