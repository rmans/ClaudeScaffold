---
name: scaffold-new-design
description: Initialize the design document by walking through each section with the user. Use when starting a new game's design or filling out an empty design doc.
argument-hint: [game-name]
allowed-tools: Read, Edit, Grep, Glob
---

# New Design Document

Guide the user through filling out `scaffold/design/design-doc.md` for: **$ARGUMENTS**

## Before Starting

1. **Read the current design doc** at `scaffold/design/design-doc.md`.
2. **Read advisory theory docs** for context (these inform suggestions but carry no authority):
   - `scaffold/theory/game-design-principles.md` — core principles to guide suggestions
   - `scaffold/theory/common-design-pitfalls.md` — anti-patterns to steer away from
   - `scaffold/theory/genre-conventions.md` — genre-specific expectations to reference when genre is known
   - `scaffold/theory/narrative-design.md` — narrative principles for the storytelling sections
   - `scaffold/theory/level-design.md` — spatial design for content structure
   - `scaffold/theory/audio-design.md` — audio principles for audio identity
   - `scaffold/theory/balance-principles.md` — balance guidance for difficulty and pacing
   - `scaffold/theory/world-design.md` — world building for content structure and world sections
   - `scaffold/theory/multiplayer-design.md` — multiplayer principles if the game has multiplayer
3. **Identify which sections are already filled** (have content beyond `*TODO:*` markers) and which are empty.
4. **Skip sections that are already complete.** Only walk the user through unfilled or partial sections.

## Walkthrough Order

Work through the design doc in this order. Each section is a conversation with the user — ask questions, listen, then write their answers into the doc.

### Pass 1 — Identity (must be answered first, everything else flows from here)

1. **Core Fantasy** — Ask: *"What does the player feel like they're doing? Not mechanics — the emotion and fantasy."*
2. **Elevator Pitch** — Ask: *"In one sentence, what's the hook? What makes someone lean in?"*
3. **Core Pillars** — Ask: *"What are the 3-5 principles that guide every decision? When two features compete, what breaks the tie?"*
4. **Non-Negotiables** — Ask: *"What rules can never be broken? What constraints define this game?"*

### Pass 2 — Shape (what kind of game this is)

5. **Genre & Reference Points** — Ask: *"What genre is this? What games are touchstones — and what do you take or reject from each?"*
6. **Core Loop** — Ask: *"What does the player do every 30 seconds to 5 minutes? Walk me through it."*
7. **Meta Loop** — Ask: *"What keeps the player coming back across sessions?"*
8. **Player Verbs** — Ask: *"List every action the player takes. What are the verbs?"*
9. **Content Structure** — Ask: *"How is the game organized? Levels, open world, procedural, branching?"*

### Pass 3 — World (where and how it feels)

10. **Place & Time** — Ask: *"Where and when does this take place?"*
11. **Rules of the World** — Ask: *"What's possible? What's impossible? What's the internal logic?"*
12. **Tone** — Ask: *"What's the emotional tone? Dark and grim? Cozy? Tense? Absurdist? Lighthearted?"*
13. **Camera / Perspective** — Ask: *"What's the camera? First-person, third-person, top-down, isometric, side-scrolling? Player-controlled or fixed?"*
14. **Aesthetic Pillars** — Ask: *"Give me 3-5 words that describe how everything should look and feel."*
15. **Audio Identity** — Ask: *"What does this game sound like?"*
16. **Lore Delivery** — Ask: *"How does the player learn about the world? Explicit or environmental? Delivered or discovered?"*

### Pass 4 — Depth (how it plays and progresses)

17. **Primary Skill** — Ask: *"What skill does the player get better at?"*
18. **Difficulty Philosophy** — Ask: *"How does difficulty work?"*
19. **Failure States** — Ask: *"What happens when the player fails? How punishing is it?"*
20. **Input Feel** — Ask: *"How should the controls feel? Snappy, weighty, precise?"*
21. **AI / NPC Behavior** — Ask: *"How smart should NPCs or enemies be? Predictable and readable, or adaptive and surprising? If not applicable, skip."*
22. **What the Player Earns** — Ask: *"What does the player unlock or become?"*
23. **Pacing** — Ask: *"How often do you reward? What's the rhythm?"*
24. **Player Identity / Build** — Ask: *"What choices does the player make about who they are in this game?"*
25. **Save / Session Structure** — Ask: *"How does the player save? How long is a typical play session?"*
26. **Target Length** — Ask: *"How long is the main path? Completionist path? Why?"*

### Pass 5 — Narrative

27. **Central Conflict** — Ask: *"What drives the game forward?"*
28. **Player Character** — Ask: *"Who is the player? Defined personality, blank slate, or something in between?"*
29. **Story Delivery** — Ask: *"How is story delivered?"*
30. **Player Choice & Consequence** — Ask: *"Does the player make choices? How meaningful are the consequences?"*

### Pass 6 — Practical

31. **First Session** — Ask: *"What does the first 5 minutes feel like? The first hour?"*
32. **The Moment** — Ask: *"What's the thing the player tells a friend about?"*
33. **Emotional Arc** — Ask: *"When does the player feel powerful? Vulnerable? Curious?"*
34. **What Fun Means Here** — Ask: *"What kind of fun is this? Mastery, discovery, expression, tension?"*

### Pass 7 — Accessibility & Scope (can be deferred)

35. **Accessibility Philosophy** — Ask: *"What's our accessibility commitment? Minimum compliance, best-in-class, or somewhere between?"*
36. **Accessibility Targets** — Ask: *"Which accessibility features do we commit to? Colorblind support, difficulty options, input remapping, subtitles, UI scaling?"*
37. **Multiplayer & Social** — Ask: *"Solo, co-op, competitive, or combination? If solo, why?"*
38. **Target Platforms** — Ask: *"What platforms? What are the performance targets?"*
39. **Biggest Technical Risk** — Ask: *"What's the hardest thing to build? What if it doesn't work?"*
40. **Scope Reality Check** — Ask: *"Is this buildable? What gets cut first?"*
41. **Vertical Slice** — Ask: *"What single chunk of the game proves the whole thing works?"*
42. **Target Audience** — Ask: *"Who is this for?"*
43. **Content Lifecycle** — Ask: *"Ship and done, or ongoing updates?"*
44. **Monetization** — Ask: *"What's the business model?"*
45. **Success Metrics** — Ask: *"What does success look like? Be concrete."*
46. **Scope Boundaries** — Ask: *"What is this game NOT? What trends are you sitting out?"*

## Rules

- **Ask one section at a time.** Do not dump all questions at once.
- **Write answers into the design doc immediately** after the user responds. Replace the `*TODO:*` marker with their answer.
- **Use the user's voice.** Capture their intent faithfully — don't rewrite their vision into generic game-design language.
- **Use theory docs as advisory context.** Reference principles or pitfalls when relevant to help the user think through decisions, but never impose them. Theory informs — it doesn't dictate.
- **If the user says "skip" or "later"**, leave the TODO marker and move on.
- **If the user gives a short answer**, that's fine. Short and clear beats long and vague.
- **After completing a pass**, summarize what was captured and ask if they want to continue to the next pass or stop for now.
- **At the end**, report how many sections are now filled vs. remaining TODOs.
- **Remind the user** to run `/scaffold-review-design` when done to audit completeness.
