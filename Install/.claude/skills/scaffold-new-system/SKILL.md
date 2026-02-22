---
name: scaffold-new-system
description: Create a new system design file. If the design doc is filled out, pre-fills Purpose and Player Intent from it. Otherwise creates a blank template.
argument-hint: [system-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# New System Design

Create a new system design document for: **$ARGUMENTS**

## Steps

### 1. Read Context

1. **Read the system template** at `scaffold/templates/system-template.md`.
2. **Read the systems index** at `scaffold/design/systems/_index.md` to find the next available SYS-### ID.
3. **Read the design doc** at `scaffold/design/design-doc.md`.
4. **Read the glossary** at `scaffold/design/glossary.md`.
5. **Read advisory theory docs** for context (these inform suggestions but carry no authority):
   - `scaffold/theory/game-design-principles.md` — principles to guide system design
   - `scaffold/theory/common-design-pitfalls.md` — anti-patterns to steer away from
   - `scaffold/theory/balance-principles.md` — balance guidance for system tuning

### 2. Determine the Next SYS ID

Find the highest existing SYS-### number. The new system gets the next sequential ID. If no systems exist yet, start at SYS-001.

### 3. Extract Context (if available)

If the design doc has content (not just TODO markers) in Core Fantasy, Player Verbs, or Core Loop, extract context for this system:

- **Player Verbs** — which verbs does this system own?
- **Core Loop / Meta Loop** — which steps involve this system?
- **Failure States** — does this system have failure modes?
- **AI / NPC Behavior** — if this is an AI-related system
- **Any other section** that references this system's domain

If the design doc is empty or too sparse, skip this step — create a blank file and tell the user why no pre-fill was possible.

### 4. Create the System File

Create `scaffold/design/systems/SYS-###-<name>.md` where `<name>` is a lowercase-kebab-case version of the system name.

- Replace `SYS-###` in the title with the actual ID.
- Replace `[System Name]` with the provided name.

If context was extracted (step 3):
- **Purpose** — One sentence derived from the design doc's description of this domain.
- **Player Intent** — Bullet list derived from relevant player verbs and loop steps.
- **Player Actions** — Draft numbered steps if the design doc provides enough detail. Otherwise leave as template prompt.
- Leave all other sections as template prompts.

If no context was available:
- Leave all sections as template prompts for the user to fill in.

### 5. Seed Glossary Terms

If the system introduces terms not yet in the glossary:
- Propose 1-5 candidate terms to the user.
- On confirmation, add them to `scaffold/design/glossary.md` in alphabetical order.

### 6. Register

1. Add a row to `scaffold/design/systems/_index.md` (Status: Draft).
2. Add a row to the System Design Index in `scaffold/design/design-doc.md` (Status: Draft).

### 7. Report

Show the user:
- The file path and assigned ID
- Whether Purpose/Player Intent were pre-filled or left blank (and why)
- Any glossary terms added
- Reminder to fill in the remaining sections
- Reminder to run `/scaffold-review-system` when the system design is complete

## Rules

- **Never overwrite an existing system file.**
- **IDs are sequential and permanent** — never skip or reuse.
- **If no system name is provided**, ask the user for one before proceeding.
- **Pre-filled content is a starting point.** Tell the user to review and refine — don't present it as final.
- **Keep both index tables in sync** — the design doc and systems/_index.md must always match.
- **Use theory docs as advisory context.** Reference principles or pitfalls when relevant to help the user think through system design, but never impose them. Theory informs — it doesn't dictate.
