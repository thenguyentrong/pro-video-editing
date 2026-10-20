# Dia Browser | Never Explain Yourself Again  (The Browser Company, 2025-06-11, 77.8 s, 16:9 with rounded film-gate corners, YouTube)
URL: https://www.youtube.com/watch?v=YVOw0TAO9ok
Purpose: launch film / ad (Dia beta opens to more users)
One-sentence point: With other AI chats you must explain your whole life in the prompt; Dia already knows it from your open tabs.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-12.6 (0-16 %) hook: a host prepares a family feast. Golden garden light, chopping, a pan of sauce, a handwritten menu notebook. Pure film, no product.
- 12.6-21.7 (16-28 %) problem: a busy kitchen; family members add demands (allergies, a theme, a menu). Quick reaction close-ups of actors.
- 21.7-37.6 (28-48 %) struggle: she types a longer and longer prompt into a generic AI chat. The screen is shot as a tilted macro with a teal tint, intercut with the family crowding behind her and waiting. The gag is the growing text box.
- 37.6-40.5 (48-52 %) turn: a 0.7 s audio drop-out and a slow close-up of her face; she has an idea.
- 40.5-56.4 (52-72 %) solution: the Dia icon is clicked in the Dock, she @-mentions her tabs (event mail, recipe), short prompt, the answer arrives. Two black text cards are cut into the UI shots: "If it's in your tabs" / "Dia already knows".
- 56.4-58.5 the cooked dish on the table.
- 58.5-64.0 (75-82 %) claim: black card with the positioning line (2.1 s), then a dusk dinner wide with the title built word by word (Never / Never explain / Never explain yourself again, about 0.8 s per step).
- 64.0-66.8 recap gag: the long prompt on black collapses into a short pill.
- 66.8-72.5 (86-93 %) payoff: candle-lit dinner, laughter, toast, the dish.
- 72.5-77.8 (93-100 %) end: Dia logo fades up over the dish (1.5 s), fade to black, logo on black, then URL card 2.4 s.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 50 shots (verified by eye on the cut sheet and 4 fps strips; 9 cuts added: two UI angle changes at 34.7/35.2, two UI cuts at 50.9/53.5, four dark dinner cuts at 66.8-70.2, one end-card change at 75.4). Text-card swaps count as shots.
- ASL 1.56 s, median 1.25 s, 34 % under 1 s, 6 % over 3 s. Quarters 1.50 / 0.97 / 1.77 / 2.16 s.
- Densest in the struggle section (19-37 s): 0.4-1.3 s shots alternating screen / faces. Shortest 0.42 s (30.1 s). Longest: the dish + logo shot 5.2 s (70.2 s), the menu notebook 4.5 s (8.1 s), the dinner title wide 3.4 s (60.6 s).
- The edit slows down once Dia solves the problem: the comedy is fast, the solution is calm.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Statement cards: a neutral grotesque (closest free: Inter 400), sentence case, white on pure black, centred, 1 line. Cap height ≈6 % H, line box ≈8 % H. 3-6 words per card. Hold 1.5-2.1 s. Hard cut in and out.
- Title over picture: same face, smaller (cap ≈3 % H), centred at ≈55 % H on a dusk wide; built word by word in 3 steps of ≈0.8 s.
- Logo: rounded half-disc symbol + serif "Dia" wordmark, white, ≈16 % H tall, centred; fades up over the last food shot, then sits on black.
- URL card: same grotesque, ≈3 % H, centred, 2.4 s.
- UI text is the product's own; no added captions, no subtitles for dialogue.

Colour/grade: palette, contrast, grain, letterbox
- Warm film look: golden daylight, teal-green walls (#49503a / #6a6d4f), red-brown apron and wood (#3a1915), creamy highlights (#afb781). Visible grain and a slight halation.
- Screen shots are tinted to match: mint UI (#b1d3c0) for the generic chat, warm beige (#bab294) for Dia.
- Night payoff is dark and warm (#1a0f0a, candle highlights).
- A rounded-corner black vignette frames every shot, like an old film gate.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Cast actors in a real house: wides, medium two-shots, reaction close-ups, food macros; mostly locked or slow handheld.
- The product is filmed on a real laptop screen with a camera: tilted, shallow focus, the cursor and typing visible. Not a clean screen capture.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- Hard cuts everywhere except a fade from the dish to black under the logo (72.5-75.0) and the soft UI collapse at 66.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Actors' dialogue drives the first half: speech detected only from 0.4 to 40.1 s (26 s of speech, ≈3.3 words/s, measured with a speech detector, not transcribed). From the Dia click at 40.5 s to the end there is no voice at all: music, UI and cards only. No narrator.
- Drop-outs at 11.4 s (0.35 s) and 37.6 s (0.7 s, the turn). Biggest rise +30.6 dB at 12.0 s (the kitchen starts).
- Integrated −17.8 LUFS, true peak −2.6 dBTP. 0.55 s silence at the very end.

What makes it premium (3-5 bullets)
- It is a short comedy film first: cast, location, grade and food styling look like a TV spot, not a product demo.
- The pain is shown as a gag (a text box that keeps growing) before the product appears at 52 %.
- The UI is filmed, not screen-captured: tilted, tinted, shallow focus, so it belongs to the film's world.
- The claim is said in plain black cards between UI shots, three to six words each.
- Fast in the problem, calm in the answer.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1920x1080, ≈75 s. 0-16 % warm establishing montage (5 shots, 2-3 s); 16-48 % problem in 0.5-1.3 s cuts alternating face / screen; 48-52 % a 2.5-3 s close-up with a 0.5-0.7 s music drop; 52-72 % product solving it, shots 1.5-3 s; 75-82 % claim; 86-93 % payoff; last 7 % logo and URL.
- Screen shots: render the UI in HTML and film-ify it: `transform: perspective(1200px) rotateX(8deg) rotateZ(-6deg) scale(1.6)`, `filter: blur(0.6px) sepia(.15) hue-rotate(110deg)` for the "other app", warm sepia for the hero app; slow push `scale 1.6 → 1.7` over the shot.
- Statement card: `#000` background, `400 72px Inter` white, centred; `tl.set` in and out (no tween), hold 1.6-2 s.
- Word-by-word title: three spans revealed with `tl.set(..., {autoAlpha:1})` at +0, +0.8, +1.6 s, `400 34px Inter`, centre y ≈55 %.
- Film gate: an overlay with `border-radius: 28px; box-shadow: 0 0 0 40px #000, inset 0 0 60px rgba(0,0,0,.6)` and a 4 % grain layer.
- Logo: `opacity 0 → 1` over 0.6 s on the last food shot, then fade the picture to black in 1 s, logo stays; URL card 2.4 s.
- Stock queries: "family cooking dinner kitchen golden hour", "outdoor dinner party dusk string lights", "laptop typing close up shallow focus kitchen", "candle lit dinner toast laughing".
