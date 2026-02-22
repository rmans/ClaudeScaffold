# Testing Strategies

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

---

## Purpose

Engine-agnostic testing principles for games — what to test, how to test it, and how to avoid shipping bugs that ruin the player experience.

This document carries no authority. It informs design decisions but never dictates them. If a principle here influences a design change, that change should be captured in an ADR, which is what carries the actual authority.

---

## 1. What to Test

- Not everything needs automated tests. Visual polish, animation feel, and subjective "does this look right" questions are better answered by human eyes than by assertions. Reserve automation for things a machine can verify objectively.
- Prioritize systems where failure is catastrophic: save/load integrity, economy and progression math, state machine transitions, and edge cases in core mechanics. A misaligned particle effect is a polish issue. A corrupted save file is a crisis.
- Test the things that would cause a player to quit permanently — data loss, softlocks, progression blockers, and economy exploits that trivialize the entire game. These are the bugs that generate refund requests and negative reviews.
- If a system touches persistent data (saves, profiles, unlocks, currency), it needs tests. Transient visual state can be verified by eye. Persistent state that is silently wrong will compound into an unfixable mess.
- When deciding whether something needs a test, ask: "If this breaks silently and nobody notices for two weeks, what happens?" If the answer is "we patch it and move on," a test is optional. If the answer is "players lose progress and we have no way to recover it," a test is mandatory.

## 2. Unit Testing Game Logic

- Game logic that is pure math — damage calculation, loot drop probability, experience curves, pathfinding costs, economy formulas — is highly testable and should be tested thoroughly. These are the easiest wins in your test suite.
- Separate logic from engine-specific code. A damage formula that takes attacker stats and defender stats as arguments and returns a number can be tested anywhere. A damage formula that reaches into scene nodes to pull values is untestable outside the engine.
- Deterministic systems are easier to test than stochastic ones. Inject randomness through a seedable interface rather than relying on a global RNG. This lets you write tests that produce the same result every run.
- Test boundary conditions explicitly: zero health, maximum inventory, negative values that should be clamped, division by inputs that could be zero, empty collections where the code assumes at least one element. Boundaries are where bugs hide.
- Keep unit tests fast. If a single test takes more than a few hundred milliseconds, it is probably testing too much. Fast tests get run often. Slow tests get skipped and rot.

## 3. Integration Testing

- Unit tests verify that individual systems work in isolation. Integration tests verify that systems work together — and the seams between systems are where the worst bugs live. Combat interacting with inventory, AI interacting with physics, dialogue interacting with game state — test these intersections.
- Integration tests catch emergent behavior that no unit test can anticipate. A damage formula might be correct and an armor formula might be correct, but the interaction between the two might produce negative damage, healing the target. Only an integration test catches that.
- Keep integration tests focused on one interaction per test. A test that sets up the entire game world and runs a full scenario is not an integration test — it is a fragile end-to-end test that will break constantly and tell you nothing about where the problem is.
- Integration tests need realistic but controlled setup. Use representative game state — not empty defaults and not a full production save. The goal is to exercise the interaction under conditions that resemble actual gameplay without requiring the full engine.
- When an integration test fails, it should be possible to determine which system is at fault within minutes. If debugging an integration failure requires the same effort as debugging a live bug report, the test is too broad.

## 4. Regression Testing

- Every fixed bug gets a test that would have caught it. This is non-negotiable. A bug that is fixed without a regression test is a bug that will return, and next time it will return at the worst possible moment.
- Regression tests are the safety net that lets you refactor confidently. Without them, every structural change to the codebase is a gamble that you have not reintroduced a previously solved problem.
- Automate regression runs on every build. A regression suite that is only run manually before milestones will miss regressions that are introduced between milestones — which is when most regressions are introduced.
- Track which bugs recur despite having regression tests. Recurring bugs indicate structural problems — a fragile architecture, unclear ownership boundaries, or a system that is fundamentally difficult to modify safely. Treat recurrence as a signal to redesign, not just re-fix.
- A growing regression suite is a sign of a maturing project, not a sign of poor quality. Every entry represents a problem that was found, understood, and permanently solved. Projects without regression suites are not bug-free — they just have not checked.

