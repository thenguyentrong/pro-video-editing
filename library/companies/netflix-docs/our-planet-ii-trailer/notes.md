# OUR PLANET II | Official Trailer | Netflix  (Netflix, 2023-05-31, 1:37 file = 83.5 s trailer + 13 s YouTube end screen, 16:9, YouTube / Netflix channel)
URL: https://www.youtube.com/watch?v=ST1sMntiQj4
Purpose: trailer for a nature documentary series
One-sentence point: animals all over the planet must travel to survive; the series follows those journeys, from June 14 on Netflix.

Structure (trailer only, 0–83.5 s):
- 0–11.3 OCEAN OPEN: orca fins at the surface (2.4 s), orcas underwater, a seal, a wave with a rainbow, a turtle hatchling macro at golden hour (2.2 s), hatchlings on the sand (2.3 s). Shots 1.1–2.4 s. Small grey "NETFLIX" bug top-right on all footage.
- 11.3–32 JOURNEYS BUILD: a 3.9 s top-down aerial of surf and a beach full of hatchlings (the longest footage shot), snow plain, pronghorn, whales underwater, a bird colony aerial, salmon, a shoreline aerial, penguins on ice. 1.0–2.3 s shots, mostly on a steady 1.04 s grid in 26–31 s.
- 32–35.2 BIG WIDE: 3.25 s aerial of a mass migration (wildebeest-like herd on dust).
- 35–64.8 SPECTACLE MONTAGE (densest, 9 cuts per 10 s in 50–60): lion in a tree, a cat's face macro, dust storm, glacier bay, wolves in snow, red crabs crossing a road and a house step, crocodile eye macro, walrus, polar bear hunting a seal, a dust devil. From 53 to 64 s almost every shot is 1.00–1.08 s long (cut on the beat).
- 58.5–59.8 CARD "LIFE MUST MOVE" over a cliff/glacier aerial; 61.9–62.8 CARD "TO SURVIVE" over a mountain plain at dusk (cards sit on footage, not black).
- 64.8–66.7 PAYOFF ACTION: a puma takes down a guanaco at full speed.
- 66.7–77.4 TITLE: a glowing 3D ring flies through the frame (ring wipe from the chase into black), chrome 3D letters fly past the camera and settle into the flat lockup "OUR ◯ PLANET II" with a teal glowing eclipse ring (locked from ≈71 s, held to 77.4).
- 77.4–80.5 "ONLY ON NETFLIX / JUNE 14" on Netflix's vertical light bars (red, purple, blue).
- 80.5–83.5 Netflix N and wordmark sting; sound out at 83.

Cut rhythm: 46 shots in 83.5 s, ASL 1.82 s, median 1.15 s (adaptive detector; 3D title counted as one 12.6 s shot with the chase). Footage-only part (0–64.8 s): 44 shots, ASL ≈1.47 s. ASL per quarter 1.90 / 1.39 / 1.16 / 4.17 s. Only 6.5 % of shots under 1 s (shortest 0.83 s): this trailer never flashes; it keeps a steady ≈1-second pulse. Cuts per 10 s: 5, 4, 8, 6, 7, 9, 5, 1. 24 % of cuts on an audio onset vs 11 % by chance: clear beat cutting, strongest in 53–64 s (11 shots of 1.0–1.08 s).

Typography:
- Cards: thin geometric sans caps (Gotham Light-like; closest free: Montserrat 300), white, tracking ≈0.15 em, cap ≈6 % H, one line, centred (y ≈52 % and ≈57 %), 2–3 words, held 0.9–1.3 s, soft fade in/out, laid over a wide landscape aerial with empty sky or rock.
- Title lockup: same thin wide-tracked caps, cap ≈4.5 % H, the "O" replaced by a teal glowing ring ≈40 % H on a black-to-teal vignette; built by 3D chrome letters flying through camera (≈4 s), then held ≈6 s.
- Date card: Netflix sans, "ONLY ON NETFLIX" small light caps (≈3 % H) over "JUNE 14" bold (≈7 % H), centred, on vertical light bars.
- Corner bug: "NETFLIX" grey condensed caps ≈3 % H top-right (x ≈93 %, y ≈5 %) on all footage, hidden on cards.

Colour/grade: natural, clean, high dynamic range nature cinematography: ocean teal-blue, golden-hour sand and grass, white ice; no stylised grade. Title world switches to deep black-teal with one glowing ring. Full 16:9, no letterbox.

Camera/shots: blue-chip natural history: long-lens close-ups of animals, macro eyes, gyro-stabilised aerials of mass movement (top-down beaches, herds, colonies), underwater, one high-speed predator chase. Every shot is a hero shot; no people at all.

Transitions: hard cuts on the beat for all footage; text cards fade; one 3D ring wipe into the title; light-bar wipe into the Netflix sting.

Sound: (I could not listen; from level data.) Integrated -14.4 LUFS, LRA 5.5 LU, true peak -0.2 dBTP. Even, music-driven level (-15…-20 dBFS in 1 s RMS), louder in the spectacle (-11…-12 at 35–40 s). Biggest rise +20 dB on the date card at 77.45 s. No drop-outs: the trailer never goes silent.

What makes it premium:
- Hero shots only, each 1–2 s, cut on a steady pulse: the footage carries the trailer, not tricks.
- Story told in two 2–3-word cards on landscapes, then one predator payoff before the title.
- Mass-movement aerials (beach, herd, colony) as the visual idea of "journeys".
- A title made of one simple symbol (the glowing ring) that the 3D letters resolve into.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080):
- 40–45 nature shots: 30 % macro/close animals, 30 % aerials of many animals moving, 20 % underwater/ocean, 20 % action. Order: calm ocean → journeys → spectacle → one chase → title.
- Cut 1.0–2.4 s; in the last 10 s before the title cut exactly every 2 beats (≈1.04 s at 115 BPM). Never under 0.8 s.
- Cards: `font: 300 6vh Montserrat; letter-spacing: .15em; text-transform: uppercase; color:#fff`, centred over an empty part of a wide shot; `opacity 0→1` 0.3 s, hold 1 s, fade 0.3 s; two cards ≈3 s apart.
- Title 10 s: ring `border: .8vh solid #bff; border-radius: 50%; box-shadow: 0 0 4vh #3cf` scales from 6 → 1 through camera (`scale 6→1`, 1.2 s, `power3.out`) as a wipe from the last shot, then letters `300 4.5vh Montserrat; letter-spacing:.3em` fade/slide in 0.8 s; hold 5 s.
- Date card 3 s, logo 3 s. Master -14 LUFS, true peak ≤ -1 dBTP.
- Stock queries: `aerial wildebeest migration`, `sea turtle hatchling macro`, `top down aerial beach waves`, `orca fin ocean`, `crane flock`, `polar bear hunting seal`.
