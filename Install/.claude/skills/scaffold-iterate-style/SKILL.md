---
name: scaffold-iterate-style
description: Adversarial per-topic review of Step 5 docs using an external LLM. Reviews style-guide, color-system, ui-kit, interaction-model, feedback-system, and audio-direction across 5 topics (visual coherence, interaction & feedback model, cross-doc consistency, player experience readiness, accessibility coherence). Consumes design signals from fix-style. Supports --target for single-doc focus and --topics for scoped review.
argument-hint: [--target doc.md] [--topics "1,2,5"] [--focus "concern"] [--iterations N] [--signals "..."]
allowed-tools: Read, Edit, Write, Grep, Glob, Bash
---

# Adversarial Style Review

Run an adversarial per-topic review of Step 5 visual/UX docs using an external LLM reviewer: **$ARGUMENTS**

This skill reviews the 6 Step 5 docs across 5 sequential topics, each with its own back-and-forth conversation. It uses the same Python infrastructure as iterate-design/iterate-references but with visual/UX-specific topics.

This is the **design reviewer** for Step 5 — not the formatter. It runs after `fix-style` has normalized the docs and detected design signals. It evaluates whether the visual/UX model is *sound* — whether the visual identity is coherent, the interaction and feedback models work together, the docs are consistent with each other and with upstream canon, and the player experience is well-served.

The real question this review answers: **do these 6 docs, taken together, give a developer everything they need to build the game's visual presentation, player interaction, system feedback, and audio — without guessing, contradicting each other, or leaving critical UX decisions implicit?**

## Topics

| # | Topic | What It Evaluates | Primary Docs |
|---|-------|-------------------|-------------|
| 1 | Visual Coherence | Does the visual identity hold together? | style-guide, color-system |
| 2 | Component & Layout Model | Is the UI component model complete and well-bounded? | ui-kit |
| 3 | Interaction & Feedback Model | Do input and response work as a coherent pair? | interaction-model, feedback-system |
| 4 | Audio Integration | Does audio direction align with visual tone and feedback coordination? | audio-direction, feedback-system |
| 5 | Cross-Doc Consistency & Player Experience Readiness | Do all 6 docs tell one consistent story? Could a developer build from them? | All 6 docs |

### Topic 1 — Visual Coherence

Does the visual identity hold together as a whole?

**style-guide.md focus:**
- **Pillar coherence** — do the aesthetic pillars reinforce each other, or do they pull in conflicting directions? "Readable at a glance" and "dense, detailed art" are in tension. Flag contradictions the doc doesn't acknowledge.
- **Tone register completeness** — do registers cover the full emotional range the design doc describes? If the game has crisis states, calm states, and transition states, are all represented? Are transitions between registers described (what triggers the shift, how fast)?
- **Rendering approach fitness** — does the rendering approach actually serve the game described in the design doc? Top-down pixel art for a game that needs "cinematic character moments" is a mismatch. Flag approach-to-vision tension.
- **Entity coverage realism** — are visual descriptions specific enough to distinguish entity types at the game's actual camera distance? A description that sounds beautiful in prose but is unreadable at 1080p zoom-out is a design failure.
- **Animation budget realism** — do the animation principles imply a production scope that matches the project? "Unique idle animations per colonist personality" in a solo-dev project is a scope trap. Flag ambition-vs-capacity tension.
- **Reference specificity** — are visual references concrete ("Rimworld's icon language for status indicators") or vague ("clean and modern")? Vague references provide no implementation guidance.
- **Iconography testability** — could an artist produce icons from these rules alone? Are size constraints, color restrictions, and state variant rules concrete enough?

**color-system.md focus:**
- **Palette-to-tone alignment** — does the palette actually evoke the mood described in style-guide tone registers? A "warm, organic" tone register with a cold blue palette is incoherent.
- **Token coverage** — are there enough semantic tokens for the UI and gameplay states the game needs? Are there gameplay states without color representation?
- **Signal color reservation** — are signal colors (health, danger, alert) truly reserved, or are they also used decoratively elsewhere? Decorative reuse of signal colors destroys information.
- **Accessibility rigor** — are contrast ratios concrete numbers, not aspirational language? "We aim for good contrast" is worthless. "WCAG AA 4.5:1 minimum for body text" is testable.
- **Theme variant coherence** — if themes exist, do they maintain token semantics? A "desert biome" theme where the danger color shifts from red to orange breaks learned associations.
- **Color count discipline** — is the total palette size manageable? Too many colors create visual noise. Too few create monotony. Is there a stated principle?

