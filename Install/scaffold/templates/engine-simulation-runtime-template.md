# [Engine] — Simulation Runtime

> **Layer:** Implementation
> **Authority:** Rank 9
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Status:** Draft
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

## Purpose

<!-- Why this document exists. What decisions it captures and who should read it. -->

*TODO: Describe the purpose of this simulation-runtime document and its intended audience.*

## Fixed-Step vs Variable-Step

<!-- Whether the simulation runs on a fixed timestep (physics tick) or variable timestep (process frame). Rationale. Tick rate. How the choice affects determinism and reproducibility. -->

*TODO: Define fixed-step vs variable-step policy and tick rate.*

## Where Simulation Ticks Live in the Engine

<!-- Which engine callback drives simulation ticks (_physics_process, _process, custom timer). Which node owns the tick entry point. How the tick relates to the engine's main loop. -->

*TODO: Define where simulation ticks are hosted in the engine loop.*

## Tick Orchestration Implementation

<!-- How systems are ordered within a single tick. The orchestrator pattern. How ordering is defined and enforced. How to add a new system to the tick sequence. -->

*TODO: Define tick orchestration and system ordering.*

## Queued Work Draining

<!-- How deferred work (queued commands, pending spawns, batched updates) is drained during or after the tick. Order of drain passes. Rules for when new work can be enqueued during draining. -->

*TODO: Define queued work draining rules and timing.*

## End-of-Tick Cleanup

<!-- What cleanup runs after all systems have ticked. Freeing destroyed entities, clearing one-shot flags, flushing event queues. Order of cleanup operations. -->

*TODO: Define end-of-tick cleanup operations and ordering.*

## Immediate vs Deferred Transition Mapping

<!-- Which state transitions happen immediately during the tick vs which are deferred to end-of-tick or next tick. How to decide which category a transition belongs to. -->

*TODO: Define immediate vs deferred transition rules.*

## Pause / Speed / Time-Scaling Behavior

<!-- How pause stops the simulation tick without stopping the engine. Speed multiplier implementation. How time-scaling affects tick rate vs tick delta. UI behavior during pause. -->

*TODO: Define pause, speed, and time-scaling behavior.*

## Simulation Update Ordering vs Engine Frame

<!-- How multiple simulation ticks per frame are handled (catch-up). Maximum ticks per frame. How rendering interpolates between simulation states. Frame-skip behavior. -->

*TODO: Define the relationship between simulation updates and engine frames.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
