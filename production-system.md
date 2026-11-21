# Production System: Vertical Explainer Shorts

**What this is.** These are the working rules I follow every time you give me a new script, narration track or footage for this project. They turn the measured reference analysis (`video-style-guide.md`, especially the corrected values in §15) into a repeatable pipeline.

**Where the values come from.** Every number below comes from the measured analysis. Where I go beyond the reference, I label it **[EXTENSION]**. The main one is sound effects, because the reference has none that I could confirm.

**Order of precedence:**
1. Your explicit instructions for a project.
2. This document.
3. `video-style-guide.md`.

---

## 0. Inputs I need, and what I do if something is missing

| Input | Ideal | If it's missing |
|---|---|---|
| **Narration** | A final voice-over audio file (WAV/MP3) | With a script only, I plan at **3.0 words/s** and **0.25 s** sentence pauses, then re-time everything once the audio exists. I never lock timings to an estimate. |
| **Script text** | Final wording | I transcribe the voice-over myself (Whisper, word timestamps) and use the *audio* as the source of truth. |
| **Art family** | One of: **Collage** (grayscale or duotone photo cutouts on flat colour, like V1/V3), **Flat illustration** (paper-textured vector, like V4), **Cartoon** (outlined caricature, like V2/V5) | I pick one from the subject matter: real named people → Collage; objects and concepts → Flat; a story with characters and dialogue → Cartoon. I tell you which I picked and why. |
| **Assets** | Photos, cutouts, logos you have the rights to use | I list every asset needed, mark which ones I can draw as vector shapes myself, and flag the ones that need a photo from you. I never use stock images or third-party logos without telling you. |
| **Identity** | Your watermark or monogram, and any brand colours | I use a neutral placeholder monogram in the watermark slot and the default palette in §13. I never reuse the reference publisher's "A" or "Tifo" marks. |
| **Footage** | Optional | Only as a cutout or framed insert treated like a photo (desaturated, §13). Full-frame live footage isn't part of this style, so I'll ask before using it that way. |
| **Format** | 1080×1920, 9:16 | Default: 1080×1920, 30 fps container. |

**Length target: 42–54 s.** If the narration runs longer, I'll tell you where to cut rather than speed up the edit.

---

## Pipeline overview

```
VO audio ─► 1 Transcribe & segment ─► 2 Keyword extraction ─► 3 Visual-need scoring
        ─► 4 Asset & metaphor mapping ─► 5 Scene / beat timeline ─► 6 Motion spec per object
        ─► 7 Sync pass ─► 8 Caption track ─► 9 Pacing audit ─► 10 Transition pass
        ─► 11 SFX & music pass ─► 12 Density / stillness audit ─► 13 Identity audit
        ─► Render ─► Measured QA (same scripts as the reference analysis) ─► Fix ─► Deliver
```

Each stage produces a concrete output that feeds the **Shot Plan** (§14). Before building anything, I show you the Shot Plan and a short summary of it for approval.

---

## 1. Analyse the narration sentence by sentence

**Step 1.1: Transcribe with word timestamps.** I run Whisper on the voice-over to get the start and end time of every word, and correct the text against your script where it's misheard.

**Step 1.2: Split into sentences and phrases.**
- **Sentence** = a run of words ending in `.`, `?` or `!`.
- **Phrase** = a sub-unit ending at a comma, a conjunction ("but", "while", "before", "and then") or a pause of ≥0.2 s.
- **Gap** = any silence between words of ≥0.15 s, recorded with its start and length.

**Step 1.3: Give each sentence a story role.** This sets its pacing and visual weight.

| Role | Typical position | What I look for | Visual weight |
|---|---|---|---|
| **HOOK** | 0–5 s | The opening question or claim ("Did you know…", "Why do…") | Big two-line captions, one striking stage image |
| **PIVOT** | ~3–6 s | "Well," / "But why?" / "And is it…" | The caption size drops; the story starts |
| **SETUP** | 5–15 s | Who, where, when | Maps, pins, people, dates |
| **COMPLICATION** | 15–30 s | The problem, conflict or expectation | Thought bubbles, X marks, comparisons |
| **TWIST / RESOLUTION** | 30–45 s | "To get around…", "insisted…", "however…" | Designed transitions, reveal devices |
| **PAYOFF** | Last 2–5 s | The final fact or punchline | A callback to the stage image, a slam with glow; credits optional |
| **LIST ITEM** | Anywhere | Repeated structure ("The most expensive 27-year-old is…", "1. Preventing…") | Anchor + slide-swap system (§10) |

