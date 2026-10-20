# Cinematic brand anthem
**Use it for:** a 30 s to 4 min brand film that sells a feeling, not a feature: athlete or team anthems, a founder or community film, a car or machine launch with mood, a heritage or anniversary film, a luxury product reveal. **Not for:** a product demo that must prove a capability (use `industrial-robotics.md`), a how-to, a talking-head explainer, or anything where the viewer must read many numbers.

**Reference films:**
Nike — So Win (2025, 1:00) — nike-films/so-win
Nike — Greatness, Rafael Nadal tribute (2024, 1:00) — nike-films/greatness-nadal
Nike Football — Rip The Script (2026, 6:00) — nike-films/rip-the-script
Nike — Kobe 10 Protro (2026, 0:28, 9:16) — nike/kobe10-protro
Porsche — The Promise (2025, 1:34) — porsche/the-promise
Porsche — 75 Years of Doing Everything Wrong (2026, 2:26) — porsche/75-years-doing-everything-wrong
Porsche — The new Cayenne Electric (2025, 2:07) — porsche/cayenne-electric
Rolex — Worn on the Wrist of History for 100 Years (2026, 3:56) — rolex/oyster-100-years
Rolex — New Watches 2026 (2026, 1:07) — rolex/new-watches-2026
adidas — You Got This (2024, 1:28) — adidas/you-got-this
adidas — Football Anthem Film (2024, 1:30) — adidas/football-anthem
adidas Originals — Superstar (2026, 1:33) — adidas/superstar
BMW — The First of a New Era, new iX3 (2025, 1:54) — bmw/ix3-new-era
BMW — The Soul of BMW (2024, 0:45) — bmw/soul-of-bmw
BMW — Vision M NEXT launch film (2019, 1:37) — bmw/vision-m-next
Mercedes-Benz — From 1886 to 2026, 140 years of innovation (2026, 1:50) — mercedes-benz/140-years
Mercedes-Benz — The all-new electric GLC, TV commercial (2026, 1:02) — mercedes-benz/glc-electric
Mercedes-Benz — The new Mercedes-Maybach S-Class (2026, 0:47) — mercedes-benz/maybach-s-class
Hermès — Astonishing orange (2023, 0:45) — hermes/astonishing-orange
Hermès — Barénia (2024, 1:00) — hermes/barenia
Hermès — The timeless allure of Hermès Cut (2024, 2:00) — hermes/timeless-allure-cut
Patek Philippe — Generations: the legacy (2015, 1:56) — patek-philippe/generations-legacy
Patek Philippe — Generations ad (2016, 1:00) — patek-philippe/generations-ad
Patek Philippe — The next chapter of Generations (2019, 0:37) — patek-philippe/next-chapter

## Signature (one paragraph)
One rhetorical device carries the whole film: a repeated line ("you can't X / so X", "it's only X"), an argument ("when they said X, we did Y"), a litany of words, a one-word question, or one object assembled from its parts. Anthems are fast (median shot 0.56-0.96 s), quiet luxury films slow down (median 1.16-2.0 s†), but every frame is calm: one subject, clean background, one grade for all sources, archive included. Cuts follow the voice, not the music beat (cuts on audio onsets are at or below chance level in every anthem measured; only dialogue commercials land above it). The film speeds up, then stops: a short silence or a black hold, a hit of real sound, the longest shot of the film, and an end card that is only the line and the logo. Text is almost absent until the end, and when it comes it is either huge and plain or tiny and quiet, never medium.

## Numbers
Measured values come from `metrics.json`; values marked ≈ are eyeballed from frames; values marked † were added in round 3 (adidas, BMW, Mercedes-Benz, Hermès, Patek Philippe).

