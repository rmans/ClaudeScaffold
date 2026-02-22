# Multiplayer Design

> **Authority:** Rank 11 — Advisory only
> **Layer:** Theory

Principles for multiplayer game design — networking models, social dynamics, and the unique challenges of shared game spaces.

---

## Networking Models

- Client-server architecture is the authoritative standard for competitive games. The server owns game state, validates all inputs, and distributes results. This prevents most classes of cheating but requires dedicated infrastructure and adds latency to every action.
- Peer-to-peer removes the server bottleneck and is simpler to deploy, but every peer must trust every other peer. Any single compromised client can manipulate shared state. NAT traversal adds friction to connection setup and fails outright for some network configurations.
- Rollback netcode predicts the outcome of remote inputs and corrects when the real input arrives. This makes local actions feel instant at the cost of occasional visual corrections — teleporting characters, rewound animations. It works best for fast-paced games where responsiveness matters more than visual consistency.
- Lockstep networking waits for every player's input before advancing the simulation. This guarantees perfect synchronization but introduces latency equal to the slowest connection in the session. It suits turn-based or strategy games where frame-perfect sync matters more than input speed.
- Hybrid approaches exist. Many games use client-server for authoritative state but apply local prediction and rollback on the client side. Choose the model that matches your game's tolerance for latency versus desync, and be honest about the infrastructure you can maintain.

## Latency & Responsiveness

- Players perceive latency above approximately 100 milliseconds. Below that threshold, most actions feel instant. Above it, the game feels sluggish regardless of frame rate or visual quality.
- Design mechanics that tolerate latency rather than fighting it. Projectiles with travel time naturally absorb network delay. Area-of-effect abilities are forgiving of slight position disagreements. Hitscan weapons and frame-precise interactions amplify every millisecond of lag.
- Input prediction makes the local player's actions feel instant by applying them immediately on the client, then reconciling with the server's authoritative response. The player presses jump and jumps now — not 80 milliseconds from now.
- Interpolation smooths remote player movement by rendering their position slightly in the past, blending between known positions. This hides network jitter at the cost of a small additional display delay for remote entities.
- Never show the player raw network state. Unsmoothed remote movement jitters and teleports. Unsmoothed latency spikes freeze the game. Always interpolate, extrapolate, or buffer — present a smooth approximation rather than an honest but ugly truth.

## State Synchronization

- Decide what is authoritative and where before writing any networking code. In competitive games, the server should own all gameplay-critical state. In cooperative games, client authority over the local player's actions can reduce perceived latency without meaningful exploit risk.
- Synchronize the minimum data necessary. Send deltas rather than full state snapshots. Filter by relevancy — a player does not need updates about entities on the other side of the map. Tune tick rate to the game's needs — a turn-based game does not need 60 updates per second.
- Delta compression reduces bandwidth by transmitting only what changed since the last acknowledged state. Combined with relevancy filtering, this keeps bandwidth manageable even with large player counts or complex game state.
- Establish clear ownership rules for every piece of state. When two systems disagree, the resolution must be deterministic and predefined. Ambiguous ownership produces desyncs that are nearly impossible to debug.
- Define graceful desync recovery. When client and server state diverge, the client should smoothly converge back to the server's version — not snap, not crash, not corrupt the save. Rubber-banding is ugly but survivable. Data corruption is not.

## Social Dynamics

- Multiplayer is a social experience before it is a technical one. The networking can be flawless and the game will still fail if players cannot communicate, cooperate, or coexist.
- Provide communication tools appropriate to the game. Voice chat and text serve different needs. Contextual pings and emotes allow communication without language barriers and without voice. Quick-chat systems with preset messages give players a voice without opening the door to abuse.
- Toxic behavior requires systems-level solutions, not just community management. Mute, block, and report must be accessible in two clicks or fewer. Automated detection of slurs and harassment in text chat is table stakes. Moderation at scale requires tooling, not just people.
- Positive social mechanics shape community culture more effectively than punishment. Shared objectives that require genuine cooperation, gifting systems, mentoring incentives, and commendation systems reward prosocial behavior rather than only punishing antisocial behavior.
- Matchmaking is a social system as much as a competitive one. Putting a new player against a veteran is a social failure even if the skill gap is technically small. First impressions of the community determine retention more than first impressions of the gameplay.

## Matchmaking & Lobbies

- Match players by skill using a rating system such as MMR, ELO, or Glicko. Time played and account level are poor proxies for skill — a returning veteran and a new player with the same playtime are not equivalent.
- Session setup must be fast. Every second spent in a lobby, loading screen, or queue is a second the player is not playing. If average queue time exceeds sixty seconds, players start leaving. Optimize matchmaking speed even at the cost of match quality in casual modes.
- Backfill — adding players to matches already in progress — keeps games populated but must be handled carefully. Never backfill a player into a match that is about to end. Provide backfilled players with loss protection or reduced penalties so they are not punished for joining a losing game.
- Let friends play together even when their skill levels differ. Social play is a primary motivator for multiplayer engagement. Use party-based matchmaking that accounts for the highest-skilled member, or provide unranked modes where balance is relaxed in favor of social grouping.
- Display estimated wait times honestly. An inaccurate "estimated time: 30 seconds" that becomes three minutes erodes trust faster than an honest "estimated time: 2 minutes" that delivers on its promise.