**Exemplar findings:**
- "Aesthetic pillars say 'readable at a glance' but rendering approach describes dense isometric detail. At default zoom, entities will be 20px tall — readability needs explicit rules for that scale."
- "Tone registers describe Baseline, Tension, and Crisis, but color-system has no palette shifts for any of them. The game will look the same during a crisis as during calm."
- "Signal palette uses red for danger AND for the faction identity color of the enemy faction. Players will confuse faction identity with danger state."
- "Accessibility section says 'WCAG AA' but 3 UI token combinations fail the 4.5:1 ratio."
- "Style-guide references 'painterly, soft edges' but color-system defines hard-edged tokens with maximum saturation. These aesthetics contradict."

Core question: *could an artist produce all visual assets using only style-guide.md and color-system.md, and have them look like they belong in the same game?*

### Topic 2 — Component & Layout Model

Is the UI component model complete and well-bounded?

**ui-kit.md focus:**
- **Component sufficiency** — does the component set cover what system designs need to display? For every system that surfaces player-visible information, is there a corresponding component? Flag systems with player-facing data but no UI component.
- **State table completeness** — does every interactive component have all necessary states (default, hover, pressed, focused, disabled, error, selected)? Are there interaction patterns in interaction-model.md that imply states ui-kit doesn't define?
- **Typography hierarchy fitness** — does the type scale serve the game's information density needs? A game that shows 20 stats on one panel needs different typography rules than one with minimal HUD.
- **Spacing discipline** — is the spacing scale actually used consistently in component definitions? Are there components that imply different spacing conventions?
- **Sound feedback boundary** — are per-component sounds here clearly distinct from feedback-system coordination? Is there overlap where the same event has both a component sound and a feedback-system entry?
- **Scope guard verification** — does the doc stay at component level, or has it drifted into screen maps, scene hierarchies, modal graphs, or full HUD structure? These belong in engine docs.
- **Resource representation coverage** — do resources from resource-definitions.md have icon or display components? Are there resource types with no visual representation?
- **Component composition patterns** — are composition rules (how components combine into panels, how panels combine into layouts) described at the right abstraction level? Too abstract = unusable. Too concrete = engine leakage.

**Exemplar findings:**
- "System designs describe 8 systems that surface player-visible data, but ui-kit only defines components for 5. Morale, skill, and trait systems have no UI representation."
- "Component state table has hover and selected but no focused state. Keyboard/gamepad navigation will have no visual feedback."
- "Typography defines 4 heading sizes but the game's densest panel (colony overview) would need at least 6 hierarchy levels to be readable."
- "Sound feedback section defines 'alert appear' sound, but feedback-system.md also defines audio response for alerts. Which one fires? Both? In what order?"
- "Doc contains a 'Screen Regions' section with HUD layout positions. That's a screen map — belongs in engine UI doc, not ui-kit."

Core question: *could a UI developer build every panel in the game using only ui-kit.md, and have them be visually consistent and interaction-ready?*

### Topic 3 — Interaction & Feedback Model

Do input and response work as a coherent pair?

This topic reviews interaction-model.md and feedback-system.md together, because they form a single input→response loop. The boundary is: interaction-model defines what the player DOES, feedback-system defines what the system DOES BACK.

**interaction-model.md focus:**
- **Player verb coverage** — does every player verb from the design doc have a corresponding interaction pattern? Are there verbs with no defined input mechanism?
- **Selection model clarity** — could two developers implement the same selection behavior from this doc? Single-select, multi-select, drag-select, deselection, persistence across mode changes — all unambiguous?
- **Command model completeness** — are commands specific enough for implementation? "The player can issue orders" is insufficient. "Click entity → right-click target → command issued if valid, error feedback if not" is implementable.
- **Modal structure coherence** — are game modes (build, zone, inspect, etc.) clearly defined? Is it clear what persists and what resets when switching modes? Are mode transitions documented?
- **Input feedback mapping** — does every interactive element have a defined hover, press, and select response? Are these consistent with ui-kit component states and color-system tokens?
- **Boundary enforcement** — does the doc strictly define player input and avoid defining system responses? If it describes what happens after a command is issued (beyond immediate input feedback), that content belongs in feedback-system.

