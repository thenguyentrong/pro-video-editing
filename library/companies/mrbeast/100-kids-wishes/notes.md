# I Granted 100 Kids Their Biggest Wish!  (MrBeast, 2026-07-25, 14:35 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=lVylRtlPOIE
Purpose: entertainment / philanthropy montage (many short wish segments, celebrity guests, a wish-granting charity partner)
One-sentence point: The channel and many famous guests grant 100 seriously ill children their biggest wish, one after another, with a counter to 100.

Data note: full upload 14.6 min; first 300 s trimmed with ffmpeg and measured. Scene detector + 13 cuts added by eye, most of them hidden behind white glow flashes (see `manual_corrections` in metrics.json). No paid sponsor read in the first 300 s; the charity partner is shown as part of the story. Children are not named in these notes.

## First 30 s (hook)
- 0.0–4.1 one wide, symmetrical shot: a big group of kids and the host in front of a fairy-tale castle, fireworks going off; the first sentence states the whole premise (100 kids, biggest wish).
- 4.1–6.0 a flash burst of 9 cuts: smiling faces at 0.10–0.43 s each, with RGB-split edges and white light flares between them. It shows "100" as faces, not as a number.
- 6.0–17.1 the emotional reason: one child's story (photo/video of him in pyjamas, then in a hospital bed), soft white glow dissolves, a short hug with the host; his wish is asked at ≈12–14 s and answered at ≈17 s.
- 17.1–30 the wish happens at once: indoor ski slope, first run, the parent's face-to-camera interview over it. The counter appears top-left as "0/100" at ≈22 s and ticks to "1/100" at ≈23 s; it stays on screen from then on.
- 30–47 re-hook: scale promise (famous creators, musicians, actors, athletes; one sports star named) over a host-on-stage shot in front of a curved video wall full of clips of the guests (33–47 s).
- Cuts in 0–30 s: 21. Loudness of the first 30 s: −9.6 LUFS. 0.3 s drop-out at 17.1 s right before the answer to the wish question.

## Retention devices seen in 0–300 s
- Counter "N/100" top-left on every shot; when it jumps it grows to a big version near the bottom of frame (≈9.5 % H) with the star logo, then shrinks back (e.g. 2 → 9 at ≈82 s; later 32, 33, 34, 40, 50).
- Bigger-than-asked twist on each wish: a child who only wanted to meet the host gets a button that sets off a large explosion (48–74 s) with a 0.7 s near-silence (62.5–63.2 s) and a second 0.4 s gap at 64.0 s (−65 dBFS) right before the blast, then the biggest rise of the window (+47 dB at 64.8 s).
- Promise early, pay off late: the star athlete is named at ≈39 s and appears at ≈205 s with a yellow name label.
- Location hopping: castle park, aquarium tunnel, a London theatre, a rocket site, a race circuit, Paris, a mall; each wish gets 5–20 s.
- A short "why it matters" beat with a doctor in a hospital corridor (≈126–135 s) between the fun.

Structure (first 300 s): premise + face burst 0–6 → first child story and wish 6–30 → scale promise 30–47 → explosion wish 48–74 → theme-park group wish 75–121 → why wishes matter 121–136 → world montage of wishes 137–200 → star athlete wish 200–235 → foundation house 235–262 → video call + mall 262–300.

Cut rhythm: 172 shots in 300 s, ASL 1.74 s, median 1.37 s. ASL by quarter 1.47 / 1.60 / 2.14 / 1.79 s. 23.8 % under 1 s, 13.4 % over 3 s. Longest 10.9 s (179.2 s, a single reaction shot), 7.0 s (75.1 s), 5.0 s. Shortest 0.10–0.13 s (the face burst at 5.6–5.97 s). Cuts per 10 s 2–10, typically 5–8; only 0 at 180–190 s (the long take). Cuts on onsets 50 % vs 46 % chance: slightly more on sound events than chance (flash hits), but mostly on speech.

