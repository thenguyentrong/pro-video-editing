# How a New U.S. Weapon Killed 21 Civilians in Iran  (The New York Times — Visual Investigations, 2026-06-02, 6:31, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=HEyfNHBeSSY
Purpose: explainer / investigation (Visual Investigations desk, reporter-led)
One-sentence point: Satellite images, official launch footage and local videos together show that a new U.S. missile (PrSM) hit a recreational centre in Lamerd and killed 21 civilians.

First 150 s analysed (of 391 s).

Structure: beats with timestamps
- 0–7 s cold open: a screen recording of satellite imagery (the mouse cursor is visible) with the reporter's face in a small rounded picture-in-picture, bottom right; 4.5–7 s the reporter at his desk in the NYT newsroom, looking at the screen (verité, not posed).
- 7–25 s one continuous satellite move: slow zoom into one building, a white square marks the impact point (17 s), then the camera pulls back while a tiny white box keeps the point (19–25 s).
- 25–33 s reporter to camera in the newsroom ("stand-up" at the desk).
- 33–37 s the target named: white outline traced around the compound + label "Recreational center".
- 37–47 s the human cost: victim photos pop on over the darkened satellite map, first 4, then a 6 x 4 grid of 21 portraits.
- 47–60 s reporter to camera, lower third 48–53 s.
- 60–72 s comparison montage: same white box + serif place label on four satellite images (Rafah, Gaza / Mariupol, Ukraine / Minab, Iran / Lamerd, Iran), date top-left, imagery credit bottom-left; ~2–2.5 s each; on Lamerd the box shrinks to show the context.
- 72–95 s the weapon: official launch videos (U.S. Space Force via DVIDS, U.S. Central Command via DVIDS) and a Lockheed Martin animation labelled "PROMOTIONAL FOOTAGE", all shown smaller inside a black frame with a source credit.
- 95–100 s aftermath photos (Lamerd street, hospital), each credited.
- 100–108 s reporter.
- 108–120 s local evidence: a vertical phone video pillarboxed on black ("IRIB TV via Agence France-Presse"), then drone footage of fresh graves ("Iranian Foreign Media Department via Reuters").
- 120–147 s the key proof: a 3-panel grid of synced CCTV + phone videos, one panel scales up to full size for the impact (129–137 s), back to the grid, then a phone video of the explosion with its on-screen timestamp.
- 147–150 s back to the reporter.

Cut rhythm: 29 shots in 150 s, ASL 5.17 s, median 3.13 s. ASL per quarter 6.25 / 4.69 / 2.89 / 7.50 s. Longest: 22.1 s (CCTV grid sequence at 120.8 s), 18.9 s (satellite zoom at 7.0 s), 14.0 s (outline + photo grid at 33.9 s). Shortest 1.33 s (photo at 96.8 s). 0 % of shots under 1 s, 55 % over 3 s. Densest 90–100 s (5 cuts / 10 s, the official launch clips). Cuts on audio onsets 57 % vs 48 % chance (not cut to music).
Note: a continuous animated graphic (satellite zoom, panel that scales up from the CCTV grid at 128.8 s and 138 s) counts as ONE shot; these grid-to-full moves are animated scale transitions of ~0.75 s, not cuts.

Typography: (fonts are guesses from 480p frames)
- Lower third: white rectangle at x 6–33 % W, y 62–74 % H (box 11 % H tall), no animation flourish. Name in bold serif (looks like NYT Cheltenham; closest free: "Source Serif 4" Bold / "Libre Caslon Text" Bold), cap height ~3 % H, dark grey #222. Role in small tracked caps sans (Franklin-like; closest free "Libre Franklin" 500), ~1.7 % H: "VISUAL INVESTIGATIONS REPORTER". Held ~5 s.
- Place labels on satellite: white serif regular, sentence case ("Mariupol, Ukraine"), ~3.3 % H, centred under the box. Date top-left white sans ~2.7 % H ("March 29, 2022"). Imagery credit bottom-left white sans ~1.5 % H ("Vantor", "Airbus DS", "Planet Labs").
- Map labels on the target: white bold sans, ~3 % H, with a soft dark shadow ("Recreational center").
- Source tags on footage: "PROMOTIONAL FOOTAGE" bold sans caps ~3 % H top-centre; credits bottom-left ~1.5 % H on every external clip.
- No captions/subtitles burned in (except the original Persian text inside local videos).

