# [Engine] — Build & Test Workflow

> **Layer:** Implementation
> **Authority:** Rank 9
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Status:** Draft
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

## Purpose

<!-- Define the build, test, and verification workflow for the project. For a simulation-heavy game, testing goes beyond unit tests — it includes simulation correctness, regression detection, and performance validation. -->

*TODO: Define build and test workflow purpose.*

---

## Build Configuration

<!-- Debug vs release builds. What is stripped in release? What is enabled in debug? Export profiles and platform targets. -->

*TODO: Define build configurations and what differs between them.*

---

## Test Layers

<!-- What kinds of tests exist in this project? Unit tests, integration tests, simulation tests, GUT tests, manual playtest scenarios? What does each layer cover? -->

*TODO: Define test layer hierarchy.*

---

## Smoke Test Expectations

<!-- What must pass before a build is considered usable? Minimum bar for "does the game run?" — not full coverage, just sanity. -->

*TODO: Define smoke test criteria.*

---

## Simulation Correctness Tests

<!-- Tests that verify simulation invariants: single-writer violations, stale handle access, state machine illegal transitions, authority conflicts. These go beyond unit tests into cross-system correctness. -->

*TODO: Define simulation correctness test approach.*

---

## Regression Test Expectations

<!-- What regression coverage is expected? When are regression tests added? What triggers a regression test failure to block a build? -->

*TODO: Define regression test policy.*

---

## Performance Test Cadence

<!-- When are performance tests run? What benchmarks exist? What thresholds trigger investigation? How does this relate to the performance budget doc? -->

*TODO: Define performance testing cadence and thresholds.*

---

## CI / Automation

<!-- Is there a CI pipeline? What does it run? Build-only? Build + test? Build + test + lint? What is the expected turnaround time? -->

*TODO: Define CI/automation expectations if applicable.*

---

## Headless Simulation Testing

<!-- Can the simulation run without rendering for automated testing? If so, how? If not, what is the alternative for batch testing simulation logic? -->

*TODO: Define headless simulation testing approach if applicable.*

---

## Project Overrides

<!-- If your project deviates from any convention above, document it here. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

---

## Rules

1. **Every code change must be buildable.** A commit that breaks the build is a bug, not a work-in-progress.
2. **Smoke tests are non-negotiable.** The game must launch and reach a playable state after every significant change.
3. **Simulation tests catch what unit tests miss.** Cross-system invariant checks are as important as per-function tests.
4. **Performance tests prevent silent regression.** Frame budget violations discovered late are expensive to fix.
5. **Test expectations match implementation reality.** Don't require tests that the engine/tooling can't support yet.