**feedback-system.md focus:**
- **Feedback type coverage** — does every player action in interaction-model have a corresponding feedback type? Are there interaction patterns with no defined system response?
- **Priority hierarchy defensibility** — is the priority ordering justified? Could a player scenario produce two simultaneous feedback events where the priority ordering is wrong? (e.g., critical alert suppressed by a building-placed confirmation)
- **Event-response table completeness** — are the major game events covered? For each event, are visual, audio, and UI responses all specified? Are there events with only one channel defined?
- **Timing realism** — are timing rules consistent with the game's simulation model? "Instant" feedback for actions that are actually tick-confirmed will feel wrong.
- **Cross-modal coordination specificity** — are coordination rules specific enough that two developers would implement the same behavior? "Visual and audio fire together" is vague. "Visual flash starts on event frame, audio plays 50ms after, UI toast appears 200ms after" is implementable.
- **Redundancy principle enforcement** — is gameplay-critical information conveyed through at least two channels? Are there critical events with only one feedback channel?
- **Failure feedback quality** — when the player tries something invalid, is the feedback specific enough to explain WHY it failed? "Can't do that" vs "Not enough iron (need 5, have 3)" is the difference between frustrating and helpful.

**Pair coherence checks:**
- **Input→response completeness** — every interaction pattern ends with a defined response. No dead ends where the player acts and nothing happens.
- **Response→input consistency** — feedback doesn't imply interaction capabilities that interaction-model doesn't define. If feedback-system mentions "drag to reorder," interaction-model must define drag behavior.
- **Boundary discipline** — interaction-model handles input, feedback-system handles response. No overlap. No gaps.

**Exemplar findings:**
- "Interaction-model defines 12 player commands but feedback-system only has responses for 8. Four commands have no defined system response."
- "Priority hierarchy puts 'action confirmation' above 'state change notification.' But a colonist dying (state change) during building placement (action confirmation) should not be suppressed by the building sound."
- "Cross-modal coordination says 'visual + audio fire together' for critical alerts, but doesn't specify timing. Two developers will implement different delays."
- "Interaction-model says drag-select is available, but there's no error feedback defined for when the drag selects zero entities."
- "Feedback-system describes 'sustained state feedback' for power outage, but interaction-model has no corresponding interaction pattern for inspecting or resolving power state. The player sees the feedback but has no action to take."

Core question: *if you played this game, would every input produce clear, timely, appropriate feedback — and would you always know what you can do and what happened?*

### Topic 4 — Audio Integration

Does audio direction align with visual tone and feedback coordination?

**audio-direction.md focus:**
- **Philosophy-to-tone alignment** — does the audio philosophy match style-guide visual tone registers? If the visual tone is "warm and organic," does the audio philosophy say "synthetic and clinical"? Flag mismatches.
- **Category completeness** — do sound categories cover all feedback types from feedback-system? Are there feedback events that need audio but have no corresponding audio category?
- **Music direction fitness** — does the music direction serve the game's pacing? If the game has long quiet stretches, does the music direction account for that? If the game has rapid escalation, does music respond fast enough?
- **Silence as design** — is silence used intentionally? Does the doc define when the game should be quiet and what quiet communicates? Or is silence just "no sounds playing"?
- **Feedback hierarchy consistency** — does the audio priority ordering match feedback-system's priority hierarchy? If feedback-system says critical alerts are highest priority, audio-direction should not put music above alerts.
- **Redundancy compliance** — does audio-direction acknowledge the no-audio-only-information rule? Are there audio events that carry gameplay information not available through any other channel?
- **Asset style coherence** — do the audio aesthetic rules (realistic/stylized, frequency range, loudness) match the visual aesthetic from style-guide?
- **Boundary enforcement** — does audio-direction define what the game sounds like (philosophy, categories, aesthetic rules)? Or does it drift into defining when sounds fire and how they coordinate with visual/UI (which belongs in feedback-system)?

