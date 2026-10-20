# Too Old Not To | Patagonia Australia  (Patagonia Australia, 2026-04-07, 6:35, 16:9, YouTube / Patagonia Australia channel)
URL: https://www.youtube.com/watch?v=ljp5H2pjAFc
Measured: first 300 s only (of 395 s). Everything below is about 0:00–5:00.
Purpose: athlete / portrait short documentary (an ocean swimmer in her fifties)
One-sentence point: a 55-year-old birth doula keeps taking on long ocean crossings because fear is a reason to go, not to stop; age is the reason to do it now.

Structure (first 5 min):
- 0–7.6 OPEN UNDERWATER: a land and sea-country acknowledgement in small hand-lettered caps over turquoise underwater footage (≈1–5 s), then the "patagonia" wordmark in black on the water (≈6–7.5 s).
- 7.6–17 HOOK MONTAGE (9 cuts in 10–20 s): a lifeguard on the beach, feet on sand, the swimmer pulling on her cap, a paddleboard, goggles underwater with 0.2–0.32 s flash cuts (9.6–12.8 s); title "TOO / OLD / NOT / TO" hand-lettered and stacked, with her first name signed in script, over a goggle close-up (≈13–16.5 s).
- 17–23 first interview on her sofa at home (6 s), warm room, coloured shelves.
- 23–100 THE SEA: headland aerials, top-down drone of her swimming, sunrise glare, pink paddleboard, underwater bubbles; interview returns every 20–30 s; one 0.5 s drop to -45 dB at 62.1 before a line (the only drop-out).
- 100–150 BACKSTORY: memorabilia inserts (medals in a jar, race numbers), a training swim with friends, close-ups of her face in the interview.
- 150–180 aerials of wet sand textures, swimmers in a pack, rain on the sea.
- 180–186 HAND-DRAWN MAP: an illustrated chart of two islands with a dashed route between pins (the crossing she is preparing for).
- 186–245 PREPARATION: open-water crossings, laughing in the interview, photos pinned up, lifeguard club, a tractor pulling boats.
- 245–272 KINETIC HANDWRITING: her spoken words appear one or two at a time as white hand-lettered caps over sunsets, ice-bath close-ups and a beach walk (≈1–2 s per word group), a typographic beat inside the doc.
- 272–300 the swim again, interview, the club at dawn.

Cut rhythm (0–300 s): 130 shots, ASL 2.31 s, median 1.96 s (adaptive detector; 6 false cuts on text changes and animations dropped after checking pairs; the scene detector found 112). ASL per quarter 1.83 / 2.21 / 2.59 / 2.59 s. 18.5 % of shots under 1 s, 24 % over 3 s; shortest 0.2–0.32 s (goggle flashes), longest 7.6–7.8 s. Cuts per 10 s steady at 3–7 (9 in the hook). 53 % of cuts on an audio onset vs 48 % by chance (music-paced, slightly above chance).

Typography:
- Everything is hand-lettered (closest free: Caveat Brush / Permanent Marker for the caps, Caveat for the signature), white or black, no boxes.
- Acknowledgement: small hand-lettered caps, cap ≈2 % H, 2 short paragraphs centred at y ≈40–55 %.
- Wordmark: "patagonia" black, ≈5 % H, centred right of centre on the water.
- Title: 4 stacked words, cap ≈6 % H each, left at x ≈10–17 %, y ≈45–75 %, with a hand-drawn wave underline; her first name as a script signature at lower right.
- Kinetic words: white hand-lettered caps ≈4 % H, centred, 1–3 words at a time, each ≈1–2 s, cut on with the spoken word.
- Map: hand-drawn islands, serif caps labels ≈3 % H, dashed pink route, black pins.
- No lower thirds; no subtitles (English speech).

Colour/grade: turquoise and teal water, warm sunrise orange, pink accents (cap, board, route); interviews warm and soft. Full 16:9.

Camera/shots: underwater, top-down drone over the swimmer, surface POV, handheld beach and club life, sofa interview with a shallow-focus home background, macro objects (medals, goggles, hands in ice).

Transitions: hard cuts; text animates on footage; map built with animated route.

Sound: (I could not listen; from level data.) Integrated -16.3 LUFS, LRA 4.4 LU, true peak -0.7 dBTP: flat, music-led level (-18…-22 dBFS in every 10 s window); one 0.5 s drop-out at 62.1 s; biggest rises +25 dB at 70.1 and +21 dB at 264.35 (the handwriting section).

What makes it premium:
- A complete hand-made type system (acknowledgement, title, signature, map, kinetic words) that feels like her own notebook.
- Fast hook (9 cuts / 10 s) with goggle flashes, then a calm 2.3 s rhythm.
- Objects as proof of a life in the sea (medals, race numbers, photos).
- The brand appears once, as a black wordmark on the water.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- 0–7.5 s: underwater plate; acknowledgement `font: 400 2vh "Caveat Brush"; text-transform: uppercase; letter-spacing:.05em` fade 0.5 s; then the logo.
- Hook 10 s: 8–9 cuts, 3 flashes of 5–8 frames; title stacked words `400 6vh "Permanent Marker"`, each word `opacity 0→1` with 0.1 s stagger, a SVG wave underline `stroke-dashoffset` 0.6 s, script name `Caveat 5vh`.
- Body ASL 2.2–2.6 s, interview every 20–30 s (4–6 s each), objects 2–3 s.
- Map 6 s: illustrated islands, pins `scale 0→1` 0.3 s `back.out`, dashed route drawn 1.5 s.
- Kinetic words 25 s near the end: 1–3 words per card, `400 4vh "Permanent Marker"`, on with the spoken word, off on the next. Master -16 LUFS, true peak ≤ -1 dBTP.
- Stock queries: `open water swimmer drone top down`, `underwater goggles swimmer close up`, `sunrise ocean glare`, `medals in jar close up`.
