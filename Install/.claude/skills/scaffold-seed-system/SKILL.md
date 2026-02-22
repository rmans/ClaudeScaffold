---
name: scaffold-seed-system
description: Create a single system design pre-filled from the design doc. Unlike scaffold-new-system (blank template), this extracts Purpose and Player Intent from the design doc context.
argument-hint: [system-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Seed Single System from Design Doc

Create a single system design file for **$ARGUMENTS**, pre-filled with context extracted from the design doc.

## Steps

### 1. Read Context

1. **Read the design doc** at `scaffold/design/design-doc.md`.
2. **Read the system template** at `scaffold/templates/system-template.md`.
3. **Read the glossary** at `scaffold/design/glossary.md`.
4. **Read the systems index** at `scaffold/design/systems/_index.md` to find the next available SYS-### ID.

### 2. Extract Context for This System

From the design doc, find content relevant to the named system:
- **Player Verbs** — which verbs does this system own?
- **Core Loop / Meta Loop** — which steps involve this system?
- **Failure States** — does this system have failure modes?
- **AI / NPC Behavior** — if this is an AI-related system
- **Any other section** that references this system's domain

### 3. Draft the System File

Create the SYS-### file with these sections pre-filled (not just template defaults):

- **Purpose** — One sentence derived from the design doc's description of this domain
- **Player Intent** — Bullet list of what the player is trying to accomplish, derived from relevant player verbs and loop steps
- **Player Actions** — Draft numbered steps if the design doc provides enough detail. Otherwise leave as template prompt.

Leave all other sections (System Resolution, Failure States, Inputs/Outputs, etc.) as template prompts for the user to fill in.

### 4. Seed Glossary Terms

If the system introduces terms not yet in the glossary:
- Propose 1-5 candidate terms to the user
- On confirmation, add them to `scaffold/design/glossary.md` in alphabetical order

### 5. Register

1. Add a row to `scaffold/design/systems/_index.md` (Status: Draft)
2. Add a row to the System Design Index in `scaffold/design/design-doc.md` (Status: Draft)

### 6. Present to User

Show the user:
- The file path and assigned ID
- The pre-filled Purpose and Player Intent
- Any glossary terms added
- Reminder to fill in the remaining sections

## Rules

- **Never overwrite an existing system file.**
- **IDs are sequential and permanent** — pick the next available after the highest existing ID.
- **If no system name is provided**, ask the user for one before proceeding.
- **If the design doc is empty or too sparse** to extract context, fall back to creating a blank file (same as `/scaffold-new-system`) and tell the user why.
- **Pre-filled content is a starting point.** Tell the user to review and refine what was extracted — don't present it as final.
