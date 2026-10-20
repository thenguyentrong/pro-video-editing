# This Is What a Godlike Civilization Would Look Like  (Kurzgesagt – In a Nutshell, 2026-09-22, 14:12 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=QW_jlUn4gA8
Purpose: animated science / futurism explainer (narrator-led)
One-sentence point: Real progress may be measured by how small you can control things, not how big you can build — so advanced aliens might be invisible to us.

Data note: first 300 s analysed (trimmed after download). Cuts measured with `--detector adaptive` (29 cuts; scene detector 25, all inside the adaptive list). No sponsor inside the first 300 s.

## First 30 s (hook)
- 0.0–0.5 slow pan across deep space with galaxies; narration starts at 0.5 s with a contrarian claim (what we believe about aliens may be wrong).
- 2.0–5.0 a fleet of crystalline ships led by a smiling alien crosses the frame (the cliché image of progress).
- 5.0–9.5 camera drifts to aliens draining planets with tentacle cables (pan, no cut).
- 9.5–15.5 a sun, then a planet's surface being strip-mined and glowing orange; tiny caveman silhouettes with a spear appear on the ridge (≈14 s): a visual match between "galactic empire" and "caveman" thinking.
- 15.5 hard cut: close-up of a cave-girl character; a speech bubble grows "MORE!" → "MOOOOOORE!!!" with her eyes turning to stars (17–20 s) — the comic beat.
- 20.0 hard cut to a dark starfield with drifting coloured ghost shapes (the hidden old civilizations).
- 24.3 hard cut to a god-like green alien in a pastel mushroom city, a glowing atom in its hands (the answer image: progress inward).
- ≈24–31 the question is posed (what if progress means going inward?).
- 31–35 the atom alone on purple blobs; 35.3 hard cut into an isometric forest camp (the human story begins). No chapter card until 215 s.
- Shape: contrarian claim at 0.5 s → cliché image → mock it (caveman match + gag at 15–20 s) → reveal the alternative image (24 s) → question (≈24–31 s). 3 hard cuts in 30 s; ≈8 set-ups (≈3.7 s each).

Structure (first 300 s):
- 0–35 hook.
- 35–83 humanity as expansionist: isometric tiles of forest, farms, factories, the Earth, a rocket launch (59–66 s), isometric cities growing from villages to towns (67–83 s).
- 83–130 the Kardashev scale: a cute octopus alien, a pink header label "The Kardashev Scale", three numbered circles (1, 2, 3) with icons of planet, star and galaxy; one 30.8 s shot (99.7 s).
- 130–182 progress from the small: pyramids at sunset, glowing writing glyphs (137–143 s), a library, a scientist, metals / medicines / fertilizer in 3 s beats (155–168 s), an isometric microchip city (169–182 s).
- 182–215 the Barrow scale: header label, hands holding a tiny world, a human-history timeline strip, isometric tiles again.
- 215.3–220 chapter title "THE IMMORTAL GODS OF NATURE / Type 2-Minus" on a dark jungle with glowing creatures; a 0.75 s audio dip (214.4–215.15) right before it, then a +28.8 dB rise at 219.9 s.
- 221–300 DNA strands, a speech bubble "break" with a multicolour word, the immortal jellyfish, super organs (eye with rainbow rays), organ banks in jars, modified pets and creatures.

Cut rhythm: 30 shots in 300 s, ASL 10.0 s, median 7.52 s. ASL by quarter 8.3 / 12.5 / 8.3 / 8.3 s. 0 % under 1 s, 93 % over 3 s. Longest 30.8 s (99.7 s), 28.7 s (228.2 s), 24.2 s (42.4 s); shortest 2.8 s (155.8 s). Cuts per 10 s: 0–2. By eye ≈1 new set-up every 3–5 s. Cuts on onsets 52 % vs 56 % chance.

Typography:
- Chapter title: white geometric sans caps, two lines, cap ≈7.3 % H, centred; a subtitle in orange-yellow #F2B649 sentence case ≈3.8 % H under it ("Type 2-Minus"). Hard on, ≈4.5 s hold. Closest free: Outfit SemiBold / Montserrat SemiBold (guess).
- Scale header: small pink pill/bar label top left ("The Kardashev Scale", "The Barrow Scale"), ≈2.5 % H.
- Numbered circles: white numerals in solid teal / blue discs under each icon, ≈4 % H.
- Speech bubbles: white rounded bubble with purple heavy caps (comic shout) or a multicolour word in quotes; they grow letter by letter.
- No subtitles; at most one short label on screen at a time.

Colour/grade: space scenes on #010925 / #0C0130 navy-black; warm human-history scenes in sand #B49059 / #D8BB85 with sunset orange #F2B649; the alien utopia in mint #ABFAED / #2DF7CF with magenta #930254; cave-girl scene in coral #EB6F47 and magenta #AA016A. Each chapter world has its own palette, all saturated, flat, no outlines, soft glow on light sources.

Camera/shots: 100 % 2D animation. Isometric dioramas (tiles that grow), wide parallax space pans, close-up character reactions for jokes. The camera keeps moving on every hold.

Transitions: hard cuts between worlds (every ≈10 s), camera pans inside worlds, a dark-dip before the chapter title.

Sound: integrated −14.7 LUFS, LRA 2.0 LU, true peak −2.3 dBTP. 50 ms RMS median −19.6 dBFS, p10 −29.0 dBFS → score ≈9–10 dB under the voice, 0 % of windows below −45 dBFS. One designed drop-out of 0.75 s before the chapter title (214.4 s), then the biggest rise (+28.8 dB at 219.9 s). SFX on bubbles, pops and whooshes.

What makes it premium:
- The opening mocks the viewer's own assumption with a funny human character before offering the new idea.
- Each era/world has its own colour world, so the eye always knows where it is.
- Long held shots (24–31 s) where the drawing itself animates, instead of fast cutting.
- Very few words on screen; the narration carries all facts.

Recipe (HTML/GSAP):
- Isometric tile world: CSS `transform: rotateX(55deg) rotateZ(45deg)` on a grid of SVG tiles; tiles pop up `gsap.from(tile,{y:40,autoAlpha:0,duration:.35,ease:"back.out(2)",stagger:.04})`; buildings swap to bigger ones every 2–3 s.
- Speech-bubble gag: bubble `scale 0 → 1` 0.2 s `back.out(3)`, text grows by appending letters every 0.05 s, the face swaps to a star-eyes version on the last letter, hold 1.5 s.
- Chapter title: footage dips (`filter: brightness(.6)`), `font:600 7.3vh "Outfit"; color:#fff; text-transform:uppercase`, sub-line `500 3.8vh "Outfit"; color:#F2B649`; audio dip 0.75 s before, a hit on the reveal.
- Rhythm: hard cut every 7–10 s on average; inside each shot a new camera target every 3–5 s.
