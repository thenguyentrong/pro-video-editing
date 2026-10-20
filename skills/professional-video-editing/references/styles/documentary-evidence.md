# Documentary evidence
**Use it for:** putting proof on screen inside any film: news headlines, studies and reports, laws and court filings, leaked or official documents, numbers and charts, maps and satellite images, other outlets' footage, real objects. Works inside an editorial explainer, a pitch film, a trailer-style problem beat or a vertical short. **Not for:** decoration (a screenshot that proves nothing), whole web pages, invented or sample documents, or a product UI demo.

**Reference films:**
Vox — How the US created an ambulance crisis (2025, 6:51) — vox/ambulance-crisis
Vox — The House of Representatives is too small (2026, 8:03) — vox/house-too-small
The New York Times — How Satellite Images of Big Bend Contradict Border Agency Claims (2026, 6:00) — nytimes/vi-big-bend-satellite
The New York Times — How a New U.S. Weapon Killed 21 Civilians in Iran (2026, 6:31) — nytimes/vi-us-weapon-iran
The New York Times — How Does Your College Choice Affect Your Income? (2026, 1:21, 9:16) — nytimes/short-college-income
WSJ — Why the World's Largest Megaproject Collapsed (2026, 10:54) — wsj/megaproject-collapsed
WSJ — This Critical Oil Chokepoint Is Now Under Houthi Control (2026, 4:04) — wsj/houthi-chokepoint
Bloomberg Originals — How India's Day Retail Traders Lost Billions (2026, 11:28) — bloomberg/india-retail-traders
Bloomberg Originals — What's Wrong With Germany? (2026, 12:29) — bloomberg/whats-wrong-with-germany
Johnny Harris — The REAL reason the US can't beat Iran (2026, 39:30) — johnny-harris/us-cant-beat-iran

## Signature (one paragraph)
A document is a physical object, not a screenshot. It is cropped to the line that matters, sits in light (a page on a dark desk, on graph paper or on black), moves slowly, and everything except the key line goes soft and dark. One mark points at the proof: a thin underline, a focus band, a white box, or one highlighter in the film's single accent colour; it reveals in about 0.5-1 s and the camera stops when it finishes. A small source line (outlet or author, date) is always on screen. Evidence is held long enough to read, and the person behind it (author, official, reporter) appears next. Maps and charts get one consistent visual world and one continuous move each, and numbers are made physical (scale comparisons, dots, a huge outlined figure).

## Numbers
Measured on the first 150 s of each film (`metrics.json`); ≈ = eyeballed from frames; (ft) = in-house taste rules (not measured).

| Metric | Range | Where it comes from |
|---|---|---|
| ASL of evidence-led films | 2.21-5.17 s | Vox 2.21-5.00, NYT investigations 4.84-5.17, WSJ 2.78-3.57, Bloomberg 2.21-2.59 |
| Median shot | 1.52-4.19 s | same films |
| % shots < 1 s | 0-29 % | NYT investigations 0 %, WSJ 2-7 %, Vox 3-19 %, Bloomberg 4-29 % |
| Shots per minute | ≈12-27 | 60 / ASL |
| Cut density curve | long holds on the proof, short bursts around it: 3 hard punch-ins of 0.5 s on a map before the full view (Vox); 3 document crops of 1.5-2 s each, getting closer (WSJ); a report section with 7 cuts in 10 s (Vox, the densest part of that film); comparison cards every 2-2.5 s (NYT) | notes |
| Headline / map montage | 8, 8, 6, 6, 5, 4, 4, 3, 3 frames at 30 fps, then a hard stop (ft); real atlases at 4-6 frames each at 24 fps (Johnny Harris) | ft, library |
| Hold times | document or object 6-13 s (Vox); proof 14-28 s (NYT); static chart 10-13 s (Economist); drawn chart 13-25 s (Bloomberg); map move 8-16 s (WSJ), 18.6-27.9 s (Vox, NYT), 14-38 s (Johnny Harris); headline card 2.5-3 s (Bloomberg); photo 3-4 s (Economist) | notes |
| Highlight / mark timing | reveal 0.5-1.2 s (ft 0.5 s; NYT 0.6 s; WSJ 0.6 s; Bloomberg box 0.5 s; Vox 0.9-1.2 s); outline box draw 0.5 s; slow push `scale 1 → 1.04-1.06` over 2-4 s, linear | notes, ft |
| Text size (% of frame height) | source / credit 1.3-3 % (NYT credit 1.5 %, map source 1.3 %, Vox corner credit 2.4 %, WSJ credit block 1.9 / 3 / 3 %); chart title 2.6-5 %; re-set key sentence ≈4.5 %; map labels 2.6-3.5 %; one huge number ≈10 % | notes |
| Words per mark | 3-5 words that matter in a headline (ft); one phrase or one sentence highlighted; map labels 1-3 words; headline card max 3 lines | ft, notes |
| Loudness | NYT investigations -17 to -20 LUFS with gaps to -71 dBFS around the hardest images; Vox -14.1 to -27.0; WSJ -19 to -24 | metrics |
| Drop-outs | 1.8-1.95 s of silence before or after the hardest evidence (NYT); 0.5-2 s bed drop before the evidence section, then up to +32 dB (WSJ) | metrics |
| Aspect | 16:9; vertical charts are built natively for 9:16 (NYT short) | notes |

