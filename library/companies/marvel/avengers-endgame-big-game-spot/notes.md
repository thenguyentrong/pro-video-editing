# Avengers: Endgame — "Big Game" TV Spot  (Marvel Studios, 3 Feb 2019, 0:30 (30.0 s), 2.41:1 file (1920×798, no bars), Super Bowl LIII broadcast + YouTube)
URL: https://www.youtube.com/watch?v=-iFq6IcAxBc
Purpose: TV spot (Super Bowl, 30 s)
One-sentence point: the world is empty after the snap, the survivors are gathering, see it in April.

## Structure (beats with timestamps)
- 0–2.9 s **studio logo**: Marvel Studios flip logo (black-and-white comic panels), then "MARVEL" disintegrates into dust (~1.5–2.9 s), leaving "STUDIOS" — the logo itself tells the story of the snap.
- 2.9–8.1 s **empty world**: foggy, empty New York harbour + Statue of Liberty (3.4 s), an empty stadium from above (1.75 s).
- 8.1–10.6 s **the question, inside the set**: a support-group poster "WHERE DO WE GO, NOW THAT THEY'RE GONE?" (2.5 s).
- 10.6–14.1 s Steve Rogers in the support group (3.5 s, the longest shot).
- 14.1–23.1 s **character montage**: Tony and Nebula on the ship, the team walking at night, Rocket, Black Widow shooting, War Machine + Ant-Man, Thor, Hawkeye, a gauntlet — 11 shots in 9 s (ASL 0.82 s).
- 23.1–24.1 s **black** (music still ringing out).
- 24.1–27.4 s **silent tableau**: silhouettes in the Avengers hangar at sunrise (3.3 s), sound down to −35 dBFS.
- 27.4–30.0 s **hit + end card**: Avengers "A" logo + "APRIL" in purple glow, #AvengersEndgame, "THIS FILM IS NOT YET RATED".

## Cut rhythm
- 18 shots (logo counted as one), **ASL 1.67 s**, median 1.13 s. ASL by quarter **2.50 · 1.88 · 0.75 · 1.88 s**.
- 44% under 1 s, 17% over 3 s. Longest 3.5 s (Steve), 3.4 s (empty city), 3.3 s (tableau); shortest 0.46–0.63 s in the montage.
- Cuts per 10 s: 3 · 9 · 5. Same shape as a 2.5-minute trailer, compressed 5×: slow open (8 s), fast middle (9 s), black + held ending (7 s).
- 27% of cuts on onsets vs. 19% chance.

## Typography
- Only two text moments, and the first one is **diegetic** (printed on a poster in the scene): condensed sans caps, 5 lines, left-aligned on the poster, the 5 lines fill ~47% of the frame height.
- End card: the Avengers "A" logo merged with "APRIL" in extended italic caps (chrome outline, purple-blue glow), centred; lockup ~26% of the frame height, the APRIL letters ~12%; hashtag and rating box small underneath. Holds 2.6 s.
- No tagline card, no title card: the film's name is never written except in the hashtag.

## Colour / grade
Desaturated, cold blue-grey for the "empty world" (fog, low contrast), dark green-teal interiors, one warm sunrise for the hope beat (hangar), purple for the end card (Thanos's colour). The file itself is scope (2.41:1), so on TV it would be letterboxed by the broadcaster.

## Camera / shots
Aerial wides of empty landmarks, static medium shots of characters looking down, quick character inserts, one silhouetted wide tableau shot against the light.

## Transitions
Hard cuts; logo dissolves to dust; one cut to black (23.1 s) and a fade-up (24.1 s); hard cut to the end card on the hit.

## Sound
- Integrated −13.5 LUFS (loudest of the Marvel set — TV spot).
- Hits: 1.0 s (logo, −9.5 LUFS M), 3.0 s (+16.7 dB on the first city shot), a steady build 13–23 s (−15 → −9.4 LUFS M).
- **Drop-out** 24.0–25.7 s: −10 → −35 LUFS for ~2 s over the silent tableau (one quiet sound at 25.75 s, maybe a line of dialogue — guess).
- **Biggest hit**: 27.3–27.4 s, +30.7 dB (−43.7 → −13 dBFS) on the cut to the end card, then a 2.5 s decay to silence.

## What makes it premium
- A complete trailer arc in 30 s: open slow, montage, black, silence, hit, date.
- The question is asked by the set (a poster), not by a title card.
- Even the studio logo is used for story (it turns to dust).
- It sells with no new action and no spoilers: faces, emptiness, a sunrise and a date.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. 0–3 s: logo, and break it apart (SVG letters → particle dust: 60 small `div`s per letter, `x/y` random ±200 px, `opacity 1→0` over 1.2 s `power2.in`, staggered 0.01 s).
2. 3–8 s: 2 empty wides (3.4 s + 1.8 s), cold grade `filter: saturate(.55) contrast(.9) brightness(.85) hue-rotate(-8deg)`.
3. 8–10.5 s: the question shown inside a real shot (a sign, a screen, a note) rather than as a card.
4. 10.5–23 s: one 3.5 s character beat, then 10–11 shots of 0.5–1.0 s rising in loudness.
5. 23 s: 1.0 s black while the music rings out; 24–27.3 s: one wide tableau with the music cut to −35 dBFS.
6. 27.3 s: +30 dB hit and hard cut to the end card (logo + month), glow `filter: drop-shadow(0 0 24px #7b5cff)`, hold 2.5 s, let the hit decay to silence. Master −13.5 LUFS for TV.
