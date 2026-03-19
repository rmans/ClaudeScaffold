# [Engine] — AI Task Execution

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

*TODO: Describe the purpose of this AI-task-execution document and its intended audience.*

## Task Reservation Lifecycle

<!-- The full lifecycle of a task reservation: creation, assignment, active, completion, cancellation. State diagram. Which system owns each transition. -->

*TODO: Define the task reservation lifecycle and state transitions.*

## Claim / Lock Ownership Implementation

<!-- How an agent claims a task or resource. Lock granularity (per-entity, per-tile, per-item). How ownership is tracked. Rules preventing double-claims. -->

*TODO: Define claim and lock ownership implementation.*

## Interruption and Retry Semantics

<!-- What happens when a task is interrupted (higher-priority need, target became invalid, path blocked). Difference between interrupt (recoverable) and cancel (permanent). Retry policy. -->

*TODO: Define interruption and retry semantics.*

## Job Selection Flow

<!-- How an idle agent selects its next task. Priority scoring. Distance weighting. Skill/capability filtering. Tie-breaking rules. -->

*TODO: Define the job selection flow and priority rules.*

## Recovery When Targets Disappear

<!-- What happens when a task's target entity is destroyed, moved, or becomes invalid mid-task. Search-and-relocate patterns. When to give up vs retry. -->

*TODO: Define recovery behavior when targets disappear.*

## Stale-Handle Cleanup

<!-- How stale handles (referencing freed entities) are detected and cleaned up. Periodic scan vs lazy detection. Diagnostic warnings for stale handles. -->

*TODO: Define stale-handle cleanup strategy.*

## Actor Arbitration Patterns

<!-- How conflicts between multiple agents targeting the same resource are resolved. First-come-first-served vs priority-based. Deadlock prevention. -->

*TODO: Define actor arbitration patterns.*

## Multi-Phase Task Structure

<!-- How complex tasks are broken into sequential phases (e.g., pick up item, walk to target, deliver item). Phase transition rules. Handling failure at any phase. -->

*TODO: Define multi-phase task structure and phase transition rules.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