## Structure
Anatomy of one evidence beat (8-25 s). Shares are ≈, computed from the Vox ambulance map beat (20.7-28.5 s: three 0.5 s punch-ins, full map from 22.2 s, highlighter 24-27 s).
0. **Optional lead-in.** The reporter handles the printed page or points at the monitor (NYT), so the viewer sees where the proof comes from.
1. **Arrive (≈0-20 %).** Three hard punch-ins of 0.5 s, or two or three crops getting closer (1.5-2 s each, WSJ), or a slow push.
2. **Context (≈20-40 %).** The full chart, map or page with its own title and the source line readable.
3. **Focus (≈40-80 %).** The key line sharp, the rest blurred and darkened; the mark reveals while the voice says those exact words; the camera stops when the mark finishes.
4. **Hold (≈80-100 %).** Hold until the voice has finished the line plus 0.5-1 s (`cutting-craft.md`), with the source line still on screen.
5. **The person.** Cut to the study author, official or reporter; a real face makes the paper credible.
In a full film: the first proof lands inside the cold open (0-13 s) and the film returns to evidence every chapter. Investigations (NYT) let proof run 14-28 s; business films (Bloomberg) show 2-3 graphics per 150 s, each held 13-25 s.

## Picture
- **Paper in light (default cinematic look, ft).** Tight crop of the headline or line, never the full page. Cream paper (`#F2EEE6`), ink slightly grey, a light noise or halftone texture in `multiply`. The page sits in soft 3D on a dark desk with a long shadow and moves very slowly; a fast zoom reads as a meme.
- **Documents on black (NYT).** The scanned page at ≈95 % width on `#000`, one flat yellow bar on the exact sentence, the rest blurred. First show the reporter handling the printed page.
- **Paper world (Vox).** Real scans and objects on off-white graph paper (`#FAFBF6`) or grey creased paper (`#E7E7E7`); the key sentence of a law re-set large in a book serif on a torn paper strip that unrolls over the original page; the page zoomed so it runs off one edge; newspaper macros with one word highlighted.
- **Focus band (Bloomberg).** Page on black; everything blurred 3 px and darkened to ≈35 % except one band; the key phrase in a light box; source label top-left.
- **Satellite (NYT, WSJ).** Natural or grayscale imagery; white 2 px box or outline with a soft shadow, white serif label under it; slow zoom in, then pull back for context; before/after pairs; date top-left and imagery credit on every frame.
- **Maps.** One map world per film. Light: pale basemap, 1 fill + max 2 line colours + 1 marker colour, direct labels, locator pull-out, source line bottom-left (NYT). Dark: desaturated satellite texture, dark seas, one colour per actor, dashed white front lines, one glow for the threatened point (WSJ). Old maps as base layers, re-tinted, credited in a corner (Vox).
- **Charts.** Explain the encoding first (zoom in, arrow, 2-word label), then compare 2 named examples with exact numbers; dim the other rows to ≈25 % (NYT short). Or put the chart on a real surface (aerial ground, a steel container) and draw the line over 20-25 s while the time axis scrolls (Bloomberg). Or one static house chart held 10-13 s (Economist). Always a title and a source line.
- **Other outlets' footage.** Keep their chyrons, logos and look; add a credit; scale to ≈85 % height on black if it needs a frame (NYT); tag corporate or military promo material as promotional footage. Multi-source sync: a grid of CCTV and phone clips, one panel scales to full frame in ≈0.75 s.
- **Numbers made physical.** Overlay a distance on a familiar region at the same scale; compare a height with famous buildings (WSJ); the data in a form people know, such as a seat chart animated across years (Vox); one outlined condensed number ≈10 % H (Johnny Harris).
- **Objects.** Film the real object like a product: macro, hands, shallow focus, the provenance sticker in close-up (WSJ).