**Step 1.4: Pick the narrative device.** If the script is a ranking or list (like V3), a numbered set of reasons (like V5) or a single story (like V1/V2), I switch to the matching template:

| Template | Persistent anchor | Unit length | Transition between units |
|---|---|---|---|
| **Story** | One "stage" scene that comes back at the payoff | A scene per subject, 2.5–5 s | Hard cuts plus 2–4 designed transitions |
| **Ranked list** | A tag that stays fixed (for example "age 27") | ~4 s per item | Exit → 0.15–0.2 s empty beat with a colour cut → enter |
| **Numbered reasons** | A section header ("1. PREVENTING / OVER-CELEBRATION") that dims to 30% | 5–9 s per reason | Vertical sheet push or soft wipe + typed heading |

---

## 2. Identify keywords and important concepts

Within each phrase, I tag every content word:

| Tag | What it covers | Examples |
|---|---|---|
| `SUBJ` | The grammatical subject of a sentence, or a new topic noun | "Fulham", "Liverpool's first match" |
| `PERSON` | A named person | "Alvaro Arbeloa", "Jamie Vardy" |
| `GROUP` | Unnamed people | "the Malaga players", "fans", "goalkeepers" |
| `PLACE` | A city, country or venue | "Malaga", "Qatar", "Villa Park" |
| `NUM` | A number, score, money amount, age, date or duration | "2-2", "£92.9m", "18 December", "7-hour" |
| `OBJ` | A concrete object | "trophy", "tape", "cast", "yellow card" |
| `VERB` | A physical action that can be shown | "kicked", "marched", "placed", "broke", "flew" |
| `NEG` | A negation or failure | "not", "didn't count", "none… workable" |
| `CMP` | A comparison or pair | "two different", "33 and 36", "instead of" |
| `MIND` | Expectation, thought or belief | "expecting", "thought", "hoped" |
| `CONSEQ` | A reaction or consequence | "deemed provocation", "furious" |
| `TIME` | Time passing | "25 years on", "the next day", "consecutive" |
| `ABSTR` | An abstract concept | "protection", "evolving", "good luck" |
| `IDIOM` | A figurative phrase | "down the tunnel", "in the middle of" |
| `VERDICT` | The final outcome | "officially awarded", "the answer is…" |

**Stress.** I mark each tagged word's stressed syllable from the audio: the peak of loudness within the word. If the audio isn't available, I use the dictionary stress. **All visual timing refers to the stressed-syllable onset, called `t_kw` from here on.**

---

## 3. Decide which words need a visual

I score each tagged word, then visualise in order from highest score down until the density budget (§12) is full.

| Factor | Points |
|---|---|
| `SUBJ`, or the first mention of a `PERSON`/`PLACE` | +3 |
| `NEG`, `CMP`, `VERDICT` | +3 |
| `NUM` | +2 |
| `VERB` that can act on an object already on screen | +2 |
| `MIND`, `CONSEQ`, `IDIOM` (a chance for a joke or visual pun) | +2 |
| `TIME`, `ABSTR` | +1 |
| Second or later mention of something already on screen | −2 (use a callback instead of a new asset) |
| Falls inside the HOOK and isn't the hook's core object | −1 |

**Thresholds:**
- **≥3:** gets its own visual event. A `SUBJ` with ≥3 normally gets a **new scene**.
- **2:** an additive event if the budget allows; otherwise the caption carries it.
- **≤1:** the caption only.

**Hard rules:**
- Every `PERSON` named for the first time **must** appear.
- Every `NEG` aimed at something visible **must** get an X.
- Every `VERDICT` **must** get the payoff treatment.
- No two of these "musts" may need separate new scenes less than 1.2 s apart. If they collide, the second one becomes an additive event.

---

## 4. Decide which visuals appear (the mapping lexicon)

### 4.1 Tag → visual

