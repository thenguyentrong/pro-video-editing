# how we make our new red chimichurri  (Chipotle, 2025-10-02, 58.3 s, 9:16, YouTube Shorts / TikTok)
URL: https://www.youtube.com/shorts/0fka6TdGRuY
Purpose: social reel (employee-creator explainer for a menu launch)
One-sentence point: Chipotle chef Maria shows the ingredients of the new red chimichurri, the sauce itself and her favourite bowl with it.

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-1.8 hook: chef in black whites in the test kitchen holds the red sauce toward camera: "my name is Maria"; 1.83 s cut to a glossy macro of the sauce dripping off a ladle ("I'm a chef here at Chipotle", "and today I'm super excited").
- 4.8-16.6: talking head (MCU / wide jump cuts): "to introduce you to our new sauce, red chimichurri... inspired by Argentinian chimichurri... a bold flavorful twist".
- 16.6-30.3: handheld B-roll down the ingredient board: lemon-lime juice, fresh cilantro, red wine vinegar, "our special ingredient", a blend of spices.
- 30.3-42.6: back to camera, then the money shot: ladle of sauce poured back into the bowl (34.5-42.6 s, 8 s): "you can see the pepper flakes... the cilantro".
- 42.6-55.3 payoff: "this new sauce goes really well with a lot of our food" -> "my favourite way to try this sauce": she spoons it over a bowl (white rice, black beans, carne asada, fajita veggies, cheese, guac), each ingredient named.
- 55.3-58.3 CTA: "it is so good! can't wait to see what you pair it with!" (comment prompt). No end card.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 16 shots (12 from cuts2 + 3 jump cuts/punch-ins found on a low-threshold pass), ASL 3.64 s, median 3.02 s, quarters 2.91 / 3.64 / 2.91 / 2.91. Longest: ingredient B-roll take 10.5 s (19.8 s), sauce pour 8.1 s (34.5 s).
- Slow and steady: the caption chunks (every ~0.8 s) keep the screen changing between cuts.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- TikTok auto-caption look: white sentence/lower case sans (TikTok Sans / Proxima Nova medium-like), soft shadow, no box; glyph line 2.0-2.3 % H (cap ~1.7 % H); one line of 2-5 words at 56.7-58.9 % H, x 23-77 % W; phrase chunks synced to speech, hard switch.

Colour/grade: palette, contrast, grain, letterbox
- Bright stainless-steel test kitchen, black uniform, the red sauce is the only saturated colour; natural phone grade.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- Phone camera: locked MCU / wide talking head, handheld top-down B-roll, macro pours. Real employee, no presenter polish.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 15 hard cuts including 3 jump cuts / punch-ins.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Chef's voice in the room, light bed; integrated -18.9 LUFS.

What makes it premium (3-5 bullets)
- An employee as the creator: credible, warm, "behind the counter".
- The hook combines a face and the product within 2 s.
- The 8 s pour is food porn that justifies the slow pace.
- Ends with a question to the audience (comments).

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, ~60 s: talking head 40 %, B-roll 35 %, product macro 25 %; ASL 3-4 s with 2-3 jump cuts per minute.
- Captions: `font: 500 38px "TikTok Sans", "Proxima Nova"; color:#fff; text-shadow:0 1px 4px rgba(0,0,0,.6)`, centre y 1235 px (57 % H), 2-5 words per chunk from a word-level transcript, `tl.set` per chunk.
- End on a spoken question, no end card.
