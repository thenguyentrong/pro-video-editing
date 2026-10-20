# we gave this guy a spanish test #duolingo  (Duolingo, 2026-10-16, 68.4 s, 9:16, YouTube Shorts / TikTok)
URL: https://www.youtube.com/shorts/ClZv9JaaOfE
Purpose: social reel (creator-style challenge series, real people, "challenge 1" of several)
One-sentence point: A man who promised to learn Spanish for his fiancée is blindfolded and must name objects in Spanish in 60 seconds.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-2.3 hook: warm 2-shot of the couple laughing, slow push-in; white text types on letter by letter: "This guy said / he'd learn Spanish / for his fiancée..." (0.0-1.0 s), then the bold punch line "...did he!?" (1.75-2.25 s). The stake and the doubt are both in the first 2.3 s.
- 3.6-7.1 setup: cut to him wearing a Duo-eye blindfold; "Watch us test his Spanish"; title card "challenge 1 / vocabulary" with 3 progress dots (5-7 s).
- 7.1-15.6 rules: host explains (60 s, name objects in Spanish); 3 cameras (wide 3-shot with Duo plush toys, CU contestant, CU host).
- 15.6-60.4 game: countdown timer + score on screen ("Score: 0/3" ... "4/3"), each object = 2-4 shots, small fails ("I don't know", "Spanish is hard", "Not shoes... but clothes...") and wins ("Very good!").
- 60.4-65.2 payoff: "Time!", Duo plush jumps in, celebration on the wide.
- 63.0-65.2 CTA text "Check out our channel to see if he passes the other challenges"; 65.2-68.4 end card Duo face on lime green, eyes blink.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 39 shots (38 verified cuts), ASL 1.75 s, median 1.33 s, 21 % under 1 s. Quarters 1.71 / 1.22 / 1.71 / 2.14 (densest in the first half of the game).
- Time compression: the timer runs 60 s while only 45 s of screen time passes (15.6-60.4 s), jump cuts remove all dead air. Longest shot 6.7 s at 45.9 s (one struggle played out).

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Hook text: IBM Plex Sans-like white, regular (3 lines) + bold punch line, soft shadow, no box, cap ~3.3 % H, centred at 43-61 % H, punch line 66-71 % H; typewriter reveal ~16 characters/s.
- Title card: "challenge 1" lowercase lime green (#58CC02-like), Feather-Bold-like, cap ~6 % H, "vocabulary" white below, 3 dots.
- Game UI: countdown digits in a white box with a thick yellow (#FFC800-like) rounded border at 65-73 % H, "Score: 1/3" bold white at 75-78 % H, subtitles white regular cap ~2.4 % H at ~87 % H (low, partly in the platform UI zone).
- Max 3 persistent elements during the game (timer, score, one subtitle line).

Colour/grade: palette, contrast, grain, letterbox
- Natural, warm backyard daylight, shallow depth of field, the contestant's mustard shirt + green blindfold + Duo plush tie into the brand green. Full-bleed, no letterbox.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Real people, produced but creator-styled: 3 cameras (wide 3-shot on ~35 mm, two CUs on ~85 mm with bokeh), slight handheld on CUs. Brand appears as props (blindfold with Duo eye, plush characters).

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- All hard cuts (38). Title card and CTA text animate in over picture.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Location dialogue + light upbeat music bed; integrated -25.6 LUFS (quiet, dialogue-led mix, much lower than the meme posts at -7 to -12). Original audio.

What makes it premium (3-5 bullets)
- Hook states a human stake (love + promise) and a doubt ("...did he!?") in 2.3 s.
- Game-show UI (timer + score) gives a reason to watch to the end.
- Jump cuts compress 60 s of play into 45 s.
- Branded props instead of logos; series CTA sends viewers to the profile.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 65-70 s. Shoot 3 cameras; edit to ASL ~1.7 s, no shot over 7 s.
- Hook text: font IBM Plex Sans 400 / 700, 64 px cap (3.3 % H), white, `text-shadow: 0 2px 8px rgba(0,0,0,.45)`, centre at y 1000 px; typewriter with GSAP TextPlugin or per-letter `tl.set` every 0.06 s.
- Timer: div 260x110 px at y 1250-1400 px, `border: 10px solid #FFC800; border-radius: 22px; background:#fff; font: 700 80px "Share Tech Mono"`; update each second of game time, but let the edit skip seconds.
- Score line under it (bold 40 px white); subtitles 46 px white at y 1660 px (keep them above 1540 px if the post is for TikTok).
- End: 3 s brand-colour card (#58CC02) with mascot face; CTA line 2 s before it.
