# The REAL reason the US can't beat Iran  (Johnny Harris, 2026-07-16, 39:30 full / first 150 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=-DDbYSg0Alw
Purpose: history/geopolitics explainer (narrator-led map documentary; Johnny not on camera in this window)
One-sentence point: Iran's behaviour today comes from 2,500 years of being a superpower and then 200 years of being squeezed by empires — the map explains it.

Structure (first 150 s):
- 0.0–3.0 slow push on a dark parchment-texture map, "IRAN" outlined with a soft glow.
- 3.0–47.8 "it's on the news" cold open: CBS, ABC News, Al Jazeera, Global News clips (vertical phone video sits in the middle with a blurred copy filling the sides; broadcaster chyrons kept, e.g. "MASSIVE ANTI-GOVERNMENT PROTESTS IN IRAN"), 1979 revolution archive pillarboxed 4:3, chants subtitled in white sentence case ("God is the Greatest.", "Death to America."), 1900s archive, oil-field archive, an animated map with octagon pins (Russian Empire, Nazi Germany, British Empire, Reza Shah portrait, Anglo-Persian Oil Company barrel) and dotted connector lines (33–39 s), war footage, Khomeini, Khamenei, missile parade. 7–11 cuts per 10 s.
- 47.8–58.1 map montage: the digital map → printed atlases flipped at 0.25 s each (Iran in the same spot), an Arabic-language school map, antique maps with the word "POWER" glowing on each (15 cuts in 50–60 s).
- 58.1–72.0 one 13.9 s map shot: region filled with yellow diagonal hatching, glowing engraved-serif label "SUPER POWER", chapter tag top centre "500BC – 1800AD • IRAN SUPER POWER"; a light-leak flash at 65 s.
- 72.0–76.0 museum artefacts as rounded cards on black (seal impression, cuneiform tablet, statuette, cylinder seal).
- 76.0–84.1 second atlas-flip montage (antique to modern maps, ~0.3–0.4 s each; 16 cuts in 70–80 s).
- 84.1–102.3 one 18.2 s animated map: Qajar Iran (orange hatch) between the Russian Empire (red) and the British Empire (blue), octagon flag pins with name tags; a new chapter tag top centre (too small to read at 480p); 1.5 s audio drop at 85–86.5 s.
- 102.3–112.4 real antique maps filmed on a dark table under a moving light: Persia map on black, push in to "PERSIA" lettering, then a text match-cut montage of the word "PERSIA" from ~14 different engraved maps at a 4-frame cadence (0.17 s each, 107.1–109.4 s), ending on a sweeping light across an old map; light-leak flash (112.0–112.45 s).
- 112.4–150 one 37.6 s continuous map move: Russian pin pushes south, glowing front over the Caucasus, flashes of battle dots, chapter tag "1804–1828 • RUSSO-PERSIAN WARS", then a dark torn-paper card slides in with treaty names in italic serif and bullet lines typing on ("Russia gets exclusive military access to Caspian Sea…").

Cut rhythm (corrected by eye, see metrics manual_corrections): 105 shots in 150 s, ASL 1.43 s, median 0.42 s. ASL by quarter 1.17 / 1.17 / 0.87 / 37.5 s. 69 % under 1 s, 6 % over 3 s. Longest: continuous animated maps 37.6 s (112.4 s), 18.2 s (84.1 s), 13.9 s (58.1 s). Shortest 0.12–0.17 s (map flips, "PERSIA" match-cuts). Cuts per 10 s: 7 9 10 7 11 15 0 16 11 0 16 2 0 0 0. Two speeds only: flip montages at 4–6 cuts per second, and very long camera moves on one animated map. The median is pulled down by the flip montages; the time is spent on the long map shots. Cuts on onsets = chance (48 % vs 52 %).

Typography:
- Map labels: glowing white engraved serif caps, wide letterspacing ("SUPER POWER", ~5.5 % H), light bloom around the letters. Closest free: Cinzel / Cormorant SC (guess).
- Pin tags: white condensed sans caps on a small black tag under each octagon ("NAZI GERMANY", "BRITISH EMPIRE", "QAJAR IRAN"), ~2 % H.
- Chapter tag: a small dark pill top-centre, ~2 % H mono-ish caps "DATE RANGE • CHAPTER NAME" with a red dot separator; stays on for the whole chapter.
- Card text: italic serif for document titles ("Treaty of Gulistan (1813)"), roman serif for bullets, white on a dark torn-paper card, typed on line by line.
- Clip subtitles: white sentence case sans ~3 % H (chants translated).

