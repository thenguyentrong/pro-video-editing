# RESIDENT EVIL | Official Teaser Trailer  (Sony Pictures, 30 Apr 2026, 113.2 s incl. 7.1 s silent end card, 16:9 file / 2.39:1 picture and cards, YouTube)
URL: https://www.youtube.com/watch?v=SJPu1spHqfk
Purpose: teaser (first footage of a game adaptation, about 4.5 months before release)
One-sentence point: a lonely night delivery in the snow turns into something very wrong, from the director of two hit horror films.

## Structure (beats with timestamps; % of 113.2 s)
- 0.0–14.1 **quiet cold open (12 %)**: a figure walks through snow toward a lit house at night (3.1 s), a porch, a door, a dark interior, a living room under one lamp (ASL 2.8 s). Sound at −28…−50 dBFS RMS with single knocks and creaks (+20…+34 dB rises).
- 14.1–19.5 **three studio logos** (Sony, Columbia, Constantin; 5.4 s, at 12–17 %).
- 19.5–45.9 **the phone call, ≈26 s in three shots**: a window (3.8 s), then **one 16.7 s take** of a young man on a wall phone, then 5.9 s from the reverse side. The director credits are printed in red **inside the shot**: "FROM THE MIND OF / ZACH CREGGER" (21.5–23.2), "THE DIRECTOR OF / WEAPONS" (26.8–31.5), "AND / BARBARIAN" (36.5–40). Voice low (−21…−35 dBFS).
- 45.9–63.5 black dip (46.0–47.4), then the night: snow, a fence, a barn, a gun case, a gas mask, a body on the ground (ASL ≈1.1 s, the densest stretch: 8 cuts per 10 s at 50–60 s and 70–80 s).
- 63.5–72.7 low-key shots in a cellar and the dark: a lamp, the man sitting up (3.6 s), a figure in blue light, a flashlight, a pale creature (2.4 s).
- 72.7–82.4 **tagline in three red cards between shots**: "THIS / SEPTEMBER" (1.6 s, 64 %), "COMES A / NEW ERA" (1.6 s), "OF EVIL" (1.7 s), with 0.7–1.6 s shots between them.
- 82.4–94.1 escalation: flashlight in a snowy field, a red-lit face, the man screaming up, a street of burning cars (ASL ≈1.6 s).
- 94.1–96.6 black (2.5 s).
- 96.6–101.4 **title** "RESIDENT EVIL" fades up from dark red to full red (4.8 s, at 85 %; 91 % of the 106 s with sound), on the last hit (+18.1 dB at 96.3).
- 101.4–103.4 writer/director credits (2.0 s). 103.4–106.1 date "09.18.26" + logos (2.75 s), sound fades out.
- 106.1–113.2 static poster end card in digital silence (7.1 s).

## Cut rhythm
- 46 shots (adaptive detector + 4 dark cuts found by eye). **ASL 2.46 s**, median 1.58 s; without the silent end card ≈2.3 s.
- ASL per quarter 3.14 · 3.14 · 1.35 · 2.83 s (the slow phone scene sits in Q1–Q2).
- 15 % of shots under 1 s, 22 % over 3 s. 24.4 shots per minute. Longest story shot 16.7 s.
- Cuts per 10 s: 3 4 1 1 2 8 6 8 5 4 3 0. Cuts on audio onsets 24 % vs 21 % chance.
- Speech in ≈87 s: one long conversation carries the first half.

## Typography
- Two systems, both from one face: ultra-condensed heavy caps with a cracked, vein-like texture (closest free: Anton, with a crack mask).
- **Red cards**: pure red (#e00000) inside the letterbox, black type ≈30 % H per line, 1–2 words per line, centred; hard cut in and out, 1.6–1.7 s.
- **Credits over picture**: red type over the long take, small wide-tracked lead line ≈3 % H, name ≈12 % H, centred slightly low; fade in/out ≈0.5 s, hold 1.7–4.7 s.
- Title ≈33 % H, spanning 12–90 % W, fades up through dark red over ≈1.5 s. Date card in red type on black.

## Colour / grade
2.39:1 everywhere. Cold blue-black snow nights, warm tungsten interiors with one lamp, a few blue and red accents; the brand red is reserved for cards and the title.

## Camera / shots
Locked or slowly drifting long takes, a human-scale POV, very low-key frames where most of the picture is black; creature shown only in pieces.

## Transitions
Hard cuts; dips to black at 14.1, 46.0 and 94.1 s; credits and title fade.

## Sound
- Integrated **−17.9 LUFS** (quiet, like the art-house trailers), LRA 12.1 LU, true peak −1.7 dBTP.
- First 14 s near −40 dBFS with single sounds; the call at −21…−35; from 60 s a steady bed at −16…−20 dBFS; no big wall of music.
- No pre-title silence: 2.5 s of black at −20…−28 dBFS, then the title hit; the end card is fully silent.

## What makes it premium
- One 16.7 s take of a phone call is the heart of a horror teaser: patience creates dread.
- The director credits live inside the scene in the brand red, so the "who made it" claim costs no screen time.
- The brand red is a system: tagline cards, credits, title, date.
- Quiet mix: the scares come from contrast, not from loudness.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Bars 138 px (2.39:1) on everything, cards included.
2. 0–14 s: 4–5 night shots of 2–5 s at −40 dBFS with single sound effects; then logos.
3. One 15–20 s held dialogue take; overlay two credits: `.lead{font:400 22px Anton; letter-spacing:.4em}` `.name{font:400 130px Anton}` `color:#e00000`, fade 0.5 s, hold 2–4 s.
4. Tagline split over three cards: `background:#e00000; color:#000; font:400 300px/0.95 Anton; text-transform:uppercase`, add a crack texture with `mask-image` (a licensed or self-made crack PNG), hard cuts, 1.6 s each, a 1 s shot between them.
5. 2.5 s of black, then title fade from `#3a0000` to `#e00000` in 1.5 s, hold 3–5 s; credits 2 s; date 2.75 s.
6. Master around −18 LUFS for a horror teaser (or −14 for a loud cut), true peak −1.5 dBTP.
