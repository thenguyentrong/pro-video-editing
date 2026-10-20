# The Dark Money Behind Myanmar's Civil War | Bloomberg Investigates  (Bloomberg Originals, 2026-08-20, 18:59, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=0EZ6f3M64rI
Purpose: investigative documentary (reporter-led field film, series "Bloomberg Investigates")
One-sentence point: A Bloomberg editor travels through Myanmar to follow the money (jade, gems, cash) that keeps the military junta's civil war going.

First 150 s analysed (of 1139 s).

Structure: beats with timestamps
- 0–7.8 s cold open: armed soldier by a road, the reporter (Matthew Campbell) filming himself selfie-style at a checkpoint (1.5–4.3 s), eyes in a car mirror, barbed wire, guard at a boom gate.
- 7.8–33.4 s the junta's show: night military parade in Naypyidaw (jets overhead, crowd watching a big screen, artillery trucks, flag bearers, rocket launchers, officials saluting); the reporter on the parade ground with a press pass (17 s).
- 33.4–39.2 s map: dark slate-textured 3D map of Myanmar, military-held areas in deep red, italic label "Controlled by the military" with a leader line and dotted underline (5.8 s).
- 39.2–44.7 s UGC combat footage, first-person with a rifle, kept with its original watermarks (KineMaster logo, a militia insignia, date stamp).
- 44.7–54 s third-party TV as evidence: a news studio ("MYANMAR civil war"), then WION news clips with their red/white chyrons ("MYANMAR: JUNTA CLAIMS DEMOCRATIC RESET", "MILITARY RULE REMAINS INTACT IN MYANMAR").
- 54–67 s human cost: displaced woman peeling a coconut, a baby on a mat, a mother and son, then her interview — all with English subtitles.
- 68–69.9 s series ident "Bloomberg INVESTIGATES" glowing on black (1.9 s).
- 70–94.7 s the reporter in the field: walking through a border market, a monk, an elder, parade spectators filming on phones, a "WA NATIONAL ARMY — WELCOME EVERYONE TO OUR LAND" sign, a guard, gems on a phone and in a dish, dollar notes counted, jets at night.
- 94.7–103.5 s title: light sweep reveals "THE WAR THE WORLD FORGOT" in spaced caps over a ghosted "DARK MONEY" (8.8 s, the longest shot).
- 103.5–121 s Yangon traffic, the reporter in a car writing notes (lower third 107–110 s), reporter's sit-down interview in a bright room.
- 121–139 s destruction: bombed houses, a shot-up car, children in rubble (slow pans, 2–4 s each).
- 139–150 s reporter in a car; second map with a region label "Sagaing / Myanmar" (142–146 s); street from the car.

Cut rhythm: 68 shots in 150 s, ASL 2.21 s, median 1.98 s. ASL per quarter 1.79 / 1.97 / 2.34 / 2.50 s (slowly calming). Longest 8.8 s (title at 94.8 s), 5.8 s (map at 33.5 s), 4.8 s (car at 106.6 s). Shortest 0.5–1.0 s. Only 4 % under 1 s, 21 % over 3 s — an even, steady pace. Densest 10–20 s and 70–90 s (7 cuts / 10 s). Cuts on audio onsets 25 % vs 30 % chance (cut on picture and story, not on beats).

Typography: (Bloomberg grotesk; closest free "Inter" — guess)
- Lower third: no box; name in bold CAPS ~4.5 % H ("MATTHEW CAMPBELL"), role regular sentence case ~3.5 % H ("Senior Editor, Bloomberg News"); left x 10 %, y 78–89 % H; fades in/out ~0.4 s, held ~3 s.
- Subtitles (foreign speech): white sans 500, ~4 % H, centred, 2 lines max, y 80–90 % H, no box, soft shadow only; full sentences ("We were in a desperate situation / because we fled with absolutely nothing.").
- Map label: white italic sans ~3.5 % H with a thin horizontal leader and a dotted underline; region label "Sagaing" + small "Myanmar" under it.
- Series ident: small "Bloomberg" wordmark over "INVESTIGATES" in widely tracked thin caps (~0.3 em), glow on black.
- Episode title: spaced caps ~5.5 % H white with RGB fringe and horizontal light streaks; "DARK MONEY" ghosted behind at ~12 % H in dark grey.
- Persistent bug: white Bloomberg "B" icon top-right.
- Third-party material keeps its own branding (WION chyrons, KineMaster watermark) — no Bloomberg overlay on it.

