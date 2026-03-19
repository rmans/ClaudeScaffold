# [Engine] — Performance Budget

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

*TODO: Describe the purpose of this performance-budget document and its intended audience.*

## Global Frame Budget

<!-- Target framerate. Total frame-time budget in milliseconds. Minimum hardware spec. Target resolution. -->

*TODO: Define global frame budget and target hardware.*

## CPU Budget

<!-- How CPU frame time is allocated across categories (physics, scripts, AI, simulation). Per-category millisecond budgets. -->

*TODO: Define CPU budget allocation.*

## Memory Budget

<!-- RAM and VRAM limits. Asset size guidelines. Streaming thresholds. Peak memory targets. -->

*TODO: Define memory budget.*

## Render Budget

<!-- Maximum draw calls per frame. Batching strategy. LOD policy. Overdraw limits. Shader complexity rules. -->

*TODO: Define render budget.*

## Per-System / Per-Category Guidance

<!-- Budget guidance for specific systems (e.g., pathfinding, particle effects, audio). How to split the global budget when multiple systems compete for the same resource. -->

*TODO: Define per-system budget guidance.*

## Profiling Tools and Cadence

<!-- Which profiling tools to use. How often to profile. What constitutes a profiling session. How results are recorded and tracked. -->

*TODO: Define profiling tools and cadence.*

## Budget Breach Response

<!-- What happens when a system exceeds its budget. Escalation process. Who decides whether to optimize, cut features, or raise the budget. -->

*TODO: Define budget breach response process.*

## C++ Escalation Criteria

<!-- When performance-critical code should be moved from script to native C++. Metrics thresholds that trigger escalation. Approval process. -->

*TODO: Define C++ escalation criteria and thresholds.*

## Test Scenarios and Benchmark Cases

<!-- Standard benchmark scenarios for measuring performance. Worst-case test maps. Entity count stress tests. Automated performance regression tests. -->

*TODO: Define test scenarios and benchmark cases.*

## Project Overrides

<!-- If your project deviates from any convention above, document it here. Overrides in this section take precedence over the defaults above. Format: what you're overriding, what you do instead, and why. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

## Rules

<!-- Binding rules derived from this document. These are enforced during code review. -->

1. *TODO: Add binding rules that reviewers and implementers must follow.*
