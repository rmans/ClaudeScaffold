---
name: scaffold-playtest-log
description: Log playtester observations into the feedback tracker. Captures observations, detects duplicates, and promotes patterns at 3+ reports.
argument-hint: [session-type]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Log Playtest Feedback

Capture playtester observations for: **$ARGUMENTS**

## Steps

### 1. Read Context

1. **Read playtest feedback** at `scaffold/decisions/playtest-feedback.md` — note existing entries and the next available PF-### ID.
2. **Read the systems index** at `scaffold/design/systems/_index.md` to identify valid system references.
3. **Read known issues** at `scaffold/decisions/known-issues.md` — be aware of existing known issues to avoid logging duplicates across trackers.
4. **Read design debt** at `scaffold/decisions/design-debt.md` — same reason.
5. **Read theory** at `scaffold/theory/playtesting-guidelines.md` for methodology context (Rule of Three, behavior > words, severity x frequency grid).

### 2. Create or Identify Session

Ask the user: *"Is this a new playtest session or are you adding observations to an existing session?"*

**If new session:**
1. Generate a session ID: `PT-YYYY-MM-DD` (use today's date; append `-2` if one already exists for today).
2. Ask for session details: Type (In-person / Remote / Self-play), number of testers, focus area, and current phase.
3. Add a row to the **Playtest Sessions Log** table in `playtest-feedback.md`.
4. Optionally ask if the user wants a detailed session doc created from `scaffold/templates/playtest-session-template.md` in a `scaffold/playtests/` directory.

**If existing session:**
1. Show the Sessions Log and ask which session.
2. Use that session ID for all new entries.

### 3. Capture Observations

Capture observations one at a time. For each observation, ask:

1. **Type** — Confusion, Frustration, Delight, Suggestion, or Bug?
2. **Observation** — *"What did the tester do or say? Describe behavior, not interpretation."*
3. **System/Spec** — Which system or spec does this relate to? (Suggest based on context.)
4. **Severity** — High / Medium / Low?
5. **Frequency** — How many testers out of total exhibited this? (e.g., `2/4`)

Write each observation into the Open Feedback table immediately after confirmation.

After each entry, ask: *"Any more observations from this session?"* Continue until the user says no.

### 4. Duplicate Check

Before adding each observation, check existing entries in the Open Feedback and Patterns tables:

- **Exact match:** If the same observation already exists, update the frequency count (e.g., `2/4` → `3/4` if new testers show the same issue) and add the new session ID to the Source column. Do not create a duplicate row.
- **Similar match:** If a similar but not identical observation exists, present both and ask the user whether to merge or keep separate.

### 5. Pattern Detection

After adding all observations, scan the updated Open Feedback table:

- **3+ frequency on any entry:** Prompt the user — *"PF-### has been reported by 3+ testers. Promote to a Pattern?"*
- If yes:
  1. Move the entry to the **Patterns (Rule of Three)** table.
  2. Set Status to `Pattern` in the Open Feedback table.
  3. Ask: *"What action should be taken?"* (e.g., "Add to next phase scope", "Create a spec", "File a known issue").
  4. Fill in the Action Taken column.
- If no, leave it in Open Feedback.

### 6. Report

Show the user:

- Number of observations logged in this session.
- Any duplicates that were merged (with updated frequencies).
- Any entries promoted to Patterns.
- Suggest running `/scaffold-playtest-review` for a full analysis if 10+ entries exist.

## Rules

- **Observations, not prescriptions.** Capture what testers did and said. If the user tries to log a solution instead of an observation, ask them to reframe.
- **Behavior > words.** Prioritize what testers *did* over what they *said*. A tester who says "this is fine" while struggling for 3 minutes is frustrated.
- **One observation at a time.** Don't batch. Walk through each observation sequentially.
- **Write immediately.** Don't wait until the end to update the file.
- **Aggregate, don't duplicate.** If the same issue appears again, update frequency — don't add a new row.
- **IDs are sequential and permanent** — never skip or reuse PF-### IDs.
- **Session IDs use date format** — `PT-YYYY-MM-DD`.
- **If no argument is provided**, ask the user whether this is a new or existing session before proceeding.
