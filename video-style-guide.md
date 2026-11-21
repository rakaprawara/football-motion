# Reference Style Guide: Vertical Football Explainer Shorts

**Source material:** 5 vertical shorts (720×1280, 9:16, 24–30 fps, 42–54 s each), all from the same publisher family:

| ID | Title | Length | Art style |
|---|---|---|---|
| V1 | How did a penalty shootout take place with only one team? | 49.0 s | Flat vector stadium + grayscale/duotone photo cutouts |
| V2 | How Liverpool had 2 different managers for 2 different games | 54.0 s | Hand-drawn cartoon caricatures + flat infographics |
| V3 | Most expensive player at each age – Part 2 | 47.1 s | Grayscale photo cutouts on flat color fields (editorial collage) |
| V4 | Why do so many footballers wear tape on their wrists? | 42.2 s | Flat paper-textured illustration + cutout heads |
| V5 | Why does football's worst law exist? | 47.3 s | Thick-outline comic illustration |

**How this was analysed.** Every video was sampled at 2 fps across its full length, and every transition and important moment was sampled again at 8–12 fps. Narration was transcribed with word-level timestamps (Whisper). Audio was checked with a spectrogram and onset detection. All timestamps are measured from frames. Narration word times come from the transcript and are accurate to roughly ±0.1 s. Times marked "~" are estimates.

**Limits (stated up front):**
- I can't listen to audio. Conclusions about music and SFX come from spectrograms and transient analysis, so they're weaker than the visual findings (see §10).
- Because of the 8–12 fps sampling, easing curves are inferred from how much an element moves between frames. Treat durations as ±1 frame.
- The five videos use **two closely related caption systems** and **four illustration styles**. The motion grammar, pacing and narration-to-visual system are the same across all of them, and that shared layer is the real "style DNA". Wherever the videos differ, this guide says so.
- The top-right "A" monogram (V1–V4) and the "Tifo" wordmark (V5) belong to the publisher. When you replicate the style, use **your own** watermark in that slot.

---

## 1. Overall Video Style

**Category:** A short-form editorial explainer, a "did you know" football trivia story told by a single narrator. It's a hybrid of a magazine collage, an infographic and a limited-animation cartoon. It's not cinematic: there's no live footage, no camera shake (with one exception, V1 10.4 s) and no lens effects apart from a depth-of-field blur used for focus.

**Tone:** It plays it straight and dry, with comic timing. The humour comes from literal visual puns: the iris "tunnel" in V1 at 19 s, the thought bubble, the "I… I'm TRAPPED!!" speech bubble, the clocks spinning for "25 years on", and the shamrock appearing on the tape for "good luck". The visuals land the joke and the narrator doesn't.

**Visual complexity:** It's low to medium. On any frame there are usually **1 hero object + 1 caption + 1 persistent watermark**, and sometimes 1 or 2 supporting objects (a tag, a label, a second figure). There are almost never more than 4 meaningful elements at once.

**Balance of assets (rough share of screen time):**
- Illustrated or flat-vector environments and objects: ~50%
- Photo cutouts (grayscale or duotone): ~30% (most in V1, V3 and V4; none in V2 and V5)
- Infographic UI (scoreboards, fixture cards, calendars, bar charts, maps): ~20%
- Live video footage: 0%

**Colour language:**
- Backgrounds are **single saturated flat fields or simple vertical gradients**: royal blue `#3550B8`, sky-to-periwinkle gradient `#6EB8F5 → #5A86E0`, teal `#3BB5AC`, magenta/purple `#C44BD8 → #7A2FA0`, hot pink `#E0305E`, grass green `#9BE86A`/`#4CEB72`, navy `#2E3388`, charcoal `#333333`.
- **Each new scene or beat gets a new background colour.** V3 cycles navy → pink → purple → slate → pink → light blue → green → charcoal → pink → blue, one colour per player.
- Accent colours are **signal red** `#E5484D` (X marks, red card, map pins), **caption yellow** `#FFE13A`, and white.
- **Photos are always desaturated**: either grayscale with lifted blacks (V1, V3, V4 heads) or a blue/violet duotone (the V1 Málaga players). That way photos never compete with the colour-coded backgrounds.

**Texture and finish:**
- A **subtle paper/noise grain** sits over the whole frame (very obvious in V4, present in V1 and V3).
- V4 has a **soft dark vignette** on its teal scenes.
- **Twinkle sparkles**: small 4-point white stars fade in and out at random on the V1 stadium backgrounds, about 2–4 visible at a time, each lasting ~0.3–0.5 s.
- Hard **contact shadows**: a flat gray ellipse sits under the balls and players in V1.
- **Glow** is used only for "special" objects: the trophy at V1 47 s and the yellow card at V5 3.6 s.
- **Blur is used only as a focus tool**: a background defocus when an overlay appears, a fast-move motion blur, or a rack defocus. It's never decorative.

**Visual hierarchy (the order the eye reads a frame):**
1. The **hero object** in the middle third (a figure, trophy, scoreboard, calendar or hand).
2. The **caption**, sitting at about 60–68% of frame height and overlapping the lower half of the hero.
3. **Labels or tags** attached to the hero (`age 26`, `£92.9m`, the club line, the name block, the numbered heading).
4. The watermark in the top right, which never moves.

**How interest is kept up without overload:** One idea is on screen at a time. There's constant *low-amplitude* motion: a slow push or pan, the ball breathing, sparkles. Every 1–2 s a *small* event happens: a tag pops, a pin drops, an X is drawn, a caption swaps. Every 3–5 s a *big* event happens: a new scene, a new background colour or a new figure.

---

## 2. Timeline and Pacing

### Pacing numbers (measured)

| Metric | V1 | V2 | V3 | V4 | V5 |
|---|---|---|---|---|---|
| Major scene changes | 14 | 15 | 12 | 14 | 12 |
| Average scene length | ~3.5 s | ~3.6 s | ~3.9 s | ~3.0 s | ~3.9 s |
| Shortest / longest scene | 0.8 s / 5.5 s | 1.4 s / 8.5 s | 2.5 s / 6 s | 1.4 s / 5 s | 2 s / 6 s |
| Small in-scene events | every ~1.2 s | every ~1.3 s | every ~1 s | every ~1 s | every ~1.5 s |
| Caption swaps | every ~0.55 s | every ~0.6 s | every ~0.6 s | every ~0.65 s | every ~0.6 s |
| Speech rate (transcript) | ~3.1 words/s | ~3.0 words/s | — | — | — |

**The rule I measured:** the frame is **never fully static for more than ~1.5 s**. The longest "nothing new arrives" stretches (V2's line-up card 36.5–43.5 s, V5's "NUKE THE WHALES" 23–27 s) still have a slow push, a caption swap every ~0.6 s, or an element settling.

### Where visual changes land relative to narration

I compared scene cuts to the word timestamps. Here are the measured offsets (negative means the visual comes *before* the word):

| Event | Spoken word (t) | Visual (t) | Offset |
|---|---|---|---|
| V1 cut to map | "**Fulham**" 4.82 | 4.78 | −0.04 (on the word) |
| V1 Málaga pin drops | "**Malaga**" 7.10 | ~7.0 | −0.1 |
| V1 cut to penalty | "**conceded**" 8.66 | 8.63 | −0.03 |
| V1 scoreboard pops | "end **2-2**" 10.90 | 10.93 | 0 |
| V1 cut to Arbeloa | "**furious**" 12.76 | 12.79 | 0 |
| V1 red card | "**red card**" 18.02 | ~17.96 | −0.06 |
| V1 iris starts closing | "down the **tunnel**" 18.92–19.36 | 19.0 | 0 (the metaphor is literal) |
| V1 iris opens | "the **Malaga players**" 21.00 | 21.15 | +0.15 |
| V1 thought bubble | "**penalty shootout**" 24.54 | 24.17–24.58 | **−0.35 (anticipates)** |
| V1 bubble becomes trophy | "**Costa del Sol** trophy" 28.14 | ~28.0 | −0.15 |
| V1 X stroke 1 | "**not** to do" 32.54 | 32.68 | +0.14 |
| V1 scoreboard over X | "**if the game**" 34.06 | 34.2 | +0.14 |
| V1 cut to stadium | "Malaga **fans**" 36.10–36.36 | 36.13 | 0 |
| V1 cut to empty net | "**before converting**" 41.24 | 41.27 | 0 |
| V1 X over penalty | "**didn't count**" 45.38 | 45.45 | +0.07 |
| V1 trophy slam | "**officially** awarded" 47.10 | 47.0 | −0.1 |
| V2 split-wipe to 2 managers | "had **two**" 1.42–1.64 | 1.38 | −0.05 |
| V2 calendars 18/19 | "**consecutive** days" 4.32 | 4.18 | −0.14 |
| V2 UCL trophy wipes in | "After **winning**" 6.54–6.88 | 6.6–7.1 | on the phrase, ahead of the noun "Champions League" |
| V2 confetti burst | "**Champions**" 7.26 | 7.15 | −0.1 |
| V2 trophy swap | "Club **World Cup**" 10.14 | 10.32 | +0.2 |
| V2 calendar pushes in | "the **middle** of the European season" 12.98 | 12.87 | −0.1 |
| V2 fixture card | "against **Monterrey**" 15.62 | 15.43 | −0.2 |
| V2 card-flip transition | "**Alternative dates**" 22.72 | 22.95 | +0.2 |
| V2 X on calendar | "**workable**" 25.66 | 25.5 | −0.15 |
| V2 zigzag reveal | "Liverpool **fielded**" 35.56–35.80 | 35.5 | −0.1 |

**The synchronisation law:**
- **Scene cuts land on the first stressed syllable of the new subject noun**, within ±1 frame ("Fulham", "furious", "conceded", "fans").
- **Additive overlays** (tags, X marks, scoreboards) land **0.05–0.2 s after** the keyword. They *reinforce* it.
- **Imagined or abstract things** (thought bubbles, upcoming topics) land **0.15–0.35 s before** the keyword. They *anticipate* it.
- **Sentence-ending pauses (~0.3–0.4 s) are not used for cuts.** The cut waits for the next sentence's subject word, so the picture never changes in silence. The one deliberate exception is V1 20.7–21.15: a ~0.4 s black hold made by the iris closing, which works as a full stop.

---

## 3. Frame-by-Frame Visual Event Analysis (the key choreography)

The most instructive sequences, measured at 12 fps:

**V1 0.0–4.8 s (hook).** Flat stadium scene with a goal and keeper silhouette, and a big ball in the foreground on a contact shadow. *Three things move at once:* (1) a slow upward camera tilt/push on the stands (~3% per second), (2) the ball **breathes**, scaling about ±4% on a ~1 s cycle with its shadow scaling in sync, and (3) sparkles twinkle. The hook caption swaps every 2–3 words with hard cuts and no in-animation. At 3.0 s the ball **is kicked out of frame**: a ~3-frame upward exit, after which only the shadow stays. At 4.37 s the caption switches from "big title" mode to "small boxed" mode on "Well".

**V1 4.78–8.6 s (map).** Hard cut to a flat Europe map (green land on a blue gradient sea). The map is **already panning slowly** (down-right, ~2% per second). **Pin drop:** the red pin appears at 4.87 with a ~3-frame drop and scale-in (it starts ~30% larger and settles), right on "Fulham". Between 6.4 and 7.0 s the camera **pans down to Spain**: an eased move that keeps both pins in view, with London leaving at the top edge. The second pin drops on "Malaga". *This is the "camera follows the story geographically" pattern.*

**V1 10.1–11.0 s (the penalty).** The keeper silhouette swaps to a dive pose (pose replacement, 1 frame). The ball **travels toward the goal**: its position moves up and left while it shrinks from ~100% to ~30% over ~6 frames with ease-out, and its shadow stays put. There's a **small camera shake/dip** (~10 px over 3 frames), the only shake in the set. At 10.93 the **scoreboard pops**: scale ~60%→105%→100% over ~4 frames. The **background defocuses at the same time** (a gaussian-blur ramp over ~4 frames), and the scoreboard then holds for 2 s.