| Metric | Athlete anthem (Nike, adidas) | Automotive (Porsche, BMW, Mercedes) | Luxury / heritage (Rolex, Hermès, Patek, Porsche 75) |
|---|---|---|---|
| ASL | 0.87-1.26 s | 0.80-2.25 s† (anthem 0.80-1.17, launch 1.46-2.25†) | 0.78-2.57 s† (Patek film part ≈2.19 s†) |
| Median shot | 0.68†-0.96 s | 0.68-1.64 s† (anthem 0.68-0.92, launch 1.12-1.64†) | 0.56-2.0 s† (Hermès 1.18-1.42†, Patek 1.16-2.0†) |
| % shots < 1 s | 50-74 %† | 0†-75 % (Maybach 0 %†, launch 27-45 %, anthem 54-75 %) | 7†-79 % (Patek 7-30 %†, Hermès 21-38 %†) |
| Shots per minute | 48-69 | 27†-75 | 23†-76 |
| Cut density curve | rises then stops: 6 → 8 → 9 → 10 → 15 cuts per 10 s, then 1 (Nadal); 4 → 9 → 12 (So Win); slow first world 5-6, then 13-17 after a format switch† (adidas) | anthem flat at 14-16 per 10 s; heritage 0-1 per 10 s for the first 15 s, peak 16, then 3 → 1; launch flat 4-10†; luxury launch flat 6 then dissolves† | tempo grid (0.60 s, 0.88 s, 0.45-0.5 s per shot); densest 17-23 per 10 s just before the end; quiet luxury even at 3-13 per 10 s, no acceleration† |
| Text size (% of frame height) | end card caps ≈19 % + ≈40 % (one justified block), or a serif line ≈4 %, or spaced serif caps on a letter grid ≈10 %†; often no text at all | caps labels ≈2.3 %; feature callouts ≈4.2 % (sub-line ≈3.3 %); wordmark ≈5 % H, ≈42 % W; serif brand line ≈3.3-3.8 %†; one question word ≈4-11 %† or bold caps ≈8 %†; product name ≈6.3 %† | landscape title ≈18 % (once); end card serif ≈3 % italic + ≈4.6 % caps; campaign line serif ≈3-3.3 %†; city caption italic ≈4.6 %†; small sans caps ≈2.5-5.2 %† |
| Words per card | 1-5 | 1†-6 (caps line), 1-2 lines (callout) | 1-4; up to 2 lines of ≈9 words for a campaign line† |
| Hold times | end cards 0.9-1.8 s†, hard on/off; 1.3-1.7 s of empty picture between cards; logo 1.4-2.2 s† | callouts ≈3-4 s across 2-4 cuts; wordmark 3-4 s; legal 3 s; supers 2-3 s on one long final shot (10-12 s)† | end card 2-19.2 s† (Patek long film 19.2 s†); product card 8-10 s† ; title shot 1.9-5.6 s |
| Loudness (integrated) | -24.4 to -10.4 LUFS (broadcast masters ≈-24, social ≈-10; adidas -13.7 to -13.8†) | -16.6† to -7.3† LUFS (-7.3 clips at +2.1 dBTP: do not copy) | -20.6† to -12.6† LUFS; quiet luxury masters -16 to -20.6†, LRA 7.0-13.9 LU† |
| Drop-outs | 0.35-0.95 s silences right before the payoff line or a new world; black holds 0.64-2.3 s; rises after them +30 to +45 dB† | 0.45†-1.75 s before a new section, then a +15 to +31 dB hit; black hold 1.1-3.6 s before the product reveal† | none in the score; quiet luxury may open near-silent (≈11.5 LU under the body†, or 1.3 s digital silence†) |
| Aspect | 16:9; pillarbox ≈1.0-1.44:1† for the "pressure" or tribute world; 2.39:1 letterbox only for "staged" scenes (Rip); 9:16 social | 16:9; launch letterbox 2.0-2.35:1† | 16:9; archive inside a rounded film gate ≈70 % wide; full-frame B&W† |

Longest shot: in anthems it is the opening (2.1-15.2 s; 12.3 s held opening in Superstar†) or the end (6.0-9.2 s†), not the middle. Exceptions: a product reveal may hold one part-assembly shot (6.7 s) mid-film, and a comedy epic holds gags up to 17.3 s. Luxury films end on a long product or logo moment (8-10 s†, Patek line card 19.2 s†).

