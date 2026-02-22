---
name: scaffold-new-system
description: Scaffold a new system design file from the template. Use when adding a new game system to the design.
argument-hint: [system-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# New System Design

Create a new system design document for: **$ARGUMENTS**

## Steps

1. **Read the system template** at `scaffold/templates/system-template.md`.

2. **Determine the next SYS ID.** Read `scaffold/design/systems/_index.md` and find the highest existing SYS-### number. The new system gets the next sequential ID (e.g., if SYS-002 exists, the new one is SYS-003). If no systems exist yet, start at SYS-001.

3. **Create the system file.** Copy the template to `scaffold/design/systems/SYS-###-<name>.md` where `<name>` is a lowercase-kebab-case version of the system name argument. Fill in:
   - Replace `SYS-###` in the title with the actual ID.
   - Replace `[System Name]` with the provided name.
   - Leave all other sections as template prompts for the user to fill in.

4. **Register in the systems index.** Edit `scaffold/design/systems/_index.md` — add a row to the Registered Systems table:
   - ID: the new SYS-### ID
   - Name: the system name
   - One-Line Purpose: leave as *TODO*
   - Status: Draft

5. **Register in the design doc.** Edit `scaffold/design/design-doc.md` — add a row to the System Design Index table:
   - ID: the new SYS-### ID
   - System: the system name
   - One-Line Purpose: leave as *TODO*
   - Status: Draft

6. **Report what was created.** Show the user the file path, the assigned ID, and remind them to fill in the system design sections.

## Rules

- Never overwrite an existing system file.
- IDs are permanent and sequential — never reuse or skip.
- If no system name is provided in the arguments, ask the user for one before proceeding.
- Keep both index tables in sync — the design doc and systems/_index.md must always match.
