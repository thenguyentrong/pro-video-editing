# Deep-tech hardware
**Use it for:** defense, aerospace, drone, autonomy and other deep-tech hardware films: product reveals, mission or recruiting manifestos, field-test and flight-test films, milestone films, investor or grant videos for a hardware startup that must look serious and be believed. **Not for:** consumer gadgets sold on lifestyle (use `apple-precision.md` or `design-tech.md`), factory robot demos with a datasheet focus (use `industrial-robotics.md`), pure brand emotion without a machine (use `cinematic-brand-anthem.md`).

**Reference films:**
Anduril — Thunder: Autonomous Attack Rotorcraft for the Deep Fight (2026, 0:56) — anduril/thunder-deep-fight
Anduril — Fight Unfair (2026, 0:31) — anduril/fight-unfair
Anduril — YFQ-44A: The Road to First Flight (2026, 3:12) — anduril/yfq-44a-road-to-first-flight
Helsing — CA-1 Europa: Autonomous Air Dominance (2025, 1:01) — helsing/ca-1-europa
Helsing — HX-2 Field Testing (2025, 1:01) — helsing/hx-2-field-testing
Helsing — Cirra: AI for Electronic Warfare (2026, 1:12) — helsing/cirra-electronic-warfare
Quantum Systems — Image Film (2025, 1:30) — quantum-systems/image-film
Quantum Systems — Vector AI (2025, 0:50) — quantum-systems/vector-ai
Quantum Systems — Vector: Real Missions. Real Results. (2025, 3:50) — quantum-systems/vector-real-missions
Skydio — F10: Real Flights. No CGI. (2026, 0:36) — skydio/f10-real-flights-no-cgi
Skydio — Reality Doesn't Care (2026, 1:00) — skydio/reality-doesnt-care
Skydio — Introducing F10 Lightrunner + MegaDock (2026, 2:13) — skydio/f10-lightrunner-megadock
Zipline — 100 million autonomous miles (2025, 1:06) — zipline/100-million-autonomous-miles
Zipline — How Zipline Delivers with Platform 2 (2025, 0:59) — zipline/platform-2-how-it-delivers
Zipline — 10 years in 1 minute (2025, 1:05) — zipline/10-years-in-1-minute
SpaceX — Starship's Tenth Flight Test (2025, 2:14) — spacex/starship-flight-10

## Signature
Trust is designed, not claimed. These films keep two worlds apart: the **reveal** (a dark, one-colour, often render-looking object with a huge name and spec-sheet labels) and the **proof** (real footage from a real place, untouched). In the proof, four things are always visible: the machine's own view (its camera feed or ground-station screen with status text and a clock), the human in control (a hand on a tablet, a finger on a confirm button, a label saying the operator is in the loop), named facts (place, partner logo, date, a count of days, miles or deployments), and one long uncut take of the decisive moment (take-off, drop, delivery, strike), which is the longest shot of the film. Text is short, technical and free of adjectives: capability labels in caps, spec sentences with units, monospaced system text. A short drop-out (0.5-1 s) comes before the biggest reveal. European brands (Helsing, Quantum Systems) are cooler and more monospaced; US brands (Anduril, Skydio, Zipline) use bigger names, numbers and people.

## Numbers
Measured on 16 films with ffmpeg-based cut detection checked by eye, EBU R128 loudness and speech timing. Values marked ≈ are eyeballed from frames.