Colour/grade: filmic, slightly warm and low-contrast field footage (dusty daylight, sodium-lit night parade); the maps are near-black slate with deep crimson (~#8E1B2C) areas; the title sequence is monochrome silver. No letterbox; fine texture on the maps.

Camera/shots: handheld cinema camera following the reporter (walking, in cars), selfie/phone shots by the reporter himself, observational long-lens parade coverage, sit-down interview in a bright room, macro inserts (gems, cash, notebook), UGC combat video, third-party TV news, 3D textured maps.

Transitions: hard cuts; title and ident are light sweeps; no dissolves between scenes.

Sound: integrated -17.4 LUFS, median momentary -16.4 (-16.0 / -16.1 / -17.1 / -16.8 by quarter). Almost no pauses: only 2 drop-outs (103–104.5 s after the title, to -37 LUFS) and 1 short gap → continuous score + location sound under narration (inference). Loudest -12.5 LUFS at 67 s, right before the series ident (music swell); rises of +15…+20 dB at 112–134 s (destruction section).

What makes it premium
- A named senior editor on the ground (selfie at the checkpoint in second 1) = first-person investigative authority.
- Raw evidence kept raw: UGC watermarks and other broadcasters' chyrons stay visible, which reads as honest sourcing.
- Two-step branding: series ident at 68 s, episode title at 95 s — after the hook and the human cost.
- Dark, textured maps with one crimson data colour and a single italic label.
- Even pace (median 2 s, almost no sub-second shots) gives it documentary weight rather than news urgency.

Recipe (real footage + HTML/GSAP, Hyperframes)
- Cold open: 1 self-filmed reporter shot (phone, wide lens) inside the first 2 s, then 4–6 location shots of ~1.5 s.
- Dark map: country shape PNG/SVG with a concrete/slate texture background (`#1d2226` + noise), controlled areas `fill:#8E1B2C` with a 10 % noise overlay; camera push `scale 1 → 1.12` over 6 s `ease:"none"`; label `italic 500 3.5vh "Inter"` white, leader line draws `scaleX 0 → 1` 0.5 s `power2.out`, dotted underline (`border-bottom:2px dotted #fff`, 25 % width of label) fades in after.
- UGC/third-party: show full-frame at native aspect, keep the source's watermark/chyron, add nothing except (optionally) your own small source credit bottom-left.
- Subtitles: `500 4vh "Inter"; color:#fff; text-shadow:0 1px 8px rgba(0,0,0,.6)`, centred at `bottom:10%`, ≤ 2 lines, ≤ 42 chars per line.
- Lower third: name `700 4.5vh`, uppercase, `letter-spacing:.02em`; role `400 3.5vh`; `left:10%; top:78%`; `opacity 0 → 1` 0.4 s, hold 3 s.
- Title: dark brushed-metal background video/gradient; ghost word `800 12vh` `color:#2a2e33`; title `400 5.5vh; letter-spacing:.25em` white, add RGB split (two text-shadows `-2px 0 rgba(255,0,0,.5), 2px 0 rgba(0,255,255,.5)`) and a light streak (`linear-gradient` sweep, `x -100% → 100%` 1.5 s `power2.inOut`); hold ~8 s; pull the score down ~20 LU right after.
- Mix: voice ~-16 LUFS short-term; score + location sound continuous ~-24…-28 LUFS; swell to ~-12.5 LUFS into the series ident.