Typography:
- Counter: small star logo (pink/teal ≈#D14B92) + "N/100" in white heavy sans with a dark shadow, cap ≈3.8 % H, top-left at x ≈6 %, y ≈4 %. Jump version: cap ≈9.5 % H, centred low (≈88 % H). Closest free: Montserrat ExtraBold.
- Name label for a famous guest: lemon yellow (≈#F5FF10) heavy comic italic caps with a dark outline and drop shadow, cap ≈7 % H, centred at ≈19 % H, hold ≈4 s. Closest free: Komika Axis (or Bangers).
- Shout caption: white italic comic caps with a black stroke, ≈3 % H, bottom centre (≈92 % H), only on a loud reaction word with stretched letters.
- Small "COURTESY OF …" credit on borrowed launch footage, bottom-left, ≈2 % H.

Colour/grade: bright and warm, high saturation; white glow and light-leak flares used as emotional punctuation; RGB-split / chromatic edges on the face burst; the host's black or white T-shirt as the constant. No letterbox.

Camera/shots: symmetrical wide group shots at landmarks, handheld mediums of reveals (blindfold off, door opens), parent interviews to a phone or webcam, drone and crane for set pieces (platform hanging from a crane), stage shot in front of an LED video wall, stock/courtesy launch footage.

Transitions: hard cuts plus many white glow flashes (≈10 in 300 s) that bridge locations; RGB-split flash frames in the face burst; light-leak dissolves on the emotional story.

Sound: integrated −8.9 LUFS, LRA 5.7 LU, true peak +1.0 dBTP on the stream. 50 ms RMS p10 −23.2 / p50 −13.6 / p90 −8.7 dBFS (≈10 dB from median to p10: a full bed). Six drop-outs 0.3–0.7 s, all directly before a reveal (17.1, 62.5, 64.0, 72.25, 142.25, 183.45 s), each followed by +35 to +47 dB. Loudest 0.5 s at 46.8 s (end of the scale promise).

What makes it premium:
- The count to 100 turns a montage into a race: the viewer watches the number climb.
- Every wish is topped by something bigger than the child asked for.
- Real places and real famous guests, shown in wide symmetrical frames that read in one second.
- Emotion is earned in 10 s (story, hospital, hug) before the fun starts, then revisited briefly with a doctor.

Recipe (real footage + HTML/GSAP):
- Open on a 4 s symmetrical wide of the whole group; then a 1.8 s burst of 8–9 faces at 0.1–0.4 s each with `filter: drop-shadow(3px 0 0 rgba(255,0,80,.7)) drop-shadow(-3px 0 0 rgba(0,200,255,.7))` and a white flash (`.flash{background:#fff}` `gsap.fromTo('.flash',{autoAlpha:.9},{autoAlpha:0,duration:.12})`) between faces.
- Counter: `font:800 3.8vh 'Montserrat'; color:#fff; text-shadow:0 2px 6px rgba(0,0,0,.6); left:6vw; top:4vh`; on increment: `tl.to('.counter',{scale:2.5,x:'40vw',y:'78vh',duration:.25,ease:'back.out(2)'}).add(()=>count++).to('.counter',{scale:1,x:0,y:0,duration:.3,ease:'power2.in'},'+=0.8')`.
- Guest name: `font:400 7vh 'Komika Axis','Bangers'; color:#F5FF10; -webkit-text-stroke:3px #111; text-shadow:0 4px 0 #111; top:15vh; text-align:center; font-style:italic`; pop in `scale:0 → 1`, 0.25 s `back.out(3)`, hold 4 s.
- Pace: ASL ≈1.7 s, a wish every 15–40 s, white flash between locations, one long reaction take (7–11 s) per minute.
- Reveal sound: 0.3–0.7 s silence before each reveal, then the hit; deliver at −14 LUFS / −1 dBTP.
