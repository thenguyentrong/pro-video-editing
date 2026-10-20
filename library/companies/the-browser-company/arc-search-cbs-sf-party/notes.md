# We aired this Arc Search commercial nationally on CBS ("SF Party")  (The Browser Company, 2024-07-02, 63.7 s, 16:9, YouTube upload of a national TV spot)
URL: https://www.youtube.com/watch?v=wc1VeqU1YoM
Purpose: ad (first national TV spot for the Arc Search mobile app)
One-sentence point: When friends need a plan for the evening, Arc Search browses for you and gives a finished answer page instead of a panic of tabs and opinions.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-3.7 (0-6 %) pre-card: "AS FIRST SEEN ON CBS" in tiny tracked caps on black.
- 3.7-13.7 (6-21 %) set-up: friends with laptops in a San Francisco park. A TV-movie super "SAN FRANCISCO / PRESENT DAY" with a "from your friends at" credit and three small logo bugs in the top corners. Dialogue sets up the plan for the evening.
- 13.7-28.0 (21-44 %) flashback, played as a horror parody: white/cyan light flashes, a dark teal party lit by neon tubes, everyone on their phones, a wide-eyed close-up, fast 0.4-1.3 s shots.
- 28.0-30.6 (44-48 %) turn: a 0.9 s audio drop-out, back to the sunny park, her face decides.
- 30.6-41.5 (48-65 %) demo: one long handheld macro (9.4 s) of the phone: tap the app, type, "browse for me" gradient, a finished results page scrolls.
- 41.5-48.6 (65-76 %) payoff: she smiles; the group rides bikes through the city at night.
- 48.6-51.7 (76-81 %) claim: a top-down formation of people in green spotlights, one centred line of bold text.
- 51.7-60.3 (81-95 %) product: "Arc Search" over a dusk skyline; the frame shrinks into a phone card and result pages slide past, with QR codes left and right (TV call to action).
- 60.3-63.7 (95-100 %) end: one line on dark grey, then the app icon with an App Store badge.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 29 shots (verified on the cut sheet and 4-12 fps strips). The white flash frames in the flashback are counted as transitions, not shots (7 flash cuts dropped); 10 cuts in the dark party and end section added by eye.
- ASL 2.20 s, median 1.54 s, 34 % under 1 s, 21 % over 3 s. Quarters 2.65 / 1.22 / 1.99 / 3.18 s.
- Densest in the flashback (22-28 s: 0.42-0.6 s shots). Longest: the phone demo 9.4 s (32.2 s), the product/QR sequence 8.6 s (51.7 s), the park opening 5.8 s.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Place/time super: heavy extended grotesque caps, white with a blue outline/drop (TV-movie parody). Closest free: Archivo Black or Archivo ExtraBold Expanded. Cap ≈4.8 % H, 2 lines centred at ≈70-77 % H; credit line in small caps + a serif company name below (≈1.5 % H). Hold ≈6 s, hard on/off.
- Corner bugs: three small white marks top-left, top-centre and top-right (≈4 % H), like a TV channel bug, only during the super.
- Tagline: rounded geometric sans bold, sentence case with a full stop, white, centred at ≈50 % H. Closest free: Plus Jakarta Sans 700 or Manrope 800. Cap ≈4.6 % H. One line, hold ≈2.7 s.
- Product name: same face, small (≈2 % H), centred over the skyline.
- End line on dark grey #11171b: same face, ≈2 % H, with the key word in italic; then the app icon (≈6 % H) and badge.
- Pre-card "AS FIRST SEEN ON CBS": tiny tracked caps (≈1.2 % H, tracking ≈0.4 em).

Colour/grade: palette, contrast, grain, letterbox
- Two worlds: sunny saturated park greens (#2a4127, #6a775e) for the present; dark teal/green neon (#102f2b, #246959, #2c816c) for the flashback and the claim shot. Dusk pink-brown (#684742) for the skyline.
- Flash transitions blow out to white/cyan (#b0e8f0-like). Mild grain, no letterbox.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Cast actors, real locations, handheld close-ups and medium shots; night party on a stage set with neon tubes; one top-down formation shot; a skyline at dusk.
- The product is a real phone filmed in a hand, shallow focus on the screen (not a screen capture), then clean UI cards in the end sequence.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Mostly hard cuts. Three white/cyan light-flash transitions in and out of the flashback (1.2 s flicker at 13.7, 0.15 s at 22.0, 0.15 s at 26.9).
- One scale-down push: the full-frame skyline shrinks into a phone result card (≈1 s, 53-54 s).

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Actors' dialogue only from 6.6 to 30.5 s (18 s of speech, ≈4.3 words/s, measured with a speech detector, not transcribed); from the phone demo on there is no voice, only music. Dramatic score and party sound in the flashback (+16 dB rises at 20.9, 22.6 and 24.6 s); upbeat music for the bike ride.
- One drop-out 0.9 s at 28.2 s (out of the flashback), followed by the biggest rise, +31.2 dB at 29.2 s.
- Integrated −15.0 LUFS, LRA 7.7 LU, true peak −0.0 dBTP. Cuts land on onsets more than chance (29 % vs 19 %).

What makes it premium (3-5 bullets)
- A genre parody (TV-movie super, horror flashback) makes a search app into a story with stakes.
- The demo is one calm 9-second shot after 15 seconds of chaos, so the product feels like relief.
- Two clear colour worlds: sunny green present, teal neon nightmare.
- TV craft: corner bugs, QR codes on the result cards, app icon end card.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920x1080, 60 s: 4 s pre-card, 10 s set-up, 14 s problem montage (0.4-1.3 s shots), 2.5 s turn with a 0.9 s silence, 9-11 s one-take product shot, 7 s payoff, 3 s claim, 8 s product cards, 3.5 s end.
- Flash transition: white layer `opacity 0 → 1` in 0.08 s, `filter: hue-rotate(160deg)` cyan tint, hold 0.04-1.0 s with 2-3 picture flickers inside, then cut.
- Super: `900 52px "Archivo Black"` caps, white, `text-shadow: 0 0 0 #2a3cff, 3px 3px 0 #2a3cff`, centred at y 760-830 px; hold 6 s, hard on/off.
- Tagline: `700 50px "Plus Jakarta Sans"`, white, centred y 540 px, hold 2.7 s.
- Shrink-to-card: video layer `scale 1 → 0.42`, `borderRadius 0 → 28px` over 1 s `power3.inOut`, then result cards slide in `x: 100% → 0` every 0.8 s, two QR codes fixed at x 12 % and 88 %.
- Stock queries: "friends picnic park laptops golden hour", "neon party crowd phones teal light", "group bike ride city night", "city skyline dusk timelapse".