| Tag | Default visual | Collage style | Flat style | Cartoon style |
|---|---|---|---|---|
| `PERSON` | That person | Grayscale/duotone full-body cutout | A grayscale head with a paper-cut edge on an illustrated body | A caricature with outlines |
| `GROUP` | Unnamed people | Black silhouettes or duotone crowd | Simple figures, hands | Comic crowd or extras |
| `PLACE` | Flat map + red pin; a dashed line for travel | Same | Same | Same, with outlines |
| `NUM` score/time | Scoreboard card (dark rounded box, light border) | ← | ← | ← |
| `NUM` money/age | A rotated tag (−8.7°) attached to the subject | ← | ← | ← |
| `NUM` date | Calendar icon, or a month grid with X'd days | ← | ← | ← |
| `NUM` a set of values | A bar chart with the axis drawn on; the highlighted bar arrives last | ← | ← | ← |
| `OBJ` | That object as a flat vector prop | ← | ← | Outlined prop |
| `VERB` | Animate the action on the object already on screen (kick, wrap, drop, tumble, jump) | Pose swap for cutouts | Tween the prop | Character pose or animation |
| `NEG` | A red X drawn in two strokes over (or behind) the negated thing | ← | ← | ← |
| `CMP` | Side by side: split panels, a duplicated cutout, or a second figure sliding in | ← | ← | ← |
| `MIND` | A thought bubble (rising puffs + cloud) holding a miniature callback image | ← | ← | ← |
| `CONSEQ` | A speech bubble with an invented one-line reaction (all-caps hand lettering) | ← | ← | ← |
| `TIME` | Clocks with spinning hands, a ticking calendar number, or a clock-tunnel bridge | ← | ← | ← |
| `ABSTR` | One icon that morphs as the concept changes (cross → X → prohibited sign) | ← | ← | ← |
| `IDIOM` | Make it literal ("down the tunnel" → an iris close) | ← | ← | ← |
| `VERDICT` | The key object slams in, biggest on screen, with a white glow | ← | ← | ← |
| Emotion word | A background device: radial speed lines (anger, urgency), sunburst (drama), line-boil halo (excitement) | ← | ← | ← |

### 4.2 Choosing between options
1. **Can an object already on screen show it?** Then animate that object (verb) or attach a label (number). Don't add a new asset.
2. **Is it a callback?** Reuse the earlier asset in exactly the same style (the same scoreboard, the same stage).
3. **Is it concrete?** Use the literal object.
4. **Is it abstract?** Use a symbol from the lexicon. If a joke is available, use invented dialogue or a literal pun, but **at most 3 jokes per video**, placed in the COMPLICATION and TWIST.
5. **Never** use a stock-photo mood image, a generic icon grid or decorative filler.

### 4.3 Asset list output
For every asset: ID, description, source (from you / I draw it / needs sourcing), treatment (grayscale, duotone, flat), and which events use it.

---

## 5. Plan the timeline

### 5.1 Scene boundaries
- **A new scene starts at `t_kw` of each `SUBJ` with a score ≥3** (snapped to the nearest frame).
- If two scene starts would be less than **2.0 s** apart, merge them (the second becomes additive). If a scene would run longer than **5.5 s** (8 s for data cards), add a sub-beat (§9).
- Each new scene gets a **new background colour** from the palette rotation (§13), and never the same colour twice in a row.

### 5.2 Beats within a scene
List the additive events in time order. Each beat has: trigger word, `t_kw`, event type, asset, motion preset (§6), layer, exit rule.

### 5.3 Chapter breaks
At most one per video: a big transition (iris, tear or fly-through) at the boundary between COMPLICATION and TWIST, or at a strong idiom.

### 5.4 Callbacks
- Pick one **stage** scene (the HOOK image) and plan its return in the PAYOFF.
- Pick up to two **props** (a scoreboard, a calendar) that reappear when the narration refers back to them.

---

## 6. The motion spec for every object

### 6.1 Animation step rate (decide once per video)
- **Collage / Flat → on twos.** Each animated pose is held for 2 frames: 15 fps animation in a 30 fps container (12 at 24).
- **Cartoon → on ones.**
- **Exceptions that always run on ones:** decorative boils (speed lines, line halos) and grain in the Collage style.

### 6.2 Motion presets (measured values; durations in seconds)

