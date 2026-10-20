# INTRODUCING Nuron - Hilti's all-new 22 Volt cordless power tool platform  (Hilti Group, 2022-01-12, 2:32, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=nBmQa89O2S0
Purpose: product / platform launch film (music + kinetic type, no voice-over)
One-sentence point: One 22 V battery platform gives cordless tools the power of corded, gas and high-voltage tools, plus data services, "without compromise".

## Structure
- 0.0-11.3 (0-7 %) hook: sunrise time-lapse of tower cranes over a city, title card "THE TIME FOR / COMPROMISE / IS OVER" (left, over the skyline), fast close-ups of gloved hands slamming a battery into tools on site.
- 11.3-14.9 (7-10 %) name: "NURON" logo over a red tool close-up (the O is a battery symbol).
- 14.9-23.4 (10-15 %) promise: "22 VOLT CORDLESS PLATFORM THAT BRINGS..." held over three shots (top-left, 4.5 s).
- 23.4-65.1 (15-43 %) claim blocks, one keyword per block, 2-6 shots each: PERFORMANCE without compromise / of corded / of gas / of 36 volt / of 72 volt; red chevron wipe at ≈45-46 s; RUN TIME without compromise; IMPROVED ERGONOMICS; MORE SPEED; COMPATIBILITY.
- 65.1-83.9 (43-55 %) CGI: "ONE PLATFORM" - rendered batteries on a white sweep, camera glides along a row of packs, then a pull-out to a grid of the whole tool range "FOR ALL YOUR CORDLESS TOOLS" (18.8 s, the longest stretch, counted as one shot).
- 83.9-100.1 (55-66 %) safety block, back on site: HEALTH AND SAFETY, DUST REMOVAL SYSTEMS, ACTIVE VIBRATION REDUCTION, ACTIVE TORQUE CONTROL, TETHERING.
- 100.1-127.9 (66-84 %) data services: battery on a charger "TRANSMIT TOOL DATA" with white line icons (Usage, Utilization, Location) popping in on the right, an animated cloud with graphs, an office manager at a laptop with floating dashboard cards and cost numbers, a phone mock-up over a tool crib "MINIMIZE DOWNTIME WITH PROACTIVE SERVICES", "OPTIMIZE YOUR TOOL CRIB", "DATA-DRIVEN SERVICES".
- 127.9-141.1 (84-93 %) recap: sunset crane time-lapse with red chevrons, NURON logo over a night city, then all claim keywords repeated in a quick list (PERFORMANCE, COMPATIBILITY, HEALTH AND SAFETY, DATA-DRIVEN SERVICES, CORDLESS) each "without compromise".
- 141.1-151.5 (93-100 %) end: 3 fast product shots, "#UNCOMPROMISE" stacked on a red chevron next to the battery, red line wipe to white, Hilti logo.

## Cut rhythm (adaptive detector; the scene detector found only 58 shots because many cuts sit under type and wipes)
- 75 shots in 151.5 s. ASL 2.02 s, median 1.28 s, 36 % under 1 s, 15 % over 3 s.
- ASL per quarter 1.26 / 1.72 / 2.53 / 3.44 s: fast site action first, slower CGI and data graphics later.
- Densest 0-10 s and 50-60 s (8-10 cuts per 10 s). Longest: CGI platform sequence 18.8 s, recap 11.6 s, data block 10.0 s. Shortest 0.32-0.44 s.
- The 65-84 s CGI block has 2-3 soft internal transitions (camera re-frames) not counted as cuts.

## Typography
- Neo-grotesk bold caps, white, no box (Helvetica/Arial Bold look; closest free font: Archivo Bold or Inter Bold).
- Two-level claim: keyword ≈12-13 % frame height caps + qualifier ≈8-9 % caps ("PERFORMANCE / OF CORDED"), or keyword + small line ≈4 % ("WITHOUT COMPROMISE"). Left-aligned, bottom-left or top-left, safe margin ≈5 % of width.
- Keyword holds over 2-6 shots (3-9 s) while footage cuts under it; text enters with a quick slide/blur-in and leaves the same way; second line follows by ≈0.2 s.
- Data icons: white line pictograms ≈8 % H + label ≈5 % sentence case, stacked on the right, pop in one by one.
- End hashtag: 4 stacked lines ≈13 % each on a red diagonal chevron band, left half.
- "NURON" product logotype ≈10 % H, centred, with a glitch/flash build.

## Colour/grade
- Warm-cool contrast: sunrise/sunset orange skies, cool grey concrete, brand red product in every shot. Moderate contrast, slight vignette. CGI on a clean white sweep. Night city in teal/orange for the recap.

## Camera/shots
- Mostly hand-held and gimbal close-ups of hands, tools and debris (sparks, dust, rebar), shallow focus, many low angles. Workers in full PPE.
- Time-lapses of cranes for bookends; one CGI product sequence in the middle; screen-like data graphics composited over real footage.
- No drone, no customer names, no real UI recording (dashboard is a designed mock-up).

## Transitions
- Hard cuts under persistent type; red chevron (">" brand shape) wipes at block changes (≈46 s, 67 s, 103 s, 128 s, 143 s); red line wipe to the white logo card.

## Sound
- Music only (driving rock-electronic, no VO, no subtitles). Integrated -13.1 LUFS, range 5.5 LU, true peak +0.4 dBTP (hot master).
- Drop-out 140.9-141.5 s (0.6 s, to -76 dB) before the final product burst; hit at 141.55 s. 0.3 s gap at 148.5 s, then the logo hit at 149.0 s (+32 dB).
- Tool sounds (impact, grinder) mixed under the music in the claim blocks. Cuts on onsets only 33 % (chance 26 %): cut more to action than to beats.

## What makes it premium
- One repeated phrase ("... without compromise") structures 2.5 minutes; each claim is one keyword.
- Type stays while shots change underneath, so the text reads and the pace stays high.
- Real site action for power claims, CGI only for the "one platform" idea, graphics only for data.
- Brand shape (chevron) used as the transition device.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- Write 8-12 keyword claims on one pattern ("PERFORMANCE / OF CORDED"). Shoot 3-5 close-ups per claim (hands, tool, debris), 1-2 s each.
- Claim type: `font:700 12.5vh/0.95 'Archivo'; text-transform:uppercase; color:#fff; left:5vw; bottom:12vh`; qualifier `font-size:8.5vh`. In: `gsap.from(line,{x:-40,opacity:0,filter:'blur(8px)',duration:.35,stagger:.2,ease:'power3.out'})`; hold over 2-6 shots; out reversed 0.25 s.
- Chevron wipe: SVG polygon `points="0,0 60,0 100,50 60,100 0,100 40,50"` in brand red, `gsap.fromTo(chev,{xPercent:-120},{xPercent:120,duration:.45,ease:'power2.inOut'})`, cut the clip at the midpoint.
- Data card: white line icons 8vh + Inter 600 5vh labels, right side, `stagger:.3` pop (`scale:.8 -> 1, back.out(1.6)`).
- Music only, master ≈-13 LUFS for social; 0.6 s silence before the last burst; logo on white after a line wipe.
