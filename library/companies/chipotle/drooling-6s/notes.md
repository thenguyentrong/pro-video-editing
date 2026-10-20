# suddenly i'm drooling 🤤 use CHIMI25  (Chipotle, 2025-10-24, 6.1 s, 9:16, YouTube Shorts / TikTok)
URL: https://www.youtube.com/shorts/FU5y1JUejAs
Purpose: ad / promo cutdown (free red chimichurri weekend, promo code in the post caption)
One-sentence point: Four 1.5-second shots of red chimichurri meeting food under one static offer line.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-1.5 hook: extreme food close-up in hard sunlight: sauce squeezed onto a foil-wrapped burrito; offer text on screen from frame 1.
- 1.5-3.0: sauce drizzled over a burrito bowl (top-down, branded napkin and fork).
- 3.0-4.5: quesadilla dipped into a cup of sauce.
- 4.5-6.1: a chip dipped into the cup (brand bag in the background). Ends mid-dip.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 4 shots of 1.48-1.58 s, ASL 1.54 s: a strict musical grid (one bar per shot); cuts on audio onsets 67 % vs 45 % chance.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- TikTok in-app "Classic" text in ALL CAPS, white with thin black outline + 🔥, cap 2.1-2.3 % H, 2 lines at 17.4-23.5 % H, x 15-88 % W. One static card for the full 6 s.

Colour/grade: palette, contrast, grain, letterbox
- Hard outdoor sun, warm, glossy red sauce, brown tortilla tones; foil highlights. Phone footage, no grade.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Handheld phone macros of hands + food (UGC "food content" look). Each shot = one action (squeeze, drizzle, dip, dip).

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 3 hard cuts on the beat.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Music only, very loud master (-6.5 LUFS); hits at 2.05 s and 4.95 s. No VO.

What makes it premium (3-5 bullets)
- 6 s cutdown logic: one message (free sauce this weekend), one visual idea repeated 4 times, cut on the bar.
- Offer readable in frame 1 and never changes: works muted, works in 1 s.
- Native look (phone, sun, hands) instead of studio food styling.
- Code and legal live in the post caption, not on screen.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 6.0 s, 4 clips x 1.5 s (at 80/160 BPM one bar = 1.5 s), each clip one "sauce meets food" action.
- Text: `font: 700 46px "TikTok Sans"/"Proxima Nova"; text-transform:uppercase; color:#fff; -webkit-text-stroke:2px #000; paint-order:stroke fill`, 2 lines centred, top at y 330 px; static, no animation.
- Music at -7 to -9 LUFS, no VO; end mid-action for the loop.
