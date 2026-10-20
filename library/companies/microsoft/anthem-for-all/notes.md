# "Anthem for All" | A hands-free music anthem for the Invictus Games  (Microsoft, 28 Apr 2022, 3:05, 16:9 with 2.39:1 letterbox, YouTube @Microsoft)
URL: https://www.youtube.com/watch?v=jHTXujh19RA
Purpose: human demo / short documentary (accessibility technology)
One-sentence point: wounded veterans who can no longer play instruments write and record the Games' anthem with eye-gaze and adaptive controllers - and hear it played at every medal ceremony.

Analysed at 360p (YouTube only served format 18 that day); cuts and loudness are reliable, text sizes ±0.5 % H.

## Structure (cut times from metrics.json, adaptive detector)
- 0-39.8 s (22 %) backstory: window light with a tiny caption, then archive photos of a young soldier as small insets on black (not full frame), a burning vehicle, a hospital photo, a burned hand; cut to the man today (slow push on his profile), the interview with a lower third, his scarred hand resting on a table. Interview voice from 2.4 s.
- 39.8-69 s (16 %) the challenge: 29 s of black with small centred text cards that build line by line (what the foundation and the project set out to do) - the longest "shot" of the film, with music thinning to near silence (2.9 s silence at 60.75 s).
- 69-96 s (15 %) the method: a studio building, a recording room, close-ups of large round adaptive buttons and an eye-gaze tablet with coloured circles; the veteran plays notes by looking and pressing; interview cut-ins.
- 96-127 s (17 %) second and third stories: archive inset photos again, a woman veteran in the studio, a music producer with them, faces in close-up.
- 127-148 s (12 %) making the anthem: eye close-up, the on-screen instrument UI (coloured drums labelled with notes), producer at the desk, a singer in headphones; cuts get faster (7 per 10 s).
- 148-174 s (14 %) payoff: the Invictus Games in the real arena - flags, wheelchair athletes, medal ceremonies, the anthem playing; hugs and raised hands.
- 174-184.7 s (6 %) end: "When everybody plays, we all win" on black, Microsoft logo, Invictus Games logo.

## Cut rhythm
- 58 shots in 184.7 s, ASL 3.18 s, median 2.2 s, 10 % < 1 s, 33 % > 3 s, 19 shots/min.
- ASL per quarter 4.62 / 6.60 / 2.43 / 1.85 s: very slow first half (interview, 29 s text section), then a steady speed-up to the arena montage.
- Cuts per 10 s: 1 / 3 / 3 / 2 / 0 / 0 / 1 / 3 / 1 / 4 / 3 / 4 / 3 / 7 / 7 / 7 / 6 / 2 / 0.
- Longest: the black text section 29.3 s (39.8 s), end cards 10.9 s, a studio take 9.1 s.
- The scene detector found only 34 shots in the dark, letterboxed footage; the adaptive detector's 57 cuts were checked on the sheet.
- Cuts on music onsets 12 % vs 20 % chance: cut on speech, not on the beat (documentary).

## Typography
- Microsoft's Segoe UI family. Closest free: **Selawik** (Microsoft's open Segoe fallback) or **Open Sans**.
- Lower third: name in bold caps cap ≈2.3 % H + rank/role in small caps ≈1.5 % H, white, left at x ≈9 % W, y ≈73 % H (inside the picture area, above the letterbox), held ≈3 s.
- Text cards: Segoe UI regular, cap ≈2 % H (very small), white, centred, 2-3 lines; each new line fades in (grey → white) while the earlier lines stay; 3-4 cards in 29 s.
- End line: Segoe UI Light, cap ≈3.75 % H, centred on black, sentence case without a full stop, ≈3 s; logos small (≈5 % H) centred.

## Colour / grade
- Documentary naturalism, low key (mean luma 0.17): warm wood studios, window light, green garden; skin tones protected.
- 2.39:1 letterbox (picture ≈75 % of frame height) for all new footage; archive photos smaller, as framed insets on black; the arena payoff in bright saturated colour (flags, stage lights).

## Camera / shots
- Interviews on a long lens with shallow focus, slow push-ins on faces; macro close-ups of hands on adaptive buttons and of an eye; real screen of the eye-gaze music app; handheld studio coverage; real event footage at the end.
- The technology is shown only in use, never as a product shot.

## Transitions
- Hard cuts; slow fades to and from the black text section; archive insets cut on black. No graphic transitions.

## Sound
- Interview voices carry the story (≈220 words in 185 s, several speakers), then the anthem itself becomes the soundtrack.
- Integrated −19.2 LUFS, LRA 10.2 LU, true peak −1.0 dBTP (broadcast-documentary level, quiet for web).
- Silences: 0.55 s at 58.7 s, 2.9 s at 60.75 s (inside the text section), 0.8 s at 68.45 s; then the music returns +36.3 dB at 63.85 s and +31.9 dB at 65.6 s. Loudest 159 s (arena).

## What makes it premium
- The people and their loss come first; the technology appears only when it gives something back.
- Archive photos as small insets on black: honest, not dramatised.
- A long, quiet black text section is the turn of the story; the music comes back after a near-silence.
- The payoff is real: the anthem heard at real ceremonies.

## Recipe (real footage + HTML/GSAP)
- Interviews (long lens, window light), hands macros on the device, one eye close-up, real screen captures, real event footage. Archive photos: `width: 64%; margin: auto` on black inside the letterbox.
- Letterbox: picture area 2.39:1 (`height: 75%` centred) for all new footage.
- Lower third: `.name{font:700 2.3vh Selawik; text-transform:uppercase} .role{font:400 1.5vh Selawik}`, `left:9%; top:72%`.
- Text card: `font: 400 2vh Selawik; text-align:center`, lines fade in one by one (0.6 s each, 1.5-2 s apart), 7-9 s per card.
- Pace: ASL 4-6 s in the first half, ≈2 s in the payoff; 25-30 s quiet text section at ≈25 % of runtime.
- Mix: dialogue-led at ≈ −19 LUFS for documentary (≈ −16 LUFS for social); 2-3 s near-silence before the music returns.
