# Reference — Index

> **Layer:** Reference — Canonical data tables.
> **Authority:** Rank 6 (per document)

## Purpose

Structured reference material that bridges design to implementation. These documents define the canonical data shapes and tunable values that all layers must respect. Unlike `theory/`, reference docs are actively maintained and carry authority.

## Documents

| File | Purpose |
|------|---------|
| [signal-registry.md](signal-registry.md) | All cross-system signals — names, payloads, emitters, consumers |
| [entity-components.md](entity-components.md) | Every entity's fields grouped by component — types, authority, cadence |
| [resource-definitions.md](resource-definitions.md) | All game resources — tiers, production chains, storage types |
| [balance-params.md](balance-params.md) | All tunable numbers — thresholds, rates, timing, capacities |

## Adding Documents

- Reference-layer docs define canonical data shapes.
- They carry authority over implementation but conform to the design layer.
- New reference docs should be registered in this index and in [doc-authority.md](../doc-authority.md).
