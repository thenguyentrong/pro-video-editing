# Robots for the Solar Energy Revolution: The RPD 35 from Built Robotics  (Built Robotics, 2023-03-14, 3:04, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=8Na6NF11iPc
Purpose: product launch / explainer with staff interviews (autonomous solar pile driver)
One-sentence point: The RPD 35 is an excavator turned into an autonomous pile driver that carries its own piles and places them by GPS, so solar farms get built three times faster and safer.

## Structure
- 0.0-9.4 (0-5 %) cold open: a worker in hard hat and hi-vis at a laptop on a truck tailgate, the robot behind; she says a short "alright" (9.4 s single shot).
- 9.4-24.5 (5-13 %) product burst: top-down drone of the machine over a solar field with piles, piles in rows top-down, the arm lifting a pile, the black-and-yellow Exosystem box, a "STOP ROBOT" button, the hammer on a pile; first interview line names the product (fastest part, 8 cuts in 10 s).
- 24.5-32.6 (13-18 %) why: solar field aerial with an animated line chart "The Growth of US Solar Capacity (GW)" (yellow solid line to today, dotted projection to 2035).
- 32.6-56.5 (18-31 %) the problem: two interviewees with lower-thirds (Head of Field Operations, an engineer), whiteboard and robot-lab scenes, a CAD model on a laptop, a manual crew distributing piles on a dirt site. Piles are heavy and the task repeats tens of thousands of times.
- 56.5-98.3 (31-53 %) the product working: cab with no driver, POV through the cab, hammer close-ups, a worker loading piles, "RPD 35 ROBOTIC PILE DRIVER" lettering on the sled, machine wide on site, top-down drone of the field with pile rows; claims in interview: carries up to 200 piles (≈30,000 lb); a manual crew sets about 100 piles a day, the robot over 300.
- 98.3-120.0 (53-65 %) CGI exploded view: on black, the excavator with the four added parts highlighted as blue wireframe holograms (sled, baskets, hammer, Exosystem box), one continuous 21.7 s camera move, while the field-ops lead names the parts.
- 120.0-142.4 (65-77 %) sequence and accuracy: piles stacked in the baskets (macro dolly), the machine placing a pile, an operator with a tablet, sub-centimeter accuracy claim.
- 142.4-156.5 (77-85 %) safety: a site engineer in a white hard hat to camera (14.1 s, one shot) states 18,000+ autonomous hours and zero robot-related incidents; the eight safety layers pop in one by one as a numbered list on the right.
- 156.5-173.9 (85-95 %) future: trenching history, worker on a laptop, hammer close-up, the opening worker again, final interview line about automation being key.
- 173.9-183.8 (95-100 %) logo: white "B" mark on black, 9.9 s with music tail.

## Cut rhythm
- 57 shots in 183.8 s. ASL 3.22 s, median 2.17 s, 5 % under 1 s, 28 % over 3 s, 18.6 shots/min.
- ASL per quarter 2.55 / 2.00 / 4.60 / 5.11 s: brisk first half (b-roll over interviews, 4-5 cuts per 10 s; 8 in the product burst), slow second half (CGI 21.7 s, safety talking head 14.1 s, logo 9.9 s).
- Shortest 0.83-0.96 s (product burst at 15-18 s). Adaptive detector found 2 extra "cuts" inside the chart animation (not real).

## Typography
- Lower third: white panel with a diagonal right edge, bottom-left, ≈32 % of frame width and ≈27 % of height; name bold ≈3.3 % H, black; role ≈2.6 % H medium, dark grey; company ≈2.6 % H light grey. Geometric grotesk (closest free: Inter / Manrope). Shown ≈4-5 s.
- Persistent bug: white "B" mark bottom-right, ≈8 % H, ≈80 % opacity, all film long.
- Chart: title white bold ≈4 % H top-left, axes labels ≈2.6 %, thin grid lines, one yellow line (brand yellow ≈#F5D90A) solid for history, dotted for forecast; drawn left to right over 6-7 s on a darkened aerial.
- Safety list: yellow circle with black number ≈7 % H, label below in white semibold ≈3.8 % H, centred in the empty right half next to the speaker; items appear one per spoken item and replace each other.
- Product name only as physical lettering on the machine ("RPD 35 ROBOTIC PILE DRIVER").

## Colour/grade
- Clean, natural, slightly warm daylight; deep blacks for the CGI; the yellow/black machine and yellow graphics are the brand palette. Interviews in a bright workshop with red tool cabinets behind.

## Camera/shots
- Two staff interviews (lab/workshop, medium close-up, shallow depth) + one site interview in PPE. Cutaways from all to site b-roll.
- Drone top-downs of the solar field and pile grid; cab POV with no driver; macro dolly on piles; real software only as a CAD view on a laptop.
- CGI only in one separated block (black background, clearly a render).
- No speed labels; the work is shown at apparent real time in 2-4 s shots.

## Transitions
- Hard cuts. The CGI enters and leaves by hard cut on black.

## Sound
- Interviews over a light electronic pop track; pile-driving hits audible in b-roll. Integrated -14.3 LUFS, range 5.6 LU, true peak +0.4 dBTP. No drop-outs; strongest hit at 24.9 s (chart reveal); hits on each safety list item (143-160 s). 1.4 s silence at the end.

## What makes it premium / credible
- Named staff with titles, PPE on site, and numbers spoken by them (200 piles, 100 vs 300 per day, 18,000 hours, zero incidents).
- One clean data chart for the market "why".
- CGI kept in its own block to explain parts; real footage for all work.
- Safety list as the late, calm, longest talking shot.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Interviews: 2-3 named people, 10-20 s blocks covered by 2-4 s b-roll; one uncut 12-15 s site talking head for the safety claim.
- Lower third: `<div class="lt">` white, `clip-path:polygon(0 0,88% 0,100% 100%,0 100%)`, `left:0; bottom:0; width:32vw; height:27vh; padding:5vh 4vw`; name `font:700 3.3vh Inter`, role `500 2.6vh #555`; in `gsap.from(lt,{xPercent:-100,duration:.5,ease:'power3.out'})`, hold 4.5 s.
- Numbered list: circle `width:7vh;height:7vh;border-radius:50%;background:#F5D90A;font:700 3.6vh Inter;color:#000`; label `font:600 3.8vh Inter;color:#fff;text-align:center`; each item `gsap.from(item,{y:20,opacity:0,duration:.3})` on the spoken word.
- Chart: SVG path, `stroke:#F5D90A; stroke-width:.6vh`, draw 5 s with `stroke-dashoffset`; forecast part `stroke-dasharray:0 1.4vh; stroke-linecap:round`.
- Bug: logo mark bottom-right, `height:8vh; right:4vw; bottom:5vh; opacity:.8`.
- End: logo mark on black 4-6 s (this film holds 10 s, too long for social).