**V1 12.79 s (Arbeloa).** Hard cut to a light-blue gradient with **radial speed lines** (a manga "emphasis" burst) slowly rotating and pulsing behind a grayscale cutout pair. The man is in photo and the referee is a pure black silhouette. *The photo cutout cycles 2–3 frames of gesture* (13.27 s: the arm moves from the referee's chest to an open palm), which reads as a **stop-motion "puppet"** gesture on the word "Arbeloa". The figures sit statically with a slow scale-up.

**V1 17.96 s (red card).** Hard cut to a new pose of the same pair walking. A red card is held up with a **dotted circle highlight** around it, a thin dashed white ring that slowly rotates.

**V1 19.0–21.4 s (iris "tunnel" transition).** A black matte with paper grain closes in as a **circular iris** around the figures. It shrinks in steps that ease in (19.0–20.45 s) while the subject also shrinks inside it. 20.45–20.75: the iris collapses to a dot, roughly ease-in. 20.75–21.15: **black hold (~0.4 s)**, with the caption still visible on black. 21.15–21.35: the iris **opens on the new scene** (Málaga players in duotone) and expands past full frame in ~5 frames with ease-out. Total ~2.4 s. *It's used once per video at most, for a story "chapter break", and here it doubles as the "tunnel" pun.*

**V1 24.17–24.6 s (thought bubble).** Three **puff circles rise** in sequence from the player's head, at about 2-frame intervals, each popping 0→100%. Then the **cloud bubble** pops in at the top of the frame. It contains a *miniature copy of the earlier penalty scene* (a visual callback). The cloud scales ~0.2→1.05→1.0 over ~4 frames. At 28.0 the bubble's content swaps (hard cut inside the bubble) to the trophy on a pink-white cloud.

**V1 29.7–30.0 s (team assembly).** Hard cut. The manager is centred alone for 1 frame, then **two players slide in from the left and right edges at the same time**, ease-out over ~6 frames, landing slightly behind him and overlapping his shoulders. They exit at 32.6 by **sliding back out the same sides** (~2 frames, ease-in), leaving him alone. Then the X is drawn.

**V1 32.68–33.2 s (X mark draw-on).** Stroke 1 (top-left → bottom-right) **wipes on along its length** in ~4 frames. There's a ~6-frame pause, then stroke 2 (top-right → bottom-left) also wipes on in ~4 frames (from 33.3). The X sits *behind* the figure, so it's a layer below the subject. In V1 45.45–46.0 the same X is drawn *in front of* the goal, with stroke 2 starting at 45.87.

**V1 34.2–34.5 s (overlay focus pull).** The scoreboard pops in front of the man and the X (same overshoot scale). **Everything behind it blurs** over ~3 frames. *Rule: an overlay card always comes with a background defocus.*

**V1 47.0 s (trophy slam).** The trophy appears at ~140% scale with a white outer glow and **settles down to 100% in ~3 frames** (ease-out, no overshoot), with the glow staying on. The previous X is **removed instantly** at the same frame.

**V2 1.38–1.55 s (diagonal split wipe).** A vertical seam line was already in the frame (it's in the first frame at 0.97 s). On "two", **two angled panels sweep across** in opposite directions, top-to-bottom diagonals, about 4 frames each with ease-out. They reveal Klopp on the left and Critchley on the right, each panel holding its own background. *The seam stays in the shot afterwards as the split-screen divider.* V2 repeats this "slanted comic panel" wipe at 4.1–4.35 s (Mané×2 → calendars) and at 6.57–7.15 s (a maroon panel with the trophy pushes in between the two calendars, widens, then takes over the frame).

**V2 12.45–12.87 s (push with motion blur).** The trophy gets a **horizontal motion blur** in place for ~2 frames (anticipation), then whips out to the left over ~3 frames. The calendar **pushes in from the right** over ~2 frames, overshoots slightly left, and settles. Total ~0.4 s.

**V2 15.0–15.45 s (vertical push).** The calendar slides **up and out** while a blueprint-grid panel **rises from the bottom** like a sheet sliding up, with a hard horizontal edge and a black hairline. ~6 frames.

**V2 19.2–19.8 s (list push).** A new fixture row ("Aston Villa vs Liverpool", Tuesday) **fades and slides down from above**. The existing Monterrey row **slides down** to make room (~8 frames, ease-out). The new row starts at ~40% opacity and dimmed, and becomes full only once it's in place. *Timeline-as-list device.*

**V2 22.95–23.4 s (card flip).** The whole blueprint panel **rotates on its Y axis** (a 3D flip with a visible mirrored back face) to reveal a magenta scene with a big app-style calendar icon. ~5 frames, with a thin light edge on the panel's edge.

**V2 23.5–27.5 s (counter).** The calendar number **ticks**: 20→21→22→23 at about 0.5 s per day (a hard swap of the number with a tiny pop), each on a beat of the narration. At 24 the red X slams on (scale ~120→100). Then 25, 26, 27 tick *with the X kept on* (24.5–27.5 s), and the X cross persists over the counting.

**V2 28.3–29.0 s (cross-dissolve to map).** It's a rare **dissolve** (~0.5 s) from the calendar into a UK map, used where the narration changes from *time* to *place*.

**V2 30.9–33.0 s (flight path).** A white **dashed line draws on** from the top-left edge toward Qatar while the map **pans** to follow it (the camera tracks the line's leading end). It ends with a yellow dot pin.

**V2 35.5–36.4 s (zigzag tear reveal).** A thin black zigzag line appears vertically at frame centre. It **opens into a jagged red band** that widens over ~10 frames to cover the frame, revealing the "Liverpool Starting XI" card. Ease-in-out.

**V2 44.0–45.0 s.** A **slow crossfade** (~0.8 s) from the line-up card to Critchley's portrait, with a ghosted overlap.

**V3 4.45–6.1 s (player intro, the V3 template).** Hard cut to a navy field. The **player cutout rises from below the frame** (ease-out, ~4 frames) and keeps a slow continuous **upward drift and scale-up** while on screen. The **`age 26` tag** (black box, white text, rotated about −12°) pops in at 0.3× → 1× over ~3 frames *one frame after* the player. Then the **name block cascades in from the top left**: the price `£92.9m` (yellow) arrives first at 5.7 s, then the name (white, heavy, 2 lines) **slides down from above the frame** at 5.87, pushing the price down, then the club line (`NEWCASTLE – SPURS`, tiny caps) arrives at 6.03. This is a 3-step stagger, ~2 frames apart. The **player's photo swaps** at 6.4 s to a second action pose (a "flipbook" pose change with no transition), so the figure keeps "moving".

**V3 8.3–8.8 s (player-to-player push).** The outgoing player and name block **slide out to the left** (~3 frames). The background colour **hard-cuts** from navy to pink at 8.63. The **age tag stays fixed in place**: it's the anchor, and only its number changes (26 → 27). The new player **slides in from the right edge** (~3 frames, ease-out). *The persistent anchor is what makes a "list" feel continuous.*

**V3 16.28–18.3 s (clock-tunnel bridge).** For the big time jump ("and 25 years on") the background switches to a **concentric-ring tunnel** with tick marks, and **4–5 white analog clocks float and drift**, with their hands spinning fast. Zidane then **fades/zooms up from the tunnel centre** (small → full, with the clocks flying *past the camera* and blurring as they get large, 17.8–18.2). It's a **fly-through zoom** transition.

**V3 33.95–34.6 s (comparison).** A second Ronaldo cutout **slides in from the right** next to the first, so both are visible. Two **price tags scale in on both at once** with clear overshoot (0.3→1.1→1.0 over ~5 frames), and the age tags are duplicated (`age 33`, `age 36`). *Comparisons are side by side, with mirrored tags.*

**V3 38.5–39.2 s.** The Ronaldo name **flies up** and out, and both cutouts slide out left. The pink background cuts in, and Sommer **scales up from ~30% at centre** (a zoom pop, not a slide) to vary the entrance.

**V4 0.0–1.4 s (hook).** An empty teal field with a vignette. The **arm slides up from the bottom** (~2 frames), and a **football rolls in from the right**, passes across the hand and exits left (0.25–1.0 s, a linear-ish fly-through). At 1.05 a **white tape strip draws across** from the left edge (its width grows), wraps (two strips layered) and settles on the wrist on "wear tape" (1.2–2.0 s). *The action is animated literally as it's spoken.*

**V4 3.1–5.3 s.** Teal **question marks pop in** at random scale and position, in sequence (one every ~0.2 s), as the hand **drops out the bottom**. At 5.15 a pale circle **grows from the centre** and **floods the frame** (a circle-wipe to a new flat colour, ~4 frames).

**V4 5.7–8.2 s (shape morph chain).** A thin line → a red rectangle → a second bar → **a medical cross builds bar by bar**. The cross then **rotates 45°** into an X (7.55–7.8, ease-in-out), the background **cuts to royal blue**, and the X **morphs into a "no entry/prohibited" circle**. That circle's inner slash **rotates** (8.05–8.4). *One shape evolves through three meanings: protection → stop → different.*

**V4 9.05–9.7 s (head pops).** The prohibited circle **shrinks to a dot and vanishes** while a Vardy head **scales up from a dot** at top left (0→110→100%, ~3 frames). Then Suárez pops the same way at the right, ~0.4 s later, on his name. The heads are **paper-cut style grayscale photos with a slightly rough edge**.

**V4 10.0–11.5 s.** The arm **rises from below** (~5 frames). At 11.4 the **heads swap expression** (neutral → shouting/laughing) on "broke bones", a reaction face swap with no transition.

**V4 12.65–13.5 s (cast drop).** A cream cast **falls in from above the frame**, rotating slightly (~+10° → 0°) with easing, and **lands on the wrist** ~0.1 s *before* "wear casts". *Physical, gravity-like motion.*

**V4 16.1–17.1 s (poof exits).** A white **radial burst** (8–10 short dash lines) explodes outward from the Suárez head, the head is gone in 1 frame, and the dashes fly out and fade. The same happens to Vardy 0.4 s later. *The burst is the standard "remove a person" exit.*

**V4 17.5–18.0 s.** A tiny green dot on the cast **scales up into a four-leaf clover** (~5 frames, with overshoot) on "good luck ritual".

**V4 35.0–36.3 s (chart build).** The hand **drops out** (falls off the bottom, ease-in). An **L-shaped axis draws on**: the vertical line first, then the horizontal (~4 frames each). The label "FOULS AGAINST" **types/fades in letter by letter**. The **bars grow up from the baseline** one after another, ~2 frames apart, ease-out. The **highlight bar is magenta** and starts small. At 36.5 it **shoots up** to the top while Neymar's head **pops on top of it**. *Data as a story beat: the "winner" bar arrives last and biggest.*

**V4 39.2–40.5 s.** Three tumbling-player photo cutouts **pop in one at a time** (~0.5 s apart), each with a **radial burst** and a black ground-shadow ellipse. It's a comic "impact" accent on "hefty tumble to the floor".

**V5 0–3.0 s.** A comic-style back-view of a player celebrating, arms up. **Animated "shake" lines** (a white scribble halo) jitter around his arms on a ~2-frame boil (hand-drawn line-boil). The yellow captions are big: 2 lines, outline plus drop shadow, centred at ~45% height.

**V5 3.0–3.4 s.** The referee **whips in from the bottom right** with heavy **motion blur** (~3 frames), and the yellow card arrives first, as a blurred streak. On "yellow card" (3.6–4.0) a **glow halo grows** behind the card, then a **sunburst background of rotating rays** fades up behind everything (3.8–4.1). That's the "drama" reveal.

**V5 5.2–5.6 s (rack focus).** On "And is it really about…" the **player in the foreground blurs** (defocus over ~4 frames) and the **referee stays sharp**: a rack focus that moves attention to the authority figure for the question.

**V5 9.0–14.6 s (jersey carousel).** The sponsor shirts **slide in from the right and push the previous shirt out left**, one per mention. The last one is slightly **offset and overlapped**, so each shirt overlaps the previous for a frame or two. ~4 frames per push.

**V5 14.4–16.5 s (numbered-list heading).** A **soft-edged horizontal wipe** reveals the new stadium-board scene from the top down (14.5–14.9, a feathered edge). The heading builds in three steps. (1) **"1."** pops at 14.6. (2) **"PREVENTING"** in red **types on letter by letter** (15.1–15.9, ~1 letter per 2 frames). (3) The subtitle **"OVER CELEBRATION"** **slides up from under** the heading (16.4). When the section is over, the heading **dims to ~30% opacity** (18.4) instead of leaving. *Section titles are the only typewriter animation in the set.*

**V5 17.6–17.9 s.** The fan **jumps up into the frame from below** with motion blur (~3 frames), lands with a tiny overshoot, and then a speech bubble **pops in from its tail** at 18.3 ("HE TOOK HIS SHIRT OFF!?"). A second fan does the same at 19.0 with a blur trail, and a second bubble pops ("LET'S RIOT!!").

**V5 21.0–21.4 s (colour-bar push).** A flat magenta panel **slides up from the bottom** and covers the old scene (a vertical push). The new player then **whips up** with motion blur at 22.5.

**V5 27.4–28.0 s.** A green panel **slides up** in the same way. A **pattern of faint clocks drifts and rotates** in the background throughout section 3. At 31.5 hands **reach in from the bottom** pulling a red shirt over the head (an action that matches "taking their shirts off").

**V5 40.6–41.6 s.** The referee **slides in from the left** with motion blur, and the shirtless player **fades and whips in** from the right.

---

## 4. Transition Analysis

| # | Transition | Where | Trigger | First mover / direction | Speed & easing | Blur? | Purpose |
|---|---|---|---|---|---|---|---|
| T1 | **Hard cut on the subject noun** | Most scene changes in all 5 videos | First stressed syllable of the new subject | Nothing moves; the new scene is often *already in motion* (a pan or drift) on its first frame | 0 frames | No | Keeps momentum. The motion carried over hides the cut |
| T2 | **Slide-out / slide-in with a persistent anchor** | V3 every player, V5 jerseys | The next item in a list | Old subject exits **left**, new one enters from the **right**; the anchor (age tag) stays put | 3–4 frames each, ease-in out, ease-out in | Sometimes slight | List continuity, "next item" |
| T3 | **Diagonal comic-panel wipe** | V2 1.4, 4.1, 6.6 | A number or contrast word ("two", "consecutive", "after winning") | A slanted panel edge sweeps across; the new panel carries its own background | ~4–8 frames, ease-out | No | Introduces a *pair* or the next chapter; panels suggest comparison |
| T4 | **Whip push with motion blur** | V2 12.5, V5 jerseys/referee | Change of object within the same topic | Old object blurs in place for 1–2 frames (anticipation), then exits horizontally; new one enters from the opposite side with a slight overshoot | ~8–10 frames total | **Yes**, directional | Energy, fast "next thing" |
| T5 | **Vertical sheet push** | V2 15.0, V5 21.0, 27.4 | Topic or section change | A full-frame flat panel slides **up from the bottom**, with a hard edge (sometimes a black hairline) | ~6 frames, ease-out | No | Chapter or section break |
| T6 | **Circle/iris** | V1 19–21.4 (iris), V4 5.15 (circle flood) | A story beat ends (V1) / a concept changes (V4) | The matte closes on the subject → black hold → opens on the new subject / a circle grows from centre to full | Iris 2.4 s total; flood ~4 frames | No | Chapter break, a visual pun ("tunnel") |
| T7 | **3D card flip** | V2 22.95 | "Alternative…" (the narration pivots) | The whole panel rotates on its Y axis, showing a mirrored back face | ~5 frames | No | "Flip side" / alternative |
| T8 | **Zigzag tear** | V2 35.5 | "To get around the issue" (a solution reveal) | A black zigzag line opens into a widening red band that becomes the new frame | ~10 frames, ease-in-out | No | Dramatic reveal of the solution |
| T9 | **Fly-through zoom** | V3 16.3–18.2 | A time jump ("25 years on") | Floating clocks scale past the camera; the new subject grows from the tunnel centre | ~1.9 s (a bridge scene) | Yes on the near objects | Passing time |
| T10 | **Cross-dissolve** | V2 28.3, 44.0 | Time→place shift; a narrative handover | Opacity crossfade | 0.5–0.8 s, linear | No | Soft link between eras or roles. **Rare: at most 2 per video** |
| T11 | **Soft-edge vertical wipe** | V5 14.5, 36.4 | A numbered section starts | A feathered horizontal edge travels top→down | ~6 frames | Soft edge | Enters a "list item" section |
| T12 | **Shape-morph bridge** | V4 5.7–8.4 | Concept evolution ("evolving into something different") | One shape rebuilds or rotates into the next meaning | 0.25–0.4 s per step | No | Shows a *concept changing* |
| T13 | **Pop-replace (in-place swap)** | V1 28.0 bubble content, V2 calendar numbers, V4 expressions, V3 pose swaps | Next value or reaction | Content swaps in 1 frame, sometimes with a ~2-frame scale pop | 0–2 frames | No | A "flipbook" sense of life, counting |

**The logic:** cuts and in-place swaps do ~70% of the work and **always ride the keyword**. Designed transitions (T3–T12) are reserved for **conceptual pivots**: pairs, time jumps, solutions, sections. Each video uses **2–4 different designed transitions, never the same fancy one twice in a row**, and at most **one "big" one** (iris, tear or fly-through) per video.

---

## 5. Object Animation and Motion Design

### Recurring entrance behaviours (the motion vocabulary)

| Name | What it looks like | Duration | Easing | Used for |
|---|---|---|---|---|
| **Pop** *(corrected in §15)* | Scale ~0–70% → 100%, **no overshoot** | 0.25–0.5 s (6–15 frames) | Exponential ease-out (UI cards, tags) or S-curve ease-in-out (photo heads) | Tags, heads, scoreboards, bubbles, pins, clover |
| **Slam** *(corrected in §15)* | Scale ~112% → 100%, with a glow | ~0.33 s | Exponential settle, no overshoot | Trophy, "final verdict" objects |
| **Rise** | Translate up from below the frame | 3–5 frames | Ease-out | Figures, arms, hands, panels |
| **Slide** | Translate in from a side edge | 3–6 frames | Ease-out (in) / ease-in (out) | List items, team-mates, jerseys |
| **Drop** | Fall from above with a small rotation that settles to 0° | ~8 frames | Ease-in (gravity) then a hard stop | Casts, physical objects |
| **Draw-on** | A stroke grows along its length | ~4 frames per stroke | Linear-ish | X marks, axes, dashed flight paths, tape strips |
| **Type-on** | Letters appear left→right | ~2 frames per letter | Stepped | Section headings only |
| **Grow** | A bar or shape scales from its base | 2–4 frames | Ease-out | Bar charts, the cross build |
| **Whip-in** | Enters fast with directional blur and a slight overshoot | ~3 frames | Very fast ease-out | Comic characters (V5) |

### Exits
- **Hard removal** (1 frame) is the most common. It happens when the next element is the new focus: the X vanishes as the trophy slams, the scoreboard vanishes on a cut.
- **Slide out** the way the element came in (list items, team-mates).
- **Kick or throw off-screen** for objects with physics (the ball at V1 3.0).
- **Burst poof** with radial dashes for people (V4).
- **Shrink to a dot** when one shape hands off to the next (V4 9.1).
- **Dim to ~30% opacity** for persistent headings (V5 18.4). They aren't removed until the section changes.

### Idle / secondary motion (every held shot has at least one)
- A slow **camera push or drift**: 2–4% scale or a few px per second (all videos).
- **Breathing** loop on hero objects, ±3–5% on a ~1 s period (V1 ball and shadow).
- **Pose flipbook**: the photo cutout changes to another frame of the same action every 1–3 s (V1 Arbeloa, V3 every player). It reads as stop-motion.
- **Line boil**: hand-drawn emphasis lines jitter every 2 frames (V5).
- **Rotating background elements**: speed lines (V1), sunburst rays (V5), floating clocks (V3, V5), dashed highlight rings (V1).
- **Twinkles**: random sparkle fades (V1 stadium, V2 trophies).

### Character of the motion
It's **graphic and cartoon-physical, not floaty**. *(Corrected in §15:)* Entrances take 0.15–0.5 s with **no overshoot in any of the 12 entrances I measured**. Everything decelerates straight into place, and there are no bounces or springs anywhere. Gravity objects ease in and stop hard. Motion blur appears only on fast whips (V2, V5) and never on pops. Rotation is minimal (tags have a fixed −10 to −15° tilt; casts settle from ~10°), except for **meaning-carrying rotations** (the cross → X, the prohibited-sign slash).

### Choreography rules
- **Staggered cascades, 1–2 frames apart**: price → name → club in V3, puffs → bubble in V1, axis → label → bars in V4.
- **Subject first, labels second**: the figure lands, then the tags attach.
- **Pairs arrive together** (V1 team-mates from both sides) or **in name order** (V4 heads on their own names).
- **Persistent anchors**: the age tag in V3, the seam line in V2, the hand/arm in V4 (it stays across 6+ beats while objects are added to it), and the stadium in V1 (it comes back for the climax).
- **Additive storytelling on one stage**: V4's hand is a stage that collects tape, a cast, a clover and finger tape, and V1's stadium collects the ball, keeper, scoreboard and X, then the trophy. The viewer watches one picture *accumulate* meaning.

---

## 6. Objects Following the Narration (the visual storytelling system)

The underlying system is: **every noun phrase the narrator stresses becomes a picture, and every verb becomes a motion.**

| Narration | Visual representation | Animation | Timing | Purpose |
|---|---|---|---|---|
| "penalty shootout" (V1 hook) | Ball on the spot in front of the goal | Ball breathes, then gets kicked | Whole hook | Establishes the subject |
| "Fulham were playing… away to **Malaga**" | Europe map with pins | Pin drops; the camera pans London→Spain | Pin on each place name | Geography = **map with pins** |
| "they **conceded** a penalty" | Ball + keeper at the goal | Kick, ball travels, keeper dives | Kick on "led the game" | **Verbs are animated literally** |
| "to end **2-2**" | Scoreboard "90:00 2:2" | Pop + background blur | On "2-2" | **Numbers become UI objects** |
| "a **furious** Alvaro Arbeloa" | Cutout + silhouette referee + speed lines | Gesture flipbook | Cut on "furious" | Emotion = graphic background (speed lines) |
| "red card… going **down the tunnel**" | Red card raised; iris closes | Iris shrinks to black | On "down the tunnel" | **Idioms become literal transitions** |
| "they'd been **expecting** a penalty shootout" | Thought bubble with a mini penalty scene | Puffs + bubble pop | **0.35 s before** "penalty shootout" | Expectation = **thought bubble** |
| "the Costa del Sol **trophy**" | The bubble content becomes a trophy | In-bubble swap | On "Costa" | The bubble updates with the next idea |
| "Fulham… had agreed **not** to…" | Manager with team-mates; then he's alone with a raised palm and a red X | Team-mates slide out; X draws on | X on "not" | **Negation = a red X drawn over the thing** |
| "**if the game ended in a draw**" | The scoreboard returns over the X | Pop + blur | On "if the game" | Calls back an earlier object (a recurring prop) |
| "**didn't count**" | X drawn over the empty net | 2-stroke draw | On "didn't count" | Negation again |
| "**officially awarded** to Malaga" | Glowing trophy slams over the scene | Slam + glow | On "officially" | Verdict = the biggest, glowiest object, last |
| "two different managers" (V2) | Split screen, one manager per panel | Diagonal wipe | On "two" | **Comparison = side by side** |
| "two **consecutive days**" | Two calendar icons, 18 and 19 | Panel wipe | On "consecutive" | Dates = calendar icons |
| "alternative dates… **none workable**" | A calendar counting up, then X'd | Number ticks; X slam | X on "workable" | Counting = ticking numbers |
| "7-hour **flight** to Qatar" | Dashed flight path on the map | Draw-on + camera follow | On "flight" | Travel = a dashed line |
| "youngest ever starting line-up" (V2) | Team-sheet card with names and numbers | Zigzag tear reveal | On "fielded" | Lists = a broadcast-style graphic |
| "26-year-old… Sandro Tonali… £92.9m" (V3) | Cutout + age tag + name block + price | Rise + pop + cascade | Tag on the age, name on the name | **Data = typographic labels on the subject** |
| "and **25 years on**" (V3) | Clocks floating in a tunnel | Fly-through | On "25 years on" | Time = clocks |
| "Ronaldo is both… at **33 and 36**" | Two Ronaldos side by side with mirrored tags | Slide-in + double tag pop | On "33 and 36" | Comparison = duplication |
| "Why do footballers **wear tape**" (V4) | Hand + tape strip | Tape draws across the wrist | On "wear tape" | Verb = action |
| "a number of **reasons**" | Question marks | Staggered pops | On "reasons" | Uncertainty = "?" |
| "**protective** measure… **evolving** into something **different**" | Cross → rotates to X → prohibited sign | Build, rotate, morph | One step per keyword | **Abstract concept = an evolving icon** |
| "**broke bones**" | Heads change to pained/shouting faces | Expression swap | On "broke bones" | Emotion = a face swap |
| "**wear casts**" | Cast drops onto the wrist | Gravity drop | 0.1 s before "casts" | Physical object = physical motion |
| "**good luck** ritual" | Shamrock grows on the tape | Pop from a dot | On "good" | Metaphor = a symbol |
| "**stop**… preventative" | Octagon stop sign with a hand | Pop | On "preventative" | Prevention = a stop sign |
| "one of the most **fouled** players" | Bar chart, Neymar's bar tallest | Axis draw, bars grow | Highlight bar last | **Superlatives = a chart with a winning bar** |
| "a hefty **tumble** to the floor" | Tumbling cutouts with impact bursts | Pops + bursts | On "tumble" / "floor" | Literal + comic emphasis |
| "**punished** with a **yellow card**" (V5) | The referee whips in holding a glowing card | Whip + glow + sunburst | On "yellow card" | Authority = a dramatic reveal |
| "the interest of **sponsors**" | Fictional sponsor shirts | Carousel pushes | One per mention | Plural nouns = a sequence of examples |
| "**deemed an act of provocation**" | Fans with speech bubbles ("LET'S RIOT!!") | Jump-in + bubble pop | On "provocation" | Abstract consequence = invented dialogue |
| "**political messages**" | Player revealing a "NUKE THE WHALES" undershirt | Whip-up + sun disc | On "political messages" | An exaggerated, made-up example (comic) |
| "took a long time to put them back on" | A player stuck in his shirt: "I… I'm TRAPPED!!" | Bubble pop | On "a long time" | A joke as illustration |
| "**misidentification**" | The referee points at a shirtless player: "Put that shirt back on whoever you are" / "Seriously?" | Slide-in + two bubbles | On "football shirts" | A dialogue punchline |

**Distilled rules:**
1. **Person named → that person's image appears on their name** (a cutout, caricature or head). Unnamed groups appear as silhouettes or generic illustrations.
2. **Place named → a map with a pin; travel → a dashed line plus a camera follow.**
3. **Number named → a UI object** (scoreboard, price tag, age tag, calendar, bar).
4. **Verb named → that action is animated on the existing object** (kick, wrap, drop, tumble, jump).
5. **Comparison → side by side (split, duplicate or pair).**
6. **Negation → a red X drawn over the thing being negated.**
7. **Expectation or idea → a thought bubble; reaction or consequence → a speech bubble with invented comic dialogue.**
8. **Time → clocks or calendars; time passing → spinning hands or ticking numbers.**
9. **Abstract concept → one icon that morphs as the concept evolves.**
10. **Idiom → make it literal** ("down the tunnel" → an iris tunnel).
11. **Verdict or punchline fact → the biggest, glowiest object, which slams in last.**

---

## 7. Captions and Typography

### Two caption systems (pick one per video and don't mix them)

**System A, "Boxed Yellow" (V1, V3):**
- **Typeface:** a heavy condensed grotesque in all caps (close matches: *Anton*, *Bebas Neue Bold*, *Oswald Bold* or *Knockout*). It's slightly rounded and has tight tracking.
- **Colour:** yellow `#FFE13A` text on a **solid black rectangle** with tight padding (~6 px vertical, ~8 px horizontal at 720 w). No outline and no shadow.
- **Size:** cap height ~22 px on a 720×1280 frame (about **3% of frame height**), so it's small.
- **Position:** horizontally centred; its **centre sits at ~67% of frame height** (y ≈ 860 px).

**System B, "White Shadow" (V2, V4, V5):**
- Same condensed all-caps family, **white**, with no box and a **soft dark drop shadow** (~2 px offset, ~4 px blur, ~60% black).
- The same small size, centred, at **~67%** (V2 also uses ~60% when a graphic needs the space).

**Common to both:**
- **2–4 words per caption chunk, one line only, never two.** Chunks break at phrase boundaries ("WHEN IN THE LAST" / "MINUTE"; "AWAY TO MALAGA").
- **Each chunk is on screen ~0.4–0.9 s** and swaps with a **hard cut. There's no entrance animation, no word-by-word highlight and no karaoke colour.** The new chunk appears on the frame its first word starts.
- The caption **stays on screen through every transition**, including the 0.4 s black hold in V1. It's the one constant layer, together with the watermark.
- Captions sit **on top of everything**, overlapping the hero's torso. The hero is framed so its face is above the caption line.
- Numbers are written as numerals with the narrator's punctuation ("TO END 2–2", "29 YEAR OLD", "5–0").
- Emphasis comes **only from the graphics, never from the caption styling.**

### The "Hook Title" caption (the first 3–5 s of every video)
- The same condensed font, **~2.5–3× larger** (cap height ~55–65 px), **two lines**, centred at **~45–50% of frame height** (right over the hero).
- V1, V2 and V3: **white with a dark drop shadow**. V4 and V5: **yellow** with a dark outline/shadow.
- It swaps every 2–3 words with hard cuts ("DID YOU / KNOW" → "THERE WAS / ONCE A" → "PENALTY / SHOOTOUT"…).
- **It switches to the small caption system at the "answer pivot" word**: "Well," (V1 4.4 s, V2 5.6 s, V3 4.0 s, V4 3.0 s) or "And is it…" (V5 5.4 s). *The size drop itself signals "hook over, story starts".*

### Other in-graphic typography
- **Name blocks (V3):** a heavy geometric sans in white, 2 lines, tight leading (surname under first name), flush left at the top-left. A tiny all-caps transfer line sits above ("NEWCASTLE – SPURS"), and the fee sits below in a **colour picked to contrast with that scene's background** (yellow on navy, lavender on slate, off-white on charcoal).
- **Tags:** black rectangles with white bold lowercase ("age 26"), or white rectangles with black text ("£100.6m"), **rotated −10° to −15°**, stuck to the player's hip or shoulder.
- **Section headings (V5):** a big numeral ("1.") in the main text colour, a heading word in red/gold with a type-on, and a subtitle in letter-spaced small caps that slides up. They sit top-left at ~8% height.
- **UI text** (scoreboards, fixtures, line-ups): a clean bold sans in a broadcast-graphics style, with a yellow highlight on the team in focus ("**Liverpool** vs. Monterrey").
- **Credits (final ~5 s):** tiny two-column credits (name in bold, role in regular) at bottom-left, **fade in under the caption** for ~2.5 s. Then a picture-agency and music credit paragraph fades in for ~2 s. *Optional for your own videos.*

---

## 8. Graphic Elements and Assets

| Category | Examples | How it's introduced | Treatment | Layering |
|---|---|---|---|---|
| **Photo cutouts (full body)** | Players, managers (V1, V3) | Rise from below / slide from a side / zoom pop | **Grayscale or blue-violet duotone**, clean cutout, no outline, no shadow (V3) or a flat ground shadow (V1 tumbles) | The hero layer, mid-ground, often overlapping the background type |
| **Photo heads** | Vardy, Suárez, Neymar, Neuer (V4) | Pop from a dot | Grayscale, rough paper-cut edge, sometimes in a solid circle badge (Neuer) | Floating in front of the illustration |
| **Silhouettes** | Referee, keeper, striker (V1) | Cut / pose swap | Pure black fill | Same plane as the cutouts, used for **unnamed** people |
| **Caricature illustrations** | Klopp, Critchley, Salah, Mané (V2); comic figures (V5) | Panel wipes, whips | Thick black outline, cel shading (V5 has stronger line art) | Full-frame hero |
| **Flat vector props** | Ball, goal, trophy, calendar, cast, tape, stop sign, glove, tape rolls | Pop / drop / draw-on | Flat colour, minimal shading, a grain overlay | Centre stage |
| **Environments** | Flat stadium with stands and pennant bunting, a pitch (V1); maps (V1, V2); blueprint grid (V2); concentric tunnel (V3); stadium ad boards (V5) | Cut with a slow push already moving | Simplified, high saturation | Background |
| **Infographic UI** | Scoreboard, fixture rows, line-up card, bar chart, calendar month grid | Pop + background blur / grow | Rounded dark card with a light border (scoreboard); black bars with yellow highlight text (fixtures) | Always the **top** content layer when present |
| **Marks and symbols** | Red X, dashed highlight ring, red map pins, yellow pin dot, dashed flight line, "?" marks, shamrock | Draw-on / pop | Flat signal red, white or teal | In front of or behind the subject, chosen deliberately (V1 X behind the man, X in front of the net) |
| **Comic devices** | Thought bubble with puffs, speech bubbles, radial speed lines, impact bursts, sunburst, line-boil halo | Pop / rotate / boil | White fills, black outlines (V5), hand-lettered all-caps dialogue | Bubbles attach to a head via a tail or puffs |
| **Particles** | Confetti (V2 UCL), sparkles/twinkles | Burst / random fades | Gold squares; white 4-point stars | Behind the hero |
| **Watermark** | Monogram top-right | Static for the whole video | White outline glyph, ~40 px | Topmost, never animated |

---

## 9. Composition and Screen Layout

**There's a fixed layout grid across all five videos (720×1280):**

```
 y=0    ┌─────────────────────────────┐
        │ [labels/name block]   [logo]│  ← 4–10%: name blocks, section headers, watermark (top-right ~x 620, y 70)
 y≈130  │                             │
        │   HERO ZONE                 │  ← 15–60%: face/upper body/main object
        │   (faces above 55%)         │     hook title sits at ~45–50%
        │                             │
 y≈860  │  ████ CAPTION ████          │  ← ~67%: caption centre line
        │                             │
        │   hero's legs / ground /    │  ← 70–95%: lower body, ground shadows, credits (final 5 s)
        │   credits                   │
 y=1280 └─────────────────────────────┘
```

- **Mostly centred, symmetrical compositions.** A single hero is centred. Pairs split left and right of centre with a ~10–20% overlap. Labels sit **asymmetrically top-left**, balancing the logo top-right.
- **Depth comes from 3–4 flat planes**: background colour or illustration → environment → hero cutout → overlays (tags, X, scoreboard) → caption → logo. Depth is reinforced by **background blur when an overlay appears** (V1, V5) and by **parallax** between the environment and the hero during slow pushes.
- **Scale relationships:** heroes fill ~60–75% of frame height. Overlay cards are ~45% of frame width. Tags are ~15% of frame width.
- **Re-composing for new information:** instead of cutting, the editor **makes room**. Team-mates slide away so the X has space (V1 32.6). Fixture rows push down to fit the new one (V2 19.3). A second Ronaldo slides in and the first stays put (V3 34). The bar chart replaces the hand by the hand *falling away* (V4 35). Persistent elements hold their exact position across the change.
- **Edges are entry points.** Everything enters from a frame edge or from a dot. Arms and hands always enter from the bottom edge, as if the viewer's own POV is the camera.

---

## 10. Sound Design and Audio Sync

*What can be stated with confidence, from the spectrograms, transients and transcripts:*
- **Narration dominates.** It's a single male voice-over in a dry, close-mic, studio style at a steady ~3 words/s. Pauses between sentences are **~0.3–0.4 s**, and there are almost no longer gaps.
- **There's a music bed underneath at a very low level.** In speech gaps the spectrogram shows steady tonal harmonics at roughly 30–40 dB below the voice. The credits name production-library tracks ("New Perspective in the Street", "Let It Flow", APM Music), so it's **upbeat library music used as a bed, ducked far under the voice**. My tempo estimates (92–108 BPM) are unreliable because the speech dominates the signal.
- **I couldn't isolate distinct SFX.** Over the transitions I checked (V1 4.78, 10.4, 19–21, 47.0), the spectrogram shows no clear broadband whoosh or impact that's separate from speech consonants. If there are SFX, they're mixed very quietly. **I can't confirm pops, whooshes or impacts, so I'm not listing any.**
- **The edit is synced to the voice, not to music beats.** Every measured cut lines up with word onsets (±1 frame) rather than a regular beat grid.

**Practical recommendation for replication** (this is inference, not something observed): keep music at around −25 to −30 dB under the voice. If you add SFX, keep them subtle and short: a soft pop for tag/head pops, a light swish for whip pushes, a marker squeak or scratch for X draw-ons. They should sit below the voice like the rest of the mix.

---

## 11. Micro-Animations and Small Details

- **Ball breathing and shadow sync** (V1): the hero never freezes during the hook.
- **Sparkle twinkles** on the stadium background (V1): ambient life that costs nothing.
- **Slow push on every held shot**: even "static" scoreboard holds keep scaling gently.
- **Pose flipbooks**: a cutout changes pose every 1–3 s (Arbeloa's arm, Tonali walking → jogging, Sommer crouch → celebrate). That gives the illusion of movement from stills.
- **Expression swaps** on a reaction word (V4 heads).
- **Anticipation blur** before a whip (V2 trophy blurs in place for ~2 frames before it leaves).
- **One-frame stagger** in cascades (name block, thought-bubble puffs, bar chart).
- **Dashed highlight ring** slowly rotating around the red card (V1).
- **Rotating background patterns** (speed lines, sunburst rays, drifting clocks).
- **Line boil** on hand-drawn emphasis marks (V5).
- **Headings dim instead of exiting** (V5), so the viewer keeps a sense of "where we are in the list".
- **Callbacks**: the mini penalty scene inside the thought bubble, the scoreboard returning, the stadium returning for the payoff. Recurring props make a 45 s story feel planned.
- **The persistent seam line** in V2 stays after the split wipe as a divider.
- **Background defocus under overlays** (always ~3–4 frames, never instant).
- **The caption stays through the black iris hold**, so the viewer is never without text.

---

## 12. THE VIDEO'S EDITING DNA

1. **Open on a question in big two-line hook captions for 3–5 s, then drop to small one-line captions on the pivot word "Well,".** The size change is the structural cue.
2. **One hero, one caption, one logo.** Never put more than ~4 meaningful elements on screen.
3. **Cut on the subject noun.** Scene changes land within ±1 frame of the first stressed syllable of the new subject. Never cut in a pause.
4. **Reinforce with overlays 0.05–0.2 s after the keyword; anticipate ideas and thoughts 0.15–0.35 s before.**
5. **Every stressed noun becomes an object, and every verb becomes an action on an existing object.**
6. **Negation is a red X drawn in two strokes. A verdict is a glowing object that slams in last.**
7. **A new scene or a new list item means a new flat background colour.** Photos are always desaturated (grayscale or duotone) so the colour belongs to the design.
8. **Liveliness comes from texture and swaps, not camera moves** *(corrected in §15)*. Most holds are locked off. V1 and V3 never sit still because the grain updates every 2 frames; V2 holds go fully still for up to 3 s while only the captions change. Add a small event every ~1–1.5 s and a scene change every ~3–4 s.
9. **Entrances decelerate into place over 0.15–0.5 s with no overshoot** *(corrected in §15)*. Exits accelerate out. Flat-collage videos animate on twos (12 fps); cartoon videos animate on ones. Blur appears only on fast moves and focus pulls.
10. **Elements enter from frame edges or from a dot.** Bodies and hands rise from the bottom; list items slide in from the right and out to the left.
11. **Keep anchors persistent** (a tag, divider, stage or hand) and let content change around them.
12. **Captions: 2–4 words, one line, hard swaps, no styling emphasis, always on top, at ~67% height.** Emphasis lives in the graphics.
13. **Overlay cards always come with a background defocus.**
14. **Hard cuts and in-place swaps carry ~70% of changes.** Save designed transitions for conceptual pivots: pairs (panel wipe), time jumps (fly-through or clocks), solutions (tear), sections (vertical push or soft wipe). Use at most one "big" transition per video.
15. **Make idioms and abstractions literal**: tunnel → iris, expectation → thought bubble, consequences → invented comic dialogue, concepts → a morphing icon.
16. **Build up the stage.** Reuse one scene and add objects to it, then bring it back for the payoff.
17. **Length is 42–54 s. Structure is hook (≈4 s) → setup (≈10 s) → complication (≈15 s) → twist/resolution (≈15 s) → payoff line (≈4 s) with the credits fading in under the last 5 s.**

---

## 13. Complete Timeline Breakdowns

### V1 – "Penalty shootout with only one team" (full detail)

| Time | Narration | Visuals | Objects/Assets | Animation/Motion | Transition | Caption/Text | Sound | Editing purpose |
|---|---|---|---|---|---|---|---|---|
| 0.00–0.48 | "Did you know" | Flat pink stadium, goal + keeper silhouette, big ball foreground | Ball, shadow, goal, stands, bunting, sparkles | Slow upward tilt/push; ball breathes ±4%; twinkles | Opens in motion | HOOK white 2-line "DID YOU / KNOW" at ~48% | VO starts on frame 1 | Hook on the object of the story |
| 0.48–1.16 | "there was once a" | Same | Same | Continued push | — | "THERE WAS / ONCE A" | — | Keep moving while the question builds |
| 1.16–1.96 | "penalty shootout" | Same | Same | Ball keeps breathing | — | "PENALTY / SHOOTOUT" | — | The keyword matches the object on screen |
| 1.96–2.70 | "that took place" | Same | Same | — | — | "THAT TOOK / PLACE" | — | — |
| 2.70–4.36 | "with only one team?" | Ball kicked away (~3.0); empty goal, shadow remains | Ball exits up | 3-frame exit; the ball reappears tiny in the net (~3.5) | — | "WITH ONLY / ONE TEAM?" | — | Visual question: a ball with no taker |
| 4.37–4.77 | "Well," | Empty goal | — | Twinkles | — | **Switch to small boxed caption** "WELL FULHAM" | Short pause | Hook→story pivot |
| 4.78–6.40 | "Fulham were playing a pre-season friendly" | Europe map, blue sea / green land | Red pin on London | Map drifts; pin drops at 4.87 | **Hard cut on "Fulham"** | "WERE PLAYING" → "A PRE-SEASON" | — | Geography |
| 6.40–7.40 | "away to Malaga" | Map pans down to Spain | 2nd pin on Málaga | Eased pan ~0.6 s; pin drop ~7.0 | Camera move | "AWAY TO MALAGA" | — | Camera follows the story |
| 7.40–8.62 | "when in the last minute they" | Map holds | Both pins | Slow drift | — | "WHEN IN THE LAST" → "MINUTE" | — | Breathing room |
| 8.63–10.40 | "conceded a penalty that led the game" | Blue stadium, ball on the spot, keeper set | Ball, keeper silhouette | Push in; ball breathes | **Hard cut on "conceded"** | "THEY CONCEDED" → "A PENALTY" → "THAT LED THE GAME" | — | Re-establish the stage (callback to the hook) |
| 10.40–10.90 | "…to end" | The kick: ball to the net, keeper dives | Dive pose swap | Ball shrinks and travels ~6 frames; small camera dip | — | "TO END 2–2" | — | A verb animated |
| 10.93–12.78 | "2-2. At full time," | Scoreboard "TIME 90:00 MALAGA 2:2 FULHAM" | Rounded dark card | Pop 60→105→100%, ~4 fr; **background blur ramps** | Overlay | "TO END 2–2" → "AT FULL TIME" → "A FURIOUS" | — | Numbers → UI; focus pull |
| 12.79–17.95 | "a furious Alvaro Arbeloa marched onto the field to remonstrate with the referee before receiving" | Light-blue gradient + radial speed lines; grayscale Arbeloa + black referee silhouette | Cutout pair | Gesture flipbook at 13.27; speed lines pulse; slow push | **Hard cut on "furious"** | "ALVARO ARBELOA" → "MARCHED ONTO THE FIELD" → "TO REMONSTRATE" → "WITH THE REFEREE" → "BEFORE RECEIVING" | — | Emotion = speed lines |
| 17.96–19.00 | "a red card and going" | The pair walk; red card raised | Red card + dashed ring | Ring rotates | Hard cut (pose change) | "A RED CARD" → "AND GOING" | — | Keyword object |
| 19.00–20.75 | "down the tunnel with the rest of his team." | Iris closes around them | Black grain matte | Stepped ease-in iris; subject shrinks | **Iris (pun on "tunnel")** | "DOWN THE TUNNEL" → "WITH THE REST" → "OF HIS TEAM" | — | Chapter break + joke |
| 20.75–21.15 | "The Malaga" | Black | — | Hold ~0.4 s | — | "THE MALAGA" | — | Full stop |
| 21.15–24.16 | "players, though, remained out on the pitch. You see, they'd been expecting" | Duotone Málaga players on the pitch, stadium behind | 3 cutouts | Iris opens ~5 frames; slow push | Iris open | "PLAYERS THOUGH" → "REMAINED OUT" → "ON THE PITCH" → "THEY'D BEEN EXPECTING" | — | New chapter: the home side |
| 24.17–27.99 | "a penalty shootout to take place at the end of the match to decide who would win" | A thought bubble above the player with a mini penalty scene | Puffs + cloud | Puffs pop in sequence, cloud pops | Overlay (anticipates by 0.35 s) | "A PENALTY SHOOTOUT" → "TO TAKE PLACE" → "AT THE END" → "OF THE MATCH" → "TO DECIDE" → "WHO WOULD WIN" | — | Expectation = thought |
| 28.0–29.70 | "the Costa del Sol trophy. Fulham, though," | The bubble now shows a trophy | Trophy in a pink cloud | In-bubble swap | — | "THE COSTA DEL SOL" → "TROPHY" → "FULHAM THOUGH" | — | Stakes |
| 29.71–32.59 | "insisted that prior to the match they had agreed" | Blue gradient; grayscale Fulham manager; two players slide in | 3 cutouts | Simultaneous L/R slides, ~6 fr | **Hard cut on "Fulham"** | "INSISTED THAT PRIOR" → "TO THE MATCH" → "THEY'D AGREED" | — | The other side of the argument |
| 32.60–34.19 | "not to do a penalty shootout" | Players slide out; manager alone with palm raised; red X behind him | X | 2-stroke draw-on | — | "NOT TO DO A PENALTY" → "SHOOT OUT" | — | Negation |
| 34.20–36.12 | "if the game ended in a draw. With Malaga" | Scoreboard pops in front; background blurs | Scoreboard (callback) | Pop + blur ramp | Overlay | "IF THE GAME" → "ENDED IN A DRAW" → "WITH MALAGA" | — | Condition = recurring prop |
| 36.13–41.26 | "fans in the stadium still expecting a shootout, striker Jauregi placed the ball on the penalty spot" | Wide stadium stands + pitch; black silhouette striker walks in from the right, bends and places the ball | Silhouette, ball | Slow pan; walk-in ~37.4–38.0 | **Hard cut on "fans"** | "FANS IN THE STADIUM" → "STILL EXPECTING" → "A SHOOTOUT" → "STRIKER JAUREGI" → "PLACED THE BALL" → "ON THE PENALTY SPOT" | — | Unnamed→silhouette; action |
| 41.27–43.40 | "before converting it into an empty net" | Callback to the penalty stage with **no keeper**; ball → net | Ball | Breathing, then the ball travels to the net (~43.2) | **Hard cut on "before"** | "BEFORE CONVERTING IT" → "INTO AN EMPTY NET" | — | Payoff of the hook image |
| 43.4–45.44 | "in front of the home support. The penalty" | Ball in the net; empty goal | — | Push | — | "IN FRONT OF THE HOME" → "SUPPORT" → "THE PENALTY" | — | Credits fade in at the bottom-left (~43.9) |
| 45.45–46.99 | "didn't count, but the trophy was" | Red X drawn over the goal | X | 2 strokes (45.45, 45.87) | Overlay | "DIDN'T COUNT" → "BUT THE TROPHY WAS" | — | Negation |
| 47.00–48.99 | "officially awarded to Malaga." | Glowing trophy slams over the scene | Trophy + glow | Slam 140→100%, 3 fr; X removed | Overlay | "OFFICIALLY AWARDED" → "TO MALAGA" | VO ends ~48.6 | Verdict / payoff |

### V2 – "Liverpool: 2 managers, 2 games" (condensed)

| Time | Narration (approx.) | Visual / motion | Transition | Purpose |
|---|---|---|---|---|
| 0.0–1.37 | "Did you know that Liverpool once" | Caricature of a celebrating player (hands to ears), a seam line down the centre; slow push | Opens in motion | Hook; HOOK captions in white |
| 1.38–2.9 | "had two different managers for" | Split screen: Klopp (left) / Critchley (right) | **Diagonal panel wipe on "two"** | Comparison |
| 2.9–4.1 | "two different games in two" | Two Mané panels, red kit vs teal kit, cups behind | Panel wipe | Pairs |
| 4.18–5.6 | "consecutive days?" | Calendar icons 18 \| 19 on yellow/blue panels | Panel wipe | Dates → icons |
| 5.6–6.55 | "Well, sort of." | Same; captions switch to small white | — | Pivot |
| 6.57–10.3 | "After winning the Champions League in 2019, Liverpool had qualified for the Club World Cup" | A maroon panel slides between the calendars with the UCL trophy, widens to full; confetti burst on "Champions"; slow push | Panel push | Achievement |
| 10.32–12.45 | "which in its old format took place" | Club World Cup trophy on green, sparkles | Hard cut / swap on "World Cup" | Swap object |
| 12.45–15.0 | "in the middle of the European season. Liverpool's first" | The trophy whips out left; December 2019 calendar pushes in (full of red X'd match days) | **Whip push with blur** | Busy schedule = crossed calendar |
| 15.0–19.1 | "match against Monterrey was set to take place in Qatar on 18 December" | A blueprint panel slides up; fixture row "Liverpool vs. Monterrey / Club World Cup" fades in; the date line appears on "18th" | Vertical push | Fixture = broadcast UI |
| 19.2–22.9 | "the day after a quarterfinal match against Aston Villa in the Carabao Cup" | A new row slides in above; the old row pushes down | List push | Timeline list |
| 22.95–25.4 | "Alternative dates for the Villa game were proposed, but none of them" | Panel **3D flips** to magenta with a big calendar icon; date ticks 20→21→22→23 | **Card flip** | Counting |
| 25.5–28.2 | "were deemed workable for Liverpool, meaning that in theory Jurgen" | A red X slams; dates keep ticking 24→27 under it | Overlay | Negation |
| 28.3–30.8 | "Klopp's side would have to finish at Villa before boarding" | Crossfade to a UK map; yellow pin at Birmingham | **Dissolve** | Time→place |
| 30.9–35.4 | "a seven-hour flight to Qatar and playing less than 24 hours later. To get around the issue," | A dashed flight line draws SE; the camera tracks it to the Gulf; yellow pin at Qatar | Camera follow | Travel |
| 35.5–44.0 | "Liverpool fielded their youngest ever starting line-up… under-23 players, while the first team, including Klopp, travelled to Qatar" | **Zigzag tear** reveals the "Liverpool Starting XI" card (numbers, names, cartoon player); long hold with a slow push | **Tear reveal** | Solution reveal |
| 44.0–47.9 | "And under-23 boss Neil Critchley stood on the Villa Park touchline instead of Klopp" | Slow crossfade to Critchley's portrait | Dissolve | Hand-over |
| 47.9–54.0 | "where they lost 5-0 before Klopp returned to see his side beat Monterrey 2-1 the next day." | Klopp slides in front of Critchley (overlapping, he's in the foreground and Critchley soft behind); credits fade in ~49.5 | Slide-in | Payoff |

### V3 – "Most expensive player at each age, Part 2" (condensed)

| Time | Caption / narration | Visual / motion | Transition |
|---|---|---|---|
| 0.0–2.0 | "WHO IS THE MOST / EXPENSIVE PLAYER / AT EACH AGE" | A hand holding a phone on purple; an old player illustration kicking a ball inside the screen; the phone **zooms toward the camera** until the screen fills the frame (1.5–2.0); a banknote drifts behind | Push-in "through" the phone |
| 2.0–4.4 | "IN FOOTBALL HISTORY? / PART 2" | The illustration changes to a **child** player (age reversed, a visual "each age" gag); notes float | Hard swap |
| 4.45–8.5 | "WELL THE MOST EXPENSIVE 26 YEAR OLD IS SANDRO TONALI…" | Navy; cutout rises; `age 26` tag pops; price→name→club cascade; pose swap at 6.4 | Hard cut + rise |
| 8.5–12.4 | "…EXPENSIVE 27 YEAR OLD IS STILL LUIS SUAREZ AFTER HIS MOVE TO BARCELONA" | Pink; slide L-out / R-in; anchor tag 26→27; Liverpool kit → Barça kit pose swap on "to Barcelona" | Slide push with anchor |
| 12.5–16.2 | "AT 28 IT'S EDEN HAZARD'S MOVE FROM CHELSEA TO REAL MADRID" | Purple; Chelsea → Real kit swap on "Real Madrid" | Slide push |
| 16.28–18.2 | "AND 25 YEARS ON" | Concentric tunnel + drifting spinning clocks | **Clock fly-through** |
| 18.2–20.9 | "ZIDANE IS STILL THE MOST EXPENSIVE 29 YEAR OLD" | Slate; Zidane emerges from the tunnel centre | Zoom out of the tunnel |
| 20.9–23.4 | "HARRY KANE IS THE MOST EXPENSIVE AT 30" | Pink; hard cut | Cut |
| 23.45–27.9 | "WHILE NEYMAR'S MOVE FROM PSG TO AL HILAL…31 YEAR OLD" | Light blue; PSG → Al Hilal pose swap on "to Al Hilal" | Cut |
| 28.0–31.0 | "RIYAD MAHREZ IS THE MOST EXPENSIVE AT 32" | Green; the tag lands before the figure (28.0), then the cutout rises | Cut |
| 31.1–38.6 | "CRISTIANO RONALDO IS BOTH THE MOST EXPENSIVE AT 33 AND 36 FOR HIS MOVES TO JUVENTUS AND MANCHESTER UNITED" | Charcoal; one Ronaldo, then a 2nd slides in on "and 36"; twin price tags pop with overshoot; club labels pop on each club name | Slide-in addition |
| 38.6–44.9 | "34 YEAR OLD… YANN SOMMER FOR HIS MOVE FROM BORUSSIA MÖNCHENGLADBACH TO BAYERN MUNICH" | Pink; Sommer zoom-pops from small; kit swap on "Bayern"; credits fade ~42.4 | Scale pop |
| 44.9–47.1 | "AND THE MOST EXPENSIVE 35 YEAR OLD IS MARKO ARNAUTOVIC" | Blue; slide-in; agency credits | Slide |

### V4 – "Why footballers wear wrist tape" (condensed)

| Time | Caption | Visual / motion | Transition |
|---|---|---|---|
| 0.0–3.0 | HOOK yellow: "WHY DO / SO MANY FOOTBALLERS / WEAR TAPE / ON THEIR WRISTS?" | Teal + vignette; the arm rises; a ball rolls across; tape draws across the wrist, two strips | Opens in motion |
| 3.0–5.1 | "WELL / THERE ARE A NUMBER / OF REASONS / IN SOME CASES" | "?" marks pop in a stagger; the hand drops away | — |
| 5.15–7.8 | "IT STARTS OFF / AS A PROTECTIVE / MEASURE / BEFORE EVOLVING" | Circle flood → pale teal; a line → bars → red medical cross; the cross rotates 45° | Circle wipe; shape build |
| 7.9–9.0 | "INTO SOMETHING / DIFFERENT" | Blue; X → prohibited sign, slash rotates | Morph |
| 9.0–11.4 | "JAMIE VARDY / AND LUIS SUAREZ / FOR EXAMPLE" | The sign shrinks to a dot; heads pop on their names; the arm rises | Shrink/pop hand-off |
| 11.4–15.9 | "BOTH BROKE BONES / IN THEIR HANDS / AND WERE REQUIRED TO / WEAR CASTS / BUT DECIDED TO KEEP / WEARING THE / STRAPPING LONG AFTER" | Expression swaps; the cast drops onto the wrist | — |
| 15.9–17.4 | "THE INJURY / HAD HEALED" | Heads poof out in radial bursts | Burst exit |
| 17.4–19.4 | "AS A GOOD / LUCK RITUAL / OTHER PLAYERS" | A shamrock grows on the cast | Pop |
| 19.4–22.4 | "WILL USE THE TAPE / AS A PREVENTATIVE / MEASURE / GOALKEEPERS" | Teal; stop sign pops and scales to fill | Hard cut + pop |
| 22.4–27.0 | "FOR EXAMPLE / TAPE THEIR FINGERS / TOGETHER IN ORDER / TO AVOID / ANY FURTHER DAMAGE" | A ball hits the hand; a big open hand; tape wraps two fingers | Hard cut |
| 27.0–30.9 | "AND MANUEL NEUER / HAS EVEN WORN / FINGERED GLOVE / IN ORDER TO DO THIS / NEYMAR" | The hand slides out right; a Neuer head badge pops; a glove slides in from the right | Push |
| 31.0–33.6 | "MEANWHILE WORE / ZINC OXIDE / ATHLETIC TAPE" | Blue; Neymar head + red tape rolls | Cut |
| 33.6–35.1 | "TO SUPPORT HIS / WRIST JOINTS" | The rolls exit up; an arm with red wrist tape rises | Vertical exchange |
| 35.1–38.6 | "AS ONE OF THE MOST / FOULED PLAYERS / IN FOOTBALL HISTORY / THIS PROVIDED HIM / WITH PROTECTION" | The hand falls; axis draws; bars grow; the magenta Neymar bar shoots up with his head on top; credits fade ~37.5 | Build |
| 38.7–42.2 | "FROM WRIST INJURIES / WHENEVER HE TOOK / A HEFTY TUMBLE / TO THE FLOOR" | The chart exits left; tumbling cutouts pop in with impact bursts | Push + pops |

### V5 – "Football's worst law" (condensed)

| Time | Caption | Visual / motion | Transition |
|---|---|---|---|
| 0.0–3.0 | HOOK yellow: "WHEN / FOOTBALLERS / TAKE OFF / THEIR SHIRTS / TO CELEBRATE / GOALS" | Comic back-view of a player, arms up; boil lines; a crowd silhouette backdrop | Opens in motion |
| 3.0–4.6 | "THEY ARE / PUNISHED / WITH A / YELLOW CARD" | The referee whips in with blur; the card glows; a rotating sunburst fades up | Whip-in |
| 4.6–5.4 | "BUT WHY?" | Hold | — |
| 5.4–8.6 | small: "AND IS IT / REALLY ABOUT / PROTECTING EXPOSURE / FOR SPONSORS? / WELL, NOT ENTIRELY" | **Rack focus**: player blurs, the referee stays sharp | Focus pull |
| 8.7–14.4 | "THE INTEREST / OF SPONSORS / IS A MINOR FACTOR / BUT THERE ARE / FOUR OTHERS / WHEN THE LAW / WAS INTRODUCED / IN 2004" | Magenta; a fictional sponsor-shirt carousel (red → striped → white, worn) | Push carousel |
| 14.5–17.6 | "IT WAS JUSTIFIED / AS PREVENTING / OVER CELEBRATION" | Stadium ad-board scene via a soft wipe; "1." pops, "PREVENTING" types on, the subtitle slides up | Soft wipe + type-on |
| 17.6–21.0 | "WITH TAKING / A SHIRT OFF / DEEMED AS AN ACT / OF PROVOCATION / IT ALSO" | Fans jump in with blur; speech bubbles "HE TOOK HIS SHIRT OFF!?" / "LET'S RIOT!!"; the heading dims | Whip-ins |
| 21.0–27.4 | "PREVENTED PLAYERS / FROM DISPLAYING / POLITICAL MESSAGES / UNDER THEIR SHIRT / WHICH WAS / A COMPLICATION / MAKERS PREFERRED / NOT TO INDULGE / ALSO" | A magenta panel slides up; "2. PREVENTING / POLITICAL MESSAGES"; the player whips up revealing a "NUKE THE WHALES" undershirt on a gold sun disc | Vertical push |
| 27.4–36.3 | "THE BLANKET BAN / WAS INSTITUTED / AS A PROTECTION / AGAINST TIME / WASTING IN INSTANCES / WHERE PLAYERS / [TOOK OFF] THEIR SHIRTS / AND THEN TOOK / A LONG TIME / TO PUT THEM BACK ON" | A green panel slides up; drifting clock pattern; "3. PREVENTING / TIME WASTING"; a player stuck in his shirt + "I… I'M TRAPPED!!" bubble | Vertical push |
| 36.3–41.0 | "AND FINALLY, ALBEIT / TENUOUSLY / WAS JUSTIFIED / AS A WAY OF ENSURING / AGAINST INSTANCES / OF MISIDENTIFICATION" | Empty-stand scene via a wipe; "4. PREVENTING / MISIDENTIFICATION?" | Soft wipe |
| 41.0–47.3 | "FOOTBALL SHIRTS / ARE NAMED / AND NUMBERED / AND IT MAKES / A REFEREE'S JOB / SLIGHTLY EASIER / IF THEY REMAIN ON / THE PLAYER" | The referee slides in with blur pointing; the shirtless player; bubbles "PUT THAT SHIRT BACK ON WHOEVER YOU ARE" / "SERIOUSLY?"; credits ~41.3 | Slide-ins |

---

## 14. Replication Blueprint

### A. Visual Style Guide
- **Canvas:** 1080×1920 (scale everything ×1.5 from the 720 measurements), at 25 or 30 fps.
- **Backgrounds:** a flat field or a 2-stop vertical gradient, with **one new hue per scene**. Rotate through ~6 saturated hues: royal blue, teal, magenta/purple, hot pink, grass green, navy or charcoal.
- **Grain:** a full-frame noise/paper overlay at 5–10% opacity, plus an optional soft vignette.
- **Photos:** cut out, then **grayscale (lifted blacks, slight contrast)** or **duotone** (dark navy → periwinkle/white). Never use full-colour photos.
- **Illustration:** pick ONE family per video: flat vector with no outlines (V1, V4), thick-outline cartoon (V2, V5), or photo collage (V3). Don't mix families inside a video.
- **Accents:** signal red for X marks, pins and cards; caption yellow; white for UI strokes, sparkles and bursts.
- **Logo:** your own small monogram at the top right (~6% of width, white outline style), static.

### B. Motion Style Guide
- *(Corrected values; full measurements in §15.)*
- **Frame rate of the animation:** for the flat or collage look, step animations on twos (hold every pose for 2 frames). For the cartoon look, animate on ones.
- **Pop (UI cards, tags):** scale 70%→100% over ~0.25 s with expo-out and no overshoot. **Pop (photo heads):** scale 0→100% over ~0.45 s, ease-in-out, no overshoot.
- **Slam:** scale 112%→100% over ~0.33 s with expo-out, plus an optional white glow.
- **Rise/slide:** 4–6 frames, cubic-out in / cubic-in out. In: from the bottom (bodies, hands) or from the right (list items). Out: to the left.
- **Drop:** 8 frames with ease-in, plus a ~10° rotation that settles to 0 and a hard stop.
- **Whip:** 3 frames with directional motion blur and ~5% overshoot; add 1–2 frames of in-place blur before an exit.
- **Draw-on:** ~4 frames per stroke, close to linear; a 4–6 frame gap between X strokes.
- **Idle:** a 2–4% per second push on every shot; a ±4% breathing loop (1 s period) on hero props during long holds; a pose swap every 1–3 s on cutouts.
- **Background defocus:** a 3–4 frame gaussian ramp (~8–12 px at 720 w) whenever an overlay card appears.
- **Stagger:** 1–2 frames between parts of a group.

### C. Caption Style Guide
- **Font:** Anton or Bebas Neue (Bold), all caps, tracking 0 to +10.
- **Hook (first ~4 s):** 2 lines, cap height ~6% of frame height, centred at 45–50%, white with a drop shadow (or yellow with a dark outline). Swap every 2–3 words.
- **Body:** 1 line, cap height ~3% of frame height, centred at **67%**.
  - *Boxed:* `#FFE13A` on a solid `#000` box, padding ~0.5 em × 0.35 em.
  - *Shadowed:* white, shadow offset 2 px, blur 4 px, 60% black.
- 2–4 words per chunk, broken at phrases. Swap with a hard cut at the first word's onset. No per-word highlight, no animation, always the top layer, and kept on screen through transitions.
- **Switch from hook to body at the narrator's pivot word** ("Well," / "But…" / "And is it…").
- Write numbers as numerals; scores use an en dash ("2–2").

### D. Narration-to-Visual Workflow
1. **Get a word-timed transcript** (Whisper or similar) and mark every **stressed noun, number, verb, negation, comparison and idiom**.
2. **Assign one visual per sentence subject.** That's your scene list. Cut on the first stressed syllable of each new subject. A new scene gets a new background colour.
3. **Within each scene, map the secondary keywords to additive events** using the §6 table: person → cutout or head pop; place → pin; number → tag or UI card; verb → action; "not" → red X; comparison → a second element side by side; expectation → thought bubble; consequence → speech bubble with a funny line.
4. **Timing:** overlays 2–5 frames after the keyword; thoughts and imagined things 4–8 frames before; cuts on the keyword.
5. **Keep a recurring prop or stage** and bring it back for the payoff.
6. **Exits:** remove the old element on the same frame the next focus arrives, or slide it out the way it came.
7. **Check density:** a small event every 1–1.5 s, a scene every 3–4 s, and no frame static for more than 1.5 s.
8. **Pick 2–4 designed transitions** for the conceptual pivots, with at most one "big" one.

### E. Transition Library (when to use what)
- **Hard cut on the subject** is the default (≥60% of changes).
- **Pop-replace / flipbook** for counts, reactions and pose changes.
- **Slide L/R with an anchor** for the next item in a list or ranking.
- **Diagonal panel wipe** when introducing a pair, comparison or "two" anything.
- **Whip push with blur** to hop between related objects quickly.
- **Vertical sheet push (from the bottom)** for a new section or numbered item.
- **Soft-edge top-down wipe + typed heading** to start a numbered list section.
- **Card flip** for "alternatively / on the other hand".
- **Zigzag tear** for "the solution was…" reveals.
- **Iris close → black hold → iris open** for a chapter break or a "tunnel/end" pun. Once per video at most.
- **Fly-through / clocks** for time jumps.
- **Cross-dissolve (0.5–0.8 s)** for a soft era or role handover. At most twice.
- **Shape-morph chain** when a concept "evolves".

### F. Pacing Guide
- **Total:** 42–54 s. **Hook** 3–5 s (2–3 word big captions), **setup** ~10 s, **complication** ~15 s, **twist/resolution** ~15 s, **payoff** ~3–4 s, with credits under the last ~5 s.
- **Scene length:** 2.5–5 s typical. Allow up to ~8 s only if in-scene events keep coming every second (list or data cards).
- **Caption chunk:** 0.4–0.9 s.
- **VO:** ~3 words/s, sentence gaps 0.3–0.4 s, no dead air. Music a long way under the voice.
- **Speed up** in lists (one item every ~4 s with sub-events every 1 s). **Slow down** only for one beat before the payoff (the iris black hold, or the hold before the trophy slam).

### G. Animation Principles
1. Fast in, settle out: one overshoot, never a bounce chain.
2. Things come from edges or dots, never fade in from nowhere (except type and credits).
3. Gravity is real for physical props; graphic UI ignores gravity and pops.
4. Blur means speed or focus only.
5. Move the camera to follow the story (map pans, flight-path tracking), not just to decorate.
6. Hold anchors still while content changes around them.
7. Animate verbs on existing objects before adding new objects.
8. Secondary motion on every hold (push, breathe, twinkle, boil, rotate).
9. Stagger groups by 1–2 frames, subject first and labels second.
10. Remove the old focus on the frame the new focus lands.

### H. Editing Checklist
- [ ] 9:16, 42–54 s, a word-timed transcript made.
- [ ] The hook question uses big 2-line captions; the switch to small captions happens on the pivot word.
- [ ] Every scene cut lands on a stressed subject noun (±1 frame); no cuts in pauses.
- [ ] Each new scene or list item has a new flat background colour.
- [ ] All photos are cutouts in grayscale or duotone; one illustration family per video.
- [ ] Every person named appears on their name; places use pins; numbers use tags or UI; verbs are animated.
- [ ] Negations use a 2-stroke red X; the verdict slams in last with a glow.
- [ ] Comparisons are shown side by side.
- [ ] At least one thought or speech bubble or literal-pun moment.
- [ ] One recurring prop or stage that comes back for the payoff.
- [ ] Entrances are 3–5 frames with one overshoot; whips have blur; overlays come with a background defocus.
- [ ] No frame static for more than 1.5 s; a small event every 1–1.5 s; a scene every 3–4 s.
- [ ] Captions: 1 line, 2–4 words, at ~67% height, hard swaps, on screen through transitions.
- [ ] 2–4 designed transitions, at most one big one, at most 2 dissolves.
- [ ] Music ducked well under the VO; any SFX subtle.
- [ ] Your own watermark at the top right; credits fade in under the final ~5 s (optional).
- [ ] No borrowed branding, characters or logos from the reference publisher.

---

## 15. Review Pass: Corrections and Additions (measured)

**Method for this pass.** In the first pass I judged motion by eye from contact sheets. This time I extracted frames at the videos' native frame rate and measured them in code:
- bounding boxes and pixel areas of individual elements, frame by frame
- frame-difference analysis, to find duplicated frames and still stretches
- phase correlation, to detect camera drift
- an automatic caption-change detector, checked against Whisper's word timestamps
- spectrograms of every gap in the narration

Pixel values are on the 720×1280 source. Times are in seconds.

### 15.1 Corrections to the first pass

| # | First pass said | What the measurements show | Evidence |
|---|---|---|---|
| C1 | Pops go "0 → 105–115% → 100%, 3–5 frames, one overshoot" | **No overshoot in any of the 12 entrances I measured.** Pops decelerate straight into their final size and are slower than I said: **0.25–0.5 s**. | V1 scoreboard width 301→392→427→429 px (70%→91%→99.5%→100%) from 10.975–11.225 s. V3 price-tag area 513→714→843→943→958 from 34.12–34.45 s. V4 Vardy head width 15→29→53→89→145→187→209→219→221 from 9.02–9.53 s. |
| C2 | Trophy slam starts at ~140% | Starts at **~112%** and settles exponentially over **~0.33 s** (height 936→878→853→839→836 px, 47.03–47.36 s). | V1 |
| C3 | V1 ball "breathes ±4% on a ~1 s loop" | **No breathing.** The ball **rises ~125 px into place** while the stadium behind it moves ~70 px the opposite way, both easing out over 0–0.8 s. After that the ball is **completely still** from 0.8 to 2.75 s, then gets kicked at 2.8 s. | V1 frame grid |
| C4 | "Every held shot has a slow 2–4%/s push" | **Most holds are locked off.** I measured zero drift on V1 Arbeloa (13.0–17.5), V1 map hold, V1 wide stadium, V3 Tonali and Kane, V4 hand stage and V5 "Nuke the Whales". Real camera moves happen only in a few places: V1 penalty stage tilts 41 px/s, V1 duotone players drift −22 px/s, and V2's line-up card zooms slowly and evenly, growing 8% over 6.8 s (~1.2%/s). | Phase correlation + bounding boxes |
| C5 | "The frame is never static for more than ~1.5 s" | True only for V1 and V3 (their grain re-randomises every 2 frames). With the caption band excluded, **V2 goes fully still for up to 3.0 s** (32.5–35.5, 20.3–22.8, 13.0–14.9), **V4 for up to 1.7 s** (24.9–26.6, 20.5–22.1) and **V5 for up to 1.1 s**. During these holds, the caption swaps every ~0.6 s are the only motion. | Frame-difference analysis |
| C6 | V1 iris closes in eased steps from 19.0 s and the black hold lasts ~0.4 s | **Three phases.** (1) At 19.11 s a fixed vignette ring appears in two jumps and covers ~28% of the frame. It then **holds static for 1.3 s**. (2) It **collapses in ~0.33 s** (20.44→20.78, ease-in). (3) A black hold lasts **0.30 s** (20.78–21.07), then the iris **opens in ~0.25 s** (21.11→21.36, ease-out). The collapse starts 0.18 s after "team." ends, so the black hold fills the sentence pause. That makes this the **one deliberate exception to "never cut in a pause"**. | Non-black pixel area per frame |
| C7 | V1 speed lines "slowly rotate and pulse" | They're **redrawn at random positions every frame** (a 24 fps boil), even though the figures around them animate on twos. They never rotate. | 8 consecutive frames at 14.00–14.29 s |
| C8 | V2 trophy "blurs in place for ~2 frames as anticipation" | There's **no anticipation hold.** It's a pure ease-in exit: the centre-x moves 2, 6, 11, 17, 23, 33, 47 then 59 px per frame (12.46–12.78 s, ~0.36 s). The blur is ordinary motion blur that grows with speed. | Centroid track |
| C9 | V2 calendar pushes in "with a slight overshoot" | **No overshoot.** The left edge goes 676→470→180→92 px and stops: 4 frames (0.16 s), ease-out. It overlaps the outgoing trophy by ~1 frame. | Red header edge |
| C10 | V2 X "slams on, scale ~120→100" | It **grows outward from the centre** over 0.28 s (25.54→25.82) and spills past the frame edges. Red area 18.9k→33k→61k→110k→159k→237k→275k→291k px. Probably a scale-up from small, not a slam down. | Red area per frame |
| C11 | Tags rotated −10° to −15° | The V3 age tag is rotated **−8.7° (±0.3°)** and holds that angle exactly. | Principal-axis angle |
| C12 | V3 players are "pushed": old out left, new in right | It's **exit → empty beat → enter.** The outgoing player leaves on ease-in over 0.2 s (8.33–8.54). The frame then holds **~0.17 s with only the age tag**, the background colour cuts during that gap (8.625), and the new player enters from the right at 8.71. | Centroid of the low-saturation pixels |
| C13 | Cast lands "~0.1 s before 'wear casts'" | It **starts falling on "were"** (12.58 s; word at 12.64) and **lands at ~13.12 s, 0.28 s before "wear"** (13.40). The whole fall happens during "were required to". | Cast area/top edge |
| C14 | V5 rack focus takes ~4 frames on "And is it" | It's a **gradual ~0.5 s defocus** that starts right after "why?" (4.88 s) and is complete by ~5.45 s, as "And is it" begins. | Native-fps crops |
| C15 | Suárez's head pops "~0.4 s after Vardy, on his name" | It starts growing at ~9.4–9.48 s, **~0.15–0.2 s before "Luis"** (9.62), and reaches full size at ~9.88 during "Suarez" (9.80). It's an ease-out, not an S-curve. | Width per 2 frames |
| C16 | V5 referee whips in "~3 frames" | It takes **0.20 s** (3.10–3.30, ease-out) and starts **exactly on "punished"** (3.10). | Navy-pixel area |

### 15.2 Things the first pass missed entirely

**A. Two animation frame rates (the biggest omission).** Frame-difference patterns show:

| Video | Container fps | How often the animation updates | Evidence |
|---|---|---|---|
| V1 penalty | 24 | **On twos = 12 fps** | Alternating 0/1 pattern; every tracked bounding box repeats in pairs (scoreboard, X, iris, pin) |
| V3 transfers | 24 | **On twos = 12 fps** | Same pattern; name-block and slide positions repeat in pairs |
| V4 wrist tape | 29.97 | **On twos ≈ 15 fps** | Head-pop widths repeat in pairs (15,15 / 29,29 / 53,53…) |
| V2 Liverpool | 25 | **On ones = 25 fps** | A new position every frame (trophy exit, calendar push) |
| V5 shirt law | 25 | **On ones = 25 fps**, with a per-frame line boil | 76% of frames change |

**Why it matters:** the stepped 12 fps motion is what gives the flat-collage videos their "cut paper / stop-motion" feel. Smooth 25–30 fps motion would make them look like generic templates. Match the step rate to the illustration style. Some decorative layers ignore the step rate: the V1 speed lines boil at a full 24 fps.

**B. The grain is animated, not static.** In V1 and V3, the frame changes every 2 frames even during holds: the paper grain re-randomises at 12 fps. That's why those two videos never register as still. V4's grain is static (it has long runs of identical frames).

**C. How long elements take to arrive, relative to the spoken word.** Measured precisely, any element that takes ≥0.25 s to arrive is **timed so it finishes on the keyword, not starts on it**:

| Element | Animation runs | Keyword (onset) | Starts relative to the word | Finishes relative to the word |
|---|---|---|---|---|
| V1 London pin | 4.92→5.17 | "Fulham" 4.82 | +0.10 | +0.35 |
| V1 scoreboard | 10.98→11.23 | "2-2" 11.06 | −0.08 | +0.17 |
| V1 X, stroke 1 | 32.73→32.98 | "not" 32.54 | +0.19 | +0.44 |
| V1 X, stroke 2 | 33.23→33.39 | "penalty" 33.36 | −0.13 | +0.03 |
| V1 trophy | 47.03→47.36 | "officially" 47.10 | −0.07 | +0.26 |
| V2 calendar push | 12.80→12.92 | "middle" 12.98 | −0.18 | −0.06 |
| V2 X grow | 25.54→25.82 | "workable" 25.66 | −0.12 | +0.16 |
| V4 Vardy head | 9.02→9.53 | "Jamie" 8.94 | +0.08 | +0.59 |
| V4 Suárez head | ~9.45→9.88 | "Luis" 9.62 | −0.17 | +0.26 |
| V4 cast fall | 12.58→13.12 | "wear casts" 13.40 | −0.82 | −0.28 |
| V5 referee | 3.10→3.30 | "punished" 3.10 | 0.00 | +0.20 |
| V5 fan jump | 17.66→18.06 | "with taking" 17.76 | −0.10 | +0.30 |
| V5 speech bubble | 18.28→~18.6 | "shirt" 18.56 | −0.28 | ~+0.04 |

**Refined rule:** start the entrance **0–0.2 s before** the keyword so it reaches about 80% size on the word's stressed syllable. Physical "falls" are the exception: they're timed to **land just before** the noun they illustrate. When I wrote "overlays land 0.05–0.2 s after", I was describing when they become *fully readable*, not when they start.

**D. Caption sync, measured on every caption change (288 changes across V1–V4):**

| Video | Changes detected | Median (word onset − caption appears) | Middle 50% range |
|---|---|---|---|
| V1 | 61 | −0.023 s | −0.08 to +0.09 |
| V3 | 48 | −0.033 s | −0.08 to +0.07 |
| V2 | 75 | 0.000 s | −0.04 to +0.06 |
| V4 | 56 | −0.054 s | −0.09 to +0.06 |

So each caption appears **on the first word's onset, to within ±2 frames** (within the error of the word timestamps), with at most a 1-frame lag. Captions never anticipate. I couldn't measure V5 reliably: its white sponsor shirts (9–14 s) set off the white-caption detector.

**E. How captions behave, confirmed frame by frame.**
- The hook title switches in a single frame ("DID YOU / KNOW" at 0.500 → "THERE WAS / ONCE A" at 0.542). The small captions do the same ("WELL FULHAM" is complete on its first frame, 4.333). There's no fade, scale or slide on either.
- **Hook typography:** V1 is white, has no outline, and has a **soft charcoal drop shadow offset straight down ~4–5 px** with little blur. V5 is yellow with a dark outline plus shadow. The letterforms are a heavy condensed sans with **softened corners**, close to a rounded version of Anton or Bebas; the "W" ends in points.
- **Small white captions (V2, V4, V5):** a soft dark shadow ~3 px down-right, about 40–50% opacity.
- **The first small caption joins the pivot word to the next noun** ("WELL FULHAM", "WELL SORT OF", "WELL THE MOST EXPENSIVE"), so the "Well," never sits on screen alone.
- **When a hook is answered by a focus pull** (V5), the big caption disappears at 5.44 s, the moment the background is fully defocused.

**F. Name-block cascade (V3), corrected order.** It's **a stack that drops in from the top edge, and the bottom line arrives first.**
1. The price ("£92.9m") slides down from above the frame (5.67 → ~5.79 s).
2. The name ("SANDRO / TONALI") slides down from above and **pushes the price down** ~45 px (5.88 → 6.04 s).
3. The club line ("NEWCASTLE – SPURS") drops in last and pushes both down (6.13 s).

Each line moves with a clean exponential ease-out over ~0.45 s, and there's no overshoot: the top line moved 54, 33, 23, 16, 12, 6, 4 then 2 px per update, 9.6–10.1 s. The age tag's number changes in a single frame, **at the same frame as the background colour cut** (8.625 s), and its position doesn't move at all.

**G. A gesture flicker on the photo cutouts.** The V1 Arbeloa cutout switches between two arm states, hand on hip and open palm (its bounding box width goes 427 ↔ 557 px). The switches are instant, with no in-between frames, every ~0.5–1 s (14.29, ~14.9, ~15.9 s). Together with the speed-line boil, that's the only motion in a fully locked 4.5 s shot.

**H. The X wobbles slightly while held.** While the V1 X holds, its bounding box shifts by **±2 px** on twos (78–82 px, 268–272 px). That's probably a deliberate hand-made wobble (it could be compression noise, but it's consistent with the stepped animation). If you replicate it, use a 1–2 px random offset every 2 frames.

**I. Pin landing.** The V1 pin appears at full size, **lifts 6 px, then settles 4 px back down** over 0.25 s (y 270→264→266→268). It's a tiny upward bob, not a drop or a scale pop.

**J. V5 fan jump profile.** It's on ones and takes 0.40 s. **~75% of the distance is covered in the first 0.12 s** (top edge y 1120→982→886→773), followed by a long deceleration (738, 710, 689, 674, 654, 650, 648). There's no overshoot or squash. The speech bubble then grows on an S-curve over ~0.3 s, starting **0.28 s before** the word it illustrates.

**K. Start and end of each video.**
- **The voice-over starts on frame 1** in all five (first word at 0.00 s). There's no music intro, logo sting or silent lead-in.
- The audio **drops to near-silence within 0.2–0.5 s of the last word**: V1 −65 dB at 48.77 s, V2 −46 dB, V4 −31 dB, V5 −35 dB relative to the voice. The videos then end **≤0.7 s after the final word**, with no outro card. That makes them loop cleanly.

### 15.3 Sound design (second look; still limited because I can't listen)

- I couldn't use source separation (the model download was blocked by the network), so I measured every gap between words longer than 0.25 s instead.
- **Music bed:** steady harmonic lines (~0.2–3.5 kHz) run through the gaps at **−15 to −23 dB below the voice**, and it's continuous. In some gaps (for example V3 30.6–31.0 s) it's barely visible at all, so it's either ducked hard or very sparse.
- **Apparent sound effects turned out to be speech.** Every high-frequency burst in a gap matches the narrator's **sibilants**: the two noise bursts at V4 2.5–2.9 s are the "s"/"ts" of "wrists?", and the ones at V4 13.9–14.2 s are "casts". Every loud gap (+1 to +2 dB) shows **speech formants** in the spectrogram, which means the word timestamps were misaligned there (V1 38.6, V3 30.4, V4 37.2, V2 42.6).
- **One unexplained event:** a single broadband click at **V1 20.77 s**, the exact frame the iris finishes closing. It could be a soft impact sound effect or a lip click. I can't tell which.
- **Conclusion:** across ~50 checked gaps I found **no sound effect that I can confirm**. If these videos use whooshes or pops, they're mixed well below the music. The safest way to replicate the mix is: voice-over, a music bed about 20 dB under it, and SFX optional and nearly inaudible.
- **Pauses between sentences:** the gaps I measured are **0.15–0.55 s**, typically 0.2–0.35 s.

### 15.4 Updated replication numbers (they replace the matching values in §5, §12 and §14)

| Parameter | Value |
|---|---|
| Animation step rate | Flat or collage style: **on twos** (12 fps at 24, 15 fps at 30). Cartoon style: **on ones**. Decorative boils (speed lines, line halos) run on ones regardless. |
| Grain | Re-randomise every 2 frames for collage videos (V1, V3); static is fine for flat illustration. |
| UI card / tag pop | 70%→100%, **0.25 s**, expo-out, no overshoot, plus a background blur ramp. |
| Photo-head pop | 0→100%, **0.4–0.5 s**, ease-in-out (or ease-out), no overshoot. Start 0.1–0.2 s before the name. |
| Slam | 112%→100%, **0.33 s**, expo-out, plus glow. |
| Slide in (UI / list) | **0.16–0.45 s** ease-out, no overshoot. |
| Slide out | **0.2–0.36 s** ease-in; the speed keeps rising until it leaves the frame, with motion blur that grows with speed. |
| List swap | Exit (0.2 s) → **0.15–0.2 s empty beat** while the background colour cuts → enter. |
| Character whip / jump | 0.2–0.4 s; cover ~75% of the distance in the first 30% of the time; no overshoot. |
| X draw | Each stroke 0.17–0.25 s, accelerating; stroke 1 lands **~0.2 s after** "not"; stroke 2 lands on the negated noun; 0.25 s between strokes; ±2 px jitter while it holds. |
| Iris chapter break | Vignette ring holds for ~1.3 s → collapse 0.33 s (ease-in) in the sentence pause → black hold 0.3 s → open 0.25 s (ease-out) on the next subject word. |
| Rack focus | ~0.5 s gradual ramp, starting right after the question word. |
| Camera | Locked off by default. Use a camera move only to show story geography (map pans at ~450 px/s, eased) or a slow, even zoom (~1.2%/s) on long data cards. |
| Caption change | On the first word's onset frame (±1 frame); never early; a single-frame swap. |
| End | Cut the music and the picture ≤0.7 s after the last word. |

### 15.5 What I still couldn't pin down
- **Exact easing curves.** At 12 fps there are only 3–6 samples per move. "Expo-out" and "ease-in-out" are the best-fitting labels, not exact Bézier values.
- **Typeface names.** I can describe the letterforms but can't identify the fonts for certain.
- **SFX.** I can't rule out very quiet sound effects. The one candidate (V1 20.77 s) needs a human to listen.
- **V5 caption sync.** Its white sponsor shirts confused the detector, so I didn't measure it. The frames I did check by eye behave like the other four videos.
