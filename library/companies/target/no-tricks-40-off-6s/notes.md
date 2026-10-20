# No Tricks, Just Up to 40% Off  (Target, 2026-10-06, 6.0 s, 9:16, YouTube Shorts / paid social cutdown)
URL: https://www.youtube.com/shorts/D5NjoNPn0vA
Purpose: ad (6 s promo cutdown for Target Circle Deal Days, Halloween)
One-sentence point: A Halloween pun, a decor product and the sale badge, then "up to 40 % off, October 6-7".

Structure: beats with timestamps (hook, build, turn, payoff, CTA/end card)
- 0.0-1.5 hook: huge white lowercase pun "you / boo / you" on teal with two stacked jack-o-lanterns layered in front of the type; on the beat at 0.375 s the pumpkins light up and "boo" scales ~130 %, settling by 0.75 s.
- 1.5-3.1 product: skeleton waving next to a 3-pumpkin stack on teal steps; red bullseye rings behind it and a "circle deal days" disc badge top-right.
- 3.1-4.75 event lockup: hard cut to full-frame red bullseye rings; "circle deal days is here!" disc zooms in from ~50 % to 100 % in 0.12 s.
- 4.75-6.0 offer: the disc does a coin-flip (Y-rotation) to "up to 40% off deals for members" + small date disc "october 6-7" top-right. Ends on the offer.

Cut rhythm: shots, ASL, median, ASL per quarter, longest/shortest, where it is densest
- 3 shots (1.5 / 1.67 / 2.87 s), ASL 2.0 s; plus 1 graphic coin-flip at 4.75 s = 4 visual beats in 6 s, one every ~1.5 s.

Typography: typeface (or closest free match), weight, case, size as % of frame height, tracking, placement, words per card, hold time, animation in/out
- Target brand sans (Helvetica Neue Bold-like), lowercase, tight tracking.
- Pun: "you" x-height 6.7 % H, "boo" 7.3 % H, big "YOU" 14.6 % H, stacked at 12-55 % H, right-aligned stagger; product overlaps the last word (depth).
- Offer disc diameter ~47 % H (83 % W), "40" cap ~14 % H, Target red #CC0000 on white; date disc ~17 % H top-right.
- Max 4 lines of text, all centred above 75 % H.

Colour/grade: palette, contrast, grain, letterbox
- Two-colour system: teal (#3BB5B0-like) for the seasonal part, Target red for the brand/offer part. Glossy 3D/CG product renders, no grain.

Camera/shots: macro, product on black/white, people, handheld, drone, screen recordings, 3D renders; moves
- CG/studio product renders on seamless colour; no people.

Transitions: hard cut / match cut / morph / mask / whip / dissolve, and how often
- 2 hard cuts + 1 coin-flip graphic transition + 1 scale-in.

Sound: music style, voice yes/no, SFX density, drop-outs, biggest hit, loudness
- Music only, hit on the pumpkin light-up; no VO. Integrated -24.0 LUFS (quiet; a cutdown designed to work muted).

What makes it premium (3-5 bullets)
- Classic "trailer house" cutdown math: 3 beats of ~1.5-2 s, one message each (hook pun / product / offer).
- The brand mark (bullseye rings) is the transition and the background, so it is branded even with sound off.
- Huge type, few words, readable in 0.5 s.
- Seasonal colour (teal) hands over to brand colour (red) at the halfway point.

Recipe: how to recreate the look with real footage + HTML/GSAP (Hyperframes), concrete values
- 1080x1920, 6.0 s: 0-1.5 pun over product, 1.5-3.1 product hero + badge, 3.1-4.75 brand lockup, 4.75-6.0 offer + date.
- Pun: `font: 700 lowercase "Helvetica Neue"; letter-spacing:-0.03em; color:#fff`; sizes 150 / 165 / 330 px; product PNG on a higher z-index than the last word. Beat pulse: `tl.to(boo,{scale:1.3,duration:0.12,ease:"power2.out"},0.375).to(boo,{scale:1,duration:0.25},0.5)`.
- Rings: 7 concentric SVG circles in #CC0000 / #E3182D / #A0000F, `scale 0.6 -> 1.1` over the shot.
- Offer disc 900 px white circle, `rotationY 0 -> 90` (0.12 s), swap text, `90 -> 0` (0.12 s). Date disc 320 px top-right at (920,300).