## Structure
Beats with share of runtime (ranges across the reference films):
1. **Hook: one held image (0-7 %, up to 10-14 %† for heritage).** A single shot of 2-4 s (anthem) or up to 15 s (heritage), often the longest shot. A still figure, a silhouette, a macro, a calm sky. No logo, no title (exceptions: a small logo over the first shot†, or the full lock-up for 2.5 s on a short luxury spot†).
2. **Teach the device (7-20 %).** Two or three pairs that show the pattern: portrait then action, claim then counter-proof, part then whole. Shots 1-2 s. Two-world films stay in the first world until the **switch at 20-38 %†** (hard cut + 0.4 s drop-out).
3. **Build (20-70 %).** Repeat the device and compress it: lines go from ≈2 s to ≈1 s; shots from 1.2 s to 0.3-0.7 s. Variety of places and people, same grade. Luxury builds keep an even pace and add places or chapters instead of speed†.
4. **Turn (≈70-85 %; ≈57 %† in a restaged-heritage launch).** The strongest line or the product. Before it: a 0.35-1.75 s silence or a 0.6-3.6 s† black hold. Slow motion appears here if anywhere (a body in the air).
5. **Payoff (≈80-92 %).** Real sound hits (crowd, engine, room), the hero shot, the longest shot of the film (6-9 s) or a burst of 0.2-0.6 s shots into it.
6. **End card (last 3-17 %†).** Black, off-white, warm white† or a silver gradient†; the line, then the logo; legal text only when a performance number was claimed.

## Picture
- **One grade for everything.** Anthem: full mono, crushed blacks, one hard key light, fine grain; archive graded to match. Automotive anthem: warm golden hour, lifted blacks, soft contrast, light flares and grain. Launch: cool teal, crushed blacks, one red accent light (or a strict black/steel/red system with one UI colour†). Heritage: archive left honest in a gate, modern footage clean.
- **Two grades on purpose:** pressure world B&W pillarbox → play world colour full frame (adidas†); B&W people → colour product (Patek†); one grade per era when the past is restaged (BMW iX3†); one hue per chapter (Hermès colour story†).
- **Two worlds, intercut:** still portrait on black (subject looks into the lens, almost no movement) vs real action or archive. Stillness makes the action hit harder.
- **One stage for a catalogue:** every object on the same grey cyc or white sweep, same scale (Rolex, Mercedes 140†).
- **Detail over faces:** textures, hands, tools, shadows, crests, macro of materials. Low angles on the hero. One top-down drone. Craft films: hands, eyes and metal only, one wide in two minutes†.
- **Camera:** mostly locked off; movement comes from the subject. Automotive adds tracking car-to-car, wheel-level, dutch angles of 20-45 degrees on speed plates, FPV/drone tops. Fashion films: canted frames 20-35°, extreme top shots†.
- **Slow motion only for bodies or objects in the air**, and for the hero ball/product moment. Never on the whole film.
- **Real people, real archive.** Keep archive watermarks and grain if it is history; never fake archive. Restaging past eras as obvious cinema with costumes and period cars is fine (BMW iX3†).
- **Product films (Rolex/Kobe):** one object, centred, clean background, same scale every time; show engineering as parts that assemble or as the same object in many materials (clay, scan, heat map, X-ray). Luxury end: the product lands on an object (concrete plinth, table) in hard light, not on a model†.
- **Format as meaning (optional):** letterbox on = staged/fiction, letterbox off = real (Rip The Script); pillarbox = pressure/memory, full frame = play (adidas†). Switch it with a hard cut.

