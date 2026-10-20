# introducing OP-XY  (teenage engineering, 2024-11-14, 0:34, 16:9, YouTube; source 360p)
URL: https://www.youtube.com/watch?v=xceQgvssxeU
Purpose: launch teaser (product reveal, no claims on screen)
One-sentence point: "It's here. It's real. It's black." (YouTube description): a black instrument slowly found by light in the dark, then its name.

Structure:
- 0.0-3.7 hook: almost black frame, two white LED dots inside dark square keys (frames/t001.5s.jpg); a light slides across the key edges.
- 3.7-6.9 side edge with USB port and a tiny green LED (frames/t004.5s.jpg).
- 6.9-12.2 key field macros with raking light, white LED dots on round knobs, then a row of keys lighting up grey-to-white (frames/t007.5s.jpg, t010.5s.jpg).
- 12.2-17.2 the TE bolt-and-nut pictogram as a chrome badge on the black body, between two fuzzy dark spheres (frames/t012.8s.jpg); then the small display with blocky pixel graphics (t015.0s.jpg). The brand mark appears as a physical object long before the logo card.
- 17.2-21.0 side view of the dark body, knobs in silhouette.
- 21.0-27.8 hero: straight-on product on a floor, light rises on the floor and on a grey panel behind it (frames/t024.8s.jpg), 6.8 s.
- 27.8-29.0 logo "[OP] XY" on black (OP inside a square outline).
- 29.0-33.5 teenage engineering pictogram logo + legal lines, fade to black.

Cut rhythm: 9 shots, ASL 3.72 s, median 3.16 s, quarters 2.79 / 2.09 / 2.79 / 4.18. Shortest 2.04 s, longest 6.8 s (hero). 0 % under 1 s, 56 % over 3 s. (ffmpeg scene cut detection found only 1 cut because the frames are nearly black; cuts2 + eye found 8.) Cuts on onset 0 % - the music has almost no onsets (0.15/s).

Typography: no words in the film body. Only the end: product logo "[OP] XY" (thin geometric sans, light grey on black, ~9 % of frame height incl. the boxed "OP"), then the TE nut-and-bolt pictogram (~20 % of height) with 2 tiny legal lines (~1.7 %). Centred, static, short fades.

Colour/grade: black on black. Median frame luma 6/255, 88 % of frames darker than 40, median saturation 1.6 % (grey only), contrast p95-p5 33 (most of every frame is black; only edges and LEDs catch light). The only colour is one tiny green LED. Light = hard raking strip lights that trace edges and key rims.

Camera/shots: very slow push-ins and slides across macros, low angles, diagonal compositions, deep shadows; the hero is the only straight-on frontal shot. Looks like CG renders or very controlled tabletop photography (cannot tell at 360p). No people, no hands, no UI except the device's own pixel screen.

Transitions: hard cuts in the dark (black-to-black, so they feel like soft cuts); logo fades out.

Sound: one ambient swell, no beat: -26 LUFS-M at 1 s rising steadily to the peak -12.7 at 18 s (the display chapter), then falling to -24 by 26 s and fading to silence by 32 s. Integrated -18 LUFS (quiet on purpose). No voice.

What makes it premium:
- Reveal by light: you never see the full product until 21 s.
- Monochrome discipline: one green LED is the only colour in 34 s.
- No claims, no specs - the description carries the copy, the film carries the mood.
- One long sound arc (crescendo/decrescendo) instead of hits.

Recipe (real footage + HTML/GSAP):
1. Shoot (or render) the product on black with one moving strip light; 5-6 macros of edges, keys, LEDs, screen; one frontal hero with a floor that the light can rise on.
2. Edit 2-4 s per macro, 6-7 s for the hero, hard cuts.
3. In HTML: video layers on `#000`; add a light sweep with a masked gradient: `background:linear-gradient(100deg,transparent 40%,rgba(255,255,255,.18) 50%,transparent 60%)`, `mix-blend-mode:screen`, GSAP `backgroundPosition:"-100% 0" -> "200% 0"` over 3 s `power1.inOut`.
4. Hero light-up: animate a floor glow `radial-gradient(ellipse at 50% 100%, #9a9a9a 0%, #000 60%)` from `opacity:0 -> 1` over 4 s.
5. Logo card: thin sans (e.g. Inter 300), `font-size:8vh`, light grey #d0d0d0, fade in 0.4 s, hold 1.2 s; brand mark 2 s; fade to black 1.5 s.
6. Sound: one pad/drone swell, peak at ~55 % of the runtime, integrated about -18 LUFS.
