# Opening credits
**Use it for:** a film or reel that borrows the grammar of a movie's opening titles: a city or place film, a team or event recap, a "cast and crew" brag, a calm pitch film where each credit carries one fact, and real series main titles. **Not for:** fast trailers with a climax (use movie-trailer), explainers that need voice and diagrams, or hook-first social clips where the first second must sell the video.
**Reference films:**
HBO — The Last of Us, opening credits (2023, 65.5 s) — hbo/the-last-of-us-titles
HBO — House of the Dragon S2, opening credits (2024, 99 s) — hbo/house-of-the-dragon-s2-titles
Apple TV+ — Severance S2, title sequence (2025, 78.5 s) — apple-tv-plus/severance-s2-titles
Apple TV+ — Pachinko, title sequence (2022, 82.1 s) — apple-tv-plus/pachinko-titles
Netflix — Narnia: The Magician's Nephew, trailer with in-scene credits (2026, 150 s) — netflix/narnia-magicians-nephew-official-trailer
A24 — Marty Supreme, trailer with a credit stack over the button (2025, 146.6 s) — a24/marty-supreme-official-trailer
Marvel Studios — "Steve Rogers will return" teaser (2025, 79.4 s) — marvel/avengers-doomsday-steve-rogers-teaser

## Signature
Real, carefully composed shots, each held about 3 seconds, with small two-line credits (a role above a name) placed in the empty part of the frame, inside a wide letterbox, carried by one song. Nothing moves except the world in the shot and a slow fade on the text. The rhythm comes from the music and from the steady cadence of the credits, not from effects. A strong model is a city film cut like the opening credits of a superhero film: ordinary streets and buildings, framed like cinema, with credits that name local places and things as if they were the cast and crew. Real series titles add one more rule: the whole piece is one idea or one material, and the title arrives at the end as its payoff.

## Numbers
"≈" marks values judged by eye from frames (the city-film grammar). The others are measured in the library examples. Cut times come from metrics.json; some contact-sheet labels run ≈0.96 s early.

| Measure | Composed-shot credits film | Panel or one-take title (HBO, Severance) | Montage title (Pachinko) |
|---|---|---|---|
| ASL | ≈3 s (≈36 shots in 110 s) | 4.1 s (panel chain); 11.2–32.8 s (one-take CG) | 0.85 s |
| Median shot | ≈3 s | 4.2–6.0 s | 0.71 s |
| Shots under 1 s | ≈0 % | 0 % | 69 % |
| Shots per minute | ≈20 | 2–15 | 70 |
| Cut density curve | even from start to end, set by the song | metronome: 15 of 24 panels 4.1–4.6 s; slightly denser in the second quarter (2.1–3 s shots), 8–9 s shots before the title; or hard cuts only in the first 20 s, then oners | accelerates every quarter: ASL 1.08 → 0.85 → 0.79 → 0.68 s |
| Text size (% frame height) | role ≈2 %, name ≈3.5 % | names 2.5–3.3 %; labels ≈1.5 % or 50–60 % of the name | names ≈1.8 %, labels ≈1.2 % |
| Words per card | 2–6 (role + name, optional small aside) | 2–6 | 2–5 |
| Card hold | in ≈0.5 s, hold ≈2 s, out ≈0.4 s | in 0.5–1.7 s, hold 1.2–3 s, out 0.5–0.7 s; a new credit every 3.1–4.5 s | in 0.25 s, hold 1.3–1.6 s, out 0.25 s or cut with the shot |
| Title | first and last card (title again at the end) | last 5–8 s; 4 % H (quiet) to ≈75 % H (stacked); hold 3–5 s, fade to black | type matte, cap ≈13 % H, 4.7 s |
| LUFS (integrated) | not measured; one song at a steady level | −15.4 to −22.4 (LRA 3.2–16.6 LU) | −16.1 (LRA 5.1) |
| Drop-outs / silences | none; the song runs through | 0.6–6.5 s quiet or silent start; no drop-outs inside; decay at the end | 1.6 s of black before the song; fade under the title |
| Aspect | ≈2:1 letterbox inside 16:9 (or 9:16 platform) | 2:1 or 2.39:1 letterbox, or 16:9 | ≈2.2:1 letterbox |