**feedback-system cross-check:**
- **Event-response audio column** — does every event in the event-response table with an audio response reference a real audio-direction category?
- **Priority alignment** — feedback-system priority hierarchy and audio-direction feedback hierarchy must agree. Divergence means two different stacking/suppression behaviors.
- **Coordination boundary** — audio-direction owns character (what sounds sound like), feedback-system owns timing (when sounds fire). Neither should duplicate the other's domain.

**Exemplar findings:**
- "Style-guide visual tone is 'clinical, precise, cold' but audio philosophy says 'warm ambient organic soundscape.' These produce conflicting player impressions."
- "Feedback-system defines audio responses for 15 event types but audio-direction only defines 4 sound categories. 11 events need category placement."
- "Audio-direction says 'silence during baseline state' but feedback-system has sustained ambient feedback during baseline. Which is true?"
- "Audio priority puts music above UI sounds. But feedback-system puts critical alerts above everything. If both are right, a critical alert during music is ambiguous."
- "Audio-direction defines 'when construction completes, play a chime.' That's timing coordination — belongs in feedback-system, not here."

Core question: *would the game sound like it looks? Would audio reinforce the visual experience or fight it?*

### Topic 5 — Cross-Doc Consistency & Player Experience Readiness

Do all 6 docs tell one consistent story? Could a developer build from them?

This topic is the integration test. It evaluates whether the complete Step 5 doc set is coherent and sufficient for downstream implementation.

**Cross-doc consistency checks:**
- **Style-guide ↔ Color-system** — do palette choices evoke the mood described in tone registers? Do tone register shifts have corresponding palette shifts?
- **Color-system ↔ UI-kit** — do all component state tokens exist in color-system? Are there raw hex values in ui-kit? Do component states use semantically correct tokens (error = danger color, not accent)?
- **Style-guide ↔ UI-kit** — do animation timings match? Does icon style match iconography rules? Does typography match the visual tone?
- **Interaction-model ↔ UI-kit** — does interaction-model assume components that ui-kit defines? Does ui-kit define interaction behavior it shouldn't?
- **Interaction-model ↔ Feedback-system** — every input has a response. Every response corresponds to a real input. No gaps, no overlap.
- **Feedback-system ↔ Audio-direction** — priority hierarchies agree. Sound categories cover feedback types. Timing coordination belongs in feedback-system only.
- **Feedback-system ↔ Color-system** — feedback visual treatments use correct color tokens for their severity.
- **Audio-direction ↔ Style-guide** — audio aesthetic matches visual aesthetic. Tone registers align across visual and audio.
- **All ↔ Design doc** — aesthetic pillars, tone, player verbs, failure philosophy, and player information model are consistently reflected across all 6 docs.
- **All ↔ State-transitions** — entity states are mapped to colors (color-system), visual states (ui-kit component states), feedback triggers (feedback-system), and audio responses (audio-direction).
- **Abstraction-level consistency** — are all 6 docs at the same abstraction level? Or has one drifted into implementation detail while others remain high-level?
- **Canonical drift detection** — is any downstream doc (feedback-system, audio-direction) more detailed or more current-looking than its upstream source (style-guide, interaction-model)? Practical source-of-truth drift.

**Player experience readiness:**
- **Spec derivation readiness** — could behavior specs be written against these docs? Can you specify "when the player places a building" in terms of interaction-model input, feedback-system response, ui-kit components, color-system tokens, and audio-direction sound?
- **Implementation path clarity** — for each major player interaction, is the full path clear? Input mechanism (interaction-model) → component representation (ui-kit) → system response (feedback-system) → visual treatment (style-guide + color-system) → audio response (audio-direction)?
- **Gap detection** — what's the biggest thing missing? Not "this could be improved" but "a developer would get stuck here and not know what to do."
- **Ambiguity detection** — where could two developers legitimately interpret these docs differently and build incompatible presentations?
- **Multi-developer divergence test** — if two UI developers independently built the same panel from these docs, where would they diverge most?

