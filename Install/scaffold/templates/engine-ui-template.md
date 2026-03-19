# [Engine] — UI Best Practices

> **Layer:** Implementation
> **Authority:** Rank 9
> **Conforms to:** [design/ui-kit.md](../design/ui-kit.md), [design/style-guide.md](../design/style-guide.md)
> **Status:** Draft
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

## Purpose

<!-- Why this document exists. What decisions it captures and who should read it. -->

*TODO: Describe the purpose of this UI-practices document and its intended audience.*

## UI Ownership and Data Access

<!-- Which systems own UI state. How UI reads simulation data (pull vs push). Rules for UI writing back to simulation (intent only, never direct mutation). -->

*TODO: Define UI ownership boundaries and data-access rules.*

## HUD / Modal / Overlay Distinctions

<!-- Define each UI layer type, its z-ordering, and input-handling rules. When each type is appropriate. How they interact with pause state and game focus. -->

*TODO: Define HUD, modal, and overlay categories and their rules.*

## Layout and Container Rules

<!-- Which container nodes to use for which layout patterns. Margin and padding conventions. Rules for nested containers and max nesting depth. -->

*TODO: Define layout container usage rules.*

## Theme Usage

<!-- How the engine theme system implements the design style guide and color system. Theme resource structure. Override rules for per-widget styling. -->

*TODO: Define theme implementation approach and override rules.*

## UI Update Cadence

<!-- How often UI elements refresh. Signal-driven vs poll-driven updates. Rules for throttling expensive UI updates. Frame-budget allocation for UI. -->

*TODO: Define UI update cadence and refresh rules.*

## Focus and Navigation

<!-- Focus mode settings. Focus neighbor assignment. Keyboard and gamepad navigation patterns. Tab order conventions. Focus trapping in modals. -->

*TODO: Define focus and navigation implementation rules.*

## Responsive Scaling

<!-- Anchor and stretch mode rules. Resolution-independent sizing. How UI scales from 720p through 8K. Banned hardcoded pixel values. Dynamic font sizing. -->

*TODO: Define responsive scaling rules and banned practices.*

## UI Polling and Performance

<!-- UI-specific performance rules: draw call limits, overdraw budgets, batching. When to use VisibilityNotifier. Rules for hiding vs removing off-screen UI. -->

*TODO: Define UI performance guidelines and budgets.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