## Structure
1. **0–3 %: black or the first image, music silent or quiet** (1.0–1.6 s in the measured titles; the music can wait until ≈10 % of the runtime).
2. **3–10 %: hook shot + first credit.** The title card or the studio-style line ("a ... production"), or the two lead names split into opposite corners.
3. **≈10–45 %: lead "cast".** One credit per shot. Order like a real film: title, production, lead cast.
4. **≈40–80 %: supporting cast and key crew** (music, editing, design). The middle may be a little denser (2–3 s shots) or darker.
5. **≈80–90 %: the turn and the authors** ("created by", "written by", "directed by"). In a title sequence the image turns to the core of the story here.
6. **Last 5–8 s: the title again,** as the payoff of the whole piece, held 3–5 s, then a fade to black while the song ends.

## Picture
- **Subjects:** real places and real people. People are small and natural in the frame, never posed. Buildings, streets, statues, water, trees and sky carry the film. In a series title: one material (moss, thread, paper) shot in macro.
- **Composition:** every shot is designed: strong lines, one clear subject, and a large calm area (sky, wall, water, dark floor) where the credit will sit. Symmetric one-point-perspective wides work well.
- **Camera:** mostly locked-off, or very slow gimbal or slider moves (2–3 cm per shot in macro). In code: a slow push `scale 1.00→1.04` over the whole shot. No whips, no fast zooms.
- **Shot sizes:** mostly wides and medium-wides; a few details (hands, a sign, a texture) every 5–6 shots.
- **Grade:** one consistent warm film look: soft contrast, slightly lifted blacks, natural skin, gentle saturation. Series titles: near-black base plus 3–4 colours, heavy vignette.
- **Texture:** fine grain (opacity 0.06–0.08); optional macro shallow depth of field.
- **Aspect:** ≈2:1 letterbox (bars 5–5.5 % of the height each) or 2.39:1 (≈12.9 %). The bars say "cinema" before anything else happens.

## Type
- **Credit block (the signature):** two tiers, centred on each other.
  - Role line: ≈2 % H, caps, tracking ≈0.3 em, ≈80 % white.
  - Name line: ≈3.5 % H, caps, tracking ≈0.18 em, white.
  - Optional third line: a short aside in the smallest size.
  - Weight: regular or light, never bold. Free font: Montserrat Light or Regular with wide tracking.
- **Alternative faces by mood** (all look-alike guesses from frames): grim and modern → Oswald 600 names with Montserrat 500 labels; historic → Cinzel 400, tracking 0.25–0.3 em, parchment colour #d8c29a; corporate or surreal → Inter 400, sentence case, grey #a9a9a9, a 1 px hairline above that runs ≈15 % past the name; joyful pop → Montserrat 500 caps, tracking 0.35 em.
- **Placement:** composed into the negative space of each shot, in a different spot almost every time (upper-left sky, lower-right wall, beside a statue). Never over the subject or a face. Useful anchors on 1080p: bottom-left (x 8 %, y 78 %), top-right (x 78 %, y 22 %), bottom-right, bottom-centre.
- **Background:** no box and no drop shadow. A 10–20 % dark local vignette is fine on a bright sky. Option for collage work: a torn black box (≈22 % × 20 % of the frame) over the edge of a photo.
- **In-world credits (advanced):** set 1 in 4 credits in perspective and tint it with the scene's light (`perspective(900px) rotateY(-14deg)`), or reveal a name behind a foreground edge during a dolly. Use sparingly.
- **Animation:** opacity only. Standard: in 0.5 s `power1.out`, hold ≈2 s, out 0.4–0.5 s. Slow and dreamy: in 1.6–1.7 s `sine.inOut`, hold 1.2 s, out 0.7 s `sine.in`. Fast montage: 0.25 s / 1.3–1.6 s / 0.25 s. No slide-ins, no typewriter, no per-letter animation.
- **Title:** the same family as the credits. Quiet version: only ≈1.6× the credit size (≈4 % H). Loud version: a stacked wordmark up to ≈75 % H, revealed by the material (growing, ink, light), not by a type effect.

