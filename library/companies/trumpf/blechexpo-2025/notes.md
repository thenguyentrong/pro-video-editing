# TRUMPF @ Blechexpo 2025  (TRUMPF, 2025-09-11, 0:31, 16:9, YouTube @TRUMPFtube)
URL: https://www.youtube.com/watch?v=o_cFeNw1wXw
Purpose: trade-fair invitation teaser (ad, 126k views - the channel's most-watched recent upload), music only
One-sentence point: Come to the TRUMPF stand at Blechexpo (21-24 October, Stuttgart) to discover, produce, meet and experience - "you win".

## Structure
- 0-3.3 blurred blue machine detail; "DISCOVER" in huge outline caps.
- 3.3-6.5 "our latest / bending technologies" (white bold + one outline word) over a machine, a diagonal blue wipe crosses the frame.
- 6.5-9 "PRODUCE" outline caps over a long factory aisle; "fully automated / and smart".
- 9-13.3 "MEET" outline caps over stand visitors; "our experts" (the second word in bold italic).
- 13.3-18.7 "EXPERIENCE" outline caps; "innovation"; "and be part of it" with a red laser line.
- 18.7-21 "Come and see us at / Blechexpo 2025" over the crowded stand.
- 21-25 date card on blue: "21-24 October / in Stuttgart", then "Get your tickets now! / www.trumpf.com".
- 25-28.5 "you win" mark on blue, blur in and out.
- 28.5-31.4 TRUMPF logo on white.

## Cut rhythm
- Adaptive detector: 8 shots in 31.4 s, ASL 3.93 s, median 3.24 s, 0 % < 1 s, 15.3 shots/min. Longest 12.7 s (18.7 s: the end sequence of cards on blue), shortest 1.0 s.
- Most changes are blur/wipe transitions, not hard cuts: one word-pair per ≈2-3 s; the image barely matters, the words carry the rhythm.

## Typography
- TRUMPF face (closest free: Noto Sans / Open Sans), white.
- Verb: ALL CAPS outline (1-2 px stroke, no fill) ≈18 % H, full width, centred, letter-spacing ≈.02em, one per section (DISCOVER, PRODUCE, MEET, EXPERIENCE).
- Phrase: lowercase bold ≈8 % H, centred, two lines; one word may switch to outline or bold italic for contrast.
- Date card: regular ≈4.5 % H, two lines, centred on blue; URL line ≈2.5 %.
- "you win" mark: bold lowercase ≈10 % H, stacked.

## Colour/grade
- Every shot is pushed to TRUMPF electric blue (#0028FF-ish): a blue gradient overlay at ≈50-70 % plus diagonal solid-blue panels; highlights stay white. One red laser line as the only other colour.

## Camera/shots
- Real stand and factory footage, mostly blurred or heavily tinted: machine details, aisles, visitors, experts at screens, the crowded stand.

## Transitions
- Diagonal blue panel wipes (≈35° edge), blur dissolves between words, blur in/out on the "you win" mark, fade to white.

## Sound
- Music only (no speech detected), bright electronic pop. Integrated -19.2 LUFS, LRA 5.3 LU, true peak -5.3 dBTP. Changes land on onsets (57 % vs 35 % chance). Rises +15-20 dB at 8.4, 12.4, 20.4, 22.4 s.

## What makes it work
- Four verbs give a 30 s ad a clear 4-beat structure.
- One brand colour over all footage makes mixed event footage look designed.
- Date, place and ticket call to action are on screen for ≈4 s each.

## Recipe (real footage + HTML/GSAP)
- Tint: footage + `<div class="tint" style="background:linear-gradient(120deg,rgba(0,40,255,.75),rgba(0,40,255,.3))">`.
- Outline verb: `font:700 18vh 'Noto Sans'; color:transparent; -webkit-text-stroke:1.5px #fff; text-transform:uppercase`; `gsap.fromTo(v,{scale:1.08,autoAlpha:0},{scale:1,autoAlpha:1,duration:.5})`, hold 1 s, then the phrase `700 8vh` replaces it.
- Diagonal wipe: a blue `div` with `clip-path:polygon(30% 0,100% 0,100% 100%,0 100%)` moving `xPercent:100 → -100` in 0.6 s.
- End: date card 3 s, CTA 2 s, mark 3 s, logo 3 s.
