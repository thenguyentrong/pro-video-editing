# Pachinko – Opening Title Sequence  (Apple TV+, uploaded 2022-03-25, 95.1 s file = 82.1 s sequence + 2.5 s Apple TV+ card + 10 s YouTube end screen, 16:9 file with ~2.2:1 letterbox, YouTube / Apple TV channel)
URL: https://www.youtube.com/watch?v=1GgKXR_J-ww
Purpose: main title sequence (series opening credits)
One-sentence point: archival photos of Korean immigrant families turn into the present-day cast dancing with pure joy in a pachinko parlour, so a story of hardship opens with celebration.

Structure:
- 0.0–1.6 black; song starts at 1.6 s (+17 dB rise).
- 1–27 PART 1, ARCHIVE COLLAGE: rough-edged photo panels on black, period family photos tinted in single-colour duotones (amber, magenta, teal, red-orange), often 2–3 panels side by side that slide; short new-footage inserts in the same tints (dancing feet in hanbok, a hand in bokeh light). Credits ("STARRING / SOJI ARAI", "LEE MINHO", "ANNA SAWAI") in tiny wide-tracked caps, often inside a black rough-edged box laid over the edge of a photo. About one cut per second.
- 27–77 PART 2, THE DANCE: full-frame, saturated pachinko parlour (red machines, orange stools, cyan and pink lights) shot down the central aisle. Each cast member dances solo to the lens, then in pairs and groups. Inserts: feet, hands, macro of a pachinko machine (46.3–47.5), golden ball macro (52–54), black-and-white Shibuya-style crosswalk split screen (57.9–58.7), hand in blue light (60.1). Cutting gets faster toward the end (18 cuts in 60–70 s).
- 77.08–77.41 neon bokeh; 77.41–82.08 TITLE: giant Korean 파친코 used as a window onto amber night-street footage (77.7) → becomes Japanese パチンコ (78.6) → becomes English PACHINKO in gold serif caps on dark plum (79.5–80.5); fades out with the song (79–82.4).
- 82.08–84.6 Apple TV+ card ("NOW STREAMING", silent); 85–94 YouTube end screen.

Cut rhythm: 96 shots in 82.1 s, ASL 0.85 s, median 0.71 s. ASL per quarter 1.08 / 0.85 / 0.79 / 0.68 s = steady acceleration. 69 % of shots under 1 s, only 1 % over 3 s; shortest 0.29 s (69.86); the only long shot is the title (4.67 s). Cuts per 10 s: 7, 11, 13, 8, 10, 15, 18, 13. All cuts checked on before/after pairs for 26–78 s; no false positives seen. Cuts on onsets 13 % vs 11 % chance: the cutting follows dance phrases and moves, not measurable drum hits (onset detection on a full pop mix is weak, so this is not proof of "no beat sync").

Typography:
- Credits: light geometric sans caps with very wide tracking (~0.35 em); closest free: Montserrat 400/500 or Josefin Sans. White. Name cap height ~1.8 % of frame height (8–9 px of 480); label ("STARRING", "EXECUTIVE PRODUCER") ~1.2 %, even wider tracking, sitting just above the name, left-aligned.
- Placement: on the black margins next to a photo panel, or centred inside a black box (~22 % × 20 % of frame) with rough, torn edges that overlaps the photo. In part 2 the credits float small over the footage in the lower third or side.
- Animation (measured on "SOJI ARAI" and "ANNA SAWAI"): quick fade in ~0.25 s, hold ~1.3–1.6 s, quick fade out ~0.25 s or cut off with the shot; the boxes move with the sliding panels. No other type animation.
- Title: three scripts in sequence (Korean → Japanese → English) = the family's three identities. Each is set huge as a matte (letters show night-street footage, background is dark plum ~#160c16). Final PACHINKO: high-contrast serif caps, Trajan-like (closest free: Cinzel 600), ~58 % of frame width, cap height ~13 % of frame height, with a ball-like dot over the I; gold from the footage inside the letters.

Colour/grade: part 1 = black canvas + one duotone per photo (amber ~#d99a2b, magenta ~#c2185b, teal ~#2bb3b1, red-orange ~#d94f2a), film grain and scratches. Part 2 = saturated retro pop: machine red ~#c8102e, stool orange ~#e8762b, cyan ~#7fd4d0, pink ~#f2a0b8, bloom on lights, warm skin. Title = dark plum + amber gold. Only 7 % of samples mostly empty. ~2.2:1 letterbox (active 388 of 480 rows).

Camera/shots: live action. Symmetric one-point-perspective wides down the aisle (locked or slow dolly), medium shots of actors dancing straight to the lens, extreme close inserts (feet, hands, machine parts), archive stills with slight slide/push. Cast perform with big, loose, happy movement.

Transitions: hard cuts only (95), plus panel slides/split screens in part 1; the title changes language by a type morph. No dissolves.

Sound: a 1960s pop-rock song with lead vocal ("Let's Live for Today" by The Grass Roots — known for this sequence, not verified by listening here). Measured: dense and compressed: −15..−17 LUFS momentary for 0–36 s, a lift to −11..−13 around 38–48 s (loudest −11 at 48 s, likely a chorus), −12..−15 to the title, fade from 79 s to silence at 82.4. Integrated −16.1 LUFS, LRA 5.1 LU, true peak −1.8 dBFS. The Apple TV+ card is silent.

What makes it premium:
- A real emotional contrast: tinted archive history first, then present-day joy; the dance makes the drama feel human.
- Cast as performers (stars dancing badly-on-purpose and well), not as credit headshots.
- Strict colour logic per section (duotones on black → saturated parlour → gold on plum).
- Tiny, wide-tracked credits leave the image alone.
- The three-language title states the show's theme in 4 seconds.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Part 1 (first third): black 1920×1080 stage with a 2.2:1 letterbox (bars 64 px). Archive stills as 2–3 panels (each 30–45 % width) with a torn-edge SVG clip-path; tint with CSS: filter: grayscale(1) contrast(1.2); mix-blend-mode color over a solid fill (#d99a2b / #c2185b / #2bb3b1). Slide panels: tl.fromTo(panel, {xPercent: 8}, {xPercent: -4, duration: 1.0, ease: "none"}). Cut every 1.0 s.
- Credits: Montserrat 500, uppercase, 20 px name / 13 px label on 1080p, letter-spacing 0.35em / 0.45em, white; optional black box (420×210 px, torn edges, opacity 0.92) overlapping a photo edge. tl.fromTo(credit, {opacity:0}, {opacity:1, duration:0.25}).to(credit, {opacity:0, duration:0.25}, "+=1.5"), or let the next cut remove it.
- Part 2: full-frame dance footage, saturation +25 %, warm highlights; cuts accelerate from 1.1 s to 0.65 s average; cut on dance accents (spins, arm throws), not on every beat; drop in a macro insert every ~6 shots.
- Title: three text layers (Noto Sans KR 900, Noto Sans JP 900, Cinzel 600) used as a mask over amber street footage: CSS background-clip: text with the video in an SVG <mask>; swap layers every 0.9 s with a 0.2 s cross-fade; final layer holds 1.5 s, then fade 1.5 s together with the music.
- Audio: one upbeat vintage song with vocals at about −16 LUFS integrated, no SFX, fade the song under the title; silent end card.
