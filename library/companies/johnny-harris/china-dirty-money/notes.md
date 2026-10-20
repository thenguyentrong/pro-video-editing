# China's Dirty Money Problem, Explained  (Johnny Harris, 2026-04-16, 33:17 full / first 150 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=nAFw5i39m9I
Purpose: investigative explainer (creator-led, recreations + interviews + maps)
One-sentence point: Chinese underground banks quietly move cartel cash around the world without "tripping a single bank alarm" — and Johnny shows how with real money on his desk.

Structure (first 150 s):
- 0.0–7.8 cold open: glowing red lines on a dark map (1.3 s), then hidden-camera clips (fisheye, tilted, cash changing hands in a van) with a centred label "UNDERCOVER FOOTAGE" in white condensed caps; 8 cuts in the first 10 s.
- 8.2–11.1 a link-analysis diagram (investigation software look: people, places, "Owner", "Friendship", "Lives in") — sound drops 2.5 s to −69 dBFS (8.45 s): the breath before the host.
- 11.1–22.5 Johnny at his desk pulling stacks of $100 bills out of a duffel, wide lens, low angle; his own travel photos/drone shots framed small on black as "I've been reporting this for years" (16–21 s).
- 22.5–40.9 talks to camera with cash in hand (7.8 s single shot), microscope footage as metaphor (29–31 s), macro of bills under a scanner light (37–38 s).
- 40.9–44.5 dark teal world map: the US lit in blue, glowing green dashed arcs across the Pacific, an octagon avatar pin "JOHNNY HARRIS / WASHINGTON, D.C." and a second pin in Asia.
- 44.5–59.0 cinematic recreation in 2.39:1 letterbox (actor with duffel, hotel lobby, bank counter, then a burst of five 0.21–0.25 s cuts at 51.1–52.1 s into an arrest and a prison corridor). 11 cuts in 50–60 s = the densest stretch.
- 59.0–89.3 practical demo: Johnny in a kitchen stamps/marks a bill (11.0 s single shot), back at the desk in a second set-up (wider, map tapestry behind), two-camera coverage (front wide + side close).
- 89.3–110 data map: dark map of Asia with red/green flow lines; burned-in yellow subtitles start ("More than $50 million in drug cash."), macro of money stacks, expert Andrea Crosta in a rounded webcam frame on black with name lower left.
- 110–126 two more experts (webcam frames on black), macro of a $100 bill with a scanline texture and the number "4 TRILLION DOLLARS" in outlined condensed caps (119–121 s), letterboxed crime b-roll (drugs, fence, ivory).
- 126–150 Johnny to camera (wide and side angle alternate), expert John Cassara, bills printing; title phrase "FLYING MONEY" in outlined condensed caps placed behind his body (146 s), into flow-line map.

Cut rhythm: 68 shots in 150 s, ASL 2.21 s, median 1.44 s. ASL by quarter 1.79 / 1.88 / 2.89 / 2.21 s. 24 % under 1 s, 24 % over 3 s. Longest 11.0 s (61.7 s kitchen demo), 7.8 s (22.5 s talk to camera), 7.0 s (72.7 s desk). Shortest 0.21–0.25 s (five-cut burst at 51.1–52.1 s, recreation). Cuts per 10 s: 8 5 2 6 5 11 1 2 5 3 2 3 6 5 3. Cuts on onsets = chance (40 % vs 41 %). Host shots are allowed to run long (7–11 s); b-roll around them is 0.8–2 s.

Typography:
- Section labels / big numbers: tall condensed grotesque caps, outline only or outline + grey fill ("4 TRILLION DOLLARS", "FLYING MONEY"), cap height ~10 % H, white/grey, often placed behind the subject (depth matte). Closest free: Bebas Neue / Anton with `-webkit-text-stroke` (guess).
- "UNDERCOVER FOOTAGE": same condensed face, white, solid, ~5.5 % H, centred, slightly transparent.
- Burned-in subtitles (from ~90 s): yellow sentence case, humanist sans, ~3.8 % H, centred at ~94 % H, no box, soft shadow; on narration and experts, not on Johnny's on-camera lines in this window.
- Expert names: inside the webcam frame, lower left, white caps semibold ~2.2 % H + smaller role line.
- Map pins: octagon photo avatar + caps name + city in small spaced caps.

