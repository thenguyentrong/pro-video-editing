# Scrub Daddy's Morning Routine  (Scrub Daddy, 2025-04-04, 22.5 s, 9:16, YouTube Shorts / TikTok)
URL: https://www.youtube.com/shorts/iGEFKEuwRCw
Purpose: social persona post (mascot as a creator)
One-sentence point: The smiley sponge does a "day in my life" morning-routine video, from mouthguard at 3:52 am to a banana breakfast at 8:45 am.

Structure: beats with timestamps
- 0.0-2.3 hook: the sponge on a stand wearing a mouthguard, clock-time caption already on screen. The format (routine vlog) is clear in 1 s.
- 2.3-12.8 routine: toothbrush, face macro, drink of water, sparkling-water pour, dunk. Each step is a new clock time.
- 12.8-16.2 the longest shot (3.4 s): bath in a tiny pink tub.
- 16.2-22.1 breakfast: banana, then the sponge "eats" it (fast push-in, motion blur).
- 22.1-22.5 outro: four 0.1 s inverted-colour glitch frames, then the loop restarts.

Cut rhythm
- 21 shots (17 edits + 4 glitch frames), ASL 1.07 s, median 1.03 s, 43 % < 1 s, ≈56 shots/min. Quarters 0.94 / 0.94 / 1.41 / 0.70 s: fast, one slower bath beat, fastest at the end.
- 40 % of cuts on audio onsets vs 28 % chance: loosely on the beat.

Typography
- Only the clock time ("3:52 am" ... "8:45 am"): white lowercase sans, cap ≈1.7 % H, soft shadow, no box, centred at ≈50 % H, changes per step (6 different times). Closest free: TikTok Sans 500 or Inter 500.

Colour/grade
- Purple/blue LED light (club-like) with magenta accents; the yellow sponge pops against it. Phone camera, clipped highlights accepted.

Camera/shots
- Handheld phone macros at the sponge's eye level; props in miniature (tub, stand, bottle). The sponge is staged as a person (POV, close-ups on its "face").

Transitions
- Hard cuts; one inverted-colour glitch burst as the outro (loop point).

Sound
- Trending track; -12.0 LUFS, peak +1.1 dBTP. Short music pauses (0.3-0.65 s) at 7.3, 12.75 and 16.5 s for small gags (a "huh?" voice at 12.4 s). Rises of 100+ dB are from digital silence.

What makes it premium
- A platform format (routine vlog) performed by the product with a face: no need for a person.
- One caption type that tells the story (time passing).
- Strong colour idea (yellow on UV purple) that makes every frame recognisable.

Recipe (real footage + HTML/GSAP, 1080x1920)
- 20-25 s; 15-20 shots of 0.5-2.3 s, one 3-3.5 s "comfort" shot at ≈60 %.
- Clock caption `500 40px "TikTok Sans"; color:#fff; text-shadow:0 2px 6px rgba(0,0,0,.5)`, centre y ≈960 px, `tl.set` per step.
- Outro glitch: 3-4 frames of `filter: invert(1) hue-rotate(90deg)` alternating with the last frame, 0.1 s each, then cut to frame 0.
- Light: purple/blue LEDs (#5A1BFF / #C21BFF) behind, white key on the product.
