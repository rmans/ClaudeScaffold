# [Engine] — Localization

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

*TODO: Describe the purpose of this localization document and its intended audience.*

## Translation Key Naming Rules

<!-- Naming convention for translation keys. Casing (SCREAMING_SNAKE_CASE). Domain prefixes (UI_, HUD_, MENU_). How to avoid key collisions. -->

*TODO: Define translation key naming conventions.*

## String Ownership Rules

<!-- Which system or file owns each set of strings. How to prevent duplicate keys. Process for adding new keys. -->

*TODO: Define string ownership rules.*

## tr() Usage Rules

<!-- When tr() is required (all player-visible strings). What is exempt (debug output, internal identifiers, signal names). How to enforce compliance. -->

*TODO: Define tr() usage rules and exemptions.*

## Runtime Formatting Rules

<!-- How to format dynamic values into translated strings. Placeholder syntax ({0}, {1}). Use of .format(). Rules for argument ordering across languages. -->

*TODO: Define runtime formatting rules.*

## Pluralization and Grammar Rules

<!-- How to handle plurals, gendered nouns, and grammar variations across languages. Engine support for plural forms. Workarounds for unsupported grammar. -->

*TODO: Define pluralization and grammar handling.*

## Fallback Behavior

<!-- What happens when a translation key is missing for the active locale. Fallback locale chain. How missing keys are surfaced during development. -->

*TODO: Define fallback behavior for missing translations.*

## CSV / Import Pipeline

<!-- Structure of the translation source file (CSV columns, encoding). Import process. How the engine picks up changes. Supported file formats. -->

*TODO: Define the CSV/import pipeline.*

## UI Truncation and Expansion Expectations

<!-- How UI handles strings that are longer or shorter in other languages. Expansion budget (e.g., 40% longer than English). Truncation rules. Ellipsis behavior. Testing with long strings. -->

*TODO: Define UI truncation and expansion expectations.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