## Anti-Cheat & Fairness

- Cheating destroys multiplayer games faster than any design flaw or technical bug. A single cheater in a lobby ruins the experience for every other player in that session, and the reputational damage spreads beyond the players who were directly affected.
- Server-authoritative logic is the first and most effective line of defense. If the server validates all game state and the client is only an input device and a renderer, most common exploits — speed hacks, teleportation, item duplication — become impossible without compromising the server itself.
- Never trust the client. Validate all inputs server-side. If a client claims to have fired a weapon, verify that the weapon was equipped, loaded, and off cooldown. If a client reports a position, verify that the movement is physically possible given the time elapsed.
- Rate-limit actions to prevent automation. Cap fire rate, movement speed, interaction frequency, and chat messages at server-enforced maximums. This prevents bots and macros from gaining an unfair advantage even if they bypass client-side checks.
- Prefer detection over instant punishment for subtle cheats. Flag suspicious behavior for review rather than auto-banning. False positives — banning a legitimate player — are far more damaging to community trust than a cheater who operates for an extra day before a manual review confirms the ban.

## Co-op Design

- Every player in a co-op session should feel useful. If one player can carry the entire team while the others watch, the co-op experience has failed. Design encounters that require contributions from multiple players or that scale so each player has meaningful work to do.
- Give players distinct roles, specialties, or tools. Asymmetric capabilities create natural cooperation — one player heals, another tanks, a third deals damage. Even subtle asymmetry, like different starting equipment, encourages players to coordinate rather than operate in parallel.
- Shared objectives should require actual cooperation, not just proximity. A boss that one player could solo given enough time is not a co-op encounter — it is a solo encounter with spectators. Design interactions that mechanically require multiple players: simultaneous switches, complementary abilities, divided attention.
- Scale difficulty with player count. A challenge tuned for four players becomes trivial with four and impossible solo. Dynamic scaling — more enemies, higher health pools, additional mechanics — keeps the experience appropriate regardless of party size.
- Drop-in and drop-out must be seamless. Players leave mid-session due to crashes, life interruptions, or boredom. The remaining players should never be stranded in an unwinnable state. AI companions, difficulty reduction, or mechanic simplification should activate automatically when a player departs.

## Competitive Design

- Competitive players need unambiguous win conditions. If the path to victory is unclear or feels arbitrary, competitive engagement collapses. Every match should end with a clear winner determined by transparent rules.
- Separate ranked and unranked modes. Ranked play serves players who want to test their skill against calibrated opponents. Unranked play serves players who want to experiment, practice, or play casually without risking their rating. Forcing both audiences into the same queue satisfies neither.
- Seasons and periodic rating resets keep the competitive ecosystem fresh. A static ladder stagnates as top players plateau and new players feel they can never catch up. Seasonal resets compress the rating range and give everyone a renewed sense of progression.
- Spectator mode and replay systems build competitive community. Players learn by watching skilled players. Tournament organizers need broadcast tools. Replay analysis drives improvement and content creation. These features feel optional but are critical infrastructure for a competitive scene.
- Balance changes must be transparent. Publish patch notes that explain not just what changed but why. Players who understand the reasoning behind a nerf accept it more readily than players who feel their favorite option was arbitrarily weakened. Avoid stealth nerfs — they erode trust.

## Handling Disconnects

- Players will disconnect. Design for it from the start, not as an afterthought. Network failures, client crashes, power outages, and intentional quits all produce the same result: a missing player. The game must handle all of these gracefully.
- In co-op, replace the disconnected player with an AI companion or pause the game until they reconnect. Never leave remaining players in an unwinnable state because a teammate vanished. If AI takeover is not feasible, reduce encounter difficulty to compensate for the missing player.
- In competitive modes, use forfeit timers that give the disconnected player a reasonable window to return before conceding the match. Two to three minutes is generally sufficient to recover from a crash and reconnect without making the remaining players wait indefinitely.
- Reconnection must be fast and restore state completely. The reconnecting player should return to the game exactly where they left off — same position, same inventory, same score. If full state restoration is not possible, get as close as possible and clearly communicate what was lost.
- Distinguish between intentional quitting and accidental disconnects when applying penalties. Repeated disconnects from the same player in a short window suggest intentional behavior. A single disconnect followed by a reconnect attempt suggests a technical issue. Penalize patterns, not isolated incidents.
