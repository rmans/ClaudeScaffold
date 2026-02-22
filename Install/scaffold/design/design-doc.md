# Design Document

> **Authority:** Rank 1 — highest. All other documents must conform to this.
> **Layer:** Canon

---

## Vision & Identity

<!-- The compass for every decision. If you can't answer these, nothing else matters. -->

### Core Fantasy

<!-- One sentence: what does the player *feel* like they're doing? Not mechanics — emotion. -->

*TODO: Define the core fantasy.*

### Elevator Pitch

<!-- One sentence that makes someone who has never played a game lean forward. -->

*TODO: Write the elevator pitch.*

### Core Pillars

<!-- 3-5 design pillars that guide every decision. When two features compete for time, pillars break the tie. -->

*TODO: Define design pillars.*

### Non-Negotiables

<!-- Constraints that must never be violated. These are the rules that define the game. If code or a lower-authority document would break one, the code is wrong. -->

*TODO: List non-negotiable design constraints.*

---

## Genre & Reference Points

<!-- What genre(s) does this game belong to? What conventions are we following? Which ones are we deliberately breaking? -->

*TODO: Define genre and conventions.*

### Reference Games

<!-- Not to copy — to establish shared vocabulary. What existing games are touchstones? What do we take from each, and what do we reject? -->

*TODO: List reference games and what we learn from each.*

---

## Player Experience

### Core Loop

<!-- The thing the player does every 30 seconds to 5 minutes. Describe it simply. -->

*TODO: Define the core loop.*

### Meta Loop

<!-- The thing that keeps the player coming back across sessions — progression, mastery, narrative, collection, competition, creation? -->

*TODO: Define the meta loop.*

### First Session

<!-- What does the first 5 minutes feel like? The first hour? What's the onboarding philosophy? -->

*TODO: Describe the first session experience.*

### The "Moment"

<!-- The thing the player tells a friend about. Every great game has one. What's ours? -->

*TODO: Define the signature moment.*

### Emotional Arc

<!-- When does the player feel powerful? Vulnerable? Curious? Tense? How do we control that arc? -->

*TODO: Map the emotional arc.*

### What "Fun" Means Here

<!-- Mastery? Discovery? Expression? Social connection? Tension and release? Management? Name it. -->

*TODO: Define what fun means for this game.*

---

## World & Setting

### Place & Time

<!-- Where and when does this take place? What's the visual and tonal identity? -->

*TODO: Define setting.*

### Rules of the World

<!-- What's possible, what's impossible, and what's the internal logic? -->

*TODO: Define world rules.*

### Aesthetic Pillars

<!-- 3-5 words that describe how everything should look and feel. Art direction starts here. -->

*TODO: Define aesthetic pillars.*

### Audio Identity

<!-- What does this game sound like? Music direction, ambient feel, feedback philosophy, use of silence. -->

*TODO: Define audio identity.*

### Lore Delivery

<!-- How much world does the player see vs. infer? Is story explicit or environmental? Delivered or discovered? -->

*TODO: Define lore delivery approach.*

---

## Core Mechanics

### Player Verbs

<!-- What does the player actually DO, moment to moment? List the verbs: jump, shoot, build, talk, solve, drive, manage, explore, trade, etc. -->

*TODO: List player verbs.*

### Primary Skill

<!-- What skill does the player develop? Mechanical precision? Strategic thinking? Pattern recognition? Resource management? Social reading? -->

*TODO: Define the primary skill.*

### Difficulty Philosophy

<!-- Fixed curve? Adaptive? Player-selected? Emergent from systems? How do we handle the spectrum from newcomer to veteran? -->

*TODO: Define difficulty philosophy.*

### Failure States

<!-- What happens when the player fails? How punishing is it, and why is that the right call for this game? -->

*TODO: Define failure states.*

### Input Feel

<!-- How should controls feel? Snappy? Weighty? Floaty? Precise? This sets the tone for everything downstream. -->

*TODO: Define input feel.*

---

## Progression & Motivation

### What the Player Earns

<!-- What does the player unlock, earn, or become? What's the carrot? -->

