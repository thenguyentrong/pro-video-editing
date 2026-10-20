# #BestPhonesForever: That's A Wrap  (Google, 18 Dec 2024, 1:57 (116.5 s), 16:9, YouTube @madebygoogle)
URL: https://www.youtube.com/watch?v=w7l6RoqH-uo
Purpose: ad (humour / narrative series episode, holiday)
One-sentence point: Pixel and iPhone, best friends, are trapped in gift boxes under a Christmas tree; Gemini Live talks them through it ("you're presents!") - a buddy comedy where the joke is the product benefit.

## Structure
- 0-6.2 s establishing: CGI presents under a decorated tree, still.
- 6.2-17 s setup: cross-cut inside two boxes - Pixel 9 Pro (porcelain, in tissue paper) and iPhone (dark, flashlight on, in shredded paper). "Hello?" "Pixel? Is that you?" "I'm trapped in a box!" "Me too!" "You should ask Gemini for help!"
- 14-30 s: Pixel's screen lights up with Gemini Live (blue glow lights the tissue paper); Gemini suggests poking a hole, then yelling.
- 30-47 s: "AAAHHH" (33-37 s, the loudest dialogue), cut out to the silent tree (35-36 s wide = nobody hears them), iPhone despairs ("doomed to spend eternity... scent of fresh pine").
- 45-50 s: iPhone's box tips over (camera tilts, "Whoa!"), Pixel figures it out.
- 50-75 s turn: Gemini: "It sounds like you might be inside a holiday gift box!" - "We're... presents?" (dead air before it), iPhone panics.
- 75-100 s heart: Pixel: "it's the holidays... friends and family that accept you for who you are" - longest takes (9.5 s at 85 s), iPhone "Awww. Thanks, Pixel."
- 97-104 s: tree wide (7.5 s hold), super "Now we're talking." (102-104 s).
- 104-109 s: the Pixel falls onto a white floor (motion-blur drop), name card "Google [phone] Pixel 9 Pro" on off-white.
- 109-112.5 s: "with ✦ Gemini" slides in with motion blur -> "with ✦ Gemini Live" (gradient text + audio-bars icon), the sparkle shrinks to a dot.
- 113-116.5 s: Google "G" + GoogleStore.com on white.

## Cut rhythm (cuts2 only - all 21 soft candidates checked by eye were camera moves, screen-light changes or text appearing inside a shot)
- 46 shots, ASL 2.53 s, median 1.84 s. Quarters 2.08 / 1.94 / 1.94 / 5.83 - dialogue pace, then long emotional holds and end cards.
- 22% < 1 s, 33% > 3 s. Longest 9.5 s (85.0 s, Pixel's speech), 7.5 s (97.2 s tree), 6.7 s (109.9 s end), 6.2 s (opening). Shortest 0.33 s (71.3 s, panic).
- 4-6 cuts per 10 s in the dialogue (shot / reverse shot on each line), 2 per 10 s at the end.
- Cuts on onsets 56% vs 47% chance - cuts land on the start of lines.

## Typography
- Only at the end: "Now we're talking." white Google Sans, centred over the tree (cap ~5% H); name card "Google | phone | Pixel 9 Pro" on off-white #F3F2EE (line 12.7% H incl. descender, cap ~8.5% H); "with ✦ Gemini Live" (line 7.3% H) with "Gemini Live" in a blue-to-pink gradient.
- Motion-blur slide-in on the Gemini line (109 s), sparkle collapse to a point (112 s).

## Colour / grade
- Warm, cosy holiday CGI (red/gold/green presents, soft window light) vs. dark box interiors with a heavy vignette; Gemini = cool blue screen glow. End cards bright off-white.
- 10% of samples >= 70% empty (all on light, the end cards).

## Camera / shots
- 100% 3-D animation, "live-action" lens language: shallow focus, lens flares, slow push-ins, handheld-like drift, a tilt when the box falls. The phones act through light (flashlight blinks, screen glows) and small moves - no faces.

## Transitions
- Hard cuts (shot / reverse shot), cut-outs to the tree wide as comic punctuation (35 s, 42 s, 45-47 s). A motion-blur fall into the end card.

## Sound
- Dialogue-led: three voices (Pixel, iPhone, Gemini). Integrated only -23.7 LUFS (quiet, TV-drama level), median -30 dBFS.
- Comic timing in silence: 32 gaps of 0.15-1.5 s at -60 to -68 dBFS between lines; dead-air beats 0.95 s (24.6 s), 0.65 s (38.2 s), 1.5 s (62.65 s, before "We're... presents?").
- Biggest rise +47.5 dB at 25.9 s; yelling 32-37 s. An indie pop song enters for the end (loudest window 107.8 s).

## What makes it premium
- Character comedy: two phones with personalities, the rival brand is a friend, not a target.
- The feature (Gemini Live) is the plot device that solves the problem.
- Cinematic CGI lighting with practical light sources (flashlight, screen glow).
- Restraint in the end card: one line, one product, one logo.

## Recipe (real footage + HTML/GSAP)
- Real-footage version: two phones on mini sets (shoe boxes, tissue paper), macro lens, one practical light each (phone torch, screen at full brightness), heavy vignette (`radial-gradient(transparent 40%, rgba(0,0,0,.75))`).
- Record dialogue first; cut shot/reverse shot on each line, leave 0.6-1.5 s of dead air before punchlines.
- Cut-away wide (3 s, silent) after a big line = comic punctuation.
- End: white super cap 5% H over the wide (1.5 s), product drop onto #F3F2EE (0.6 s, `y: -60% -> 0`, `ease: bounce.out` subtle), name card split around product, then "with ✦ Gemini Live" sliding in (`x: 40 -> 0, filter: blur(8px) -> 0`, 0.5 s) with gradient text (`background: linear-gradient(90deg,#4285F4,#C76BD3); -webkit-background-clip: text`).
- Mix dialogue around -24/-20 LUFS; let the song lift the end.
