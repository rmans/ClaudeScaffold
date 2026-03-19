# [Engine] — Scene Architecture

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

*TODO: Describe the purpose of this scene-architecture document and its intended audience.*

## Scene Tree Philosophy

<!-- High-level approach to the scene tree. Top-level organization (root, world, UI, services). How the tree reflects the game's logical structure. -->

*TODO: Define the scene tree philosophy and top-level structure.*

## Node Lifecycle and Ownership

<!-- Who creates, owns, and frees nodes. Ownership transfer rules. Rules for add_child/remove_child timing. Queue-free vs immediate-free. Orphan prevention. -->

*TODO: Define node lifecycle and ownership rules.*

## Service vs Node Distinction

<!-- What qualifies as a "service" (stateless or singleton logic) vs a "node" (scene-tree entity with visual/physical presence). How services are accessed. -->

*TODO: Define the service vs node distinction.*

## Instantiation Patterns

<!-- How scenes and nodes are instantiated at runtime. Factory patterns. When to use PackedScene.instantiate() vs direct construction. Deferred instantiation. -->

*TODO: Define instantiation patterns.*

## Packed Scene Conventions

<!-- Naming, directory structure, and composition rules for .tscn files. When to split a scene into sub-scenes. Inheritance vs composition of packed scenes. -->

*TODO: Define packed scene conventions.*

## Pooling and Reuse

<!-- When to pool objects vs create/free on demand. Pool sizing rules. Reset-on-return contracts. Which entity types are candidates for pooling. -->

*TODO: Define pooling and reuse rules.*

## Singleton / Autoload Policy

<!-- Which systems qualify as autoloads. Naming conventions. Initialization order. Rules limiting autoload count. Alternatives to autoloads (service locators, dependency injection). -->

*TODO: Define singleton and autoload policy.*

## Allowed Communication Paths

<!-- Approved patterns for node-to-node communication: signals, direct reference via get_node, service locator, event bus. When each is appropriate. -->

*TODO: Define allowed communication paths and when to use each.*

## Forbidden Communication Patterns

<!-- Banned patterns: deep get_node paths across unrelated branches, global mutable state, circular signal chains, polling for references every frame. Rationale for each ban. -->

*TODO: Define forbidden communication patterns and rationale.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