*TODO: Define progression rewards.*

### Pacing

<!-- How often do we reward? How do we prevent fatigue? What's the rhythm? -->

*TODO: Define pacing philosophy.*

### Player Identity / Build

<!-- What choices does the player make about who they are in this game? Are those choices reversible? -->

*TODO: Define player identity system.*

### Content Structure

<!-- Levels? Open world? Procedural? Branching? Linear with hubs? How is the game organized? -->

*TODO: Define content structure.*

### Target Length

<!-- How long is the main path? For completionists? Why is that the right length? -->

*TODO: Define target length.*

---

## Narrative & Context

### Central Conflict

<!-- What drives the game forward? Even abstract games have tension. What's ours? -->

*TODO: Define central conflict.*

### Player Character

<!-- Defined personality? Blank slate? Silent protagonist? Something in between? -->

*TODO: Define player character approach.*

### Story Delivery

<!-- Cutscenes? Dialogue? Environmental? Emergent from systems? Minimal/none? -->

*TODO: Define story delivery method.*

### Player Choice & Consequence

<!-- Does the player make narrative choices? How meaningful are they? What's our commitment to consequence? -->

*TODO: Define choice and consequence philosophy.*

---

## System Design Index

> Individual system designs live in [systems/](systems/_index.md).
> Each system has its own file using the [system template](../templates/system-template.md).
> This table is the master index — add systems here as they are designed.

| ID | System | One-Line Purpose | Status |
|----|--------|------------------|--------|
| *None yet* | — | — | — |

<!-- Example entries:
| SYS-001 | Construction | Player places blueprints; colonists haul materials and build | Draft |
| SYS-002 | Needs & Mood | Colonists have needs that affect mood and behavior | Draft |
| SYS-003 | Combat | Turn-based tactical combat on grid maps | Complete |
-->

---

## Multiplayer & Social

<!-- If singleplayer only: say so and why. If multiplayer: answer the questions below. -->

*TODO: Define multiplayer stance.*

### Social Loop

<!-- How do players find each other, interact, and form relationships? -->

### Competitive Balance

<!-- Skill-based? Loadout variety? Asymmetric? -->

### Community & Modding

<!-- Are players consumers or creators? What's the UGC strategy? -->

---

## Technology & Scope

### Target Platforms

<!-- What are we shipping on? What are the performance targets? -->

*TODO: Define platforms and targets.*

### Biggest Technical Risk

<!-- Name it now. What's the plan if it doesn't work? -->

*TODO: Identify top technical risk.*

### Scope Reality Check

<!-- Given team size, budget, and timeline — is this buildable? What gets cut first? -->

*TODO: Define scope constraints and cut list.*

### Vertical Slice

<!-- What single chunk of the game, if built, proves the whole thing works? -->

*TODO: Define the vertical slice.*

---

## Business & Lifecycle

### Target Audience

<!-- Who is this game for? Primary audience. Secondary audience. -->

*TODO: Define target audience.*

### Content Lifecycle

<!-- Ship and done? Seasonal updates? Expansion packs? Endless live service? -->

*TODO: Define content lifecycle.*

### Monetization

<!-- Premium? Free-to-play? Subscription? Where are the ethical lines? -->

*TODO: Define monetization model.*

### Success Metrics

<!-- Sales? Retention? Critical reception? Cultural impact? Define it concretely. -->

*TODO: Define what success looks like.*

---

## Scope Boundaries — What We're NOT Doing

<!-- Features we're explicitly cutting or avoiding, and why. Trends we're sitting out. Complexity we refuse to add. This section is a shield against scope creep. -->

*TODO: Define what this game is NOT.*

---

## Gut-Check Questions

*These should be answerable at any point in development:*

1. **"Is this fun right now?"** — Not fun in theory. Fun in the build you can play today.
2. **"Can you explain it to someone who doesn't play games?"** — If not, it might be too complicated.
3. **"What's the thing only THIS game does?"** — If nothing, why does it exist?
4. **"Would I play this for free on a Saturday?"** — Honest answer only.
5. **"What breaks if we cut this feature?"** — If nothing breaks, cut it.
