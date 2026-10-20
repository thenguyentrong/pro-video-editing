# 28 Years Later: The Bone Temple | New Trailer  (Sony Pictures, 3 Dec 2025, 139.6 s incl. 7.1 s silent poster card, 16:9 file / 2.39:1 picture and cards, YouTube)
URL: https://www.youtube.com/watch?v=QlF68NIz8dg
Purpose: second (main) trailer, about 6 weeks before release
One-sentence point: in the wild, infected north a doctor's bone temple and a violent cult meet, and "change is coming".

## Structure (beats with timestamps; % of 139.6 s)
- 0.0–25.0 **dialogue cold open (18 %)**: a weathered face in close-up, towers of bones against a pink sky, a forest of bone pillars from below (2.9 s), the cult leader talking, a stag silhouette, a forest hillside (ASL ≈1.5 s).
- 25.0–34.9 **the silence**: a boy alone in the forest, then 5.75 s of near-silence (29.05–34.8 s, floor −52 dBFS) over slow stalking shots, broken by an attack and a +42.4 dB hit at 34.9.
- 35.4–44.5 struggle in the forest, a calm lake wide.
- 44.5–51.0 **studio logos late** (Sony, Columbia, at 32 %), with black holds of 0.7 and 1.4 s around them.
- 51.0–75.0 **Act 2**: candle-lit interiors, an aerial of ruins (3.3 s), the cult in tracksuits, an infected close-up, a train carriage (ASL ≈1.2 s).
- 74.7–76.0 **true silence 1.3 s at −72 dBFS**, then a +60 dB rise into a wild-man close-up (the scare beat).
- 76.0–90.0 a field: a man with a rifle, a figure far away, the doctor in a 4.2 s close-up; another dip (83.5–85) and a +33 dB hit.
- 90.0–92.2 **card "THIS / JANUARY"** (2.1 s, 64 %), hit +27 dB.
- 92.2–114.5 **tagline montage**: "CHANGE" (1.4 s, 72 %), "IS" inside a burning ring (1.3 s, 77 %), "COMING" over a lake landscape (1.0 s, 80 %), shots between them at 0.5–1.4 s. Densest window 110–120 s, 13 cuts per 10 s (79–86 %).
- 114.5–117.9 black + silence (two short gaps of 0.4–0.65 s), then the **biggest hit +48.5 dB at 117.9** (loudest 0.5 s, −10.5 dBFS) and a fire montage at ≈0.5 s per shot.
- 123.3–128.2 **title**: the franchise badge, then "THE BONE TEMPLE" builds in red (4.9 s, at 88 %), music falls to −35 dBFS.
- 128.2–132.5 credits ("from director … writer … and producer …", 2.3 s) and "THEATRES ONLY / JANUARY 16" (2.0 s).
- 132.5–139.6 poster card in digital silence.

## Cut rhythm
- 95 shots (adaptive detector + 2 card changes by eye). **ASL 1.47 s**, median 1.17 s.
- ASL per quarter 1.74 · 1.45 · 1.34 · 1.25 s (a steady speed-up). 31 % under 1 s, 6 % over 3 s. 40.8 shots per minute.
- Cuts per 10 s: 5 7 5 4 7 6 9 9 3 7 11 13 5 1. Shortest 0.33 s.
- Cuts on audio onsets 29 % vs 19 % chance. Speech in ≈100 s (72 %).

## Typography
- Heavy grotesque caps (closest free: Archivo Black), white with a rough stone texture, centred, inside the letterbox, on a near-black plate with dark red ember texture.
- Sizes (≈): "JANUARY" 17 % H with "THIS" 10 % H above; one-word cards 13–20 % H; the title in red, two lines ≈13 % H each, under a round franchise badge.
- **The tagline is split into four cards** (THIS JANUARY / CHANGE / IS / COMING), one or two words each, 1.0–2.1 s, with footage in between; the last word sits over a landscape instead of a plate, the "IS" sits inside a burning ring.
- In and out by hard cut; title letters build in from the dark.

## Colour / grade
2.39:1 (62 px bars at 480p). Lush green forests and fields in flat daylight, pink and orange skies behind bone structures, candle-lit and fire-lit interiors; red is kept for the title.

## Camera / shots
Close-ups in long lenses, low-angle bone architecture, aerial ruins, handheld forest chases; a few very wide fields with tiny figures.

## Transitions
Hard cuts; black holds around the logos and before the final hit; no dissolves.

## Sound
- Integrated **−15.3 LUFS**, LRA 10.0 LU, true peak +0.4 dBTP.
- **Silence is the main tool**: 7 drop-outs or silences (0.35–5.75 s), floors −45 to −72 dBFS, each followed by a rise of +33…+60 dB. The 5.75 s silence at 21–25 % is the longest held quiet in this set.
- After the final hit the mix stays at −11…−14 dBFS for the fire montage, then drops under the title.

## What makes it premium
- A long silence early in the trailer, not only before the title.
- Logos moved to one third of the runtime: the story owns the opening.
- A four-card tagline with images between the words, each card designed differently (plate, ring of fire, landscape).
- Beauty and horror side by side: pink skies, green fields and bones.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Bars 138 px (2.39:1) on everything.
2. 0–25 s: dialogue open, ASL 1.5 s, two or three held low-angle images of 2.5–3 s.
3. 25–35 s: mute the music for 4–6 s under slow stalking shots (room tone only, −50 dBFS), then a +40 dB hit.
4. Logos at ≈30 %, with 0.7–1.4 s black holds.
5. Tagline cards: `font: 400 150px "Archivo Black"; color:#f2f2f2; text-transform:uppercase` with a stone texture via `background-clip:text`, on `#070505` with a dark red smoke image at opacity .35. One card per word, 1.0–2.1 s, hard cuts, shots of 0.5–1.4 s between them.
6. 1–3 s of silence, a +45 dB hit, 6 s of shots at 0.5 s, title in `#b5121b` building 2–5 s, credits 2.3 s, date 2 s.
7. Master −15 LUFS, true peak −1 dBTP.
