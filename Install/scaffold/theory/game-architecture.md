# Game Architecture

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

---

## Purpose

Engine-agnostic software architecture principles for games — patterns, decoupling strategies, and structural decisions that apply across engines and languages.

This document carries no authority. It informs design decisions but never dictates them. If a principle here influences an architectural choice, that choice should be captured in an ADR, which is what carries the actual authority.

---

## 1. Composition Over Inheritance

- Deep inheritance hierarchies become brittle the moment requirements change. Adding a feature to a base class propagates side effects to every descendant, and overriding behavior in a leaf class often breaks assumptions made three levels up. Prefer shallow hierarchies with composed behaviors.
- An entity that "has a" health component and "has a" movement component is more flexible than one that "is a" HealthMovingEntity. When a designer asks for a moving object without health, composition handles it by omission. Inheritance requires a new branch in the tree.
- Reserve inheritance for true is-a relationships where the subtype genuinely substitutes for the parent in every context. A Fireball is-a Projectile. A Player is not an Enemy with different stats — they share behaviors, which should be composed, not inherited.
- When you find yourself creating classes like FlyingEnemyWithShield, the hierarchy has failed. Each adjective in the name is a component that should be attached independently. Combinatorial explosion of subclasses is the clearest signal that composition is overdue.
- Composition enables runtime flexibility. Components can be added, removed, or swapped during play — an entity can gain flight or lose its shield without changing its class. Inheritance locks structure at compile time.

## 2. Entity-Component Systems

- ECS separates data (components) from behavior (systems). Components are pure data structs with no logic — position, health, velocity. Systems iterate over entities that have specific component combinations and apply behavior. This separation makes each piece independently testable and replaceable.
- Cache-friendly data layout is a practical benefit. When components of the same type are stored contiguously in memory, systems that iterate over them get predictable access patterns. This matters at scale — thousands of entities updating per frame benefit measurably from data locality.
- Not every game needs a full ECS framework. The principle — separate data from behavior, iterate over data sets — is valuable even in an object-oriented codebase. A lightweight component container with manual iteration captures most of the architectural benefit without the framework overhead.
- Systems should be stateless where possible. A movement system reads position and velocity, writes new position. It does not remember what it did last frame. Stateless systems are easier to reason about, easier to parallelize, and easier to test in isolation.
- Define clear component ownership. If two systems write to the same component, you have a race condition waiting to happen. Each component should have one system responsible for writing it, even if multiple systems read it.

## 3. State Machines

- Every game object with distinct modes of behavior benefits from an explicit state machine. A character that can be idle, running, jumping, attacking, and stunned has five states with defined transitions between them. Making these states explicit prevents impossible combinations like attacking-while-stunned from occurring silently.
- State machines are documentation as much as architecture. A state diagram is immediately reviewable — designers, artists, and programmers can look at it and verify that the behavior is correct before any code runs. Hidden implicit states (boolean flags, nested conditionals) resist this kind of review.
- Hierarchical state machines manage complexity for objects with many states. A character's "grounded" superstate contains idle, running, and crouching. The "airborne" superstate contains jumping and falling. Shared transitions (taking damage interrupts any grounded state) are defined once on the superstate, not duplicated across every leaf.
- Transitions should be explicit and enumerable. If you cannot list every valid transition out of a given state, the state machine is underspecified. Unexpected transitions are a primary source of animation glitches, physics bugs, and logic errors.
- Keep state logic in the state, not in the thing being stated. The character does not decide what to do based on checking its current state — the current state decides what to do and the character executes it. This inversion keeps state-specific logic contained and prevents cross-state contamination.

## 4. Event Systems & Decoupling

- Direct references between systems create coupling that resists change. When the combat system calls the audio system directly, changing the audio API means editing combat code. An event — "damage dealt" — lets any interested system respond without the sender knowing who is listening.
- Fire-and-forget events (signals, observer pattern) are the simplest form. The sender emits an event and does not wait for or expect a response. This works for notifications: health changed, enemy died, item collected. The sender's logic does not depend on who handles the event or whether anyone handles it at all.
- Request-response patterns are more complex but necessary when the sender needs a return value. "Can this entity take damage?" requires an answer before proceeding. Keep request-response events to a minimum — they reintroduce temporal coupling and are harder to debug than fire-and-forget.
- Too many events create invisible dependencies that are harder to trace than direct calls. If understanding a single interaction requires following a chain of six events across four systems, the decoupling has become its own form of complexity. Balance decoupling with traceability.
- Establish a central event registry or signal list. Every event in the game should be documented with its name, payload, sender, and expected receivers. Undocumented events become invisible wiring that no one dares to change.
- Avoid event chains where event A triggers handler B which emits event C which triggers handler D. These cascades are difficult to debug, can cause infinite loops, and make execution order unpredictable. If a chain is necessary, make it explicit and document the full sequence.

## 5. Data-Driven Design

