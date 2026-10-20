# Spider-Man: Brand New Day — New Trailer  (Marvel Studios / Sony, 17 Jun 2026, 2:35 (154.5 s), 16:9 with 2.39:1 letterbox, YouTube)
URL: https://www.youtube.com/watch?v=tLeBDumanoc (Marvel Entertainment upload; matched by duration, the original analysis did not store the URL)
Purpose: trailer (second / "new" trailer, ~6 weeks before release)
One-sentence point: Peter Parker is alone and unknown, but Spider-Man is back in a bigger, street-level New York full of old and new faces.

Reuse note: analysed on 19–20 Oct 2026 in an earlier analysis run (cuts checked by eye there). The media was already deleted and not downloaded again, so the key frames are 320 px tiles cut from the contact sheet (with the yellow time label burned in). Sheet tiles show the frame ~0.96 s *after* their label (fps=1:round=down); times in these notes come from the cut list, not from tile labels.

## Structure (beats with timestamps)
- 0–17.5 s **cold open**: night street fight, Spider-Man vs. a gunman, very short shots; two eye extreme close-ups (7.1–9.1 s, 16.2–17.5 s); a 0.8 s black hold at 14.3 s.
- 17.5–21.1 s **studio logos**: SONY on black (17.5) → Columbia (18.5) → red Marvel Studios flip logo (19.4–21.1). The logos come *after* the cold open, not first.
- 21–51 s **Act 1 (the world)**: video call, Peter in bed, suit-up inserts, Bruce Banner in a lecture hall and on campus, a gala crashed by Spider-Man, city swinging.
- 51.3–52.9 s **date card 1**: "THIS JULY" on black (1.6 s).
- 53–87 s **Act 2 (escalate)**: chase, Ned / MJ party scenes, street confrontation; 0.8 s black at 87.8 s.
- 88–128 s **Act 3**: upside-down reflection in a puddle (88.6–91.5 s), Hulk, MJ, Punisher, a prison fight with red ninjas, Peter smiling at a grave (126.9–128.9 s) and an insert of the May Parker headstone (128.9–129.5 s).
- 128.6 s **silence** 0.35 s at −59 dBFS, running across the cut to the headstone insert → 129.5 s **biggest hit** (+31 dB) exactly on the cut to the building collapse (129.46) → 132.2 s title.
- 132.2–135.7 s **title** fades up from black, holds 3.5 s.
- 135.7–151.9 s **button**: a 16 s comedy scene (Spider-Man posing in front of riot police, then getting knocked over).
- 151.9–154.5 s **end cards**: "TICKETS ON SALE NOW" → blue lens-flare wipe → "JULY 31 / IN PREMIUM FORMATS / EXCLUSIVELY IN MOVIE THEATRES" + billing block.

## Cut rhythm
- 135 shots, **ASL 1.14 s**, median 1.04 s. ASL by quarter 1.07 · 1.10 · 1.02 · 1.33 s (flat, slightly slower at the end).
- 45% of shots under 1 s, only 1% over 3 s. Longest: title 3.46 s (132.2), button shots 2.67 s (137.7), 2.42 s (11.9). Shortest normal shots 0.42–0.54 s.
- Cuts per 10 s: 10 · 9 · 9 · 8 · 5 · 9 · 11 · 12 · 9 · 9 · 10 · 9 · 10 · 5 · 6 · 3. Densest 60–80 s (11–12 cuts per 10 s = ~45% of the runtime); the button and end cards slow down (3–6 per 10 s).
- Cuts are not locked to the beat: 29% of cuts sit on an audio onset vs. 32% by chance (the music is dense, 1.6 onsets/s).

## Typography
- Only 4 text moments in 155 s: THIS JULY, the title, TICKETS ON SALE NOW, the date card.
- "THIS JULY": extended heavy caps with a red/blue chromatic split, centred, ~6% H, 1.6 s on black.
- Title: small "MARVEL STUDIOS" (~3% H) above "SPIDER-MAN" (~22% H, red letters with a blue outline, comic-book logo) and "BRAND NEW DAY" (~4.4% H, gold, extended caps). Fades up from black over ~0.8 s; no animation after that.
- End cards: chrome red/blue extended caps (closest free match: Michroma or Orbitron Bold, guess); "JULY 31" ~10% H, the two lines under it ~4.4–5% H.

## Colour / grade
Warm practical-light nights (orange street lamps, fire) against teal shadows; day scenes are soft, slightly desaturated naturalism. Red suit is the only saturated colour in most frames. 2.39:1 bars all the way, including the end cards. Light grain (hard to judge at 480p).

## Camera / shots
Mostly real locations and sets with handheld or dolly; big VFX wides (water tower, building collapse 129–131 s); extreme close-ups of eyes as punctuation; a single surreal image (upside-down reflection 88.6–91.5 s) as the Act 3 door. Character close-ups are centred.

## Transitions
Hard cuts almost everywhere. Three black holds (0.8, 1.6, 0.8 s) mark the act breaks. One fade-up (title) and one lens-flare wipe (end card). No whips or morphs.

## Sound
- Integrated −16.7 LUFS (the quietest of the Marvel set); loudness nearly flat by quarter (median M −16.3 · −15.9 · −15.9 · −16.2).
- Short drop-outs (0.2–0.5 s) before big moments: 37.5 s, 48.1 s, 76.0 s (−18 → −38 LUFS, then +22 LU).
- The biggest one: 0.35 s at −59 dBFS at 128.6 s, hit at 129.5 s (+31 dB), title 2.7 s after the hit.
- In the button, three gaps of 0.5–0.85 s (143.9, 145.8, 147.5 s) at −52…−58 dBFS: dead air as comic timing before each punchline.

## What makes it premium
- The cold open earns the logos: 16 s of action before any branding.
- Very even 1.0–1.1 s cutting, then the title gets 3.5 s and the button 16 s: the contrast feels confident.
- Sound design does the structure: tiny drop-outs before each new reveal, one real silence before the climax hit.
- Only four text moments; the date is said twice (THIS JULY, JULY 31) and nothing else is written.
- A comedy button after the title sends the viewer out smiling.

## Recipe (real footage + HTML/GSAP in Hyperframes)
1. Cut 12–16 s of the strongest action first (shots 0.4–1.0 s), then a 1.1 s logo sting, then the story at ASL ~1.1 s.
2. Put a 1.5 s black card "THIS <MONTH>" at ~33% of the runtime: `font: 900 64px/1 "Michroma"; letter-spacing:.06em;` with a chromatic split via two copies offset `x:±3px` in `#e1262d` and `#2b6cff`, `mix-blend-mode:screen`; in 0.25 s `power2.out`, out by hard cut.
3. Before the climax: duck all audio to −60 dBFS for 0.35 s (`data-automation` volume 0 for 8 frames), then the hit (+30 dB), then 2–3 s of the biggest action, then title.
4. Title: fade from black `opacity 0→1` over 0.8 s `power1.out`, main word ~22% of frame height, subtitle ~4.5%, hold 3.5 s.
5. Button: one 10–16 s comic scene with 0.5–0.8 s gaps of dead air before each joke, then the date card (hold ≥ 1.5 s).
6. Letterbox 2.39:1 on top of everything (138 px bars at 1080p), mix at −16 LUFS.