| Metric | Product reveal (Thunder, CA-1, Vector AI, F10 launch, Zipline P2) | Mission manifesto (Fight Unfair, Reality, QS image film, Zipline 100M, Zipline 10 years) | Field-proof demo (HX-2, Cirra, Vector missions, F10 real flights, YFQ-44A, Starship) | European deep-tech (Helsing x3, Quantum Systems x3) |
|---|---|---|---|---|
| ASL | 1.05-4.17 s | 1.09-3.02 s | 1.20-2.20 s (6.39 s with long text cards) | 1.05-4.17 s (6.39 s) |
| Median shot | 0.60-3.60 s | 0.77-1.68 s | 0.90-1.88 s (3.60 s) | 0.60-3.60 s |
| % shots < 1 s | 0-66 % | 20-64 % | 8-57 % | 0-66 % |
| Shots per minute | 14.4-57.0 | 19.9-55.0 | 27.2-49.9 (9.4) | 9.4-57.0 |
| Cut density curve | slow-fast-slow; fragments first, the whole object only at 0-13 % and 77-92 %; or a steady deceleration 16 → 0 cuts per 10 s | fastest in the first 10 s (9-15 cuts per 10 s), slowing to one long people or proof shot (7-17 s) at the end | fast montage (10-17 cuts per 10 s) around slow UI and proof takes (0-3 cuts per 10 s) | as left; UI and sensor takes 4-15 s |
| Longest proof take | hero or outro 5.2-10.7 s (delivery take 6.6 s) | held drop 17.0 s; people 8.4 s | 6.2-9.3 s (take-off 9.26 s, strike 6.24 s, fly-by 6.98 s); sensor holds ≈13-14 s | 4.9-6.2 s; sensor ≈13-14 s |
| Big name / number (% H) | ≈12-35 % (cropped title, wordmark, bold+light pair ≈16 %) | slogan ≈13 %; big number ≈20 % | mono title ≈10 %; wordmark ≈25 % | mono ≈4.5-10 %; light name ≈5 % |
| Label / caption (% H) | caps ≈4.5 %; feature label ≈4 % + ≈2.3 % | number super ≈5 %; title line ≈2.2 % | caps label ≈5 % x 2 lines; spec sentence ≈3.5 %; caption ≈3.5 % + ≈2 % | caps ≈5 %; caption ≈3.5 % + ≈2 % |
| Data text (% H) | ≈1-2 % caps metadata | ≈1.2 % | ≈1.2-2.5 % mono (location, telemetry, status bar) | ≈1.2-2.5 % mono |
| Words per card | 1-4 (label), 1 name | 3-8 per line | label 2-6 words; sentence 4-9 words | 2-6 |
| Hold | label for the whole section (≈10 s) | number 2-3 s | label across 2-6 shots; caption = the whole take (3-15 s) | as left |
| Voice | none | narrator ≈1.6-2.4 words/s, or none | none, real radio/mission call-outs, or an engineer interview ≈2.2 words/s | none or engineer; QS brand film narrator ≈1.6 words/s |
| Loudness (integrated) | -20.0 to -10.7 LUFS | -24.5 to -8.9 LUFS | -21.8 to -11.9 LUFS | -19.0 to -8.9 LUFS |
| Drop-outs | 0.5-1.7 s before the hero or the logo; silent title up to 4 s | 0.5 s before the first hit; 1-2.5 s inside the held proof shot | 0.6-0.9 s before the title or first reveal, then a +26 to +41 dB hit | 0.5-1.7 s before title or logo |
| Aspect | 16:9 | 16:9 | 16:9; 2.39:1 letterbox for documentary or post-logo proof | 16:9 |

Several masters peak above 0 dBTP (up to +1.9); do not copy that, deliver at -1 dBTP.

## Structure
Field-proof demo (the default when you must be believed), beats with share of runtime:
1. **Hook (0-5 %).** The most dramatic real POV or a cold open with real radio/control audio over dark shots. No logo.
2. **Title and context (5-12 %).** 0.5-0.9 s silence, then a monospaced title typed on, or 2 text cards on black with date, customer and task.
3. **Setup (12-25 %).** Named place (location super), named partner (label + logo), the people (faces blurred if needed), the machine prepared.
4. **Machine view + human control (25-55 %).** The real UI or onboard feed 4-5 s per state; a hand confirms; manual and automatic modes shown as separate states, each with a label.
5. **Capability montage (55-85 %).** One caps label per claim, held across 2-6 short real shots; densest part (10-17 cuts per 10 s).
6. **Proof take (inside 45-90 %).** The decisive moment uncut, 6-10 s, the longest shot.
7. **Logo (85-90 %).** 2-6 s on black.
8. **After the logo (90-100 %, optional).** One letterboxed proof shot, or a quiet black-and-white epilogue of the team watching.

Product reveal: title 0-13 % → 3-4 sections of one part each (13-77 %) → drop-out + full object hero (77-92 %) → logo (92-100 %). Mission manifesto: fragments or domains (0-25 %) → list of hard facts or proof reel (25-70 %) → climax proof (70-88 %) → slogan / call to action (88-92 %) → logo.

## Picture
- **Reveal:** near-black (mean luma ≈0.12-0.16), one saturated key colour (green, or cold white/teal), a warm practical as second light; symmetrical front-on wides and macro slides; the camera barely moves, the light moves (LED tubes switching, light rings, rows of ceiling lights).
- **Proof:** real places, natural or overcast light, mild desaturation; native colour for sensor feeds, UI and onboard cameras (fish-eye and compression kept).
- **Machine view:** full-screen UI recordings with real status text, compass tape, reticle and clock; never redrawn.
- **People:** operators, engineers, customers (police, firefighters, utility crews, clinic staff, families). Named people in lower-left supers; anonymous personnel blurred.
- **Real vs render:** never in the same shot. Renders only for reveal, design, internal parts or a product family; flight, delivery and strike proof are always real. A real-only cut of the same product is the strongest trust signal.