**Accessibility coherence (cross-doc):**
- **Color-only information** — are there gameplay states communicated only through color? (color-system + ui-kit)
- **Audio-only information** — is there gameplay-critical information conveyed only through audio? (audio-direction + feedback-system)
- **Hover-only interaction** — are there interaction cues available only through hover, inaccessible to keyboard/gamepad? (interaction-model + ui-kit)
- **Redundant channel coverage** — does every critical gameplay event have at least two feedback channels? (feedback-system + ui-kit + audio-direction)

**Exemplar findings:**
- "Interaction-model assumes a 'context menu' component that ui-kit doesn't define. A developer would have to invent the context menu design."
- "Feedback-system priority says critical alerts are highest, but audio-direction says music is never interrupted. Both can't be true during a crisis."
- "Style-guide describes tone register shifts but color-system has no corresponding palette shifts and audio-direction has no corresponding mood changes. The game will shift visual tone without color or audio following."
- "Power failure state is communicated only through a color shift (amber). Color-blind players have no other channel."
- "Two developers would diverge on tooltip behavior — interaction-model says 'hover to inspect' but doesn't specify delay, content structure, or dismissal. UI-kit defines tooltip components but not when they appear."

**After all topics complete**, the reviewer must answer final questions and provide a rating:

1. **What is the single most dangerous cross-doc inconsistency?** — the mismatch most likely to produce a confusing player experience if not caught.

2. **What could a developer get wrong despite reading all 6 docs?** — the implicit assumption or undocumented convention most likely to produce inconsistent presentation.

3. **Which doc is weakest?** — the doc that contributes least to implementation clarity or has the most unresolved content.

4. **Blocker classification** — for each issue found, classify its downstream impact:
   - **Blocks engine UI doc** — can't write engine UI implementation without this resolved
   - **Blocks specs** — can't derive behavior specs involving UI/interaction without this resolved
   - **Blocks art/audio production** — can't generate consistent assets without this resolved
   - **Does not block, increases risk** — implementation can proceed but this will cause UX inconsistency later

5. **Visual/UX Model Strength Rating (1–5):**
   - 1 = fundamentally broken (major cross-doc contradictions, critical docs mostly TBD)
   - 2 = major gaps (interaction model incomplete, feedback system missing, visual identity unclear)
   - 3 = workable but risky (some cross-doc drift, several TBD areas, ambiguity in key UX decisions)
   - 4 = solid visual/UX model (docs mostly consistent, minor gaps bounded, implementation path clear)
   - 5 = strong visual/UX model (all docs consistent, no contradictions, developer could implement from docs alone)

## Reviewer Bias Pack

Include these detection patterns in the reviewer's system prompt. They represent the most common failure modes in visual/UX doc sets.

1. **Aesthetic coherence without operational precision** — the docs describe a beautiful vision but lack the concrete rules needed to implement it. "Warm, organic feel" with no color tokens, timing values, or spacing rules. Test: could you build a UI panel from this description alone?

2. **Boundary erosion** — interaction-model starts defining system responses. Feedback-system starts defining input behavior. Audio-direction starts defining coordination timing. UI-kit starts defining screen layout. Each doc drifts into its neighbor's domain, creating ambiguity about which doc is canonical for what.

3. **Priority hierarchy fantasy** — feedback priority ordering looks clean on paper but fails under realistic gameplay scenarios. Two simultaneous events, three overlapping audio cues, a critical alert during a modal dialog. The priority system was designed for one-at-a-time events in a game that produces many simultaneous ones.

4. **Component-level completeness, interaction-level gaps** — every component is beautifully defined (ui-kit is thorough), but the interaction patterns that connect components are underspecified (interaction-model is thin). Or vice versa. The docs look complete individually but the seam between them is the real gap.

5. **Accessibility as afterthought** — accessibility sections exist in color-system and audio-direction, but no cross-doc check ensures the principle is actually enforced. Color-only health indicators. Audio-only alert events. Hover-only inspection. Each doc passes individually; the system fails as a whole.