- Separate data from code. Game content — levels, items, abilities, dialogue, enemy stats — should live in data files (JSON, CSV, resource files), not hardcoded in scripts. When a designer wants to change a goblin's health from 50 to 60, they should edit a data file, not a script.
- Data-driven design enables iteration without recompilation. Hot-reloading data files during play lets designers tune values in real time. This shortens the feedback loop from minutes to seconds, which compounds into dramatically more iteration cycles over a project's life.
- Define clear schemas for every data type. An item definition must have a name, a cost, and a category. A level definition must have dimensions, spawn points, and exit conditions. Unstructured data (freeform dictionaries with no validation) becomes unmaintainable the moment more than one person touches it.
- Validate data at load time, not at use time. If an item references a nonexistent ability, the game should fail loudly on startup, not crash silently when a player equips it twenty minutes into a session. Early validation converts mysterious runtime bugs into clear load-time errors.
- Data-driven does not mean data-only. Behavior that involves branching logic, complex conditionals, or algorithmic computation belongs in code. Data defines the parameters; code defines the process. Trying to encode complex behavior in data files produces a worse programming language.

## 6. Scene & Object Lifecycle

- Every object needs a clear creation, initialization, update, and destruction path. If any of these stages is ambiguous — "this node might or might not be initialized when you access it" — bugs will accumulate at the boundaries between stages.
- Initialization order matters and must be documented. If system A depends on system B being ready, that dependency should be explicit, not an accident of load order that happens to work. When initialization order is implicit, adding a new system can break unrelated systems by shifting the sequence.
- Lazy initialization defers cost but creates unpredictable first-frame spikes. The first time a lazily-initialized system is accessed, it pays its full setup cost, which may cause a visible hitch during gameplay. Prefer eager initialization at known points (scene load, level start) where a loading screen can absorb the cost.
- Object pooling prevents allocation churn for frequently created and destroyed objects. Projectiles, particles, hit effects, and short-lived enemies should be drawn from a pool and returned to it rather than allocated and freed every time. Allocation spikes cause frame drops; pooling converts spikes into flat overhead.
- Destruction must clean up all references. A destroyed entity that is still referenced by a system, an event listener, or a UI element creates dangling references, null access errors, or memory leaks. Ensure every system that holds a reference to an object is notified of or can handle its destruction.

## 7. Dependency Management

- Systems should depend on abstractions, not concrete implementations. The combat system depends on "something that provides health data," not on a specific HealthComponent class. When the health implementation changes, the combat system is unaffected as long as the interface is stable.
- Circular dependencies between systems indicate an architectural problem. If system A depends on system B and system B depends on system A, the two are functionally one system split across two files. Either merge them, extract the shared dependency into a third system, or introduce an event to break the cycle.
- Dependency injection — passing dependencies in rather than reaching out for them — makes testing and refactoring easier. A system that receives its dependencies as constructor arguments can be tested with mock data. A system that grabs its dependencies from global state can only be tested in a fully initialized environment.
- Map dependencies explicitly. Draw the dependency graph for your project. If you cannot draw it, the structure is too tangled. If the graph has many arrows pointing in both directions, the architecture has coupling problems. Dependencies should flow in one direction — from high-level systems down to low-level services.
- Singletons and global state are implicit dependencies that hide coupling. Every system that accesses a global is coupled to it, but that coupling is invisible in the code's structure. Limit globals to true infrastructure (logging, configuration) and pass everything else explicitly.

## 8. Separation of Concerns

- Rendering code should not know about game rules. Input handling should not know about UI layout. Physics should not know about scoring. Each system should have a single, clear responsibility. When you describe what a system does and use the word "and," consider splitting it.
- The test for good separation: can you replace one system's implementation without modifying any other system? If swapping the renderer requires editing the combat system, those two systems are coupled through a concern that should be isolated behind an interface.
- When a system does too many things, split it. When two systems always change together — every time you edit one, you must also edit the other — they might actually be one system that was artificially divided. Separation should follow natural fault lines in the domain, not arbitrary file-size limits.
- Presentation and logic are the most common concerns to entangle. A health system that directly modifies a health bar sprite is mixing game logic with rendering. The health system should expose health data; a separate display system should read that data and update the visual representation.
- Cross-cutting concerns (logging, analytics, save/load) touch many systems but should not be embedded in them. Implement cross-cutting concerns as services that systems call into, or as event listeners that observe system behavior without modifying it.

## 9. Update Loops & Timing

- Separate fixed-timestep logic (physics, game rules, state transitions) from variable-timestep logic (rendering, animation, interpolation). Fixed update runs at a constant rate regardless of frame rate. Variable update runs once per frame. Mixing the two produces behavior that changes with frame rate.
- Frame-rate-independent movement requires delta time — the elapsed time since the last update. Multiplying velocity by delta time produces consistent movement speed whether the game runs at 30fps or 144fps. Omitting delta time ties game speed to frame rate.
- Fixed-timestep updates prevent physics instability at varying frame rates. A physics simulation that runs 60 times per second produces identical results on every machine. A physics simulation that runs once per frame produces different results at different frame rates — objects tunnel through walls at low fps and float gently at high fps.
- Never tie game logic to frame rate. Timers, cooldowns, spawn rates, and animation speeds should all use elapsed time, not frame counts. A 60-frame cooldown is 1 second at 60fps, 0.5 seconds at 120fps, and 2 seconds at 30fps. A 1.0-second cooldown is 1.0 seconds everywhere.
- Interpolation smooths the gap between fixed update and render. If physics runs at 50Hz but rendering runs at 144Hz, the display will stutter unless you interpolate between the last two physics states based on how far the current frame falls between them. This is a rendering concern, not a physics concern.
- Be deliberate about update order within a frame. Input, then game logic, then physics, then rendering is a common and sensible order. If rendering happens before game logic processes input, the display is always one frame behind, which adds perceived input latency.
