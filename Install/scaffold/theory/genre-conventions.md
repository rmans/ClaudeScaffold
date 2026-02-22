# Genre Conventions

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

---

## Purpose

A practical reference of genre-specific conventions and player expectations. Use this document to inform design decisions, not to dictate them. When building a game that blends genres, identify which conventions apply and which to deliberately break (and document the reasoning in an ADR).

---

## 1. Platformer

- **Tight, responsive controls are non-negotiable.** Players expect sub-frame input latency. Variable jump height (short press vs. long press), coyote time (jump grace period after leaving a ledge), and input buffering are baseline expectations, not bonuses.
- **Collision must be readable and fair.** Hitboxes should match visual silhouettes closely. When a player dies, they should understand why. Ambiguous collision on platforms or hazards destroys trust quickly.
- **Level readability guides the player.** Foreground, background, and interactive elements must be visually distinct. The player should always know where they can stand, what will hurt them, and where to go next without a tutorial tooltip.
- **Checkpoints respect the player's time.** Checkpoint spacing should scale with difficulty. Punishing players with long replays after hard sections causes frustration, not challenge. Separate difficulty from repetition.
- **Common mistake: slippery or floaty movement.** Platformer players expect precise acceleration and deceleration curves. A character that slides past ledges or drifts after releasing the stick feels broken, regardless of how polished everything else is.
- **Good vs. great:** Good platformers have tight controls. Great platformers make movement itself the reward — the act of traversal is satisfying independent of level goals.

---

## 2. Action RPG

- **Character progression must feel meaningful.** Players expect visible power growth — stronger attacks, new abilities, better gear. If a level-up does not change how the player plays or what they can do, it fails.
- **Loot loops drive engagement.** The cycle of kill, loot, equip, repeat is the core motivation. Loot must be frequent enough to maintain excitement and varied enough to support different builds.
- **Build variety enables personal expression.** Players want to solve combat their way — melee, ranged, magic, hybrid. Funneling everyone into a single optimal build kills replayability.
- **Combat feel matters as much as combat math.** Hit impact, screen shake, enemy stagger, and sound design communicate damage better than floating numbers. If attacks feel weightless, stats do not save the game.
- **Common mistake: difficulty scaling that invalidates builds.** When late-game enemies are tuned exclusively around one stat or strategy, players who invested in alternative builds feel punished. Scale challenges, not hard counters.
- **Good vs. great:** Good action RPGs have satisfying loot and progression. Great action RPGs make every encounter a tactical decision where build choices create distinct play experiences.

---

## 3. Strategy (RTS / Turn-Based)

- **Information clarity is the foundation.** Players make decisions based on what they can see and understand. Unit stats, resource counts, tech trees, and threat indicators must be readable at a glance. Hiding critical information behind tooltips or sub-menus costs games.
- **Unit counters create strategic depth.** Rock-paper-scissors relationships (or more complex webs) force composition decisions. Without meaningful counters, the optimal strategy devolves to massing the strongest unit.
- **Resource management creates tension.** Players should face genuine trade-offs — spending on military vs. economy, expanding vs. defending. If resources are abundant enough to do everything, strategic choices disappear.
- **Map control rewards proactive play.** Vision, territory, and positioning should matter. Players who scout, expand, and control chokepoints should have an advantage over passive turtling (unless turtling is an intentional valid strategy).
- **Common mistake: information overload.** Showing every possible stat, modifier, and prediction simultaneously is just as bad as hiding information. Layer complexity — surface-level readability with drill-down detail.
- **Good vs. great:** Good strategy games present meaningful decisions. Great strategy games ensure that no two matches play out the same way because player decisions and map conditions create emergent scenarios.

---

## 4. Survival

