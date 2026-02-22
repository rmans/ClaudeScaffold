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
2. **Identify which sections are already filled** (have content beyond `*TODO:*` markers) and which are empty.
3. **Skip sections that are already complete.** Only walk the user through unfilled or partial sections.

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
12. **Aesthetic Pillars** — Ask: *"Give me 3-5 words that describe how everything should look and feel."*
13. **Audio Identity** — Ask: *"What does this game sound like?"*
14. **Lore Delivery** — Ask: *"How does the player learn about the world? Explicit or environmental? Delivered or discovered?"*

### Pass 4 — Depth (how it plays and progresses)

15. **Primary Skill** — Ask: *"What skill does the player get better at?"*
16. **Difficulty Philosophy** — Ask: *"How does difficulty work?"*
17. **Failure States** — Ask: *"What happens when the player fails? How punishing is it?"*
18. **Input Feel** — Ask: *"How should the controls feel? Snappy, weighty, precise?"*
19. **What the Player Earns** — Ask: *"What does the player unlock or become?"*
20. **Pacing** — Ask: *"How often do you reward? What's the rhythm?"*
21. **Player Identity / Build** — Ask: *"What choices does the player make about who they are in this game?"*
22. **Target Length** — Ask: *"How long is the main path? Completionist path? Why?"*

### Pass 5 — Narrative

23. **Central Conflict** — Ask: *"What drives the game forward?"*
24. **Player Character** — Ask: *"Who is the player? Defined personality, blank slate, or something in between?"*
25. **Story Delivery** — Ask: *"How is story delivered?"*
26. **Player Choice & Consequence** — Ask: *"Does the player make choices? How meaningful are the consequences?"*

### Pass 6 — Practical

27. **First Session** — Ask: *"What does the first 5 minutes feel like? The first hour?"*
28. **The Moment** — Ask: *"What's the thing the player tells a friend about?"*
29. **Emotional Arc** — Ask: *"When does the player feel powerful? Vulnerable? Curious?"*
30. **What Fun Means Here** — Ask: *"What kind of fun is this? Mastery, discovery, expression, tension?"*

### Pass 7 — Scope & Business (can be deferred)

31. **Multiplayer & Social** — Ask: *"Solo, co-op, competitive, or combination? If solo, why?"*
32. **Target Platforms** — Ask: *"What platforms? What are the performance targets?"*
33. **Biggest Technical Risk** — Ask: *"What's the hardest thing to build? What if it doesn't work?"*
34. **Scope Reality Check** — Ask: *"Is this buildable? What gets cut first?"*
35. **Vertical Slice** — Ask: *"What single chunk of the game proves the whole thing works?"*
36. **Target Audience** — Ask: *"Who is this for?"*
37. **Content Lifecycle** — Ask: *"Ship and done, or ongoing updates?"*
38. **Monetization** — Ask: *"What's the business model?"*
39. **Success Metrics** — Ask: *"What does success look like? Be concrete."*
40. **Scope Boundaries** — Ask: *"What is this game NOT? What trends are you sitting out?"*

## Rules

- **Ask one section at a time.** Do not dump all questions at once.
- **Write answers into the design doc immediately** after the user responds. Replace the `*TODO:*` marker with their answer.
- **Use the user's voice.** Capture their intent faithfully — don't rewrite their vision into generic game-design language.
- **If the user says "skip" or "later"**, leave the TODO marker and move on.
- **If the user gives a short answer**, that's fine. Short and clear beats long and vague.
- **After completing a pass**, summarize what was captured and ask if they want to continue to the next pass or stop for now.
- **At the end**, report how many sections are now filled vs. remaining TODOs.
