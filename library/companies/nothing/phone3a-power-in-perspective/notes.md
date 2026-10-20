# Phone (3a) Series: Power in Perspective  (Nothing, 2025-03-04, 1:53, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=YxlN6WI97z0
Purpose: launch film (feature walkthrough, mostly 3D product render + UI)
One-sentence point: Two phones, one light and one dark, with their best cameras, Essential Space AI and a faster chip, shown as a calm, typographic product tour.

Structure:
- 0.0-6.3 hook on black: a small light streak (0 s), then the dot-matrix line "phone(3a) / phone(3a) pro" decodes in letter by letter (3-5.5 s, scrambled glyphs resolve into letters, frames/t004.8s.jpg). Quiet sound.
- 6.3 reveal on a big hit (+32 dB): split-screen diptych, white (3a) on a light grey left half, grey (3a) Pro on a dark right half. 6.3-14.7 four diptych shots (light/dark = "perspective").
- 14.7-16.6 black card, serif: "Our most advanced camera systems" (words appear in 2 steps).
- 16.6-34 (3a) camera chapter on light grey: flank label "(3a)  camera" either side of the product, callouts with dotted leader lines (50 MP / Shake-free / OIS camera...), exploded lens stack, PCB, lock screen with a dot-matrix "10:20" clock, camera UI demo.
- 34-52 (3a) Pro camera chapter on dark grey: same flank label "(3a) pro  camera", periscope prism + lens elements exploded with a blue light beam, callout list, landscape zoom demo.
- 52-60 "TrueLens  Engine 3.0" flank over glowing colour layers; pixel mosaic of white squares that resolves into a photo; three-line mono list ("Advanced computational technology / AI processing / Multi-frame technology").
- 60.8-62.4 black serif card "Your second memory".
- 62-79 Essential Space UI demo on light grey (red Salone del Mobile poster, voice-note bar with a quoted mono caption "Remind me to buy tickets tomorrow"), "essential  space" flank, then "powered by  NOTHING OS 3" flank and a line-up of home screens.
- 80-88 dark: fade through black, red glowing chip "power  house" flank, spec lines left/right, chip resolves into the board.
- 88-96 display chapter: screen-side render with spec list (6.77" AMOLED / 3000 nits...).
- 96-104 bookend: the light/dark diptych again.
- 104.8-112.8 end on black: serif "Designed in London", dot-matrix "phone(3a) / phone(3a) pro", "NOTHING(R)", "nothing.tech" (~1.5-2 s each), in silence.

Cut rhythm: 31 hard-cut shots, ASL 3.64 s, median 2.40 s, quarters 3.13 / 3.13 / 3.13 / 4.03 (very even). Longest 16.1 s (74.8, a continuous render that moves from UI line-up to chip via a fade), 7.9 s (end cards), 7.5 s, 7.0 s. Shortest 0.48-0.60 s (63-64 s, the poster zoom). 10 % under 1 s, 42 % over 3 s. Plus about 12 soft transitions (morphs and fades, see below): counted as beats it is ~42 beats = one new picture every ~2.7 s. Cuts on onset 13 % vs 16 % chance = cuts do not follow the beat.

Typography (three voices, all small, all centred or symmetric):
- Dot-matrix (Nothing "Ndot" style, free match: Doto or DotGothic16), lowercase, used for product names and the flank labels. Flank labels sit on the horizontal centre line, mirror-placed at x 5-13 % and 83-95 % of the width, height ~3.4 % of frame height; centre title "phone(3a) / phone(3a) pro" ~5 % high incl. brackets. Animation: per-letter scramble/decode in ~2 s.
- Light serif with a typewriter flavour (looks like Nothing's own serif; free match: Cutive or IBM Plex Serif Light), sentence case, white on pure black, ~5.8 % of frame height incl. descenders, 1 line, 2-5 words, held 1.6-2 s, words added in steps.
- Monospace (typewriter mono; free match: Cutive Mono / IBM Plex Mono), sentence case, cap height ~1.9 %, line pitch ~3.4 %, left-aligned blocks of 1-4 lines, joined to the product by 1 px dotted leader lines (frames/t020.5s.jpg).
Text is never bigger than ~6 % of the frame; the product is the hero.

Colour/grade: two studio worlds that alternate by chapter: light grey gradient (#e9edf0 -> #c9d3da) for the white (3a), dark charcoal gradient (#1a1f24 -> #3a434b) for the Pro. Accent colours come only from the product world: Nothing red square, the red chip glow, a red poster, a teal wallpaper. Median luma 77, 27 % dark frames and 27 % bright frames (balanced), median saturation 12.5 % (very grey), R-B -8.9 (slightly cool).

Camera/shots: almost all 3D CG product renders: slow orbits, macro push-ins on the camera ring, exploded views (lens elements, prism, PCB), side-on screen. UI is shown on the rendered phone screen, not full-screen. No people (one model appears only inside the phone's photos).

Transitions: 30 hard cuts plus object-continuity morphs inside the render: lens stack shrinks into the module -> module turns into the PCB -> PCB lands as the lock screen (24-27 s); phone rotates from screen to back (31-33); slide/push up from the white phone to the Pro macro (33.8); fade through black 80.0-80.5 into the red chip; chip -> board -> screen flip (86-89). Pixel-mosaic resolve (55-59) as a "digital" transition.

Sound: no voice-over (whisper found none). One electronic music bed, heavily levelled: -11 to -13 LUFS-M for 75 s. Hit on the reveal at 6.3 s; dip to -26 LUFS-M at 82-87 s (the dark chip build) then the loudest moment at 88.3 s (screen reveal). Music fades out 103-107 s; the logo cards (106-112.8) are fully silent. Integrated -13.7 LUFS. Low onset density (0.76/s).

What makes it premium:
- Strict system: three type voices with fixed jobs (dot = names, serif = statements, mono = specs).
- Symmetric "flank label" layout: product dead centre, one word on each side. Instantly Nothing.
- Light/dark duality as the concept AND the colour script; the diptych opens and closes the film.
- Exploded technical renders with thin dotted leaders: engineering shown as beauty.
- Calm: even ASL (3.1 s every quarter), small type, silence on the logo.

Recipe (real footage + HTML/GSAP):
1. Background: full-frame CSS gradient, light `linear-gradient(180deg,#eef1f3,#c7d0d7)` or dark `linear-gradient(180deg,#14181c,#3b444c)`. Product as cut-out photo or render, centred, 60-75 % of frame height.
2. Flank label: two `span`s in a dot-matrix font (Doto 400, lowercase, 3.2-3.6 % of frame height, letter-spacing 0.02em), left at 5 % and right-aligned at 95 %, both on `top:50%`. Decode-in: for each letter, cycle 3-5 random glyphs every 40 ms, then lock; stagger 0.05 s per letter.
3. Statement card: black frame, serif (IBM Plex Serif 300 or Cutive), 5-6 % height, centred, words in with `opacity 0->1` stagger 0.35 s, hold 1.6 s, cut (no fade-out).
4. Spec callouts: mono 1.8-2 % cap height, 1-4 lines, `line-height:1.75`; leader = SVG polyline with `stroke-dasharray:1 3`, 1 px, drawn with GSAP `strokeDashoffset` 0.6 s `power1.out`, text fades in 0.2 s after.
5. Rhythm: 2.5-4 s per shot, each chapter = 1 statement card + 4-8 shots. Morph between shots by scaling the same object (`scale 3 -> 1`) instead of cutting when you can.
6. Sound: one levelled bed, a dip of 4-6 s before the hero spec, hit on the reveal, logo cards in silence.
