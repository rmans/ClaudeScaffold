# Balance Parameters

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

Master registry of all tunable numbers in the game. Every threshold, rate, timing value, and capacity that affects game balance is defined here. This is the single source of truth for "what are the numbers?" — designers tune here, engineers read from here.

## Parameters

### SYS-### [SystemName]

<!-- One subsection per system that owns tunable parameters. Organize by system ID in ascending order. -->

| Parameter | Value | Unit | Type | Range | System | Dependency Notes | Notes |
|-----------|-------|------|------|-------|--------|------------------|-------|
| ... | TBD / value | unit | threshold / rate / duration / capacity / multiplier | min–max | SYS-### | Other parameters this depends on or affects | What this parameter controls |

<!-- Type values:
  - threshold: A boundary value that triggers behavior when crossed (e.g., hunger_critical_threshold).
  - rate: A per-unit-time value (e.g., hunger_decay_per_hour, healing_rate).
  - duration: A time span (e.g., construction_time, sleep_duration).
  - capacity: A maximum quantity (e.g., max_colonists, storage_capacity).
  - multiplier: A scaling factor applied to a base value (e.g., speed_modifier, damage_multiplier).

Dependency Notes: List any parameters that interact with this one. Examples:
  - "Scales hunger_decay_rate" — this multiplier modifies another parameter.
  - "Must be < max_health" — this threshold must stay below a capacity.
  - "Inverse of construction_speed" — derived relationship.
  Leave blank if the parameter is independent.
-->

<!-- Column definitions:
  - Parameter: snake_case name matching code constant
  - Value: Current tuned value, or TBD if not yet set
  - Unit: What the number measures (hp, per hour, multiplier, seconds, normalized 0–1, degrees, tiles, etc.)
  - Range: Valid min–max bounds for balancing. Code should clamp to this range.
  - System: Owning system ID (redundant with subsection heading but useful for search/filtering)
  - Notes: What this parameter does, what it affects, edge cases
-->

---

<!-- Repeat for each system. Also include non-system parameter groups if needed (e.g., MapManager, global constants). -->

### [Non-System Group Name]

<!-- For parameters owned by non-system components (MapManager, global settings, etc.) -->

| Parameter | Value | Unit | Type | Range | Owner | Dependency Notes | Notes |
|-----------|-------|------|------|-------|-------|------------------|-------|
| ... | TBD / value | unit | threshold / rate / duration / capacity / multiplier | min–max | ComponentName | ... | ... |

---

## TBD / Unresolved Tuning

<!-- Track parameters that are known to be needed but whose values, ranges, or even existence are uncertain. Resolve each entry during balancing or playtesting. -->

| Parameter | System | Issue | Resolution |
|-----------|--------|-------|------------|
| ... | SYS-### | Why this parameter is unresolved (no playtest data, conflicting design goals, etc.) | Pending playtest / ADR-### / TBD |

---

## Rules

1. **Every tunable number must be registered here.** If code uses a magic number that affects gameplay balance, it must appear in this document.
2. **Values may be TBD.** During design, parameters start as TBD with a valid Range. Values are set during balancing and playtesting.
3. **Range bounds are hard limits.** Code should clamp parameters to their stated range. Values outside the range are balance bugs.
4. **System column enables lookup.** Even though parameters are grouped by system subsection, the System column allows flat searching across all parameters.
5. **Units must be concrete.** "per hour" means per in-game hour. "multiplier" means a scaling factor applied to a base value. Never use vague units.
6. **New parameters are added when systems are implemented.** When a task introduces a tunable number, register it here before implementation.