## Type
| Use | Brand face | Closest free font | Weight / case | Size (% H) | Placement | Animation |
|---|---|---|---|---|---|---|
| Payoff end card (athlete) | Futura Condensed ExtraBold | Anton | ExtraBold, ALL CAPS, tracking ≈-1 %, line-height 0.88 | ≈19 % line 1, ≈40 % line 2, both set to ≈90 % width | centred block | hard on (`gsap.set`), no ease; line 2 added 1.3 s later |
| Letter-grid end card† | custom serif | Libre Caslon Text / EB Garamond | Regular caps, one letter per grid cell | cap ≈10 %, block ≈44 % W, line pitch ≈34 % | centred on black | hard on, hold 1.5-1.8 s, dissolve 0.3 s to logo |
| Quiet tribute line | custom book serif | EB Garamond / Libre Caslon Text | Regular, sentence case | ≈4 % (≈3.2vh) | centre, ≈47-49 % from top, over the image | hard on/off, 1.0-1.5 s hold, 1.3-1.7 s empty between cards |
| Brand line, automotive luxury† | corporate serif | Cormorant Garamond | sentence case, or caps with letter-spacing .12em | ≈3.3-3.8 % | centre (y ≈46-50 %) or in the sky (y ≈25 %) | fade 0.5-0.8 s, hold 2-3 s |
| Question word in space† | corporate sans light | Inter Light / Manrope Light | caps, letter-spacing ≈.5em | ≈4-11 %, new size each shot | empty area of each shot, perspective-matched | cut on/off with the shot |
| Automotive caps label | Porsche Next | Inter SemiBold | 600, ALL CAPS, letter-spacing .02em | ≈2.3 % | aligned to a product line (tail-light height), left and right of the car | fade in 0.5-0.8 s, hold 2.5-7 s |
| Rotated chapter label† | corporate sans light | Inter Light | caps, `writing-mode: vertical-rl` | ≈4.8 %, length ≈29 % H | left edge, x ≈2-4 % | on with the chapter, 5-15 s |
| Feature callout | Porsche Next | Inter SemiBold + Regular sub-line | 600, sentence case, number + unit written in full | ≈4.2 % + ≈3.3 % | empty area next to the feature, x 6-30 % | fade 0.3 s, hold ≈3.5 s across 2-4 cuts |
| Wordmark end | custom wide caps | Michroma / Syncopate | wide extended caps, letter-spacing .35em | ≈5 % H, ≈42 % W | dead centre on black | `filter: blur(18px) → 0` + fade, 0.9 s `power2.out`; hold 3-4 s; out 0.8 s |
| Landscape title | custom wide | Syncopate Bold | caps, letter-spacing .08em | ≈18 % | behind the horizon, bottom masked into haze | drift `x: -2vw` over 2 s |
| City caption† | book serif italic | EB Garamond Italic | italic, title case | ≈4.6 % | lower right, x ≈90 %, y ≈80 % | on for the whole vignette |
| Heritage end card | serif | EB Garamond / Cormorant Garamond | italic line + roman caps, letter-spacing .04em | ≈3 % + ≈4.6 % | centre on off-white radial gradient | fade 0.6 s, hold 4 s, cross-fade to logo 3 s |
| Campaign line card† | book serif | EB Garamond | Regular, sentence case, 2 lines | ≈3-3.3 % | centre of a silver gradient | line 1 fade 1 s, line 2 +2-4 s, hold 5 s, dissolve to logo |

Rules: no boxes, no lower-third bars, no icons. Max one typeface family plus the logo. Text either IS the line the voice says, or is absent. Quiet luxury puts text only in the last 10-15 %†.

## Transitions
- Hard cuts almost everywhere (So Win: 57 of 57).
- Black hold as the breath before the last act: 0.64 s (Nadal), 2.3 s (Rip), 3.56 s before the new car (BMW iX3†), 10.9 s of black for the closing cards (Porsche 75).
- One flash frame of 0.12 s (3 frames white or a cut) to jump from a dark tease into daylight; a 0.36 s black flash to jump from intimate to open (Barénia†).
- Archive "windows on black": small frames (≈11 % to 35 % of width) appear one per voice phrase, 1-3 at once; the last one grows to full frame.
- Sliding split-screen panels instead of cuts: one change every ≈1.35 s, a growing tile grid as finale (Mercedes 140†).
- Physical wipes: smoke, a round hole in a wall as a mask between colour worlds (Hermès†).
- Match cuts on shape (round movement → dial → crown; insole outline → real insole → thermal insole; sketch circle → case ring → eye → loupe†).
- Long dissolve (≈4 s) from a held opening into the main world (Superstar†).
- Fades only on end text and the logo.

