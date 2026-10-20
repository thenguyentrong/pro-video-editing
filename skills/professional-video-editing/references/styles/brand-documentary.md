# Brand documentary
**Use it for:** a short documentary or documentary trailer paid for or presented by a brand, platform or company imprint: an activist or mission film (the brand's values shown through real people and archive), an athlete or adventure portrait, a nature or place documentary, a founder / community / tech-history mini-doc, a trailer for a doc series or feature doc. Length 1-25 min (trailers 1-2.5 min). **Not for:** a product launch (use `apple-precision.md`, `startup-launch.md`, `tech-launch-loud.md`), a 30-60 s feeling-only ad with no real story (use `cinematic-brand-anthem.md`), a news explainer built on evidence (use `editorial-explainer.md` + `documentary-evidence.md`), a vertical stunt clip (use `social-vertical.md`).

**Reference films:**
Patagonia — What's Next? (2023, 2:00) — patagonia/whats-next
Patagonia Films — The High Life (2023, 15:30, first 5 min measured) — patagonia/the-high-life
Patagonia Australia — Too Old Not To (2026, 6:35, first 5 min measured) — patagonia/too-old-not-to
National Geographic — Africa: Earth's Wild Home, trailer (2026, 1:13) — national-geographic/africa-earths-wild-home-trailer
National Geographic Documentary Films — Ghost Elephants, trailer (2026, 2:13) — national-geographic/ghost-elephants-trailer
National Geographic Short Film Showcase — Return of the Sun (2018, 3:45) — national-geographic/forty-days-darkness
Red Bull Media House — The Way of the Wildcard: the armed robber turned triathlete (2018, 13:46, first 5 min) — red-bull-media/armed-robber-triathlete
Red Bull Media House — The Way of the Wildcard: Mira Rai (2020, 15:59, first 5 min) — red-bull-media/mira-rai-trail-runner
Red Bull Snow — The Rise of Eileen Gu (2026, 13:38, first 5 min) — red-bull-media/rise-of-eileen-gu
Netflix — Our Planet II, trailer (2023, 1:24) — netflix-docs/our-planet-ii-trailer
Netflix — Formula 1: Drive to Survive S8, trailer (2026, 1:54) — netflix-docs/drive-to-survive-s8-trailer
Netflix — Rafa, trailer (2026, 2:27) — netflix-docs/rafa-trailer
Stripe Press — We Are As Gods, trailer (2021, 2:21) — stripe-press/we-are-as-gods
Stripe Press — The Street Network (2022, 21:29, first 5 min) — stripe-press/street-network
Stripe Press — The Big Score, book micro-doc (2021, 1:00) — stripe-press/big-score

## Signature
The brand is almost invisible. A tiny "presents" credit, a "Films" label, a monogram or a logo placed inside the first landscape; never a product shot. The film belongs to a real person, place or cause, and the brand borrows their credibility. It opens small and real (one locked take, home video, a talk-to-camera, a quiet wide after 2-4 s of silence), shows the hardest or biggest fact early as raw proof (archive in a window on black, headlines, a scan, a protest), and waits before the title (13-80 s in films, the last 5-10 % in trailers). Interviews are lit low-key in the subject's own place and held 6-18 s with real pauses. Archive keeps its own look and is framed as an object (a window on black, a print on paper, a viewfinder frame, a feed on a monitor); the present is shot like cinema. Each film adds one strong device (a black-and-white reconstruction, a hand-lettered type system, a viewfinder frame, an aged-paper world). Type is quiet: spaced thin caps, classical serif caps, condensed tags, subtitles as design.

## Numbers
Measured with `analyze_video.py` (adaptive detector, cuts checked on before/after pairs); long films on the first 300 s only; trailers without channel end screens. ≈ = eyeballed from frames.

| Metric | Range | Where it comes from |
|---|---|---|
| ASL, doc trailers | 1.12-1.99 s (median 0.92-1.58) | Africa 1.17, DTS 1.12, Ghost Elephants 1.37, Rafa 1.43, Our Planet II 1.82, We Are As Gods 1.99 |
| ASL, activist brand film (2 min) | 1.45 s (median 1.33) | Patagonia What's Next |
| ASL, athlete / portrait docs (first 5 min) | 2.27-2.65 s (median 1.14-2.08) | Armed Robber 2.27, Too Old Not To 2.31, Mira Rai 2.54, Eileen Gu 2.65 |
| ASL, place / observational docs | 3.90-4.76 s (median 2.59-4.08) | Street Network 3.90, Return of the Sun 4.40, High Life 4.76 |
| ASL, 60 s interview micro-doc | 6.03 s | Big Score |
| % shots under 1 s | trailers 6.5-56.5 %; portrait docs 18.5-42 %; place docs 2-17 % | metrics |
| % shots over 3 s | trailers 1-15.5 %; portrait docs 24-32 %; place docs 42-76.5 % | metrics |
| Trailer acceleration | last-quarter ASL 0.92-0.95 s (Africa, Ghost Elephants); last 10 s at 0.33-0.4 s; or slower last quarter 1.9-4.2 s when a held final image + title close it (Rafa, Our Planet II) | metrics |
| Cold open | 12.9 s locked take (Mira Rai); 11 cuts in 10 s incl. 0.12 s flashes (Armed Robber); talk-to-camera 13 s (Eileen Gu); home video 8.4 s (Rafa); 8 s texture shot (Ghost Elephants); 2-4.6 s silence or black first (High Life, Street Network, We Are As Gods, Return of the Sun) | notes |
| Flash / contrast burst | 5 shots of 0.38-0.5 s at 86-88 % (What's Next); 7-10 shots of 0.16-0.25 s (Rafa, DTS); 20-25 cuts in 10 s at 0.2-0.5 s (Armed Robber); 16 cuts in 10 s (Eileen Gu) | metrics |
| Title position (films) | 13 s (Too Old Not To), 19-27 s (Armed Robber), 43.5 s (Street Network), 46 s (Mira Rai), 80 s (High Life); Return of the Sun 11 s, small | notes |
| Interview holds | 6-7.3 s (Wildcard, Rafa confession 7.0); 8.9-12.2 s (High Life); 11.9-12.8 s (Eileen Gu); 15-18 s (Street Network, Big Score) | metrics |
| Longest hero hold | 11.7 s sun (Return of the Sun); 14.1 s glacier aerial (High Life); 10.3 s helmet close-up (Eileen Gu); 8.0 s water texture (Ghost Elephants) | metrics |
| Text sizes (cap height, % of frame height) | presents/credit 1.6-2 %, tracking 0.1-0.3 em; subtitles 2.5-3.5 %; name tags 3-4.5 % + role 2.2-2.8 %; context cards 2-3.2 %; cards on footage 4.5-6.5 %; auteur title ≈8 %; series logo 7-11 % | frames |
| Card count | 0-2 cards per people trailer (2-4 words, 0.9-2 s); 2-4 credit cards per nature trailer (brand, narrator, director, laurels); context cards in films 1-2, 6-8 s | notes |
| Letterbox | 2.35:1 in Mira Rai and Return of the Sun; 16:9 elsewhere | cropdetect |
| Black and silence | black holds 1.8-6.7 s as chapter breaks; near-silences 8-11 s at -40...-48 dBFS; 0.3-1 s pauses kept in speech; 0.75-1 s drop to -43...-54 dB before a key line; 2.2-3.1 s digital silence after a trailer title | metrics |
| Loudness | short docs -15.0 to -22.7 LUFS (Wildcard -22.2/-22.7, High Life -19.7, Too Old Not To -16.3, Return of the Sun -16.6, Eileen Gu -15.0); trailers -14.4 to -19.2; activist anthem -9.7 (TP +2, do not copy) | metrics |
| Cut-on-onset | 23-24 % vs 11-20 % chance in nature trailers (beat-cut); ≈ chance in people films (cut on speech) | metrics |

## Structure
**Short brand doc (5-20 min).**
1. **Cold open (0-5 %).** One patient real moment (a 13 s locked take, a talk-to-camera) or a 10 s jolt of flashes; then the hardest fact as raw archive (6-10 s).
2. **Credit + promise (5-15 %).** Tiny "presents" credit over movement; a 10-12 s promise montage at 8-9 cuts per 10 s; a 3 s black; title on one long landscape or drone shot (4-8 s); episode card.
3. **Chapter 1 (15-45 %).** First interview 7-18 s with pauses; cutaways 2-4 s; subtitles; lower thirds without a box.
4. **Chapter break.** 8-11 s near-silence on a landscape, a 3-7 s black hold, or serif context cards on black (6-8 s).
5. **Chapter 2-3 (45-90 %).** Backstory with family, archive evidence and one stylised device (reconstruction, hand-drawn map, archive prints); a contrast montage of 16-25 cuts per 10 s if the story has a "before" life.
6. **Ending (90-100 %).** The person today, one held image, small logo.

**Doc trailer (70-150 s).** Texture or intimate open 8 s (≈6 %) → brand / laurel / credit cards → world 10-15 s → flash burst (≈17 %) → confession or hero hold 7 s (≈27 %) → story → 1-2 cards or credit cards (≈60-75 %) → acceleration to 0.33-0.9 s → held final image (≈90 %) → title 3-6 s → date / sponsor card 2-3 s → logo, or 3 s black silence.

**Activist brand film (2 min).** Archive open with logo (0-4 %) → sport/joy (4-16 %) → protest turn inside the montage (16-25 %) → both together (25-56 %) → joy montage with one 5-shot burst (56-90 %) → quiet decision: handwriting, 0.9 s drop, the founder's face (90-95 %) → end line + logo on a 6 s nature shot.

## Picture
- **Present day = cinema.** Natural light, shallow focus, warm interiors with window light; 2.35:1 for the most cinematic films. Interviews in the subject's own place (kitchen, sofa, room with their kit), off-centre, 3/4 profile; confessions very tight and low-key.
- **Archive = record.** Keep its own look (16 mm, 4:3 TV, webcam, black and white) and frame it as an object: a 4:3 window on black (56 % of frame width, full picture height), a small square print on black (≈30 % H), a photo with rounded borders on aged paper, a viewfinder frame with corner ticks, a feed revealed on a monitor in a room, tabloid headlines filmed in macro.
- **Proof as images:** MRI or X-ray, mugshots, CCTV, bleached skulls, banners, handwriting, medals in a jar.
- **One stylised device per film:** black-and-white theatrical reconstruction with dissolve chains showing time passing; red-lit reconstruction; hand-lettered type and maps; an aged-paper collage world.
- **Nature:** hero shots 1-2 s in trailers (macro eyes, top-down aerials of mass movement, underwater, one predator chase); in short films 4-12 s holds, cold world with one warm colour for the story's symbol.
- **Athlete:** low feet POV, tracking from behind, drone over the route, selfie/helmet cameras, white fog as a near-blank frame with one dark figure.
- **Brand presence:** a credit line, a "Films" label on black, a monogram, a festival-style laurel, or the logo placed inside the first landscape. No product shot.

## Type
- **Credit / presents:** small spaced caps, cap 1.6-2 % H, tracking 0.1-0.3 em, centred (free: Montserrat 500 / IBM Plex Mono 400); optional italic serif eyebrow "a film by" ≈1.3 % H.
- **Series / film logo:** heavy rounded slab caps ≈9 % H (free: Bowlby One / Archivo Black), condensed caps ≈7 % H (Oswald 600 / Bebas Neue), bold sentence-case sans ≈5 % H (Nunito Sans 800), or spaced classical serif caps ≈8 % H (Cormorant Garamond 500 / Cinzel).
- **Blue-chip nature cards:** warm gold bevel caps ≈6.5 % H (`linear-gradient(#ffe08a,#c98a1e)` clipped to text) with a white spaced eyebrow ≈2.8 % H; or thin white caps ≈6 % H on landscapes (Montserrat 300).
- **Cards on black (people):** small line ≈1.5 % H over a big word ≈4 % H, very wide tracking (0.5 / 0.8 em), warm grey classical caps.
- **Context cards:** book serif ≈3.2 % H (Source Serif 4) or small sans ≈2 % H, 2-3 lines, 6-8 s on black.
- **Name tags:** bold condensed 3-4.5 % H + role 2.2-2.8 % H, no box, beside the speaker; optional skewed colour ribbons.
- **Hand-made system (portrait):** hand-lettered caps for title (≈6 % H), maps and kinetic words (≈4 % H, 1-3 words per beat) (free: Permanent Marker / Caveat Brush, Caveat for a signature).
- **Subtitles:** white sans with a soft shadow, 2.5-3.5 % H, bottom centre or in the lower letterbox bar, on every non-English line.
- **Activist end line:** bold sans + italic serif in one line (≈4.5 % H), left at x ≈25 %, typed on and erased into the logo.

## Transitions
- Hard cuts almost everywhere; movement lives inside the shot (slow push over a photo, a magnifier across a page, drone drift).
- Black: dips of 0.3-1.8 s between trailer sections; holds of 3-7 s as film chapter breaks; 3 s black after a trailer title.
- Dissolve chains only inside a reconstruction (time passing on a locked frame).
- One stylised move per film at most: a 3D ring wipe or 3D letters into the title, a white flash into a packshot, a viewfinder scale-in, a light-bar wipe into the platform logo.

## Sound
- Real sound first: room tone, breath, wind, family voices, speech in the original language with subtitles. Music low under interviews.
- Start in silence or near-silence (2-4.6 s), or with ambience at about -20...-30 dBFS.
- Keep real pauses in speech (0.3-1 s); use 8-11 s near-silences and 3-4 s silences in reconstructions as chapter breaks.
- Before a key line, a date card or a title: a 0.75-1 s drop to about -45...-54 dB.
- Trailers build from -21 to -11 dBFS RMS into the title, then cut to silence or fade under the sponsor card.
- Masters: quiet docs -20 to -23 LUFS (LRA 8-12 LU); music-led docs and trailers -15 to -17; true peak at or below -1 dBTP (two reference films clip at +1.8 and +2.0).

## Do / Don't
- Do let the person, place or cause carry the film; keep the brand to a credit, a label or a mark inside the first shot.
- Do show the hardest fact early as raw archive or an object, before any explanation.
- Do hold interviews 6-18 s in the subject's own place and leave real pauses in.
- Do keep archive in its own look and frame it as an object.
- Do pick one stylised device and use it for the hardest part of the story.
- Do subtitle every non-English line, cleanly, as part of the design.
- Do put credit cards (brand, narrator, director) on the most graphic shots.
- Don't show a product, price or feature list.
- Don't drive a people documentary with beat cutting; cut on speech (only nature trailers cut on the beat).
- Don't add explanatory text where a real banner, headline, handwriting or document can say it.
- Don't over-grade archive or upscale it to look new.
- Don't master a doc as hot as an ad (-9.7 LUFS / +2 dBTP clips after encoding).
- Don't invent press quotes or laurels; use only real ones.
- Don't name or show private people without consent; use public figures and consenting subjects.

## Recipe
Hyperframes, 1920x1080; real footage you own or licence; HTML/GSAP only for type, frames and cards.
1. **Brief.** One person, place or cause, one sentence of change. List the proof you have (archive, objects, documents) and choose one stylised device.
2. **Shoot or source.** Interviews in the subject's place (window key, medium + tight), action, landscapes, details, a drone shot for the title. Stock queries: `16mm film surfing 1970s`, `protest march banner crowd`, `mountain hut glacier drone`, `runner mountain road drone snow`, `trail runner feet dirt trail low angle`, `open water swimmer drone top down`, `aerial wildebeest migration`, `sea turtle hatchling macro`, `arctic village snow storm`, `newspaper headline close up`, `old paper texture`, `studio interview black background portrait`.
3. **Open.** 2-4 s silence, then one 9-13 s take with ambience; or a 10 s jolt of 10-11 cuts with 3-frame flashes.
4. **Archive window.** `.arch{position:absolute;left:22%;top:12.5%;width:56%;aspect-ratio:4/3;background:#000}`; 6-8 flashes of 0.5-1.5 s against today's face. Or prints on black: `width:22vh;height:22vh;border-radius:1vh`, 3-4.5 s.
5. **Credit.** `.credit{font:500 1.7vh Montserrat;letter-spacing:.3em;text-transform:uppercase;color:#fff}` fade 0.5 s over movement.
6. **Title on one drone shot (4-8 s).** `font:400 9vh "Bowlby One"` (or `600 7vh Oswald`, or `500 8vh "Cormorant Garamond"; letter-spacing:.25em`), `opacity 0→1, y 10→0` 0.6 s; episode line `300 2vh Montserrat; letter-spacing:.4em`.
7. **Body.** Interviews 6-18 s, cutaways 2-4 s, ASL 2.3-4.8 s by register. Name tag `700 3vh "Roboto Condensed"` + `400 2.2vh Roboto`. Subtitles `500 3vh Inter; text-shadow:0 1px 4px rgba(0,0,0,.6); bottom:6%`.
8. **Device.** Reconstruction: locked black-and-white frame, 3-4 takes layered with 1.5 s crossfades, level under -30 dBFS. Viewfinder: clip scales 100 → 76 % in 0.5 s onto `#f7f7f7` with corner ticks and a `700 1.8vh` location tag. Hand-made: `Permanent Marker` words 1-3 per beat on the spoken word.
9. **Chapter break.** 8-11 s landscape at about -42 dBFS, or 2 context cards `400 3.2vh "Source Serif 4"`, 6-8 s each.
10. **End.** One held image 6 s, small logo (SVG `stroke-dashoffset` draw 1 s), fade to black 1-2 s.
```js
// archive flashes against the present
flashes.forEach((f,i)=>tl.set(f,{autoAlpha:1},t+i*0.9).set(f,{autoAlpha:0},t+i*0.9+0.6));
// reconstruction: ghosted takes on a locked frame
takes.forEach((k,i)=>tl.fromTo(k,{opacity:0},{opacity:1,duration:1.5,ease:"none"},t2+i*5));
// viewfinder insert
tl.fromTo(".vf-clip",{scale:1},{scale:.76,duration:.5,ease:"power2.inOut"},t3).from(".vf-ui",{opacity:0,duration:.3},t3+.3);
```

## Variants
- **Activist brand doc (Patagonia What's Next).** 2 min, ASL 1.45 s, archive 16 mm + modern; logo centred at 0.9-3 s; protest turn at ≈16 % with real banners as the only text; one 5-shot burst at 86-88 %; quiet decision beat (handwriting, 0.9 s drop, founder's face); bold-sans + italic-serif end line. Master -12 to -14 LUFS, not the original -9.7.
- **Place doc (Patagonia High Life, National Geographic Return of the Sun).** ASL 4.4-4.8 s, median ≈4 s, 64-76.5 % of shots over 3 s, first cut after 9 s, credits on black, title at 11-80 s, one 11.7-14.1 s hero hold, subtitles, one context card. -16.6 to -19.7 LUFS.
- **Nature doc trailer (National Geographic Africa, Netflix Our Planet II).** Hero shots 0.33-2.4 s, ASL 1.17-1.82 s; logo inside the first aerial; credit cards on the most graphic shots (gold caps ≈6.5 % H) or 2 thin-caps cards (6 % H); habitat sequence; 3D title (ring or letters onto a satellite map); sponsor or date card. -14.4 to -19.2 LUFS.
- **Auteur expedition trailer (National Geographic Ghost Elephants).** 8 s texture open, logo + laurels on black, archive prints on black, director credits on a night sky, spaced serif caps for everything, quarter ASL 2.21 → 0.92 s, title on a monochrome plate, 3.1 s black silence. -16.6 LUFS.
- **Athlete / adventure doc (Red Bull Wildcard, Eileen Gu, Patagonia Too Old Not To).** ASL 2.27-2.65 s; cold open (jolt, patient take or talk-to-camera); "presents" credit; slab-caps series logo on a drone shot; archive as evidence; one device (reconstruction, archive window, viewfinder, hand-lettering); interviews 6-13 s; a 16-25 cut contrast montage. -15 to -22.7 LUFS.
- **Athlete doc trailer (Netflix Rafa, Drive to Survive).** ASL 1.12-1.43 s; intimate open; flash burst of 0.16-0.25 s shots; a 7 s confession with a 1 s drop; 0-2 cards on black; held final image; title in the show's world, date on the platform's light bars. -14.7 to -15.1 LUFS.
- **Founder / company mini-doc (Stripe Press).** Publisher mark only. Archive trailer: aged-paper world, photos as framed objects, magnifier over documents, ASL 2 s, small serif title at the end, -21.4 LUFS. Observational short: silent open, place tag on colour ribbons, first interview 17.7 s, title at 43.5 s, serif context cards 8 s, explainer graphic 21.6 s, ASL 3.9 s, -22.2 LUFS. 60 s promo: one remote interview (pull back to reveal it on a monitor), two inserts, a flat brand-colour packshot card, ASL 6 s.
