# Privacy on iPhone: Safari helps block data trackers  (Apple, 2026-06-04, 1:05 file / 1:00 content, 4:3, YouTube)
URL: https://www.youtube.com/watch?v=Spb-ka7xrR8
Purpose: narrative privacy ad (comedy, music-led)
One-sentence point: Data trackers are literally people in silver suits riding on your back; Safari on iPhone makes them vanish.

## Structure
- 0-9.4 s **Set-up (dialogue)**: library; a man reads on his phone while a person in a silver suit sits on his shoulders. Woman across the table: "Excuse me… who's that?" — "Online data tracker." — "Follows me everywhere I browse." Wide symmetrical library shot (4-6 s). Then 1 s of silence.
- 9.4-37.9 s **Montage (music in)**: Swedish folk song "Hårga-Låten" (Zero8) starts; trackers cling to people everywhere — dog walker, museum, restaurant, campers in a tent, treadmill, hair salon, waiting room with a human tower of trackers. One gag per location, 1-3 shots each.
- 37.9-43.6 s **Turn**: line "Oh, chrome." over a 0.8 s music drop, music slams back (39.5 s); the heroine walks out of the library, trackers chase her.
- 43.6-52 s **Payoff**: super "Keep data trackers off your back."; trackers hide in trees; she uses her orange iPhone → trackers burst into silver glitter ("poofing", spooky laughter).
- 52-57.1 s **Lines**: "Safari. A browser that's actually private." over glitter; then "Privacy. That's iPhone." built word by word over her holding the phone up.
- 57.1-60 s **End**: padlock morphs into the Apple logo over the courtyard, lock click, glitter.

## Cut rhythm
- 40 shots in 60.06 s → **ASL 1.50 s**, median 1.42 s; quarters 1.50 / 1.67 / 1.16 / 1.36.
- 30 % < 1 s, 0 % > 3 s — very even. Densest 40-50 s (11 cuts / 10 s, the chase and "poof").
- Cuts on onsets 18 % vs chance 22 % → cut to action/gags, not to the beat.

## Typography
- SF Pro Display medium, white, centred at y ≈ 49 %, cap ≈ 5 % H, one line, sentence case with full stop. No shadow, no box.
- Word-by-word build: "Privacy." → "Privacy. That's" → "Privacy. That's iPhone." — each word appears in its final position (the line does not re-centre), ~0.7 s per step.
- 3 text moments only, all in the last 16 s.

## Colour / grade
- Rich, warm, slightly desaturated "storybook" grade: teal-green tiles and leather, warm wood, brick red; silver suits pop as the brightest element.
- 4:3 frame, symmetrical centred compositions (library, museum, waiting room) — Wes-Anderson-like staging.
- Hero product colour (orange) appears only in the payoff.

## Camera / shots
Locked-off symmetric wides + medium two-shots, phone-screen inserts, a few tracking shots in the chase, practical silver-suit performers, VFX glitter explosion, logo morph.

## Transitions
Hard cuts; VFX "poof" (people → glitter) as the transformation; padlock → Apple logo morph.

## Sound
- Opens with dry dialogue, **1.0 s silence (8.45 s)**, then the folk song as the main track; SFX: spooky laughter, poofing (×5), lock clicking.
- Integrated **−16.2 LUFS**. 0.8 s drop at 38.25 s for the spoken joke, then the loudest hit 39.5 s (−9.3 dBFS, +32.4 dB). Lock click hit 57.95 s.

## What makes it premium
- A literal visual metaphor that needs no explanation (trackers = people on your back).
- Odd, memorable music choice and very composed, symmetric frames.
- Product and text arrive only in the last 15 %; the brand line is short and rhythmic.

## Recipe (real footage + HTML/GSAP)
- Frame 4:3 (1440×1080), centred symmetric wides; cut every 1.2-1.8 s, one gag per location.
- Grade: `saturate(.85) contrast(1.05)` + warm overlay `#3a2a14` 10 % soft-light; keep silver costumes bright.
- Supers: Inter/SF Pro 500, `font-size: 7vh` (cap ≈ 5 % H), white, centred. Word build: render the full line with each word in a `<span style="opacity:0">`, then `gsap.to(spans,{opacity:1,duration:.15,stagger:.7})` so words appear in place.
- "Poof": 200 small silver particles from the subject's silhouette, `gsap.to(p,{x:"random(-300,300)",y:"random(-200,200)",opacity:0,duration:1.2,ease:"power2.out"})` + poof SFX.
- Sound: dialogue first, 1 s silence, then the song; drop the music 0.8 s for the spoken joke.
