# [Engine] — Asset & Import Pipeline

> **Layer:** Implementation
> **Authority:** Rank 9
> **Conforms to:** [design/design-doc.md](../design/design-doc.md)
> **Status:** Draft
> **Created:** YYYY-MM-DD
> **Last Updated:** YYYY-MM-DD
> **Changelog:**
> - YYYY-MM-DD: Initial creation from template.

## Purpose

<!-- Define how art, audio, data, and content assets flow from source files into the runtime game. For a simulation-heavy game, this includes not just textures and sounds but also CSV data tables, content definitions, and authored configuration that feeds into the simulation layer. -->

*TODO: Define asset and import pipeline purpose.*

---

## Source Asset Conventions

<!-- Where do source assets live? What naming conventions do they follow? What directory structure? What metadata or tagging is expected? -->

*TODO: Define source asset location, naming, and organization conventions.*

---

## Import Presets

<!-- What import presets exist for each asset type? Textures, spritesheets, audio, fonts, data files. What compression, filtering, mipmapping, or format settings are standard? -->

*TODO: Define import presets per asset type.*

---

## Texture & Spritesheet Pipeline

<!-- How are textures and spritesheets authored, imported, and referenced at runtime? Atlas packing? Individual sprites? Naming conventions for animation frames? -->

*TODO: Define texture and spritesheet import workflow.*

---

## Audio Asset Pipeline

<!-- How are audio files authored, imported, and referenced? Format conventions (WAV, OGG, MP3)? Bus assignment? Streaming vs preloaded? -->

*TODO: Define audio asset import workflow.*

---

## Data Table Pipeline

<!-- How are CSV, JSON, or other authored data tables loaded into the simulation? What validation runs on import? How do data table changes propagate to runtime entities? This is distinct from the content pipeline doc — this covers the raw file → runtime data path. -->

*TODO: Define data table import and validation workflow.*

---

## Content Definition Import

<!-- How do content definitions (items, structures, recipes, traits) flow from authored files into the ContentRegistry or equivalent runtime system? What format are they authored in? What validation catches errors before runtime? -->

*TODO: Define content definition import workflow.*

---

## Runtime vs Authored Asset Boundary

<!-- Which assets are used directly at runtime (e.g., .tres, .tscn, imported textures) and which are intermediate/source-only (e.g., PSD files, raw WAV, spreadsheet masters)? What should never be in the export? -->

*TODO: Define the boundary between source assets and runtime assets.*

---

## LOD / Variant Policy

<!-- If applicable: how are level-of-detail variants managed? Resolution variants for different display targets? Compressed vs uncompressed variants? -->

*TODO: Define LOD and variant policy if applicable.*

---

## Export & Platform Considerations

<!-- What asset processing happens at export time? Platform-specific texture compression? Audio format conversion? Data file baking? -->

*TODO: Define export-time asset processing.*

---

## Project Overrides

<!-- If your project deviates from any convention above, document it here. -->

| Convention | Default | Override | Rationale |
|------------|---------|----------|-----------|

---

## Rules

1. **Source assets and runtime assets are distinct.** Source files (PSDs, master spreadsheets, uncompressed audio) never ship. Only imported/processed assets reach the player.
2. **Naming conventions are mandatory.** Every asset type has a naming convention. Assets that don't follow it are import errors.
3. **Data tables are validated on import.** CSV/JSON data that feeds the simulation must pass structural validation before it reaches runtime. Invalid data is caught at import, not at play.
4. **Content definitions follow the content pipeline doc.** This doc governs the file → import path. The content pipeline engine doc governs the import → runtime path. They must agree on format and validation rules.
5. **Import presets are documented, not assumed.** If a texture uses a non-default import preset, that preset must be documented here or in a project override.