## Sound
- **Voice first, picture second.** Record or choose the voice-over before cutting; one shot per phrase. Product reveals without voice use a tempo grid instead (beat = 60 / BPM; 0.60 s at 100 BPM). A slow narrator may say only 7 lines in 100 s (BMW iX3†).
- **Silence before the payoff:** cut the music to silence for 0.35-1.75 s, then hit with real ambient sound (crowd, engine). Measured rises after the silence: +21 to +45 dB†.
- **Logo sting:** a hit on the wordmark or swoosh (+15 to +29 dB rise), then silence (0.6-2.7 s† at the very end).
- **Heritage exception:** continuous score, no drop-outs; emphasis comes from archive voices entering.
- **Quiet luxury (Hermès, Patek, Maybach†):** no voice, continuous score, wide range (LRA 7.0-13.9 LU); open near-silent, open up +10 LU at the switch.
- **Level as story:** raise the mix ≈+6 LU when the future/product starts (BMW iX3 -19.9 → -14.1 LUFS†).
- **Loudness:** the quiet broadcast masters (≈-24 LUFS) are not a target for social; copy the dynamics (silence → hit), deliver social at ≈-14 to -10 LUFS. Never deliver above -9 LUFS or above -1 dBTP (one measured master clips at +2.1 dBTP†).

## Do / Don't
| Do | Don't |
|---|---|
| Build the film on one device and repeat it 6-12 times, faster each time | Mix three ideas or list features |
| Grade every source the same (or code two grades on purpose) | Leave stock and own footage in different looks |
| Cut on voice phrases | Cut every shot on the music beat |
| Make the last or first shot the longest | Hold the middle |
| Put silence (0.35-1.75 s) before the strongest line | Run music wall to wall under the payoff |
| End on the line + logo, hard on, nothing else | Add a website, CTA, price or date to the end card |
| Keep text tiny (≈2-4 %) or huge (≈19-45 %) | Use medium-size captions with boxes |
| Use real people and real archive | Use AI-generated "archive" or fake history |
| Let format carry the meaning (B&W pillarbox → colour full frame)† | Explain the switch with a title card |
| Slow down with price: luxury median 1.2-2.0 s, no shot under 1 s for the top tier† | Cut a luxury film at anthem speed |
| Put a 1-3.5 s black hold before the product reveal† | Reveal the product in the middle of a montage |
| Show the watch or product worn inside a human moment, then alone on a plinth or table† | Hand the product to camera or add feature supers in a luxury film |
| Cut the 10-s silent "Visit us" web slate when you study a film† | Copy platform end slates into your film |

## Recipe
1. **Write the device.** One line pattern, 6-12 repeats, then a turn and a payoff line. Record the voice (or pick the music for a voiceless reveal) and mark every phrase start. For luxury, write the visual principle instead (colour chapters, quiet → open, sketch → object → sketch)†.
2. **Shot list (35-60 shots for 60 s; 20-35 for quiet luxury†).** 1 hero opening image (2-4 s), 6-12 still portraits on black, 20-40 action/detail clips, 2-3 drone tops, 1-3 archive moments, 1 slow end shot (6-8 s).
3. **Source licensed footage only.** At least 1080p, prefer 4K, one frame rate for the whole film, no AI stock, no visible third-party logos, a licence log line per clip. Search with what is IN the picture:
   - athlete: `athlete portrait black background`, `boxer training dark gym`, `sprinter start blocks slow motion`, `chalk dust hands close up`, `empty stadium night`, `clay court aerial`, `street football kids black and white`†
   - automotive: `sports car mountain road drone`, `car tracking shot golden hour`, `headlights night road`, `raindrops car paint macro`, `tunnel driving night`, `car light sweep dark studio`†, `vintage car coastal road 1960s`†
   - luxury/heritage: `watch macro rotating`, `watchmaker hands loupe`, `water surface sun glints`, `white seamless studio product`, `leather texture macro`†, `horse galloping mountains`†, `father son black and white garden`†; archive from public-domain sources (NASA, Wikimedia Commons PD/CC0 files)
