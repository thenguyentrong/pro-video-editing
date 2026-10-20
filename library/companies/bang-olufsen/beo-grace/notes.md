# Beo Grace  (Bang & Olufsen, 2025-09-23, 1:00, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=kdNeaCbBlR0
Purpose: launch film (earbuds), lifestyle / mood
One-sentence point: With these earbuds the world opens up around you: sea, dunes, forest, birds, the person you love.

Structure:
- 0.0-1.7 wordmark "BANG & OLUFSEN" small on black, cross-fades into a train interior (frames/t000.5s.jpg).
- 1.7-10.2 product moment in a vintage red train: case on a blue knit sweater, hand takes it, a woman in a red jumper puts the earbuds in, smiles (t004.5s).
- 10.2-10.8 black (0.6 s), then 10.8-11.7 a flash montage of 3-frame shots (sea, tree, couple, black).
- 12-18 the world: woman in red on green dunes, earbud close-up in profile with a tiny lower caption (t017.0s).
- 18.5-21.3 texture flurry: forest, wet rock, stone, sand, a black mineral on white (t021.0s), shots of 0.12-0.25 s.
- 21.3-31.6 a man on grass, hand on bark, bison on a plain, man on a sand cliff; 31.6-31.9 another 3-frame texture burst.
- 31.9-46 dusk: silhouettes against a purple sky, a rainbow, a starling murmuration, small captions (t046.5s area).
- 46-53 the couple forehead to forehead at sunset, two silhouettes under the birds.
- 53-56 back to the woman in the train; the brand line appears at the right of her face (t055.0s).
- 56-58 the man in the train, product name "Beo Grace" small.
- 58-60 the train passes; the wordmark sits on the red train side between windows (t058.5s).

Cut rhythm: 40 shots, ASL 1.50 s, median 1.10 s, 47.5 % under 1 s, 7.5 % over 3 s, 40 shots/min. Quarters 1.50 / 1.07 / 1.25 / 2.14 s: fastest in Q2 (texture flurries), slows down at the end. Longest 4.8 s (earbud insert), 3.5 s (man on grass). Two flurries of 0.12-0.25 s texture shots (10.8-11.7 s and 18.5-21.3 s, plus 31.6-31.9 s) break otherwise calm 2-5 s shots. Cuts on onsets 23 % vs 10 % chance: the flurries land on the music.

Typography: tiny poetic captions in lowercase sentence case, white, geometric sans (closest free: Jost), cap ≈ 2.2 % H, centred at y ≈ 86-87 % (low, like a subtitle), 1-3 words each ("where to?"-type questions and one-word answers), held ≈ 1-1.5 s, fade. Brand line ≈ 3.3 % cap, one line, placed at x ≈ 60-83 %, y ≈ 50 % in the empty space beside the face. Product name small (≈ 2.5 %) lower centre. Wordmark printed on the train = in-world logo.

Colour/grade: warm-filmic, slightly warm (R-B +9), soft contrast (p95-p5 116), dark overall (median luma 40, 34 % of frames dark) because of dusk and silhouettes. Colour script: red jumper / red train (the accent) against blue-green landscapes and purple-teal dusk. Saturation median 33 % but it is held in a narrow palette.

Camera/shots: live action on film-like lenses, shallow depth of field; close-ups in profile, wides with one small figure in a big landscape, silhouettes; macro textures (stone, bark, water). Mostly locked or slow handheld; no product renders.

Transitions: hard cuts, short blacks (0.6 s) before a flurry, a cross-fade only at the very start (wordmark to train).

Sound: music only (no VO), airy score with a pulse; −20.4 LUFS integrated, LRA 9.3 LU (big dynamic range, quiet start, swells), true peak −4.4 dBTP. No drop-outs; rises of +16-19 dB at 14.9, 21.3 and 26.1 s.

What makes it premium:
- One accent colour (red) carried by wardrobe and the train, the logo printed in-world.
- Text is almost invisible: 2 % H captions, one short brand line in empty space.
- Long, quiet shots broken by two 3-frame texture flurries = the "sound opening the world" idea without explaining it.
- Wide landscapes with a tiny figure: scale and calm.

Recipe (real footage + HTML/GSAP):
1. Pick one accent colour for wardrobe and one in-world object; grade landscapes cool and the accent warm.
2. Structure: product moment (15 %), world (70 %), product name + in-world logo (15 %).
3. Base rhythm 2-5 s; insert 1-3 flurries of 6-12 texture shots at 3-6 frames each, preceded by 0.5 s of black, cut on music hits.
4. Captions: `font: 400 3vh 'Jost'; text-transform:none; bottom:12%; left:50%; translateX(-50%)`, `opacity 0→1` 0.3 s, hold 1.2 s, out 0.3 s. Brand line `font-size:4.5vh` at `left:60%; top:50%`.
5. End on the logo as a real object in the scene (sign, print, product), not a card.
6. Master around −16 LUFS for social (the original is −20); keep the dynamic swells.