## Transitions
- Hard cuts only for the composed-shot film and the panel chain. No flashes, zooms, whooshes or glitches.
- Fade to black once, at the very end.
- For a one-take look: hide 1.5 s cross-dissolves in dark areas, or use camera-move transitions (push through an object: outgoing `scale 1→5` in 0.7 s `power3.in`, incoming `scale 0.35→1`, `opacity 0→1` in 0.9 s `power3.out`, same transform-origin).
- Credits change on their own cadence (every 3–4.5 s), not always on the cut.

## Sound
- **Music:** one song or one theme carries the whole piece. Choose it first and cut to its phrases (a new shot every 1–2 bars), not to every beat. Multi-cut titles put only 13–17 % of cuts on onsets, near chance.
- **Voice-over:** none. The credits are the narration.
- **SFX:** none, or at most a soft room tone. No hits on the cuts.
- **Level:** mostly flat (LRA 3.2–7.5 LU in three of four titles; a quiet piano theme can swing 16.6 LU). The loudest moment is on the title, then a decay.
- **Start and end:** 1–1.6 s of silence or near-silence at the start; the song fades under the final title; any end card after it is silent.
- **Mix:** −16 LUFS integrated for online (titles measured −15.4 to −22.4); true peak −1 dBTP.

## Do / Don't
**Do**
- Choose the song first, then the shots, then the credits.
- Frame every shot with a clear empty area for the text before you shoot or pick stock.
- Hold shots ≈3 s (2.5–4.5 s) and keep a steady cadence of one credit per shot.
- Follow a real credit order and repeat the title at the end.
- Put the humour or the message in the words: specific, local, self-aware and kind credits (a building credited as the lead actor, the weather in the special thanks).
- For a pitch: one credit = one fact of the story (the problem, the proof, the fix), in the same calm style.

**Don't**
- Don't use bold, big or boxed text, lower-third bars or animated captions.
- Don't place text on faces or on the busiest part of the frame.
- Don't add flashes, speed ramps, zoom transitions or whooshes.
- Don't mix several grades or several songs.
- Don't add a voice-over that explains what the credits already say.
- Don't drop the letterbox halfway through.

## Recipe
Target: a 60–110 s composed-shot credits film, 1920×1080 (or 1080×1920), 24 fps, real or licensed stock footage plus HTML/GSAP compositions (Hyperframes).
1. **Song and length.** Pick one licensed song. Mark its phrases. Plan ≈20 shots per minute (≈3 s each); 60 s ≈ 20 shots, 110 s ≈ 36 shots.
2. **Credit list.** Write the credits in film order: title → "a ... production" → lead cast → supporting cast → music / editing / design → written and directed by → title again. 2–6 words each.
3. **Shot list.** For each credit pick a shot with a matching calm area. Prefer locked-off wides; add one detail shot every 5–6 shots.
4. **Frame.** Black bars on top of everything: 60 px each for 2.00:1, 138 px for 2.39:1 on 1080p. Grade every clip soft and warm; a starting point (≈, tune by eye) is `filter: contrast(.95) saturate(.9) sepia(.08)`, plus grain at opacity 0.06–0.08. Optional slow push per clip: `gsap.fromTo(clip,{scale:1},{scale:1.04,duration:shotLen,ease:"none"})`.
5. **Credit component.**
   ```css
   .credit{position:absolute;text-align:center;color:#fff;font-family:"Montserrat",sans-serif;font-weight:300}
   .credit .role{font-size:22px;letter-spacing:.3em;opacity:.8;text-transform:uppercase}   /* ≈2 % H */
   .credit .name{font-size:38px;letter-spacing:.18em;margin-top:10px;text-transform:uppercase} /* ≈3.5 % H */
   ```
   Place each credit with `left`/`top` in % of the frame inside the shot's empty area.
