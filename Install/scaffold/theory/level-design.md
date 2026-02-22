# Level Design

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

Principles for designing game spaces — how to guide players, teach mechanics, and create memorable environments. This document is a reference for reviewing level layouts and spatial design. It informs decisions but never dictates them — cite specific principles in ADRs when they influence a choice.

---

## Teaching Through Space

- Introduce every new mechanic in a safe environment before testing the player on it. The first encounter with a hazard should be observable — the player sees it kill an NPC or trigger harmlessly — before they must deal with it themselves.
- Use "training wheels" versions of challenges before the real thing. Wide platforms before narrow ones. Slow-moving hazards before fast ones. A single enemy before a group. The player should feel competent before being pressured.
- Every new mechanic needs a dedicated teaching moment — a space built specifically to let the player experiment without punishment. If the mechanic is important enough to exist, it is important enough to teach properly.
- Combine previously taught mechanics only after each has been learned in isolation. The player should recognize the individual parts before encountering them together.
- If a mechanic can kill the player, the teaching space should demonstrate the danger at a distance first. Seeing a pit trap spring before walking over one builds understanding without frustration.

## Spatial Pacing

- Alternate between tight, intense spaces and open, calm spaces. Corridors create tension and focus. Open areas create relief, awe, or anticipation. Neither works without the other.
- Verticality adds drama and navigation interest. Looking up at where you are going or down at where you have been creates a sense of journey. Flat levels feel monotonous over time.
- Dead-end paths must contain rewards — items, lore, vistas, or secrets. An empty dead end teaches the player to stop exploring. Never waste the player's time with a path that leads to nothing.
- Vary the rhythm of encounters. Three combat rooms in a row feel like a grind. A combat room, then a puzzle, then a vista, then combat again keeps engagement high.
- Give the player breathing room after peak-intensity moments. A boss fight should be followed by a calm transition, not another gauntlet. Recovery spaces let tension reset so the next peak has impact.

## Guiding the Player

- Use light, color, contrast, and motion to draw the eye toward the critical path. A bright doorway at the end of a dark corridor, a moving element amid static scenery, a unique color against a neutral palette — these guide without explicit markers.
- Landmarks help orientation in open spaces. A distinctive tower, a mountain on the horizon, a unique tree — anything the player can see from multiple angles and use as a reference point. Without landmarks, open spaces become disorienting.
- Breadcrumb rewards — collectibles, minor pickups, environmental details — guide the player along the intended route without arrows or waypoints. The player follows them because they want to, not because they are told to.
- The camera should reveal the path. Frame important routes and objectives within the player's natural viewing angle. Do not fight the player's perspective — if the critical path is behind them or above their default look direction, they will miss it.
- Composition matters. Place the destination in the visual center of key vistas. Use leading lines — roads, fences, rivers, light beams — to point the player's eye where it needs to go.

## Challenge Placement

- Escalate difficulty within each level in clear steps, with reset points between sections. The player should feel the ramp but never feel ambushed by a sudden spike.
- Place checkpoints before challenges, not after. Dying and then replaying a long safe section to reach the challenge again is punishment without purpose. The checkpoint should put the player right back at the attempt.
- Group enemy encounters by theme: introduce a new enemy type alone, then combine it with familiar enemies, then test mastery with a complex encounter mixing several types. This introduce-combine-master pattern is reliable because it respects learning curves.
- Boss arenas should teach the player how to win through their geometry. Pillars for cover against ranged attacks, elevated platforms for aerial bosses, environmental hazards that can be turned against the enemy. The space is part of the fight design, not just a flat room.
- Difficulty should reset partially at the start of each new area or level. The opening encounters of a new zone should be manageable, establishing the new baseline before ramping again. Continuous unbroken escalation across the entire game exhausts players.

## Exploration & Secrets

- Reward curiosity. Players who leave the critical path should find something worthwhile — a useful item, a lore fragment, a shortcut, a vista. The reward does not need to be powerful, but it must exist.
- Visible-but-unreachable areas create goals. A treasure chest behind a locked door, a ledge just out of jump range, a path blocked by an obstacle the player cannot yet remove — these create motivation to return and a sense of satisfaction when the player finally reaches them.
- Secret areas should be discoverable through observation, not through exhaustively checking every wall. Visual cues — a cracked texture, an unusual shadow, a draft of particles, a subtle difference in geometry — signal that something is hidden. Players should feel clever for finding secrets, not lucky.
- Backtracking should reveal new content. If the player must return through a previously explored area, change it — new enemies, opened shortcuts, altered lighting, environmental shifts. Retreading identical content feels like wasted time.
- Layer secret complexity. Surface-level secrets are found by most players who explore casually. Deep secrets require combining knowledge from multiple areas or mechanics. This gives both casual explorers and completionists something to find.

## Flow & Navigation

- Players should rarely feel lost unless disorientation is an intentional design goal. If the player stops moving to figure out where to go, the level has a wayfinding problem.
- One-way gates and shortcuts create efficient loops. A locked door that opens from the other side, a ladder that drops down, a bridge that extends — these let the player traverse the level efficiently on return trips without cheapening the initial exploration.
- Minimize backtracking without purpose. If a quest sends the player back through cleared content with nothing new to encounter, the quest structure needs revision, not the level.
- Fast travel is an admission that traversal is not fun enough. Before adding fast travel, ask whether the traversal itself can be made engaging through encounters, environmental variety, or movement mechanics. Fix the journey before skipping it.
- Critical paths should be the most natural route through a space. If players consistently miss the intended path and wander into optional areas first, the spatial hierarchy is wrong. The main route should feel like the obvious choice; side paths should feel like deliberate detours.

## Environmental Storytelling

- Levels are narrative spaces. Every room, corridor, and vista communicates something about the world. Object placement, lighting shifts, and architectural details tell stories without a single line of dialogue.
- Before/after contrasts communicate history powerfully. A pristine room adjacent to a destroyed one. A well-maintained path that gradually deteriorates. A thriving market next to an abandoned one. The contrast does the narrative work.
- Every area should feel like it had a purpose before the player arrived. A kitchen should have cooking implements. A guard post should have sight lines to the approach. A library should have shelves. Spaces that feel functional feel real; spaces that feel like game geometry feel hollow.
- Use environmental details to foreshadow. Claw marks on walls before a beast encounter. Increasing numbers of warning signs before a hazard zone. Abandoned equipment from previous failed expeditions before a difficult section. The environment should prepare the player emotionally.
- Restraint is essential. Not every room needs a tragic story told through scattered objects. Some spaces should simply be spaces. Overusing environmental storytelling dilutes the moments that matter.

## Scale & Proportion

- Human-scale references help players judge distance and size. Doors, furniture, vehicles, trees, and figures give the player an intuitive sense of how large a space is. Without these references, scale becomes ambiguous.
- Exaggerated scale creates spectacle. Massive doors, towering structures, impossibly deep chasms — these work because the player has already internalized normal scale from human-referenced spaces. The contrast is what creates awe.
- Consistent scale rules prevent disorientation. If doors are 3 meters tall in one building, they should be 3 meters tall in similar buildings. Breaking scale consistency without reason makes the world feel unreliable.
- Small spaces feel intimate, tense, and dangerous. Large spaces feel epic, exposed, and contemplative. Use scale deliberately to evoke the intended emotional response for each area.
- Transition spaces between different scales help the player adjust. Moving from a cramped tunnel into a vast cavern is more impactful with a brief intermediate space — a widening passage, a ledge overlooking the cavern — than an abrupt cut from tight to enormous.
