# [Engine] — Coding Best Practices

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

*TODO: Describe the purpose of this coding-practices document and its intended audience.*

## C++ vs Scripting Boundary

<!-- Define the boundary between native (C++/GDExtension) code and scripted (GDScript) code. Which responsibilities belong in each layer. When to escalate logic from script to native. -->

*TODO: Define the C++ vs scripting boundary rules.*

## Naming Conventions

<!-- Naming rules for classes, functions, variables, signals, files, and directories. Casing style per language. Prefixes or suffixes for special types (e.g., I_ for interfaces, _System for systems). -->

*TODO: Define naming conventions for all code and file artifacts.*

## Signal Usage Policy

<!-- When to use signals vs direct calls. Signal naming conventions. One-to-many vs one-to-one patterns. Rules for signal registration and connection lifetime. -->

*TODO: Define signal usage policy and naming rules.*

## Node Ownership and Lifetime

<!-- Who creates and frees nodes. Ownership transfer rules. Orphan prevention. Rules for add_child/remove_child timing. Queue-free vs immediate-free. -->

*TODO: Define node ownership and lifetime management rules.*

## Serialization-Safe Coding

<!-- Rules that keep runtime state serializable. Which types are safe to persist. Avoiding closures, lambdas, or engine objects in saved state. Handle vs raw-reference policy. -->

*TODO: Define serialization-safe coding rules.*

## Testing Expectations

<!-- Testing approach, tools, and coverage expectations. Unit test framework. What must be tested vs what is tested manually. Test naming and organization. -->

*TODO: Define testing strategy and expectations.*

## Allowed Patterns

<!-- Explicitly approved patterns: composition, observer, state machine, command, etc. For each, state when to use it and link to the engine-implementation-patterns doc if available. -->

*TODO: List allowed coding and architecture patterns.*

## Forbidden Patterns

<!-- Explicitly banned patterns and why. Examples: global mutable state outside autoloads, direct cross-system writes, circular signal chains, polling in _process when signals suffice. -->

*TODO: List forbidden patterns and rationale.*

## Project Coding Patterns

<!-- Prescribed coding patterns that are project-specific — not universal engine conventions, but mandated by architecture decisions. These translate architecture.md Code Patterns (design-layer WHAT) into engine-level implementation (HOW). Each pattern should include: name, when to use, structure/template, and a concrete code example.

Common project coding patterns include:
- System resolution (how systems find each other — e.g., get_parent()->get_node_or_null() in _ready())
- Entity handle validation (how code checks handle validity before use)
- Query API return conventions (Dictionary returns, null/empty conventions)
- Entity storage access (SlotPool usage, iteration patterns)
- Signal wiring patterns (where and how signals are connected)
- Intent/request object patterns (how intents flow from UI to simulation)
- Error recovery patterns (what code does when a dependency is null, a handle is stale, or state is invalid)

These patterns are derived from architecture.md but expressed as concrete engine-level code. If a pattern here conflicts with architecture.md, architecture wins — update this section. If a pattern becomes broadly useful beyond this project, consider whether it belongs in Allowed Patterns instead. -->

### Pattern: [Name]

**When to use:** ...
**Structure:**
```
// code template
```
**Example:**
```
// concrete usage
```

*TODO: Add project coding patterns derived from architecture.md.*

---

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
