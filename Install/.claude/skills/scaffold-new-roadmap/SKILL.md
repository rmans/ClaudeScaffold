---
name: scaffold-new-roadmap
description: Create the project roadmap by defining phases from start to ship. Use after design docs, systems, and reference docs are complete.
allowed-tools: Read, Edit, Grep, Glob
---

# New Roadmap

Guide the user through creating the project roadmap at `scaffold/phases/roadmap.md`.

## 1. Read Context

1. **Read `scaffold/phases/roadmap.md`** to check its current state.
2. **Read `scaffold/design/design-doc.md`** — especially Core Fantasy, Scope Reality Check, Vertical Slice, and Target Platforms.
3. **Read `scaffold/design/systems/_index.md`** to see all registered systems.
4. **Read `scaffold/decisions/known-issues.md`** and **`scaffold/decisions/design-debt.md`** for open issues.
5. **If the design doc is empty or systems aren't designed**, tell the user to complete those first. Do not proceed with an incomplete foundation.

## 2. Vision Checkpoint

Copy the Core Fantasy from the design doc into the roadmap's Vision Checkpoint section. This anchors every phase to the original vision.

## 3. Define Phases

Walk the user through defining phases one at a time. For each phase, ask:

- *"What's the goal of this phase? What does it prove or deliver?"*
- *"What systems or features are in scope?"*
- *"What's the key deliverable — the thing you can show/play at the end?"*

Typical phase progression (suggest but don't impose):

- **Foundation** — Core loop proof. The smallest playable thing.
- **Systems** — Build out primary systems from system designs.
- **Content** — Populate the world with real content.
- **Polish** — Juice, UX, accessibility, performance.
- **Ship** — Final testing, platform compliance, release.

For each phase, add a row to the Phase Overview table. Mark the first phase as "Active" and the rest as "Planned."

## 4. Set Current Phase

Set the Current Phase section to the first phase with a link.

## 5. Upcoming Phases

Fill in the Upcoming Phases section with brief descriptions of each phase beyond the first.

## 6. Report

Show the user:

- The completed roadmap overview.
- How many phases were defined.
- Reminder that upcoming phases are tentative and will change based on ADRs.
- Suggest running `/scaffold-new-phase` to create the first phase document.

## Rules

- **Ask one phase at a time.** Don't dump all questions at once.
- **Write answers into the roadmap immediately** after the user responds.
- **Use the user's voice.** Capture their intent faithfully — don't rewrite their vision into generic project-management language.
- **If the user says "skip" or "later"**, leave the TODO marker and move on.
- **Phases should be outcome-oriented** ("prove the core loop works") not task-oriented ("implement 5 systems").
- **Reference known issues and design debt** when discussing scope — they may affect phase planning.
- **Remind the user** that the roadmap is a living document that updates after each phase.
