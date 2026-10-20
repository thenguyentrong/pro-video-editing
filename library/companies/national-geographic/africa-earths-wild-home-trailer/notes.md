# Africa: Earth's Wild Home | Official Trailer | National Geographic  (National Geographic, 2026-09-10, 1:28 file = 72.5 s trailer + 15 s channel end screen, 16:9, YouTube / National Geographic channel)
URL: https://www.youtube.com/watch?v=dK6vnPToC_E
Purpose: trailer for a blue-chip nature documentary series (sponsor-presented)
One-sentence point: the series travels the whole African continent, from rainforest to desert and coast, to show how its animals live; new series on a set date.

Structure (0–72.5 s):
- 0–0.5 black, sound rises +31.6 dB at 0.5 s.
- 0.5–12.4 LOGO IN THE WORLD: an aerial of a jungle waterfall where the brand's yellow rectangle sits inside the falls (1–3.5 s), an elephant in the river, a gorilla, a camel caravan on dunes, a turtle and a shark underwater, rock desert, a young gorilla, a dead-tree pan. Shots ≈1 s. Show bug top-left (series logo, ≈3 % H), streamer logos top-right.
- 12.4–16.8 GLOBE: a dip to black, then a 3D Earth turning to Africa (4.4 s, the second-longest shot).
- 15.8–17 CARD "FROM / NATIONAL GEOGRAPHIC" on a desert dune (+17.7 dB at 15.8 s, the biggest hit).
- 17–37 WILDLIFE MONTAGE: forest aerial, antelope, black leopard, baboons, then CARD "NARRATED BY ACADEMY AWARD® NOMINEE / [name]" over running buffalo silhouettes (20.8–22.3), camels at a water hole, chimps, an elephant shrew leaping, a frog, an insect, a tortoise and a bird beak to beak (comedy beat, 32–36).
- 37–64.9 SPECTACLE (densest, 10 cuts per 10 s in 50–70): snow on a forest and a monkey in snowfall, hyena among flamingos, a carpet of crabs, a forest river, eagle, pelicans, Kilimanjaro over herds, elephants at sunset, desert arch, dunes, waterfall, bush fire, kingfisher, hatchling at sunset, hippo, elephants and antelope, flamingos taking off, baboons, lechwe running, a lion's breath in cold light. Shots 0.33–1.2 s at the end.
- 64.9–70.3 TITLE: a lemur, then "AFRICA" in 3D gold letters flies out of the frame and lands on a satellite view of Africa: "AFRICA / EARTH'S WILD HOME", "NEW SERIES / FRIDAY OCT 2 8/7c", network and streamer logos (≈3 s hold).
- 70.3–72.5 "PRESENTED BY [sponsor]" card on a monkey in grass; sound fades from -37 to -63 dBFS (1.25 s silence at 71.3).

Cut rhythm: 62 shots in 72.5 s, ASL 1.17 s, median 0.92 s (adaptive detector; 3D title and end card counted as a 5.4 s shot). ASL per quarter 1.29 / 1.07 / 1.21 / 0.95 s. 56.5 % of shots under 1 s, 5 % over 3 s; shortest 0.33 s (61.6–62.3), longest the title (5.4 s), the globe (4.4 s) and the snow monkey (4.1 s). Cuts per 10 s: 7, 8, 9, 7, 9, 10, 10. Cut-on-onset 23 % (the chance figure in metrics.json is broken for this clipped run; full-file run gave 23 % vs 20 %).

Typography:
- Cards: gold geometric caps with a warm gradient and slight bevel (closest free: Montserrat 700 / Josefin Sans 700, gold `#f1c14b`-like), cap ≈6.5 % H; small line above in white spaced caps ≈2.8 % H, tracking ≈0.2 em; centred at y ≈38–45 %.
- Narrator card: small white spaced caps ≈2.5 % H over the name in big warm caps ≈6 % H with a soft glow, on silhouettes against a bright sky.
- Title: "AFRICA" ≈11 % H gold bevel caps, "EARTH'S WILD HOME" white spaced caps ≈3 % H, date block in yellow and white caps ≈2.5 % H, logos at the bottom; on a satellite map.
- Sponsor card: "PRESENTED BY" white spaced caps ≈2.5 % H + the sponsor wordmark ≈5 % H, centred on footage.
- Bugs: series logo top-left (≈3 % H), streamer logos top-right (≈2.5 % H), on every footage shot.
- The brand's yellow rectangle is placed inside the first landscape (logo as part of the world).

Colour/grade: saturated warm nature grade: golden deserts, green jungles, teal water, orange fire and sunsets. 16:9.

Camera/shots: aerials, long-lens wildlife, macro, underwater, slow motion (breath, water), a CG globe; no people.

Transitions: hard cuts on a rising score; two short dips to black (12.4–13.0, 64.9); 3D title fly-in.

Sound: (I could not listen; from level data.) Integrated -19.2 LUFS (whole file), LRA 4.3 LU, true peak -4.6 dBTP: a steady orchestral bed at -19…-22 dBFS (3 s RMS), no drop-outs until the 1.25 s tail at 71.3. Narration presumably over it (credited on screen).

What makes it premium:
- The brand mark is built into the first shot (the yellow frame inside a waterfall).
- Steady 1-second pulse of hero shots across every habitat, accelerating to 0.33 s at the end.
- Credit cards (brand, narrator) are placed on the most graphic shots (a dune, silhouettes).
- One comedy beat (tortoise and bird) inside the spectacle.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- 60 hero shots; ASL 1.1–1.2 s, last 10 s at 0.33–0.6 s; habitats in a sequence (water → forest → desert → snow → coast → fire).
- Logo-in-world: place your mark (outline only, 6 % H) over the brightest vertical element of the first aerial, `opacity 0→1` 0.3 s, hold 2 s.
- Cards: `font: 700 6.5vh Montserrat; background: linear-gradient(#ffe08a,#c98a1e); -webkit-background-clip:text; color:transparent; text-shadow:0 2px 8px rgba(0,0,0,.35)`, eyebrow `500 2.8vh; letter-spacing:.2em`, on the most graphic shot, 1.2–1.5 s.
- Title: 3D-style letters `scale 3→1, z-blur` 1 s onto a satellite map, then date block `stagger .1`. Sponsor card 2 s, fade audio to silence over 1.5 s. Master -16 to -19 LUFS.
- Stock queries: `africa waterfall aerial`, `camel caravan dunes`, `fiddler crabs mass`, `flamingos taking off`, `earth from space africa`.
