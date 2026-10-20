# Netflix — trailer and promo style

Four official Netflix uploads measured at 480p (cuts2 + eye check of every detected cut on before/after pairs, soft cuts added by eye, EBU loudness, 50 ms RMS, text measured in % of frame height H). I could not listen to the audio: everything about sound comes from level data, subtitles and the picture. All four files end with the same 10.6–13.3 s YouTube end screen (N + SUBSCRIBE on red); it is cut off before every number below.

| Example | Kind | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Aspect |
|---|---|---|---|---|---|---|---|---|
| [Stranger Things 5, official trailer (2025)](stranger-things-5-official-trailer/notes.md) | series, final season | 161.2 s | 96 | 1.68 / 1.36 | 2.01 · 1.34 · 1.26 · 2.37 | 29 % / 10 % | −17.1 | 2.00:1 |
| [Squid Game S3, official trailer (2025)](squid-game-s3-official-trailer/notes.md) | series, final season | 107.6 s | 89 | 1.21 / 0.92 | 1.58 · 0.84 · 0.79 · 2.99 | 60 % / 3 % | −14.1 | 2.00:1 |
| [Narnia: The Magician's Nephew, official trailer (2026)](narnia-magicians-nephew-official-trailer/notes.md) | film, theatrical/IMAX first | 150.0 s | 80 | 1.88 / 1.40 | 2.21 · 1.79 · 1.25 · 2.50 | 16 % / 12 % | −14.1 | 1.90:1 |
| [Netflix Tudum 2025, official trailer](tudum-2025-official-trailer/notes.md) | live-event promo | 76.8 s | 75 (+14 word pops) | 1.02 / 0.58 | 1.48 · 0.80 · 0.71 · 1.37 | 79 % / 5 % | −14.2 | 2.00:1 |

## The core idea
Netflix runs a **brand frame around a show-skinned trailer**. The frame is fixed and almost identical every time: a corner title bug, the red N light-ribbon sting, an "ONLY ON NETFLIX / date" card in Netflix Sans, the N at the end, the YouTube end screen. Inside the frame, everything else is borrowed from the show: the N sting is rebuilt out of the show's sets and colours, mid-trailer cards use the show's own typeface and palette, the title is the show's own title animation. When the product is a theatrical film (Narnia) the frame is switched off almost completely and the trailer behaves like a studio trailer. For brand events (Tudum) the frame becomes the content: logo, light streaks, kinetic type.

## Sub-styles

**1. Series trailer, flagship / final season** (Stranger Things 5, Squid Game 3)
- Quiet cold open (3–14 s at −26…−44 dBFS) on one strong image or sound idea (a sung nursery rhyme in Squid Game).
- **N sting after the cold open**, not at 0 s: 14.14 s and 16.64 s, 2.2 s long, built from the show's world (Upside-Down vines and red light bars; the pink/green stair-maze set), then 0.5 s of the flat red N on black. +25…+33 dB over the cold open.
- Body ASL 1.2–1.7 s with 3–4 cards in the show's typeface, 1–3 words each.
- A "THE FINAL SEASON" statement card (2.0–2.4 s), the title in the show's own logo animation (6.3–6.6 s), then 1–2 date cards and the end N.

**2. Film trailer with a theatrical release** (Narnia)
- No corner bug, no opening N. Credits are placed inside shots ("C.S. LEWIS" over a wide, "GRETA GERWIG" revealed behind a foreground edge during a dolly, "THE DIRECTOR OF Barbie" inside a glass orb), later 4 short cards (1.2–1.4 s) on one nebula plate in one serif.
- Studio end block: title 4.0 s, director credit, IMAX card, "ONLY IN THEATERS / FEBRUARY 12" + format logos (each ~1.2 s), then a 1.8 s N recoloured to the film's prismatic palette.
- Slower open (8.7 s before the first credit), 4.5 s of black before the last act, no drop-out before the title.

**3. Event / brand promo** (Tudum 2025)
- Logo first (7.2 s chrome 3D TUDUM on a spectral light-streak floor), then kinetic type sentences built word by word on the beat, a roll call of show logos (0.4–0.9 s each + 1–2 clips), "LIVE ON NETFLIX" badge, date.
- The fastest cutting (ASL 1.02 s, 79 % under 1 s) and the only one clearly cut to the beat (36 % of cuts on onsets vs 18 % chance).
- Ends like a trailer: talent button (3.9 s) → 1 s of black at −62 dBFS → logo on a +54 dB hit → date card → N.

## Measured ranges
- **Pace:** ASL 1.2–1.9 s for trailers, 1.0 s for the event promo; median 0.9–1.4 s (0.58 promo). Under-1 s shots 16–60 %. Shortest normal shots 0.29–0.46 s.
- **Where it peaks:** in three of four the densest 10 s windows sit at 60–80 % of the runtime (ST5 100–120 s = 9 per 10 s; Narnia 100–110 s = 11; Tudum 50–60 s = 17); Squid Game runs flat-out from 28 % to 74 % (12–14 per 10 s, max 14 at 37–46 %). The last quarter always slows down: ASL 2.4–3.0 s in the three trailers.
- **Beat sync:** trailers 14–23 % of cuts on onsets (chance 11–16 %) = cut to dialogue and action; the promo 36 % (chance 18 %).
- **Title position:** at 88–93 % of the runtime (145.5/161.2, 95.9/107.6, 139.8/150.0; the Tudum logo returns at 67.7/76.8). Title holds 4.0–6.6 s.
- **End block after the title:** 5.4–9.1 s from the end of the title to the end: statement card 2.0–2.4 s, date cards 1.3–2.5 s each, end N 1.8–3.5 s.
- **Text moments:** 3–4 body cards in the series trailers, 3 in-scene credits + 4 cards in the film, ~10 type stacks in the promo. Body card holds 0.95–1.75 s (a 2 s build-in for Stranger Things).
- **Empty frames:** 6–32 % of samples mostly empty (dark trailers high, the candy-coloured Squid Game lowest).

## Title-card typography and timing
- **Corner bug** (series + event): first 4–5 s of footage = top-left thin red vertical rule + 2-line white sans "SHOW: / SEASON N" (cap ~2 % H, x 5 %, y 10–15 %) and a grey N monogram top-right (~7.5 % H). Then a semi-transparent "NETFLIX" wordmark top-right for the rest of the trailer (~4 % H, x 85–95 %, y 10–15 %, just under the letterbox bar). Hidden on full-frame cards, title and end block. Absent in the theatrical film trailer.
- **Body cards = the show's type and colour:** Stranger Things: outlined Benguiat-style serif in red neon on red smoke, cap 8–9 % H, letters assembling out of blur over ~2 s. Squid Game: the logo alphabet (wide geometric caps) in white on guard-pink grunge (#f0538a), cap ~13.5 % H, word starts 1.4× and settles in 0.4 s, holds ~1.0 s, alternating with 0.5 s shots ("EVERY GAME" / "One." / "COMES" / "Two." / "TO AN END" / "Three."). Narnia: cream flared serif (Cinzel-like) on a dark nebula plate, eyebrow ~6–7 % H + main line 12–13 % H.
- **Netflix's own type** appears only in the brand frame: "THE FINAL SEASON" (heavy geometric caps, light grey #afb2b6 with a soft glow, cap ~10 % H, 2.0 s on black) and the date cards: centred white sans, light eyebrow "ONLY ON NETFLIX" ~3.5 % H over a bold date 6.5–8.5 % H, sometimes light + bold in one line ("VOL 1 **NOVEMBER 26**"), 1.4–2.5 s, placed over a moving plate from the show.
- **Event type:** white Netflix-Sans-Black-like caps with a spectral edge glow (cyan → violet → red → amber), word stacks growing ~1.8× per line (9.5 → 17 → 26 % H), new word every 0.17–0.5 s, hard pops.
- In and out: cards cut in and out hard; only builds (letters assembling, words settling, shapes morphing into the logo) are animated. One dissolve per trailer at most.

## Colour and letterbox
- **2.00:1** letterbox for both series trailers and the event promo (bars ~27 px of 480 = 5.5 % H), kept on every card and logo. **1.90:1** (IMAX) for the film (bars 3.3 % H).
- The brand colour is the N's light-ribbon spectrum: red #e50914 for the series frame, the full spectrum (red, magenta, violet, cyan, amber) for events, and a recoloured N when the film's palette demands it (prismatic N in Narnia).
- Inside, each trailer keeps its show's grade: blue night vs red Upside-Down (ST5), saturated candy sets (SG3), desaturated London → jewel-tone other worlds → violet nebula (Narnia).

## Sound structure
- Integrated −14 LUFS (Stranger Things 5 is the exception at −17.1).
- **Quiet start:** −26…−44 dBFS in the first 3–15 s, then the first big rise on the N sting or the first hit (+25…+33 dB).
- **One real silence near the end**, then the biggest hit: ST5 3.7 s of black at −38…−49 dBFS before the title run (title back at −14 dBFS); Tudum 0.75 s at −62 dBFS → +54 dB on the logo; SG3 a 0.4 s dip to −33 dBFS → +22 dB on "THE FINAL SEASON" and a 0.75 s near-silence (−51 dBFS) before a key line. The film trailer (Narnia) keeps the music under the title and uses a 4.5 s black where the level only drops 10–15 dB.
- **Loudest block** = the card run or the montage at 60–75 % of the runtime (−8…−13 dBFS).
- **Outro:** music fades 20–50 dB under the date card and the N; a small level bump on the N in three of four (probably the "ta-dum", not verified by ear).

## What makes it premium
- The brand is re-skinned per show (N sting built from the sets, cards in the show's font and colour), so the logo never feels pasted on.
- A strict, repeatable frame (bug → sting → acts → title → statement → date → N) that viewers learn, while the inside changes every time.
- Restraint at the end: slower last quarter, one silence, one hit, a short plain date card.
- Few words: 3–4 cards of 1–3 words; in non-English shows the subtitles carry the story (34 % of Squid Game samples).
- Mixed weights instead of decoration on the date card (light label + bold date).

## Recipe (real footage + HTML/GSAP, Hyperframes)
Target: a 90–120 s "season" trailer for your own project.
1. **Frame:** 1920×1080, 2.00:1 bars (60 px top/bottom, black divs on top of everything). Master −14 LUFS.
2. **Cold open 0–12 s:** 2–4 shots on one strong idea, music under −30 dBFS. Corner bug for the first 5 s: 4 px red rule (`#e50914`) + two lines Inter 500 20 px white at `left:96px; top:110px`, a monogram 80 px high top-right at 60 % opacity; then swap to a 40 px wordmark top-right at 70 % opacity until the title; hide it on cards.
3. **Brand sting at 12–16 s (2.2 s):** your logo masked over a plate from your own footage, with 6–10 vertical light bars (`linear-gradient(to bottom, transparent, #e50914 40%, transparent)`, `filter:blur(2px)`) that `scaleY 0→1` staggered 0.04 s `expo.out`; 0.5 s flat logo on black; audio +25…+30 dB over the cold open.
4. **Body:** ASL 1.2–1.5 s, rising to 9–14 cuts per 10 s at 60–75 % of the runtime; cut to lines and actions. 3–4 cards in your project's own typeface/colour, 1–3 words, hard cut in/out, hold 1.0–1.5 s; a three-card run alternating with 0.5 s shots works well. Settle move: `gsap.fromTo(word,{scale:1.4},{scale:1,duration:.4,ease:"expo.out"})`.
5. **Brake:** last 20–25 % at 2.5–6 s per shot; 0.75–3.7 s of black with the music ducked to about −45 dBFS; one last image (a question, a stare), then the title on the biggest hit.
6. **Title (5–6.5 s):** build it from your own motif (letters sliding in from scale 1.6 and off-frame `power3.out` 2.5 s, or shapes morphing 2.5 s `power3.inOut`), hold ≥ 2.5 s.
7. **End block:** statement card 2.0 s (Montserrat 800, `#afb2b6`, `text-shadow:0 0 30px rgba(255,255,255,.25)` on black) → date card 2.0 s (eyebrow Inter 300 caps 40 px, date Inter 800 90 px, over a moving plate from your footage) → 1 s light-bar wipe → logo 2.5 s while the music fades 25 dB. Keep it all inside the bars.
