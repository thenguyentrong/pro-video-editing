# Stripe Sessions 2024  (Stripe, 2024-06-04, 108.9 s, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=KH0_HM6e66w
Purpose: keynote sizzle / event recap (annual user conference with many product launches)
One-sentence point: In under two minutes the conference feels huge, busy and important: founders on stage, many launches, famous guests, a full expo.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-5.2 cold open (0-5 %): dark hall, crowd silhouettes against a pink stage, wide of the two founders on stage; a stage line starts the music.
- 5.2-7.0 (5-6 %): event lockup on a soft pink-orange-violet blur (wordmark in a navy box + event name in a second, offset navy box). Hit on the lockup.
- 7.0-21.6 (6-20 %): CEO on stage (lower third), venue signage with the conference tagline, arrivals in the hall, expo booths, hands-on product demos.
- 21.6-45.0 (20-41 %): keynote stage: founders, product leads with big feature slides behind them, an on-stage live demo on a giant screen, audience reaction shots (dark, magenta light).
- 45.0-62.8 (41-58 %): more launches: speakers in front of slide titles, a live data graphic (requests per second climbing), signage.
- 62.8-65.6 (58-60 %): partner logo burst: 10 shots of 0.17-0.3 s (logos on booths and walls), the fastest moment.
- 65.6-88.0 (60-81 %): guest speakers from big partners, expo crowd, product macros of the reader on violet light.
- 88.0-98.0 (81-90 %): fireside chat with a famous tech CEO on a saturated blue stage (biggest rise +23.6 dB at 88.4 s).
- 98.0-105.6 (90-97 %): atmosphere (sticker table, attendee CU, a humanoid prop), founders close on stage.
- 105.6-108.9 (97-100 %): the lockup again, the boxes collapse into a navy shape. End.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 92 shots, ASL 1.18 s, median 0.98 s, 50 % under 1 s, 3 % over 3 s, 51 shots/min. Quarters 1.09 / 1.30 / 1.01 / 1.24 s: fast and flat.
- Cuts per 10 s: 7, 12, 9, 6, 6, 7, 15, 7, 8, 7, 7. Densest 60-70 s (15: the logo burst, shots of 0.17 s).
- Longest 3.8 s (live demo on the big screen), 3.4 s (speaker at lectern), 3.3 s (end lockup).
- Verified by eye: 7 cuts added in dark audience/hall footage that the scene detector missed (1.4, 2.6, 4.3, 36.8, 43.2, 44.2, 97.0 s).

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Lockup: brand wordmark white in a navy box (wordmark ≈8 % H), event name in caps in a second navy box offset down-right (cap ≈11.5 % H, light grotesque, free: Inter 300/400 caps), boxes ≈#1a1b2f, left-of-centre at x ≈18-82 %, y ≈23-73 %. On a blurred mesh gradient (≈#eb91ad, #e67fb6, orange, violet). Hold 1.8 s at the start, 3.3 s at the end.
- Lower thirds: Stripe grotesque (Söhne-like; free: Inter). Thin bar | name regular cap ≈3.8 % H | thin bar | role ≈2.9 % H, white, one line at y ≈83 % H, x from ≈6 %. Fade in ≈0.3 s, hold 1.5-2.5 s (often across a cut).
- On-stage slides do the feature naming (big white or black headlines inside the shot); no added feature titles.

Colour/grade: palette, contrast, grain, letterbox
- Stage lighting in brand colours: magenta/pink, deep violet, one saturated blue stage ≈#2c00de, one orange stage set. Dark house, crushed blacks, saturated highlights. Expo shots bright and neutral. No letterbox.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Event coverage: long-lens stage shots (multi-camera), handheld gimbal through the expo, low-angle walking shots, audience CUs, macro product shots in violet light, signage close-ups. No UI capture; the product shows only on stage screens and devices.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts (91 of 92). The lockup boxes animate (slide/scale) and collapse at the end; one graphic wipe into the lockup.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Voice: stage speech bites from many speakers almost wall to wall (2.2-105.9 s, ≈2.5 words/s), each 2-6 s, laid on the music. No narrator.
- Music: driving electronic track. Integrated −13.9 LUFS, LRA 4.1 LU, true peak +0.3 dBTP. Two short drop-outs at 34.9 s (0.4 s) and 36.0 s (0.7 s) for a speaker line. Hits on the lockup (+21 dB at 5.3 s) and the fireside chat (+23.6 dB at 88.4 s).
- Cuts on onsets 47 % vs 46 % chance: cuts follow the bites, not the beat.

What makes it premium (3-5 bullets)
- Scale shown, not told: crowd, many speakers, partner logos at 0.17 s, a famous guest.
- One colour world (magenta/violet stage light) makes 92 shots from many cameras look like one film.
- The lockup is a strong, simple graphic used twice as bookends.
- The founders open and close it; the launches are sold by the stage slides inside the shots.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920×1080, 100-110 s, ASL ≈1.2 s (median 1.0). Cold open 5 s in the dark → lockup 1.8 s on a hit → arrivals/expo 14 s → stage launches 40 s → logo burst 3 s (10 × 0.2-0.3 s) → guests 22 s → star guest 10 s → close 7 s → lockup 3 s.
- Lockup: two navy boxes `#1a1b2f`, box 1 wordmark (8 % H), box 2 event name `Inter 300 11.5vh` caps white, offset `+18% x, +100% y` of box 1; background = 3 blurred radial gradients (`#eb91ad`, `#f29b5c`, `#7b5cf5`) `filter: blur(80px)` drifting 4 s. Boxes scale `0.96 → 1` + clip reveal 0.4 s `power3.out`.
- Lower thirds as in the Reader S700 film (same system: bars, name 3.8 vh, role 2.9 vh, y 83 %).
- Grade: lift saturation of magenta/violet only, crush blacks to ≈2 %.
- Sound: bites 2-6 s each over the track, duck music −8 dB under speech; master −14 LUFS; 0.4-0.7 s music cut before one key line.
