# Linear — launch film style

Three official Linear films measured at 480p (adaptive cut detection + eye check of every cut on before/after pairs, EBU loudness, 50 ms RMS, speech detection for voice timing; text measured in % of frame height H). Analysed Oct 2026.

| Example | Length | Shots | ASL / median | ASL by quarter | <1 s / >3 s | LUFS (I) | Voice | Aspect |
|---|---|---|---|---|---|---|---|---|
| [Introducing Linear Agent (2026)](introducing-linear-agent/notes.md) | 54.9 s | 10 | 5.49 / 5.32 | 4.57 · 4.57 · 3.43 · 4.57 | 0 % / 100 % | −28.9 | none | 2:1 |
| [Introducing Linear Diffs (2026)](introducing-linear-diffs/notes.md) | 51.9 s | 11 | 4.72 / 3.73 | 3.24 · 4.33 · 4.33 · 3.24 | 0 % / 73 % | −13.9 | none | 16:9 |
| [INSPECT, customer film (2026)](inspect-ramp-film/notes.md) | 236.8 s | 42 | 5.64 / 3.34 | 5.38 · 9.87 · 3.70 · 4.93 | 5 % / 60 % | −14.2 | interview, ≈2.8 w/s | 16:9 |

Method note: the two feature films are near-black (mean luma 0.05-0.06); ffmpeg scene detection found 0 cuts in both. Use the adaptive detector for this look.

## The core idea
Linear films the real interface like a luxury product: the UI is a dark object in a black void, tilted in perspective, lit from inside, with shallow depth of field and a slow camera. Nothing explains it: no voice, no feature labels, no captions. One task plays out from first click to result (ask → result → plan; open → read → change → approve), and a single short tagline closes it. The customer films use the same restraint in live action: documentary interviews, warm practical light and one mono HUD language instead of screen recordings.

## Rules with numbers
1. **Black void, real UI as the hero.** Background #000; UI greys; mean luma 0.05-0.06. Colour only from the product (status dots, red/green diff, one indigo button ≈#5e6ad2).
2. **Perspective and depth.** Tilt the UI card ≈20-35°, keep a sharp band and blur the rest; one flat frontal wide per film (at 35-40 s or 15-25 s).
3. **Even, slow pulse.** Feature films: 10-11 shots in 52-55 s, ASL 4.7-5.5 s, no shot under 2.2 s, longest 8-10 s. The camera moves inside every shot; the cut changes the angle.
4. **One task, no words.** Typing at ≈10 chars/s, lists build line by line; the only copy is a 3-4 word tagline at the end.
5. **End system.** Hard cut or 0.4 s dip to black → wordmark/tagline centred (line box 9-10 % H, cap ≈6-7 % H, ≈50-53 % of the width) for 2.5-5 s → logo for 4.5 s → 0.9-2.2 s silence.
6. **Sound: music only, often quiet.** No VO in feature films. Either a whisper-quiet ambient bed (−28.9 LUFS) or a two-part electronic bed that lifts +6 to +8 dB on the key action at ≈50 % (−13.9 LUFS). Cuts follow camera moves, not beats.
7. **Customer films = documentary.** Off-axis interviews, inserts of hands and objects, warm tungsten vs cool daylight, ASL ≈5.6 s with a 37 s graphics hold mid-film, voice almost wall to wall (≈2.8 words/s), music steady under it (−14.2 LUFS), crew credits and logo at the end.
8. **One graphic language in live action.** White mono type with a block cursor and 1-px boxes; captions cap ≈1.9 % H bottom-left at x ≈6 %.

## Recipe (Hyperframes, 1920×1080)
1. Build the UI as live HTML or high-res screenshots; wrap it in a 3-D card (`perspective:1600px; rotateX(25-30deg) rotateZ(-12 to -16deg)`), black background, vignette `radial-gradient(ellipse at 50% 45%, transparent 40%, #000 85%)`.
2. Depth: duplicate the card, blur the copy 4-6 px and mask the sharp one to a band (`mask-image: linear-gradient(...)`).
3. 9-11 shots of 2.2-10 s. Each = a slow move on the card (`x/y` 3-8 %, `scale 1 → 1.08`, `sine.inOut`). Hard cuts between angles. Order: macro → long track → macro → frontal wide → button macro → typing close-up → result.
4. Animate the task inside shots: caret typing (`steps`, ≈10 chars/s), row stagger 0.08-0.12 s, document lines writing in, diagram lines drawing (`strokeDashoffset` 0.6 s).
5. End: dip or cut to black, tagline `400-600 6vh Inter` centred (fade 0.5-2 s), logo 4.5 s, silent tail 1-2 s.
6. Sound: no VO; ambient pad or electronic bed with one lift at ≈50 %; master −14 LUFS (or −16 for a hushed feel).
7. Customer-film variant: shoot a real team on location, cut on sentence ends, add mono HUD graphics over a soft plate instead of screen captures, credits in the same mono.
