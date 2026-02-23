# Theory — Index

> **Layer:** Reference only — never canonical.
> **Authority:** Rank 11 (lowest). Theory informs decisions but never dictates them.

## Documents

<!-- Add reference materials as needed. Format:

| File | Topic |
|------|-------|
| example-theory.md | Description |

-->

| File | Topic |
|------|-------|
| [game-design-principles.md](game-design-principles.md) | Core game design principles — agency, feedback, pacing, economy, etc. |
| [common-design-pitfalls.md](common-design-pitfalls.md) | Recurring game design anti-patterns and how to avoid them |
| [playtesting-guidelines.md](playtesting-guidelines.md) | How to structure, run, and interpret effective playtests |
| [ux-heuristics.md](ux-heuristics.md) | General UX principles for games — onboarding, feedback, accessibility, etc. |
| [genre-conventions.md](genre-conventions.md) | Genre-specific player expectations and design pillars |
| [narrative-design.md](narrative-design.md) | Narrative design principles — storytelling through interactive systems |
| [level-design.md](level-design.md) | Level design principles — teaching through space, pacing, navigation, secrets |
| [audio-design.md](audio-design.md) | Audio design principles — feedback, hierarchy, adaptive audio, silence, accessibility |
| [balance-principles.md](balance-principles.md) | Game balance principles — difficulty, economies, feedback loops, tuning |
| [world-design.md](world-design.md) | World building — sense of place, internal logic, biomes, navigation, ecosystems |
| [color-theory.md](color-theory.md) | Color fundamentals — harmony, psychology, contrast, saturation, palettes |
| [visual-design.md](visual-design.md) | Visual composition — hierarchy, readability, silhouette, contrast, style consistency |
| [multiplayer-design.md](multiplayer-design.md) | Multiplayer — networking, social dynamics, matchmaking, co-op, competitive |
| [game-architecture.md](game-architecture.md) | Software architecture — ECS, state machines, events, decoupling, data-driven design |
| [performance-engineering.md](performance-engineering.md) | Performance — profiling, frame budgets, memory, batching, LOD, optimization traps |
| [testing-strategies.md](testing-strategies.md) | Testing — unit tests, integration, regression, edge cases, determinism |

## Topic Index

Use this index to find theory relevant to a specific design concern.

| Concern | Theory Doc | Section |
|---------|-----------|---------|
| Player agency & choice | game-design-principles.md | Player Agency |
| Feedback clarity | game-design-principles.md | Feedback Loops |
| Game feel & juice | game-design-principles.md | Game Feel / Juice |
| Pacing & flow | game-design-principles.md | Pacing |
| Depth vs complexity | game-design-principles.md | Depth vs Complexity |
| Risk vs reward | game-design-principles.md | Risk vs Reward |
| Economy design | game-design-principles.md | Economy Design |
| Progression systems | game-design-principles.md | Progression Systems |
| Information presentation | game-design-principles.md | Information Design |
| Common anti-patterns | common-design-pitfalls.md | (all sections) |
| Playtesting structure | playtesting-guidelines.md | (all sections) |
| Onboarding UX | ux-heuristics.md | Onboarding |
| Tutorial design | ux-heuristics.md | Tutorialization |
| UI clarity | ux-heuristics.md | UI Clarity |
| Accessibility | ux-heuristics.md | Accessibility |
| Cognitive load | ux-heuristics.md | Cognitive Load |
| Genre player expectations | genre-conventions.md | (match by genre) |
| Environmental storytelling | narrative-design.md | Environmental Storytelling |
| Dialogue systems | narrative-design.md | Dialogue Design |
| Branching narrative | narrative-design.md | Branching and Consequence |
| Ludonarrative consistency | narrative-design.md | Ludonarrative Consistency |
| Teaching through space | level-design.md | Teaching Through Space |
| Spatial pacing | level-design.md | Spatial Pacing |
| Exploration & secrets | level-design.md | Exploration & Secrets |
| Audio feedback hierarchy | audio-design.md | Audio Hierarchy |
| Adaptive music | audio-design.md | Adaptive Audio |
| Spatial audio | audio-design.md | Spatial Audio |
| UI audio | audio-design.md | UI Audio |
| Balance & difficulty curves | balance-principles.md | Difficulty Curves |
| Economy tuning | balance-principles.md | Economy Tuning |
| Dominant strategies | balance-principles.md | Dominant Strategies |
| Feedback loops (positive/negative) | balance-principles.md | Feedback Loops in Balance |
| Difficulty options | balance-principles.md | Difficulty Options |
| Sense of place | world-design.md | Sense of Place |
| Biome & region design | world-design.md | Biome & Region Design |
| World navigation | world-design.md | Navigation & Wayfinding |
| Color palette harmony | color-theory.md | Color Harmony |
| Color psychology | color-theory.md | Color Psychology |
| Value & contrast | color-theory.md | Value & Contrast |
| Color accessibility | color-theory.md | Color for Gameplay |
| Color palette construction | color-theory.md | Color Palette Construction |
| Visual hierarchy & readability | visual-design.md | Visual Hierarchy |
| Readability | visual-design.md | Readability |
| Silhouette design | visual-design.md | Silhouette Design |
| Visual noise | visual-design.md | Visual Noise & Clarity |
| Multiplayer networking | multiplayer-design.md | Networking Models |
| Latency & responsiveness | multiplayer-design.md | Latency & Responsiveness |
| Co-op design | multiplayer-design.md | Co-op Design |
| Competitive design | multiplayer-design.md | Competitive Design |
| ECS architecture | game-architecture.md | Entity-Component Systems |
| State machines | game-architecture.md | State Machines |
| Event systems & decoupling | game-architecture.md | Event Systems & Decoupling |
| Data-driven design | game-architecture.md | Data-Driven Design |
| Frame budgets & profiling | performance-engineering.md | Profile First, Frame Budgets |
| Memory management | performance-engineering.md | Memory Management |
| Batching & draw calls | performance-engineering.md | Batching & Draw Calls |
| Common performance traps | performance-engineering.md | Common Performance Traps |
| Testing strategies | testing-strategies.md | (all sections) |
| Unit testing game logic | testing-strategies.md | Unit Testing Game Logic |
| Determinism & reproducibility | testing-strategies.md | Determinism and Reproducibility |

## Rules

- Theory documents are reference material only.
- They carry no authority over design, engine, or implementation decisions.
- Cite theory docs in ADRs when they influence a decision, but the ADR is what carries authority.
- No other document is required to conform to theory.
