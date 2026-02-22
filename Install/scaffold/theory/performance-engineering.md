# Performance Engineering

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

Engine-agnostic performance principles for games — how to think about optimization, budgets, and profiling without wasting effort.

---

## Profile First

- Never optimize without profiling. Intuition about where time is spent is wrong more often than it is right. Measure, then act.
- Measure before and after every optimization to verify it actually improved performance. An optimization that does not move the numbers is wasted work — or worse, a regression hiding behind assumptions.
- Optimize the hottest path first. The function called 10,000 times per frame matters more than the function called once at startup. Profilers rank by cumulative time for exactly this reason.
- Premature optimization wastes effort on code that is not the bottleneck. If a system uses 0.3% of the frame, making it twice as fast saves 0.15% — meaningless next to the system using 40%.
- Distinguish between CPU-bound, GPU-bound, and memory-bound problems before choosing a fix. The correct optimization depends entirely on which resource is saturated.

## Frame Budgets

- At 60fps you have 16.67ms per frame. At 30fps you have 33.33ms. Pick a target frame rate, calculate the budget, and treat it as a hard constraint — not a suggestion.
- Allocate the budget across systems: rendering, physics, scripts, AI, audio, garbage collection. Each system gets a slice. If one system exceeds its slice, others must shrink to compensate.
- Track budget usage over time, not just in a single frame. Spikes matter as much as averages — a single 40ms frame in a stream of 12ms frames produces a visible hitch the player will feel.
- Reserve headroom. If your target is 16.67ms, design for 14ms. The remaining margin absorbs unexpected spikes, platform variance, and future feature growth.
- Test budget on the weakest target hardware, not your development machine. A frame that fits in budget on a high-end PC may blow through it on a minimum-spec laptop or console.

## Memory Management

- Allocation and deallocation during gameplay cause stutters. Garbage collection pauses are the most common source of frame-time spikes in managed-language engines.
- Pre-allocate during loading screens and reuse during gameplay. If you know you will need 200 projectiles, allocate all 200 before the level starts.
- Object pools prevent allocation churn for frequently spawned and destroyed objects — projectiles, particles, enemies, hit effects. Pooling turns allocation into a reset-and-reuse operation.
- Know your platform's memory limits. Mobile devices have a fraction of desktop memory, and exceeding the limit means the OS kills your process without warning. Budget memory per scene and enforce it.
- Monitor memory usage continuously throughout development, not just before ship. Memory leaks compound over time — a leak that adds 1MB per minute is invisible in a five-minute test and catastrophic in a two-hour play session.

## Batching & Draw Calls

- Every draw call has fixed overhead on both CPU and GPU. Reducing draw call count is often the single largest rendering optimization available.
- Batch objects that share the same material and mesh into fewer draw calls. Most engines provide static or dynamic batching for this purpose — understand which your engine supports and what the constraints are.
- Texture atlasing combines multiple textures into one, reducing material switches. Fewer unique materials means more objects can share a draw call.
- GPU instancing renders many copies of the same mesh in a single draw call. Trees, grass, rocks, debris, crowd NPCs — anything repeated is a candidate for instancing.
- UI draw calls add up fast and are easy to overlook. Every unique texture, font, or clipping region can break a batch. Consolidate UI atlases, minimize layering, and batch UI elements aggressively.

## Level of Detail (LOD)

- Do not render what the player cannot see. Frustum culling removes objects outside the camera's view. This is usually automatic, but placing objects correctly and setting bounds accurately ensures it works.
- Occlusion culling removes objects hidden behind other objects. A building behind a wall does not need to be drawn. Occlusion systems need setup — bake or configure them, do not assume they work by default.
- LOD swaps high-detail meshes for simpler versions at distance. A character with 10,000 triangles at close range can drop to 2,000 at medium range and 500 at far range without visible quality loss.
- Impostors replace 3D objects with flat billboard sprites at extreme distances. For distant trees, buildings, or props, a well-rendered impostor is indistinguishable from the real mesh at a fraction of the cost.
- Every LOD transition should be invisible to the player. Popping — a visible snap from one LOD to another — breaks immersion. Use distance hysteresis or crossfade blending to smooth transitions.

## Lazy & Deferred Work

- Do not compute what you do not need yet. If a value is expensive to calculate and only used conditionally, defer the calculation until the condition is met.
- Spread expensive work across multiple frames instead of doing everything in one. If 300 enemies need pathfinding updates, update 50 per frame over six frames rather than all 300 in one frame and causing a spike.
- Background loading prevents load-screen stalls. Stream assets for the next area while the player is still in the current one. By the time the player arrives, the content is ready.
- Streaming — loading nearby content and unloading distant content — keeps memory bounded in large worlds. Define streaming volumes or distance thresholds and enforce them.
- Cache expensive results. If a calculation produces the same output for the same input, store the result and reuse it instead of recalculating. Pathfinding results, visibility checks, and physics queries are common candidates.

## Data-Oriented Thinking

- How data is laid out in memory affects performance more than algorithmic cleverness for most game workloads. Cache misses — when the CPU must fetch data from slow main memory instead of fast cache — dominate the cost of data access.
- Arrays of structs versus structs of arrays matters. If you iterate over 10,000 entities but only read their position, storing positions in a contiguous array is faster than storing full entity objects with position buried among fields you do not need this frame.
- Sequential access patterns are faster than random access patterns. Iterating through an array in order is cache-friendly. Jumping between scattered heap allocations is cache-hostile.
- Separate hot data (accessed every frame) from cold data (accessed rarely). Position, velocity, and health are hot. Lore text and inventory history are cold. Storing them together pollutes the cache with data you are not using.
- Shrink your data. Smaller data structures mean more entries fit in a cache line. An 8-byte position fits twice as many entries per cache line as a 16-byte position. Use the smallest data type that meets your precision requirements.

## Common Performance Traps

- String operations in hot loops are expensive. String comparison, concatenation, and formatting allocate memory and burn cycles. Use integer IDs, enums, or hashed keys for lookups that happen every frame.
- Physics raycasts every frame add up fast. Cache results when the query parameters have not changed, use physics layers to limit what gets tested, and cap ray length to the minimum needed.
- Instantiating and destroying objects every frame causes garbage collection pressure. Pool frequently created objects — projectiles, effects, pickups — instead of allocating and freeing them repeatedly.
- Logging in release builds wastes cycles. Debug prints, console output, and string formatting for log messages should be compiled out or gated behind a debug flag in shipping builds.
- Searching unsorted lists when a dictionary or hashmap would work is a common silent cost. A linear search through 1,000 items every frame is 1,000 comparisons. A hashmap lookup is effectively one.
- Updating things that have not changed wastes work. If an object has not moved, do not recalculate its transform. If a UI element has not changed, do not redraw it. Dirty flags and change detection prevent unnecessary recomputation.
