# I Survived The Most Extreme Places On Earth  (MrBeast, 2026-09-05, 23:27 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=gTKS8SAwUzE
Purpose: entertainment / adventure race (three two-person teams, three biomes)
One-sentence point: Three teams race across a jungle, a desert and a polar ice field to reach their own rescue helicopter, and the first team there wins $100,000 for their mothers.

Data note: full upload 23.5 min; first 300 s trimmed with ffmpeg and measured. The scene detector missed many low-contrast jungle and snow cuts, so this film uses the adaptive detector with 3 false cuts dropped and 2 white-flash cuts added (see `manual_corrections` in metrics.json). No sponsor read in the first 300 s.

## First 30 s (hook)
- 0.0–3.5 one team in the jungle, a quick push-in, host starts the premise at once (we are in X, they are in Y and Z).
- 3.5–7.4 the frame splits into three vertical panels (polar / jungle / desert), each team in its own panel, the panels slide in one after another on the words: the cast and the three worlds in one image.
- 7.4–10.0 back to single shots; 8–9 s a wide polar drone shot of two tiny figures.
- 10.0–14.5 three-panel top-down drone pull-backs (team becomes a dot), then glowing route lines draw across each panel in the team colour (cyan, green, orange) from start to goal (12–14 s): the task as a line.
- 14.5–19.9 the goal: a helicopter in the desert outlined in neon green, then the prize "$100,000" in neon green glow floats over it (16–19 s) on the word "wins". Stakes stated by ≈15 s.
- 19.9–27.6 taunts between teams (≈17–19 s), a polar whiteout shot, then three-panel start line with a checkered strip under each team and a countdown (21–26 s).
- 27.6–30 race starts: selfie-cam running shots, one per team.
- Cuts in 0–30 s: 9 (but the three-panel split screens hold 3 shots each). Loudness of the first 30 s: −9.0 LUFS.

## Retention devices seen in 0–300 s
- Standings every ~100 s: a race HUD bottom-left (team avatar circle + coloured bar + percentage) at ≈101 s and ≈287 s, and a 3D diorama board on a black grid with one biome slab per team, the team badge and "10 %" on top (≈204–211 s).
- "Each team has a disadvantage" round at 37–92 s: one biome per team with its problem (water weight, a written danger list read aloud with 0.5–0.6 s cutaway inserts of each animal, whiteout).
- Teaser line at ≈85–92 s that obstacles will "change the direction" of the race.
- Small set pieces every 30–60 s: a fall at the start (≈32–36 s), the creek bridge (≈155–182 s), finding water (≈188–203 s), carrying a partner's bag (≈228–236 s), a big view reveal (≈242–250 s), a skeleton found (≈297 s).
- Cross-cutting between the three teams every 20–60 s, often with a direct taunt to another team.

Structure (first 300 s): hook 0–27.6 → start 27.6–37 → disadvantages per biome 37–92 → first standings 92–107 → polar camp decision 107–135 → jungle creek set piece 135–183 → water 183–204 → diorama standings 204–212 → desert/jungle progress 212–268 → contrast cut (hot vs cold) 268–287 → standings 287 → new discovery 297.

Cut rhythm: 116 shots in 300 s, ASL 2.59 s, median 2.12 s. ASL by quarter 2.21 / 3.75 / 2.50 / 2.14 s (the polar whiteout and the creek scene slow the second quarter). 11.2 % under 1 s, 28.4 % over 3 s. Longest 8.5 s (polar whiteout 116.9 s; jungle walk 141.8 s), 7.6 s (288.6 s). Shortest 0.2–0.57 s (the danger-list inserts at 63.7–68.2 s: 8 cuts in 60–70 s, the densest window). Cuts per 10 s 1–8, typically 3–5. Cuts on onsets 42 % vs 43 % chance.

