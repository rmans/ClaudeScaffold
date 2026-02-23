---
name: scaffold-new-prototype
description: Create a new prototype document for a throwaway code spike. Walks through question, hypothesis, scope, and approach interactively with auto-ID assignment.
argument-hint: [prototype-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# New Prototype

Create a new prototype document for: **$ARGUMENTS**

## Steps

### 1. Read Context

1. **Read the prototype template** at `scaffold/templates/prototype-template.md`.
2. **Read the prototypes index** at `scaffold/prototypes/_index.md` to find the next available PROTO-### ID.
3. **Read the design doc** at `scaffold/design/design-doc.md` for project context.
4. **Read the systems index** at `scaffold/design/systems/_index.md` to identify valid system references.
5. **Read relevant engine docs** from `scaffold/engine/` if the prototype involves engine-level questions.
6. **Read all ADRs** — Glob `scaffold/decisions/ADR-*.md` — to check if this question has already been decided.

### 2. Determine the Next PROTO ID

Find the highest existing PROTO-### number in `scaffold/prototypes/_index.md`. The new prototype gets the next sequential ID. If no prototypes exist yet, start at PROTO-001.

### 3. Pre-Check: Is This Actually a Prototype?

Before proceeding, verify the question fits prototype criteria:

- **Specific and answerable** — not a broad design exploration.
- **Requires building to answer** — can't be resolved by reading docs alone.
- **Not already decided** — no existing ADR that resolves this question.

If the user's question is too broad, help them narrow it to a single specific question. If it's already answered by existing docs or ADRs, point them there instead.

### 4. Interactive Walkthrough

Walk the user through each pre-spike section one at a time:

1. **Question** — *"What single question does this prototype answer?"* Help refine until it's specific and answerable. Reject compound questions — each prototype gets ONE question.
2. **Hypothesis** — *"What do you expect the answer to be, and why?"* A hypothesis without reasoning is just a guess.
3. **Scope: Build** — *"What's the minimum you need to build to answer the question?"* Push back on scope creep. If they list more than ~5 build steps, the prototype is too big — suggest splitting.
4. **Scope: Skip** — *"What are you explicitly NOT building?"* This section is a discipline boundary. The more explicit the exclusions, the better.
5. **Approach** — *"How will you execute this spike?"* Numbered steps. Optionally ask about a time box.
6. **Related Documents** — *"Which scaffold docs raised this question?"* Suggest references based on the question's domain (systems, engine docs, specs, etc.).

Write each section immediately after the user confirms it.

### 5. Create the Prototype File

Create `scaffold/prototypes/PROTO-###-<name>.md` where `<name>` is a lowercase-kebab-case version of the prototype name.

- Replace `PROTO-###` in the title and header with the actual ID.
- Replace `[Prototype Name]` with the provided name.
- Fill in all pre-spike sections from the walkthrough.
- Leave all post-spike sections (Answer, Evidence, Surprises, Design Impact, ADRs Filed, Disposition) as TODO markers.
- Set Status to Draft.

### 6. Register

Add a row to the Prototype Registry table in `scaffold/prototypes/_index.md`:
- ID, Name, Question (short summary), Status: Draft, Disposition: —, ADRs Filed: —

### 7. Report

Show the user:
- The file path and assigned PROTO-### ID
- A summary of the question and hypothesis
- Scope boundaries (build vs skip)
- Reminder that post-spike sections should be filled using `/scaffold-prototype-log` when the spike is complete
- Reminder to run `/scaffold-review-prototype` to audit the prototype before starting the spike

## Rules

- **Never overwrite an existing prototype file.**
- **IDs are sequential and permanent** — never skip or reuse.
- **If no prototype name is provided**, ask the user for one before proceeding.
- **ONE question per prototype.** If the user has multiple questions, create multiple prototypes.
- **Push back on scope creep.** The whole point of a prototype is a narrow, focused spike. If Build scope exceeds ~5 steps, suggest splitting.
- **Check ADRs first.** If an ADR already answers the question, point the user there instead of creating a prototype.
- **Created documents start with Status: Draft.**
- **Post-spike sections stay as TODOs.** Never fill Answer, Evidence, Surprises, Design Impact, ADRs Filed, or Disposition at creation time.
