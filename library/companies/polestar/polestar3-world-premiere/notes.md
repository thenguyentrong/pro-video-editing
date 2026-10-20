# Polestar 3 world premiere  (Polestar, 2022-10-12, 1:15 film + 21 s silent red frame, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=55aLCfyNByU
Purpose: launch / reveal film
One-sentence point: On a bare rock island in the Swedish archipelago, a white architectural box opens and the Polestar 3 rolls out into the light - architecture and car as one minimal object.

Structure:
- 0.0-7.5 hook: top-down drone, a dark rock islet in black water, a small white square with the Polestar star on its roof (frames/t001.5s.jpg); fade to black (4 s).
- 7.5-9.4 inside the dark box: only a thin red light bar (the tail light) glows (t005.5s, from the end of shot 1), then a figure in a bright doorway with lens flare.
- 9.4-23.4 details, 1.3-2.8 s each, cut on the beat: the box on the rocks, wheel macro next to a white wall (t011.5s), bonnet and rear from low angles, the cabin through the windscreen, a rotary button macro (t017.5s), the rear on the box platform, the star on the glass roof, tail lights.
- 23.4-49.9 the object in the landscape: the white box with its side open and the car on a cantilevered platform over the rocks (t024.0s), a frontal symmetric shot of the open steel frame with the car centred inside it against the sea horizon (t036.0s), top-down onto the car roof through the box (t042.0s), the car driving out of the box into backlight.
- 49.9-66.0 one 16.1 s drone pull-back: the box on its islet gets smaller and smaller in the grey sea.
- 66.0-68.1 transition: white flash, light leak and lens flare in white/pink/purple, sound drops out for 1.3 s.
- 68.1-74.5 brand card: Polestar red full frame with a soft flare drifting, white "Polestar" wordmark at the left (t072.0s).
- 74.5-96.1 plain red, silent (end-screen space; excluded from the stats).

Cut rhythm (0-75 s): 20 shots, ASL 3.75 s, median 2.06 s, quarters 2.68 / 2.68 / 3.12 / 6.25 - quick details first, then long holds. Shortest 1.28 s, longest 16.1 s (the pull-back) and 7.5 s (opening drone). 0 % under 1 s, 40 % over 3 s. Densest 10-20 s (5 cuts). Cuts on onset 63 % vs 24 % chance = the detail section is cut hard on the music beat (the strongest beat-sync of all films in this folder).

Typography: one word. "Polestar" wordmark in a neo-grotesk (Polestar's own "Polestar Unica"; free match: Inter Medium / Unica77-like), white on red, left-aligned at x 15 %, vertically centred, line box ~6 % of frame height (cap height ~4.5 %). Fades in on the flare (68.5-69.5), holds ~5 s, fades out. No product name, no claim on screen.

Colour/grade: cold Nordic palette for the film (0-66 s): grey-blue sea and sky, grey granite, white architecture and white car; median R-B -23.6 (clearly cool), median saturation 25 %, median luma 108, contrast p95-p5 171 (crisp). Accent: the red tail light bar at the start and the full-frame Polestar red (#d12f36, sampled) at the end - the only warm colour, saved for the brand.

Camera/shots: real live action. Top-down drone (open and close), frontal symmetric architecture shots, low-angle details of the car, macro interior detail, backlit silhouettes with lens flare. Moves: very slow drone moves, slow slides; one long drone pull-back.

Transitions: 19 hard cuts, one fade to black (4 s), and the white flash + light-leak flare into the red card (66-68 s).

Sound: no voice. Electronic/cinematic music, steady -16 to -11 LUFS-M, slowly rising through the film (loudest 22.9 s and the 50-66 s plateau). 1.3 s of near silence at 66.55 s (floor -60 dBFS) during the white flash, then a hit (+38.7 dB) at 68.1 s on the red brand card. Music ends ~72 s; 21 s of silence on the red frame. Integrated -14.7 LUFS.

What makes it premium:
- Architecture as packaging: the car is revealed by a minimalist building, not by a turntable.
- Symmetry and negative space: frontal frames, the car small inside a big frame, a 16 s pull-back that makes it tiny.
- Colour discipline: cold greys for 66 s, then one red frame for the brand.
- Beat-cut detail section (63 % on beat) vs. long calm holds = two speeds.

Recipe (real footage + HTML/GSAP):
1. Shoot the product inside/with one simple white architectural shape (box, frame, plinth) in a raw landscape; top-down drone open, 8-12 detail shots, 3-4 frontal symmetric wides, one long drone pull-back. Grade cool: R-B about -20, saturation ~25 %.
2. Edit: details at 1.3-2.8 s on beats (aim >50 % on onsets), then 4-6 s holds, then a 12-16 s pull-back.
3. Brand card in HTML: full frame `background:#d12f36`; flare = two radial gradients (`radial-gradient(circle at 35% 50%, rgba(255,255,255,.95), rgba(255,120,200,.5) 20%, transparent 45%)`) animated in x by GSAP over 3 s `power1.out` and faded out; before it a 0.6 s white flash (`#f4f8f8` full frame, opacity 0->1->0).
4. Wordmark: `font: 500 4.6vh 'Inter'; letter-spacing:-.01em; color:#fff; position:absolute; left:15%; top:50%; transform:translateY(-50%)`, fade in 0.8 s after the flash, hold 5 s.
5. Sound: cut the music to silence for ~1.2 s under the flash, hit on the red card.
