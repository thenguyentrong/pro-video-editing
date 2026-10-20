# Life at Hilti Headquarters  (Hilti Group, 2021-08-27, 2:26, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=UeJPLBszc2A
Purpose: recruiting / employer-brand film
One-sentence point: Working at Hilti's headquarters region means a caring, international company in the middle of Alpine nature, with family support and room to grow.

## Structure
- 0.0-10.9 (0-7 %) hook: black open, POV drive on a country road through cornfields (5 s), drone pull-back over the HQ campus with mountains behind. Female VO starts: you could be commuting here.
- 10.9-51.5 (7-35 %) the region: skier, hikers on a ridge, people on a lake raft, kids in snow, a town river at dusk, drone over the HQ town, a hiker on a summit, old-town aerial, cows, meadow with boots in grass, church tower in fog, fondue, a woman in a forest, paddle-boarder top-down, snow peaks, campus aerial. VO lists leisure and "this can be your backyard".
- 51.5-70.0 (35-48 %) the company: employee walking through the bright lobby, red staircase top-down, team lunch, three colleagues in red Hilti shirts, campus aerial, logistics hall with two staff in hi-vis checking a tablet, an exoskeleton demo, the Jaibot drilling robot, a stage panel. VO: 60+ nationalities, three locations, innovation.
- 70.0-109.4 (48-75 %) culture and care: meetings, labs, an engineer in a white helmet on a site, product demo table, open office corridor, campus walk, a handshake on site, volunteers hugging, a parent on a video call with a baby, the on-campus child care sign, e-bike commute. VO: inclusive, growth, family.
- 109.4-139.2 (75-95 %) invitation: desk work, valley aerial, a child running to a parent at home, a woman studying, two women talking, a group selfie of staff in red jackets, mountain valley, kids walking to school, slow farmland drone (5.6 s).
- 139.2-146.1 (95-100 %) red jackets cheering, red line wipe to the Hilti logo on white (6.9 s incl. logo).

## Cut rhythm
- 66 shots in 146.1 s. ASL 2.21 s, median 2.04 s, 12 % under 1 s, 20 % over 3 s, 27.1 shots/min.
- ASL per quarter 2.61 / 1.66 / 1.74 / 3.04 s: calm open, faster middle (company + culture, up to 9 cuts per 10 s at 60-70 s), slow drone end.
- Longest: logo/tail 6.9 s, farmland drone 5.6 s, snow peak 5.3 s. Shortest 0.64-0.76 s (robot and exoskeleton inserts).
- Cuts are not beat-locked (46 % on onsets vs 48 % chance): cut on VO phrases.

## Typography
- None: no supers, no names, no captions. The only graphic is the end logo (red Hilti box ≈9 % of frame width, centred on light grey) after a thin red diagonal line wipe.

## Colour/grade
- Bright, saturated "travel film" grade: blue skies, green meadows, white snow; offices bright and airy. Hilti red as the uniform colour of staff (shirts, jackets) - the brand colour lives in people, not graphics.

## Camera/shots
- About a third is aerial (drone over campus, towns, lakes, peaks, farmland); a large share of the scenery and lifestyle shots look like licensed stock (generic travel and family moments, mixed lens looks).
- Company footage: gimbal walks through lobby and office, team scenes, logistics hall, product demos (exoskeleton, Jaibot) - only 2-3 construction shots in the whole film.

## Transitions
- Hard cuts; red line wipe into the logo; no type transitions.

## Sound
- Warm female voice-over over a light acoustic-pop track, continuous. Integrated -18.6 LUFS, range 3.6 LU (very flat), true peak -1.8 dBTP. No drop-outs; biggest hit at 129.35 s (+36 dB, music lift into the final valley aerial); 1.3 s silence on the logo tail.

## What makes it premium (and what is weak)
- Strong sense of place: aerial geography first, then the campus inside it.
- Brand red worn by real staff, so a stock-heavy film still looks "Hilti".
- Weak: no named employees, no voices of staff, heavy stock; reads like a regional tourism film. For recruiting a site crew it would need real people speaking.

## Recipe (real footage + HTML/GSAP, Hyperframes)
- 60-70 shots of 1.5-3 s; start and end on 5-7 s drone shots.
- Order: commute POV -> region (30 %) -> campus and teams (15 %) -> culture/family (25 %) -> invitation (20 %) -> logo.
- Dress staff in the brand colour; no text until the logo.
- Logo wipe: SVG line `stroke:#d2051e; stroke-width:.4vh` drawn diagonally across white in 0.4 s (`stroke-dashoffset`), logo cuts in on the next frame, hold 3 s.
- Stock queries (licensed, 4K): `alpine valley aerial summer`, `hiker summit sunrise`, `office lobby walking`, `family child running home`. Mix at most 1 stock shot per 2 own shots.
