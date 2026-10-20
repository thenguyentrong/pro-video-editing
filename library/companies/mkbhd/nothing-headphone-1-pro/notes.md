# Nothing Headphone 1 Pro: They Copied the Wrong Thing!  (MKBHD / Marques Brownlee, 2026-09-29, 14:20 full / first 300 s analysed, 2:1 frame inside 16:9 player, YouTube)
URL: https://www.youtube.com/watch?v=rayrrXot17M
Purpose: tech review (single product vs its category)
One-sentence point: a design-led brand enters the top price tier of noise-cancelling headphones, so it gets tested against the best, and it gets many things right but copies one wrong thing.

Data note: first 300 s analysed (trimmed with ffmpeg after download). Frame 854x428 = 2:1. One cut added at 2.4 s (end of the logo sting). Both detectors agree otherwise; the 38.9 s talking head at 201.4 s was checked on the sheet and shows one framing, but jump cuts with identical framing cannot be seen at 1 frame/s.

## First 30 s (hook)
- 0.0–2.4 channel logo sting (same 2.4 s red 3D logo, dip to black 1.5–2.4 s). Loudest 0.5 s of the film at 0.85 s.
- 2.4 iris reveal straight onto the host, talking to camera in a dark studio (mesh panels, purple-pink light, window glow). Voice starts at 2.48 s; the brand and the category are named in the first sentence.
- 11.5–22.9 rival montage while he lists the market leaders: him wearing a rival pair in another set, product shots of each rival (pink, white, silver) at 1.3–2.7 s each. 5 cuts in 10–20 s = the densest 10 s of the 300 s.
- 22.9–26.7 rival line-up / product table shot.
- 26.7–41.1 back to the host for 14.4 s, product in hand; product name and price stated at ≈27.7–32 s (the stakes: "most expensive they have made").
- Cuts in 0–30 s: 8 (2.4, 11.5, 14.2, 15.9, 17.9, 19.1, 22.9, 26.7). No title card, no sponsor.
- Sound: voice dry from 2.5 s; light music only under the rival montage.

## Structure (first 300 s)
- 0–41 sting, thesis to camera, rival montage, price/stakes.
- 41–48 overhead hands-on of the product on a desk; 48–52 product hung on a red chair in the office; 52–56 outdoor stairwell, wearing them.
- 56–68 talking head; 68–75 case on an orange surface; 75–106 macro details (cups, hinge, buttons), product on desk.
- 107–113 product on red fabric; 113–121 outdoor brick wall, wearing.
- 121–131 weighed on a scale with a spec card listing five rival weights.
- 131–163 talking head with the headphones on, close wearing shots; 164–180 phone app screens next to the product.
- 180–201 macro; 201–240 one 38.9 s talking head (the main verdict on sound); 240–260 macro on a cutting mat; 260–282 talking head 22.0 s; 282–300 product on a red sofa, hands.

## Cut rhythm
43 shots in 300 s, ASL 6.98 s, median 6.11 s. 0 % under 1 s, 86 % over 3 s, 8.6 shots/min. ASL by quarter 4.69 / 5.77 / 8.33 / 9.38 s (gets slower as it moves from setup to verdict). Longest 38.9 s (201.4 s), 22.0 s (260.9 s), 14.4 s (26.7 s). Shortest 1.27 s (17.9 s, rival montage). Cuts per 10 s 0–5, typical 1–2. Cuts on onsets at chance (62 % vs 61 %).

## Typography
- Spec card (121.5–131.5 s, visible ≈5 s): rounded white box (radius ≈2 % H), dark text, neutral sans like SF Pro / Inter regular, 5 lines "Product: weight", text cap height ≈3.5 % H, line pitch ≈6.5 % H, box at x ≈4–34 % W, y ≈63–92 % H, lower left, beside the object being weighed. Closest free: Inter 400.
- No lower thirds, no chapter cards, no captions in the first 300 s.

## Colour / grade
Neutral and clean; product on light grey desks with orange-accent keyboard, or on saturated single-colour backdrops (red fabric, orange). Studio talking head: dark set with purple-pink key colour and cool window highlights. No grain.

## Camera / shots
Locked centred talking head (two sets in this film: dark studio, plus a bright office for rival shots). Overhead hands-on, macro with very shallow focus, wearing shots outdoors (stairwell, brick wall), product as a still life on colour. Phone screen shown in hand next to the product.

## Transitions
Hard cuts; iris reveal out of the sting only.

## Sound
Integrated −19.6 LUFS, LRA 4.1 LU, true peak −0.2 dBTP. Voice median −26.6 dBFS (50 ms RMS), p10 −54.5 dBFS → pauses ≈28 dB under the voice, no bed under talking; 16.4 % of 50 ms windows below −45 dBFS. One drop-out ≥0.8 s (279.6 s). Music under b-roll stretches only.

## What makes it premium
- The thesis is spoken in the first 10 s by the host himself, then proven with the whole category on screen.
- Every claim about the object has a physical test: scale with a comparison card, macro of the part, wearing it outside.
- Long talking-head holds (22–39 s) for the verdict: trust comes from the person, not from editing.
- One small, clean info card instead of motion graphics.

## Recipe (real footage + HTML/GSAP)
- 2.4 s logo sting → iris onto the host; first line names product + category before 5 s.
- Rival montage under the list: 5–6 product shots of 1.3–2.7 s, cut on each name.
- Spec card: `.spec{position:absolute;left:4%;bottom:8%;background:rgba(255,255,255,.94);border-radius:2vh;padding:1.6vh 2.2vh;font:400 4.6vh/1.4 Inter;color:#1d1d1f}`; `gsap.from('.spec',{autoAlpha:0,y:12,duration:.3,ease:'power2.out'})`, hold ≈5 s, hard off with the cut.
- Pace: start at ASL ≈4.7 s, end at ≈9.4 s; at least one 20–40 s talking-head verdict.