| Preset | Properties | Duration | Easing | Overshoot | Use |
|---|---|---|---|---|---|
| `POP_UI` | Scale 0.70→1.00 + opacity 0→1 in the first update | 0.25 | Expo-out | **None** | Scoreboards, fixture cards, tags, price labels |
| `POP_HEAD` | Scale 0→1.00 from the anchor point | 0.40–0.50 | Ease-in-out (or ease-out) | None | Photo heads, icons, clover, stop sign |
| `SLAM` | Scale 1.12→1.00 + glow on | 0.33 | Expo-out | None | `VERDICT` objects, trophy |
| `RISE` | translateY from below the frame | 0.20–0.45 | Ease-out | None | Bodies, arms, hands, cutouts |
| `SLIDE_IN` | translateX from the right edge | 0.16–0.45 | Ease-out | None | List items, a second comparison figure, carousels |
| `SLIDE_OUT` | translateX to the left edge | 0.20–0.36 | **Ease-in** (keeps accelerating) + motion blur that grows with speed | — | Outgoing list items, objects leaving |
| `DROP_STACK` | Lines fall in from the top edge, each pushing earlier lines down | 0.45 per line, staggered 0.2 | Expo-out | None | Name/price/club text blocks |
| `FALL` | translateY from above + rotation 10°→0° | 0.50 | Ease-in, hard stop on landing | None | Physical props (cast, tape) |
| `WHIP` | translate from off-frame with motion blur | 0.20–0.40, with ~75% of the distance in the first 30% of the time | Strong ease-out | None | Cartoon characters entering |
| `DRAW` | A stroke grows along its length | 0.17–0.25 per stroke | Accelerating | — | X marks, chart axes, dashed flight paths, tape strips |
| `GROW_BAR` | scaleY from the baseline | ~0.15 per bar, staggered | Ease-out | None | Bar charts; the highlighted bar goes last and tallest |
| `TYPE_ON` | Letters revealed left to right | ~2 frames per letter | Stepped | — | Section headings only |
| `BUBBLE` | Puffs pop one after another (2-frame stagger), then the cloud grows from its tail | 0.30 | S-curve | None | Thought and speech bubbles |
| `PIN_BOB` | Appear at full size, move −6 px up, then settle 4 px down | 0.25 | Ease-out | — | Map pins |
| `POSE_SWAP` | Instant replacement with the next pose or expression | 0 | — | — | Cutout gestures, reactions, kit changes |
| `COUNT` | Instant number swap | 0 | — | — | Calendars, counters (~0.5 s per step, on narration beats) |
| `MORPH` | Rotate or rebuild a shape into its next meaning | 0.25–0.40 per step | Ease-in-out | — | Abstract-concept chains |
| `BURST_EXIT` | 8–10 white dashes shoot out radially; the object disappears in 1 frame | 0.40 | Ease-out, fading | — | Removing a person or head |
| `DEFOCUS_BG` | Gaussian blur on all layers below the overlay | 0.15–0.20 (≈0.5 for a rack focus) | Linear | — | Whenever an overlay card appears; questions |
| `CAM_PAN` | Camera translate | Speed driven by the content (~450 px/s eased for map moves) | Ease-in-out | — | Following geography or a drawn path |
| `CAM_ZOOM_SLOW` | Uniform scale +1.2%/s | Length of the hold | Linear | — | Long data cards (≥4 s) only |

### 6.3 Entrance rules
- Everything enters **from a frame edge or from a dot**. Bodies and hands come from the bottom edge; list items from the right; dropped text blocks from the top. Nothing fades in from nowhere, except credits.
- **Subject first, labels second**: tags and labels start 1–2 animation steps after their subject lands.
- Group stagger: **1–2 animation steps** (0.07–0.13 s) between members.

### 6.4 Exit rules
1. **Instant cut** (the default) on the frame the next focus arrives.
2. `SLIDE_OUT` to the left for list or sequence items.
3. `BURST_EXIT` for people who are "dismissed".
4. **Shrink to a dot** when one shape hands off to the next.
5. **Dim to 30% opacity** for section headers that stay on screen until the section ends.
6. Physical objects get **kicked or thrown off the frame**.

Never fade out an object in the middle of a scene.

### 6.5 Layer order (bottom to top)
```
L0 background colour/gradient → L1 environment (stadium, map, grid) → L2 decorative boil (speed lines, sunburst, floating clocks)
→ L3 hero cutout(s) → L4 attached labels (tags, name block) → L5 marks (X, rings, pins)
→ L6 overlay cards (scoreboard, bubble) + DEFOCUS of L0–L5 → L7 caption → L8 watermark (static, never animated)
```
An X may go **behind** the hero (L2.5) when it negates the person's idea, or **in front** (L5) when it negates an object or event.

