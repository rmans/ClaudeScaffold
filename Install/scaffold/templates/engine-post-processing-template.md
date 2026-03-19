# [Engine] — Post-Processing

> **Layer:** Implementation
> **Authority:** Rank 9
> **Conforms to:** [design/design-doc.md](../design/design-doc.md), [design/style-guide.md](../design/style-guide.md)
> **Status:** Draft
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

## Purpose

<!-- Why this document exists. What decisions it captures and who should read it. -->

*TODO: Describe the purpose of this post-processing document and its intended audience.*

## Scope vs Style / Art Docs

<!-- What this document covers (engine-side implementation of visual effects) vs what belongs in design/style-guide.md or art direction docs (aesthetic intent). This doc is HOW, not WHAT. -->

*TODO: Define the boundary between this doc and style/art docs.*

## Approved Effect Categories

<!-- List of approved post-processing effect categories (e.g., color grading, bloom, vignette, screen shake). Each must have a design justification. No effects without design approval. -->

*TODO: List approved effect categories and their design justification.*

## Global vs Contextual Effects

<!-- Which effects are always active (global) vs triggered by game state (contextual). How contextual effects are activated and deactivated. Blending rules when multiple contextual effects overlap. -->

*TODO: Define global vs contextual effect rules.*

## Runtime Cost Limits

<!-- Per-effect and total post-processing frame budget in milliseconds. Maximum shader passes. Rules for scaling down effects on lower-end hardware. -->

*TODO: Define runtime cost limits for post-processing.*

## Readability Safeguards

<!-- Rules ensuring post-processing never obscures gameplay-critical information. Minimum contrast requirements. Effects that must be disabled or reduced during critical gameplay moments. -->

*TODO: Define readability safeguards.*

## UI Overlay Interaction Rules

<!-- How post-processing interacts with UI layers. Whether UI is rendered before or after post-processing. Rules for effects that should not apply to UI (e.g., blur, color grading). -->

*TODO: Define UI overlay interaction rules.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
