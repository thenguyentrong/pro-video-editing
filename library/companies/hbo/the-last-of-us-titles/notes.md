# The Last of Us – Opening Credits  (HBO, uploaded 2023-01-16, 79.3 s file = 64.5 s sequence + 3 s HBO Max card + 11 s YouTube end screen, 16:9, YouTube / HBO Max channel)
URL: https://www.youtube.com/watch?v=8SWhBsbxmpk
Purpose: main title sequence (series opening credits)
One-sentence point: a fungus grows over a miniature world like a map of civilisation, and the title itself grows out of the fungus.

Structure:
- 0.0–1.0 black, music silent.
- 1.0–5.5 HOOK: macro of thin ochre tendrils in the dark; first card is the two stars split into opposite corners (PEDRO PASCAL lower-left, BELLA RAMSEY upper-right). Music enters at 6.55 s (+15 dB jump, the biggest rise in the piece).
- 6–16 BUILD 1: camera cranes up over a fungal "terrain" with river-like veins; at 8–16 a "city skyline" of pale fungal stalks rises against a blown-out backlight, with red cordyceps blooms in the foreground (city = overgrown).
- 17–31 BUILD 2: top-down over a glowing golden spore network that reads like a satellite photo of city lights at night (my reading, not stated).
- 32–44 DARK MIDDLE: moss ridge, then red tendrils curl into a ring and reach like fingers (41–43).
- 45–55.5 TURN: ground-level view through fungal "grass" toward a bright hazy horizon; two tiny silhouettes (an adult and a child = Joel and Ellie) appear at 53–55 under "CREATED FOR TELEVISION BY".
- 56.5 hard cut to black: a red fungus cluster grows in frame centre and forms the title THE LAST OF US (58–60), holds to ~62, fades to black by 64.5.
- 65.5–68.5 HBO Max end card ("CHOOSE YOUR PLAN", "STARTING AT $9.99/MONTH"); 69–79 YouTube end screen (not part of the sequence).

Cut rhythm: 2 shots in 65.5 s (ASL 32.8 s). One continuous CG camera move of 56.5 s, then one hard cut to the title shot (9 s). No cut is visible on the 1 fps sheet inside the long move (the soft detector fires 23 times, all on credit text fading in/out). The real rhythm comes from the credits: about 18 credit cards in 56 s = one new card every ~3.1 s, each visible ~2 s.

Typography:
- Names: condensed bold grotesque, all caps, off-white (~#d9d5cc), slight tracking (+2–3 %). Closest free match: Oswald 600 or Bebas Neue. Cap height measured 3.3 % of frame height (t=2.5 s).
- Role labels ("PRODUCTION DESIGNER", "EXECUTIVE PRODUCER"): small regular wide sans caps (Montserrat 500 / Gotham-like), ~1.5 % of frame height, ~70 % opacity, sitting directly above the name, centred on it.
- Placement roams: lower-left, upper-right, lower-right, bottom-centre; always inside the dark negative space, never over the bright subject.
- Animation: plain opacity fade, about 0.5 s in, ~2 s hold, 0.5 s out. No motion on the text.
- Title: three stacked lines "THE / LAST / OF US", heavy condensed grotesque with worn/eroded texture, off-white, centred, letters span ~13–88 % of frame height (~75 %). It is revealed by red CG fungus growing through it (56.5–60 s), not by a type animation.

Colour/grade: near-black base (~#0b0d0e) with ochre/amber fungus (~#c89a3a), cordyceps red (~#b8343a) and warm white haze. Heavy vignette, very shallow depth of field (miniature/tilt-shift look). 29 % of sampled frames are "mostly empty" (all dark). No letterbox. HBO bug bottom-right throughout (YouTube watermark).

Camera/shots: 100 % CG macro "miniature landscape" (no live action, no actors). Slow continuous crane/dolly moves, top-down for the network section, ground-level for the ending. Focus pulls give the only sense of "edit".

Transitions: 1 hard cut (to the title), 1 fade to black at the end. Everything else is a continuous camera move; "scene changes" happen by flying over the next area.

Sound: the show's guitar-led theme by Gustavo Santaolalla (known track; I did not listen, the shape below is measured). Silent first second, then quiet (−37 LUFS momentary) until the music enters at 6.55 s. After that a flat plateau between −19 and −23 LUFS for 50 s, no drop-outs, no build to a drop. Loudest at 58–60 s while the title grows (−17), then decays to −39 by 64 s. Integrated −22.4 LUFS, LRA 7.5 LU, true peak −5.3 dBFS: mixed quiet, like TV, not like a YouTube ad. The single cut lands on an audio onset. No voice.

What makes it premium:
- One idea, one continuous move: the metaphor (fungus = civilisation map) carries everything; there is no montage.
- Restraint in type: tiny condensed caps, fade only, placed in negative space so they never fight the image.
- Miniature macro look (shallow DOF + backlight haze) makes CG feel tactile and real.
- The title is the payoff of the same process (fungus grows the letters) instead of a separate logo animation.
- Quiet, flat music level; the image does the work.

Recipe (real footage + HTML/GSAP, Hyperframes):
- Footage: real macro of moss, lichen, mould/slime-mould time-lapse, dry roots; shoot or source with 100 mm macro at f/2.8 so the depth of field is very shallow. Grade: lift blacks to ~#0b0d0e, push mids to amber (#c89a3a), keep one accent red (#b8343a), add radial vignette (transparent 45 % → rgba(0,0,0,0.85) at 100 %) and fine grain (opacity 0.08).
- Fake the single long move: chain 4–5 clips with 1.5 s cross-dissolves hidden in dark areas, and add a slow GSAP camera on the video wrapper (scale 1.00 → 1.12 and y −3 % over the whole clip, ease "none").
- Credits: names Oswald 600, uppercase, letter-spacing 0.03em, 36 px on 1080p (3.3 %); label Montserrat 500, 16 px, letter-spacing 0.14em, opacity 0.7, 6 px above the name. One card every 3.0 s; tl.fromTo(card, {opacity:0}, {opacity:1, duration:0.5, ease:"power1.out"}).to(card, {opacity:0, duration:0.5}, "+=2.0"). Rotate anchors: bottom-left (8 %/78 %), top-right (78 %/22 %), bottom-right, bottom-centre.
- Title: black frame, stacked condensed title at ~75 % of frame height; reveal with an SVG mask fed by an animated feTurbulence + feDisplacementMap (baseFrequency 0.02 → 0.006 over 2.5 s) or a real mould time-lapse used as a luma matte; hold 2 s; fade out 2.5 s.
- Audio: one acoustic theme, enters ~6 s in, keep level flat (about −20 LUFS momentary), let the title be the loudest moment, end in a decay, no SFX hits.