Typography:
- Prize label: heavy rounded slab-ish sans caps, neon green fill (≈#39FF14) with a thick dark green outline and a wide green outer glow, cap height ≈8 % H, floats above the object it belongs to. Closest free: Lilita One or Luckiest Guy.
- Route lines: 3–4 px glowing lines in team colours (cyan, green, orange/yellow) with a white core, drawn on over ≈1.5 s; the whole panel then floods with the team colour for a few frames.
- Race HUD: three rows bottom-left, round avatar photo (≈7 % H), a short rounded bar in the team colour (yellow/blue/green), percentage in white bold sans ≈4 % H. Slides in from the left.
- Diorama label: team badge + neon "10 %" in green glow on top of a 3D terrain slab on a black grid floor.
- No subtitles, no name lower thirds in this window.

Colour/grade: each biome keeps its own strong colour: jungle saturated green with red team jackets, desert warm orange-pink with violet sky, polar near-white with cyan-tinted shadows. Colour-coded team clothing (red / dark / teal) matches the HUD colours. High saturation, no grain, no letterbox.

Camera/shots: wide-angle selfie and chest cams worn by the teams, a follow camera operator (who also struggles on screen), drones for top-down pull-backs and scale shots, triptych split screens to compare the three teams, 3D CG for standings and the goal outline, illustrative inserts for spoken lists.

Transitions: hard cuts; panel slides for split screens; white glow flashes between biomes (204 s, 211 s); colour flood on the route-line panels; the goal outline glows on over the real helicopter shot.

Sound: integrated −11.6 LUFS (the quietest of the three films studied), LRA 6.8 LU, true peak +1.3 dBTP on the stream. 50 ms RMS p10 −27.9 / p50 −17.2 / p90 −11.4 dBFS: still a dense bed, ≈11 dB from median to p10. Drop-outs only 0.30–0.45 s (59.55, 141.5, 234.3 s), each followed by a +36 to +40 dB re-entry. Biggest rise +47 dB at 285.1 s (standings sting). Loudest 0.5 s at 168.3 s (the tree falls for the bridge). Music marked through most of the window.

What makes it premium:
- The comparison is built into the picture: three panels, three colours, three progress bars; the viewer always knows who leads.
- Real places at real scale (drone pull-backs), with CG used only for game information (route, goal, standings).
- Each team has a stated disadvantage, so every cut to a team pays off a question.
- Set pieces arrive every 30–60 s and each is solved on camera.

Recipe (real footage + HTML/GSAP):
- Triptych: three `<video>` panels `width:33.33vw; height:100vh; object-fit:cover` with a 6 px white gap; `gsap.from('.panel',{yPercent:100,duration:.35,ease:'power3.out',stagger:.4})` on the three team names in the voice.
- Route line: SVG path per panel, `stroke:#3CFF6B; stroke-width:4; filter:drop-shadow(0 0 6px #3CFF6B) drop-shadow(0 0 16px #3CFF6B)`, draw with `strokeDashoffset` over 1.5 s `power1.inOut`, then `gsap.to(panel,{backgroundColor:'rgba(60,255,107,.35)',duration:.15,yoyo:true,repeat:1})`.
- Prize label: `font:400 8vh 'Lilita One'; color:#39FF14; -webkit-text-stroke:3px #0B4D12; text-shadow:0 0 12px #39FF14,0 0 32px #39FF14`; `gsap.from(label,{scale:.6,autoAlpha:0,duration:.3,ease:'back.out(2)'})`, hold 2–3 s.
- Race HUD: rows `left:6vw; bottom:6vh`, avatar `height:7vh; border-radius:50%`, bar `height:2.2vh; border-radius:1.1vh; width:calc(var(--p)*1%)` in team colour, value `font:800 4vh 'Montserrat'; color:#fff`; slide in `x:-40`, 0.3 s; animate bars to new values over 0.8 s.
- Pace: ASL ≈2.5 s, standings every ~100 s, a set piece every 30–60 s, cross-cut teams every 20–60 s.
- Mix: continuous bed, short 0.3–0.5 s drops before each standings reveal, master −14 LUFS / −1 dBTP for delivery.
