# A24 — trailer style

Four official A24 trailers measured at 480p (cuts2 + eye check of every cut, EBU loudness, 50 ms RMS, faster-whisper for speech, text measured in % of frame height H). Examples:

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Aspect |
|---|---|---|---|---|---|---|---|
| [Civil War, official trailer (2023)](civil-war-official-trailer/notes.md) | 143.4 s | 106 | 1.35 / 1.04 | 1.43 · 1.12 · 1.28 · 1.49 | 44 % / 8 % | −17.0 | 1.85:1 |
| [Midsommar, official trailer (2019)](midsommar-official-trailer/notes.md) | 150.6 s (+7.7 s black) | 100 | 1.51 / 1.13 | 3.14 · 1.98 · 1.30 · 0.88 | 36 % / 11 % | −17.4 | 2.00:1 |
| [The Zone of Interest, official trailer (2023)](zone-of-interest-official-trailer/notes.md) | 60.9 s | 33 | 1.85 / 1.96 | 2.54 · 1.52 · 1.38 · 1.69 | 9 % / 3 % | −21.1 | 16:9 |
| [Marty Supreme, official trailer (2025)](marty-supreme-official-trailer/notes.md) | 146.6 s | 116 | 1.26 / 0.88 | 2.29 · 1.02 · 0.87 · 1.47 | 59 % / 7 % | −16.8 | 2.39:1 |

Method note: the 1 fps contact-sheet tiles show the frame ~1 s *after* their label (ffmpeg `fps=1:round=down` keeps the last frame of each second). All times in these notes come from cut detection and 4–24 fps strips, not from the sheet labels.

## The core idea
A24 has no single house look. Each trailer borrows the film's own design (aspect ratio, card typeface, card colour, even the logo material) and keeps the trailer grammar very sparse: few text moments, dialogue on top, and one strong idea per trailer (a metronome, a slow burn, a silence, a loud word). What is constant is restraint and taste: hard cuts, no motion-graphics tricks, cards that look printed rather than animated, and the A24 logo treated as a beat in the edit.

## Sub-styles

**1. Genre-event main trailer** (Civil War)
- 27 s cold open on voice-over/dialogue, then the A24 logo in **silence** (music cut at the logo, 0.65 s of digital silence at −78…−81 dBFS), with the hit on the next picture.
- One strict type system for every card: tracked semibold caps (~0.3 em), warm tan, on the same smoke-and-embers plate. The tagline is split into one-word cards (ALL / EMPIRES / FALL, 0.7–0.9 s each) between ~1 s shots.
- A music-free dialogue scene as the turn (13 s; ~4 s near −65 dBFS), broken by gunshots, then a wall of music.
- Climax ASL 0.91 s, then a **7.3 s slow aerial before the title**; title fades up over 1.2 s.

**2. Auteur slow burn** (Midsommar)
- Dialogue-led and quiet for half the trailer; ASL falls every quarter (3.1 → 2.0 → 1.3 → 0.9 s); the last 6 s run at 0.25–0.40 s per shot, then a **hard cut to black** and a calm shot.
- Light cards (near-black old-style serif on off-white, italic lowercase lead-in + roman caps, 2.3–3.3 s holds, hard cuts) that match the film's white-linen world.
- A custom A24 logo made of the film's material (flowers) at 0 s; the end logo is drawn in **silence**.

**3. Prestige minimal / critics' grid** (The Zone of Interest)
- Festival credential first (Cannes red card at 2.3 s).
- A **metronome edit**: picture / black quote card / picture … every ~2.0 s, every cut on a percussive thump (69 % of cuts on an onset vs 18 % chance). Text is on screen 47 % of the time.
- No dialogue, no faces; locked-off symmetrical wides; mastered very quiet (−21 LUFS).

**4. Star-character trailer** (Marty Supreme)
- 32 s comic dialogue cold open that sells the character before the logo.
- **Loud type**: ultra-condensed heavy caps at 41–68 % H (MARTY, DREAM, BIG); a two-word phrase is split over two 0.6–0.8 s cards with 1.3 s of footage between them.
- An anachronistic pop needle-drop (identified from the lyric "Welcome to your life": Tears for Fears).
- Fastest stretch 0.69 s ASL at 68–82 % of the runtime → 4 s dialogue beat → title → 12 s "button" scene with credits building over the footage.

