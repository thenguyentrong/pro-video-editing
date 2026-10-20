# Gen 7 - The Destination Platform for Physical AI  (Universal Robots, 2026-09-21, 1:32, 16:9, YouTube @UniversalRobotsVideo)
URL: https://www.youtube.com/watch?v=7SDlVddZ30U
Purpose: product launch teaser (new cobot generation, 100 % CGI, music only, kinetic type)
One-sentence point: UR's 7th generation (arm, controller, teach pendant) is ready for AI: more sensors, more compute, more connectivity, faster programming.

## Structure
- 0-3 dark reveal: macro of a joint, blue status ring lights up.
- 3-11.6 context: whole arm + controller on deep blue; small text block left builds line by line (built on 100,000 deployments and 20 years, 7th generation); UR logo bottom-left; "Gen 7" huge (≈20 % H), then "Gen 7 / is AI-ready".
- 11.6-25.5 feature 1: big statement "Plug in / Cameras and sensors", then the tool flange with thin leader-line callouts (≈1.5 % text in blue pills: "Safety rated inputs", "M8 I/O connectivity"); title top-left "g-Series robot arm" (white + light blue).
- 22-25.5 statement "Faster teaching and programming from the tool" typed word by word.
- 25.5-35 feature 2: SP7 Smart Panel on the tool, callouts for buttons; "Connect more and simplify integration".
- 37-52 feature 3: CB7 controller, macro pass over ports, callouts ("3x 1 Gb Ethernet ports"...), "Compatible with g-Series, e-Series and UR Series robots", "Flexible configuration options".
- 50-66 feature 4: "Program faster with greater ..." then the TP7 Core teach pendant with callouts (multi-gesture touchscreen, virtual joystick, ergonomic design).
- 66-88 summary chain of short statements over hero shots: "Less cabling. / More EOATs. / Higher compute. / More connectivity. / Ready for AI-enabled automation. / Universal Robots Gen 7. / Industrial Automation. Built for AI."
- 88-92 UR logo centred on blue.

## Cut rhythm
- Dark film: the default scene detector found only 6 cuts; the adaptive detector finds 36 (37 shots), a few of which are big type changes on the same background. With adaptive: ASL 2.49 s, median 1.72 s, 38 % < 1 s, 30 % > 3 s, 24.1 shots/min; ASL per quarter 2.6 / 1.8 / 3.3 / 2.1 s.
- Longest 13.3 s (52.7 s, teach-pendant orbit), 8.3 s, 8.2 s. Shortest 0.28 s (type change).
- 3-6 changes per 10 s: product orbits of 5-13 s alternate with fast type beats of 0.3-1 s.

## Typography
- Statements: heavy condensed grotesk (closest free: Anton or Oswald 700), sentence case, 3-4 lines, ≈14 % H per line (cap ≈11 %), left-aligned at x ≈18-20 %, tight leading; two colours per statement: UR light blue (#5FA8D8-ish) for the first words, white for the last words. Words appear one by one (≈0.15-0.3 s each); hyphenated breaks allowed ("program- / ming").
- Hero word "Gen 7": same face ≈20 % H, light blue.
- Product titles: regular condensed ≈5 % H top-left ("g-Series" white + "robot arm" light blue).
- Callouts: thin 1 px light-blue leader line with a small circle on the part, ending in a dark-blue pill with text ≈1.8 % H (bold key word + regular rest), e.g. "**Safety rated** inputs".
- Small text block (intro): ≈2.8 % H condensed, white with one bold blue word, 6 short lines.

## Colour/grade
- Deep blue gradient (navy #001a4d to UR blue #0033a0) with faint "+" grid marks; dark grey product with light-blue joint caps; one cyan light ring. No other colours.

## Camera/shots
- 100 % CGI: macro pushes, slow orbits, a 360° pass around the teach pendant; the type cards sit on the empty blue background or beside the product.

## Transitions
- Hard cuts and type-on/type-off on the same background; light sweeps across metal surfaces.

## Sound
- Music only (no speech detected), pulsing electronic. Integrated -19.6 LUFS, LRA 3.0 LU (very compressed), true peak -3.8 dBTP. 0.95 s silence at the start; no drop-outs. Biggest rise +35 dB at 26.25 s (Smart Panel reveal). Changes land on onsets (56 % vs 37 % chance).

## What makes it premium
- One brand colour field for the whole film; product dark grey + light blue only.
- Statements are short, concrete benefits; two-colour words make the key part pop.
- Precise callouts with leader lines touching the real ports.
- Weak as proof: no real cell, no AI demo, no number about compute or speed.

## Recipe (HTML/GSAP)
- Background: `linear-gradient(180deg,#00122e 0%,#00297a 100%)` + faint "+" marks (`opacity:.15`).
- Statement: `<p class="st"><span class="b">Faster teaching and program-ming</span> from the tool</p>`, `font:400 14vh/0.95 Anton; left:18vw`; `.b{color:#5FA8D8}`; split into words, `gsap.from(words,{autoAlpha:0,duration:.01,stagger:.2})`.
- Callout: SVG `<circle r=4>` on the part + 1 px line + pill `background:#0b2c6e; padding:.8vh 1vw; font:400 1.8vh Inter` with `<b>` key word; draw the line `stroke-dashoffset` 0.4 s, then the pill fades in 0.2 s.
- Product shots: if you have no render, film the real product on black with a slow slider and grade the black to navy.
