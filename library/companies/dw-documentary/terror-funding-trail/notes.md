# Tracing the path of funding for Islamist terrorist groups  (DW Documentary, published 2026-10-15 on dw.com, 41:04 full / first 300 s analysed, 16:9, dw.com + YouTube)
URL: https://www.dw.com/en/tracing-the-path-of-funding-for-islamist-terrorist-groups/video-79667536
Note: downloaded from DW's own site at 640x360; type sizes read from upscaled frames.
Purpose: documentary explainer (investigative "DocFilm": narrator, experts, officials, an anonymous informant in recreation)
One-sentence point: Small donations, crypto wallets and charity fronts keep Islamist groups funded, and the film follows investigators and an insider to show how.

Analysed: the first 300 s (5 min) of 41:04.

Structure (first 300 s):
- 0.0-2.0 night field with satellite dishes.
- 2.0-5.1 series ident: "DocFilm" with the DW roundel on a black block over a rainbow gradient.
- 5.1-20 cold open: flash montage of attacks, police, money and crypto apps; 14 cuts in 10-20 s, shots of 0.12-1 s.
- 20-58 the case: a terrorism-financing expert (dark interview set), police at night, forensic teams, an attack site, a second expert.
- 58.4-65 title card: frame split, a blurred image on the left with the series kicker "SEARCHING FOR CLUES" in black caps on white, the episode question "Donations for Islamist Terrorism?" in bold white on black on the right.
- 65.4-75 credits "A Film by ..." in bold white on black boxes over a police helicopter.
- 70-86 German TV news report with English subtitles.
- 86-114 police raid footage.
- 114-138 the interior minister's statement (24.2 s, the longest shot), lower third.
- 138-171 prison and court exteriors, an expert.
- 171-268 the informant: a ≈95 s recreation in near-darkness (eye macro, cigarette, skyline at night, lake at dusk, hands), subtitled voice.
- 268-300 war footage, then a car interior.

Cut rhythm: 71 shots in 300 s, ASL 4.23 s, median 3.84 s, 18 % under 1 s (the flash open), 59 % over 3 s, 14.2 shots/min (adaptive detector because of the dark recreation + 3 verified flash cuts; the scene detector found only 55 and a false 59.9 s "shot"). ASL per quarter 2.50 / 5.36 / 4.17 / 6.25 s. Cuts per 10 s: 14 in the open, then 0-4. Longest 24.2 s (minister), 19.8 s, 10.6 s.

Typography:
- DW roundel top left ≈5.5 % H, always on.
- DW house sans (closest free "Noto Sans"): title question bold ≈7 % H white on black; kicker caps ≈7 % H black on a white box; credits bold ≈4 % H white on black boxes, one box per line.
- Lower third, no box, bottom left at x ≈5 % W: name in bold caps ≈4.5 % H, role ≈3 % H bold (dates in brackets for former posts).
- Subtitles (German speech, informant): white semibold ≈4 % H on a 60 % black box, max 2 lines, centred at ≈88 % H.

Colour/grade: cool, dark and desaturated for night and recreation; interviews low-key with coloured background light; news archive as broadcast.

Camera/shots: dark interview set-ups, police and news archive, a stylised recreation with extreme close-ups and silhouettes (identity hidden), aerials, a handheld car interior.

Transitions: hard cuts; flash frames (3 frames) in the cold open; the title card is a split-screen layout.

Sound: integrated -16.3 LUFS, LRA 6.4 LU, true peak -2.2 dBTP, median RMS -22.7 dBFS. Score and tension beds; 15 drop-outs (0.3-1.75 s), two of 1.75 s at 239.5 and 247.9 s inside the informant section; a 0.6 s silence to -78.5 dBFS right before the ident ends (4.5 s), then +66 dB into the montage. Cuts below chance on onsets (37 % vs 45 %).

What makes it premium:
- A hard series identity (DocFilm ident, split title card with a kicker) in the first minute.
- The informant's story is told with a stylised, identity-safe recreation instead of a blurred face.
- Officials are given long, uncut statements; the montage energy is kept for the open.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Open: 2 s mood shot, 3 s ident, then a 10-15 s flash montage (0.12-1 s) with a 0.5 s silence before it.
- Title card: two halves: left image with `filter:blur(6px)`, kicker `span{background:#fff;color:#000;font:800 7vh "Noto Sans";text-transform:uppercase}`; right black with the question `font:800 7vh "Noto Sans";color:#fff`; hold 6 s.
- Lower third: `.n{font:800 4.5vh "Noto Sans";text-transform:uppercase}` `.r{font:700 3vh "Noto Sans"}` at `left:5%;bottom:8%`, no box, hold 4-6 s.
- Subtitles: `background:rgba(0,0,0,.6);font:600 4vh "Noto Sans";padding:.3vh 1vh`.
- Recreation: macro and silhouettes, `filter:brightness(.55) saturate(.6)`, 5-10 s shots.
- Mix: score continuous, master -16 LUFS.
