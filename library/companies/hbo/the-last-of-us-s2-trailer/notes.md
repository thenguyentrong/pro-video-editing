# The Last of Us Season 2 – Official Trailer  (HBO, uploaded 2025-03-08, 125.0 s file = 104.8 s trailer + 5.3 s title card + 4 s Max card + 11 s YouTube end screen, 16:9, YouTube / HBO Max channel)
URL: https://www.youtube.com/watch?v=_zHPsmXCjB0
Purpose: series trailer (season launch)
One-sentence point: the quiet world of Season 1 is gone; every path now costs something.

Structure (three-act trailer with two black "breaths"):
- 0–24 COLD OPEN, slow: boots in the dark, a cracked wristwatch in macro (7.6 s), a grave cross with a pendant (10 s), Ellie close-up in a green forest (13.6 s), Ellie tiny in a clearing (19 s). 7 shots in 24 s (ASL 3.4 s). Low level (−17 to −28 LUFS).
- 24.0–29.9 CARD 1: "THE ACCLAIMED / HBO ORIGINAL SERIES / RETURNS" on black, hit on the card (24.05 s, +15.5 dB), then a ~1 s cross-dissolve (26.5–27.5) into an aerial of the snowy town.
- 30–50 ACT 2, the world: map and hand, MILLER mailbox, guitar scene, warm dance hall with string lights (35–38 s), then threat: armoured vehicle and soldier with the WLF mark (43–45 s), group in snow, infected horde in a blizzard (48 s). Shots 1.3–1.7 s. Music builds −20 → −14 LUFS.
- 50.3–52.7 BLACK HOLD 2.5 s with an audio drop-out (to −42 dBFS), then re-entry hit at 52.75 s (+17.8 dB) on the horde at the wall and explosions (53 s).
- 57.0–58.6 BLACK HOLD 1.6 s + drop-out, re-entry hit at 58.6 s (+18.6 dB, the loudest single onset) on an empty overgrown road.
- 58.6–98 ACT 3, acceleration: new antagonists, corridors, a kiss, Ellie's tattoo, red-flare fights; cuts every ~1.1 s (8–9 cuts per 10 s from 70 to 100 s). Tagline split into two punch cards: "EVERY PATH" (92.2–93.0 s) and "HAS A PRICE" (94.9–95.6 s), each held only ~0.75 s between 0.5–0.7 s action shots. Loudest section 94–98 s (−11 LUFS).
- 98.0–104.8 FACE-OFF: Joel and Ellie confrontation (3.3 s two-shot, Ellie close-up shouting, Joel turning). Audio drops 5.5 s to −35/−46 (dialogue only, my reading of the levels).
- 104.8–110 TITLE CARD: THE LAST OF US in dark letters over a deep red glow from a road flare at bottom, "HBO ORIGINAL" above, "NOW STREAMING" below; slam hit at 104.95 s (+23.5 dB).
- 110–114 Max card on the same red glow ("max", "PLANS START AT $9.99/MONTH").

Cut rhythm: 63 shots in 114 s, ASL 1.81 s, median 1.38 s. ASL per quarter 3.17 / 1.50 / 1.36 / 1.68 s (the cold open is 2× slower than the rest). 13 % of shots under 1 s, 13 % over 3 s. Shortest 0.54 s (96.3 s). Densest window 90–100 s (9 cuts). Cuts on audio onsets 21 % vs 19 % by chance = cut to picture and dialogue, not to the beat.

Typography:
- Cards: the show's heavy condensed grotesque, all caps, eroded/rough edges, white-to-grey vertical gradient, centred, on pure black. Closest free match: Oswald 700 or Anton with a grunge mask. Cap height 12.5 % of frame height for the main lines (measured at 92.5 and 95.2 s), the "THE ACCLAIMED" line about half that.
- One idea per card, 2–3 words, hold 0.7 s (tagline) to 3 s (returns card). No motion except a fade/dissolve.
- End card: same condensed title stacked in 3 lines (dark letters ~40 % of frame height) lit from behind by red; "NOW STREAMING" in a wide, widely-tracked geometric sans (~0.3 em tracking), red on dark red.

Colour/grade: naturalistic, low-key. Three worlds by colour: green forest (cold open), warm amber interiors/string lights (Jackson), steel-blue snow (horde), then red flare light in the night fights (84–91 s) which becomes the red end card. 21 % of frames mostly dark. No letterbox in this upload.

Camera/shots: live action; macro inserts (watch, pendant, tattoo), close-ups of faces, aerials and wide crowd/VFX shots. Mostly steady, slow push-ins in the cold open; handheld in the action.

Transitions: hard cuts almost everywhere; one ~1 s cross-dissolve from card 1 into the town aerial; two black holds (2.5 s and 1.6 s) used as "breaths" before re-entry hits; title arrives by hard cut on the slam.

Sound: score-driven trailer with dialogue (the 99–104 s drop reads like spoken lines; I did not listen). Integrated −18.4 LUFS, LRA 12.7 LU (big dynamics), true peak −1.2 dBFS. Big events: hits at 24.05 (card), 52.75 and 58.6 (re-entries after black), 104.95 (title slam). Three drop-outs (51.5, 57.5, 99–104.5 s), each followed by a +16 to +33 dB rise.

What makes it premium:
- Patience first: 24 s of slow, quiet images before any text or music push.
- Black holds + drop-outs as punctuation, each followed by a hard re-entry hit.
- Tagline split over two tiny cards between the fastest shots, so the message lands inside the climax.
- Colour story that ends in the red of the end card (flare red = brand red for this season).
- The show's own condensed title face is reused for all cards = one typographic voice.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Edit plan for ~105 s: 0–24 s slow open (6–7 shots, 3–4 s each, macro detail + lonely wide), card 1 at 24 s, act 2 30–50 s (shots 1.3–1.7 s), black hold 2.5 s, re-entry, black hold 1.5 s, re-entry, act 3 at 1.0–1.2 s per shot, two 0.75 s tagline cards, 6 s dialogue face-off with the music pulled to −35 LUFS, title slam.
- Cards: black #000, text Oswald 700 uppercase, 135 px on 1080p (12.5 %), fill linear-gradient(#ffffff, #9a9a9a), mask with a rough-edge noise texture; GSAP opacity 0 → 1 in 0.15 s, hold, out 0.15 s (tagline) or 0.4 s (opening card).
- Black hold: 1.5–2.5 s of #000 with audio ducked −25 dB, then the next cut on a +18 dB hit.
- End card: background radial-gradient(circle at 50% 95%, #ff2a1a 0%, #8a0b0b 25%, #1a0303 70%); stacked title in #140404 at 40 % frame height; "NOW STREAMING" Montserrat 500, 32 px, letter-spacing 0.3em, #c0262a; slow flicker on the glow (opacity 0.85 ↔ 1.0, 0.12 s, random) to mimic a flare.
- Grade per act: green open, amber middle, blue-steel action, red climax.