### 6.6 Idle life (any hold longer than 1.2 s needs at least one)
In order of preference:
1. Grain re-randomised every 2 frames (Collage)
2. `POSE_SWAP` every 0.5–1.5 s
3. Boil devices (speed lines, halo) on ones
4. Sparkle twinkles: 2–4 visible, 0.3–0.5 s each
5. ±2 px jitter on held marks every 2 frames
6. `CAM_ZOOM_SLOW`, only on data cards

**Don't add camera drift by default.** The reference holds are locked off.

---

## 7. Synchronise with the narration (timing formulas)

All targets snap to the nearest frame. `t_kw` is the stressed-syllable onset; `D` is the animation's length.

| Event type | Start time | Lands / complete |
|---|---|---|
| **Hard scene cut** (`SUBJ`) | `t_kw` ± 1 frame | — |
| **Instant swap** (`POSE_SWAP`, `COUNT`, colour cut) | `t_kw` + 0 to +0.05 s | — |
| **Additive pop/slide** (`D` ≥ 0.25 s) | `t_kw − 0.15·D` (≈0–0.1 s early) | Reaches ~80% on `t_kw`, done by `t_kw + 0.85·D` |
| **Head pop for a name** | 0.10–0.20 s before the first name's onset | Full size during the surname |
| **NEG X**, stroke 1 | `t_kw("not") + 0.2 s` | Stroke 2 starts 0.25 s after stroke 1 finishes, aiming to land on the negated noun |
| **SLAM verdict** | `t_kw − 0.07 s` | Settled ~0.26 s after the word |
| **MIND bubble** (anticipates) | `t_kw(object) − 0.30 s` | ~`t_kw` |
| **CONSEQ speech bubble** | 0.15–0.30 s before the key word of the reaction | On the word |
| **FALL** (physical) | When the preceding verb phrase starts | **Lands 0.25–0.3 s before** the noun it illustrates |
| **WHIP** character | `t_kw` of the action verb ("punished") | +0.2–0.4 s |
| **Camera pan to a place** | Starts on the phrase *before* the place name | The pin lands `t_kw(place) + 0.1 s` |
| **Overlay + DEFOCUS_BG** | Both start on the same frame | — |
| **Iris close** | ~0.18 s after the sentence ends, inside the pause | Black hold 0.3 s; opens on the next `SUBJ` onset |
| **Rack focus** | Right after the question word | Complete as the next sentence starts |

**Ordering rule.** If two events would start within 0.1 s of each other, keep both only when they're part of the same choreography (a subject plus its label, or an overlay plus its defocus). Otherwise move the lower-scoring one to the next stressed word.

**Pause rule.** No scene cuts in silence. The only exceptions are the single chapter-break iris and a payoff hold of ≤0.3 s before the verdict.

---

## 8. The caption track

### 8.1 Two modes
| Mode | When | Style |
|---|---|---|
| **HOOK** | From frame 1 until the PIVOT word | 2 lines, cap height ~6% of frame height (~115 px at 1920), centred at **45–50%** height |
| **BODY** | From the PIVOT word to the end | 1 line, cap height ~3% (~58 px at 1920), centred at **67%** height |

Pick one BODY look per video (never mix them):
- **Boxed (Collage):** yellow `#FFE13A` on a solid black box, padding 0.5 em × 0.35 em, no shadow.
- **Shadowed (Flat/Cartoon):** white, soft dark shadow 3 px down-right at 40–50% opacity, no box.

**HOOK colour:** white with a soft charcoal shadow straight down 4–5 px. **[Alternative]** Yellow with a dark outline plus shadow for a high-energy topic.

**Font:** a heavy condensed sans in all caps with slightly softened corners (Anton or Bebas Neue as stand-ins until you pick a licensed face).

### 8.2 Chunking algorithm
1. Walk the word list. Start a new chunk at every phrase boundary, or once the chunk holds 4 words, whichever comes first.
2. HOOK chunks are 2–3 words.
3. Never leave a single short function word ("A", "THE") alone in a chunk; attach it to the next chunk.
4. **Join the PIVOT word to the next noun phrase** ("WELL FULHAM", "WELL, SORT OF").
5. Aim for 0.4–0.9 s on screen per chunk. If a chunk would be under 0.3 s, merge it with a neighbour. If it would be over 1.2 s (a slow phrase), split it at a word boundary.
6. Write numbers as numerals and scores with an en dash ("2–2", "£92.9M", "5–0"); keep "?" and "!".

