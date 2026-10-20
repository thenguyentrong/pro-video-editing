# Stripe — launch and event film style

Three official Stripe films measured at 480p/360p (scene + adaptive cut detection, every cut checked by eye on the contact sheet and cut pairs, EBU loudness, speech spans by voice detection; no transcripts). Sizes are % of frame height (H). "≈" = by eye.

| Example | Year | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | Voice | LUFS (I) |
|---|---|---|---|---|---|---|---|---|
| [Introducing Stripe Radar](introducing-radar/notes.md) | 2016 | 100.7 s | 41 | 2.45 / 2.17 | 2.29 · 2.80 · 2.10 · 2.10 | 5 % / 24 % | 2 interviewees, ≈90 s of speech | −18.1 |
| [Introducing Stripe Reader S700](introducing-reader-s700/notes.md) | 2023 | 74.1 s (72.7 s + black) | 45 | 1.62 / 1.36 | 1.51 · 1.65 · 1.40 · 1.65 | 31 % / 11 % | 3 interviewees, ≈60 s of speech | −19.6 |
| [Stripe Sessions 2024](sessions-2024/notes.md) | 2024 | 108.9 s | 92 | 1.18 / 0.98 | 1.09 · 1.30 · 1.01 · 1.24 | 50 % / 3 % | stage bites, ≈100 s of speech | −13.9 |

## The core idea
Stripe sells infrastructure that nobody can see, so it never shows "the product" as a hero for long. It shows **the people who build on it**: a customer's workshop, café or conference crowd, with real voices (customer founders, Stripe engineers, speakers on stage) and no narrator. The software appears as filmed screens, a few seconds of renders, or slides on a stage. The brand lives in a small, strict graphic layer: the violet palette, one lower-third system, one end card. The films are calm, documentary and credible; even the event sizzle has no hype text.

## Sub-styles
**1. Customer-story launch film** (Radar, Reader S700)
- Opens in the customer's physical world without a title (Radar: 11 s of factory; S700: a 2 s product flash of five 0.36 s shots).
- 2-3 interview voices carry the whole film (speech 60-90 s of 74-101 s). Cuts follow sentences, not the beat (cuts on onsets at or below chance).
- Product proof in the second half: filmed UI with the cursor (Radar, 47-80 %), 3-4 s of clean renders on a lavender gradient + real taps in the café (S700, 46-71 %).
- Even pulse: quarter ASL varies only 1.4-1.65 s (S700) or 2.1-2.8 s (Radar).
- Quiet master: −18 to −20 LUFS integrated, LRA 2.5-4.5 LU, no drop-outs.

**2. Keynote sizzle** (Sessions 2024)
- Cold open in the dark (5 s), then the event lockup on a hit, then 100 s of stage, crowd and expo at ASL 1.18 s (half the shots under 1 s).
- Stage speech bites (2-6 s each) laid over a driving track; the launches are named by the slides inside the shots, not by added titles.
- One speed-up: a partner-logo burst of 10 shots at 0.17-0.3 s at 58-60 % of the runtime.
- Star guest at 81-90 %; founders open and close; the lockup bookends the film. Master −13.9 LUFS, two 0.4-0.7 s music cuts for key lines.

## Rules with numbers
- **No narrator.** Voices are customers, staff or speakers, identified by a lower third the first time (hold 2-3 s).
- **Lower third (2023-24 system):** thin vertical bar | name (cap ≈3.8 % H) | thin bar | role (≈2.9 % H), white, one line at y ≈83 % H, starting x ≈6 %. 2016 system: name/role in navy on angled gradient ribbons, bottom-right.
- **Graphics in brand violet only:** ≈#5d4df8 / #796af9 panels and maps, lavender gradient ≈#a6a7f7 → #bfc0f9 for renders, navy ≈#0f1f2c type, off-white ≈#f5f9fa end card; 2016 gradient ≈#8052d9 → #cd7dee; event gradient pink ≈#eb91ad / orange / violet.
- **Words on screen per film:** 0 claims. Only names, a city, 1-2 word feature labels (S700: 4 labels, ≈5 % H condensed caps), and the end card.
- **Product on screen:** filmed screens at an angle with shallow focus, or 3-4 s of renders; never a long screen capture.
- **End card:** product or event name + URL, centred, 1.5-4 s; S700 adds a three-logo partner row; Sessions repeats the opening lockup.
- **Transitions:** hard cuts (≥95 %). Graphic transitions are rare and branded: split-screen panel wipe, circle iris from a map, white wave wipe to the end card.
- **Loudness:** customer films −18 to −20 LUFS (voice-first), sizzle −14 LUFS.

## Recipe (real footage + HTML/GSAP, 1920×1080)
1. Pick the format: customer-story (75-100 s, ASL 1.6-2.5 s) or sizzle (100-110 s, ASL 1.2 s).
2. Customer-story: open on the customer's world (no title) 2-11 s → interviews with split-screen feature labels → product proof (filmed UI or 3-4 s renders + real use) → payoff montage at ≈1 s per shot → end card.
3. Sizzle: dark cold open 5 s → lockup on the first hit (1.8 s) → arrivals/expo → stage launches with bites → 10-shot logo burst at ≈60 % → star guest at ≈85 % → founders close → lockup.
4. Lower third: `Inter 400 3.8vh` name + `2.9vh` role, white, 1 px bars, `left:6%; top:80%`, fade 0.3 s.
5. Split-screen label: right half `#5d4df8`, icon + `Oswald 600 5vh` caps, panel slides in 0.4 s.
6. End card: `#f5f9fa`, name `Inter 600 5.5vh #0f1f2c`, URL `3.5vh`, hold 1.5-2 s, then a logo row 1.5 s.
7. Sound: voices on top, bed 8-10 dB under speech; customer films master −19 LUFS, sizzle −14 LUFS; at most two short music cuts before key lines.