4. **Grade in CSS (one class for all clips).** Mono: `filter: grayscale(1) contrast(1.25) brightness(.92)` + grain PNG at 3 % opacity, `mix-blend-mode: overlay`. Soft luxury B&W†: `grayscale(1) brightness(1.08) contrast(.9)`. Warm: `sepia(.15) saturate(1.1) contrast(.95) brightness(1.03)` + an orange `radial-gradient` flare layer, `mix-blend-mode: screen`, opacity .25, on 3-4 shots. Teal launch: `saturate(.8) hue-rotate(-8deg) brightness(.8)`. Workshop low-key†: `sepia(.25) contrast(1.2) brightness(.8)`. Product montage: `grayscale(.85) contrast(.95) brightness(1.02)`.
5. **Cut to the curve.** Open 2-4 s, middle 0.8-1.2 s, last third 0.3-0.7 s, then one 6-8 s end shot or a 0.6-2.3 s black. For a grid: intro shots = 1 beat each, line-up shots = 1.5 beats. A 60 s template built from the measured anthems:
   - 0-4 s: hero image, one shot
   - 4-12 s: device taught, 5-6 shots of 1.0-2.0 s
   - 12-42 s: build, 30-36 shots, from ≈1.2 s down to ≈0.8 s (9-12 cuts per 10 s)
   - 42-50 s: turn line, one slow-motion shot of ≈2 s, short silences of 0.35 s
   - 50-51 s: 0.6-0.85 s silence or black
   - 51-56 s: payoff with real sound, 4-6 shots or one long hero
   - 56-60 s: end card (line 1.3 s, line 2 0.9 s) or line + logo, then ≈0.9 s black
   Quiet luxury 60 s†: 0-4 s calm wide; 4-48 s, 25-30 shots of 1.2-3 s at an even pace; 48-55 s product on a plinth or text card; 55-60 s logo on warm white or silver.
6. **Silence.** 0.35-0.85 s before the payoff: `gsap.to(music, {volume: 0, duration: 0.05}, tPayoff - 0.6)`, then the real-sound hit at `tPayoff`.
7. **End card.** Black `<div>`; `font-family: Anton; text-transform: uppercase; line-height: .88; letter-spacing: -0.01em`; line 1 `19vh`, line 2 `40vh`, both fit to 90 % width. `tl.set(l1, {autoAlpha: 1}, t).set(l2, {autoAlpha: 1}, t + 1.3)`, hold 0.9 s. Or the wordmark: `gsap.fromTo(logo, {filter: 'blur(18px)', autoAlpha: 0}, {filter: 'blur(0px)', autoAlpha: 1, duration: .9, ease: 'power2.out'})`, hold 4 s, sting SFX at +0.6 s. Or the silver line card†: `background: linear-gradient(#8c8c8c, #e9e9e9 45%, #e9e9e9 55%, #8c8c8c)`, EB Garamond 3.3vh, two lines 2-4 s apart, dissolve to the logo.
8. **QC.** Check that the first or last shot is the longest; that no shot in the build is longer than 1.2 s (luxury: no shot shorter than 0.5 s except one flash†); that the payoff has silence before it; that every clip has one grade; that the end card has nothing but the line and the logo; that the master is ≤ -1 dBTP.

## Variants
**Athlete anthem (Nike, 60 s).** Mono, portraits on black vs real action, voice call-and-response or a word litany (one word = one shot, 0.28-0.7 s). ASL 1.0-1.2 s, 50-62 % under 1 s. End card huge condensed caps or a tiny serif on the last image. Social 9:16 cut: either one locked shot with a typed paragraph (ASL ≈10 s, -24 LUFS, text = subtitle) or a 30-shot material montage (ASL 0.87 s, 72 % under 1 s, no text, logo in the material as end card).