- **Resource scarcity creates moment-to-moment tension.** Players should regularly face trade-offs: use this material now or save it, explore for more supplies or secure what they have. Abundant resources turn survival into inventory management.
- **Crafting must be intuitive and purposeful.** Every recipe should solve a problem the player recognizes. Crafting trees that require wiki lookups or trial-and-error guessing frustrate rather than engage.
- **Environmental threats provide pressure beyond combat.** Temperature, hunger, weather, day/night cycles, and terrain hazards force players to plan and adapt. Combat alone is an action game, not a survival game.
- **Risk of loss raises the stakes.** Whether through permadeath, item drop on death, or base raiding, the possibility of losing progress makes every decision matter. The severity should match the game's intended tone.
- **Common mistake: punishing early game, trivial late game.** Many survival games front-load difficulty when players have nothing and become trivially easy once a base is established. Threats should scale or evolve to maintain tension throughout.
- **Good vs. great:** Good survival games make players manage resources. Great survival games tell emergent stories — the blizzard that forced a desperate supply run, the base that barely survived the night.

---

## 5. Roguelike / Roguelite

- **Run variance keeps players returning.** Each run should feel distinct through randomized layouts, item pools, enemy encounters, and event sequences. If runs blend together, the format fails.
- **Meaningful choices define each run.** Players should make build-defining decisions regularly — which item to take, which path to follow, which upgrade to prioritize. Choices without consequence are not choices.
- **Meta-progression (roguelite) must not replace skill.** Permanent unlocks should expand options (new items, characters, starting conditions), not simply add stat bonuses that trivialize the game over time. The player should still need to play well.
- **Synergy discovery is the deepest hook.** When players realize two items or abilities combine in powerful ways they had not anticipated, that moment of discovery is the genre's greatest reward. Design item pools with combinatorial interactions in mind.
- **Common mistake: run-ending bad luck.** Pure randomness without safeguards (pity mechanics, guaranteed minimums, reroll options) can produce unwinnable runs. Players accept dying to their own mistakes; dying to an impossible seed feels unfair.
- **Good vs. great:** Good roguelikes generate variety. Great roguelikes make every death a lesson — the player returns not just for a new seed but because they have a new strategy to try.

---

## 6. Puzzle

- **Rule clarity is paramount.** Players must understand the mechanics before they can solve puzzles. If a player fails because they did not understand the rules (rather than failing to apply them), the puzzle is broken, not hard.
- **Difficulty escalation should be deliberate.** Introduce one concept at a time. Let the player master a mechanic in isolation before combining it with others. Difficulty spikes alienate players; difficulty curves retain them.
- **The "aha" moment is the reward.** Puzzles succeed when the player feels clever for solving them. The solution should feel discovered, not stumbled upon. If the player solves it but does not understand why it worked, the puzzle failed.
- **Solvability must be guaranteed.** Every puzzle in a required path must be solvable with the information and tools available. No pixel hunting, no hidden interactions, no solutions that depend on outside knowledge the game never provides.
- **Common mistake: confusing difficulty with obscurity.** Hard puzzles have complex logic. Bad puzzles have hidden information. Making the player click every pixel or try every combination is not puzzle design — it is a guessing game.
- **Good vs. great:** Good puzzle games challenge the player. Great puzzle games teach players to think in new ways — the mechanics become a language the player learns to speak fluently.

---

## 7. Simulation / Management

- **Systems transparency builds trust.** Players need to understand cause and effect. When a system produces an unexpected outcome, the player should be able to trace why. Opaque systems feel arbitrary; transparent systems feel fair.
- **Cascading consequences create depth.** The best simulation moments happen when one decision ripples through interconnected systems — a staffing change affects production, which affects revenue, which affects expansion plans. Isolated systems feel shallow.
- **Optimization loops sustain engagement.** Players return to improve — higher efficiency, better throughput, more elegant solutions. The game must support and reward iterative refinement.
- **Pacing control belongs to the player.** Speed controls (pause, fast-forward, slow-motion) and the ability to plan without time pressure are essential. Forcing real-time decisions in a game about deliberate planning frustrates the audience.
- **Common mistake: failing to communicate system interactions.** When systems are interconnected but the connections are not visible to the player, decisions feel random. Provide feedback loops — graphs, overlays, notifications — that show how systems relate.
- **Good vs. great:** Good management games let players build systems. Great management games let players express themselves — two players solving the same scenario produce fundamentally different solutions.