## Measured ranges (4 trailers)
- ASL 1.26–1.85 s; median 0.88–1.96 s. For the three full-length trailers ASL is 1.26–1.51 s and median 0.88–1.13 s.
- Shots under 1 s: 36–59 % for the full trailers (9 % for the metronome teaser). Over 3 s: 3–11 %.
- Cold open before the first card or logo: 0 s (custom-logo or festival openers) or **27–33 s** (19–22 % of the runtime) for the main trailers.
- Fastest section, always right before the title: ASL 0.40–0.91 s. The densest 10 s window sits at **70–90 % of the runtime** (Civil War 70–77 %, Midsommar 86–93 %, Marty 68–82 %), later than in the Marvel trailers (50–65 %).
- Title at **86–93 % of the runtime**; title hold 2.1–4.5 s; from title to end 5–20 s (an end card, or a "button" scene with credits).
- Text moments per trailer: 7–9 (main trailers), 15 (the critics' teaser). Text on screen: 12–16 % of the runtime (main), 47 % (critics' teaser).
- Card holds: one-word cards 0.6–0.9 s; credit/tagline cards 1.7–3.3 s; quote cards 2.0 s; date / end cards 1.5–4.0 s; A24 logo 1.5–2.2 s (the custom flower opener 6.0 s).
- Card size (ink height): quiet films 6–12 % H (Civil War taglines and title 11.5–12.3 %, Midsommar caps 7.5 % and title 10.6 %, Zone quotes 5.6–6 % and title 9.8 %); loud film 41–68 % H (Marty). The title is often **not bigger** than the taglines (Civil War 12.1 % vs 11.5–12.3 %).
- Loudness: −16.8 to −17.4 LUFS integrated for the main trailers, −21.1 for the minimal teaser. Loudest momentary −8.5 to −13.5 LUFS.
- Beat sync: the main trailers do **not** cut on the beat (27–31 % of cuts on onsets vs 27–29 % chance); they cut on lines and actions. The minimal teaser is fully beat-locked.

## Title-card typography and timing
- **The face comes from the film**, never a house font: tracked geometric caps (Civil War), old-style serif with an italic lead-in (Midsommar), condensed DIN-like mixed case (Zone), ultra-condensed heavy grotesque (Marty). All typeface names in the notes are look-alike guesses.
- One face and one colour per trailer, used for credits, taglines, title and date alike.
- Mostly **hard cut in, hard cut out**, with no slide, scale or blur motion. Exceptions are slow and filmic: a 1.2 s fade-up (Civil War title), a fade over picture then a dissolve to a plain card (Midsommar title), a second word popping in 0.9 s later (Marty), a credit stack building one line per 0.5 s (Civil War) or two names per 1 s (Marty).
- Colours: tan #A39077 on black with smoke, #1C1D18 on off-white #F1F2EC, white on black, white on a #121011 vignette. Festival red #A30001 for the Cannes card.
- Cards stay inside the film's letterbox.
- Credits used: "from / ARI ASTER", "director of / HEREDITARY", "THE WRITER OF / 28 DAYS LATER / EX MACHINA / ANNIHILATION". The filmmaker is the star of the card set.

## Colour and letterbox
- The film's own aspect ratio inside 16:9: 1.85:1 (10 px bars at 480p), 2.00:1 (26 px), 2.39:1 (62 px), or full frame.
- The film's own grade, untouched by trailer looks: naturalistic photojournalism (Civil War), cold-blue act 1 vs high-key pastel Sweden (Midsommar), flat cool daylight with deep focus (Zone), warm dark tungsten with teal accents (Marty). Lots of dark or empty frames (21–56 % "mostly empty" samples, almost all dark).

