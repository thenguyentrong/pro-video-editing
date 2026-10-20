# "The biggest stage in basketball": NBA Finals begin tonight  (NBA on ESPN, uploaded 2026-06-03, 80.7 s, 16:9, YouTube / NBA on ESPN channel, 720p upload)
URL: https://www.youtube.com/watch?v=sAdGK-qXziw
Purpose: event promo / base version of the Finals graphics package (the game-day opens such as espn/nba-finals-2026-g5-intro are versions of it)
One-sentence point: the Finals are a golden stage where every era of champions plays at once, and the stage opens tonight.

Structure (times from metrics.json):
- 0.0–7.0 HOOK: the same gold CG open as the Game 5 intro (ring, liquid-gold sculpture, gold logo, "Finals" script in particles).
- 7.0–17.9 ARCHIVE IN GOLD: archive champions inside gold portholes and frames, then full-frame current action with gold particle bursts (a dunk at 15 s gets a spark burst).
- 17.9–48.0 CG VAULT: three very long continuous CG moves (9.1 s, 8.4 s, 10.6 s): archive on curved vault screens, a glass globe with a current star inside, a particle explosion that reveals the wordmark on a gold floor.
- 48.0–75.4 GOLD STAGE: legends from different eras are cut out (rotoscoped) and placed together on one CG gold court with light rays, falling sparks and the wordmark in the background: 1980s rivals, then 2010s stars, then 1990s and 2000s icons; shots 0.4–7 s.
- 75.4–80.7 LOCKUP 5.2 s: trophy on a gold stage with light fans, "Finals" wordmark in gold before it.

Cut rhythm: 34 shots in 80.7 s, ASL 2.37 s, median 1.15 s, 47 % under 1 s but 26.5 % over 3 s (the long CG moves). ASL per quarter 1.26 / 5.04 / 2.24 / 2.52; cuts per 10 s 10, 5, 1, 2, 1, 7, 3, 4: fast hook, a 30 s slow CG valley, then a medium "stage" section. Adaptive detector (gold haze and particles hide cuts); the scene detector found one extra candidate (77.2 s) inside the lockup move. Cuts are not on onsets (6 % vs 8 % chance).

Typography: none except the gold 3D script wordmark (≈20–25 % of frame height) and the league logo; a small "Finals" wordmark also appears as a set element in the background of the stage shots. No date or channel on this upload (the YouTube title carries the tune-in).

Colour/grade: the same one-material world as the Game 5 intro: gold on black, archive and current footage warmed to gold, bloom, light rays from above, sparks. Every frame shares the palette, even 1980s tape.

Camera/shots: CG fly-throughs; archive composited on CG surfaces; rotoscoped players on a virtual gold court with a slow camera drift and parallax sparks; a back view of a hero player with arms spread and sparks rising (73–75 s) as the climax image.

Transitions: moves through CG geometry and particle bursts; hard cuts inside the stage section. No dissolves to black.

Sound: broadcast level again: integrated −23.8 LUFS, LRA 4.1 LU, true peak −10.4 dBTP; momentary max per second −18 to −27 throughout, loudest 0.5 s at 11.8 s (early, in the archive section), small rise at 43–47 s (the particle explosion). Steady, no drop-outs. Voice-over not verified (I did not listen).

What makes it premium:
- A package, not a one-off: hook, wordmark build and trophy lockup are identical across the base promo and each game open; only the middle changes.
- "All eras on one stage": rotoscoped legends share one virtual court, which tells the history story in a single image.
- Long CG moves (8–11 s) give the piece a calm, expensive feel inside a sports promo.

Recipe (real or licensed footage + HTML/GSAP, Hyperframes):
- Build the package once: a 7 s hook, a 5 s lockup, a gold "stage" background plate; swap only the middle per version.
- Stage shot: rotoscoped player clip (alpha WebM/ProRes 4444) over a gold court plate; behind them a blurred wordmark at 30 % opacity; light rays = 5 `linear-gradient` beams (`rgba(255,200,120,.35)`, `blur(12px)`, rotate −20°…20°); sparks canvas (300 particles, 1–4 px, `#ffd27a`, fall 40–90 px/s); parallax: plate `x -2%`, player `x +3%` over the shot.
- Rhythm: 7 s fast hook → 10 s archive (≈1 s) → 25–30 s of 3 long CG moves → 25 s stage section (0.5–7 s shots) → 5 s lockup.
- Mix at −24 LUFS for TV; keep the momentary range inside 10 dB.
- Stock queries: "gold particles falling black", "light rays stage haze", "basketball court empty spotlight", "sparks rising slow motion" (player cut-outs need licensed footage and roto).
