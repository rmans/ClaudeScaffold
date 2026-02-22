# Playtesting Guidelines

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

---

## Purpose

A reference for planning, running, and interpreting playtests. Playtesting is the primary way to validate design assumptions against real player behavior. This document provides structured guidance but carries no authority over design or implementation decisions.

---

## 1. Types of Playtests

- **Internal playtests** use team members or close collaborators. They catch broken mechanics, missing feedback, and pacing problems early. Run these frequently -- they are cheap and fast.
- **External playtests** use people outside the team who have no insider knowledge. They reveal onboarding failures, unclear UI, and hidden assumptions. Run these at milestone boundaries.
- **Focus tests** isolate a single feature or system (e.g., "Can players figure out the crafting menu?"). Use these when you have a specific hypothesis to validate.
- **Full session tests** let the player engage with the game naturally from start to finish. Use these to evaluate pacing, flow, and overall feel.
- **First-time player tests** are the most valuable for onboarding and discoverability. A feature that is obvious to the team may be invisible to a new player.
- **Experienced player tests** reveal depth problems, balance issues, and late-game pacing. Use these after core systems are stable.

---

## 2. Setting Up a Playtest

- **Define a hypothesis before starting.** Write one sentence: "I believe the player will [expected behavior] when they encounter [feature/situation]." If you cannot state the hypothesis, you are not ready to test.
- **Test one thing at a time.** A playtest that tries to validate combat, crafting, and UI simultaneously will produce noise, not signal. Scope each session to one focus area.
- **Prepare an observation sheet.** List the specific moments or decisions you want to watch for. Without a sheet, you will forget what you saw by the time you debrief.
- **Record the session if possible.** Screen capture with face cam is ideal. At minimum, record the screen. Recordings let you re-watch moments you missed live.
- **Set a time limit.** Tell the tester how long the session will take and stick to it. Fatigue degrades feedback quality. 20-40 minutes is a good default for focus tests.
- **Ensure the build is stable.** Crashes and unrelated bugs waste the tester's time and contaminate your observations. Fix known blockers before the session.

---

## 3. During the Playtest

- **Do not help the player.** If they are stuck, let them be stuck. The moment you say "try clicking there," you have invalidated the test. Your goal is to see what happens without you.
- **Do not explain mechanics.** If the player asks "what does this do?" during the test, note it as a failure of in-game communication. The game must teach itself.
- **Note where they get stuck.** Write down the exact moment, what they were trying to do, and how long they spent. Friction points are your most valuable data.
- **Note where they get confused.** Confusion is different from difficulty. A player who understands the challenge but fails is having a difficulty moment. A player who does not know what to do is having a confusion moment. Track both separately.
- **Note where they get bored.** Watch for alt-tabbing, phone checking, sighing, or repetitive clicking without purpose. Boredom means the challenge-reward loop has stalled.
- **Watch body language.** Leaning forward means engagement. Leaning back means disengagement. Furrowed brow means concentration or frustration. Smiling means you did something right.

---

## 4. Questions to Ask

- **"What did you enjoy most?"** — Opens with a positive frame and reveals what the player values. Protect whatever they name here.
- **"What confused you?"** — Direct and non-judgmental. Better than "was anything confusing?" which invites a polite "no."
- **"What would you do next if you kept playing?"** — Reveals whether the player has formed goals and expectations. If they have no answer, the game has not given them enough motivation.
- **"Was there a moment you wanted to quit?"** — Identifies the hardest friction points. If multiple testers name the same moment, it needs redesign.
- **Avoid leading questions.** "Did you find the combat too hard?" tells the player what answer you expect. Instead ask "How did the combat feel?" and let them choose the direction.
- **Ask about feelings, not solutions.** Players are reliable reporters of their experience ("I felt lost") but unreliable designers ("you should add a minimap"). Collect the problem, not the prescription.

---

## 5. Common Biases

- **Confirmation bias.** You see what you want to see. If you built the feature, you will unconsciously focus on the moments it works and downplay the moments it fails. Have someone else observe alongside you or review the recording independently.
- **Familiarity bias.** You have played your own game hundreds of times. Things that are "obvious" to you are invisible to a new player. Never assume the player knows what you know.
- **Recency bias.** The last playtest session overwrites your memory of earlier ones. Keep written notes from every session and compare them side by side, not from memory.
- **Politeness bias.** Testers do not want to hurt your feelings, especially friends and family. They will say "it's fun" even when it is not. Watch what they do, not just what they say. Actions during the test are more honest than words after it.
- **Sample-size-of-one bias.** A single tester's strong reaction can dominate your thinking. One person hating a feature is an anecdote. Five people hating it is a pattern.

---

## 6. Interpreting Results

- **Behavior outweighs words.** If a tester says "the controls felt fine" but fumbled the same input three times during the session, the controls are not fine. Observation data trumps interview data.
- **The rule of three.** If three or more testers independently hit the same wall, it is a design problem, not a player problem. Do not rationalize it away.
- **One complaint is a data point, not a verdict.** A single tester disliking a feature may reflect personal preference. Note it, but do not redesign around it unless it recurs.
- **Separate confusion from difficulty.** A player who understands the mechanic but fails the challenge may be having a fair difficulty experience. A player who does not understand the mechanic at all has encountered a communication failure. The fixes are different.
- **Look for silent successes.** If every tester completes a section without comment or hesitation, that section is working. Do not over-iterate on things that are already good.

---

## 7. Acting on Feedback

- **Prioritize by frequency and severity.** A problem that blocks progress for most testers is higher priority than a minor annoyance reported by one. Plot feedback on a frequency-vs-severity grid to see what matters most.
- **Not all feedback requires action.** Some feedback reflects the tester's genre preferences, personal taste, or play style. If the feedback contradicts the design vision and only comes from one person, it is safe to acknowledge and set aside.
- **Distinguish "this is confusing" from "I don't like this genre."** A puzzle-hating player will report that puzzles are bad. That does not mean your puzzles are bad. Know your target audience and filter feedback accordingly.
- **Fix the problem, not the symptom.** If testers say "I keep dying here," the answer might not be making the section easier. It might be giving better feedback before the danger, or teaching the mechanic earlier.
- **Track what you changed and why.** After acting on feedback, note which playtest data drove the change. This prevents circular redesign where you fix something, break something else, and forget why the original change was made.

---

## 8. Metrics Worth Tracking

- **Time to first death.** How long before the player fails for the first time? Too early suggests insufficient onboarding. Too late suggests insufficient challenge.
- **Time to complete tutorial.** Measures how effectively the game teaches its core mechanics. Compare across testers to spot outliers who got stuck.
- **Drop-off points.** Where do players stop playing voluntarily? If multiple testers quit at the same point, that section has a retention problem.
- **Session length.** How long players choose to play when given no time constraint. Longer is not always better -- look for whether they stopped at a natural break or out of frustration.
- **Retry rate.** How often players attempt a challenge again after failing. High retry rate means the challenge feels fair and motivating. Low retry rate means the player has given up or lost interest.
- **Menu navigation time.** How long players spend in menus versus gameplay. Excessive menu time may indicate unclear UI, too many options, or information overload.
