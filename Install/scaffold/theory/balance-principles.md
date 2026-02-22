# Balance Principles

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

---

## Purpose

Principles for game balance — how to tune difficulty, economies, and systems for satisfying gameplay.

This document carries no authority. It informs design decisions but never dictates them. If a principle here influences a design change, that change should be captured in an ADR, which is what carries the actual authority.

---

## 1. When to Balance

- Do not balance before the mechanics are fun. If the core interaction is not enjoyable at placeholder values, no amount of number tuning will save it. Fun first, numbers second.
- Balance is an ongoing process, not a one-time task. Every new feature, content addition, or system change shifts the balance landscape. Budget time for rebalancing after every major change.
- Prototype with deliberately extreme values — make things too powerful, too fast, too cheap — so the mechanical interactions are visible and testable. Placeholder values should make the system's behavior obvious, not realistic.
- Tune based on playtesting data, not theory. A spreadsheet that proves balance mathematically is worthless if players do not experience it that way.
- Premature optimization of numbers is one of the most common time sinks in game development. Tuning values for a system that will be redesigned next week is wasted effort. Wait until the mechanics are stable before investing in precision balance.

## 2. Difficulty Curves

- Difficulty should escalate with player skill, not just time played. A player who has mastered the controls in hour two should face meaningfully different challenges than a player still learning in hour five, regardless of how much calendar time has passed.
- Spikes are fine if they teach — plateaus are boring. A sudden difficulty increase forces the player to engage with a mechanic they have been coasting on. A long flat stretch where nothing changes breeds disengagement.
- Each difficulty tier should introduce a new dimension, not just bigger numbers. Enemies that dodge, limited resources, time pressure, environmental hazards — these create qualitatively different challenges. Doubling enemy health creates quantitatively more tedium.
- Provide breathing room after difficulty spikes. A hard boss followed by a calm exploration section lets the player recover and feel accomplished. A hard boss followed by another hard boss followed by a platforming gauntlet causes fatigue and frustration.
- Map your difficulty curve explicitly. Plot expected challenge level against progression and look for unintended plateaus, double-spikes, or sections where the curve goes backward. Intentional design beats accidental difficulty.

## 3. Economy Tuning

- Every resource needs sources (where it comes from) and sinks (where it goes). If sources outpace sinks, inflation happens and the currency loses meaning. If sinks outpace sources, players feel starved and stop engaging with the system.
- Test economies at 10x and 0.1x normal play speed to find breaking points. A player who grinds aggressively or one who barely collects anything will both stress the economy in ways a typical player will not. Design for the extremes, not the average.
- Multiple currencies should serve different decision spaces. If gold buys gear and gems buy cosmetics, the player makes two independent decisions. If gold and gems both buy gear, one will always be more efficient and the other becomes dead weight.
- Track the ratio of earning rate to spending rate over the full game arc. Early generosity followed by late-game tightening teaches resource value gradually. Early scarcity followed by late-game abundance devalues the whole system retroactively.
- Price items relative to each other, not just to earning rates. Players compare options side by side. If a sword costs 100 and a shield costs 500, the player infers the shield is five times more valuable — make sure that inference is correct.

## 4. The Knobs Principle

- Design systems with exposed tuning parameters from the start. Every value that affects game feel — damage, speed, cooldowns, spawn rates, drop chances — should live in data, not in code.
- Balance changes should require data edits, not code changes. If adjusting enemy health means modifying a script, recompiling, and redeploying, balance iterations will be slow and rare. If it means changing a number in a resource file, iterations will be fast and frequent.
- Group related parameters so they can be tuned together. Damage, attack speed, and range form a coherent cluster for a weapon. Scattering them across unrelated files makes holistic tuning impractical.
- Name parameters clearly and descriptively. Future-you needs to understand what `factor_2b` means six months from now. `enemy_base_health_multiplier` is longer but saves hours of archaeology.
- Document the expected range and intent of each parameter. A comment that says "0.5 = half speed, 2.0 = double speed, tested safe between 0.1 and 5.0" prevents someone from setting it to 1000 and filing a bug report.
- Record balance parameters in `reference/balance-params.md` once the mechanics they govern are stable. This creates a single source of truth for tuning values across the project.