## Type
| Use | Seen as | Closest free font | Weight / case | Size (% H) | Placement | Animation |
|---|---|---|---|---|---|---|
| Reveal title | technical grotesk | Inter Tight | 700, title case, tracking -.04em | ≈35 % cap, cropped by the top edge | top, bleeding off | fade 0.4 s, hold 5-7 s |
| Spec label | grotesk caps | Inter Tight | 600 caps, 2 lines | ≈4.5 % | top-left, x 5 %, y 8 % | character scramble 0.3-0.5 s |
| Role row | grotesk caps | Inter Tight | 600 caps, 3-4 words | ≈4.5 % | bottom line, spread edge to edge | scramble, stagger 0.1 s |
| Capability label | grotesk caps | Inter | 700 caps, 2 lines | ≈5 % per line | bottom-left, x 3 %, y 88 % | on with the cut, letter reveal optional |
| System title / location | monospaced caps | JetBrains Mono / IBM Plex Mono / Space Mono | 400-700, letter-spacing .1em | title ≈4.5-10 %, location ≈2.5 % | centred or left of centre | typewriter 0.03-0.04 s per character |
| Feature label | geometric sans | Montserrat | 700 name + 400 benefit | ≈4 % + ≈2.3 % | bottom-right, right-aligned | fade + y 10 px, 0.3 s |
| Proof caption | geometric sans | Montserrat | 700 label + 400 line | ≈3.5 % + ≈2 % | bottom-left, x 4 % | fade 0.3 s, hold the whole take |
| Spec sentence | neutral grotesk | Inter | 500, sentence case, full stop | ≈3.5 % | centred, y 50 %, soft shadow | random letter flicker 0.4 s |
| Counter | neutral grotesk | Inter | 500 | ≈5 % | centred | value steps up over 3 shots |
| Big number | grotesk | Inter | 700 + 3.5 % question line + 3 % unit | ≈20 % | left of centre | digits roll 1.6 s |
| Context card | grotesk | Inter | 500, sentence case | ≈4.5 % | two columns at x 6 % and 52 % on black | words one by one, stagger 0.12 s |
| Data / metadata | mono or grotesk caps | JetBrains Mono / Inter | 400 | ≈1-2.5 % | corners, under titles, status bars | static or per-frame counters |
| Name super | grotesk | Inter | name 500 + role 400 | ≈3 % + ≈2 % | lower-left | fade 0.3 s, hold 3 s |