## 5. Smoke Testing and Sanity Checks

- Smoke tests answer one question: "Is the build catastrophically broken?" They do not verify correctness, balance, or polish. They verify that the game launches, loads, and runs without crashing.
- Smoke tests should run in under five minutes. If they take longer, they are doing too much. The purpose is a fast gate that catches total breakage before anyone wastes time on deeper testing.
- If the smoke test fails, nothing else matters — fix it first. A build that does not launch cannot be playtested, demonstrated, or shipped. Smoke failures are stop-the-line events.
- Automate the core smoke path: launch the game, load a save or start a new game, complete one gameplay loop (move, interact, trigger a system), verify no crashes or exceptions. This can run unattended on every build.
- Smoke tests are the first line of defense, not the last. They catch catastrophic breaks early and cheaply, leaving the more expensive and thorough test suites to focus on correctness rather than wasting cycles on a build that cannot even start.

## 6. Edge Cases and Boundary Conditions

- Players will do things you did not expect, did not design for, and did not think were possible. Spam every input simultaneously. Alt-tab during a save. Disconnect the controller mid-action. Pull the network cable during a transaction. Your game needs to survive all of it.
- Test at the extremes of every value range: zero health, maximum level, empty inventory, full inventory plus one more item, zero currency, maximum currency, one frame before a timer expires, one frame after. If a value has a defined range, test both ends and just outside both ends.
- Common edge cases that ship as bugs: dying and pausing simultaneously, opening a menu during a cutscene, filling inventory then receiving a quest reward, saving during a state transition, loading a save from a previous game version. Test these explicitly.
- Edge case testing is where "it works on my machine" goes to die. Test on minimum spec hardware, test with bad network connections, test with unusual input devices, test with saves that are months old. The conditions under which your game will actually be played are far more varied than the conditions under which it was developed.
- When a player reports a bug that involves an unusual sequence of actions, add that exact sequence to your edge case suite. Player-discovered edge cases are worth more than hypothetical ones because they represent real behavior.

## 7. Playtest vs Automated Test

- Automated tests verify correctness — does the system produce the right output for a given input? Playtests verify experience — is the game fun, clear, and satisfying to play? Both are necessary. Neither replaces the other.
- Automated tests run on every build and catch regressions within minutes. Playtests happen at milestones and catch design problems that no automated test can detect: confusing UI, unsatisfying game feel, unclear objectives, pacing issues.
- Automated tests are objective and repeatable. Playtests are subjective and variable. This is not a weakness of playtests — the subjective player experience is exactly what they are designed to evaluate.
- Never use playtest sessions to find bugs that automated tests should catch. If playtesters are reporting crashes, save corruption, or broken progression, your automated test coverage has gaps that need filling. Playtester time is expensive — spend it on questions only humans can answer.
- Feed playtest observations back into automated tests where possible. If playtesters consistently trigger a specific bug through a specific action sequence, automate that sequence so it never ships broken again.

## 8. Determinism and Reproducibility

- A bug you cannot reproduce is a bug you cannot fix. Every investment in reproducibility — logging, state snapshots, input recording — pays for itself the first time it turns a "cannot reproduce" into a five-minute fix.
- Seed your random number generator and log the seed. When a bug occurs during a session with seeded RNG, replaying the same seed reproduces the same sequence of events. Without a seed, you are guessing.
- Record input sequences so sessions can be replayed deterministically. Input replay is the single most powerful debugging tool for gameplay bugs. It turns a vague bug report into an exact reproduction.
- Deterministic game logic — where the same inputs always produce the same outputs — enables replay-based testing at scale. Run thousands of automated playthroughs with different seeds and flag any that produce anomalous results.
- When a bug is reported from outside the team, capture enough state to reproduce it: game version, save file, RNG seed, platform, and a description of the actions taken. A bug report without reproduction steps is a wish, not actionable information.
- Save game state snapshots at regular intervals during play sessions. When something goes wrong, the nearest snapshot provides a starting point that is minutes away from the bug, not hours of manual setup away.
