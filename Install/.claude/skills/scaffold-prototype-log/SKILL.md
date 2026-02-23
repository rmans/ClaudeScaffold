---
name: scaffold-prototype-log
description: Log findings from a completed prototype spike. Captures answer, evidence, surprises, design impacts, files ADR stubs, and sets disposition.
argument-hint: [PROTO-### or prototype-name]
allowed-tools: Read, Edit, Write, Grep, Glob
---

# Log Prototype Findings

Capture findings from a completed spike for: **$ARGUMENTS**

## Locate the Prototype

1. If the argument is a PROTO-### ID, look for the matching file in `scaffold/prototypes/`.
2. If the argument is a name, search `scaffold/prototypes/_index.md` for a matching entry and find the file.
3. If no argument is provided, list all Draft or In Progress prototypes and ask the user which one to log findings for.
4. If the prototype file doesn't exist, report that and stop.

## Steps

### 1. Read Context

1. **Read the prototype file** — note the Question, Hypothesis, and Scope.
2. **Read the prototypes index** at `scaffold/prototypes/_index.md`.
3. **Read the decision template** at `scaffold/templates/decision-template.md` — needed for filing ADR stubs.
4. **Read the decisions index** at `scaffold/decisions/_index.md` to find the next available ADR-### ID.
5. **Read all existing ADRs** — Glob `scaffold/decisions/ADR-*.md` — to avoid duplicate ADRs.
6. **Read the related documents** listed in the prototype's Related Documents section.

### 2. Update Status

Set the prototype's Status from Draft/In Progress to Complete (update both the file header and the index).

### 3. Capture Findings

Walk the user through each post-spike section one at a time:

1. **Answer** — *"What's the direct answer to your question: '[Question from prototype]'?"*
   - The answer should directly address the Question. If it doesn't, ask the user to refine.
   - Compare to the Hypothesis — was it confirmed, partially confirmed, or wrong?

2. **Evidence** — *"What specific measurements, observations, or outputs support this answer?"*
   - Push for specifics: numbers, timings, error messages, screenshots, test results.
   - Reject vague evidence like "it seemed to work fine."

3. **Surprises** — *"Did you discover anything unexpected during the spike?"*
   - Surprises are often the highest-value output of a prototype.
   - If there were no surprises, explicitly note "None" — don't leave it blank.
   - For each surprise, ask: *"Does this affect any design decisions?"*

4. **Design Impact** — *"Based on your findings, which scaffold documents need to change?"*
   - Walk through the findings and related documents.
   - For each impacted document, ask what needs to change and the severity (High / Medium / Low).
   - Fill in the Design Impact table.

5. **Disposition** — *"What happens to the spike code?"*
   - **Discarded** — code deleted, only the document remains. This is the default.
   - **Archived** — code kept in `prototypes/spikes/` for reference but not production-ready.
   - **Absorbed** — code will be refactored into the real codebase via a TASK-###. Ask for the task reference.

Write each section immediately after the user confirms it.

### 4. File ADR Stubs

For each entry in the Design Impact table:

1. **Check if an ADR already covers this impact.** If yes, reference the existing ADR instead of creating a new one.
2. **If no existing ADR covers it**, create a new ADR stub:
   - Assign the next sequential ADR-### ID.
   - Create `scaffold/decisions/ADR-###-<name>.md` from the decision template.
   - Fill in: Title (from impact), Status (Proposed), Context (from prototype findings), Decision (TODO — needs discussion), Consequences (from Design Impact severity).
   - Reference the prototype PROTO-### as the source.
   - Register in `scaffold/decisions/_index.md`.
3. **Update the prototype's ADRs Filed table** with each ADR-### and summary.

### 5. Update Registry

Update the prototype's row in `scaffold/prototypes/_index.md`:
- Status: Complete
- Disposition: [as chosen]
- ADRs Filed: [comma-separated ADR-### IDs]

### 6. Report

Show the user:
- Prototype ID and name
- Answer summary (confirmed/refuted hypothesis)
- Number of surprises logged
- Design impacts identified: N documents affected
- ADRs filed: N new, N existing referenced
- Disposition chosen
- Reminder to review the filed ADRs and move them from Proposed to Accepted
- Reminder to run `/scaffold-review-prototype` for a quality audit of the completed prototype

## Rules

- **Answer must directly address the Question.** If the user's answer doesn't match the question, help them refine it.
- **Evidence must be specific.** Push back on vague claims. Numbers, timings, and concrete observations only.
- **Every Design Impact should produce an ADR.** If the user identifies a design impact but doesn't want to file an ADR, flag this as a gap.
- **Write immediately.** Don't wait until the end to update the file.
- **ADR stubs are stubs, not complete ADRs.** The Decision section is TODO — it needs team discussion. Only Context and Consequences are filled from prototype findings.
- **IDs are sequential and permanent** — never skip or reuse PROTO-### or ADR-### IDs.
- **Disposition defaults to Discarded.** The spike code is throwaway unless there's a specific reason to keep it.
- **If the prototype is still Draft**, update its Status to In Progress before logging findings, or ask if the user wants to complete it now.
