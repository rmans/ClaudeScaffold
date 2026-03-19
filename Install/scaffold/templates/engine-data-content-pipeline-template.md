# [Engine] — Data / Content Pipeline

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

*TODO: Describe the purpose of this data/content-pipeline document and its intended audience.*

## Content Data vs Runtime State Boundary

<!-- What counts as authored content data (definitions, templates, balance tables) vs runtime state (spawned entities, current HP, task progress). How the two interact but never merge. -->

*TODO: Define the boundary between content data and runtime state.*

## Where Definitions Live

<!-- Directory structure and file formats for authored content definitions. Naming conventions. How definitions are organized (by type, by domain, alphabetical). -->

*TODO: Define where content definitions live and how they are organized.*

## How Authored Data Is Loaded

<!-- Loading pipeline: discovery, parsing, validation, registration. When loading happens (startup, lazy, streaming). Error handling for malformed data. -->

*TODO: Define the authored data loading pipeline.*

## Content ID to Runtime Entity Mapping

<!-- How a content definition ID (e.g., "wall_stone") maps to a runtime entity instance. Registry lookup. Factory patterns. How runtime entities reference back to their definition. -->

*TODO: Define content ID to runtime entity mapping.*

## Validation of Authored Content

<!-- What validation runs on authored content. Schema validation, referential integrity checks, range checks. When validation runs (import time, load time, CI). -->

*TODO: Define content validation rules and when they run.*

## Hot-Reload Policy

<!-- Whether content can be hot-reloaded at runtime during development. Which content types support hot-reload. How hot-reload affects running simulation state. Production behavior. -->

*TODO: Define hot-reload policy.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
