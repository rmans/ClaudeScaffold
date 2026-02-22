---
name: scaffold-bulk-seed-systems
description: Read the design doc, seed the glossary with key terms, and bulk-create all system design stubs. Use after the design doc is filled out.
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Systems from Design Doc

Read the completed design doc and use it to seed the glossary and bulk-create system design files.

## Prerequisites

1. **Read the design doc** at `scaffold/design/design-doc.md`.
2. **Verify it's sufficiently filled out.** The following sections must have content (not just TODO markers):
   - Core Fantasy
   - Core Pillars
   - Core Loop
   - Player Verbs
   - Content Structure
3. If the design doc is too empty, stop and tell the user to run `/scaffold-new-design` first.

## Phase 1 — Seed Glossary

1. **Read** `scaffold/design/glossary.md`.
2. **Extract candidate terms** from the design doc. Look for:
   - Game-specific nouns (entities, locations, resources, mechanics)
   - Terms that appear multiple times with a consistent meaning
   - Terms that could be confused with synonyms (these need a NOT column entry)
3. **Present the proposed terms** to the user as a table:
   ```
   | Term | Proposed Definition | NOT (suggested) |
   ```
4. **Ask the user to confirm, edit, or reject** each term.
5. **Write confirmed terms** into the glossary table, preserving alphabetical order.

## Phase 2 — Identify Systems

1. **Analyze the design doc** to identify all major systems the game needs. Sources:
   - **Player Verbs** — Each verb or verb cluster often maps to a system (build → Construction, fight → Combat, trade → Trading)
   - **Core Loop** — Each step in the loop implies a system
   - **Meta Loop** — Progression, unlocks, reputation etc. imply systems
   - **Failure States** — Damage, death, loss conditions imply systems
   - **AI / NPC Behavior** — May imply one or more AI systems
   - **Save / Session Structure** — May imply a save/persistence system
   - **Content Structure** — World generation, level loading etc.
   - **Progression & Motivation** — Skill trees, unlocks, crafting
2. **For each proposed system**, draft:
   - A name (concise, noun-based: "Construction", "Combat", "Needs & Mood")
   - A one-line purpose (what it does from the player's perspective)
   - Which player verbs it owns
3. **Present the full system list** to the user as a table:
   ```
   | ID | Proposed Name | One-Line Purpose | Player Verbs |
   ```
4. **Ask the user to confirm, rename, merge, split, or remove** systems before creation.

## Phase 3 — Bulk Create System Files

For each confirmed system:

1. **Read the system template** at `scaffold/templates/system-template.md`.
2. **Assign the next sequential SYS-### ID** (starting from SYS-001 or the next available).
3. **Create the file** at `scaffold/design/systems/SYS-###-name.md`:
   - Replace `SYS-###` with the actual ID
   - Replace `[System Name]` with the confirmed name
   - Fill in the **Purpose** section with the confirmed one-line purpose
   - Fill in **Player Intent** with bullet points derived from the relevant player verbs
   - Leave all other sections as template prompts
4. **Register in both indexes:**
   - Add a row to `scaffold/design/systems/_index.md`
   - Add a row to the System Design Index in `scaffold/design/design-doc.md`
   - Set Status to `Draft`

## Phase 4 — Report

Summarize what was created:
- Number of glossary terms added
- Number of systems created, with their IDs and names
- Remind the user of next steps: fill in each system design, run `/scaffold-bulk-review-systems` to audit, then run `/scaffold-bulk-seed-references` once systems are complete

## Rules

- **Never create systems the user hasn't confirmed.** Always present the proposal first.
- **Don't over-split.** 8-15 systems is typical for a medium game. If you're proposing 25+, you're probably too granular — suggest merging related concerns.
- **Don't under-split.** If a proposed system owns 5+ unrelated verbs, it's probably two systems. Suggest splitting.
- **System names are nouns, not verbs.** "Construction" not "Building things." "Combat" not "Fighting."
- **IDs are sequential and permanent.** Never skip or reuse.
- **Preserve any existing systems.** If SYS-### files already exist, start numbering after the highest existing ID and don't overwrite.
- **Created documents start with Status: Draft.**
