# Microsoft Copilot: Your everyday AI companion  (Microsoft, 21 Sep 2023, 0:45, 16:9, YouTube @Microsoft)
URL: https://www.youtube.com/watch?v=l4B1UflAty8
Purpose: launch ad (introduces Copilot across Windows, Edge, Microsoft 365)
One-sentence point: everything you make, you now make "co-" with Copilot - shown as one prefix that sticks to forty verbs over real people at work.

## Structure (cut times from metrics.json; sheet labels are exact)
- 0-3.9 s hook: black, then a silhouette at a blueprint wall; the first glass prompt pill ("Help us build a ...") types on over the scene.
- 3.9-9.1 s build: hands sketching, sparks in a workshop, night city, Paint UI; first word card "Co-" arrives white, then "create" types on in a blue gradient (8-9.5 s).
- 9.1-29.5 s middle: alternating rhythm - real person at a creative job (designer, tailor, make-up artist, coder, rider) -> prompt pill over that person -> real product UI (Excel, terminal, Edge, Spotify plug-in) -> "Co-<verb>" card. Cards every 6-7 s: Co-create, Co-edit, Co-develop, Co-author.
- 29.5-37 s acceleration: overhead team table + prompt, laptops and tablets, people laughing at work; cards every ≈1 s (Co-laborate, Co-construct, Co-produce, Co-compose, Co-choreograph, Co-assemble).
- 37.0-38.7 s flash run: 13 shots of 0.125-0.17 s (3-4 frames each), each a different person with a different "Co-<verb>" (Co-write, Co-plan, Co-blend, Co-draw, Co-compute, Co-invent, Co-mingle, Co-present, Co-render ...).
- 38.7-40 s payoff: the real Copilot side panel in Windows ("Create an Instagram reel with photos from my vacation" typed), UI windows slide.
- 40-45.1 s end: the Copilot ribbon logo flies in on a pale blue-white gradient and settles; "Introducing Copilot" under it, held ≈4 s.

## Cut rhythm
- 60 shots in 45.1 s, ASL 0.75 s, median 0.52 s, 80 % of shots < 1 s, 3 % > 3 s, 80 shots/min.
- ASL per quarter 0.87 / 0.87 / 0.81 / 0.49 s: flat fast, then the flash run in the last quarter.
- Cuts per 10 s: 10 / 12 / 10 / 27. Longest shot = end card (5.8 s from 39.3 s), then the opening blueprint shot (3.9 s).
- Shortest: 0.125 s (3 frames at 23.976 fps) in the 37-38.7 s flash run.
- The adaptive detector adds 7 more candidate cuts (UI changes inside one screen recording, a dark fade at 1.75 s); not added - most are UI animations, not new shots.
- Cuts on music onsets 32 % vs 34 % chance: the edit follows the word cards, not the beat.

## Typography
- Word cards: "Co-" in white + the verb in a gradient (blue/teal on cool shots; pink-orange-purple "Copilot" gradient on warm shots). Bold geometric sans, lower case after the capital C. Cap ≈13 % H, centred at ≈50 % H, ≈60 % W for long verbs. Closest free font: **Selawik Bold** (Microsoft's open Segoe fallback) or **Inter Bold**.
- Animation: "Co-" appears first (one shot, ≈0.5-1 s), then the verb types on letter by letter in the same position; in the flash run the whole word changes with the picture every 3-4 frames.
- Prompt pill: frosted-glass rounded rectangle ≈59 % W × 34 % H centred, white blurred fill (backdrop blur), prompt text left-top (regular, cap ≈3 % H, dark grey), app icon bottom-left (Windows / Edge), counter "15/4000" + blue send arrow bottom-right, mic top-right. A thin gradient line along the bottom edge. Types on at reading speed, held 1-2 s.
- End card: ribbon logo ≈38 % H tall centred at ≈45 % H; "Introducing Copilot" in a dark-blue-to-teal gradient, semibold, cap ≈7 % H, centred at ≈75 % H.

## Colour / grade
- Each shot keeps its own world: cyan blueprint, warm workshop sparks, purple gamer light, neon synthwave, sunny pastel offices. Contrast medium-high, saturated, clean digital (no grain, no letterbox).
- The glue is the gradient word and the frosted pill, not one grade. End = pale blue-white gradient with a soft blue swoosh.

## Camera / shots
- Real people doing real crafts (sketching, welding, tailoring, make-up, coding, film sets, dance); overhead table shots; close hands; real screen recordings of Windows / Edge / Excel; motion-graphics end card.
- Mostly slow handheld pushes; each shot is a fragment of a longer move.

## Transitions
- Hard cuts almost everywhere. The prompt pill and the word card act as overlays across cuts (the same pill continues over two shots).
- UI windows slide in at 39 s; the logo flies in with a soft 3-D twist (40-41 s).

## Sound
- Music-led, no narrator (speech recognition found no clear spoken lines; any vocal is part of the track).
- Integrated −21.5 LUFS, LRA 6.7 LU, true peak −4.5 dBTP: very quiet for an ad (≈6 LU under the Pixel ads, ≈11 LU under Samsung). No silences, no drop-outs.
- Biggest rise +31.6 dB at 0.5 s (music start out of silence), +21.8 dB at 3.75 s (first cut), +20 dB at 12 s. Loudest moment 39.2 s, the end of the flash run.

## What makes it premium
- One language idea ("Co-") carries the whole ad; the word card does the explaining, so no narrator is needed.
- Every prompt sits over a real person at a real craft - the AI is the helper, the person is the maker.
- Real product UI in between, readable and short.
- A flash run of 13 three-frame word cards right before the logo turns a list into a rush.

## Recipe (real footage + HTML/GSAP)
- Footage: 15-20 short clips of people at hands-on crafts (stock: "designer sketching on paper close up", "welding sparks workshop night", "tailor measuring fabric", "make-up artist backstage ring light", "gamer purple light keyboard", "team overhead table laptops", "friends laughing office tablet"). Cut each to 0.4-0.9 s; the opener 3-4 s.
- Word card: `font: 700 13vh/1 'Inter'`; "Co-" white, verb `background: linear-gradient(90deg,#2B7FFF,#20C7E8)` (cool shots) or `linear-gradient(90deg,#E84BD0,#FF8A3D,#8A5CFF)` (warm shots) with `-webkit-background-clip:text; color:transparent`. "Co-" in at 0 s; verb typed with GSAP `stagger: 0.04` per letter.
- Prompt pill: `width:59%; height:34%; border-radius:24px; background:rgba(255,255,255,.55); backdrop-filter:blur(24px)`; prompt `font:400 3vh Inter; color:#222`, typed at ≈45 ms per character; send arrow #2B7FFF bottom-right.
- Pace: ASL ≈0.8 s for 30 s, then a 1.5-2 s flash run of 3-4-frame shots with a new word each, then a 5 s end card.
- Mix: music only. If you want the reference level, master ≈ −16 LUFS for web instead of −21.5 (the original is unusually quiet).