### 8.3 Timing and behaviour
- **Appears** on the frame of the first word's onset (+0 to +1 frame, never early). **Disappears** on the frame the next chunk appears. Single-frame hard swap, with **no fade, scale, slide or per-word highlight**.
- Captions **stay on screen through every transition**, including the black iris hold.
- At the very end, the last chunk stays until the final frame.
- **Captions are never emphasised.** Emphasis lives in the graphics (§4). The one structural change is the HOOK → BODY switch.
- **Caption-safe zone:** keep faces and key data out of a band ±5% around the caption line. Overlays may cross the band but must not hide the caption.

---

## 9. Pacing

| Budget | Target |
|---|---|
| Total length | 42–54 s |
| HOOK | 3–5 s, captions changing every 2–3 words |
| Scene length | 2.5–5 s (data cards up to 8 s, with sub-beats) |
| Additive events | One every 1.0–1.5 s on average |
| Caption changes | Every ~0.6 s (comes naturally at ~3 words/s) |
| Designed transitions | 2–4 per video, at most 1 big one, at most 2 dissolves |
| Jokes (bubbles, puns) | 1–3, in the COMPLICATION or TWIST |
| End | Picture and music cut ≤0.7 s after the last word; no outro card |

**Pacing audit** (run on the draft timeline):
1. List every gap of more than 1.5 s between visual events, excluding caption changes. Fill each one with the highest-scoring visual the narration in that gap hasn't used yet. If there isn't one, add an idle-life device (§6.6).
2. List every window where 3 or more events start within 0.5 s. Spread them out or drop the lowest-scoring one.
3. Lists: one item every ~4 s, with 2–3 sub-events per item (tag, name block, pose swap).
4. **Speed up** through SETUP and lists. **Slow down** only once: the beat before the PAYOFF (an iris hold or a 0.3 s hold before the slam).

---

## 10. Transitions

### 10.1 Which transition to use

```
Is this a new SUBJ inside the same chapter?
 ├─ yes → Is it the next item in a list/ranking?
 │        ├─ yes → LIST SWAP (exit 0.2s → 0.15–0.2s beat + colour cut → SLIDE_IN)
 │        └─ no  → Is the narration introducing a PAIR / "two" / contrast?
 │                 ├─ yes → DIAGONAL PANEL WIPE (Cartoon) or SLIDE_IN second figure (Collage)
 │                 └─ no  → HARD CUT on t_kw  (default, ≥60% of all changes)
 └─ no (chapter / section boundary) →
          Numbered section?             → SOFT-EDGE TOP-DOWN WIPE + TYPE_ON heading, or VERTICAL SHEET PUSH (from bottom)
          Time jump ("years later")?    → CLOCK FLY-THROUGH bridge (≈1.9s)
          Solution reveal ("to get around")? → ZIGZAG TEAR (≈0.4s)
          "Alternatively / other side"? → 3D CARD FLIP (≈0.2s)
          Idiom of ending/exit/tunnel?  → IRIS (once per video)
          Concept evolves?              → SHAPE MORPH chain
          Era/role handover, soft?      → CROSS-DISSOLVE 0.5–0.8s (max 2)
          Quick hop between related objects? → WHIP PUSH (ease-in out 0.36s + ease-out in 0.16s, 1-frame overlap)
```

### 10.2 Rules
- **Every scene opens with something already happening**: an element arriving or a pan in progress. It never opens on a fully frozen frame unless the very next event lands within 0.3 s.
- Don't use the same designed transition twice in a row.
- Elements that persist (anchor tags, the caption, the watermark, a divider line) **don't move** across a transition.
- **Background colour changes**: hard cut on the transition frame, or during the empty beat in a list swap.

---

## 11. Sound

### 11.1 What the reference does (measured)
- The voice-over starts on frame 1.
- A music bed sits **~20 dB under the voice** (measured −15 to −23 dB in the gaps).
- **No sound effects I could confirm.**
- Audio stops ≤0.5 s after the last word.

### 11.2 [EXTENSION] SFX policy
You asked for sound effects to reinforce visual events, and I'll add them. To stay true to the reference's restraint, they must be **felt, not noticed**:

