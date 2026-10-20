# Shot on iPhone 18 Pro: "new trick" by ROSÉ  (Apple, 2026-09-18, 0:35 file / 0:30 content, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=1WLqGs7c_yA
Purpose: "Shot on iPhone" ad = music-video cut-down (co-branded end card with T-Mobile)
One-sentence point: A real pop music video was shot on iPhone 18 Pro — proven by cutting the performance with behind-the-scenes shots of the iPhone in its rig.

## Structure
- 0-2.5 s **Hook**: guitar strums; fisheye wide of ROSÉ singing in a gym/ballroom with a band.
- 2.5-16 s **Verse**: close-ups, a lollipop "new trick" gag (5-6 s), crowd on bleachers, band, **BTS insert of the iPhone in a cage rig (4.1-5.2 s)**, BTS rig on a gimbal (11 s), camera macro (12.6 s), skateboard and top-down shots.
- 16-28 s **Chorus**: fisheye, rig on a crane, through a chain fence, guitar close-up, rig + guitarist, sparks over the band, rig in motion (26.9 s).
- 26.9-28.1 s **Super**: "Shot on iPhone 18 Pro" over the spark-filled performance.
- 28.65-30 s **End cards**: T-Mobile "T" on black → Apple logo on black, then black.

## Cut rhythm
- 24 shots in 30 s → **ASL 1.25 s**, median 1.02 s; quarters 1.88 / 0.75 / 0.94 / 1.50.
- 50 % of shots < 1 s; shortest 0.38 s (11.4 s); longest 3.1 s (23.7 s) and 2.8 s (16.2 s).
- Densest 10-20 s (10 cuts / 10 s).
- Cuts on onsets 30 % vs chance 27 % → near chance; cut to lyric phrases and motion, not every drum hit.
- BTS rig inserts: 4 of 24 shots (≈ 1 in 6).

## Typography
- One super: "Shot on iPhone 18 Pro", white SF Pro Display medium, centred (y ≈ 47 %), cap ≈ 4.5 % H, 38 % of W wide, 1.2 s on screen, no shadow, over busy footage.
- End cards: carrier "T" logo then Apple logo, white on black, ≈ 9-13 % H tall.

## Colour / grade
- Warm golden interior (wood, tungsten, sparks) vs. cool teal exterior (fence, sky) — two-world music-video grade.
- High saturation in costumes (yellow/blue argyle, red/white stripes), crushed blacks, light grain.

## Camera / shots
iPhone in cage rigs on gimbals, cranes and a handheld bar; fisheye/ultra-wide close to the subject; top-down; through-fence; whip pans and fast push-ins. BTS shots show the phone itself as the hero (burgundy iPhone in a silver cage).

## Transitions
Hard cuts only; motion-matched cuts on whips.

## Sound
- The song "new trick" by ROSÉ as the full track; no VO, no added SFX besides the song's intro strums.
- Integrated **−16.0 LUFS**; no drop-outs; song ends around 28.6 s under the end cards.

## What makes it premium
- The proof is built in: BTS rig inserts every ~5 s keep saying "this was a phone".
- Real talent and real production design — the product is the camera, not the subject.
- One quiet, small super instead of a feature list.

## Recipe (real footage + HTML/GSAP)
- Cut the performance at ~1.0 s median (0.4-3 s), fast in the chorus; every 4-6 shots insert a 0.6-1.2 s BTS shot of the phone in its rig.
- Grade interior warm (`sepia(.15) saturate(1.2)`), exterior cool (teal overlay 15 % soft-light).
- Super at the climax: Inter/SF Pro 500, `font-size: 6vh` (cap ≈ 4.5 % H), white, centred; `gsap.fromTo(s,{opacity:0},{opacity:1,duration:.3})`, hold 1.2 s, cut out.
- End: brand logos on black, 0.5-0.8 s each, then 2-5 s black.