Rules: white on picture, no boxes (except a real UI's own status bar). Units always written. One proof word in brand colour per film at most. No adjectives on screen.

## Transitions
- Hard cuts almost everywhere.
- Section wipes in reveals: three 0.25 s light-streak shots, or 1-3 frame black dips between fragments.
- Fades only to and from black cards (title, context, logo).
- Letterbox or a shrinking picture window to mark an epilogue.

## Sound
- **Reveal:** no voice. Music with hits on section changes; 0.5 s silence before the hero, then the loudest hit (+29 dB). A silent title of up to 4 s, then the first hit on the first cut.
- **Field proof:** real audio as the voice: radio traffic, countdowns, status call-outs, or one engineer interviewed at the site. Music under it. 0.6-0.9 s silence before the title or first reveal, +26 to +41 dB hit after it.
- **Manifesto:** one narrator, 1.6-2.4 words/s, short lines with pauses; anaphora (the same opening words per line) works well. Or no voice with 2-3 number supers.
- **Held proof shot:** pull music to silence for 1-2.5 s inside it and bring it back with a hit.
- Master to -14 LUFS / -1 dBTP for web (the studied films range from -24.5 to -8.9 LUFS).

## Do / Don't
| Do | Don't |
|---|---|
| Show the machine's own screen with real status text and time | Draw a fake HUD over footage |
| Show and label the human in control | Imply full autonomy without showing who decides |
| Name the place, the partner (with logo), the date, the count | Use vague claims without anchors |
| Make the decisive moment the longest uncut shot | Montage the proof into sub-second cuts |
| Keep renders for reveal, design and internals | Mix render and real in one proof shot |
| Release or include a real-only cut when the reveal is render-like | Leave viewers guessing whether flights are CGI |
| Write labels as test-report headings, caps, 2 lines | Write marketing adjectives on screen |
| Blur faces when people cannot be shown | Cast actors as operators |
| Put 0.5-1 s silence before the big reveal | Keep music wall-to-wall at one level |

## Recipe
1. **Choose the variant** (below) and write one claim per beat. Each claim needs one real shot, and if possible one screen recording and one number with a unit.
2. **Shoot or collect (real or licensed only):** wide of the real site at dawn (6 s, drone); the machine prepared by people (3-4 shots); the operator's screen recorded with OBS or a screen-capture device during the test; a hand confirming on the screen (2-3 s); the decisive moment locked off or long lens, 8-10 s uncut; onboard or POV camera on the machine; the team watching; 30 s of room tone and radio. For a reveal: the real machine in a black space lit by one coloured LED tube + one warm practical, slider moves 3-7 s.
3. **Stock only for context, never for proof.** 1080p minimum, prefer 4K, no AI clips, licence logged. Queries: `aircraft hangar dark lights`, `control room operator monitors`, `airfield aerial dawn`, `radar antenna tripod`, `rugged tablet hands outdoor`, `firefighters night operation`, `utility worker power line inspection`, `suburban houses aerial`.
4. **Build the type in HTML/GSAP:**
   - Capability label: `font:700 5vh/1.05 Inter; text-transform:uppercase; position:absolute; left:3vw; bottom:6vh; text-shadow:0 0 6px rgba(0,0,0,.5)`.
   - Mono title / location: `font:400 2.5vh 'JetBrains Mono'; letter-spacing:.1em`; typewriter with `tl.set(el,{textContent:str.slice(0,i)}, t0 + i*0.035)`.
   - Scramble label: per character pick a glyph from `'ABCDEFGHJKLMNPRSTUVWXYZ0123456789'` by `Math.floor(t/0.04)` and a seed, lock the real letter at 0.4 s (seek-safe).
   - Counter: `gsap.to(o,{v:120, duration:2.4, ease:'steps(3)', onUpdate:()=>el.textContent=Math.round(o.v)+' minute flight time'})` over 3 real shots.
   - Context card: 2-column grid (6vw / 52vw), Inter 500 4.5vh, words `from({autoAlpha:0}, .15, stagger .12)`, hold 2 s.
5. **Cut:** montage 0.6-1.5 s per shot; UI 4-5 s per state; proof take 6-10 s; logo 2-6 s on black.
6. **Sound:** real audio first (radio, call-outs, interview), music second; one 0.5-1 s drop-out before the main reveal; master -14 LUFS / -1 dBTP.
7. **QC:** every proof shot real and unaltered; every speed change or render labelled or kept out of proof; the human role visible; place, partner and date on screen; the longest shot is the proof.

## Variants
**Product reveal (Anduril Thunder, Helsing CA-1, Quantum Vector AI, Skydio F10 launch).** One object in a black space with one coloured light; a giant cropped name at the start (or the name withheld to 80 % and set small in light weight); 3-4 sections, one part per section with a caps spec label top-left (or one component per 3.6 s shot with a bold label bottom-right); 0.25 s light-streak bursts or 1-frame black dips between sections; 0.5 s silence, hero, logo. ASL 1.05-4.17 s. A narrated launch (Skydio) adds 10-13 s of customer work first, counters on real flights, the robot dock in 8 s takes, and keeps renders to design and family shots.

**Mission manifesto (Anduril Fight Unfair, Skydio Reality Doesn't Care, Quantum image film, Zipline 100M and 10 years).** A short spoken creed or anaphora (6-8 lines, ≈2 words/s) over real footage, one domain or hard fact per shot; 12-16 shots of 1.2-1.8 s, or fragments under 0.6 s at the start slowing to one long people shot; slogan card in the last 10 %; logo. Or no voice: 2-3 number supers on real shots around one 15-17 s held proof shot with a music drop.

**Field-proof demo (Helsing HX-2 and Cirra, Quantum Vector missions, Skydio F10 real flights, Anduril YFQ-44A, SpaceX Starship).** The default structure above. Real UI 4-5 s per state, caps labels per claim, partner logos, named location, dates and day counts, the proof take as the longest shot. Documentary form: cold open with real radio, two-column text cards, build montage, operator and button, take-off 9 s uncut, claim super with a day count, logo, black-and-white epilogue. Chronicle form: mission audio first, strict time order, onboard and human views alternating every 3-5 shots, no supers.

**European deep-tech (Helsing, Quantum Systems).** Cooler and more technical than the US films: monochrome or natural overcast colour, monospaced system type for titles and locations, geometric sans for captions, no slogans on screen, interview with an engineer at the site instead of a narrator, capability labels that read like test-report headings, faces blurred, datasheet tables (span, weight, endurance) and dated timelines. Fast cutting (ASL 1.05-1.54 s in Helsing films) with UI and sensor takes held longer.
