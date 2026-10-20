# EXIT 8 | Final Trailer  (NEON, 8 Apr 2026, 84.1 s, 16:9 file / 1.85:1 picture, YouTube)
URL: https://www.youtube.com/watch?v=zzEDWwhtAHc
Purpose: final trailer for the US release of a Japanese horror film (2 days before release); sells critics' praise
One-sentence point: a man is trapped in an endless subway corridor and must spot what is wrong to get out, and critics call it horrific and entertaining.

## Structure (beats with timestamps; % of 84.1 s)
- 0.0–2.0 **festival laurel inside a shot** (a subway door with an official-selection notice).
- 2.0–3.7 **NEON logo** in yellow on black (an "0" counter that becomes the word), 1.7 s, at 2 %.
- 3.7–14.2 **the rules**: black, a crowd, the white-tiled corridor, the man walking, a passer-by, locked doors (ASL ≈0.8 s), hits up to −6.6 dBFS at 12.3.
- 14.2–20.6 three held corridor shots of 2.6–3.4 s, the music falls to −45 dBFS.
- 20.6–23.2 **press quote typed letter by letter** on black (2.6 s, at 25 %); a 0.7 s drop-out at 22.85 (floor −53 dBFS).
- 23.2–27.6 two reaction shots (2.2 s each). 27.6–30.0 **second quote**, typed (2.3 s, at 33 %).
- 30.0–36.5 **strobe run**: 16 shots in 6.5 s, eight of them 0.12–0.29 s (corridor, the exit sign, a pile of debris).
- 36.5–46.3 a schoolgirl, a body on the floor, 1.8 s of black with only a subtitle, the girl again (one 7.3 s span with a black hold inside).
- 46.3–61.3 **montage at ≈0.5 s per shot** (densest 50–60 s, 21 cuts per 10 s = 59–71 %): a child running, a monster face flash, a laughing man, a flooded ceiling, loudest moment −8.2 dBFS at 60.8.
- 61.3–63.5 **title card**: "8番出口 / Exit 8" in black on full yellow (2.2 s, at **73 %**), after a 0.55 s silence.
- 63.5–74.2 **one 10.8 s take**: the man at a wall of lockers; **3.3 s of digital silence** (67.6–70.9, −78 dBFS), then a +67.8 dB rise at 73.55 (rise from silence, so the number only means "from nothing to full").
- 74.2–78.0 **third quote typed over the picture** (3.75 s), 78.0–79.75 the man screaming in the corridor.
- 79.75–84.1 **yellow end card** "IN THEATERS / APRIL 10", the yellow fades down to dark over 2 s, sound fades out.

## Cut rhythm
- 77 shots (adaptive detector; the scene detector suggests 3 extra cuts at 40.2 and 58.6–58.8 that were not added). **ASL 1.09 s**, **median 0.58 s**.
- ASL per quarter 1.11 · 0.91 · 0.66 · 3.50 s: very fast until the title, then one long take.
- **70 % of shots under 1 s**, 6.5 % over 3 s. 54.9 shots per minute. Shortest 0.12 s (three in a row at 35.4 s).
- Cuts per 10 s: 9 8 5 18 6 21 5 4. Cuts on audio onsets 34 % vs 24 % chance.
- Dialogue is Japanese with small English subtitles (bottom centre, ≈2 % H); the English speech detector is not usable here.

## Typography
- Three systems, all yellow and black (the film's exit-sign colours):
  - **Press quotes**: monospace caps (closest free: Space Mono or IBM Plex Mono), yellow #fdfe5a, ≈4.5 % H cap, two lines centred at 40–51 % H, outlet name in a small box ≈1.5 % H below. **Typed in one character at a time** (≈10 characters per second), hold ≈1 s, hard cut out.
  - **Title**: the sign itself: black bold sans (closest free: Noto Sans JP Black + Inter Bold) on full-frame yellow #ffe600, number "8" ≈40 % H.
  - **End card**: small monospace "IN THEATERS" ≈2 % H over "APRIL 10" ≈4 % H in black on yellow.
- The third quote is typed **over the live picture** (no plate).

## Colour / grade
1.85:1 picture. Cold, flat, fluorescent white-green corridor; only the signs are saturated (yellow). A few warm or pink inserts (monster, flooded ceiling).

## Camera / shots
Symmetrical one-point corridor views, over-the-shoulder walking shots, locked reaction close-ups; the horror is shown in 0.1–0.3 s flashes.

## Transitions
Hard cuts; black holds at 3.7, 20.6 and 40.6 s; the end card fades down.

## Sound
- Integrated **−12.3 LUFS** (the loudest trailer in this set), LRA 13.6 LU, true peak +1.4 dBTP.
- Body very loud (−8…−12 dBFS RMS in the montage), so the **silences are deep**: 0.55 s before the title, 3.3 s inside the locker take, then 1.0 s and 0.6 s gaps, then the final hit.
- The title comes after the loudest stretch, on a cut to silence, not on a hit.

## What makes it premium
- The film's own sign is the type system: yellow and black, monospace, numbers.
- Critics' quotes typed like a terminal, so the praise feels like part of the puzzle.
- Very fast flashes (0.12 s) against one 10.8 s take with 3.3 s of total silence.
- Title at 73 %, then a scare and a quote: the trailer keeps going after the title.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Bars 9 px top and bottom at 480p (1.85:1: 21 px at 1080) or none.
2. Festival laurel shown inside a real shot; distributor logo 1.7 s.
3. Quotes: `font: 700 48px "Space Mono"; color:#fdfe5a; text-transform:uppercase; text-align:center` on `#000`; type them with `tl.to(span,{opacity:1,duration:0},t+i*0.1)` per character; outlet name in a 1 px yellow box below. Hold 1 s after the last letter.
4. A strobe run of 0.12–0.3 s shots, then a 15 s montage at 0.5 s per shot, mixed at −9 dBFS.
5. Cut to silence (0.5 s), then a full-yellow title card 2.2 s: `background:#ffe600; color:#111; font:900 380px Inter`.
6. One 10 s take with 3 s of total silence, a hit, one more quote over the picture, then a yellow date card fading to black in 2 s.
7. Master −14 LUFS (the original is −12.3 with true peak +1.4 dBTP; do not copy that).
