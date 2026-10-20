# Bagspotting in Chicago with @tiffbaira  (Target, 2026-10-17, 77.5 s, 9:16, YouTube Shorts / TikTok / Reels)
URL: https://www.youtube.com/shorts/4_rfxdVYqp4
Purpose: social reel (creator-hosted street-interview series "Bagspotting")
One-sentence point: A comedian in a red suit hunts people carrying red Target bags around Chicago and asks what is inside.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-1.2 hook: locked wide: host in a head-to-toe red suit slides along stone steps toward a woman with a red Target bag (physical comedy, no text). 1.25 s cut to a CU of both laughing on the bench ("Where'd you get it?").
- 2.6-12.4 intro: bag close-ups, Wrigley Building clock (whip-tilt in at 4.5 s), host intro to camera with lower third "Tiffany Baira / Chicago Bagspotter" (5.0-6.4 s), B-roll of red bags on the street, "Hey beautiful Chicago... I'm Tiff and you're watching Bagspotting".
- 12.4-13.0 show title: "bagspotting" wordmark (bullseye as the "o") over radiating red rings.
- 13-74 interviews: 6 strangers, each = approach wide -> CU answers -> insert of the bag contents (cards, grip socks, digital camera, Huggies, Little People toys, a capybara plush), jokes from the host ("In your dating life?").
- 74-77.5 end: host walks off with a family and stroller; no end card, no CTA.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 52 shots, ASL 1.49 s, median 1.25 s, 27 % under 1 s, longest 4.5 s (68.9 s). Quarters 1.08 / 1.29 / 1.61 / 1.94: fast intro montage, slowing into the interviews.
- Classic interview cutting: wide 2-shot -> CU -> CU -> insert; every answer trimmed to its punch.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Only 2 graphics in 77 s. Lower third: white Helvetica Neue Bold-like with a red outline, cap ~3 % H at ~70 % H, left at x 14-60 % W, sub-line in a small red pill; on 1.4 s.
- Show title: white bold lowercase "bagspotting" wordmark, x-height ~4.5 % H at ~50 % H, over concentric red rings radiating out (bullseye pulse), 0.6 s.
- No burned-in dialogue subtitles (relies on platform captions).

Colour/grade: palette, contrast, grain, letterbox
- Bright autumn sun, high contrast, deep shadows; everything orchestrated around Target red (suit, mic flag, bags, feather cuffs) against grey stone and blue glass. Clean, slightly warm grade.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Produced creator format: 2-3 cameras, long-lens CUs with bokeh, wide 2-shots, inserts of products in hands, city establishing shots. Real passers-by.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts; one whip-tilt (4.5 s); title over rings.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Dialogue-led, music bed under B-roll. Integrated -11.7 LUFS. Original.

What makes it premium (3-5 bullets)
- The brand is a colour, not a logo: red suit + red bag = Target in every frame.
- Creator with a strong persona carries the format; Target only provides the game ("spot the bag").
- Series name + wordmark makes it repeatable in any city.
- Product discovery hidden inside small talk (bag contents = catalogue).

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 60-80 s, ASL ~1.5 s; per guest: wide approach 1.5 s, 2-4 CU answers 1-2 s, 1 product insert 0.8 s.
- Lower third: `font: 700 58px "Helvetica Neue", Arial; color:#fff; -webkit-text-stroke: 3px #CC0000; paint-order: stroke fill` at y 1340 px, x 150 px; pill below `background:#CC0000; border-radius: 999px; font: 600 22px`. In: `from {x:-40, autoAlpha:0}` 0.2 s; out after 1.4 s.
- Title: wordmark 0.6 s with 6 SVG circles `stroke:#CC0000; stroke-width:24` scaling 0 -> 3 with `stagger:0.06`.
- Wardrobe and props in the brand colour; no end card.
