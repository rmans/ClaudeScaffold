# Assets — Index

> **Purpose:** Hub for all production art and audio assets. Organized by what the asset is for, not what tool made it.

## Structure

| Directory | What goes here | Examples |
|-----------|---------------|---------|
| [entities/](entities/_index.md) | Everything for a specific game entity — sprites, models, icons, SFX, voice, all together | `entities/colonist/`, `entities/iron-ore/`, `entities/workshop/` |
| [ui/](ui/_index.md) | Shared UI assets not tied to one entity — panel graphics, cursors, shared icons, UI SFX | Component assets, navigation sounds, shared status icons |
| [environment/](environment/_index.md) | Biome and location assets — tilesets, environmental art, ambience loops | `environment/forest/`, `environment/cave/`, biome tilesets |
| [music/](music/_index.md) | Scene and mood-level music tracks — not tied to one entity or location | Calm theme, tension theme, menu music |
| [shared/](shared/_index.md) | Reusable base assets used across multiple entities — base meshes, shared skeletons, generic SFX | Base humanoid mesh, generic impact SFX, shared material textures |
| [concept/](concept/_index.md) | Exploration and reference art — not production assets | Mood boards, concept sketches, visual exploration |
| [promo/](promo/_index.md) | Marketing and promotional art — store pages, press kit, social media | Key art, screenshots, banner images |

## Principle

**Everything about a thing lives with the thing.** A colonist's sprites, model, icon, portrait, SFX, and barks all live in `entities/colonist/`. When implementing the colonist, you look in one place.

**Exceptions** that stay grouped by purpose:
- **UI** — shared components not owned by any entity
- **Environment** — biome-wide, not entity-specific
- **Music** — scene/mood-level, not entity-level
- **Shared** — base assets reused across entities (shared skeleton, generic sounds)
- **Concept** — exploratory, not production
- **Promo** — marketing, not in-game

## Creating Entity Directories

When a new entity needs assets, create a directory under `entities/`:

```
entities/colonist/
├── sprite-idle.png
├── sprite-downed.png
├── portrait.png
├── icon-status.png
├── model.glb
├── sfx-footstep-01.ogg
├── sfx-footstep-02.ogg
├── bark-hungry-01.ogg
└── _index.md
```

Each entity directory gets its own `_index.md` listing all assets for that entity.

## File Naming

- **Kebab-case** for all filenames
- **Type prefix** for clarity: `sprite-`, `icon-`, `model-`, `sfx-`, `music-`, `ambience-`, `voice-`, `texture-`
- **State/variant suffix** where applicable: `-idle`, `-damaged`, `-01`, `-loop`
- **Timestamp suffix** for generated assets: `-YYYYMMDD-HHMMSS`

Examples:
- `sprite-colonist-idle.png`
- `sfx-build-complete.ogg`
- `icon-resource-iron.png`
- `model-workshop.glb`
- `ambience-forest-loop.ogg`
