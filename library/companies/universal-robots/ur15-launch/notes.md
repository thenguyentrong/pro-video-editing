# Meet the all-new UR15 - A sharper, faster, more agile cobot  (Universal Robots, 2025-05-16, 2:58, 16:9, YouTube @UniversalRobotsVideo)
URL: https://www.youtube.com/watch?v=UZpq2Bfqw1s
Purpose: product launch film (new 15 kg cobot; real footage + CGI spec section, VO)
One-sentence point: The UR15 is UR's fastest, most capable cobot so far - optimised, personalised and ready for the future, built on 20 years of cobots.

## Structure
- 0-4.7 logo build: UR mark assembles on teal-grey.
- 4.7-24 heritage: desaturated blue-grey real footage of engineers, labs, welding sparks, earlier cobots, with years in small square tiles (2008 ... 2025) floating over the shots; dark macro of the new arm.
- 24-33 reveal: real/CGI macro passes along the joints; title "UR15" (white, ≈7 % H) next to the arm on a pattern of blue squares and quarter circles.
- 33-81 chapter 1 "Optimized" (≈6 % H word on dark teal): CGI product on light grey with moving blue square/quarter-circle shapes; one spec per shot: "Speed 5 m/s", "Weight 40.7 kg / 89.7 lbs", "Payload 15 kg / 33 lbs", "Footprint Ø 204 mm"; small icon chips ("Costs", "Productivity"); wireframe box shots for certifications (cleanroom, UL 1740, TÜV) and feature chips ("Seamless compliance", "Safer operations", "Faster ROI").
- 81-105 chapter 2 "Personized" (sic, on screen): real footage of a woman operator in a factory with the cobot, hand-guiding the arm, LED ring changing colour, teach-pendant touch screen.
- 105-156 chapter 3 "Futurized": "Powered by PolyScope X" as a layer over real footage, CGI application tiles flowing in a ribbon ("Machine tending", "Palletizing", "Material handling", "Quality inspection"), fleet of arms, people silhouettes, "UR Care" service plans (1-2-3-4 tiles).
- 156-169 hero: dark studio, arm with green light, "The all-new UR15" stacked, operator touches the arm.
- 169-178 end card: UR logo + line on teal, 9 s.

## Cut rhythm
- 41 shots in 178 s (the second detector finds 54; many changes are soft pattern wipes). ASL 4.34 s, median 2.48 s, 10 % < 1 s, 46 % > 3 s, 13.8 shots/min. ASL per quarter 2.6 / 4.5 / 4.1 / 7.4 s.
- Longest 19.5 s (122.6 s, CGI application ribbon), 18.7 s (65.2 s, certification sequence), 13.5 s. Shortest 0.80 s.
- Fastest in the heritage open (7 cuts in 10-20 s); the CGI chapters are long continuous animations.

## Typography
- Geometric sans (closest free: Montserrat / Manrope), white on dark or navy on light.
- Chapter words: 600 weight, sentence case, ≈6 % H, centred-left, typed with a block reveal from a square; hold ≈4 s.
- Spec card: label bold ≈6 % H ("Weight") over value regular ≈6 % ("40.7 kg / 89.7 lbs"), white over the moving blue shapes, beside the arm; metric first, imperial after a slash; hold ≈3 s.
- Feature chips: small rounded rectangles ≈4 % H with an icon + 1-2 words ≈1.8 %, attached to the product.
- Years in square tiles ≈6 % H, translucent white, floating over archive footage.

## Colour/grade
- Heritage: desaturated teal-grey grade. CGI chapters: light grey studio + UR blues (#0d3b66 navy, #3a8dde blue, #a8d1f0 light) in flat square and quarter-circle shapes. Real factory: cool, clean, blue-grey.

## Camera/shots
- Real: handheld/gimbal people shots, macro of hands guiding the arm, LED ring close-up, teach-pendant close-up. CGI: product turntables, macro joints, wireframe boxes, a flowing ribbon of application cards. Real and CGI alternate by chapter, rarely in one shot (the PolyScope layer over real footage is the exception).

## Transitions
- Shape wipes: blue squares and quarter circles slide across and reveal the next shot (the soft-transition candidates at 1.2, 21.7, 33.7 s); hard cuts in real footage; fade to the end card.

## Sound
- Female VO ≈169 s (≈266 words, slow ≈1.6 words/s, many pauses) over a warm, steady electronic track. Integrated -13.4 LUFS, LRA 2.8 LU (very compressed), true peak -2.2 dBTP. No drop-outs; 1.25 s silence only at the very end. Rises +16-19 dB on chapter changes (65.1, 104.6 s).

## What makes it premium
- A graphic system (squares + quarter circles in brand blues) that also does the transitions.
- Chapter words structure a long spec list into three ideas.
- Each spec sits alone with metric + imperial units.
- Weak as proof: speed "5 m/s" is never shown on real footage; no customer, no long real take.

## Recipe (real footage + HTML/GSAP)
- Shape wipe: 6-8 `div`s (squares and `border-radius:0 0 0 100%` quarter circles) in `#0d3b66 #3a8dde #a8d1f0`, `gsap.from(shapes,{xPercent:-120,duration:.6,stagger:.05,ease:'power3.inOut'})`, next shot revealed under them.
- Spec: `<b>Weight</b><span>40.7 kg / 89.7 lbs</span>`, `b{font:700 6vh Montserrat}`, `span{font:400 6vh Montserrat}`, white, left of the product, fade + y 10, 0.4 s.
- Chapter word: dark teal card `#0b2f3a`, word `600 6vh Montserrat`, revealed by a square sliding off it (0.5 s).
- Use real footage for people and hands; keep CGI for specs; put a "1x" label on any real speed claim.