Colour/grade: teal-and-amber. Desk set = warm practical lamps, dark walls, a red map tapestry; recreations and maps = cold teal/navy (#0D1C1F map ground, #174E75 lit country, green glow arcs). Macro money shots get a teal tint + CRT scanlines. Hidden-camera footage keeps fisheye distortion and blown highlights with a scanline/VHS texture. Webcam frames sit on pure black.

Camera/shots: wide-lens low-angle host shots with hands pushing cash toward the lens; two-camera host coverage (front wide, side close, shallow focus); macro inserts (bills, stamp, scanner light); a hired-actor recreation shot like a feature (2.39:1, moody); stock-like crime b-roll in letterbox; drone and travel photos framed as an archive.

Transitions: hard cuts; flash-frame bursts (0.2–0.25 s) for tension; glitch/scanline texture on macro; maps move continuously (camera flies along the arc).

Sound: integrated −15.2 LUFS, loudest −8.2 LUFS momentary at 108.5 s (map), median momentary −15.1 LUFS — loud, dense. 50 ms RMS median −22.3 dBFS, p10 −37.1 dBFS → a bed sits ~15 dB under the voice. Designed silences: 2.5 s at −69 dBFS on the link diagram (8.45 s) before the host's first line; 1.0 s dip at 28.5 s; a 4.5 s drop at 68.5–73 s (kitchen demo — practical sound only) then a hit at 73.5 s (+15 LU). Cuts don't follow the beat.

What makes it premium:
- Real physical props as evidence (stacks of cash on the desk) make an abstract money flow tangible.
- The film switches visual "registers" cleanly: lit host set (warm) / recreation (2.39:1, cold) / data maps (dark teal glow) / undercover (raw, textured).
- Huge numbers get their own typographic moment; everything else is carried by voice + subtitles.
- Investigation-tool visuals (link diagram, pins with faces) signal "this is reporting", not opinion.

Recipe (real footage + HTML/GSAP):
- Big number over macro: footage `filter: hue-rotate(-15deg) saturate(.8) contrast(1.1)` + scanline overlay `repeating-linear-gradient(0deg, rgba(0,0,0,.18) 0 1px, transparent 1px 3px)`; text `font:400 10vh 'Anton'; letter-spacing:.02em; color:transparent; -webkit-text-stroke:2px #f2f2f2` for the number and `color:rgba(220,220,220,.55)` for the unit; `gsap.from(text,{opacity:0, scale:1.06, duration:.5, ease:'power2.out'})`, hold 1.5–2 s.
- Title behind the host: matte the host (remove-background on the clip) and stack `footage → text → host cutout`; letters wipe in left→right with `clip-path: inset(0 100% 0 0) → inset(0 0 0 0)` in 0.6 s.
- Undercover label: `font:400 5.5vh 'Bebas Neue'; color:rgba(255,255,255,.85)`, centred, on footage with `filter: contrast(1.2)` + scanlines + a light chromatic offset.
- Flow map: dark ground #0D1C1F, land #102A2E, focus country #174E75 with `filter: drop-shadow(0 0 12px #3fa9f5)`; arcs as SVG paths `stroke:#7CFFB2; stroke-dasharray:4 6; filter: drop-shadow(0 0 6px #7CFFB2)`, drawn with `strokeDashoffset` over 1.5 s, camera `scale 1→1.15` along the arc; octagon avatar pin with `font:600 1.8vh Inter; letter-spacing:.08em`.
- Expert webcam on black: frame at 80 % W, `border-radius:12px`, name `600 2.2vh Inter` uppercase lower-left inside the frame.
- Subtitles: `font:500 3.8vh 'Lato'; color:#FFF24C; bottom:4vh; text-shadow:0 1px 4px #000`, 1 line, ≤ 42 characters.
- Rhythm: host 7–11 s, b-roll 0.8–2 s, one flash burst of 4–5 × 0.25 s per act; silence 1–2.5 s before the host's first sentence.
