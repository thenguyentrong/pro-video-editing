# AGIBOT - style

Examples (official @AGIBOT uploads):
| Example | Date | Length | Shots | ASL | Median | Sub-style |
|---|---|---|---|---|---|---|
| [a3-mask-is-off](a3-mask-is-off/notes.md) | 2026-08 | 2:34 | 103 | 1.49 s | 1.16 s | humanoid launch as a kung-fu short film, letterboxed |
| [d1-max-all-terrain](d1-max-all-terrain/notes.md) | 2026-03 | 2:10 | 106 (≈99 without flash frames) | 1.23 s | 0.98 s | quadruped spec montage, trailer energy |
| [precision-manufacturing-deployment](precision-manufacturing-deployment/notes.md) | 2026-04 | 2:10 | 33 | 3.93 s | 2.60 s | B2B deployment: real result → simulation → RL → bullets |
| [a3-ultra-shangri-la](a3-ultra-shangri-la/notes.md) | 2026-10 | 1:52 | 36 | 3.10 s | 2.70 s | customer testimonial at a named hotel |

## Sub-styles
1. **Cinematic launch:** a genre short film (wuxia) with actors, sets, letterbox ≈2.4:1, teal/amber grade, fight cutting at ASL 1.5 s, subtitles; the robot is costumed and played as a character. One permanent label "Real footage. No CGI, no AI." (≈2.5 % H, bottom-right).
2. **Spec montage (quadruped):** one number per block ("8 m/s", "IP67", "80cm", "45°", "30kg", "-20°C to 55°C", "5 hour / 30 km"), 0.8-1.4 s shots, FPV chases, flashes and glitch-bar wipes, VFX overlays, trailer drop-out before the logo. ASL 1.2 s.
3. **Deployment case (industrial):** result first in one real 23.9 s take with a named customer line, then "Simulation Reconstruction" / "Simulation Testing" / "AGIBOT G2 Testing" blocks marked by a top-right tag, then feature-bullet cards, then both logos.
4. **Hospitality testimonial:** documentary gimbal at a named hotel, the manager in interview with the robot behind her, the interviewer's question shown as a text card, every line subtitled, scene shots of 2-4 s.

## House rules
- **Everything in English on screen**, even with Chinese speech: burned-in subtitles ≈3.5-4.5 % H in every film with dialogue.
- **Section tags and bullet cards:** top-right tag ≈4.5 % H with a thin brand-blue underline; bullet stacks of three lines ≈4.5 % H with a blue bar on the left; bottom-left keyword tag. Short wipe-ins (≈0.3 s).
- **Spec value + line:** value bold ≈6 % H, explanation ≈3.5 % H, bottom-left; units always written.
- **Customer named in the title and in the frame** ("× Shangri-La", "× LONGCHEER" logo lockup).
- **Brand accents:** cyan/blue (industrial), cyan + purple (quadruped glitch bar), yellow brush lettering for the film IP.
- **Loud masters:** -8.4 to -14.6 LUFS integrated, true peaks above 0 dBTP in all four.
- Channel mix (titles studied): entertainment and events (galas, circus, film festivals, robot games medals) far outnumber proof films.

## How they show a real machine working / keep it credible
- Strong: real customer sites named on screen; one long real result take in the industrial film (23.9 s, then 14.8 s); "Real footage. No CGI, no AI." written for the whole launch film; real guests and staff in the hotel film.
- Weak, and different from US/EU proof films:
  - **No speed labels at all** in the four films studied, although the quadruped film has visible speed-ups/ramps and the fight film is ramped.
  - **Autonomy is a bullet word** ("Autonomous Operation", "Autonomous Navigation", "Autonomous Self-Charging"), never a label on a specific take; teleoperation is never mentioned. The quadruped opening shows a hand with what looks like a handheld controller.
  - **Photoreal simulation next to real footage**: in the industrial film only a 4.5 % H corner tag ("Simulation Testing" vs "AGIBOT G2 Testing") tells them apart.
  - **VFX on real footage** (floor arrows, light tunnels) in the spec montage.
  - Fast cutting (ASL 1.2-1.5 s) in the launch and spec films hides task duration.

## Compared with US/EU makers and with Unitree
- US/EU (BD, Figure, Tesla, ABB, Siemens): one-take proof with small "Autonomous"/"2X" labels, named engineers, restrained grade. AGIBOT: production value of a film studio or a car ad, entertainment framing (kung fu, galas, celebrities), customers as proof, almost no speed/autonomy disclosure.
- Unitree: plainer footage, big honest speed sentences, no people speaking. AGIBOT: interviews, subtitles, named customers, cinematic grade, but no speed sentences.
- Both Chinese makers write "real / not AI / no CGI" on screen; none of the US/EU films studied needed to.

## Recipe (real footage + HTML/GSAP)
1. Pick the lane: brand film (genre story, letterbox, 1.5 s ASL) or proof film (named customer, 15-25 s real takes). Do not mix both in one cut.
2. Customer film: open on the real result take with a caption naming the site (3.5vh), tag top-right `font:500 4.5vh 'Source Sans 3'` + `border-bottom:.6vh solid #2b8cff`.
3. Tag every block with what it is: "Real footage · 1x", "Real footage · 2x", "Simulation". Make the simulation tag a different colour (e.g. amber) so it cannot be confused.
4. Spec card: value `700 6vh`, line `600 3.5vh`, bottom-left `left:7vw; bottom:20vh`; one card per 3-6 s block; glitch-bar wipe = three coloured divs (`#29c6f0`, `#fff`, `#7a3cff`) sliding `x:-100%→100%` in 0.3 s.
5. Testimonial: put the question on screen as an outlined card (3vh), subtitle every line (4.5vh), keep the robot in the background of the interview shot.
6. Master at -14 LUFS / -1 dBTP; keep a ≈1 s drop-out before the logo hit if you use trailer music.
