# KUKA KMF 1500P: Autonomous Forklift for Smarter Intralogistics  (KUKA Group, 2026-10-09, 1:59, 16:9, YouTube @KUKARobotGroup)
URL: https://www.youtube.com/watch?v=sJd45wo4N_c
Purpose: product launch film (two forklift AMR variants, 100 % CGI render)
One-sentence point: KUKA's new autonomous forklifts (counterbalance and pallet-stacker versions) move pallets safely and precisely in narrow, dense warehouses, run by KUKA's AMR software.

## Structure
- 0-6.6 hook: long fly-through down a white warehouse aisle towards a forklift, VO starts at frame 1; caption line under it.
- 6.6-12.7 "how": three quick render inserts: lidar head with an orange scan ring ("Intelligent navigation"), orange sensor rays from below ("advanced sensors"), front of the machine ("KUKA AMR software ecosystem").
- 12.7-48.7 variant 1 (KMF 1500P-CB): fork-level POV towards a pallet, lifting to a high rack; product name as a big white title over the shot (23-26 s); feature captions per shot ("Autonomous pallet transport", "Intelligent pallet handling", "Intelligent pallet recognition"); top-down shot with an orange safety field and "Precise pick-up and drop-off", "360° safety in dynamic environments". Dip through black at 33-35 s bridges warehouse → production.
- 48.7-86 variant 2 (KMF 1500P-PS): one 20.1 s aerial fly over a dense block store, product name title at 53-56 s; orange laser grid over racks ("Narrow aisles and high storage density"), lift to second level, two machines side by side, "Respond to growing market demand".
- 86-94.8 hero: both forklifts in a long aisle, closing claim.
- 94.8-98.6 KUKA logo on white, line "making automation easier."
- 98.6-118.6 20 s animated brand ident (orange particles, ring logo) - shared by all current KUKA uploads.

## Cut rhythm
- 17 shots in 118.6 s (16 in the 98.6 s film without the ident). ASL 6.97 s (≈6.2 s without the ident), median 6.40 s, 0 % < 1 s, 65 % > 3 s, 8.6 shots/min. ASL per quarter 4.2 / 9.9 / 4.2 / 9.9 s.
- Longest 20.1 s (48.7 s aerial) and 20.0 s (ident); 13.2 s (27.1 s). Shortest 1.48 s (sensor inserts).
- 0-4 cuts per 10 s; densest in the first 13 s (5 cuts). Many scene changes are hidden in continuous virtual camera moves, so "shots" are long camera journeys, not edits. The scene detector misses the 33-35 s dip and a light-wipe at ≈60 s.

## Typography
- Captions = the VO phrase, humanist sans (KUKA corporate face; closest free: Source Sans 3 or Fira Sans), regular, sentence case, white (black on white backgrounds), ≈4 % H (cap ≈2.7 %), centred, y ≈18 % (top) or ≈80-88 % (bottom); fade in/out with the line, 2-4 s.
- Product title "KMF 1500P-CB / -PS": same face, regular, white ≈7 % H, centred over the moving shot, held ≈3 s.
- End card: KUKA wordmark orange on white ≈7 % H + "making automation easier." grey ≈2.2 %.

## Colour/grade
- Clean, bright CGI: white floor, grey racks, warm cardboard. KUKA orange only as data light (scan ring, sensor rays, laser grid, safety field) and in the logo.

## Camera/shots
- 100 % CGI. Low-angle fly-throughs at fork height, fork POV pushing into a pallet, top-down safety views, aerial over a block store, a slow orbit on two machines. Smooth virtual dolly moves, no handheld.

## Transitions
- Hard cuts plus hidden transitions inside camera moves; one dip through black (33-35 s); fade to the white logo card.

## Sound
- Male VO wall to wall (≈97 s of speech, ≈190 words, ≈1.9 words/s) over a driving corporate electronic track. Integrated -14.8 LUFS, LRA 11.5 LU, true peak +0.8 dBTP (clips). Short drop-outs 0.3-0.45 s at 2.6, 6.3, 12.0 s (between first VO phrases); 2.95 s silence at 97.5-100.5 s between film and ident. Biggest rise +24.8 dB at 36.6 s.

## What makes it premium / credible
- Every feature claim has its own dedicated render shot and the caption repeats the VO word for word.
- Data shown as orange light in space (scan ring, rays, grids), not as overlays on top.
- Weak as proof: no real machine, no real site, no number on screen (payload "1500" only in the name).

## Recipe (HTML/GSAP, Hyperframes)
- Caption bar: `font:400 4vh 'Source Sans 3'; color:#fff; text-align:center; bottom:12vh`; `gsap.fromTo(cap,{autoAlpha:0},{autoAlpha:1,duration:.3})`, change the text with each VO phrase.
- Product title: `font:400 7vh 'Source Sans 3'`, centred, fade 0.4 s, hold 3 s over the moving shot.
- Data light: an SVG ellipse ring (`stroke:#FF5800; stroke-width:6; filter:blur(2px)`) scaled from 0.6 → 1.3 around the sensor in 1 s, opacity 1 → 0.
- If you have real footage, keep this structure but swap renders for real takes and add a "1x" label.