6. **Tone register orphaning** — style-guide defines tone registers but color-system, audio-direction, and feedback-system don't reference them. The tone registers exist in isolation — they describe mood shifts that no other doc implements.

7. **Feedback coordination gap** — feedback-system describes coordinated responses, but the individual docs it coordinates (ui-kit for visual, audio-direction for audio, color-system for color) were written independently without referencing the coordination rules. The coordination doc exists; the coordinated docs don't know about it.

8. **Scope creep into engine territory** — UI-kit defines screen maps. Interaction-model defines input routing. Feedback-system defines signal dispatch timing. Audio-direction defines audio middleware configuration. Each has drifted from "what" into "how" — which belongs in engine docs.

## Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--target` | No | all | Target a single doc by filename (e.g., `--target ui-kit.md`). When set, topics are scoped to the targeted doc's concerns — but cross-doc topics (5) still read all docs. |
| `--topics` | No | all | Comma-separated topic numbers to review (e.g., `"1,3,5"`). |
| `--focus` | No | — | Narrow the review within each topic to a specific concern. |
| `--iterations` | No | 10 | Maximum outer loop iterations. Stops early on convergence. |
| `--max-exchanges` | No | 5 | Maximum back-and-forth exchanges per topic. |
| `--signals` | No | — | Design signals from fix-style to focus the review on known issues. Format: comma-separated signal descriptions. |

### --target to --topics mapping

When `--target` is set without explicit `--topics`, the skill automatically selects the relevant topics:

| Target | Auto-selected Topics |
|--------|---------------------|
| `style-guide.md` | 1, 5 |
| `color-system.md` | 1, 5 |
| `ui-kit.md` | 2, 5 |
| `interaction-model.md` | 3, 5 |
| `feedback-system.md` | 3, 4, 5 |
| `audio-direction.md` | 4, 5 |

Topic 5 (Cross-Doc Consistency & Player Experience Readiness) is always included because it evaluates doc interactions.

Explicit `--topics` overrides this mapping.

## Preflight

Before running external review:

1. **Check docs exist.** Verify at least style-guide.md, ui-kit.md, interaction-model.md, and feedback-system.md exist and are not at template defaults. If fewer than 4 Step 5 docs exist, stop: "Style docs not ready. Run `/scaffold-bulk-seed-style` first."
2. **Check fix-style has run.** Verify the docs are structurally clean — no missing required sections, no invalid token references. If structural issues remain, stop: "Run `/scaffold-fix-style` first to normalize structure."
3. **Check design doc exists.** The reviewer needs Design Invariants, Aesthetic Pillars, and Player Control Model as context.

## Context Files

Read and pass as `--context-files` to the Python script:

| Context File | Why |
|-------------|-----|
| All 6 Step 5 docs | Primary targets |
| `design/design-doc.md` | Aesthetic Pillars, tone, player verbs, failure philosophy, accessibility — high-authority context |
| `design/glossary.md` | Canonical terminology |
| `scaffold/doc-authority.md` | Document authority ranking, same-rank conflict resolution |
| `design/systems/_index.md` + system files with player-visible behavior | What the UI must display and what events the game produces |
| `design/state-transitions.md` | Entity states that need visual, color, and feedback mapping |
| `reference/entity-components.md` | Entity types for component and icon coverage |
| `reference/resource-definitions.md` | Resources for UI representation coverage |
| `decisions/known-issues/_index.md` | Known gaps and constraints |
| ADRs with status `Accepted` (canonical: internal Status field) | Decision compliance |
| Design signals from fix-style (if `--signals` provided) | Focus areas for the reviewer |

Only include context files that exist — skip missing ones silently.

## Execution

Follow the same topic loop, inner loop (exchanges), consensus, and apply-changes pattern as `/scaffold-iterate-references`.

**Stop conditions** (any one stops iteration):
- **Clean** — a complete topic pass produces no new issues.
- **Converged** — two consecutive passes produce the same issue set with no new findings.
- **Human-only** — only issues requiring user decisions remain; further iteration won't resolve them.
- **Limit** — `--iterations` maximum reached.

### Review Consistency Lock

Across iterations and topics, resolved issues are locked. Once an issue is **accepted and fixed** or **explicitly rejected with reasoning**, it must not be re-litigated.