## Type
- **Source line (always on).** Pick one format per film:
  - ft / cinematic: small wide-tracked caps under the page, outlet + date. Free font: Inter 500 or IBM Plex Mono, letter-spacing ≈0.2 em.
  - NYT: `400 1.5vh "Libre Franklin"`, white, bottom-left (x 3 %, y 96 %); maps and charts carry a source + graphic credit at ≈1.3 % H.
  - WSJ: three lines top-left at x ≈4.7 %: source caps 1.9 % H, place 3 % H, date 3 % H.
  - Vox: corner credit `500 2.4vh Inter`, black on paper; study citation as author + month/year at ≈2.5 % H under the chart title.
  - Johnny Harris: citation bar (name, programme in italics, date) `400 2.2vh Inter` in a 55 % black box, bottom-left.
- **Chart titles:** bold serif ≈5 % H (Vox, Source Serif 4) or bold sans 2.6-3.6 % H (NYT, Bloomberg, Economist).
- **Re-set key sentence:** book serif ≈4.5 % H (free: Libre Caslon Text), black on paper.
- **Map labels:** 2.6-3.5 % H white sans (Libre Franklin 600-700); actor names in caps; place names in sentence case; Johnny Harris uses glowing engraved serif caps ≈5.5 % H (free: Cinzel).
- **Marks:** one accent per film: white boxes (NYT), teal (WSJ `#1FB5B5`), yellow (Vox `#FEFF0F`), light grey box (Bloomberg), pale gold underline `#e8d9a8` (ft).
- **Animation:** mark reveals 0.5-1.2 s `power1.inOut` or `power2.inOut`; labels fade 0.3-0.4 s with a small rise (y 6-8 px); leader lines `scaleY 0 → 1` 0.3 s; pins `scale 0 → 1` 0.3-0.35 s `back.out`.

## Transitions
- Hard cuts between proof pieces. The move lives inside the shot (push, zoom, pull-back), not between shots.
- Headline match-cut montage, once per film: 10-12 crops with the key word at the same screen spot, getting shorter, a click on each cut, then a hard stop on the main headline.
- Photos slide in over ≈8 frames with blur ≈50 → 0 (ft). Old photos can drop onto the paper like prints (Vox).
- Paper strip unroll ≈0.7 s, then roll back up when the point is made (Vox).
- Deletion or missing data: a 0.3 s glitch, then cut (NYT Opinion only; not for neutral reporting).

## Sound
- Paper foley on page moves; a click or shutter on each montage cut.
- Let a borrowed clip's own sound enter hard for ≈1 s, then duck under the voice.
- Before the hardest proof, drop the bed for 0.5-2 s; around images of harm, use true silence (1.8-1.95 s, NYT).
- Keep the voice on top; music 10-15 dB under it or absent.

## Do / Don't
- Do crop to the line that matters and show the source on screen every time.
- Do time the mark to the spoken words and stop the camera when the mark is done.
- Do show the person behind the document right after it.
- Do keep one map world, one chart style and one accent colour per film.
- Don't show a full web page with menus, ads, cookie banners or buttons.
- Don't use more than one filled highlighter box per film in the cinematic look (ft); prefer focus, underline or a white box.
- Don't zoom fast on paper, don't spin pages, don't use stock as proof.
- Don't change numbers, quotes or dates; don't stage a document to look real.

**Licensing (not legal advice).** News screenshots go in only as a cited quotation for commentary: crop to the line you discuss, show the outlet and date on screen, never reproduce a whole article, remove ads and cookie banners, and hide the article's own photo or illustration (it is a separate work). Other outlets' video: short excerpts that you discuss, with their branding kept and a credit added. Editorial-only or non-commercial material never goes into an ad or promo. Public-domain and open sources (government documents, NASA imagery) still get a credit line; commercial satellite images need a licence and a credit. Log every source in the licence log.

## Recipe
One evidence beat (≈10 s) in Hyperframes, 1920x1080. Assets: your own screenshot or PDF page, rendered at 2x.
1. **Capture.** Render the PDF page or take the screenshot at 2x. Crop to the headline or the paragraph that holds the key line. Note outlet, author, date.
2. **Desk.** `background: radial-gradient(ellipse 60% 55% at 50% 45%, #2a2622, #121110 70%, #0b0b0c)`. Optional real plate: stock queries `dark wooden desk top view`, `desk lamp warm light dark room`, `paper texture close up`, `printed newspaper close up macro`.
3. **Page.** Two stacked copies of the crop: a blurred, darkened base and a sharp copy masked to the key line (CSS below). Cream tint and texture on top in `multiply`.
4. **Move.** Whole shot, `ease:"none"`: `rotationX 12 → 8, rotationY -9 → -6, rotationZ -1.2 → -0.6, scale .98 → 1.06`.
5. **Mark.** Underline `height:5px; background:#e8d9a8`, `scaleX 0 → 1` in 0.5 s `power2.inOut`, starting on the first spoken word of the line. Or a highlighter span `#FFFF00` in `multiply`, 0.6-0.9 s.
6. **Source line** under the page in small wide-tracked caps; on for the whole shot.
7. **Sound.** Paper foley at the start, bed 10-15 dB under the voice (or out), voice reads the key line, 0.5-1 s hold after it.
8. **Next shot:** the author, the official or the reporter.

