# Planet Earth III – Official Trailer  (BBC Earth, uploaded 2023-10-08, 77.9 s file = 59.0 s trailer + 19 s silent end slate, 16:9, YouTube / BBC Earth channel)
URL: https://www.youtube.com/watch?v=nNWXMAJF7ww
Purpose: landmark natural-history series trailer
One-sentence point: 17 years after Planet Earth, the planet is still beautiful, powerful and fragile – and its future is ours.

Structure (a written poem in 10 captions over a montage, no narrator visible in the edit):
- 0.0–2.3 HOOK: aerial of red rock and pale salt flats with a giant Roman numeral "III" made of translucent vertical bars; dissolves (2.3 s) into a slow aerial of sand dunes.
- 2.3–5.7 CAPTION 1 "17 YEARS AGO OUR EYES WERE OPENED" fades in over the dunes; music enters at 2.6 s (+18.5 dB).
- 5.7–13.4: macro animal eyes (baboon, eye in a tree hole), leopard; CAPTION 2 "TO THE SHEER WONDER OF OUR PLANET" over a forest (7.4–8.3 s).
- 13.4–15.6 CAPTION 3 "BUT THERE'S STILL SO MUCH TO DISCOVER" over a dark sea floor with purple anemones (2.2 s, the first slow shot).
- 15.6–37 CHAPTERS: each chapter = one adjective caption over a calm graphic shot, then 2–5 action shots: "BREATHTAKINGLY BEAUTIFUL" (braided river aerial, 22.9 s), "FIERCELY POWERFUL" (wave, 25.4 s), "PERILOUSLY FRAGILE" (ostrich with chicks, 29.3 s), "A WORLD OF HOPE" (sunset sea, 36 s). Frogs, saiga, sea lions, octopus, deep-sea creatures, locusts, a jumping ray.
- 37–53 HUMAN TURN: paragliders with birds, people touching an elephant, Indigenous women, "WITH CHALLENGES WE FACE TOGETHER" over a forest fire (42 s), burning bush, a sloth rescue, "THIS IS OUR HOME" over a dune aerial (47.1 s), herds, "THIS IS OUR FUTURE" over a desert road aerial (51–53 s), an elephant walking through a town at night (53 s).
- 55.1–59.0 END TITLE: star sky, a black silhouetted quiver tree inside a thin bright eclipse ring; small BBC blocks above "PLANET / EARTH / III" stacked in very wide-tracked caps. Two short silences (57.6 s 0.2 s, 58.55 s 0.25 s) set up the final stings (+29.5 dB at 57.85 s).
- 59–78 static rock-texture end slate, silent (YouTube end screen, not part of the trailer).

Cut rhythm: 50 shots in 59 s (51 counting the opening dissolve), ASL 1.18 s, median 0.92 s. ASL per quarter 1.64 / 1.05 / 0.87 / 1.13 s; densest 40–50 s (13 cuts, shots of 0.52–0.6 s during the fire/human section). 54 % of shots under 1 s. Long shots only at the start (5.7 s) and on the end title (3.9 s). Caption shots are the calm ones (1.3–2.2 s); action shots between them are 0.5–1 s. Cuts on onsets 2 % (chance 7 %): cut to picture rhythm, not to beats.

Typography:
- Captions: clean geometric sans, regular/light weight, all caps, very wide tracking (~0.2 em), white, no shadow box. Closest free match: Montserrat 400 (or Gotham Book). Cap height ~2.5 % of frame height; always one line, centred horizontally at ~49 % of frame height; 3–6 words per caption. Fade in ~0.4 s, hold 1–2 s, fade out with the shot.
- Captions only sit on calm, low-detail, graphic shots (aerials of dunes, rivers, sea, savannah sky) so they read without a box.
- Opening numeral: "III" as three tall translucent bars (~70 % frame height) over an aerial, like a frosted-glass window.
- End title: BBC blocks (~3 % height) above PLANET / EARTH / III in the same sans, letter-spacing ~0.5 em, ~4 % cap height, inside an eclipse ring of light.
- BBC blocks logo top-left on every shot (~3 % height).

Colour/grade: natural but rich; warm earth tones (ochre dunes, red rock), teal water, green forest, black-blue deep sea; fire orange in the human section; end card deep blue star sky with white ring. Not desaturated, no heavy look; 8 % of frames mostly empty (only the deep-sea shots).

Camera/shots: landmark natural-history footage: drone/helicopter aerials (graphic, top-down), long-lens wildlife, macro eyes, underwater, slow motion (ray jump, water drops), a few human/documentary shots in the last third.

Transitions: hard cuts; one cross-dissolve at 2.3 s (numeral aerial → dunes); captions fade. No whips, no flashes.

Sound: one epic song/score build (the BBC Earth uploads of this trailer credit Bastille / Hans Zimmer elsewhere; not verified by listening). Measured: music in at 2.6 s, slow climb from −19 to −12 LUFS by 13 s, a small dip at 18–20 s (−20), then a long loud plateau −9 to −13 LUFS from 27 to 56 s (loudest 33 s, −9). Two micro-silences right before the end-title stings. Integrated −14.1 LUFS (loud for YouTube), LRA 7.6 LU, true peak −1.4 dBFS. No narrator visible from the edit; the captions do the talking.

What makes it premium:
- The copy is a short poem (adjective chapters: beautiful / powerful / fragile / hope) – it gives a structure to 50 random wildlife shots.
- Captions only on calm graphic aerials; action shots never carry text.
- Thin, widely tracked caps at small size = calm authority, never shouts over the footage.
- A turn from wonder to responsibility in the last third (fire, people, "our future").
- Symbolic end card (eclipse ring + one tree silhouette) instead of a busy montage.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Copy: write 8–10 captions of 3–6 words that form one sentence-chain; place one caption every ~5 s.
- Edit: caption shot (calm aerial, 1.3–2.2 s) + 2–5 action shots (0.5–1.0 s) per chapter; 50 shots in 60 s; make 40–50 s the densest part; end on a 4 s symbolic title.
- Captions: Montserrat 400, uppercase, letter-spacing 0.2em, cap height 2.5 % (~27 px font on 1080p ≈ 38 px font-size), #fff, centred at top 49 %; GSAP fromTo opacity 0→1 duration 0.4 ease "power1.out", hold, opacity →0 duration 0.3 just before the cut. No box, no shadow (choose calm plates instead); if the plate is busy, add a 20 % dark radial vignette behind the line.
- Opening: three div bars (width 11 % each, gap 5 %, height 70 %), background rgba(255,255,255,0.18) with backdrop-filter: blur(6px) brightness(1.15), fade in 0.6 s, then 1.2 s cross-dissolve to the next plate.
- End title: dark blue star plate, SVG circle stroke 2 px white with a soft glow (filter: drop-shadow(0 0 12px #fff)) drawn with stroke-dashoffset over 1.2 s, logo + stacked title letter-spacing 0.5em; put a 0.2 s silence before the final hit.
- Audio: song/score with a slow 25 s build to a loud plateau (−10 to −12 LUFS momentary), no VO.