**Issue identity rule:** Issues are tracked by root cause, not wording. Different framings of the same underlying concern count as the same issue. Examples:
- "color palette doesn't match tone" and "palette-to-mood mismatch" → same issue if about the same palette/tone register pair.
- "component state missing" and "no focused state defined" → same issue if about the same component.

**Lock enforcement:**
- The reviewer must NOT reintroduce a resolved issue in a different form.
- The reviewer must NOT raise stricter variants of a resolved issue unless: (a) new evidence exists that wasn't available when the issue was resolved, OR (b) the fix itself introduced a new problem.
- If a previously resolved issue reappears: classify it as a **review inconsistency**, not a new issue.

**Cross-topic lock:** If Topic 1 resolves an issue, later topics may not re-raise it under a different name.

**Tracking:** Maintain a running resolved-issues list in the review log during execution. Before engaging with any new reviewer claim, check it against the resolved list by root cause.

**Edit scope:**
- When `--target` is set, only edit the targeted doc. Flag cross-doc issues for fix-style.
- When `--target` is not set, edit any of the 6 Step 5 docs.
- Never edit Step 1–4 docs (design-doc, system designs, architecture, reference docs, engine docs) or planning docs.

### Issue Adjudication

Every issue raised by the reviewer must be classified into exactly one outcome:

| Outcome | Action |
|---------|--------|
| **Accept → edit Step 5 doc** | Apply change immediately. The issue is valid and the fix is within Step 5 doc scope. |
| **Reject reviewer claim** | Record reasoning in review log. The reviewer is wrong or the issue is out of scope. |
| **Escalate to user** | Requires design judgment, unclear authority, or the reviewer and Claude remain split after max-exchanges. |
| **Flag for revise-design** | Design doc (Rank 1) is likely incomplete or ambiguous on visual/UX direction. Step 5 doc may be correct; design needs tightening. |
| **Defer (valid TBD)** | The section is correctly blocked by an unresolved design decision. Not a gap — an honest wait. |
| **Flag ambiguous design intent** | Design doc permits multiple valid visual/UX interpretations and the Step 5 doc chose one. Not incorrect — genuinely ambiguous upstream. Flag for user decision. |

**Adjudication rules:**
- Prefer fixing Step 5 docs over escalating — most issues are presentation-level clarity.
- Never "half-accept" — choose exactly one outcome per issue.
- If the issue depends on a missing design decision → flag for revise-design, not Step 5 fix.
- If the issue is style/component/interaction-specific clarity → accept and fix.
- If the reviewer and Claude disagree after max-exchanges → escalate to user.
- If multiple valid interpretations of a design-doc decision exist and the Step 5 doc chose a reasonable one → flag ambiguous design intent.

### Scope Collapse Guard

Before accepting any change to a Step 5 doc, enforce these tests:

**1. Upward Leakage Test:**
Does this change introduce or modify decisions that belong in system designs or the design doc?
- Step 5 docs may: define visual identity, component behavior, interaction patterns, feedback coordination, audio direction.
- Step 5 docs must NOT: change what systems do, alter gameplay mechanics, or redefine system responsibilities. Those belong in Steps 1-2.

**2. Downward Leakage Test:**
Does this change introduce engine-specific implementation detail that belongs in engine docs?
- Step 5 docs must NOT: specify scene tree structure, node types, signal wiring, render pipelines, or engine-specific APIs. Those belong in Step 4 engine docs.
- Test: could this rule be implemented in any engine? If engine-specific → wrong layer.

**3. Lateral Leakage Test:**
Does this change belong in a different Step 5 doc?
- Interaction-model must not define system responses (→ feedback-system).
- Feedback-system must not define input behavior (→ interaction-model).
- Audio-direction must not define coordination timing (→ feedback-system).
- UI-kit must not define screen maps or modal hierarchies (→ engine docs).

### Review Log

Create review log in `scaffold/decisions/review/`:
- Name: `ITERATE-style-[target-or-all]-<YYYY-MM-DD>.md`
- Use the template at `scaffold/templates/review-template.md`.
- Update `scaffold/decisions/review/_index.md` with a new row.

