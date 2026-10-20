# Pranking a Pro NASCAR Driver  (LEGO, 2026-09-22, 36.7 s, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/Sa01say-CmI
Purpose: social prank / build challenge with a sports guest
One-sentence point: A host and a NASCAR driver race to build a LEGO car against a clock; the host secretly swaps in a finished model and the driver's reaction is the payoff.

Structure: beats with timestamps
- 0.0-1.8 hook: the end reaction first (flash-forward), with the finished car pixelated so the reveal is not spoiled; a question caption asks how he built it so fast.
- 1.8-7.5 set-up: host introduces the challenge; name tag for the guest (6-8 s).
- 7.5-20.9 challenge: countdown box top right (13 → 00), cuts between both builders every ≈1 s; "Prank time!" aside caption at ≈13 s; the host pulls a finished car from the bin under the table (17-19 s).
- 20.9-24.3 time up: split screen of both reactions with the timer at 00.
- 24.3-33.9 reveal: the guest's broken build vs the host's perfect car; faces and laughs, cuts every 0.25-1.5 s.
- 33.9-36.7 end: both laughing, legal line at the bottom. No end card.

Cut rhythm
- 36 shots, ASL 1.02 s, median 0.96 s, 53 % < 1 s, ≈59 shots/min. Quarters 1.02 / 1.02 / 0.92 / 0.83 s: constant pace, fastest at the reveal (four shots of 0.25-0.5 s at 28.25-29.6 s).
- Cut-to-onset 49 % vs 45 % chance: cuts on reactions and lines.

Typography
- Hook question: white bold sans with a black outline, 2 lines, cap ≈3 % H, centred at 40-45 % H, 0-2.6 s.
- Name tag: two black boxes (name white caps cap ≈2.2 % H; role smaller) with a red LEGO-brick accent, top centre at 13-21 % H.
- Countdown: black rounded box with white (then yellow at 00) digits, cap ≈3 % H, top right at ≈13.5 % H (x ≈62-85 % W), with a yellow "tick" burst and a red brick.
- Aside caption "Prank time!": white bold with outline, beside the face at ≈35 % H.
- Closest free: TikTok Sans 700 / Inter 800.

Colour/grade
- Bright outdoor event light, branded backdrop, checkered-flag table, colourful brick bins; no grade.

Camera/shots
- Two handheld/tripod phones: wide two-shot, singles, overheads of hands in bins; one split screen of both faces.

Transitions
- Hard cuts; split screen at time-up.

Sound
- Dialogue + laughs on a light bed; -13.3 LUFS, peak +0.4 dBTP. Hits +22 dB at 12.05 s and +20 dB at 28.55 s (laughs).

What makes it premium
- Flash-forward hook: the reaction and a question in frame 1.
- Game graphics (name tag, timer) look like a TV show but stay small and in the top band.
- The prank is the twist and the product is the joke (a finished set vs loose bricks).

Recipe (real footage + HTML/GSAP, 1080x1920)
- 35-40 s: 1.8 s flash-forward hook with question caption, 6 s set-up, 13 s timed challenge, 3 s split reaction, 10 s reveal, 3 s end on laughter.
- Timer: `.timer{background:#111;color:#fff;font:800 56px Inter;border-radius:12px;padding:6px 14px}` at x 670 px, y 230 px; `tl.set` per second; at 00 `color:#FFD400` + scale pulse 1.15 in 0.12 s.
- Name tag: two stacked black boxes at y 250-400 px, `from {x:-40, autoAlpha:0}` 0.2 s.