| Visual event | SFX character | Level vs. voice | Sync |
|---|---|---|---|
| `POP_UI`, `POP_HEAD`, `PIN_BOB` | A short soft "pop" or "tick", <80 ms | −24 to −28 dB | SFX transient on the first visible frame |
| `SLIDE_IN` / `SLIDE_OUT` / `WHIP` | A light airy swish, 150–300 ms, rising | −26 dB | Peak at the fastest point (the start of an ease-out, the end of an ease-in) |
| `DRAW` (X marks) | A marker scratch per stroke, ~200 ms | −24 dB | Stroke start |
| `SLAM` (verdict) | A low, soft thud plus a short shimmer tail | −20 dB | The first frame of the slam |
| `BURST_EXIT` | A tiny "poof" | −26 dB | The vanish frame |
| `BUBBLE` | A soft bubble blip | −26 dB | Cloud start |
| `COUNT` | A soft click per step | −28 dB | Each number swap |
| Iris close | A low muffled "thump" when fully black | −22 dB | The fully-closed frame |
| Hard cuts | **None** | — | — |

**SFX limits:**
- At most **1 SFX per 1.0 s** on average, and never two within 0.15 s of each other.
- **Never put an SFX on a hard cut or a caption change.**
- Never let an SFX mask a stressed syllable: duck it or nudge it ±2 frames off the syllable.
- Only use SFX with clear licensing (your library or royalty-free).
- If you want the pure reference sound, I'll leave SFX out entirely.

### 11.3 Music
- An upbeat instrumental bed at a steady level, about −20 dB under the voice, with no build-ups or drops (the edit follows the voice, not musical beats).
- Starts on frame 1 and cuts or fades out within 0.5 s of the final word.

---

## 12. Avoid static screens and clutter

### 12.1 Stillness checks
- Hold ≤1.2 s with no new event → it needs idle life.
- Hold ≤3.0 s maximum even with idle life, unless it's a data card with sub-beats.
- Collage style: animated grain means no frame is ever identical to the last.

### 12.2 Clutter limits (any single frame)
- **One hero + ≤3 supporting elements** (labels, marks, overlay), plus the caption and watermark.
- **≤2 cutout people** on screen, except a group shot that counts as one hero.
- **≤1 overlay card**; when a card appears, the background defocuses.
- **≤1 decorative boil device** (speed lines *or* sunburst *or* floating clocks).
- **Faces stay out of the caption band and the watermark corner.**
- **Remove before you add**: when a new focus element arrives, retire anything the narration has finished with (instant cut on the arrival frame).

---

## 13. Visual identity

### 13.1 Default tokens (replace them with your brand colours if you give me any)

| Token | Value | Use |
|---|---|---|
| `bg.royal` | `#3550B8` | Background rotation |
| `bg.sky` | `#6EB8F5 → #5A86E0` (vertical gradient) | Background rotation |
| `bg.teal` | `#3BB5AC` (+ soft vignette) | Background rotation |
| `bg.magenta` | `#C44BD8 → #7A2FA0` | Background rotation |
| `bg.pink` | `#E0305E` | Background rotation |
| `bg.grass` | `#9BE86A` / `#4CEB72` | Background rotation, pitches |
| `bg.navy` | `#2E3388` | Background rotation |
| `bg.charcoal` | `#333333` | Background rotation (gravitas) |
| `accent.red` | `#E5484D` | X marks, pins, cards, highlighted bars |
| `accent.yellow` | `#FFE13A` | Captions, prices, highlighted team names |
| `ink.white` | `#FFFFFF` | Strokes, sparkles, bursts, UI text |
| `ink.black` | `#000000` | Caption box, tags, silhouettes |

### 13.2 Rules
- **Photos:** cut out, then grayscale with lifted blacks and +10% contrast, **or** a duotone (`#1B1F5E` → `#C9CCFF`). **Never** full-colour photos.
- **Grain:** full-frame paper/noise at 5–10% opacity, re-randomised every 2 frames in the Collage style.
- **Glow:** only on `VERDICT` objects and the one "drama" reveal.
- **Blur:** only motion blur on fast moves, and focus defocus. Never decorative.
- **Tags:** black box with white bold lowercase ("age 26"), or white box with black ("£100.6m"), rotated **−8.7°**, attached to the hip or shoulder.
- **Name blocks:** a heavy geometric sans, 2 lines, flush left at the top-left. A tiny all-caps context line goes above it; the number in the contrast colour for that scene.
- **Section headers:** numeral + coloured heading (`TYPE_ON`) + small-caps subtitle (`SLIDE_IN` up). Top-left at ~8% height. Dims to 30% when no longer active.
- **Watermark:** your monogram, top-right (~6% of width), white outline, never animated.
- **One illustration family per video.** Never mix Collage, Flat and Cartoon.

