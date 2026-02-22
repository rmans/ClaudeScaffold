# Resource Definitions

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Status:** Draft

---

## Purpose

Master registry of all game resources — anything the player collects, spends, stores, or transforms. Defines tiers, production chains, storage rules, and categories.

## Resource Categories

<!-- Define broad categories first, then individual resources. -->

| Category | Description |
|----------|-------------|
| *None yet* | — |

<!-- Example:
| Raw Materials | Gathered directly from the map — stone, wood, steel ore |
| Refined Goods | Produced from raw materials — steel bars, planks, cloth |
| Consumables | Used and depleted — food, medicine, ammunition |
| Currency | Abstract value — silver, reputation, influence |
-->

## Resources

<!-- One row per resource. -->

| Resource | Category | Tier | Produced By | Consumed By | Storage Type | Stack Limit | Notes |
|----------|----------|------|-------------|-------------|--------------|-------------|-------|
| *None yet* | — | — | — | — | — | — | — |

<!-- Example:
| Stone      | Raw Materials  | 1 | Mining          | Construction, Stonecutting | Stockpile | 75  | Abundant, heavy    |
| Wood       | Raw Materials  | 1 | Woodcutting     | Construction, Fuel, Crafting | Stockpile | 75  | Burns as fuel      |
| Steel ore  | Raw Materials  | 2 | Deep mining     | Smelting            | Stockpile | 75  | Requires research  |
| Steel bar  | Refined Goods  | 3 | Smelting (ore)  | Advanced construction, Weapons | Stockpile | 50  | 2 ore → 1 bar     |
| Meal       | Consumables    | 2 | Cooking (food)  | Colonist hunger     | Refrigerated | 10 | Spoils without cold |
-->

## Production Chains

<!-- Define multi-step production relationships. -->

*None yet.*

<!-- Example:
### Steel Production
1. **Mine** steel ore (Deep mining → Raw ore)
2. **Smelt** at furnace (2 ore → 1 steel bar, requires Fuel)
3. **Craft** at smithy (steel bar → weapons, armor, components)
-->

## Rules

1. **Every resource must be registered here** before it appears in any system design or implementation.
2. **Tiers indicate complexity.** Tier 1 = gathered directly. Higher tiers require processing from lower-tier inputs.
3. **Production chains must be acyclic.** No resource can be an input to its own production.
4. **Storage type constrains placement.** Resources with special storage needs (refrigerated, secure, etc.) must define those constraints.