```css
.stage3d{position:absolute;inset:0;perspective:1600px}
.paper{position:absolute;box-shadow:0 50px 90px rgba(0,0,0,.55),0 8px 18px rgba(0,0,0,.35)}
.paper .base{filter:blur(3px) brightness(.62) sepia(.25)}
.paper .sharp{mask-image:linear-gradient(to bottom,transparent 39%,#000 42%,#000 61%,transparent 64%);filter:sepia(.18) contrast(1.04)}
.paper .tint{position:absolute;inset:0;background:#f2eee6;mix-blend-mode:multiply;opacity:.9}
.src{font:500 1.5vh "IBM Plex Mono";letter-spacing:.2em;text-transform:uppercase;color:#f4f3ef;opacity:.82}
.sat-box{fill:none;stroke:#fff;stroke-width:.19vh;filter:drop-shadow(0 1px 3px rgba(0,0,0,.6))}
.wsj-src{font:600 1.9vh Inter;letter-spacing:.08em;text-transform:uppercase}
```
```js
tl.fromTo(".paper",{rotationX:12,rotationY:-9,rotationZ:-1.2,scale:.98},
  {rotationX:8,rotationY:-6,rotationZ:-.6,scale:1.06,duration:dur,ease:"none"},0);
tl.fromTo(".underline",{scaleX:0},{scaleX:1,duration:.5,ease:"power2.inOut",transformOrigin:"left"},tLine);
// satellite: slow zoom, box pops, pull back for context
tl.fromTo(".sat",{scale:1},{scale:2.2,duration:10,ease:"power1.inOut"},t)
  .from(".sat-box",{scale:3,opacity:0,duration:.8,ease:"power2.out"},t+6)
  .to(".sat",{scale:1,duration:4,ease:"power1.inOut"},t+11);
// headline montage: frames at 30 fps, then hard stop on the main one
[8,8,6,6,5,4,4,3,3].reduce((at,f,i)=>{tl.set(`.h${i}`,{autoAlpha:1},at).set(`.h${i}`,{autoAlpha:0},at+f/30);return at+f/30},t3);
```

## Variants
- **Paper in light (cinematic, default).** Dark desk, soft 3D page, focus band or underline, wide-tracked source caps. For pitch films and trailer-style problem beats.
- **Vox paper world.** Graph or creased paper ground, real scans in a strip, yellow `#FEFF0F` outline box drawn in 0.5 s, torn-strip unroll for laws, 3 hard 0.5 s punch-ins before a full choropleth, corner credit 2.4 % H.
- **NYT investigation.** Reporter's desk and screen recordings first; documents full-frame on black with one yellow bar; white 2 px boxes on satellite; comparison cards every ≈2.2 s; credit bottom-left on every clip; silence around the hardest images.
- **WSJ provenance.** Promise first (the subject's own renders), then proof; three document crops of 1.5-2 s with a teal ellipse and highlighter; credit block top-left (source, place, date); one continuous move per map; scale comparisons on familiar places.
- **Bloomberg focus band + charts in the world.** Regulator text on black with one sharp band and a boxed phrase; charts composited on real surfaces with a 20-25 s line draw; own headline cards over footage darkened ≈50 %.
- **Economist house chart.** Black ground, one red, y-axis on the right, source bottom-left; cut in complete, no build; hold 10-13 s; show it again on a screen in the next wide.
- **Johnny Harris map world.** Antique paper, hatching, octagon photo pins, glowing serif labels, continuous moves of 14-38 s; real atlases filmed under a moving light; word match-cut over 12-14 scans at 4-6 frames each.
- **Vertical chart (NYT short).** Chart built for 9:16 on `#F2F2F2`; zoom `scale 1 → 2.2` in 1.2 s to explain the encoding, arrow drawn in 0.5 s, others dimmed to 25 % in 0.4 s; source note always under the chart; captions per phrase in the safe zone (`social-vertical.md`).
