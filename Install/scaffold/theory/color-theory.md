# Color Theory

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

Fundamentals of color theory applied to games — how color communicates meaning, directs attention, and creates mood.

---

## Color Harmony

- Complementary colors (opposites on the wheel) create high contrast and energy. Use them for elements that need to pop against each other — an enemy highlight against the environment, a collectible against its background.
- Analogous colors (neighbors on the wheel) create calm and cohesion. They work well for environments, palettes within a single biome, or any context where unity matters more than contrast.
- Triadic schemes (three colors equally spaced on the wheel) produce vibrant variety while maintaining balance. They suit stylized or cartoony aesthetics that embrace bold color.
- Split-complementary offers the contrast benefits of complements without the visual harshness. Pick a base color, then use the two colors adjacent to its complement. This is often easier to work with than pure complementary.
- Choose a harmony model early and stick with it across the project. Random colors without a governing relationship look amateur and undermine visual identity.

## Color Psychology

- Red communicates danger, urgency, health loss, and passion. It is the most attention-grabbing color and should be reserved for signals that demand immediate response.
- Blue communicates calm, trust, cold, and sadness. It is the default for water, sky, and safe UI elements, and it recedes visually, making it useful for backgrounds.
- Green communicates nature, health, safety, and — depending on context — poison or corruption. Its meaning is highly context-dependent, so establish which reading your game uses and reinforce it consistently.
- Yellow communicates caution, energy, treasure, and cowardice. It has the highest visibility of any hue against dark backgrounds, making it effective for warnings and pickups.
- These associations are culturally constructed, not universal. Western audiences read white as purity; East Asian audiences may read it as mourning. Know your target audience and test assumptions.

## Warm vs Cool

- Warm colors (red, orange, yellow) advance — they appear closer to the viewer and feel more urgent. Use them for foreground elements, active threats, and anything that should demand attention.
- Cool colors (blue, green, purple) recede — they appear farther away and feel calmer. Use them for backgrounds, safe zones, and ambient environmental detail.
- Temperature contrast creates depth without geometry. A warm-toned character against a cool-toned background separates visually even at low resolution or small scale.
- Shift color temperature to signal emotional changes in the scene. A level that transitions from cool blue calm to warm red tension tells the player something has changed before any enemy appears.
- Avoid mixing warm and cool randomly within a single composition unless the contrast is intentional. Unintentional temperature clashes create visual confusion.

## Value & Contrast

- Value (light vs dark) matters more than hue for readability. A red enemy on a green background is invisible if both colors share the same value. Difference in lightness is what the eye reads first.
- Apply the squint test: defocus your eyes or convert a screenshot to grayscale. If you cannot distinguish gameplay-critical elements from their surroundings, your values are too similar.
- High contrast draws the eye — use it for interactive elements, threats, objectives, and anything the player needs to find quickly. The brightest or darkest element on screen wins attention.
- Low contrast causes elements to recede — use it for backgrounds, environmental detail, and decorative elements that should not compete with gameplay.
- Gameplay-critical elements need the highest value contrast in the scene. If a health pickup is the same value as the floor it sits on, players will walk past it.

## Saturation Control

- Highly saturated colors demand attention. Use them sparingly for the most important on-screen elements — critical UI indicators, rare items, active abilities.
- Desaturated palettes feel grounded and realistic. They work well for naturalistic environments and make the occasional saturated accent stand out dramatically.
- Mixing high and low saturation in the same scene creates a natural visual hierarchy. The most saturated element reads as the most important without any additional cues.
- Full saturation everywhere creates visual fatigue. When every surface is vivid, nothing stands out, and the player's eyes have nowhere to rest. The result looks noisy rather than vibrant.
- The most saturated thing on screen should be the most important thing on screen. If a background prop is more saturated than the player character, the hierarchy is inverted.

## Color for Gameplay

- Color should communicate game state: health levels, faction allegiance, elemental types, item rarity, buff and debuff status. Assign each meaning a distinct color and enforce it globally.
- Establish color meanings in the first minutes of play and never contradict them. If red means damage, a red health pickup confuses. Consistency builds the visual language the player relies on.
- Red health bar with green health pickup is near-universal in games. Deviating from deeply established conventions requires strong justification and clear onboarding.
- Rarity tiers need distinct, visually ordered colors. The convention white, green, blue, purple, orange (common to legendary) is widely understood. If you deviate, ensure your ordering still reads as escalating.
- Always pair color with a secondary signal — shape, icon, pattern, or text — for colorblind accessibility. Approximately 8% of men have some form of color vision deficiency. Color alone is never sufficient for critical information.
- Test all color-coded systems with deuteranopia, protanopia, and tritanopia simulation filters. Red-green distinctions fail for the most common forms of colorblindness.

## Lighting & Color

- Lighting changes color perception. A red object under blue light shifts toward purple or black depending on intensity. Design palettes with your lighting model active, not under neutral white light.
- Establish a consistent lighting model for each environment. If one cave is lit with cool blue and another with warm amber, both are valid, but the choice should be deliberate and tied to narrative or gameplay purpose.
- Time-of-day lighting shifts should feel natural and gradual. Sudden color temperature jumps break immersion. Dawn moves through blue to gold, midday is neutral, sunset is amber to purple, night is deep blue.
- Dramatic lighting (high contrast, strong directional color) creates mood and atmosphere but can obscure gameplay elements. When mood lighting is active, ensure interactive elements retain sufficient value contrast.
- Flat lighting (even, neutral, low contrast) prioritizes readability and gameplay clarity over atmosphere. Use it in contexts where the player needs to process information quickly — menus, inventory screens, complex combat arenas.

## Color Palette Construction

- Start with 3-5 base colors derived from your chosen harmony model, then generate variants by adjusting lightness and saturation. Each base color should have at least a light, mid, and dark variant.
- Limit the total palette. Constraint creates cohesion. A 12-color palette with clear roles (background, foreground, accent, UI, danger, safe) will always look more polished than an unlimited one.
- Name colors semantically — danger-red, health-green, rarity-epic — rather than by hex value. Semantic names make the palette maintainable and communicative in design documents and code.
- Test your palette under all lighting conditions the game uses. A color that reads clearly under neutral light may become ambiguous under the warm tones of a sunset scene or the blue cast of an underwater level.
- Test with colorblind simulation tools before finalizing any palette. Correct issues at the palette level, not after assets are built. Retrofitting accessibility into a finished palette is expensive and often compromised.
- Document the palette in a single source of truth with swatches, names, hex values, and intended usage. Every team member and every tool should reference the same definitions.
