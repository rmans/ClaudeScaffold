# Audio Design

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

Principles for game audio — how sound design, music, and silence shape the player experience.

---

## Sound as Feedback

- Every player action should produce audio confirmation. A button press, a jump, a hit, a pickup — if the player did something and heard nothing, the game feels unresponsive.
- Sounds communicate success, failure, and state changes faster than visuals. The player registers a damage sound before they notice a health bar moving.
- Pitch, volume, and timing convey intensity without new assets. A higher-pitched hit sound implies a critical strike. A quieter sound implies distance or weakness. A faster sequence implies urgency.
- Layer sounds to sell impact. A sword hit is not one sound — it is the slash through air, the impact on the target, and the target's reaction. Each layer adds believability.
- Audio should be informative, not decorative. If a sound does not help the player understand what just happened, it is clutter competing for attention in the mix.

## Audio Hierarchy

- Not all sounds are equal. Gameplay-critical audio (damage taken, cooldown ready, enemy alert) must always cut through the mix. If ambient rain masks a hit confirmation, the mix is wrong.
- Establish priority tiers and mix accordingly: UI sounds sit on top, then gameplay feedback, then music, then ambience. When sounds compete, the higher-priority tier wins.
- Reserve distinct, recognizable sounds for high-priority events. The player should be able to identify "I just took damage" or "an item dropped" by sound alone without looking at the screen.
- Ambience sets mood but should never fight with gameplay audio. Keep ambient layers broad and low in the mix so they fill space without occupying the frequency ranges that feedback sounds need.
- Test the mix in the worst case, not the average case. Play a busy combat encounter with maximum enemies, effects, and music running simultaneously. If critical sounds are buried, the hierarchy needs adjustment.

## Music Design

- Music sets emotional tone and pacing. A tense string drone communicates danger before the player sees the threat. An upbeat theme after a boss fight validates the victory.
- Looping tracks need seamless loop points. Audible seams — a pop, a gap, a mismatched reverb tail — break immersion every time the loop restarts. Test loops by listening through multiple cycles.
- Silence between tracks is a valid compositional choice. Not every moment needs music. The absence of a score creates contrast that makes the next musical moment more powerful.
- Music should respond to gameplay state. Calm exploration, rising tension, active combat, and victory each deserve distinct musical treatment. Static music that ignores what the player is doing feels disconnected.
- Avoid ear fatigue over extended sessions. Vary instrumentation, dynamics, and key across tracks the player will hear for hours. A single repeated motif becomes grating long before the player consciously notices why.

## Adaptive Audio

- Music and ambience should react to game state, not play on fixed timers. When the player enters combat, the audio should reflect it — not finish the current peaceful loop first.
- Layered stems feel more natural than hard cuts. Start with a base layer during exploration, add percussion when enemies appear, bring in full orchestration during combat, and pull layers back out when combat ends.
- Crossfade between states. A jarring cut from combat music to silence breaks immersion. A two-second fade feels intentional and polished.
- Vertical remixing — adding and removing layers within a single composition — generally produces smoother transitions than horizontal switching — jumping between entirely different tracks. Use vertical remixing as the default approach and reserve horizontal switches for major state changes.
- Design transition points in advance. Compose music with natural break points where layers can enter or exit cleanly. Trying to force adaptive behavior onto music that was not designed for it produces awkward results.

## Spatial Audio

- Sound in 3D space helps players locate threats, objectives, and points of interest before they see them. An enemy growl from the left tells the player where to look.
- Distance attenuation should feel natural. Sounds grow quieter with distance, but the falloff curve matters — linear falloff sounds artificial, while logarithmic falloff matches human perception.
- Reverb communicates environment. A cave should sound different from an open field, which should sound different from a small room. Even without visuals, reverb tells the player where they are.
- Off-screen audio cues are critical for awareness. The player cannot see behind them, but they can hear behind them. Footsteps, growls, and mechanical sounds from off-screen give the player spatial information they cannot get from visuals alone.
- Stereo panning and volume differences between ears are the minimum for spatial awareness. Full 3D audio with height information is ideal when the platform supports it, but left-right panning alone still provides significant value.

## The Power of Silence

- Silence is a design tool, not a gap to fill. Deliberately removing sound creates tension, unease, or stillness that no amount of audio can replicate.
- Removing music while keeping ambient sound makes a scene feel grounded and real. The world continues, but the emotional framing disappears, leaving the player alone with the environment.
- Quiet moments make loud moments more impactful. A sudden explosion after thirty seconds of near-silence hits harder than the same explosion in an already-noisy scene.
- A sudden silence after sustained noise is one of the most powerful audio tools available. Cutting all sound after a detonation, a boss death, or a dramatic moment creates a beat that forces the player to process what just happened.
- Do not fill silence with anxiety. If a quiet stretch exists in the design, resist the urge to add filler audio. Trust the silence to do its job.

## UI Audio

- UI sounds should be subtle, consistent, and satisfying. They are the most frequently heard sounds in the game — the player navigates menus hundreds of times per session.
- Provide distinct sounds for hover, select, back, and error states. The player should be able to navigate a menu by sound alone and know what just happened.
- Keep UI sounds short and clean. Long tails, heavy reverb, or dramatic flourishes on basic menu interactions become grating within minutes.
- Match UI audio to the game's overall audio identity. A fantasy RPG and a sci-fi shooter should not share the same menu click sound. UI sounds are part of the aesthetic.
- Test UI sounds at high repetition rates. A sound that is pleasant once may be intolerable when triggered rapidly during fast menu scrolling. Design for the fastest input the player can produce.

## Accessibility

- Provide visual alternatives for every critical audio cue. Subtitles for dialogue, directional indicators for off-screen threats, screen flash or border color for damage — never rely solely on sound for gameplay-critical information.
- Offer separate volume sliders for music, SFX, voice, and UI at minimum. Players need to balance channels for their hearing ability, speaker setup, and personal preference.
- Support mono audio for single-speaker setups and players with hearing loss in one ear. Spatial information encoded only in stereo separation is lost entirely in mono without a downmix option.
- Provide subtitle options with adjustable size and optional background panels for readability. Speaker labels help when multiple characters speak in sequence.
- Test the game with audio muted entirely. If any gameplay-critical information becomes inaccessible, a visual fallback is missing and must be added.
