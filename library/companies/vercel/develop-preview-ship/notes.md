# Develop. Preview. Ship.  (Vercel, 2021-02-22, 41.8 s, 16:9, YouTube / homepage)
URL: https://www.youtube.com/watch?v=Kas0jIob5QQ
Purpose: product explainer / brand film (platform workflow in four chapters)
One-sentence point: Vercel covers the whole loop: you develop, preview with your team, ship worldwide and keep improving.

Structure: beats with timestamps (by eye; one continuous animation)
- 0.0-1.9 logo mark on black, in silence.
- 1.9-5.5 social proof: tiny tracked caps line ("trusted by" type) over a row of ≈8 customer logos in white, fading up one by one.
- 5.5-10.8 chapter 1 "Develop" (blue): numbered dot + gradient word, under it a code editor and a browser preview.
- 10.8-12.0 a thin vertical line travels down from the dot to the next chapter (the connective device).
- 12.0-20.6 chapter 2 "Preview" (magenta): a deploy log, then comment bubbles stack up like a chat.
- 20.6-22.0 line travel.
- 22.0-28.0 chapter 3 "Ship" (orange): a deployment list, then a dark globe with red points.
- 28.0-29.5 line travel.
- 29.5-34.0 chapter 4 "Iterate" (green): a performance score ring counts 94 → 96 → 100.
- 34.0-36.0 black. 36.0-38.5 URL card. 40.0-41.8 logo mark.

Cut rhythm (verified)
- Mean luma 0.013 (near black). Both detectors 0 cuts; the film is one continuous animation with wipes and fades. By eye ≈10 beats, ≈4.2 s each; chapters 4.5-8.6 s.
- Measured: 1 shot, 41.8 s.

Typography
- Chapter words: bold geometric sans, cap ≈6-7 % H, centred at y ≈27 %, filled with a two-stop gradient per chapter (cyan-blue ≈#00a3ff→#0070f3, magenta ≈#ff0080→#7928ca, orange ≈#ff4d4d→#f9cb28, green ≈#50e3c2→#00c853 by eye). Number in a matching dot (≈5 % H) above the word.
- Social-proof line: tiny caps, tracking ≈0.3 em, cap ≈1 % H.
- URL card: white bold ≈3.5 % H, centred.
- Closest free font: Inter Bold (the brand later moved to Geist; Geist Bold also fits).

Colour/grade
- Pure black #000 background; white UI line art; one gradient colour per chapter, used for the dot, the word and the UI highlights in that chapter.

Camera/shots
- Flat 2-D motion graphics; simplified UI drawings (code, browser, chat, globe, score ring). No 3-D camera, no people.

Transitions
- A line that draws downward links chapters (a vertical "timeline" metaphor); fades and scale-ins inside chapters. No hard cuts.

Sound
- Voice-over narrator from 1.6 s to 36.7 s: ≈102 words in 35 s (≈2.9 words/s), one sentence per chapter beat (speech detection only, not transcribed).
- Light electronic bed with pops on element entrances (hits +21 to +35 dB at 2.3, 6.1, 11.1, 34.9 s).
- Integrated −27.8 LUFS (very quiet master; true peak −9.4 dBTP). Silence 0-1.85 s and under the final logo.

What makes it premium
- The product's own name is the script: three verbs become three chapters plus one bonus.
- One colour per chapter, one connecting line, black everywhere else.
- Social proof before the product, in 3.5 s, silently small.

Recipe (Hyperframes, 1920×1080, 40 s)
- `background:#000`; 4 chapters × 5-8 s, each: dot `48px` circle with the number, word `800 7vh Inter` with `background:linear-gradient(90deg,A,B); -webkit-background-clip:text; color:transparent`, at `top:22%`; content panel `top:38%-88%`.
- Between chapters a 1 px line `scaleY 0 → 1` from the dot downward (0.8 s `power2.in`), then the next dot pops (`back.out(2)` 0.3 s).
- Score ring: SVG circle `strokeDashoffset` + counter tween 94 → 100 over 3 s.
- VO at ≈2.9 words/s, one sentence per beat; master louder than the original (−16 LUFS for web).