Colour/grade: no stylised grade. Satellite imagery kept natural, darkened ~40 % under the photo grid. Only one annotation colour: white (1.5–2 px box strokes, polygon outline with soft shadow). Newsroom shots are neutral, cool office light, shallow depth of field. Non-16:9 sources sit on pure black (#000), scaled to ~80–90 % of frame height. No letterbox, no grain.

Camera/shots: screen recordings of satellite tools (cursor visible), Google-Earth-style slow zooms, reporter stand-ups in the newsroom (eye-level, shallow focus, slight handheld drift), official military footage, corporate promo animation, wire-agency photos, vertical phone video, drone, CCTV multi-cam grid. No 3D renders made by NYT in this window.

Transitions: hard cuts only, plus animated in-frame moves (zoom, box shrink, panel scale-up). No dissolves between scenes (soft.py's flags are the zooms and layout moves). No whip pans, no flashes.

Sound: integrated -19.9 LUFS (quieter than typical YouTube -14). Voice-led: 32 gaps between phrases drop to -50…-71 dBFS (e.g. 1.95 s at -71 dBFS at 45.5 s, after the victim grid; 1.8 s at 144.7 s before the explosion) — so for long stretches there is NO continuous music bed (inference from the silent floors). Source audio is used as SFX: rocket launch at 71.25 s rises +52 dB, CCTV explosion at 121 s +41 dB. Loudest momentary -11.6 LUFS at 2 s.

What makes it premium
- Every piece of evidence is labelled where it comes from (credit bottom-left, "PROMOTIONAL FOOTAGE" top-centre) — trust is the design.
- One annotation language (white box + serif place label) repeated across four places makes the comparison instant.
- The reporter's real workspace (newsroom, screen recording with cursor) shows the method, not only the result.
- Restraint: no colour coding, no music under the human-cost moment, silence before the explosion.
- Long holds on the proof (22 s CCTV grid) instead of fast cutting.

Recipe (real footage + HTML/GSAP, Hyperframes)
- Layers: footage/satellite still (full-bleed) → dim layer `background:#000; opacity:.4` when overlays appear → annotation SVG (stroke #fff, 2 px at 1080p = 0.19 % H, `filter: drop-shadow(0 1px 3px rgba(0,0,0,.6))`) → label → credit.
- Satellite move: still image scale 1 → 2.2 over 10 s `ease:"power1.inOut"`, then box `scale` from 3 → 1 in 0.8 s `power2.out` on the target; pull back scale 2.2 → 1 in 4 s while box width shrinks with it.
- Comparison cards: same box (34 % W x 50 % H, centred) and serif label `font: 400 3.3vh "Source Serif 4"; color:#fff` under it; date `font:400 2.7vh "Libre Franklin"` at top 4 %, left 3 %; credit `1.5vh` at bottom 4 %, left 3 %. Hard-cut every 2.2 s.
- Photo grid: tiles 9 % W, gap 0.4 %, stagger in `from {opacity:0, scale:.9}` 0.15 s each, `stagger: 0.04`, over a 40 % black dim.
- Lower third: `background:#fff; padding:1.2vh 1.6vh; left:6%; top:62%`; name `700 4vh "Source Serif 4"` #222; role `500 1.8vh "Libre Franklin"; letter-spacing:.08em; text-transform:uppercase`. Fade 0.3 s, hold 5 s.
- External clips: scale to 85 % H, centred on #000, credit `1.5vh` white bottom-left; for promo material add `PROMOTIONAL FOOTAGE` `700 3vh` caps top-centre.
- Multi-source sync: CSS grid 2 x 2 (left column 2 stacked panels, right one tall), then GSAP `Flip`-style tween of one panel to full frame in 0.75 s `power2.inOut`.
- Mix: voice at -16…-18 LUFS short-term; no music bed under evidence; let source SFX peak ~6 LU above the voice; leave 1–2 s of near-silence before the key clip.
