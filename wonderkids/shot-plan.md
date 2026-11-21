# Shot Plan: "Top 3 Premier League Wonderkids Who Failed"

**Status: DRAFT v1, built on estimated timings.** The voice-over doesn't exist yet. Every time below comes from the script at the reference speaking rate (~3.0 words/s, 0.3 s pauses). Once the text-to-speech audio is generated, I'll transcribe it with word timestamps and re-snap every event to its real stressed syllable (production system §7). The **order, assets, motion and logic** in this plan are final unless you change them; the **numbers** will shift slightly.

---

## A. Header

| Setting | Value | Why |
|---|---|---|
| Length | **~47 s** (estimated) | 139 words at the reference rate. The script's own timestamps (42 s) assume ~3.4 words/s, faster than the reference. 47 s sits inside the 42–54 s target. |
| Format | 1080×1920, 30 fps container | Production system default |
| Art family | **Flat illustration** (paper-textured flat vector, the V4 look) | Your choice: illustrated. No photos. |
| People | **Generic illustrated footballers**, told apart by kit colour, hair and number, with **no facial likeness** of the real players | Avoids likeness rights. Identity comes from the name blocks and narration, not the faces. |
| Club identity | Plain kit colours plus **text-only** club names. No badges, crests, sponsors or kit-maker marks. | Avoids third-party logos |
| Animation step | **On twos** (15 fps steps). Decorative boils (sparkles, speed lines) on ones. | Flat family rule |
| HOOK captions | White, 2 lines, soft charcoal shadow straight down, centred at 47% | §8.1 |
| BODY captions | **Shadowed white**, 1 line, 2–4 words, centred at 67% | Flat family rule |
| Watermark | **None for this video** (slot L8 left empty) | Your instruction |
| Template | **Ranked list**: three mini-stories (rise → fall), each with a persistent **rank badge** anchor | §1.4. The ranks aren't spoken, so the badge carries them visually. |
| Recurring motif | **The gold star** above each player's head = "future superstar". It appears with the hype and **cracks and falls** at each failure. | One prop carries the whole thesis, and it pays off in the outro. |
| Callback stage | The hook's **three-player line-up** returns in the outro, now with three cracked stars | §5.4 |
| Designed transitions (4) | ① Vertical sheet push (hook → #3) ② Whip push (Everton → City transfer) ③ Shape morph (rising arrow turns into a dive, in the hook) ④ Soft-edge top-down wipe (→ outro). **No big transition**: this script has no tunnel or time-jump idiom that would earn one. | §10 budget: 2–4 designed, ≤1 big |
| Background rotation | teal → royal → grass → charcoal → sky → navy → pink → magenta → grass → royal → charcoal → teal | Never the same colour twice in a row; teal opens and closes (callback) |
| Music | Upbeat instrumental bed, ~20 dB under the voice, starts on frame 1, cut ≤0.5 s after "most?" | §11.3. Needs the HeyGen catalog (same sign-in as the voice-over). |
| SFX | **[EXTENSION]** Quiet, sparse: pops, swishes, marker scratch, soft thud. ~1 per 1.3 s. | Your earlier request (§11.2) |

---

## B. Narration map (estimated `t_kw`, seconds)

| S | Time | Role | Tagged keywords (score) |
|---|---|---|---|
| S1 | 0.0–5.4 | HOOK | three players `NUM/GROUP`(4) · future of football `ABSTR`(3, hook core) · careers `SUBJ` · completely different turn `IDIOM`(4) |
| S2 | 5.7–11.6 | LIST ITEM #3 / SETUP | 17 `NUM`(2) · Federico Macheda `PERSON`(3, must) · Manchester United `PLACE/SUBJ`(2) · hero `ABSTR` · scoring `VERB`(2) · dramatic winner `OBJ`(3) · Aston Villa `CMP`(2) |
| S3 | 11.9–18.3 | #3 / COMPLICATION | unforgettable moment `TIME` · struggled `VERB`(2) · live up to the hype `IDIOM`(3) · **never** became `NEG`(3, must) · superstar `OBJ`(3) |
| S4 | 18.6–22.1 | LIST ITEM #2 / SETUP | Everton `SUBJ`(3) · believed `MIND`(3) · Jack Rodwell `PERSON`(3, must) · England's next great midfielder `ABSTR`(2) |
| S5 | 22.4–27.1 | #2 / COMPLICATION | Manchester City `SUBJ`(3) · signed `VERB`(2) · millions `NUM`(2) · injuries `OBJ/CONSEQ`(3) · inconsistent performances `ABSTR`(2) · derailed `IDIOM`(4) |
| S6 | 27.4–30.8 | #2 / RESOLUTION | brightest prospects `CMP` from→to (3) · forgotten name `VERDICT`(3) |
| S7 | 31.1–36.3 | LIST ITEM #1 / SETUP | Sir Alex Ferguson `PERSON`(3, must) · called `CONSEQ`(2) · Ravel Morrison `PERSON`(3, must) · naturally gifted `ABSTR`(2) |
| S8 | 36.6–41.6 | #1 / COMPLICATION → VERDICT | unbelievable talent `NUM-ish/ABSTR`(2) · off-field problems `CONSEQ`(2) · inconsistency `ABSTR`(1) · **stopped** … potential `NEG/VERDICT`(4) |
| S9 | 41.9–45.2 | PAYOFF | three talents `CALLBACK` · three careers · **never** reached `NEG`(3) |
| S10 | 45.5–46.9 | PAYOFF / CTA | Who disappointed you the most? `MIND`(2) |

---

## C. Event timeline

**Notation.** `t` = planned start (est.) · preset names from production system §6.2 · layer per §6.5 · "→ exit" = the exit rule.

### HOOK: 0.0–5.6 s · background **teal `#3BB5AC` + soft vignette**

| ID | t | Trigger | Event | Motion / timing | Exit | SFX | Purpose |
|---|---|---|---|---|---|---|---|
| H1 | 0.00 | frame 1 | **Stage:** three generic footballers standing side by side on a flat pitch strip, seen from the front (red kit #9, blue kit #8, red kit #7), no faces, simple hair shapes | Already mid-`RISE`: bodies rise from below and settle by 0.45 s (ease-out, staggered 2 steps L→C→R) | Stays until S1 ends | Soft swish −26 dB at 0.10 | Opens in motion; "three players" is on screen as it's said |
| H2 | 1.85 | "future" (1.9) | **A gold star pops above each head**, stagger L→C→R, 0.13 s apart | `POP_HEAD` 0.40 s ease-in-out, no overshoot; then twinkle sparkles (2–4 visible) around the stars | → falls at H4 | Three tiny pops −28 dB | MOTIF intro: "future of football" = superstar |
| H3 | 3.05 | "but" (3.1) | **A thick white arrow draws on** behind the players, rising bottom-left → top-right | `DRAW` 0.25 s, accelerating | → morphs at H4 | Marker scratch −26 dB | Sets up "careers" as an upward trajectory |
| H4 | 4.75 | "different" (4.8) → "turn" (5.2) | **The arrow's head swings down** (pivots ~120°, `MORPH` 0.33 s ease-in-out) into a downward dive. On "turn", **all three stars drop** off the frame (`FALL` 0.5 s, ease-in, ±10° tumble), staggered 2 steps | Morph done by ~5.1; stars gone by 5.6 | Instant cut at 5.7 (end of hook) | Low soft thud −22 dB at 5.2 | IDIOM made literal: "a completely different turn" |

**Hook captions** (HOOK mode, hard swaps): `THESE THREE / PLAYERS` 0.0 · `WERE ONCE / CALLED` 0.8 · `THE FUTURE / OF FOOTBALL…` 1.7 · `BUT THEIR / CAREERS` 3.1 · `TOOK A / COMPLETELY` 3.8 · `DIFFERENT / TURN.` 4.8

### #3 FEDERICO MACHEDA: 5.7–18.4 s

| ID | t | Trigger | Event | Motion / timing | Exit | SFX | Purpose |
|---|---|---|---|---|---|---|---|
| A1 | 5.70 | "At just 17" | **Vertical sheet push**: a **royal `#3550B8`** panel slides up from the bottom over the hook (hard edge + black hairline). **Captions switch HOOK → BODY.** | 0.20 s ease-out (designed transition ①) | — | Airy swish −26 dB | Section break into the list |
| A2 | 5.75 | (with A1) | **Rank badge "#3"** pops top-left (black box, white bold, rotated −8.7°). **Persistent anchor** for the whole item. | `POP_UI` 0.25 s, expo-out | Number swaps to "#2" at B1 | Soft tick −28 dB | Ranks aren't spoken, so the badge carries them |
| A3 | 6.10 | "17" (6.1) | **Age tag "age 17"** pops on the hip of the incoming figure position (black box, white lowercase, −8.7°) | `POP_UI` 0.25 s | Stays through #3 | — | `NUM` → tag |
| A4 | 6.55 | "Federico" (6.6) | **Macheda figure** (generic: red kit #27, dark hair, slim teen build) **rises** from the bottom to centre | `RISE` 0.35 s ease-out, starting ~0.1 s before the name | Stays through A12 | Soft swish −26 dB | `PERSON` must appear |
| A5 | 6.85 | (after A4) | **Name block DROP_STACK**, top-left: line 1 `MAN UTD · 2009` (small caps) / line 2 `FEDERICO` / line 3 `MACHEDA` (heavy geometric sans). The bottom line lands first and pushes the others down. | 3 lines × 0.45 s, staggered 0.2 s, expo-out | Slides out left with the figure at A12 | — | Name and context; club as text only |
| A6 | 8.55 | "hero" (8.9) | **Gold star pops** above his head (callback to the hook motif) + sparkle twinkles | `POP_HEAD` 0.40 s | Cracks at A11 | Bright soft pop −26 dB | "Hero" = the hype begins |
| A7 | 9.35 | "scoring" (9.4) | **Hard cut** to a **grass-green** flat pitch scene: low angle on a goal (white net, simple post lines); the same figure in a side-on shooting pose at left, ball at his foot | Cut on `t_kw`. Scene opens mid-motion: the figure's leg already swinging (`POSE_SWAP` wind-up → strike at 9.6) | — | — (no SFX on cuts) | `VERB` animated: scoring |
| A8 | 9.65 | (strike) | **Ball flies into the top corner**: travels right and up while shrinking 100%→35%; the net **bulges** (2-step pose swap) | 0.35 s ease-out; net bulge 2 steps | Ball stays in the net | Ball thump −24 dB | The action itself |
| A9 | 10.20 | "winner" (10.3) | **Scoreboard card pops** centre-top: `90+3'` / `MAN UTD 3–2 ASTON VILLA` (dark rounded box, light border; no crests). **Background defocuses** under it. | `POP_UI` 0.25 s + `DEFOCUS_BG` 0.18 s on the same frame | Instant cut at A10 | Soft tick −26 dB | `NUM`/score → UI card. "Dramatic" = stoppage time. |
| A10 | 11.85 | "But" (11.9) | **Hard cut** back to **charcoal `#333333`**: the figure standing centre, star above his head, badge and tag in place. The scene is quiet and dim. | Cut. Idle life: the star's twinkle sparkles slowly stop (2→0 by 13.0) | — | — | Tone shift: the high is over. Darker colour = the fall begins. |
| A10a | 12.55 | "unforgettable" (12.7) | **Thought bubble flashback** above him: puffs + cloud containing a miniature of the goal with the **net bulging** (callback to A8) | `BUBBLE` 0.30 s, starting ~0.15 s before the word; the net bulges once inside | Shrinks to a dot on "struggled" (14.0) | Bubble blip −26 dB | Callback; closes the 2.6 s gap |
| A11 | 14.45 | "live up to the hype" (14.5–15.5) | **The star wobbles** (±6° rotation pose swaps, 3 steps), then **sinks**: it slides down ~40 px and dims to 60% | Wobble 0.4 s on twos; sink 0.45 s ease-in | — | — | "Struggled to live up" = the hype sagging |
| A12 | 16.00 | "never" (16.0) | **Red X draws over the star**: stroke 1 starts 0.2 s after "never"; stroke 2 lands on "superstar" (17.0) | `DRAW` 0.2 s per stroke, 0.25 s gap, ±2 px jitter while held | Removed when the star falls | Marker scratch per stroke −24 dB | `NEG` (must): never became the superstar |
| A13 | 17.40 | "everyone expected" (17.4) | **The cracked star falls** off the bottom of the frame (`FALL` 0.5 s ease-in, tumbling), the X going with it; the figure's **pose swaps to slumped** (head down) | Star leaves by 17.9 | Slump holds to the list swap | Soft thud −22 dB on exit | Verdict for #3: the star is gone |

**Captions:** `AT JUST 17,` 5.7 · `FEDERICO MACHEDA` 6.6 · `BECAME A` 7.5 · `MANCHESTER UNITED HERO,` 8.1 · `SCORING A DRAMATIC` 9.4 · `WINNER AGAINST` 10.3 · `ASTON VILLA.` 11.0 · `BUT AFTER THAT` 11.9 · `UNFORGETTABLE MOMENT,` 12.7 · `HE STRUGGLED` 13.8 · `TO LIVE UP` 14.3 · `TO THE HYPE` 15.1 · `AND NEVER BECAME` 15.8 · `THE SUPERSTAR` 16.8 · `EVERYONE EXPECTED.` 17.4

### #2 JACK RODWELL: 18.4–31.0 s

| ID | t | Trigger | Event | Motion / timing | Exit | SFX | Purpose |
|---|---|---|---|---|---|---|---|
| B1 | 18.20 | (sentence end) | **List swap, step 1**: the slumped Macheda + name block `SLIDE_OUT` left | 0.25 s ease-in with motion blur | — | Swish −26 dB | §10 list-swap rule |
| B2 | 18.45 | (beat) | **Empty beat** with only the rank badge. **Background cuts to sky `#6EB8F5→#5A86E0`**; the **badge number swaps "#3" → "#2"** on the same frame | 0.15 s beat | — | Tick −28 dB | Anchor continuity |
| B3 | 18.60 | "Everton" (18.6) | **Rodwell figure** (generic: royal-blue kit #26, tall, short hair) `SLIDE_IN` from the right; **name block** DROP_STACK: `EVERTON · 2008` / `JACK` / `RODWELL` | Figure 0.35 s ease-out; name block cascade starts at the name (19.7) | Figure stays to B6 | Swish −26 dB | `SUBJ` on its noun; `PERSON` must |
| B4 | 19.15 | "believed" (19.3) | **Thought bubble** (above the figure's head, representing the club's hope): 3 puffs pop up in sequence, then a cloud grows. Inside: **the same figure in a plain white kit with a gold star** (England hope, no crest). | `BUBBLE`: puffs 2-step stagger, cloud 0.30 s S-curve, timed ~0.3 s before "England's" (20.9) completes | Instant cut at B5 | Bubble blip −26 dB | `MIND` → thought bubble with a miniature of the hope |
| B5 | 21.30 | "great midfielder" | **The star in the bubble twinkles** (sparkle burst, 4 dashes) | 0.3 s | Bubble cut at B6 | — | Idle life on the hold |
| B6 | 22.30 | "Manchester City" (22.4) | **Whip push** (designed transition ②): the Everton scene whips out left (ease-in 0.3 s, blur growing); a **navy `#2E3388`** scene whips in from the right with **the same figure now in a sky-blue kit**. Badge "#2" holds still. | Out 0.30 s ease-in + in 0.16 s ease-out, 1-frame overlap | — | Swish −24 dB (at the fastest point) | A transfer is a move: the whip literally moves him |
| B7 | 23.05 | "signed" (23.1) | **Name block updates**: context line swaps to `EVERTON → MAN CITY · 2012`. **Money tag "£ MILLIONS"** (white box, black text, −8.7°) pops on his shoulder on "millions" (23.9) | Line swap instant; tag `POP_UI` 0.25 s | Tag stays to B9 | Tick −28 dB | `NUM` → tag. The script says "millions", so no unverified figure. |
| B8 | 24.55 | "injuries" (24.6) | **Pose swap → limping** (one knee bent, hand on thigh) + a **red medical cross icon** pops on the knee + a white ice pack **drops in** onto the knee | Pose instant; icon `POP_HEAD` 0.4 s; ice pack `FALL` 0.5 s landing just before "and" (25.0) | Icon and pack stay to B10 | Pop −26 dB | `CONSEQ`: injuries made visible |
| B9 | 25.15 | "inconsistent performances" (25.2–25.7) | **A white line chart draws on** to the right of the figure: axis first, then a **jagged up-down line** left to right | Axis `DRAW` 0.2 s → line `DRAW` 0.45 s (linear zig-zag) | → B10 | Marker scratch −26 dB | "Inconsistent" = the zig-zag |
| B10 | 26.15 | "derailed" (26.2) | **The line literally derails**: its last segment snaps off at the end and tumbles down off the chart (`FALL` 0.5 s, rotating); a small red X pops where it broke | Snap on "derailed", fall done by ~26.7 | Chart cut at B11 | Soft crack/thud −22 dB | IDIOM made literal |
| B11 | 27.40 | "He went from" | **Hard cut** to **pink `#E0305E`**: the figure centre in sky-blue kit; a **large gold star above him glows** (white glow) | Cut; star `SLAM` 112→100% 0.33 s on "brightest" (29.0), timed −0.07 s | — | Soft shimmer −24 dB | "Brightest prospects" = peak glow |
| B12 | 29.75 | "forgotten" (30.1) | **The spotlight goes out**: instant **background cut pink → charcoal**; the star loses its glow and **falls** (`FALL` 0.5 s); the **name block dims to 30%** (the "forgotten name") and the figure desaturates to gray | All on the "forgotten" frame; star fall lands ~30.5 ("name") | Holds until the list swap | Soft thud −22 dB | VERDICT for #2: literally forgotten |

**Captions:** `EVERTON ONCE BELIEVED` 18.6 · `JACK RODWELL` 19.7 · `COULD BECOME` 20.3 · `ENGLAND'S NEXT` 20.9 · `GREAT MIDFIELDER.` 21.4 · `MANCHESTER CITY` 22.4 · `SIGNED HIM` 23.1 · `FOR MILLIONS,` 23.6 · `BUT INJURIES` 24.4 · `AND INCONSISTENT` 25.0 · `PERFORMANCES` 25.7 · `DERAILED HIS CAREER.` 26.2 · `HE WENT FROM` 27.4 · `ONE OF ENGLAND'S` 28.1 · `BRIGHTEST PROSPECTS` 29.0 · `TO A FORGOTTEN NAME.` 29.6

### #1 RAVEL MORRISON: 31.0–41.8 s

| ID | t | Trigger | Event | Motion / timing | Exit | SFX | Purpose |
|---|---|---|---|---|---|---|---|
| C1 | 30.85 | (sentence end) | **List swap**: grayed Rodwell `SLIDE_OUT` left → 0.15 s beat → background cuts to **magenta `#C44BD8→#7A2FA0`**, badge "#2" → **"#1"** | Exit 0.25 s ease-in; beat 0.15 s | — | Swish −26 dB, tick −28 dB | Anchor continuity |
| C2 | 31.25 | "Ferguson" (31.6) | **Manager figure** (generic older man: dark long coat, grey hair, arms folded, no likeness) `RISE` at **left of centre**; small name label `SIR ALEX FERGUSON` above (white, small caps), no tag | `RISE` 0.35 s, starting ~0.3 s before the surname so it lands on it | Stays to C6 | Swish −26 dB | `PERSON` must appear (generic, labelled) |
| C3 | 32.55 | "called" (32.5) | **Speech bubble** from the manager, top-right: hand-lettered all caps `"ONE OF THE MOST GIFTED I'VE SEEN"` | `BUBBLE` 0.30 s S-curve, starting ~0.25 s before "called" completes | Instant cut at C6 | Bubble blip −26 dB | `CONSEQ` → a speech bubble. The script says "reportedly", so the line is paraphrased in quote marks. |
| C4 | 33.05 | "Ravel" (32.8) / "Morrison" (33.2) | **Morrison figure** (generic: red kit #49, slim, short dark hair) `SLIDE_IN` from the right to right of centre, slightly in front of the manager (overlapping, pair composition); **name block** DROP_STACK top-left: `MAN UTD · 2010` / `RAVEL` / `MORRISON` | Figure 0.35 s ease-out starting −0.15 s; name block cascade from 33.2 | Stays to C6 | Swish −26 dB | `PERSON` must; the pair = mentor + talent |
| C5 | 34.50 | "naturally gifted" (34.5–35.0) | **Gold star SLAMS** above Morrison with a white glow; a **radial sparkle burst** (8 white dashes) around him | `SLAM` 0.33 s at −0.07 s from "gifted"; burst 0.4 s | Star stays to C9 | Shimmer −24 dB | Peak hype; MOTIF |
| C6 | 36.55 | "He had" (36.6) | **Hard cut** to **grass `#4CEB72`**: Morrison alone, left of centre, star above. To his right, a **vertical "TALENT" bar** (white outline) and a **dashed line near the top labelled `POTENTIAL`** draw on | Axis/outline `DRAW` 0.2 s; dashed line `DRAW` 0.25 s | — | Marker scratch −26 dB | Sets up the gauge. Visual: talent vs potential. |
| C7 | 37.10 | "unbelievable talent" (37.1–37.7) | **The bar fills gold** quickly up toward the POTENTIAL line (`GROW_BAR`, ease-out 0.45 s), stopping at ~85% | Lands on "talent" | — | Rising soft whoosh −28 dB | "Unbelievable talent" = a nearly full bar |
| C8 | 38.30 | "off-field problems" (38.4–38.7) | **A small grey storm cloud pops** above his head beside the star; then **warning icons** (two small ⚠ triangles in red/white) pop beside the figure on "problems" | Cloud `POP_HEAD` 0.4 s; icons `POP_UI` 0.25 s, staggered 2 steps | Stay to C10 | Pop −26 dB | `CONSEQ` made visible without depicting specifics |
| C9 | 39.25 | "inconsistency" (39.3) | **The gold bar flickers**: its height swaps instantly 85→55→75→40% in 4 steps (0.15 s each) | `COUNT`-style instant swaps | — | 4 soft clicks −30 dB | "Inconsistency" = an unstable level |
| C10 | 39.80 | "stopped" (39.8) | **A red barrier bar SLAMS** across the gauge just below the POTENTIAL line; then the gold bar **shoots up and hits the barrier**, stopping short (40.6–40.9). On "potential" (41.2), **red X draws** over the dashed POTENTIAL label; the **star cracks and falls** | Barrier `SLAM` 0.33 s; bar `GROW_BAR` 0.3 s; X `DRAW` 2×0.2 s, the 2nd stroke landing on "potential"; star `FALL` 0.5 s | Holds to the outro wipe | Thud −22 dB on the barrier; scratch on the X | NEG + VERDICT for #1 |

**Captions:** `SIR ALEX FERGUSON` 31.1 · `REPORTEDLY CALLED` 32.0 · `RAVEL MORRISON` 32.8 · `ONE OF THE MOST` 33.6 · `NATURALLY GIFTED` 34.5 · `PLAYERS HE'D EVER SEEN.` 35.4 · `HE HAD` 36.6 · `UNBELIEVABLE TALENT,` 37.1 · `BUT OFF-FIELD PROBLEMS` 38.2 · `AND INCONSISTENCY` 39.0 · `STOPPED HIM FROM` 39.8 · `REACHING HIS POTENTIAL.` 40.6

### OUTRO / PAYOFF: 41.9–47.4 s · background **teal** (callback to the hook)

| ID | t | Trigger | Event | Motion / timing | Exit | SFX | Purpose |
|---|---|---|---|---|---|---|---|
| D1 | 41.85 | "Three" (41.9) | **Soft-edge top-down wipe** (designed transition ④) reveals the **hook stage again**: the same three figures in a row on teal with vignette, now **in their final kits** (red #27, sky-blue #26, red #49), with **rank badges 3 · 2 · 1** on their hips. The **rank badge anchor at top-left exits** with the wipe. | Feathered wipe 0.20 s | — | Soft swish −26 dB | CALLBACK to the opening image |
| D2 | 42.10 | "unbelievable talents" (42.1–42.7) | **Three gold stars pop above them** again, stagger L→C→R (the hook's H2, replayed) | `POP_HEAD` 0.4 s, 0.13 s stagger | → cracked at D3 | Three tiny pops −28 dB | Restates the promise |
| D3 | 43.85 | "never" (43.9) | **All three stars crack** (crack-line pose swap) and on "reached" (44.2) **fall together**; the three figures **swap to slumped poses** on "potential" (44.8) | Crack instant; `FALL` 0.5 s; slump instant | Stars gone by ~44.8 | One soft thud −22 dB | NEG + VERDICT for all three: the thesis in one image |
| D4 | 45.45 | "Who" (45.5) | **Large white question marks pop** around and above the three figures (3 sizes, staggered 0.13 s), and the figures' badges **pulse** once (100→108→100%, the one deliberate "invite" pulse) | `POP_HEAD` 0.4 s each; badge pulse 0.3 s | Hold to the end | Three soft pops −28 dB | Call to action: invites the comment answer |
| D5 | 47.20 | ≤0.5 s after "most?" (46.7) | **End**: picture and music cut. No outro card, no logo. | — | — | Music cut | Clean loop (§9) |

**Captions:** `THREE UNBELIEVABLE TALENTS…` 41.9 · `THREE CAREERS` 43.2 · `THAT NEVER REACHED` 43.7 · `THEIR POTENTIAL.` 44.6 · `WHO DISAPPOINTED YOU` 45.5 · `THE MOST?` 46.4 (holds to the last frame)

---

## D. Asset list (everything drawn by me as flat SVG; nothing sourced)

| ID | Asset | Treatment | Used in |
|---|---|---|---|
| P-base | **Generic footballer figure rig**: head (no facial features), hair shape, torso/kit, shorts, socks, boots; poses: stand, celebrate, shoot (wind-up/strike), limp, slump | Flat fills, light paper grain, soft 1-colour shading | All players |
| P-macheda | Rig + red kit #27, dark short hair | — | H1, A4–A13, D1 |
| P-rodwell | Rig + royal-blue kit #26 → sky-blue kit #26; tall build | — | H1, B3–B12, D1 |
| P-morrison | Rig + red kit #49, slim, short dark hair | — | H1, C4–C10, D1 |
| M-manager | Generic older man, long dark coat, grey hair, arms folded | — | C2–C5 |
| star | Gold 5-point star, with cracked variant + glow | Flat gold, white glow for SLAM | Motif everywhere |
| arrow | Thick white rising arrow (morphs into a dive) | Flat white | H3–H4 |
| pitch / goal | Flat grass strip; goal with net lines (2 bulge states) | Flat | H1, A7–A8, D1 |
| ball | Flat white ball with simple panels | Flat | A7–A8 |
| scoreboard | Dark rounded card, light border: `90+3'` / `MAN UTD 3–2 ASTON VILLA` | UI | A9 |
| tags | Rank badges (#3/#2/#1), `age 17`, `£ MILLIONS` | Black or white box, −8.7° | A2, A3, B7, D1 |
| name blocks | 3 × context line + 2-line name | Heavy geometric sans | A5, B3, B7, C4 |
| bubbles | Thought bubble (puffs + cloud); speech bubble | White fill, dark outline | B4, C3 |
| icons | Medical cross, ice pack, storm cloud, ⚠ warning, question marks | Flat | B8, C8, D4 |
| chart | Line chart (axis + zig-zag + broken end) | White strokes | B9–B10 |
| gauge | Vertical talent bar, dashed POTENTIAL line, red barrier | White outline / gold fill / red | C6–C10 |
| marks | Red X (2 strokes), sparkle twinkles, radial burst | `accent.red` / white | A12, B10, C10, C5, H2 |
| texture | Paper grain overlay 6% (static for flat, per the reference) + teal vignette | — | Global |

---

## E. Audits on the draft (will be re-run on the real VO timings)

| Check | Result |
|---|---|
| Scene length | 0.8–5.8 s (A1 hook→#3 sheet; longest hold: A10–A13 at 6.5 s, with 3 events inside) ✓ |
| Event spacing | The first draft had a 2.6 s gap (A10 → A11). Fixed by **A10a** (a flashback bubble on "unforgettable"). The longest gap is now **~1.6 s** (A10a exit 14.0 → star wobble 14.45 is covered by the bubble's exit; B5 → B6 ≈ 1.0 s) ✓ |
| Elements per frame | Max = hero + 3 (C8: star, cloud, warning icons, + badge/name block dimmed) ✓ |
| "Must" visuals | 4 PERSON ✓ · 3 NEG (A12, C10, D3) ✓ · VERDICTs A13, B12, C10, D3 ✓ |
| Transitions | 4 designed (sheet push, whip push, arrow morph, soft wipe), 0 big, 0 dissolves ✓ |
| Jokes / puns | 3 literal idioms (different turn, derailed, forgotten name) ✓ (≤3) |
| Captions | 49 chunks, 2–4 words each, one line; HOOK → BODY at "At just 17" ✓ |
| SFX | ~34 events over 47 s ≈ 1 per 1.4 s; none on hard cuts or caption swaps ✓ |
| Rights | No logos, crests, sponsors, photos or facial likenesses; club names in text only ✓ |
| Facts to confirm | Macheda's winner: 5 Apr 2009, Man Utd 3–2 Aston Villa, stoppage time. Rodwell moved Everton → Man City in 2012. Morrison's Man Utd debut season ~2010. **Please confirm the years and score on the cards, or I'll drop them to text-free versions.** |

---

## F. What happens next

1. **Voice-over**: generate it with HeyGen text-to-speech (needs the sign-in, see chat), then transcribe it with word timestamps.
2. **Re-time**: snap every `t` in this plan to the real `t_kw`; regenerate the caption track from the real words; re-run the audits; write `shot-plan.json`.
3. **Build** in HyperFrames: SVG rig and assets → scenes → motion presets on twos → captions → audio mix.
4. **Measured QA** (production system §15), then hand over the video.