## Sound structure
- **Dialogue on top** in three of four trailers (a voice from the first second); the minimal teaser has no speech at all.
- Drop-outs are used as **drama inside the trailer, not as the pre-title trick**: silence under the logo (Civil War, music out for 1.4 s, 0.65 s of it digital silence), a music-free stand-off (4 s near −65 dBFS), 0.45 s of silence before an insert hit (Marty). None of the four has a true silence right before the title. Instead the music thins (Marty, −30 dBFS for 1.5 s), drops 4 dB at a cut to black (Midsommar), or simply carries on.
- Hits: the biggest hit comes **after a silence on the next picture** (+28 LU at the flag after the Civil War logo; +25 dB on the ball after Marty's 0.45 s gap) or as a metronomic thump on every cut (Zone).
- Endings fade out under the date or end card; the Midsommar end logo plays in digital silence.
- Music choice is part of the concept: a period-wrong pop needle-drop (Marty), a slow crescendo score (Midsommar), a wall of score after the turn (Civil War), drone + thump (Zone). (I cannot listen; the loudness data show no repeated big braam-type stabs.)

## What makes it premium
- **Restraint**: 7–9 text moments in 2.5 minutes, hard cuts, no animated graphics, quiet masters.
- **The film designs the trailer**: aspect, grade, typeface, card colour and even the logo material come from the film.
- **One idea per trailer**: a metronome, a slow burn, a silence, a loud word. It is executed strictly from start to end.
- **The logo is an edit beat** (in silence after a cold open, or built from the film's world), not a pre-roll.
- **Slow before the title**: a long aerial, a 4 s dialogue beat or a cut to black between the fastest montage and the title.

## Recipe (real footage + HTML/GSAP Hyperframes, 1920×1080, ~120 s)
1. **Pick the film's frame**: bars 21 px (1.85), 60 px (2.00) or 138 px (2.39) top and bottom; a light grade only (`contrast(1.04–1.12)`, ±10 % saturation). No LUT look on top.
2. **Pick ONE card system and use it for everything**:
   - Quiet caps: Montserrat 600, uppercase, `letter-spacing:.3em`, #A39077, 180 px for taglines/title (≈ 12 % H ink), 45/80 px for credit role/name; on #030102 with a slow smoke loop at the bottom (`opacity:.55`).
   - Printed serif: Cormorant Garamond 600 caps 115 px (`letter-spacing:.06em`) under a Cormorant Italic lowercase lead-in of 62 px; #1C1D18 on #F1F2EC.
   - Critic grid: Barlow Condensed 500, 56 px, white on #000, with a 30 px italic attribution right-aligned under the quote.
   - Loud: Anton caps, white, sized by ink at 41 % H (title) or 68 % H (single words), on `radial-gradient(#141213,#080808)`.
3. **Cards are cuts**: `tl.set(card,{opacity:1},t); tl.set(card,{opacity:0},t+hold)`. Holds: one word 0.6–0.9 s; tagline/credit 1.7–3.3 s; quote 2.0 s; title 2.1–4.5 s; date 1.5–4 s. A title may fade up over 1.2 s (`power1.out`). Credit stacks build one line every 0.5–1.0 s.
4. **Edit shape**: cold open 25–30 s on dialogue (ASL ~1.5–2.3 s) → logo 1.5–2 s → build (ASL ~1.1–1.4 s) → a music-free dialogue turn of 8–13 s → climax at 0.4–0.9 s ASL, peaking at 75–90 % of the runtime → one slow 4–7 s shot or a cut to black → title → 3–4 s date card or a 10–12 s button scene with credits over the footage.
   - Metronome variant (60 s): picture/card alternation on a fixed `P = 2.0 s`, a thump on every cut, 2–3 inserts of 0.4–0.6 s to break the grid, 7 s of untexted pictures before the title.
5. **Logo beat**: put the logo after the cold open. Duck the music to 0 over 0.1 s at the logo's in point, rack-focus the logo (`blur 14px → 0` in 0.4 s), hold 1.1 s, and put the hit on the first frame of the next shot.
6. **Sound**: dialogue on top at −20…−23 LUFS short-term; music builds from −24 to −14…−9 LUFS momentary at the climax. Use real silence only for drama (the logo, a stand-off, 0.4–0.5 s before an insert hit), not as a pre-title cliché. Fade out under the end card. Master −17 LUFS integrated (−21 for a minimal teaser).
