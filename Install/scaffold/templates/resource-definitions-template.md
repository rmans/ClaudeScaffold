# Resource Definitions

> **Authority:** Rank 6
> **Layer:** Reference
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Status:** Draft
> **Changelog:**
> - YYYY-MM-DD: Initial creation.

---

## Purpose

Master registry of all game resources — anything the player collects, spends, stores, or transforms. Defines tiers, production chains, storage rules, and categories.

## Tier Definitions

| Tier | Meaning |
|------|---------|
| 1 | Gathered, harvested, or hunted directly — no processing required |
| 2 | Basic processing — one crafting step at a single station |
| 3 | Advanced processing — multiple crafting steps, multiple station types, or rare inputs |
| 4 | Import only — cannot be produced locally |

## Storage Types

| Type | Description |
|------|-------------|
| Bulk | Loose raw mass; outdoor stockpiles or bulk bins |
| Stockpile | Processed and packaged goods; shelving or crates |
| Refrigerated | Perishable goods; require powered cold storage or spoil |
| Secure | High-value or hazardous items; locked or shielded storage |

<!-- Add additional storage types as needed. -->

## Resource Categories

| Category | Count | Description |
|----------|-------|-------------|
| ... | ... | ... |
| **Total** | **...** | |

---

## [Category Name]

<!-- One section per resource category. Use the table format appropriate to the category:

For raw/gathered resources (no recipe):
| Resource | Tier | Source | Storage | Notes |
|----------|------|--------|---------|-------|

For processed resources (require crafting):
| Resource | Tier | Recipe | Station | Storage | Notes |
|----------|------|--------|---------|---------|-------|

For special resources (unique acquisition):
| Resource | Tier | Source | Storage | Notes |
|----------|------|--------|---------|-------|
-->

| Resource | Tier | Source | Storage | Fungibility | Physical / Abstract | Transportability | Notes |
|----------|------|--------|---------|-------------|---------------------|-------------------|-------|
| ... | ... | ... | ... | fungible / unique | Physical / Abstract | hauled / piped / instant / immovable | ... |

<!-- Fungibility values:
  - fungible: Interchangeable units — any unit of this resource is identical to any other (e.g., raw ore, food rations).
  - unique: Each instance has distinct identity or properties (e.g., named artifacts, colonist-crafted items with quality).

Physical / Abstract values:
  - Physical: Exists in the game world, occupies storage space, must be transported.
  - Abstract: A conceptual quantity (e.g., research points, morale score, power capacity). No physical presence.

Transportability values:
  - hauled: Must be physically carried by a colonist or vehicle.
  - piped: Transported through infrastructure (pipes, wires, conveyors).
  - instant: Transferred instantly (abstract resources, global pools).
  - immovable: Cannot be moved once placed (e.g., installed structures, terrain features).
-->

---

<!-- Repeat for each resource category. -->

## Resource State Variants

<!-- Some resources can exist in multiple states (raw vs. processed, fresh vs. spoiled, charged vs. depleted). Track those variants here so that state transitions are explicit and systems know which variant they're working with. -->

| Resource | Variant | Transition From | Trigger | Notes |
|----------|---------|-----------------|---------|-------|
| ... | ... | Base resource or prior variant | What causes the transformation | ... |

<!-- Examples:
  - Food → Spoiled Food (triggered by expiry timer, no refrigeration)
  - Raw Ore → Refined Metal (triggered by smelting at a furnace)
  - Battery → Depleted Battery (triggered by charge reaching 0)
-->

---

## Production Chains

<!-- Define the transformation chains: which raw resources become which processed resources, through which stations. -->

### [Chain Name] Chain

| Input | Station | Output | Notes |
|-------|---------|--------|-------|
| ... | ... | ... | ... |

---

## Production Stations

<!-- Registry of all crafting/processing stations. -->

| Station | Recipes | Power Required | Notes |
|---------|---------|----------------|-------|
| ... | ... | Yes / No | ... |

---

## Rules

1. **Every resource the player can interact with must be registered here.** If code references a resource type, it must appear in this document.
2. **Tier assignment follows the definitions above.** A resource's tier is determined by its acquisition method, not its value.
3. **Storage type determines zone compatibility.** Resources can only be stored in zones that accept their storage type.
4. **Production chains must be complete.** Every processed resource must trace back to raw resources through documented stations.
5. **New resource categories require a summary entry** in the Resource Categories table and their own section below.
