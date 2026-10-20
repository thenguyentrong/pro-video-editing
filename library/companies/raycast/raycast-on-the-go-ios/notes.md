# Raycast, on the go.  (Raycast, 2025-04-30, 101.1 s, 16:9, YouTube / social)
URL: https://www.youtube.com/watch?v=VXrq58zBdl8
Purpose: launch film (Raycast for iOS, "out now")
One-sentence point: You no longer need the whole desk setup; the phone in your pocket is enough.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-9.2 (0-9 %) hook: a locked-off wide of a designed desk setup (big monitor, arc lamp, glass desk, chair) alone in a warm white cyclorama. Nothing happens for 9 s.
- 9.2-74.5 (9-74 %) the clear-out: a man walks in and carries the setup away piece by piece. A loop of wide (the whole set, he walks in and out) → close-up on the desk (the item lifted out of frame) → wide again. Monitor, lamp, cables, keyboard, computer, accessories.
- 74.5-86.6 (74-86 %) packing: a box on the floor of the empty cyc; he kneels and packs; an overhead insert of the gear inside the box.
- 86.6-90.1 (86-89 %) the empty desk in the wide; the light dims to grey.
- 90.1-95 (89-94 %) payoff: top-down of the near-empty glass desk in low light; a phone screen lights up (the only thing left).
- 95.0-100.9 (94-100 %) end line in two columns over the same shot, then a 0.2 s black tail.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 21 shots (verified on the cut sheet; 2 cuts added from the adaptive detector at 74.5 and 90.1 and checked on 8 fps strips; black tail excluded).
- ASL 4.80 s, median 3.68 s, 0 % under 1 s, 86 % over 3 s. Quarters 5.04 / 4.20 / 2.80 / 6.31 s.
- Shortest 1.9 s (45.4 s), then 2.4-2.6 s; longest 11.1 s (20.6 s, wide of him carrying the monitor away), 10.8 s (final top-down), 9.2 s (opening wide).
- Faster in the third quarter (the small items go quickly), then slow for the ending.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Only one text moment: a wide geometric sans in caps with full stops (closest free: Lexend Exa 400 or Archivo SemiExpanded), white. Cap ≈2.7 % H. Two columns on the centre line: product line left-aligned at x ≈15 %, "OUT NOW." in italic right side at x ≈73 %. 3 + 2 words. Hold ≈5.5 s, appears without motion over the last shot.
- No logo animation, no UI on screen at all.

Colour/grade: palette, contrast, grain, letterbox
- Warm off-white cyc (#c5bfac, #dcd2bc) with soft shadows; teal shirt and green-glass desk (#32484b) as the only colour, a red cable as a small accent.
- Low contrast, slightly faded film look. The ending is graded down to grey-green (#404b44) as the light goes out.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Two locked-off set-ups repeated: a frontal wide (≈35 mm look, subject small, lots of headroom) and a static close-up / top-down of the desk. The performer enters and leaves frame; the camera never moves.
- Deadpan performance, no face to camera, no dialogue.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 20 hard cuts, no effects. The light dimming (≈88-90 s) works as the only "transition".

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Music and Foley (steps, objects), no voice (speech detector found none).
- Biggest rises: +22.3 dB at 94.8 s (just before the end line), +19.1 dB at 29.5 s. Loudest 0.5 s at 95.8 s, on the end line. No drop-outs; 0.55 s silence at the end.
- Integrated −13.8 LUFS, LRA 8.0 LU, true peak +0.2 dBTP.

What makes it premium (3-5 bullets)
- An idea told only with objects: the product (a phone app) appears as one lit screen at 90 %.
- Set design is the brand: a curated desk in a white void, like a furniture catalogue.
- Locked-off frames and long holds (9-11 s) give a gallery calm and dry humour.
- One line of small wide caps at the very end, nothing else.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920x1080, ≈100 s. Shoot two locked-off positions on a white cyc: wide (subject ≈30 % of frame height, desk at the lower third) and a close/top-down of the desk. Repeat the action loop: wide 3-11 s → close 2-4 s → wide.
- Grade: lift blacks, warm whites `#dcd2bc`, saturation ≈70 %; last 10 s fade the key light to 40 %.
- End line: two spans on the centre line, `400 29px "Lexend Exa"` caps, white; left span at `left:15%`, right span italic at `left:73%`; `autoAlpha 0 → 1` over 0.3 s, hold 5.5 s, cut to black.
- Stock queries (if not shooting): "minimal desk setup white studio", "man carrying monitor white background", "packing moving box studio floor", "phone on desk top down low light".
