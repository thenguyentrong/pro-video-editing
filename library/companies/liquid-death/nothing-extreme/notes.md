# There's nothing extreme about new Liquid Death Sparkling Energy.  (Liquid Death, 2026-01-09, 30.1 s, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/ZSIBciBYpf0
Purpose: social ad / product launch (energy drink)
One-sentence point: A sober health-claims script ("better for you", caffeine like coffee, zero sugar, made with a doctor) is read by black-metal, biker, snake and gimp characters, so the claim "nothing extreme" is the joke.

Structure: beats with timestamps
- 0.0-0.8 hook: the can racks into focus from bokeh in a hand, word caption "INTRODUCING" already on screen; the product is the first image.
- 0.8-3.0 product hero with captions naming it; the can fills ≈60 % of the frame height.
- 3.0-19.4 build: six "testimonial" set-ups, one per claim (metal guy doing yoga, biker in a sauna, tattooed woman with a python, gimp-suit cyclist). Each person reads one claim to camera; deadpan wellness-ad acting.
- 19.4-22.0 authority beat: a real doctor with lower third (name + title), in a clean clinic.
- 22.0-26.0 payoff: a sword swallower in the clinic behind him; captions ask why everyone tries to be so extreme.
- 26.0-30.1 end card: purple gradient, 3-line headline + 1-line spec, two cans floating. Hard end.

Cut rhythm
- 11 shots, ASL 2.73 s, median 2.67 s, 0 % < 1 s, 36 % > 3 s, ≈22 shots/min. Quarters 1.88 / 1.88 / 1.88 / 3.76 s: an even grid, then the 4 s gag and 4 s card.
- Cut on line ends, not on music (50 % of cuts on an audio onset vs 47 % chance).

Typography
- Word/phrase captions: heavy italic extended caps, warm cream fill (≈#F3E3B5) with a black outline, 2-4 words per card, cap ≈1.6 % H, centred at ≈67 % H; switched per spoken phrase (≈0.8-1.5 s), no animation. Closest free: Archivo Black with a -10° skew, or Barlow Black Italic.
- Small legal line in white under the caption on the stunt shot (≈71 % H, cap ≈0.6 % H).
- Lower third: white bold caps name (cap ≈1.6 % H) + light sentence-case title, centred at ≈45-47 % H, no box.
- End card: 3 lines heavy caps (cap ≈2.6 % H) at 12-23 % H, then a condensed spec line; free: Archivo Black + Barlow Condensed 600.

Colour/grade
- Bright, glossy commercial grade (warm sun, clean clinic). Characters in black; brand colours come from the cans (cyan, pink, gold). End card purple-to-violet gradient.

Camera/shots
- Locked or slow push-in mediums at eye level, subject centred, shallow depth of field. Product in hand in most shots. No handheld.

Transitions
- 10 hard cuts. One rack focus in the first second. No effects.

Sound
- Read-to-camera lines + light upbeat bed; -15.2 LUFS, LRA 2.3 LU, peak -1.9 dBTP. Biggest hit +26 dB at 22.4 s on the sword-swallow reveal. No drop-outs.

What makes it premium
- Real commercial production value (lighting, casting, art direction) used for a deadpan parody of wellness ads.
- One rule: every claim is sober, every speaker is extreme; the contradiction repeats 6 times on a 2-3 s grid.
- Captions do the reading for sound-off viewers but keep the brand's metal look (heavy italic caps).
- End card states the plain offer once, after the joke.

Recipe (real footage + HTML/GSAP, 1080x1920)
- 30 s: 0-3 s product in hand (rack focus 0.4 s), 6 × 2.5-3.5 s testimonial set-ups, 2.5 s authority, 4 s gag, 4 s end card.
- Caption: `font: italic 900 46px "Archivo Black"; transform: skewX(-10deg); color:#F3E3B5; -webkit-text-stroke:3px #000; paint-order:stroke fill; text-transform:uppercase`, centre y ≈1290 px, `tl.set` per phrase.
- End card: `radial-gradient(#7A2BE0,#3B0D8F)`, headline 3 lines `900 56px` at y 230-440 px, cans `from {y:80, rotation:-8, autoAlpha:0}` 0.5 s `power3.out`.
