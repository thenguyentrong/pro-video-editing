# The Beginning of Your Tomorrow  (Boston Dynamics, 2026-01-05, 2:04 incl. ~13 s logo/black tail, 16:9, YouTube @BostonDynamics)
URL: https://www.youtube.com/watch?v=sd8ivhpjI6g
Purpose: brand film (company story -> launch of product Atlas)
One-sentence point: From children's drawings and 30 years of legged-robot research to robots at work today, Atlas is "not the end of our journey, but the beginning of your tomorrow".

## Structure (cut list + English captions)
- 0.0-11 dream: top shot of kids drawing a sun (0-2 s), children's faces, kids' robot drawings and letters to Boston Dynamics (4-8 s), girls in a robotics class. VO (female, warm): "As children, we imagined the promise of tomorrow..."
- 11-31 history: archive in small windows on black (MIT Leg Lab 1980s, ~25-35 % frame width, B&W and faded colour, original "© The Leg Laboratory" watermarks kept), the old hopping robot in the BD museum (13-16 s), nature references (ram, cheetah, 19-21 s), early wireframe simulation (22 s), BigDog (25-28 s), first Atlas (29-30 s). "Animals and humans move so easily... we gave them legs, arms, hands."
- 31-40 the viral years: Spot in a kitchen, Atlas parkour and flips - original YouTube clips, letterboxed/windowed, BD watermark visible. "You watched our robots do the impossible. Jump, run, climb and flip."
- 40-57 robots at work: Stretch unloading trucks, Spot inspecting rail, a plant, gauges, a data dashboard on a monitor (49 s), customers in hi-vis. "What if we could automate the hard work... For 5 years, we've been taking robots out of the lab and into the world."
- 57-76 new Atlas: real footage in a warehouse/plant - Atlas standing up from the floor (57-59 s), hand macro, sorting parts, carrying a long part (65-69 s), head ring lights blue (72-75 s). "A superhuman robot built to perform, built to work."
- 76-84 people: HQ drone, engineers, kids' drawing, school class, team cheering at a demo.
- 84-95 future vision (CGI, stylised): Atlas units in a car plant with sparks, robots in a warehouse, offshore rig, nuclear/industrial site, a suburban street with delivery robots (91-95 s). "A world where physical automation expands our horizons... helpers and companions."
- 96-101 real engineers working on Atlas (hands, tools, laptop).
- 102.3-111.6 hero: Atlas walks towards camera in the real lab, head ring turns yellow, slow push-in (9.3 s). "Atlas is not the end of our journey, but the beginning of your tomorrow."
- 111.6-124.5: Boston Dynamics logo on black (3 s), then black.

## Cut rhythm
- 102 shots in 124.5 s. ASL 1.22 s, median 0.92 s. ASL per quarter 1.20 / 0.97 / 0.97 / 2.07 s.
- Longest 12.85 s (logo + black), 9.30 s (102.31, the hero push-in), 4.13 s, 3.59 s. Shortest 0.29 s (89.26, in the CGI vision), 0.38 s.
- 59 % under 1 s, 4 % over 3 s. Densest 30-40 s and 80-100 s (12 cuts per 10 s).
- One 0.88 s black hold at 22.2 s (a separator inside the archive section).

## Typography
- None in the film. Only the original watermarks on archive clips ("© The Leg Laboratory", "Boston Dynamics", "BigDog" labels) - kept on purpose as proof of origin.
- End: "BostonDynamics" wordmark + icon, white on black, small (~2 % height), centred.

## Colour/grade
- Warm, natural documentary grade for new footage; archive left in original quality (low-res, 4:3, faded) inside black windows; CGI vision brighter and more saturated (orange sparks, green suburbia).
- Brand accent: the robot head ring (blue at 72 s, yellow at the end).

## Camera/shots
- Documentary: long lenses on people, macro on hands and grippers, eye-level medium shots of robots at work, drone of HQ.
- Robots: real footage of real deployments (Stretch, Spot, Atlas) + 11 s of clearly CGI "future" shots placed after the real ones.
- Slow motion only in the hero shot (push-in, ~0.5x look - a guess).

## Transitions
- Hard cuts, frame-in-frame (archive windows on black) as the "memory" device, one black hold at 22.2 s, fade to logo.

## Sound
- Female VO + emotional orchestral/piano score building to the end. Integrated -21.9 LUFS, loudest 0.5 s at 100.65 s.
- Short gap 104.95 s (0.25 s) before the final line, then +25.5 dB hit at 105.3 s.

## What makes it credible
- Real history first (archive with original watermarks), then real deployments with customers, then real new Atlas - only after that the CGI vision, which looks clearly stylised (not passed off as real).
- Engineers' hands on the robot (96-101 s) right after the CGI dream pulls the film back to reality.
- The final hero shot is real footage in the real lab.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Order: dream (people) -> archive -> today's real work -> product -> vision (CGI, max ~10 % of runtime) -> real team -> real hero shot.
- Archive windows: `<div class="win">` on black, 30-35vw wide, keep the original aspect and watermark, `gsap.from(win,{autoAlpha:0,duration:.2})`, 0.5-1.0 s each.
- Hero: 8-10 s push-in on the machine walking towards camera (`gsap.fromTo(video,{scale:1},{scale:1.08,duration:9,ease:'none'})`); trigger the brand light on the machine at the VO's last line.
- VO first; montage cuts 0.6-1.0 s on VO phrases; 0.25 s silence before the last line.
