# Audio Direction

> **Authority:** Rank 2
> **Layer:** Canon
> **Conforms to:** [design-doc.md](design-doc.md), [style-guide.md](style-guide.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

This document defines **what the game sounds like** — the role of audio in the player experience, when sounds play, what they communicate, and how audio density relates to game state. It is engine-agnostic and describes intent, not implementation.

<!-- This doc works alongside style-guide.md (visual identity), color-system.md (color meaning), and ui-kit.md (component feedback sounds). It defines the audio philosophy and direction; ui-kit.md defines specific per-component sound events. -->

---

## Audio Philosophy

<!-- What role does sound play in this game? Is audio primarily for simulation awareness (hearing what's happening offscreen), emotional tone (music setting mood), player feedback (confirming actions), or spectacle? What's the balance? -->

### Core Audio Identity

<!-- In one sentence: what should this game sound like? Reference the style-guide's visual tone registers (Baseline/Escalation/Crisis) — how does audio mirror them? -->

### Audio as Information

<!-- What information does audio convey that visuals don't (or reinforce)? Off-screen events? State changes? Approaching danger? -->

### Restraint Principle

<!-- When should the game be quiet? Not every system needs sound. Define the threshold: what earns audio presence and what doesn't. -->

## Sound Categories

<!-- Define the major categories of sound in the game. Each category has a purpose and a priority level. -->

### UI Sounds

<!-- Button clicks, panel opens/closes, tab switches, confirmations, errors. These are defined per-component in ui-kit.md — this section defines the character and style of UI sounds as a category. -->

<!-- Sonic character: clean, minimal, synthetic? Mechanical clicks? Soft tones? -->

### Feedback Sounds

<!-- Player action confirmation: structure placed, zone designated, colonist assigned, task queued. The "I heard you" sounds. -->

<!-- Sonic character: satisfying, brief, distinct per action type? Or uniform? -->

### Alert Sounds

<!-- Critical alerts, warnings, informational notices. Defined in ui-kit.md Alert Feed — this section defines the audio escalation model. -->

<!-- How do alert sounds escalate? Does critical interrupt music? Does warning have a subtler cue? -->

### Ambient World Sound

<!-- The base layer: facility hum, ventilation, distant machinery, weather outside. What the player hears when nothing specific is happening. -->

<!-- Sonic character: industrial? Clinical? Oppressive? Changes with facility state? -->

### System Event Sounds

<!-- Events from the simulation: construction completing, colonist arriving, research finishing, containment breach. These are gameplay events, not UI events. -->

<!-- How prominent are these? Background notification or foreground event? Spatial (from the event location) or global? -->

### Music

<!-- Scored music, if any. See Music Direction section below for full treatment. -->

## Music Direction

<!-- Does this game have music? When does it play? What does it communicate? -->

### When Music Plays

<!-- Always? Only during specific states (crisis, peace, night)? Triggered by events? Fades in/out based on game state? -->

### What Music Communicates

<!-- Mood (tension, calm, urgency)? Phase of the game (early colony, established, late-game crisis)? Or purely atmospheric? -->

### Pacing Relationship

<!-- How does music tempo/intensity relate to gameplay pacing? Does it respond to the simulation (adaptive) or follow a fixed schedule? -->

### Musical Style

<!-- Genre, instrumentation, production style. Reference the style-guide's visual tone — how does music reflect the same aesthetic? -->

## Silence & Space

<!-- Silence is a design choice, not a bug. Define when the game should be intentionally quiet. -->

### Ambient Density Curve

<!-- How does audio density change with game state? Early colony (sparse, quiet) vs established facility (busy, layered) vs crisis (intense, alarming)? -->

### Quiet Moments

<!-- When should the game pull back audio? After a crisis resolves? During peaceful nighttime? When the player is reading a panel? -->

### Silence as Signal

<!-- Does sudden silence mean something? (e.g., power failure kills ambient hum, containment breach stops all non-alert audio) -->

## Feedback Hierarchy

<!-- When multiple sounds compete, which wins? Define the priority stack. -->

### Priority Ordering

<!-- Example stack (highest to lowest):
1. Critical alerts (containment breach, colonist death)
2. Warning alerts (hunger, injury)
3. Player action feedback (structure placed, command issued)
4. System events (construction complete, research done)
5. UI sounds (panel open, button click)
6. Music
7. Ambient world sound
-->

### Simultaneous Sound Rules

<!-- How many simultaneous sounds? What gets ducked (volume reduced) when higher-priority sounds play? What gets cut entirely? -->

### Spatial vs Global

<!-- Which sounds are positional (from a location in the world) and which are global (play at full volume regardless of camera position)? Alerts are typically global. Ambient is typically spatial. -->

## Asset Style Rules

<!-- Technical direction for audio asset creation. -->

### 2D vs 3D Audio

<!-- Is audio spatialized (3D positioned in the world) or flat (2D, no spatial positioning)? Mix of both? Which categories use which? -->

### Realistic vs Stylized

<!-- Should sounds be realistic recordings or stylized/synthesized? Reference the style-guide's visual approach — if visuals are stylized, should audio match? -->

### Frequency & Loudness

<!-- Any frequency range restrictions? Maximum loudness for categories? Dynamic range expectations? -->

### Audio Format Conventions

<!-- Sample rate, bit depth, file format, naming conventions for audio assets. -->

## Accessibility

<!-- Audio accessibility requirements. -->

### Visual Alternatives

<!-- Every sound that conveys gameplay information must have a visual equivalent. No audio-only information. (Cross-reference: ui-kit.md already enforces this.) -->

### Subtitles / Captions

<!-- If there is voice or significant narrative audio, provide subtitles. Closed captions for sound effects? -->

### Volume Controls

<!-- Separate volume sliders for: Master, Music, SFX, UI, Ambient, Voice? -->

### Mono Support

<!-- Mono downmix option for hearing-impaired players who use one speaker/hearing aid. -->

## Rules

<!-- Enforceable rules that govern audio design decisions. -->

1. <!-- No audio-only information — every sound has a visual equivalent. -->
2. <!-- Critical alerts override all other audio. -->
3. <!-- Silence is intentional, not a missing asset. If a state has no sound, document why. -->
4. <!-- Audio density tracks game state — quiet colony, busy colony, crisis colony all sound different. -->
5. <!-- Music never obscures alert sounds — alerts duck music automatically. -->
