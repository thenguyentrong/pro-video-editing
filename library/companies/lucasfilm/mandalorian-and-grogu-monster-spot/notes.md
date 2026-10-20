# The Mandalorian and Grogu | "Monster" TV spot  (Lucasfilm / Star Wars channel, 25 Apr 2026, 30.1 s, 16:9 file / 2.39:1 picture, cards full frame, YouTube + TV)
URL: https://www.youtube.com/watch?v=3XD0CSrBYuA
Purpose: TV spot (30 s, 4 weeks before release)
One-sentence point: one dark mission, one monster, the galaxy at stake: see it on May 22 in IMAX and 3D.

## Structure (beats with timestamps; % of 30.1 s)
- 0.0–5.3 **cold open on a threat line**: the hero in a dark cave, a giant serpent rising out of water, jungle, a city (6 shots, ASL 0.9 s). No logo.
- 5.3–7.6 **tagline card 1** "WHEN DARKNESS / FALLS" on a starfield (2.25 s, at 18 %).
- 7.6–10.4 three dark action shots + one dialogue close-up (ASL 0.7 s).
- 10.4–13.4 **tagline card 2** "ONE MISSION" (3.0 s, longest shot): the card **dissolves into a snow-mountain shot** at ≈11.8 s, the text stays over the picture; biggest hit +17.9 dB at 10.55 (loudest moment, −9.1 dBFS).
- 13.4–15.5 Grogu with a rifle, a walker in the snow.
- 15.5–16.5 **tagline card 3** "WILL CHANGE / THE GALAXY" (1.0 s, at 51 %).
- 16.5–25.2 **release info inside the action** (ASL ≈0.8 s): "ON / MAY 22" over an explosion, "IN / IMAX" over a crash, "AND / 3D" over a jungle flight, each word pair over a different shot.
- 25.2–27.7 **title logo** (2.5 s, at 84 %), hit +16.1 dB at 26.9.
- 27.7–29.3 "ONLY IN THEATERS / MAY 22 / FILMED FOR IMAX" + format logos (1.5 s). 29.3–30.1 "GET TICKETS NOW" (0.8 s).

## Cut rhythm
- 30 shots, **ASL 1.00 s**, median 0.80 s. ASL per quarter 0.94 · 0.94 · 0.68 · 1.25 s (per-quarter values are rough for a 30 s piece).
- **70 % of shots under 1 s**, one shot over 3 s (the dissolving card). 59.9 shots per minute.
- Cuts per 10 s: 11 · 10 · 8. Shortest 0.38 s.
- Cuts on audio onsets **41 % vs 31 % chance**: cut to the music (the trailer: 25 % vs 21 %).
- Speech in ≈25 s of 30 s: one line per 2–3 s, none of them longer than a sentence.

## Typography
- **Nine text moments in 30 s** (the main trailer has three in 132 s). The spot needs taglines because it has no time to tell the story with scenes.
- Same face as the trailer's date card: semi-bold geometric caps (closest free: Montserrat 600), pale green metallic with a bevel and a dark lower extrusion, centred.
- Two-size stack: small line ≈8 % H, big line ≈12 % H. On black cards they sit on a faint starfield; over action they sit directly on the picture at ≈50–60 % H with no box.
- In: hard cut. Out: hard cut, or the picture dissolves in under the text (0.8–1.2 s). Holds 1.0–3.0 s.
- Title: the trailer's 3D slanted green logo with the "STAR WARS" wordmark on top (the trailer title has no wordmark until the end).

## Colour / grade
2.39:1 footage; cards full frame. The darkest shots of the campaign (cave, serpent) open the spot, then snow, jungle and desert daylight.

## Camera / shots
Creature reveal, hero close-ups, vehicle action, explosions; the comic beats of the trailer are cut out except one line.

## Transitions
Hard cuts; one dissolve from a card into a shot; text over picture instead of separate cards for the release info.

## Sound
- Integrated **−14.1 LUFS**, **LRA 3.8 LU** (trailer 8.6): a wall of music with no quiet section and no silence.
- Two hits: the "ONE MISSION" card (+17.9 dB) and the title (+16.1 dB). The music fades under the end block (−20…−22 dBFS) to digital silence at 30 s.

## What makes it premium
- It reuses the trailer's type system, so the spot reads as part of the same campaign.
- The release facts (date, IMAX, 3D) are cut into the action as two-word overlays: no separate info slide stops the energy.
- One card dissolves into the picture: a tiny moment of air in a wall-to-wall 30 s.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. 0–5 s: six shots of 0.4–1.3 s, threat line on top, no logo.
2. Three tagline cards at ≈18 %, 35 % and 51 %, 1.0–3.0 s each: `.sm{font:600 38px Montserrat}` `.lg{font:600 58px Montserrat}`, `color:#e8f5d8; text-shadow:0 3px 0 #2e4a2b`, on black with 200 tiny star dots at opacity .3.
3. On one card, fade the next shot in under the text: `tl.fromTo(shot,{opacity:0},{opacity:1,duration:1.0,ease:"none"},t+1.4)`.
4. 16–25 s: date and format words over action shots, one word pair per shot (0.7–1.0 s), placed at 45–60 % H.
5. Title 2.5 s at ≈84 % on a hit; end block 1.5 s; call to action 0.8 s.
6. Cut on the beat; keep the music compressed (LRA ≈4 LU); master −14 LUFS for web, true peak −1.5 dBTP.