6. **Credit timing.** For a shot starting at `t`: `tl.fromTo(credit,{opacity:0},{opacity:1,duration:.5,ease:"power1.out"},t+0.1)` and `tl.to(credit,{opacity:0,duration:.4},t+2.6)`. In 0.5 s, hold ≈2 s, out 0.4 s: the text fits inside a 3 s shot and is gone before the next cut.
7. **Title.** Same font, name tier only, centred or in the main empty area, held 3–5 s; fade the whole frame to black over 1–2.5 s with the song.
8. **Sound.** Song only; fade in over the first 1–2 s, fade out under the final title. Master `loudnorm=I=-16:TP=-1:LRA=11`.
9. **QC.** Watch on a phone: every credit readable, never touching a face, never over a busy area; no two shots of the same size in a row.
10. **Stock queries:** "city street wide static morning", "symmetric building facade", "empty plaza wide locked off", "rooftop skyline wide sky", "river bridge wide static", "tram passing wide", "pedestrians small in frame wide", "old town alley golden hour", "park bench wide calm", "moss macro shallow depth of field", "embroidery macro raking light" (licensed only; no AI people).

## Variants
- **Composed-shot city film** (the core): ≈3 s shots, two-tier credits in negative space, ≈2:1 bars, warm film grade, one song, credits that cast local places as actors and crew.
- **Continuous-metaphor title** (hbo/the-last-of-us-titles): one 56.5 s camera move over one material, a credit every ≈3.1 s (fade 0.5 / hold 2 / out 0.5), then one hard cut to black where the material grows the title.
- **Panel chronicle** (hbo/house-of-the-dragon-s2-titles): 24 hard-cut panels of one craft object, most 4.1–4.6 s; historic serif credits with staggered indents (0 / 40 / 16 px); theme compressed flat.
- **Surreal loop** (apple-tv-plus/severance-s2-titles): hard cuts every 3.5–6 s in the first 20 s, then oners with push-through transitions; tiny grey sentence-case credits with a hairline; the last shot matches the first.
- **Archive-to-joy montage** (apple-tv-plus/pachinko-titles): tinted archive panels on black for the first third, then present-day joy cut on movement; tiny wide-tracked credits with 0.25 s fades; title as a footage matte.
- **Credits inside a trailer** (netflix/narnia-magicians-nephew-official-trailer): names composited into wide shots (no plate), or revealed behind a foreground edge during a camera move.
- **Credit stack over a closing scene** (a24/marty-supreme-official-trailer): names build two at a time, about every 1 s, right-aligned near x ≈90 %, ≈6 % H, over dark footage for ≈6.6 s.
- **Single teaser line** (marvel/avengers-doomsday-steve-rogers-teaser): one small line on black, built in 3 word groups 2.5 s apart with 0.75–1.0 s fades, landing on sparse musical strikes.
- **Vertical (9:16):** keep a letterboxed band inside the vertical frame (a 2:1 band on 1080×1920 is 540 px tall, 28 % of the height) and size the credits as % of the band height, not of the full frame.

## Measured reference
The city-film grammar above was first judged by eye. It is now measured in aachen-city-film/brand-new-day (2026, 110.4 s; see also place-film.md). Where the measurement differs from the ≈ values, follow the measurement:
- **Grid:** 34 shots = 32 picture shots of 3.24–3.44 s + 1.92 s black open + 2.08 s black tail. ASL 3.25 s, median 3.32 s, 0 % under 1 s, 18.5 shots/min, exactly 3 cuts in every 10 s window. ≈3.33 s is one 4/4 bar at ≈72 BPM (inferred). Cuts on onsets 9 % vs 8 % chance: the cuts follow bars, not hits.
- **Aspect:** 2.39:1 (delivered as 854×358), not ≈2:1. On 1080p use bars of 138 px.
- **Credit size:** role 2.5 % and name 4.2 % of the picture band = ≈1.9 % and ≈3.1 % of a 16:9 frame; the title uses the name size; line gap ≈0.7 × name height; names 20–28 % of the frame width.
- **Credit timing:** no fades. Each credit is on from the first to the last frame of its shot and cuts with the picture (checked on 25 fps strips). One credit per shot, 32 in total.
- **Placement measured:** centre (title), right third x 70–94 % / y 54–64 %, bottom centre y 82–92 %, upper sky x 57–78 % / y 32–41 % of the picture band.
- **Sound:** −18.4 LUFS integrated, LRA 1.8 LU, true peak −5.1 dBTP. The song starts 0.5 s into the black open (1.4 s before the first picture); it drops out for 0.8 s under the last card (floor −71 dB), one final note 0.2 s before the hard cut to black.