## 5. Dominant Strategies

- If one strategy always wins regardless of context, the game has a balance problem. Players will find the optimal path and ignore everything else, reducing a rich system to a single rote execution.
- Rock-paper-scissors relationships create interesting choices. When strategy A beats B, B beats C, and C beats A, the player must read the situation and adapt rather than defaulting to one approach.
- Perfect balance is often boring — slight imbalances create metagames. If every weapon is mathematically identical, none feels special. Small asymmetries give players reasons to explore, compare, and develop preferences.
- Extreme imbalance kills engagement. A slight edge encourages experimentation; a dominant option that outperforms all alternatives by 3x makes every other option feel like a trap. The line between "interesting asymmetry" and "broken balance" is narrower than it appears.
- Watch for emergent dominant strategies that players discover but designers did not anticipate. Playtesters and communities will find combinations, exploits, and optimization paths that internal testing missed. Monitor post-release behavior, not just pre-release spreadsheets.

## 6. Feedback Loops in Balance

- Positive feedback loops — the rich get richer — create snowball effects. A player who gains an early advantage becomes increasingly hard to catch. This produces exciting finishes when the snowball is rolling toward victory but miserable experiences when one mistake cascades into an unrecoverable deficit.
- Negative feedback loops — rubber banding — keep games close. The leading player faces stiffer resistance or the trailing player receives assistance. This prevents blowouts but can feel punishing if the player who earned the lead feels it being taken away.
- Both types have valid uses. Positive loops within a single encounter create satisfying momentum. Negative loops across a session keep overall tension alive. The key is choosing which type serves each layer of the experience.
- Identify every feedback loop in your game and determine whether it is intentional. Unintentional positive loops are the most common source of balance complaints — they feel unfair because the advantage compounds invisibly.
- Design circuit breakers for runaway loops. Caps on stacking bonuses, diminishing returns on consecutive advantages, or catch-up mechanics that activate at extreme gaps all prevent loops from destroying the experience at the margins.

## 7. Testing and Metrics

- Win rates, completion rates, and time-to-complete are your primary balance signals. These are objective, quantifiable, and comparable across play sessions. Gut feeling is a starting point, not a conclusion.
- If a level has a 5% completion rate, it is too hard or broken. If an item has a 95% pick rate, it is overpowered. Extreme statistical outliers almost always indicate a balance problem, not a player skill problem.
- Playtest with different skill levels — designer skill is not representative. The person who built the system knows every interaction, every shortcut, and every edge case. They are the worst possible test subject for difficulty assessment.
- Track the full distribution, not just averages. An average completion time of 10 minutes might mean everyone finishes in 10 minutes, or it might mean half finish in 2 minutes and half give up at 18. These are very different problems requiring very different solutions.
- Establish balance targets before testing, not after. Decide in advance what win rate, completion rate, or time-to-complete you consider acceptable. Without a target, every result looks fine and no action is taken.

## 8. Difficulty Options

- Difficulty settings should change the experience, not just multiply health and damage. Reducing enemy health by 50% on easy mode makes combat shorter but not easier to understand. Reducing enemy aggression, adding more healing resources, or providing clearer telegraphs makes the game more approachable.
- Easy mode should still be fun and teach the game's systems. If easy mode lets the player ignore mechanics entirely, they learn nothing and are unprepared for any increase in challenge. The goal is reduced punishment for mistakes, not removal of the need to engage.
- Hard mode should demand mastery, not patience. Tripling enemy health makes fights longer, not harder. Faster enemy attacks, more complex patterns, fewer resources, and tighter execution windows demand genuine skill improvement.
- Consider adaptive difficulty — invisible or visible — as an alternative to fixed tiers. Systems that subtly adjust based on player performance avoid the binary choice of "too easy" or "too hard" and can maintain flow state more reliably than static settings.
- Never shame players for choosing easy mode. Derisive difficulty names, locked content, or condescending messaging punish players for knowing their own preferences. Every difficulty setting is a valid way to play.
