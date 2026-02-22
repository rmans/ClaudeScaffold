# Game Design Principles

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

This document collects foundational game design principles for reference during design and implementation. It carries no authority. Cite it in ADRs when it informs a decision, but the ADR is what governs.

---

## Player Agency

- A choice is only meaningful if the player can predict at least some of its consequences. Blind choices are coin flips, not decisions.
- False choices — options that all lead to the same outcome — actively erode trust. If the player notices, they stop engaging.
- Agency scales with consequence visibility. Show the player what changed because of what they did. Delayed consequences need eventual payoff or the player forgets they chose anything.
- Constraint creates agency. A player with unlimited options feels paralyzed. A player choosing between three meaningful options feels empowered.
- Reversible choices feel low-stakes. Permanent or costly-to-reverse choices carry weight. Use irreversibility deliberately, not accidentally.

## Feedback Loops

- A **positive feedback loop** amplifies advantage: the winning player gets stronger, making them win more. Left unchecked, this creates runaway leaders and disengaged losers.
- A **negative feedback loop** dampens advantage: the leading player faces harder challenges or the trailing player gets assistance. This keeps sessions competitive but can feel punishing if too aggressive.
- The best systems layer both: positive loops within a single encounter for moment-to-moment satisfaction, negative loops across the session to keep overall tension alive.
- Every feedback loop should have a cap or circuit breaker. Uncapped loops — positive or negative — eventually break the experience.
- Test loops at extremes. A loop that feels fine in the middle of a run may be catastrophic when a player is far ahead or far behind.

## Game Feel / Juice

- Input responsiveness is non-negotiable. The gap between button press and on-screen reaction must be imperceptible. If the player feels lag, no amount of polish saves it.
- Screen shake, hit pause (freeze frames), and particle bursts convert a mechanical event into an emotional one. A sword swing that displaces the camera by 3 pixels feels powerful; the same swing without it feels limp.
- Animation follow-through — the overshoot and settle after an action completes — sells weight and physicality. Without it, movement feels robotic.
- Sound confirms action. A satisfying impact sound on hit, a crisp click on menu selection, a low thud on landing. Remove all sound from a game and notice how hollow every interaction becomes.
- Juice is multiplicative, not additive. One effect does little. Screen shake plus particles plus sound plus a brief time-scale dip together create impact far greater than the sum of the parts.
- Restraint matters. If everything is juicy, nothing stands out. Reserve the heaviest effects for the most important moments.

## Pacing

- Tension without release is exhausting. Release without tension is boring. Alternate between the two deliberately.
- After every intensity peak, give the player a valley: a safe room, a cutscene, a shopping phase, a walk through calm territory. Recovery time lets the player process what just happened.
- Difficulty curves should generally ramp in steps, not linearly. Introduce a new challenge, give the player time to master it, then introduce the next. Flat stretches between steps are where learning solidifies.
- Flow state requires the challenge to stay just ahead of the player's skill. Too easy produces boredom, too hard produces anxiety. Both break engagement.
- Pacing applies to information as well as action. Revealing too many systems at once overwhelms. Stagger introductions so each new mechanic gets its own spotlight.

## Depth vs Complexity

- Depth is the number of meaningful outcomes that emerge from a system. Complexity is the number of rules the player must learn. Maximize the ratio of depth to complexity.
- Simple rules that interact produce emergent behavior. Chess has six piece types and creates near-infinite strategic depth. Adding a seventh piece type would add complexity but not necessarily depth.
- Every rule the player must remember is a cost. Justify each rule by the depth it creates. If a rule adds complexity without adding interesting decisions, cut it.
- "Easy to learn, hard to master" is the target. The first hour should feel intuitive. The hundredth hour should still surface new strategies.
- When in doubt, remove a mechanic and see if the game is worse. Often it is not.

## Risk vs Reward

- Players naturally seek the highest reward for the lowest risk. If a safe strategy dominates, they will use it every time and the risky option becomes decorative.
- Proportional rewards drive engagement: higher risk must yield meaningfully higher reward, but not so much that the safe path feels pointless.
- The most compelling risks involve partial information — the player can estimate odds but not guarantee outcomes. Pure randomness is not risk; it is lottery.
- Stakes must be real but recoverable. Losing everything to a single bad gamble feels unfair. Losing meaningful but replaceable progress feels dramatic.
- Make the risky option visible and tempting. If players do not even notice the high-risk path exists, the system is not doing its job.

## Economy Design

- Every economy needs **sources** (where currency enters) and **sinks** (where currency exits). If sources outpace sinks, inflation makes currency meaningless. If sinks outpace sources, scarcity stalls progression.
- Multiple currencies prevent a single resource from doing too many jobs. A currency that buys both consumables and permanent upgrades will always be spent on the permanent upgrade.
- Scarcity drives value and decision-making. If a resource is always abundant, spending it is not a choice. If it is always scarce, the player hoards it and never engages with the system.
- Test the economy at both ends: a new player with nothing and a veteran player with everything. Both should have meaningful spending decisions.
- Faucets (sources) should be tied to player actions — rewards for playing well. Drains (sinks) should be tied to player choices — optional expenditures that feel worth it.
- An economy that feels generous early and tightens later teaches the player to value resources gradually rather than punishing them upfront.

## Progression Systems

- The best progression systems teach. Each unlock introduces a new tool, and the content that follows is designed for the player to learn that tool. Unlocks without purpose are clutter.
- Skill-based progression (player gets better) is more durable than time-based progression (character gets stronger). The ideal system uses both: the character grows, and the challenges grow to match, so player skill remains the deciding factor.
- Power curves should have visible plateaus where the player consolidates. A constant upward slope of new abilities overwhelms and devalues each individual gain.
- Front-load the feeling of progress. Early unlocks should come quickly to build momentum. Later unlocks can take longer because the player is already invested.
- Every unlock the player never uses is a design failure. If the majority of players ignore an upgrade path, it is either poorly communicated, underpowered, or unnecessary.

## Information Design

- Show what the player needs to act on. Hide what would overwhelm them without improving their decisions.
- Perfect information (all data visible) favors strategic planning. Imperfect information (some data hidden) favors adaptability and surprise. Choose based on the experience you want.
- UI is communication, not decoration. Every element should answer a question the player is asking: "How much health do I have? What can I afford? Where do I go next?"
- Clarity beats aesthetics every time. A beautiful health bar that is hard to read in combat is worse than an ugly one that is instantly legible.
- Progressive disclosure works for UI just as it does for mechanics. Show the core HUD elements first. Reveal advanced information (detailed stats, sub-menus, tooltips) as the player needs it.
- Consistency reduces cognitive load. If red means danger in one context, it should not mean "active ability" in another.

## The 80/20 Rule

- Roughly 80% of players will engage with roughly 20% of the game's content. That 20% is the critical path. Design, polish, and test the critical path first.
- Optional content is valuable but should not drain resources from the core experience. A game with a brilliant side quest and a broken main quest has failed.
- Edge cases in mechanics, economies, and progression exist. Acknowledge them, but do not spend disproportionate time solving problems that affect a fraction of a percent of players.
- When prioritizing work, ask: "How many players will experience this, and how much will it affect their experience?" Multiply frequency by impact to rank effort.
- Perfecting a feature no one uses costs the same as perfecting a feature everyone uses. Spend accordingly.
