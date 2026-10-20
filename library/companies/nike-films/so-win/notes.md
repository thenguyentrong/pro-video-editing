# So Win  (Nike, 2025-02-13 upload, 1:00, 16:9, YouTube - NikeHongKong regional channel)
URL: https://www.youtube.com/watch?v=W2VLEmzPC1U
Purpose: ad (Super Bowl LIX anthem spot, women athletes)
One-sentence point: Every "you can't" that is said to women athletes is answered with "so, do it" - and the last one is "you can't win. So win."

Note: this regional upload has burned-in Chinese subtitles (white, ~3 % frame height, bottom centre). They are not part of the global film design; ignore them.

## Structure (times from the cut list + English captions)
- 0.0-4.1 hook: one held shot (longest shot, 4.1 s). Sprinter (Sha'Carri Richardson) crouched behind a white hurdle bar, black void, fingers spread. VO 2.2 s: "You can't be demanding."
- 4.1-12 setup: the pattern is taught. Each "You can't X" = a studio portrait (still, staring), each "So, X" = the same athlete or archive action. Cuts every 1.0-2.0 s.
- 12-42 build: the call/response gets faster. "You can't" lines shrink from ~2 s to ~1 s (12.1, 14.0, 17.7, 20.8 ... 40.3, 41.0). Cuts go from 9 per 10 s to 12 per 10 s.
- 42.1 turn: "Whatever you do, you can't win." Two short audio drop-outs (42.9 s and 44.2 s, 0.35 s each, -48 / -72 dBFS) and a slow-motion gymnast flying horizontally against grey (44.8-46.9 s, the most "floating" shot of the film).
- 50.3-51.1: 0.85 s silence (floor -64 dBFS), then VO "So, win." over real race and game footage (50.1 sprinter 2.2 s, 52.2 bench celebration, 53.4 Clark, 53.9 trophy parade).
- 55.7 end card 1: black, "YOU CAN'T WIN." (1.3 s)
- 57.0 end card 2: "SO WIN." added under it, twice the size (0.9 s)
- 57.8-59.1 one more performance shot (dancer/gymnast at a wall), then 0.9 s black. No swoosh lock-up is shown in this cut.

## Cut rhythm
- 58 shots in 60 s. ASL 1.03 s, median 0.88 s. ASL per quarter 1.67 / 0.83 / 0.88 / 0.88 s.
- Longest 4.13 s (opening), then 2.17 s (50.05, the "So, win" sprint), 2.04 s. Shortest 0.29 s (35.99), 0.46 s, 0.50 s.
- 62 % of shots are under 1 s, only 2 % over 3 s.
- Densest 20-30 s (12 cuts). Cuts follow the voice phrases, not the music: only 16 % of cuts fall on an audio onset (chance would be 23 %).

## Typography
- Only on the end card. Nike's Futura Condensed ExtraBold (closest free: Anton), all caps, white on pure black, tight tracking (about -1 %), period after each line.
- "YOU CAN'T WIN." cap height ~19 % of frame height, spans x 6-96 % (90 % of width).
- "SO WIN." directly under it with almost no leading, cap height ~40 %, set to the SAME width as line 1 (justified block).
- Words per card: 3, then 5. Hold 1.3 s, then 0.9 s. In/out: hard cuts, no animation, no fade.

## Colour/grade
- 100 % black and white, also the archive game footage (they grade everything mono so the archive matches the studio).
- High contrast, crushed blacks in the studio (25 % of samples are "mostly empty dark" frames), single hard key light from above or the side, often a pool of light on a black floor. Fine grain. No letterbox.

## Camera/shots
- Two worlds, intercut: (1) studio portraits on black, mid-shot or close-up, athlete looking into the lens, almost still; (2) real broadcast/archive game footage (WNBA, track, tennis, football, parade).
- Set pieces: chain-link cage (34 s, 40 s), brick wall (36 s), smoke/chalk cloud (15-17 s), spotlight + shadow on the wall (24 s).
- Slow motion only for the bodies in the air: gymnast flying (44.8-46.9 s), dancer at the wall (57.8 s).
- Mostly locked-off camera; movement comes from the athletes, not the camera.

## Transitions
- Hard cuts only (57). soft.py candidates at 0.5 s and 35.2 s are a camera move and a whip-fast movement inside a shot, not dissolves. No dips to black until the very end.

## Sound
- Female rap/spoken VO (Doechii) carries the film; sparse score under it. Integrated loudness -24.4 LUFS (broadcast-level master; quiet for YouTube). Loudest 0.5 s at ~9.3 s (-18.7 LUFS momentary).
- Drop-outs: 42.9 s and 44.2 s (0.35 s each) and 50.3-51.1 s (0.85 s) - silence right before the payoff "So, win."
- Biggest rise: 52.35 s (+21 dB in 0.5 s) - the crowd/game sound after "So, win."

## What makes it premium
- One rhetorical device, repeated 12 times, getting faster - the edit IS the copy.
- Total visual unity: everything mono, archive included.
- Stillness vs. action: still staring portraits make the action shots hit harder.
- Silence before the payoff line, then real crowd noise.
- End card is huge, plain, no motion - confidence.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Footage: alternate "portrait on black" (subject still, looking at lens, 1 hard light) with real action. Grade all clips the same: CSS `filter: grayscale(1) contrast(1.3) brightness(0.92)` on every `<video>`; add a 3 % opacity grain PNG overlay with `mix-blend-mode: overlay`.
- Script the VO first as "You can't X. / So, X." pairs; cut on every phrase start (not on beats). Start pairs at ~2.0 s each, compress to ~1.0 s by the last third. Target ASL 1.0 s for a 60 s spot, first shot held 4 s.
- Before the payoff line: duck music to silence for 0.35-0.85 s (`gsap.to(music, {volume: 0, duration: 0.05})`), then hit the line with real ambient crowd sound.
- End card: `<div>` black, `font-family: Anton; text-transform: uppercase; color: #fff; letter-spacing: -0.01em; line-height: 0.88`. Line 1 `font-size: 19vh`, line 2 `font-size: 40vh`, both scaled to 90 % width (fit-text). Show line 1 with a hard cut (`gsap.set(card, {autoAlpha: 1})`), add line 2 1.3 s later with `gsap.set`, hold 0.9 s, cut back to one 2 s action shot, end on 0.9 s black.
