# [Engine] — Save / Load

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

*TODO: Describe the purpose of this save/load document and its intended audience.*

## Serialization Boundaries

<!-- What is saved to disk vs what is reconstructed at load time. Which state is canonical (persisted) and which is derived (rebuilt from persisted state). -->

*TODO: Define what is saved vs what is reconstructed.*

## Save Snapshot vs Incremental Persistence

<!-- Whether saves capture a full snapshot or use incremental/delta persistence. When saves are triggered (autosave cadence, manual save). Atomicity guarantees. -->

*TODO: Define snapshot vs incremental persistence strategy.*

## Entity Restoration Order

<!-- The order in which entities, systems, and resources are restored during load. Dependency ordering. How to handle circular restore dependencies. -->

*TODO: Define entity restoration order and dependency rules.*

## Handle Rebind / Reference Repair

<!-- How runtime handles (entity IDs, generational handles, node references) are rebound after load. How stale references are detected and repaired. -->

*TODO: Define handle rebinding and reference repair rules.*

## Restoring In-Flight Tasks / Reservations / Queued Intents

<!-- How tasks, reservations, and queued intents that were active at save time are restored. Whether they resume, restart, or are cancelled. Edge cases for half-completed operations. -->

*TODO: Define rules for restoring in-flight work.*

## Post-Load Validation and Cleanup

<!-- Validation pass that runs after all state is restored. Invariant checks. How to handle corrupt or inconsistent save data. Cleanup of orphaned state. -->

*TODO: Define post-load validation and cleanup pass.*

## Versioning and Migration

<!-- Save format version numbering. How old saves are migrated to new formats. Breaking vs non-breaking changes. Migration function structure. -->

*TODO: Define versioning and migration rules.*

## File Format and Location

<!-- Save file format (binary, JSON, custom). File extension. Save directory location per platform. File naming conventions. Backup/rotation policy. -->

*TODO: Define file format, location, and naming conventions.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
