# FORMULA 1 – video style

Examples studied (Oct 2026):

| Example | Type | Content length | Shots | ASL | Median | Integrated / LRA |
|---|---|---|---|---|---|---|
| [f1-2026-opening-titles](f1-2026-opening-titles/notes.md) | broadcast opening titles (driver roll-call) | 57.0 s | 43 | 1.33 s | 1.00 s | −14.1 LUFS / 3.4 LU |
| [f1-2026-season-launch](f1-2026-season-launch/notes.md) | :60 season campaign spot | 60.0 s | 72 | 0.83 s | 0.70 s | −16.2 LUFS / 2.0 LU |
| [drive-to-survive-s7-trailer](drive-to-survive-s7-trailer/notes.md) | Netflix docu-series trailer | 96.8 s | 97 | 1.00 s | 0.84 s | −15.2 LUFS / 6.7 LU |

## The look in one paragraph
F1 cuts fast and flat: ASL 0.8–1.3 s, almost no shots over 3 s, and the rhythm does not slow down for an intro or speed up for a climax; the only long shot is the logo at the end. Speed is made readable by a template (one person = portrait + name card, or one person = one spoken fragment). People are the product: faces to camera fill a large share of the shots, cars appear as CG renders, macro details or onboard plates. Graphics use one colour, F1 red (#E10600), on carbon black (#15151E), pure black or light grey; team colours come only from suits and cars. Type has three voices: wide extra-bold caps (names), widely tracked techno mono (data, endlines), and a fast script (first names). Sound is a compressed wall (LRA 2–3.4 LU on F1's own pieces) with one hit at the start and the loudest moment on the logo.

## Sub-styles
1. **Broadcast titles / roll-call** (opening titles). Studio portraits on 3 rotating sets (red studio, grey cyc, black), 22 people × ~2.2 s, each with a kinetic name card (script first name + wide surname + giant cropped surname behind + corner numbers). Transitions: hard cuts, motion-blur smears, giant-glyph wipes. Ends: light streaks collapse into the logo, 6 s hold, 3 s silence for the broadcast handover.
2. **Campaign spot / relay dialogue** (season launch). One sentence split across a host and ~15 drivers, each 0.5–1.8 s to camera, intercut with 0.3–0.6 s texture shots (macro eye, sparks, crowd, CG car). Hardly any type: one tracked-mono endline ("IT'S ALL TO DRIVE FOR") and a red-on-black logo card with legal lines.
3. **Docu-series trailer** (Drive to Survive, Netflix-framed). Confessional interviews on dark grey anchor every 15–20 s block of race chaos; three word-built text cards carry one sentence across the trailer; title lockup over a top-down pit-stop plate with a wipe + glitch; a comic button after the title; Netflix date card and ident. Here the brand frame is Netflix's, F1 lives inside the footage.

## Rules (most important first)
1. **Flat fast rhythm, held by a template.** ASL 0.8–1.3 s, median 0.7–1.0 s, 50–75 % of shots under 1 s, 8–14 cuts per 10 s in every 10 s window. Never cut randomly: every shot belongs to a unit (person card, spoken fragment, block ending on an interview).
2. **Red is the only graphic colour.** #E10600 on #15151E / #000 / light grey #cdcbce. No gradients of other hues in the graphics.
3. **Three type voices with fixed jobs.** Names = wide extra-bold caps at 8.5–9.5 % of frame height; data/endlines = tracked mono caps at 2–5 % with ~0.4–1 em spacing; personality = script first name at ~10 %. Plus one giant cropped word (40–75 % of frame height) as background texture.
4. **Faces first.** People to camera are the core shot; cars appear as details (macro, CG render, onboard) between people.
5. **Speed transitions only.** Hard cuts, motion-blur smears (~0.15–0.25 s), whip pans, giant-glyph wipes, light-streak morphs. No dissolves.
6. **The logo is the payoff.** Longest shot, loudest moment (−9 LUFS momentary on the titles), plain card: red F1 logo ~37 % of frame width, centred, on carbon black or black.
7. **Compressed audio wall.** −14 to −16 LUFS integrated, LRA 2–3.4 LU; one hit at the start, peak on the logo, then decay/silence. Cuts follow the grid of the edit, not every beat (only 15–28 % of cuts sit on an onset, near chance).
8. **No explaining supers.** No lower thirds in promos; names appear only as designed title cards. Recognition is assumed.

## Recipe: an F1-style roll-call / launch in Hyperframes (real footage + HTML/GSAP)
- Footage: per person 2 clips (tight portrait slow push-in, full body holding helmet) shot on grey paper or black with a red edge light; plus 6–10 texture inserts (macro eye, sparks, wheel, visor, crowd), 0.3–0.6 s each. Grade: deep blacks, natural skin, red only from light.
- Canvas 1920×1080, background tokens: --f1-red #E10600, --carbon #15151E, --grey #CDCBCE, --white #FFFFFF.
- Name card: `.surname` Archivo 900 (or Archivo Expanded), uppercase, font-size 128 px (cap ≈ 96 px = 9 %), letter-spacing −0.01em; `.first` script (Mrs Saint Delafield / Allison) 120 px, rotate(−8deg), overlapping the surname by 20 px; `.giant` same family, 640 px, -webkit-text-stroke 2px rgba(255,255,255,.18), color transparent, cropped by the frame; `.num` / `.team` Space Mono 700, 22 px / 18 px, letter-spacing 0.4em, in 3–4 corners.
- Timeline per person (2.2 s): portrait 0–1.0 s; cut to full body; surname x +120 → 0 with blur 18 → 0 px, 0.25 s, "power4.out"; red copy clip-path wipe 0.35 s; script stroke-dashoffset write-on 0.4 s; giant word x drifts −6 % over the whole unit (ease "none"); exit = smear (scaleX 1 → 1.4, blur 0 → 30 px, 0.15 s) or glyph wipe (0.2 s, "expo.inOut").
- Launch-spot variant: drop the name cards; cut each spoken fragment to the word (0.5–1.0 s); endline in Space Mono 700, 54 px, letter-spacing 0.95em, white, hard on, 0.8 s.
- End: red light streaks (3–5 divs, height 6 px, blur 12 px, x sweep 0.6 s) collapse into the logo (scale 1.6 → 1, 0.8 s, "power3.out"), logo 37 % width on --carbon, hold 4–6 s. Music: compressed bed, first hit at ~1.5 s, biggest hit on the logo, then 2–3 s decay.
- Sonic branding: F1's theme (Brian Tyler, since 2018) is the broadcast sonic identity; use a licensed driving orchestral-electronic bed of similar character and make the logo the loudest moment (I did not listen to these files, so the theme attribution for the titles is an inference).
