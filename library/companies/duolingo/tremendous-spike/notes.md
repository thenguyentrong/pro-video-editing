# i'm feeling TREMENDOUS (spike is not)  (Duolingo, 2026-09-25, 8.8 s, 9:16, YouTube Shorts / TikTok cross-post)
URL: https://www.youtube.com/shorts/O5SimBldLJM
Purpose: social reel (mascot meme on a sung audio, Brawl Stars collab tease)
One-sentence point: Duo brags in song that finishing one Spanish sentence makes him famous, told in four 2-second gag shots.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-2.2 hook: 3D Duo struts toward camera down a tree-lined road (photo background). The sung lyric appears as Duolingo word-bank tiles, one word at a time: "I'm" (0.0), "feeling" (0.5), "TREMENDOUS" (1.0, lower tile). Viewer knows the joke (arrogant owl) before 1 s.
- 2.2-4.4 build: hard cut to a pixel-true copy of the app lesson screen ("Complete the sentence", "Soy el ___", tiles mejor/peor/la). Duo drops into the tile slot; at 3.5 s the green "correct" bar fires and a black clapping-crowd silhouette rises from the bottom (lyric: "people clap when I finish up a sentence").
- 4.4-6.4 turn: one-frame whip blur to Duo standing in front of a sandstone statue of himself (lyric: "build a statue").
- 6.4-8.8 payoff: whip to a showroom; Duo holds up a phone with lock-screen notifications from "CEO of Brawl Stars"; a speech bubble with a Brawl Stars character pops in at 7.5 s (crying at 8.0 s). Hard end, no end card, no logo.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 4 shots in 8.8 s, ASL 2.19 s, median 2.21 s. Every shot is about one lyric line (2.0-2.3 s). Quarters 2.19 / 1.09 / 0.73 / 2.19 (densest in Q3 because of the two whips).
- Cuts sit on lyric line starts, not on drum onsets (cuts on onset 0 % vs 33 % chance).

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Captions = the app's own word-bank tiles: white rounded rectangle (radius ~12 % of tile height), 1-2 px light grey border plus a darker 3 px bottom edge, text dark grey #3C3C3C, DIN Next Rounded / Nunito-like regular, sentence case except the shouted word in caps.
- Tile height 11-13 % H; cap height 3.9 % ("I'm") to 4.4 % ("TREMENDOUS"). Line 1 tiles at 14.6-26 % H, the shout tile at 71-84 % H, x 10-90 % W. One word per tile, pop-on per sung word (no tween visible at 4 fps), whole lyric holds until the cut.
- Captions only in shot 1; after that the joke is carried by app UI and props. Max 3 words on screen.

Colour/grade: palette, contrast, grain, letterbox
- Saturated: Duo green #58CC02, white app UI, blue sky, warm sandstone. Clean, no grain, no letterbox, full-bleed 9:16.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- 3D-rendered Duo composited on stock-photo backgrounds; one fake screen recording of the app (UI rebuilt, not captured); one phone prop. Static framing, Duo animates; no camera moves except the whips.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 1 hard cut (2.2 s), 2 one-frame directional-blur whips (4.4 s, 6.4 s), 1 crowd silhouette wipe-up inside a shot (3.5 s).

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- One sung track carries everything (lyrics = story). No VO, no added SFX heard in the analysis. Integrated -7.0 LUFS (very loud, music-master level), loudest 0.5 s at 7.6 s; no drop-outs. Track source not named in the metadata, so treat as audio meme / possibly original.

What makes it premium (3-5 bullets)
- The caption IS the brand: word tiles from the app make the lyric look like a lesson.
- One idea per lyric line, one shot per line: 4 shots, 4 jokes, under 9 s.
- App UI recreated pixel-perfect, so fans recognise it in a frame.
- No logo, no CTA, no end card: it plays like a creator post and loops into the next video.
- Collab tease (Brawl Stars) hidden in the last 1.5 s rewards rewatch.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- Canvas 1080x1920, 30 fps, 9 s. Four clips of 2.0-2.3 s, cut on the first syllable of each lyric line.
- Word tiles: div with background #fff, border 2px solid #E5E5E5, border-bottom 5px solid #E5E5E5, border-radius 24px, padding 28px 40px, font "Nunito" 600 (or DIN Round) 84 px (= 4.4 % H cap), color #3C3C3C. Place line 1 at top 290-500 px, shout tile at 1360-1610 px. GSAP per word: `tl.from(tile,{scale:0.6,autoAlpha:0,duration:0.08,ease:"back.out(3)"}, wordTime)`.
- Whip: last 2 frames of clip A and first 2 of clip B get `filter: blur(18px)` + `x: ±120px` (or a CSS motion blur via 4 offset copies at 25 % opacity).
- Crowd pop-up: black PNG silhouette, `from {yPercent:100}` 0.25 s `power3.out` on the "correct" beat.
- Audio: one song at about -9 to -7 LUFS; no VO; keep the cut to the lyric line, not the beat.
