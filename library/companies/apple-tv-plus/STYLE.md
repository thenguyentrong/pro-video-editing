# Apple TV+ – style across examples

Examples (all from the official Apple TV YouTube channel):

| Example | Type | Content length | Shots | ASL | Median | Integrated loudness | Letterbox |
|---|---|---|---|---|---|---|---|
| severance-s2-titles | title sequence (CG) | 78.5 s | 7 (+~10 invisible camera-move transitions) | 11.2 s | 6.0 s | −21.7 LUFS, LRA 16.6 | 2.39:1 |
| pachinko-titles | title sequence (live action + archive) | 82.1 s | 96 | 0.85 s | 0.71 s | −16.1 LUFS, LRA 5.1 | ~2.2:1 |
| slow-horses-s4-trailer | season trailer | 126.3 s (incl. 2.9 s end card) | 99 | 1.28 s | 0.96 s | −14.8 LUFS, LRA 9.6 | 2.0:1 |

## The big picture
Apple TV+ has almost no "network look" inside the content. Each show gets its own complete identity (typeface, colour, aspect ratio, music), and Apple only signs at the end with a black card: the white Apple "tv+" logo inside a soft light bloom, a small tracked-caps tagline, and silence. The premium feeling comes from restraint and from one strong idea per piece, not from house graphics. The only constants are: cinematic letterbox (always wider than 16:9), small type, and the silent bloom end card.

## Sub-styles

### A. Surreal CG oner (Severance S2 titles)
- One concept carried by camera moves: tiny figure, giant objects; push through one object into the next world.
- Few hard cuts (4 in the first 20 s), then 20–36 s continuous shots with invisible transitions; ends on the exact first frame (loop).
- Credits: tiny neo-grotesque, sentence case, grey #a9a9a9, a hairline above, slow 1.7 s fade in; sometimes set in 3D in the scene's light. Title only ~4 % of frame height.
- Dark teal world + one accent red. Very dynamic, quiet music (LRA 16.6 LU, −21.7 LUFS).

### B. Archive-to-joy montage (Pachinko titles)
- Two parts with a clear switch: tinted archive collage on black (1–27 s) → saturated present-day dance (27–77 s) → multi-script title.
- Fast cutting (ASL 0.85 s) that accelerates every quarter (1.08 → 0.68 s); cuts follow dance accents.
- Credits: tiny wide-tracked caps (~0.35 em), 0.25 s fades, often in a torn black box over the photo edge.
- One vintage pop song with vocals, compressed (LRA 5 LU), fades under the title.

### C. Show-branded trailer (Slow Horses S4)
- The show's own card system (distressed condensed caps on teal) on every card; 1.1–1.4 s cards with a 0.4 s shred reveal, hard cut in and out.
- YouTube-first open: 3.7 s letter-matte hook + "TRAILER STARTS NOW" lockup + 1 s black silence, then the trailer starts with a hit and an in-world network logo.
- Classic arc: setup → date card → stakes with talent cards ("ACADEMY AWARD® WINNER") → loud escalation (loudest −7 LUFS momentary) → 11 s quiet dialogue button → title → "NEW SEASON" → Apple card.
- Dialogue-driven cutting (no beat sync measured), ASL 1.28 s.

## Rules (what to copy)
1. The show owns the look; the platform signs only at the end. Do not put platform branding in the creative except a small corner bug and the end card.
2. One concept per piece (scale loop / archive-to-joy / shredded card system). Every shot and every card serves that one idea.
3. Small type. Credits are 1.8–2.5 % of frame height; even the Severance title is ~4 %. Big type is used only when the type IS the image (Pachinko and Slow Horses titles as mattes onto footage, 13–70 % height).
4. Always cinematic aspect: 2.0–2.39:1 letterbox inside 16:9.
5. One accent colour against a controlled base (red on dark teal; duotone per photo; black/white type on teal).
6. Match transitions to the concept: camera-move push-throughs for a dream loop, hard cuts on dance accents for joy, hard-cut cards for a thriller.
7. Title sequences end with a quiet decay; trailers end with a loud build, then a quiet dialogue button, then the title.
8. End card: black, logo in a light bloom (~0.8 s), tagline fade (0.4 s), hold ~0.8 s, fade out 0.8 s, total ~2.9 s, silent — let the show's music tail die under it.

## Recipe (real footage + HTML/GSAP, Hyperframes)

Stage: 1920×1080, background #000, letterbox bars as two black divs (2.39:1 → 140 px each; 2.2:1 → 104 px; 2.0:1 → 60 px). Film grain overlay (PNG noise, opacity 0.06, blend overlay).

Credit (sub-style A):
```css
.credit{font:400 27px/1 "Inter",sans-serif;color:#a9a9a9;letter-spacing:0}
.credit::before{content:"";display:block;height:1px;width:115%;background:#a9a9a9;margin-bottom:10px}
```
```js
tl.fromTo(".credit",{opacity:0},{opacity:1,duration:1.6,ease:"sine.inOut"})
  .to(".credit",{opacity:0,duration:0.7,ease:"sine.in"},"+=1.2");   // one credit every ~4.5 s
```
Push-through transition: `tl.to(A,{scale:5,duration:0.7,ease:"power3.in"}).fromTo(B,{scale:0.35,opacity:0},{scale:1,opacity:1,duration:0.9,ease:"power3.out"},"<0.35")` with the same transform-origin (the object you enter).

Credit (sub-style B): Montserrat 500 uppercase, 20 px name / 13 px label, letter-spacing 0.35em / 0.45em, white, optional torn black box (420×210 px); fade 0.25 s, hold 1.5 s. Archive photos: `filter:grayscale(1) contrast(1.2)` + a colour layer with `mix-blend-mode:color` (#d99a2b, #c2185b, #2bb3b1, #d94f2a). Cut every 1.0 s, accelerate to 0.65 s.

Card (sub-style C): teal #5fa9a5 + paper texture + vignette; Bebas Neue / Anton uppercase with a grunge mask; 8-slice shred reveal 0.4 s (`ease:"steps(4)"`, random x offsets ±12 %), hold 0.7 s, hard cut out.

Type as matte (B title, C hook): set the word at 13–70 % of frame height and show footage inside it (SVG `<mask>` with `<text>`, or `background-clip:text` over a video poster sequence); swap words/languages every 0.9 s.

Apple-style end card:
```js
tl.fromTo(bloom,{opacity:0,scale:0.6,xPercent:-20},{opacity:1,scale:1.2,xPercent:20,duration:0.8,ease:"sine.inOut"})
  .to(bloom,{opacity:0,duration:0.4})
  .fromTo(tagline,{opacity:0},{opacity:1,duration:0.4},"<")
  .to(card,{opacity:0,duration:0.8},"+=0.8");
```
Logo white at 18 % of frame height, centred; tagline 2.5 % height, uppercase, letter-spacing 0.12em; bloom = `radial-gradient(circle, rgba(255,255,255,.9) 0%, rgba(255,255,255,0) 60%)`, `mix-blend-mode:screen`. No sound effect; fade the music to silence by the end of the card. (Use your own brand mark — never the Apple logo.)

Audio targets: title sequences −16 to −22 LUFS integrated (Severance very dynamic, Pachinko compressed); trailers about −15 LUFS with 1 s silence before the first hit and impacts on cards.

## Honest gaps
- I did not listen to the audio; music descriptions (Shapiro theme, "Let's Live for Today") come from known facts about these sequences, the shapes are measured.
- No Apple TV+ sonic logo exists in these three uploads (the end card is silent in all three); broadcast/in-app versions may differ.
- Font matches are visual guesses.
