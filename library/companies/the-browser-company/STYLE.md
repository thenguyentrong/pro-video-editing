# The Browser Company (Arc, Arc Search, Dia) — launch style

Three official films measured at 480p (analyze_video.py, cuts checked by eye on cut sheets and 1-12 fps strips, EBU loudness, speech spans from a speech detector; nothing transcribed). Sizes are % of frame height (H).

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice |
|---|---|---|---|---|---|---|---|
| [Dia: Never Explain Yourself Again (2025)](dia-never-explain-yourself/notes.md) | 77.8 s | 50 | 1.56 / 1.25 | 1.50 · 0.97 · 1.77 · 2.16 | 34 % / 6 % | −17.8 | actors' dialogue 0-40 s, then none |
| [Arc Search "SF Party" CBS spot (2024)](arc-search-cbs-sf-party/notes.md) | 63.7 s | 29 | 2.20 / 1.54 | 2.65 · 1.22 · 1.99 · 3.18 | 34 % / 21 % | −15.0 | actors' dialogue 7-31 s, then none |
| [Meet Act II of Arc Browser (2024)](arc-act-ii-launch/notes.md) | 860.4 s | 242 | 3.56 / 2.38 | 4.22 · 3.12 · 3.65 · 3.26 | 18 % / 39 % | −17.3 | CEO + team, 77 % of runtime |

## The core idea
The Browser Company sells software like a film studio would: every launch is a short film with a cast, a location, a genre and a grade, and the product UI is filmed on real screens inside that world. There are two modes. **Ads** (Dia, Arc Search) are comedy shorts: a relatable pain played as a gag by actors, the product arrives at ≈50 % as relief, the cutting slows down once it does, and the voices stop. **Founder launches** (Act II) are documentary episodes: the CEO on black talks to camera with real pauses, then chapters with a blue title card each, observational demos with real people at a table, archive and a skit for the "why", and a summary with status lower thirds. The type system is always a pair: a loud wide grotesque (or neutral sans) for the claim, a classic serif for small, warm lines.

## Rules with numbers
1. **Problem first, product at ≈50 %.** Dia: product appears at 52 %, Arc Search at 48 %. Act II: no feature is named before 14 %.
2. **Fast in the pain, calm in the answer.** Dia's struggle runs 0.4-1.3 s per shot, the solution 1.5-3 s; Arc Search's flashback 0.42-0.6 s, then a single 9.4 s phone take.
3. **Voices stop when the product starts.** Speech ends at 40.1 s (Dia, product at 40.5 s) and 30.5 s (Arc Search, demo at 30.6 s); the rest is music, UI and cards.
4. **Film the screen.** The UI is shot on a real laptop or phone: tilted 6-15°, shallow focus, graded to the scene (mint vs warm beige in Dia). Clean captures appear only for detail.
5. **One turn beat with a drop-out.** 0.7 s (Dia, 37.6 s) and 0.9 s (Arc Search, 28.2 s) audio drop-outs mark the moment the character decides; the biggest rise follows (+31 dB in Arc Search).
6. **Text is rare and plain.** Ads: 4-6 text moments, 3-6 words each, white on black or over picture, hold 1.5-2.7 s, hard cuts. Act II: 4 chapter cards (≈4 s each) + serif captions + 4 status lower thirds in 14 min.
7. **Genre pastiche as the hook:** TV-movie supers and corner bugs, a horror flashback with white/cyan flashes (Arc Search), a sitcom kitchen (Dia), a film-poster title and a black-void interview (Act II).
8. **Endings:** product logo over the last food/picture shot, fade to black, logo on black, URL card 2.4 s (Dia); one line + app icon + store badge (Arc Search); logo mark then URL on black, ≈7 s total (Act II).
9. **Mix:** −15 to −18 LUFS integrated, not loud; the founder film has no music under the 36 s cold open (20 silences of 0.35-2 s).

## Type
- Statements: neutral grotesque, sentence case (Dia; free: Inter 400), cap ≈6 % H on black; or a rounded bold geometric with a full stop (Arc Search; free: Plus Jakarta Sans 700), cap ≈4.6 % H over picture.
- Chapter cards (Act II): royal blue #0f3ff7, cream #f3f0dc, heavy wide caps (free: Archivo ExtraBold Expanded / Unbounded 800) at ≈19 % H per line, serif subline (free: Sorts Mill Goudy / EB Garamond) ≈4 % H; built word by word in ≈0.35 s steps.
- Serif lower thirds and captions: cap 2-4 % H, centred, "Feature — Status".
- Parody supers: heavy extended caps with a blue outline, ≈4.8 % H, bottom-centre, plus small corner bugs.

## Recipe (ad, 60-80 s)
1. Write a 3-act gag: daily scene (15 %) → the pain played out with a growing obstacle (30 %) → turn with a 0.7-0.9 s silence (4 %) → product as relief in 1-2 long takes (20 %) → 2-3 black or over-picture claim cards (8 %) → warm payoff (10 %) → logo + URL (7 %).
2. Cast real-looking people in a real home or park; warm film grade with grain, one colour world per act (sunny vs teal night).
3. Shoot the screen with the camera; in HTML, tilt and tint the UI (`perspective(1200px) rotateX(8deg) rotateZ(-6deg)`, `sepia(.15)` + `hue-rotate`), slow push 1.6 → 1.7.
4. Cards: `#000`, `400 72px Inter` white, hard set in/out, hold 1.6-2 s; title over picture built word by word every 0.8 s.
5. Mix: dialogue only in the problem half, music carries the second half, master −15 to −18 LUFS.

## Recipe (founder launch, 10-15 min)
Founder on black for the cold open (no music, real pauses) → blue poster title → chapters (card → observational demo at a real table → filmed and clean screen inserts → reactions) → one archive/skit interlude for the "why" → summary with status lower thirds → logo + URL. See arc-act-ii-launch/notes.md for card values.