**Platform anthem, two worlds (adidas, 90 s)†.** Pressure world in B&W pillarbox (1.0-1.37:1), slow (first-quarter ASL 1.7 s), faces into the lens; a hard switch at 20-38 % with a 0.4 s drop-out to colour full frame; then an "it's only X" litany, ASL 0.93 s, median 0.68 s, 67-74 % under 1 s, stars and amateurs mixed; a 10-s comedy beat in the longer cut; same letter-grid serif end card in every film of the platform. Originals form: a 12-s held opening, a symmetrical one-point corridor set, a celebrity narrator, a 5-colour palette.

**Automotive (Porsche).** Two forms. Anthem: 100+ real clips of real people at 0.5-0.9 s, warm grade, no supers, wordmark blur-in, legal line. Launch: no voice, dark tease 10-15 s → 0.12 s flash → daylight reveal; 6 feature callouts (one fact + unit each, held across cuts); median 1.44 s; studio ring-light shot as bookend; 1.75 s silence before the new section. Heritage argument: one 12-15 s designed opening shot, then archive windows on black and a 10-16 cuts-per-10 s build, then ≈11 s of black with two cards.

**Automotive, restaged eras and questions (BMW)†.** Launch: 4-5 eras rebuilt as cinema (each its own grade), 2.2:1 letterbox, a 7-line narrator, even pace (median 1.16 s), a 3.56 s black hold, the car revealed from darkness by a light sweep, old characters riding in the new car, mix +6 LU after the reveal. 45-s anthem: one question word in every shot (size 4-11 %), median 0.76 s, the answer as faces, one 9-s crane shot with two claim lines. Concept film: fashion-film portraits in red light, a bold caps question split around a figure, 1.1 s black + 0.45 s silence, then the score.

**Automotive by tier (Mercedes-Benz)†.** Commercial: celebrity dialogue, median 1.12 s, a 0.24-0.5 s burst to say who the hero is, one long final road shot under two serif supers. Heritage: every car on one grey cyc, rotated chapter words, sliding panels (≈1.35 s per change), a growing tile grid. Top luxury: CGI world, 2.0:1, no voice, no shot under 1 s, small serif caps, dissolves into two logos on black and 2.7 s silence.

**Luxury / heritage (Rolex).** Calm frames at high speed: one object centred on white or black, median 0.56 s (heritage) or 1.46 s (novelty reveal). Engineering shown as parts that float and assemble (`power3.out`, 1.2 s, stagger 0.25 s, 1-2 % landing bounce). Archive in a rounded gate (`border-radius: 4%`, ≈70 % wide, grayscale + light flicker), catalogue runs of one item per 0.45-0.5 s, a testimonial run of faces at 0.45 s each before the end. Continuous score, no silences. Off-white end card with a small serif, held 2-7.6 s.

**Quiet luxury (Hermès, Patek Philippe)†.** No voice, median 1.16-2.0 s, 7-38 % under 1 s, 23-45 shots per minute, no acceleration. One visual principle: colour chapters with canted fashion frames and physical wipes; quiet-to-open (near-silent macro of skin and leather, a black flash, then wide running shots); craft circle (sketch → metal → hands → sketch, 90 macro shots in 2 min); or B&W parent-child vignettes in several cities with italic city captions. Text only in the last 10-15 %, small; product on a plinth or table, or the only colour shot; end on a warm-white logo (2-4.4 s) or a silver line card (up to 19 s).

**Comedy epic (long form, 6 min).** Same fast median (0.96 s) but with long comedy holds (up to 17 s), format parodies (CCTV with mono time code ≈1.6vh, TV studio, B&W flashback in 4:3), letterbox = staged, flat full frame = real; 0.6-0.95 s silences before each gag; 2.3 s black before the final act.
