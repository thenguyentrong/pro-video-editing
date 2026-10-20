# You Got This  (adidas, 2024-02-11, 1:28, 16:9 with 4:3 pillarbox section, YouTube @adidas)
URL: https://www.youtube.com/watch?v=FzaS0V_FCrI
Purpose: brand anthem (global "You Got This" platform launch)
One-sentence point: Pressure is real, but it is "only" pressure: play anyway, and enjoy it.

## Structure
- 0.0-2.0 adidas performance logo (white, ≈20 % of frame height) over the first B&W shot of young players.
- 2-33 **Pressure world**: black-and-white, 4:3 pillarbox (picture 1.33:1, black bars left/right). Non-famous young athletes before a game: faces, waiting, a referee, a girl breathing in a gym, a boy in goal. Slow faces, many looks into the lens. Longest shot of the film 7.6-11.7 s (4.1 s). No voice.
- 33.0 **The switch**: hard cut to full-frame colour on the same girl (now in colour, basketball gym). A 0.4 s audio drop-out at 33.4 then the biggest rise of the film at 34.75 s.
- 35.9-82 **Litany**: voice-over in short "It's only ..." lines (one line = one idea, 1-5 s each). Picture: pros and amateurs mixed - boxing, basketball, rugby haka, volleyball, tennis, a football archive moment, a breakdancer, BMX, gymnastics, cricket, ice climbing. Densest 50-60 s (17 cuts per 10 s), shortest shots 0.12-0.16 s at 58-59 s.
- 77-84 return to the opening characters, now playing and laughing.
- 84.3-85.8 end card: "YOU GOT THIS" in spaced serif caps on black (1.5 s).
- 85.8-88.0 adidas logo on black; last 1.3 s silent.

## Cut rhythm
- 95 shots in 88 s. ASL 0.93 s, median 0.68 s, 67 % under 1 s, 65 shots per minute.
- ASL per quarter 1.69 / 0.73 / 0.71 / 0.92 s: slow B&W first quarter, then it doubles in speed at the colour switch.
- Cuts per 10 s: 5, 6, 15, 9, 13, 17, 13, 13, 3.
- Longest 4.08 s (7.6 s, B&W portrait), 3.74 s (84.28, end card), 2.92 s (79.08). Shortest 0.12 s (58.28).
- Cuts on audio onsets 18 % vs 15 % chance: cut to the voice and the action, not to the beat.

## Typography
- No supers in the film. Only the end card.
- End card: serif caps (closest free: Libre Caslon Text / EB Garamond, regular weight), white on black. 3 lines of 2-4 letters, each letter set on a wide grid so the words read as a block of letters: cap height ≈10 % of frame height, block ≈44 % of frame width, line pitch ≈34 % of height. Hard on, held 1.5 s, then the logo.

## Colour/grade
- First 33 s: neutral B&W, soft contrast, light grain, 4:3 pillarbox.
- From 33 s: full colour, natural, bright, slightly warm; sports-broadcast and archive clips graded to the same warmth.

## Camera/shots
- B&W part: close portraits, faces looking into the lens, low angles on kids, wide empty pitches at night.
- Colour part: mix of staged hero shots, real broadcast/archive moments and phone-style shots; top-downs on courts; one slow motion on a fall.

## Transitions
- Hard cuts everywhere. The only "transition" is the format change (B&W 4:3 to colour 16:9) at 33 s, done with a hard cut and an audio drop.
- Soft dissolve from the end card to the logo (≈85.8 s).

## Sound
- First third: music bed, no voice. Voice enters at 35.9 s and runs as a litany to 82 s.
- Section loudness 0-33 s -13.9 LUFS, 34-85 s -13.4 LUFS (the energy change is in the picture, not the level).
- Integrated -13.7 LUFS, LRA 3.9 LU, true peak -1.4 dBTP. Drop-out 0.4 s at 33.4 s before the colour switch, then the biggest rise of the film (34.75 s). Final 1.3 s silent under the logo.

## What makes it premium
- One device (pressure world vs play world) carried by format: B&W 4:3 vs colour 16:9.
- Real people first, stars later and mixed with amateurs, all the same weight.
- Calm first third (median > 1 s) makes the fast second half feel like release.
- End card is pure type, no claim, no CTA.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Two layers: `.pressure {filter: grayscale(1) contrast(.95); clip-path: inset(0 12.5%)}` (4:3 inside 16:9) for 0-33 % of runtime; `.play` full frame colour.
- First part: 10-12 portraits at 1.5-4 s each; second part: 60-70 action clips at 0.3-0.8 s, densest just after the middle.
- At the switch: `gsap.to(music, {volume: 0, duration: .05}, tSwitch - .4)`, real-sound hit at `tSwitch + 1.3`.
- End card: three lines, `font-family: 'Libre Caslon Text'; font-size: 10vh; text-transform: uppercase`, each letter in its own grid cell (`display: grid; grid-template-columns: repeat(3, 1fr); width: 44vw`), hard on, hold 1.5 s, dissolve 0.3 s to the logo, 1.3 s silence.
