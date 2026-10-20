# Discover the Dyson Airstrait straightener. A new way to straighten.  (Dyson, 2023-05-12, 0:30 film + 5 s end screen, 16:9, YouTube / TV)
URL: https://www.youtube.com/watch?v=3ucfKv2YbU0
Purpose: launch ad (TV-length product spot)
One-sentence point: Airstrait straightens wet hair with focused air instead of hot plates - shown as black-and-white beauty footage with the product in full colour and a CG look inside the airflow.

Structure (VO from whisper in quotes):
- 0.0-5.1 hook: black-and-white shots of a woman with wet curly hair pulling the straightener through it; the device is the only thing in colour (Prussian blue + copper) (frames/t001.5s.jpg, t004.0s.jpg). "Dyson Airstrait dries and straightens simultaneously from wet,"
- 5.1-13.1 one continuous CG move (8 s): x-ray of the device, cyan airflow through the motor and pink/magenta heat flow across the arms (t006.5s, t009.0s), the camera pulls back as hair passes through the two arms (t011.5s). "...not with plates and extreme heat but with high-velocity air... concentrated into powerful focused airflow."
- 13.1-16.2 the product moving through dark hair on a dark set.
- 16.2-24.0 results: macro of smooth straight hair, then three models with straight hair (b/w), each 1.7-2.0 s (t019.0s). "...saving time, maintaining hair strength and creating natural straight styles."
- 24.0-27.0 end card 1: light grey gradient, product vertical on the right, text left "Available in Prussian blue and rich copper" + "dyson airstrait" (t025.0s).
- 27.0-30.0 end card 2: black, "Only at Dyson.com" + "dyson" (t027.8s).
- 30-35 black YouTube end screen (excluded from stats).

Cut rhythm (0-30 s): 10 shots, ASL 3.00 s, median 2.60 s, quarters 2.5 / 3.75 / 1.5 / 2.5. Longest 8.0 s (CG one-take), shortest 1.72 s. 0 % under 1 s, 30 % over 3 s. Fastest in the results section (1.7-2.0 s per model). Cuts on onset 30 % vs 33 % chance = cut to the VO, not the beat.

Typography: end cards only. Dyson sans (geometric-humanist, sentence case; free match Lexend / Outfit), left-aligned at x 15 %, 2 lines, line box 6.9 % of frame height (cap height ~4.5 %), line pitch ~9 %; on card 2 the second line ("Dyson.com") is a heavier weight than the first ("Only at"). Wordmark "dyson" ~5.8 % high at y ~67-72 %, model name in a light grey next to it. Product vertical at x ~70-78 %. Two cards of 3 s each, light then dark.

Colour/grade: selective colour. Live action is fully desaturated to black-and-white (median saturation 3 %) while the product keeps its Prussian blue and copper (p90 saturation 51 % comes from the product and the CG). Grey seamless backdrops, soft beauty light. Median luma 86, contrast p95-p5 146. The CG section goes cyan + magenta on black.

Camera/shots: beauty close-ups (hands, hair, device), side profile medium shots, three model portraits waist-up; CG x-ray of the airflow; a macro of hair texture. Slow push-ins, locked portraits.

Transitions: hard cuts; inside the CG shot the camera moves from inside the device to outside without a cut.

Sound: female VO from 0.1 s to 23 s, two long sentences (13 s + 9 s), nearly wall-to-wall; soft music bed underneath (onsets 1.66/s, level flat -20 to -22 LUFS-M); music ends at 28-29 s. Integrated -22.8 LUFS = broadcast master.

What makes it premium:
- Selective colour: b/w world, coloured product - the eye can only go to the product.
- The invisible mechanism (air) made visible with CG colour flows.
- Fashion-beauty casting and grey seamless instead of a bathroom.
- The end card names the colour like a fashion item ("Prussian blue and rich copper").

Recipe (real footage + HTML/GSAP):
1. Shoot on grey seamless; grade live action to b/w but key the product colour back (in Resolve: qualifier on the product hue, desaturate the rest). In HTML: two stacked videos, bottom `filter: grayscale(1) contrast(1.05)`, top = same video with a product mask (`mask-image` from a rotoscoped PNG sequence or a luma key).
2. Mechanism shot: 6-8 s on dark; draw airflow with SVG paths (`stroke: #3fd8ff`, 2 px, `stroke-dasharray` animated with GSAP `strokeDashoffset` loop, `mix-blend-mode: screen`, 8 px blur glow layer under it).
3. Results: 3 portraits x 1.8 s.
4. End cards: 2 x 3 s, light grey `linear-gradient(#cfd2d4,#a9adb0)` then black; text left at 15 % x, 4.5 % cap height, line 2 heavier weight; wordmark at 67 % height; product cut-out at 70-78 % x.
5. VO wall-to-wall, two long sentences; -23 LUFS for TV, -14 for social.
