# Visual Design

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

Principles of visual composition and style for games — how to create readable, cohesive, and visually engaging experiences.

---

## Visual Hierarchy

- The player's eye should be drawn to the most important element first. Size, contrast, color, and motion all compete for attention — use them deliberately to rank elements by importance.
- Gameplay-critical elements (player character, enemies, interactables) need the strongest visual weight. If the player has to search for what matters, the hierarchy has failed.
- Background and decorative elements should recede. Lower contrast, reduced saturation, softer edges, and less detail push elements back in the visual stack.
- UI elements sit on top of the entire scene hierarchy. Health bars, minimaps, and prompts must read clearly against any background the game can produce.
- If everything is loud, nothing is. When every element demands equal attention, the player's eye has nowhere to land and gameplay-critical information gets buried.

## Readability

- The player must instantly distinguish three things: what can hurt me, what can I interact with, and where can I go. If any of these require study, readability is insufficient.
- Silhouette clarity is the first line of defense. Every important object should be recognizable by its outline alone, without relying on color or internal detail.
- Foreground, midground, and background should separate cleanly through contrast, value, and saturation differences. When these layers blend together, the scene becomes a flat, confusing image.
- Readability beats aesthetics when they conflict. A beautifully rendered scene that the player cannot parse is worse than a simple scene where everything is immediately clear.
- Test readability at the smallest screen size and lowest resolution you intend to support. Details that read fine on a development monitor may collapse into noise on a handheld or a stream thumbnail.

## Composition

- Rule of thirds applies to game cameras and UI layouts. Place key subjects at intersection points rather than dead center — it creates more dynamic, visually interesting framing.
- Leading lines guide the eye toward objectives. Roads, fences, light beams, architectural edges, and environmental geometry can all point the player where they need to look.
- Framing — using environment elements to surround or bracket the subject — draws attention to what matters. A doorway framing a distant objective, tree branches forming a natural vignette, or walls converging on a focal point all work.
- Negative space gives the eye a place to rest and makes focal points more powerful. A cluttered frame with no breathing room exhausts the viewer. Leave emptiness where emptiness serves the composition.
- Symmetry creates formality, stability, and grandeur. Asymmetry creates tension, dynamism, and unease. Choose the composition that matches the emotional intent of the scene.

## Contrast & Focal Points

- Contrast in any dimension — color, value, size, shape, motion, or level of detail — creates focal points. The element that is most different from its surroundings will be seen first.
- The player character should always be the highest-contrast element during gameplay. If the player loses track of their own character, no amount of visual polish compensates for that failure.
- Use contrast sparingly. When too many elements compete for attention through high contrast, no single focal point emerges and the scene becomes visually chaotic.
- Enemies and interactables need secondary contrast levels — strong enough to notice, but not stronger than the player character. Establish a clear contrast budget and allocate it by gameplay importance.
- Value contrast (light versus dark) is the most powerful and reliable tool. Color contrast and saturation contrast support it but cannot replace it. A scene should read correctly even when desaturated to grayscale.

## Style Consistency

- Pick an art style and enforce it everywhere. Every asset, effect, UI element, and animation should look like it belongs in the same game.
- Mixed styles — realistic characters in cartoon environments, pixel-art UI on 3D gameplay, hand-painted textures next to photographic ones — feel jarring unless the contrast is intentionally stylized and consistently applied.
- Line weight, color saturation, level of detail, and rendering approach should be consistent across all assets. A single character rendered at higher fidelity than everything else will look pasted in, not polished.
- A unified style at lower fidelity looks better than inconsistent style at higher fidelity. Cohesion creates a stronger aesthetic impression than raw quality.
- Document the style rules. Define acceptable color ranges, outline weights, texture densities, and material properties so that every contributor produces assets that fit together without constant art direction.

## Silhouette Design

- Players identify objects by shape before they register color or detail. Distinct silhouettes are the most efficient way to communicate identity at a glance.
- Character silhouettes should be recognizable at the smallest rendered size the game produces. If two characters look the same when small or distant, players will confuse them during gameplay.
- Weapons, tools, and pickups need unique outlines. A sword, an axe, and a spear should be distinguishable by shape alone. If pickups share similar blobby silhouettes, players cannot make quick decisions about what to grab.
- Avoid symmetrical, boxy silhouettes for important objects. Asymmetry, exaggerated proportions, and distinctive profiles — a long coat, oversized weapon, unusual headgear — create memorable and readable shapes.
- Test silhouettes by filling objects solid black. If you cannot tell them apart as flat black shapes against a white background, the silhouettes are too similar and need redesign.

## Motion & Animation as Communication

- Motion draws attention more powerfully than any static element. The human eye tracks movement involuntarily, making animation the most reliable tool for directing the player's focus.
- Use animation to communicate state. Idle, alert, attacking, damaged, and dying should each have visually distinct motion signatures so the player can read an entity's state without checking UI indicators.
- Anticipation frames — the wind-up before an action — give players time to read and react. A telegraph is not a courtesy; it is a core communication tool that makes combat feel fair and responsive.
- Follow-through and overshoot after an action create satisfying weight and physicality. A sword swing that stops dead at the contact point feels weightless. A swing that carries past and settles communicates force.
- Consistent animation timing builds player intuition. If similar enemies have similar wind-up durations, players can transfer learned timing between encounters. Inconsistent timing forces relearning and feels unreliable.

## Visual Noise & Clarity

- Too much visual detail creates noise that obscures gameplay. Dense textures, busy patterns, and excessive environmental decoration compete with the elements the player actually needs to see.
- Reduce detail in non-interactive areas. Background geometry, distant terrain, and decorative surfaces should be visually quieter than the gameplay space. The eye should settle on the playfield, not the wallpaper.
- Particle effects should enhance readability, not obscure it. An explosion that looks spectacular but hides the enemies inside it is actively harmful to gameplay. Scale, opacity, and duration of effects must respect the player's need to see.
- Screen shake, flash effects, and chromatic aberration need restraint. At high intensity or frequency they cause discomfort, trigger accessibility issues, and degrade readability. Always provide options to reduce or disable these effects.
- Post-processing — bloom, vignette, color grading, depth of field — should serve the mood and support the visual hierarchy. If an effect exists only to showcase the renderer rather than improve the player's experience, it is noise.