## Report

```
## Style Review Complete [target / all]

### Most Dangerous Cross-Doc Inconsistency
[The mismatch most likely to produce a confusing player experience.]

### What Could a Developer Get Wrong
[The implicit assumption most likely to produce inconsistent presentation.]

### Weakest Doc
[The doc that contributes least to implementation clarity.]

### Topic Summary

| Topic | Issues | Accepted | Rejected |
|-------|--------|----------|----------|
| 1. Visual Coherence | N | N | N |
| 2. Component & Layout Model | N | N | N |
| 3. Interaction & Feedback Model | N | N | N |
| 4. Audio Integration | N | N | N |
| 5. Cross-Doc & Player Experience | N | N | N |

### Per-Doc Issues
| Document | Issues Found | Accepted Changes | Key Finding |
|----------|-------------|-----------------|-------------|
| style-guide.md | N | N | ... |
| color-system.md | N | N | ... |
| ui-kit.md | N | N | ... |
| interaction-model.md | N | N | ... |
| feedback-system.md | N | N | ... |
| audio-direction.md | N | N | ... |

**Visual/UX Model Strength Rating:** N/5 — [one-line reason]
**Iterations:** N completed / M max [early stop: yes/no]
**Changes applied:** N
**Review log:** scaffold/decisions/review/ITERATE-style-[target]-YYYY-MM-DD.md
```

## Rules

- **Design doc and system designs are the primary authority.** Step 5 docs interpret and present; they do not override. When the reviewer suggests changes that conflict with Rank 1–5 docs, reject.
- **Step 5 docs describe PRESENTATION, not IMPLEMENTATION.** If the reviewer suggests engine constructs, node types, or rendering pipeline details, reject and propose presentation-level alternatives.
- **Edit only Step 5 docs.** Never edit design-doc, system designs, architecture, reference docs, engine docs, planning docs, or ADRs during review.
- **Authority flows downstream within Step 5.** style-guide → color-system → ui-kit. Interaction-model and feedback-system are peers. Audio-direction derives priority from feedback-system. On mismatch, upstream is canonical. Downstream issues may reveal upstream incompleteness — report both directions.
- **Never apply changes that violate document authority.** style-guide wins over color-system. color-system wins over ui-kit token references. feedback-system wins over audio-direction priority ordering.
- **Never blindly accept.** Every issue gets evaluated against project context and design doc intent.
- **Pushback is expected and healthy.** The reviewer is adversarial — disagreement is normal.
- **Reappearing material issues escalate to the user.** Escalate when the same material issue persists for 2 outer iterations, or when the reviewer and Claude remain split after max-exchanges on a topic.
- **When --target is set, respect edit scope.** Cross-doc issues found during targeted review are flagged for fix-style, not fixed directly.
- **Sleep between API calls.** Add `sleep 10` between topic transitions.
- **Clean up temporary files** after use.
- **If the Python script fails, report the error and stop.**
- **Cross-doc consistency (Topic 5) is the highest-value topic.** If time or iteration budget is limited, prioritize Topic 5 over per-doc topics.
- **Ambiguous upstream design is not a Step 5 defect.** When the design doc genuinely permits multiple valid visual/UX interpretations and a Step 5 doc chose a reasonable one, do not treat it as incorrect. Flag for user decision.
- **Practicality check before finalizing changes.** Before accepting any change, ask: (a) would this make the doc harder to use during implementation? (b) does this improve clarity for developers and artists, or does it just enforce internal consistency for the review system's benefit? Reject changes that increase rigidity without improving usability.
- **Scope collapse guard.** Before accepting any change, apply three tests: (1) Upward leakage — does this change gameplay or system behavior? If yes, reject or flag upstream. (2) Downward leakage — does this introduce engine-specific detail? If yes, reject. (3) Lateral leakage — does this belong in a different Step 5 doc? If yes, flag for relocation via fix-style.
- **Resolved issues are locked across iterations.** Once accepted+fixed or rejected with reasoning, an issue is closed. The reviewer may not reintroduce it under different wording. Only new evidence or a regression can reopen. Issues are identified by root cause, not phrasing.
