# "Steve Rogers Will Return" — Avengers: Doomsday teaser  (Marvel Studios, 23 Dec 2025, 1:21 (80.6 s), 16:9 with 2.40:1 letterbox, YouTube)
URL: https://www.youtube.com/watch?v=UiMg566PREA
Purpose: teaser (one of a series of character teasers on the same channel: "Thor / The X-Men / Steve Rogers Will Return"; probably also shown in cinemas before Christmas releases — not verified)
One-sentence point: Steve Rogers, retired and a father, will come back.

## Structure (beats with timestamps)
- 0–6.4 s **drone**: golden-hour farm road, a windmill turning (one shot).
- 6.4–11.1 s **static wide** of a farmhouse (4.6 s, nothing moves).
- 11.1–19.1 s **details**: motorcycle kickstand (low angle), a hand puts a helmet on a Triumph tank, wedding ring visible.
- 19.1–27.0 s **front door**, static 7.9 s; a figure appears behind the glass at ~24 s.
- 27.0–34.1 s **the suit**: hands take the folded Captain America suit out of a box (star revealed at ~29 s), close the box.
- 34.1–35.6 s **black** (1.5 s) on the loudest strike.
- 35.6–56.5 s **one 20.9 s shot**: fade up, Steve holding a baby by a window, a slow push-in from behind his shoulder to his face, smiling. The face is only shown here, from ~47 s to 56.5 s.
- 56.5–67.9 s **text on black**: "Steve Rogers" → "Will Return" → "In Avengers: Doomsday", then a slow fade-out.
- 68.3–77.8 s **end card**: Doom's green-lit window room, "December 18 2026", then a countdown clock 11 : 24 : 15 : 00 : 00 ticking each second.
- 77.8–80.6 s black, sound fades to digital silence.

## Cut rhythm
- 12 boundaries incl. 3 black holds → ASL 6.62 s (median 4.9). Picture only: **8 live-action shots in 55 s, ASL ~6.9 s**. 0% of shots under 1 s, 75% over 3 s.
- Cuts per 10 s: 1 · 3 · 1 · 3 · 0 · 1 · 1 · 1. Shot lengths in order: 6.4 · 4.6 · 3.5 · 4.5 · 7.9 · 5.2 · 1.9 · (black 1.5) · 20.9 · (text 11.8) · 9.5.
- This is the opposite of the trailer grammar: the longest shot (20.9 s) is the payoff, and the edit gets *slower* toward the end.

## Typography
- One line of text on black, built word by word: "Steve Rogers" fades in at 57.0 s (0.75 s fade), "Will Return" at 59.5 s, "In Avengers: Doomsday" at 62.0 s (1.0 s fade). Full line holds to 65.25 s, then a 2.25 s fade-out. 2.5 s between word groups.
- The left edge stays fixed at x = 15.5% and the line grows to the right (ends at 84.4%), so the finished line looks centred. Vertical centre 49.5% of the frame.
- Size: ink height 3.3–3.75% H including descenders (cap height ~2.5% H), i.e. small. Semibold humanist sans (looks like Segoe UI / Frutiger; closest free match: Source Sans 3 SemiBold or Noto Sans, guess), **Title Case**, very wide tracking (~0.3 em). New words appear grey and brighten to white.
- End card: "December 18 2026" in small spaced semibold text, centred; the countdown digits ~3.5% H with colons and tiny unit labels; "THIS FILM IS NOT YET RATED" box + "© 2025 MARVEL".

## Colour / grade
Warm, nostalgic Americana: golden-hour amber, cream house, teal sky accents; soft contrast, shallow depth of field in the details and the baby scene. End card switches to Doom's green-black. 2.40:1 bars (62 px of 480).

## Camera / shots
Drone (opening), locked-off static wides (farmhouse, door), low-angle inserts of hands and objects (helmet, ring, suit), one long slow push-in for the emotional payoff. No action, no VFX, no dialogue on screen.

## Transitions
Hard cuts between the first seven shots; cut to black on a sound strike (34.1 s), fade up into the baby scene (35.6–36.2 s), cut to black for the text, fade up into the end card (68.0–68.5 s).

## Sound
- Integrated −15.2 LUFS; median momentary −18.9 LUFS.
- The score is a series of single strikes (piano or low orchestral notes — guess, I cannot hear it) at 0, 6.5, 12, 16.5, 21, 30.5, 34, 39, 41.5, 47, 50, 57, 59.5, 62.5 and 68 s; each one decays 15–25 LU over 4–5 s.
- Longest lull: 24.0–30.5 s (−17 → −39 LUFS) over the door and the box.
- Loudest moment: 34.0 s (−8.6 LUFS M), the strike on the cut to black before the baby scene.
- Each word group and the date card lands on a strike (57.0, 59.5, 62.5, 68.0 s). The countdown has one tick per second (71–76 s).

## What makes it premium
- It withholds: no face until ~47 s, no name until 57 s, no logo in the body at all.
- Objects tell the story (ring, helmet, folded suit, baby); the viewer does the work.
- Long static frames and one 21 s take: confidence that the image is enough.
- Small, quiet, perfectly spaced text that builds word by word on musical strikes.
- The countdown gives a tiny teaser the weight of an event.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. 6–8 shots of 3.5–8 s each: one drone or wide establishing, one locked-off static, 2–3 detail inserts of meaningful objects, one reveal object. Then 1.5 s black on a sound strike.
2. Payoff: one 15–20 s take with a slow push (`scale 1.0→1.12`, `ease:"none"`).
3. Text on black: one line, `font: 600 26px/1 "Source Sans 3"; letter-spacing:.3em;` left edge at 15.5% of the width, words in separate spans. Each group: `opacity 0→1` + `color #8a8a8a→#ffffff` over 0.75 s `power1.out`, 2.5 s apart, each on a music strike. Hold 2.25 s, fade the whole line out over 2.25 s `power1.inOut`.
4. End card: dark brand background, date in small caps, then a countdown computed from timeline time (one tick per second with a tick SFX).
5. Sound: sparse single notes with long decay, a −35 LUFS lull before the reveal object, master −15 LUFS. Letterbox 2.40:1.