---

## 14. Deliverable: the Shot Plan (what I produce before building)

For each project I write `shot-plan.md` (for you to read) and `shot-plan.json` (for me to build from) containing:

**A. Header.** Title, length, art family, step rate, BODY caption look, background rotation order, chapter-break choice, the callback stage, and the music/SFX choice.

**B. Narration map.** One row per sentence: time span, story role, tagged keywords with `t_kw` and scores.

**C. Event timeline.** One row per visual event:

```json
{
  "id": "E14",
  "t_start": 32.73, "t_end": 32.98,
  "trigger": {"word": "not", "t_kw": 32.54, "rule": "NEG +0.2"},
  "type": "DRAW", "asset": "red_x", "layer": "L2.5 (behind hero)",
  "from": "stroke1 TL→BR", "to": "complete",
  "easing": "accelerating", "step": "twos",
  "exit": {"rule": "instant", "at": 34.20, "reason": "scoreboard overlay arrives"},
  "sfx": {"name": "marker_scratch", "db": -24, "at": 32.73},
  "purpose": "negation of the agreement"
}
```

**D. Caption track.** Chunk text, start, end, mode (HOOK/BODY).

**E. Asset list.** As in §4.3.

**F. Audit results.** Longest gap between events, maximum element count, transition count, caption-sync check, and the SFX count and spacing.

You approve or change the plan, then I build it. The default renderer is HyperFrames (HTML-to-video), with Remotion as an alternative.

---

## 15. Measured QA after rendering (the same tools I used on the reference)

| Check | Pass criterion |
|---|---|
| Caption sync | Median (word onset − caption appears) within ±0.04 s; ≥90% of chunks within ±2 frames |
| Scene-cut sync | Every hard cut within ±1 frame of its planned `t_kw` |
| Stillness | No stretch over 1.2 s without a visual change outside the caption band (3.0 s allowed for data cards) |
| Overshoot | Measured scale/position never passes the final value (preset compliance) |
| Step rate | The frame-difference pattern shows on-twos behaviour for Collage/Flat |
| Density | ≤1 hero + 3 supporting elements on every sampled frame (2 fps sample) |
| Audio | Music −18 to −23 dB under the voice in gaps; SFX spacing ≥0.15 s; no SFX within 2 frames of a stressed syllable; audio ends ≤0.5 s after the last word |
| Length | 42–54 s; the picture ends ≤0.7 s after the last word |
| Identity | No full-colour photos; one illustration family; no third-party logos without your clearance |

Anything that fails gets fixed and measured again before I hand the video over. I'll report the results to you, including anything I chose to leave as is and why.

---

## 16. Quick-reference card

1. Use the audio as the source of truth: transcribe it, tag the keywords, score them.
2. **A new subject means a hard cut on the stressed syllable and a new background colour.**
3. Additive visuals start slightly before their word and reach ~80% on it. Ideas arrive early, falls land early, and verdicts slam right on the word.
4. Named person → they appear. Place → pin. Number → UI. Verb → animate it. "Not" → red X. Pair → side by side. Thought → bubble. Idiom → literal.
5. Entrances decelerate into place over 0.15–0.5 s with **no overshoot**; exits accelerate out; Collage and Flat animate on twos.
6. Captions: a HOOK until "Well,", then BODY captions of 1 line and 2–4 words at 67% height, swapping hard on the word onset and never emphasised.
7. Use 2–4 designed transitions, one big one at most, and make hard cuts the default.
8. One hero plus at most 3 supporting elements; remove before you add; nothing still for more than 1.2 s.
9. Grayscale or duotone photos, flat saturated backgrounds, grain, your monogram at the top right.
10. Music ~20 dB under the voice; SFX quiet and sparse, never on cuts; end the video ≤0.7 s after the last word.