---

## 8. FPS / Shooter

- **Weapon feel is everything.** Recoil patterns, fire rates, reload animations, and muzzle effects must make every weapon feel distinct and satisfying. If guns feel like pointing and clicking, the core loop fails.
- **Time-to-kill (TTK) sets the game's identity.** Low TTK (tactical shooters) emphasizes positioning and awareness. High TTK (arena shooters) emphasizes tracking and movement. Mismatching TTK with the rest of the design creates a confused experience.
- **Movement fluidity keeps players engaged.** Whether the game uses sprint-slide-mantle or simple strafe-jump, movement must feel responsive and smooth. Clunky movement is unforgivable in a genre where milliseconds matter.
- **Map flow dictates encounter quality.** Maps need clear lanes, sight lines, cover placement, and rotation paths. Players should be able to read a map intuitively — where enemies are likely to be, where the power positions are, and how to flank.
- **Common mistake: poor audio-visual hit feedback.** Players need immediate, unambiguous confirmation that their shots connected — hit markers, blood splatter, damage numbers, audio cues, or some combination. Without feedback, even accurate shooting feels unreliable.
- **Good vs. great:** Good shooters have tight gunplay. Great shooters create skill expression through the intersection of movement, aim, positioning, and game sense — the gun is only one element.

---

## 9. Adventure / Narrative

- **Story pacing must respect gameplay rhythm.** Long cutscenes should not interrupt active gameplay sequences. Alternate between exposition and agency — give the player something to do between story beats.
- **Dialogue choices should feel meaningful.** If choices do not affect outcomes, relationships, or at minimum the tone of a response, players will stop reading and start clicking through. Flag which choices matter and which are flavor, or make all of them matter.
- **Environmental storytelling rewards exploration.** Notes, environmental details, overheard conversations, and world state changes tell stories without interrupting gameplay. Players who explore should learn more about the world than players who rush.
- **Journal and quest tracking prevent frustration.** Players who return after a break must be able to understand what they were doing and where to go. A clear quest log, objective markers (optional), and conversation recaps are essential quality-of-life features.
- **Common mistake: ludonarrative dissonance.** When gameplay mechanics contradict the story the game is telling (e.g., a narrative about mercy in a game that rewards killing), players lose immersion. Align mechanics with theme.
- **Good vs. great:** Good adventure games tell a compelling story. Great adventure games make the player feel like the story is theirs — their choices, their pace, their interpretation.

---

## 10. Sandbox / Open World

- **Player-driven goals sustain the experience.** Without authored quest chains driving every moment, the game must provide tools, systems, and objectives that let players set and pursue their own goals. Aimless sandboxes lose players; toolbox sandboxes retain them.
- **Emergent gameplay comes from systemic interactions.** When fire spreads to grass, which startles animals, which alerts guards, that chain of consequences is more memorable than any scripted event. Design systems that interact with each other.
- **Discovery density keeps exploration rewarding.** Open worlds need a consistent density of interesting things — loot, encounters, environmental puzzles, lore, vistas, secrets. Large empty spaces should be intentional (pacing, atmosphere), not a sign of thin content.
- **Fast travel vs. exploration is a design tension.** Players need efficient traversal for repeated trips, but fast travel that is too convenient removes the journey entirely. Solutions include unlockable fast travel, travel with trade-offs, or making traversal itself engaging.
- **Common mistake: content repetition masked by distance.** Scattering identical outposts, collectibles, or encounters across a large map does not create meaningful content. Players recognize copy-paste. Fewer, more distinct locations outperform many identical ones.
- **Good vs. great:** Good open worlds are large and filled with content. Great open worlds make the player feel like every direction is a possibility — that the next horizon holds something they have not seen before.