Colour/grade: antique-paper world — dark vignetted map with paper/terrain texture, desaturated land (~#7C533D–#B89B78 in the light), empires in muted fills with diagonal hatching: Russia brick red (~#532A2E in shadow), Britain slate blue, Iran orange, superpower yellow-green (~#716A26). Heavy vignette, light leaks, a warm film look. News and archive keep their own colours; 4:3 archive is pillarboxed in black.

Camera/shots: no presenter in this window. Archive newsreel, broadcast news, phone video, war footage, museum objects, physical maps shot macro on a table with a moving key light, and 3D-ish camera moves over a 2D textured map (push, pan, tilt with parallax-like vignette).

Transitions: hard cuts in montages, light-leak flashes between "worlds" (65 s, 112 s), dissolves into the physical-map table shots (102.3, 105.0 s), a text match-cut ("PERSIA" in the same screen position) — the signature move.

Sound: integrated −16.3 LUFS, loudest −10 LUFS momentary at 4 s (news clip). 50 ms RMS median −21.0 dBFS, p10 −34.2 dBFS, only 1.3 % of windows below −45 dBFS → a fuller, continuous bed (~13 dB under the voice median) than in his talk-driven films. One drop: 1.5 s at 85–86.5 s (−17 → −41 LUFS) at the start of the long map, then the narration resumes. Clip audio (chants, protests) is let through briefly under the voice.

What makes it premium:
- A whole visual language for maps: textured paper, hatched regions, octagon pins with faces/flags, glowing serif labels, a persistent chapter tag — consistent for minutes.
- Real artefacts and real antique maps, filmed physically with light, used as rhythm (flip montages, match-cuts).
- Extreme contrast in pace: 0.17 s flips vs 18–38 s single map moves.
- The news cold open proves relevance before the history starts.

Recipe (real footage + HTML/GSAP):
- Map ground: a high-res terrain/paper texture PNG with `filter: sepia(.35) saturate(.7) brightness(.85)`; vignette `radial-gradient(ellipse at center, transparent 45%, rgba(0,0,0,.65) 100%)`; regions as SVG paths with `fill: url(#hatch)` where `#hatch` is a 45° pattern (stripe 3 px, gap 5 px) in the region colour at 55 % opacity. Camera = a wrapper div: `gsap.to(cam,{scale:1.35,x:'-12vw',y:'6vh',duration:12,ease:'sine.inOut'})`.
- Octagon pin: `clip-path: polygon(30% 0,70% 0,100% 30%,100% 70%,70% 100%,30% 100%,0 70%,0 30%)` around a flag/portrait, 9 % H, white 3 px border; name tag `font:700 1.9vh 'Oswald'; background:#111; color:#fff; padding:.15em .4em`. Pop with `scale 0→1, 0.35 s, back.out(2)`; dotted connector `stroke-dasharray:2 4; stroke:#C0392B`, draw 0.8 s.
- Glow label: `font:600 5.5vh 'Cinzel'; letter-spacing:.12em; color:#fff; text-shadow:0 0 8px rgba(255,255,255,.8),0 0 24px rgba(255,240,200,.5)`; fade + `letterSpacing` 0.2em→0.12em over 1.2 s.
- Chapter tag: `top:2vh; left:50%; transform:translateX(-50%); background:rgba(10,10,10,.85); font:500 1.9vh 'IBM Plex Mono'; color:#ddd` with a 0.6vh red dot; keep for the whole chapter.
- Match-cut montage: 12–14 scans of the same word, each aligned so the word sits at the same centre and size; 4 frames each at 24 fps (`tl.set(img[i],{autoAlpha:1}, t + i/6)`), a soft paper-rustle/click per cut, stop on the one you talk about.
- Atlas flip: 8–10 map photos at 0.25 s each, Iran centred; then hold.
- Treaty card: dark card #342A21 with a torn-edge mask PNG, slide in `x:20vw→0, 0.6 s, power3.out`; title `italic 600 2.6vh 'Cormorant Garamond'`; bullets typed (`stagger:.03` per char).
- Light leak between sections: a full-frame leak video in `mix-blend-mode:screen` for 0.4–0.5 s.
