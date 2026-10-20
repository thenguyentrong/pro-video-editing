# Milano Cortina 2026 Opening Ceremony Highlights  (Olympics, uploaded 2026-02-08, 59.9 s, 9:16, YouTube Shorts / Olympics channel)
URL: https://www.youtube.com/shorts/fXYPMo3vFw0
Purpose: social highlight package of a live broadcast event (the ceremony) — vertical re-cut of the host broadcast feed
One-sentence point: the whole ceremony in one minute, in running order, from the first song to the rings in fire.

Structure (times from metrics.json):
- 0.0–6.4 HOOK: a star performer singing, one 6.4 s shot (the longest), centred vertical crop.
- 6.4–19.4 SHOW: dancers with wings, the host flag raised, a second singer (one 5.1 s shot).
- 19.4–27.0 RINGS: dark stadium, then the Olympic rings lit in pyro over the field (the visual peak, 21–26 s), loudest section (−17 to −19 LUFS momentary).
- 27.0–38.0 PARADE: flag bearers, athletes taking selfies, the field filled with flags (wide reframed).
- 38.0–48.5 PROTOCOL: a speech at the lectern, torch bearers, a tenor, flag at the mast; quickest cutting (8 cuts in 40–50 s).
- 48.5–59.9 CAULDRON: the cauldron lights, landmark fireworks, rings in fire to end; no end card.

Cut rhythm: 28 shots in 59.9 s, ASL 2.14 s, median 1.82 s, 18 % under 1 s, 28 shots/min. ASL per quarter 2.14 / 2.49 / 2.14 / 1.36. Cuts per 10 s 4, 3, 4, 3, 8, 5: calm and even, a little faster at the end. Cuts on audio onsets 4 % vs 12 % chance: cut to the event's beats (moments), not to music. Adaptive and scene detectors agreed.

Typography: none. Only the rings as a small white corner bug (top-right, ≈10 % of frame width, ≈2 % margin) on every shot. No captions, no names, no title, no end card.

Colour/grade: the host broadcast's colour untouched: deep blue-black night stadium, warm pyro orange, white costumes; the flag's green-white-red is the only strong colour besides fire.

Camera/shots: the host feed reframed to 9:16 (centre crops of 16:9 broadcast cameras; wides become narrow strips with lots of crowd top and bottom); close-ups of performers, aerial-like high wides of the field, handheld athlete shots.

Transitions: hard cuts only.

Sound: live ceremony audio (songs, crowd, music), no added music bed or voice-over measured as separate. Integrated −23.2 LUFS, LRA 4.7 LU, true peak −6.6 dBTP; momentary −17 to −26; peak at 21–25 s on the rings. Not verified by listening.

What makes it premium:
- Restraint: the event is the spectacle, so the edit adds nothing but order and selection.
- Chronological order keeps it honest and easy to follow; one moment per beat.
- The brand bug is the only graphic; the rings also appear inside the event (pyro), which is the real brand moment.

Recipe (licensed event footage + HTML/GSAP, Hyperframes):
- Pick 25–30 moments in running order; hold the opening and the peak moment 5–6 s, everything else 1–2.5 s.
- Reframe 16:9 to 9:16 with a keyframed crop that follows the subject (`object-position` animated, or a GSAP `x` on a 3.16× scaled video).
- Bug: white SVG mark 108 px wide at 1080×1920, `top:2%; right:3%`.
- Keep the original live sound, normalise to ≈−23 LUFS (or −14 for platforms that do not normalise), no added music.
