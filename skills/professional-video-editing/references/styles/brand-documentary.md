# Brand documentary
**Use it for:** a short documentary or documentary trailer paid for by a brand, platform or company imprint: an activist or mission film (the brand's values shown through real people and archive), an athlete or adventure portrait, a nature or place documentary, a founder / community / tech-history mini-doc, a trailer for a doc series. Length 1-25 min (trailers 1.5-2.5 min). **Not for:** a product launch (use `apple-precision.md`, `startup-launch.md`, `tech-launch-loud.md`), a 30-60 s feeling-only ad with no real story (use `cinematic-brand-anthem.md`), a news explainer built on evidence (use `editorial-explainer.md` + `documentary-evidence.md`), a vertical stunt clip (use `social-vertical.md`).

**Reference films:**
Patagonia — What's Next? (2023, 2:00) — patagonia/whats-next
Red Bull Media House — The Way of the Wildcard: Mira Rai (2020, 15:59, first 5 min measured) — red-bull-media/mira-rai-trail-runner
Netflix — Our Planet II, official trailer (2023, 1:24) — netflix-docs/our-planet-ii-trailer
Netflix — Formula 1: Drive to Survive S8, official trailer (2026, 1:54) — netflix-docs/drive-to-survive-s8-trailer
Netflix — Rafa, official trailer (2026, 2:27) — netflix-docs/rafa-trailer
Stripe Press — We Are As Gods, trailer (2021, 2:21) — stripe-press/we-are-as-gods
Stripe Press — The Street Network (2022, 21:29, first 5 min measured) — stripe-press/street-network
Stripe Press — The Big Score, book micro-doc (2021, 1:00) — stripe-press/big-score

## Signature
The brand is almost invisible. A small "presents" credit or a monogram, maybe a logo at the very end, never a product shot. The film belongs to a real person, a place or a cause, and the brand borrows their credibility. It opens small and real (one locked take, home video, a quiet wide with silence), shows the hardest or biggest fact early as raw proof (archive window, a scan, a protest), and waits before the title (8-45 s in films, at the end in trailers). Interviews are lit low-key and held long, with real pauses left in. Archive is kept in its own look and framed as an object (a small window on black, a photo on paper, a webcam on a monitor), while the present is shot like cinema (2.35:1, shallow focus, natural light). Typography is quiet and editorial: wide-tracked thin caps, small serif cards, condensed name tags, subtitles as part of the design.

## Numbers
Measured with `analyze_video.py` (adaptive detector, cuts checked on before/after pairs); long films on the first 300 s only; trailers without the YouTube end screen. ≈ = eyeballed from frames.

| Metric | Range | Where it comes from |
|---|---|---|
| ASL, activist brand film (archive montage) | 1.45 s (median 1.33) | Patagonia What's Next |
| ASL, doc series trailers | 1.12-1.82 s (median 1.00-1.15) | Drive to Survive 1.12, Rafa 1.43, Our Planet II 1.82 (footage only 1.47) |
| ASL, documentary trailer from archive | 1.99 s (median 1.58) | We Are As Gods |
| ASL, athlete short doc (first 5 min) | 2.54 s (median 2.08) | Mira Rai |
| ASL, observational short doc (first 5 min) | 3.90 s (median 2.59); first quarter 12.5 s | Street Network |
| ASL, 60 s interview micro-doc | 6.03 s (median 5.23) | Big Score |
| % shots under 1 s | 6.5-46 % | nature trailer 6.5, doc 17-20, Patagonia 23, Rafa 42, DTS 46 |
| % shots over 3 s | 1-42 % | trailers 1-5, Patagonia 1, archive trailer 15.5, athlete doc 25, observational doc 42 |
| Cold open (before any title) | one locked take 12.9 s (Mira Rai); home video 8.4 s (Rafa); 1.75-4 s silence on a wide (Street Network, We Are As Gods) | notes |
| Flash burst | 5 shots of 0.38-0.5 s at 86-88 % of runtime (Patagonia); 7-10 shots of 0.16-0.25 s (Rafa trophies, DTS slates); archive flashes 0.5-1.5 s (Mira Rai) | metrics |
| Title position | at 3-4 % of runtime (Patagonia logo at 0.9 s), 15 % (Mira Rai 46 s of 300+), 14 % of first 5 min (Street Network 43.5 s); trailers 90-95 % of runtime | notes |
| Interview holds | 6.2-7.3 s (Mira Rai), 7.0 s confession (Rafa), 9.7-17.7 s (Street Network, Big Score) | metrics |
| Text sizes (cap height, % of frame height) | presents/credit 1.6-1.7 %, tracking 0.1-0.3 em; episode/subtitle lines 2-2.5 %; name tag 3-4.5 % + role 2.2-2.8 %; subtitles 2.8-3.5 %; serif context cards 3.2 %; cards on footage 4.5-6 %; series logo 7-9 % | frames |
| Card count | 0-2 cards per trailer, 2-4 words each, 0.9-2.0 s; context cards in films 8 s, 2-3 lines | notes |
| Letterbox | 2.35:1 for the present-day athlete doc; 16:9 for the rest | cropdetect |
| Loudness | short docs -21.4 to -22.2 LUFS (LRA 5-12); trailers -14.4 to -15.1; activist anthem -9.7 (hot, true peak +2 dBTP, do not copy) | metrics |
| Silences | 1.75-4 s silent open; 0.3-1 s pauses kept in interviews (9-21 per 5 min); 8-10 s near-silence (-40...-48 dBFS) as chapter breaks; 0.75-0.95 s drop to -50 dB before a key line or the date card | metrics |
| Cut-on-onset | 24 % vs 11 % chance (nature trailer, beat-cut); 29-39 % ≈ chance in all people films (cut on speech, not beats) | metrics |

## Structure
**Short brand doc (5-20 min).**
1. **Cold open (0-5 %).** One patient real moment (12-13 s locked take, or a quiet wide in silence), then 6-10 s of the hardest fact as raw archive.
2. **Credit + promise (5-15 %).** Small "presents" credit over movement; a 10-12 s promise montage at 8-9 cuts per 10 s; 3 s of black; title on one long landscape (8 s).
3. **Chapter 1 (15-45 %).** First interview 7-18 s with pauses; cutaways 2-4 s; lower thirds; subtitles.
4. **Chapter break.** 8-10 s near-silence on a landscape, or serif context cards on black (8 s each).
5. **Chapter 2-3 (45-90 %).** Childhood / backstory with family interviews, objects, one stylised reconstruction (red light, silhouette); pace 2-4 cuts per 10 s.
6. **Ending (90-100 %).** The person today, one held image, small logo.

**Doc trailer (85-150 s).** Intimate open 8 s (≈6 %) → world 10-15 s → flash burst 3-4 s (≈17 %) → confession 7 s (≈27 %) → mid brand sting or card → story → card (≈63 %) → glory → card (≈72 %) → climax → final image 6 s (≈90 %) → title 2-10 s → date 2-3 s → logo 3 s.

**Activist brand film (2 min).** Archive open with logo (0-4 %) → sport/joy (4-16 %) → protest turn inside the montage (16-25 %) → both together (25-56 %) → joy montage with one 5-shot burst (56-90 %) → quiet decision: a handwritten line, 0.9 s drop, the founder's face (90-95 %) → end line + logo on a 6 s nature shot.

## Picture
- **Present day = cinema.** Natural light, shallow focus, warm interiors with window light; 2.35:1 for athlete films. Interviews off-centre with the real environment behind (kit, bookshelves, home); confessions very tight and low-key (half the face in shadow).
- **Archive = record.** Keep its own look (16 mm fade, 4:3 TV video, webcam, black and white) and frame it as an object: a 4:3 window on black (56 % of frame width, full picture height), a photo with rounded borders and a shadow on aged paper, a feed revealed on a monitor in a room. Never upscale-and-grade archive to look new.
- **Proof of pain or stakes** as images, not words: an MRI or X-ray, taped hands, a protest banner, a slogan spelled with kayaks, real handwriting.
- **Nature:** hero shots only, 1-2 s each: macro eyes, top-down aerials of mass movement (beach, herd, colony), underwater, one predator chase. Mass-movement aerials carry the idea of "journey".
- **Athlete:** low feet POV on trails, tracking from behind, drone over terraces, selfie-camera clips by the athlete, a race start at dawn.
- **Brand presence:** a credit line, a monogram on a flat brand colour or paper, a corner wordmark on trailers, a logo on the last shot. No product shot.

## Type
- **Credit / presents:** small wide-tracked caps, cap 1.6-1.7 % H, tracking 0.1-0.3 em, centred. Free: Montserrat 500 or IBM Plex Mono 400.
- **Series / film logo:** heavy rounded slab caps ≈9 % H (free: Bowlby One / Archivo Black) or condensed caps ≈7 % H (free: Oswald 600 / Bebas Neue) over one long aerial; episode line in light very wide-tracked caps 2-2.5 %.
- **Cards on footage (nature):** thin geometric caps, cap ≈6 % H, tracking ≈0.15 em, centred in empty sky or rock (free: Montserrat 300). Fade 0.3 s, hold 1 s.
- **Cards on black (people):** small line ≈1.5 % H over a big word ≈4 % H, both very wide-tracked (0.5 / 0.8 em), warm grey, classical caps (free: Cinzel 400 / Cormorant SC). Hold 1.9-2.0 s.
- **Context and definition cards:** book serif ≈3.2 % H, 2-3 lines, white on black or blurred footage (free: Source Serif 4 / Libre Caslon Text). Hold ≈8 s.
- **Name tags:** bold condensed name 3-4.5 % H + role 2.2-2.8 % H, no box, beside the speaker inside the picture (free: Roboto Condensed 700 / Oswald 600). Optional: two skewed ribbons in the place's colours behind the text.
- **Subtitles:** white sans with a soft shadow, 2.8-3.5 % H, bottom centre (or in the lower letterbox bar), on every non-English line. They are part of the design, not an add-on.
- **End line (activist):** bold sans + italic serif in one line at the same size (≈4.5 % H), left-aligned at x ≈25 %; type on per letter, hold 2 s, erase from the right; a glyph of the logo stays and the logo builds around it (free: Inter 800 + Newsreader Italic).

## Transitions
- Hard cuts almost everywhere. Movement lives inside the shot (slow push over a photo, magnifier across a page, drone drift).
- Black: 3.3 s black hold before an archive line (Mira Rai); 0.3-0.5 s dips to black as act breaks in trailers.
- Fades only for type and for the very start and end.
- One stylised move per film at most: a 3D ring wipe into the title (Our Planet II), a white flash into the packshot (Big Score), a light-bar wipe into the platform logo.

## Sound
- Real sound first: room tone, breath, family voices, speech in the original language with subtitles. Music low under interviews.
- Start in silence or near-silence (1.75-4 s at about -50 dBFS, or room tone at -20 dBFS).
- Keep real pauses in speech (0.3-1 s); use 8-10 s near-silences (-40...-48 dBFS) as chapter breaks.
- Before the key line or the date card: a 0.75-0.95 s drop to about -50 dB.
- Music peaks under context cards or the montage (about -16 dBFS RMS), never under the confession.
- Masters: short docs -18 to -22 LUFS (LRA 5-12 LU); trailers -14 to -15 LUFS; true peak at or below -1 dBTP.

## Do / Don't
- Do let the person, place or cause carry the film; keep the brand to a credit and a last-shot logo.
- Do show the hardest fact early as raw archive or an object, before any explanation.
- Do hold interviews 7-18 s and leave real pauses in.
- Do keep archive in its own look and frame it as an object.
- Do subtitle every non-English line, cleanly, as part of the design.
- Do put the activist turn inside the montage, not on a slogan card.
- Don't show a product, price or feature list.
- Don't drive a people documentary with beat cutting; cut on speech (only nature trailers cut on the beat).
- Don't add explanatory text where a real banner, handwriting or document can say it.
- Don't over-grade archive or upscale it to look like new footage.
- Don't master a doc as hot as an ad (-9.7 LUFS with +2 dBTP clips after encoding).
- Don't name or show private people without consent; use public figures and consenting subjects.

## Recipe
Hyperframes, 1920x1080; real footage you own or licence. HTML/GSAP only for type and frames.
1. **Brief.** One person or one cause, one sentence of change. List the proof you have (archive, objects, documents).
2. **Shoot or source.** Present day: interviews in the subject's own place (key light from a window, 2 set-ups: medium + tight), action, landscapes, details. Archive: ask the subject for photos and video. Stock queries: `16mm film surfing 1970s`, `protest march banner crowd`, `himalaya terraces drone`, `trail runner feet dirt trail low angle`, `aerial wildebeest migration`, `sea turtle hatchling macro`, `old paper texture`, `magnifying glass old book`, `studio interview black background portrait`.
3. **Open.** One 12-13 s locked shot with room tone; or 2-4 s silence on a wide with the credit.
4. **Archive window.** `.arch{position:absolute;left:22%;top:12.5%;width:56%;aspect-ratio:4/3;background:#000}` on a black stage; 6-8 flashes of 0.5-1.5 s cut against today's face.
5. **Credit.** `.credit{font:500 1.7vh Montserrat;letter-spacing:.3em;text-transform:uppercase;color:#fff}` fade 0.5 s over movement.
6. **Title on one aerial (8 s).** `font:400 9vh "Bowlby One"` (or `600 7vh Oswald`), `opacity 0→1, y 10→0` 0.6 s; episode line `300 2vh Montserrat; letter-spacing:.4em`; crossfade 0.5 s.
7. **Body.** Interviews 7-18 s, cutaways 2-4 s, ASL 2.5-4 s. Name tag `700 3vh "Roboto Condensed"` + `400 2.2vh Roboto`, fade 0.4 s, hold 4 s. Subtitles `500 3vh Inter; text-shadow:0 1px 4px rgba(0,0,0,.6); bottom:6%`.
8. **Chapter break.** 8-10 s landscape with ambience at about -42 dBFS, or 2 serif cards `400 3.2vh "Source Serif 4"; line-height:1.35; max-width:40%`, 8 s each.
9. **Letterbox (optional).** Picture 1920x818 centred; subtitles in the lower bar.
10. **End.** One held image 6 s, small logo or monogram (SVG `stroke-dashoffset` draw 1 s), fade to black 1-2 s.
```js
// archive flashes against the present
flashes.forEach((f,i)=>tl.set(f,{autoAlpha:1},t+i*0.9).set(f,{autoAlpha:0},t+i*0.9+0.6));
// slow push on a photo on paper
tl.fromTo(".photo",{scale:1,x:"30%"},{x:0,duration:.8,ease:"power2.out"},t2)
  .to(".photo",{scale:1.04,duration:4,ease:"none"},t2+.8);
```

## Variants
- **Activist brand doc (Patagonia).** 2 min, 83 shots, ASL 1.45 s, archive 16 mm + modern; logo centred at 0.9-3 s, cap ≈4 % H; protest turn at ≈16 % of runtime with real banners as the only text; joy montage with one 5-shot burst of 0.38-0.5 s at 86-88 %; quiet decision beat (handwriting, 0.9 s drop to -33 dBFS, founder's face); end line bold sans + italic serif on a 6 s cloud shot. Master -12 to -14 LUFS, not the original -9.7.
- **Nature doc (trailer form, Netflix Our Planet II).** Hero shots 1-2.4 s, no shot under 0.8 s, cut every 2 beats (1.04 s) in the last 10 s; two thin-caps cards on landscapes (6 % H, 1 s); one predator payoff; title from a glowing ring. -14.4 LUFS. A full-length nature short doc was not measured in this round; slow the body to 3-6 s shots and add narration before using it for a film.
- **Athlete / adventure doc (Red Bull Wildcard, Netflix Rafa / Drive to Survive).** Film: 2.35:1, 13 s cold open, window-boxed archive of the past, "presents" credit, promise montage at 9 cuts per 10 s, title at 46 s on an aerial, ASL 2.5 s, interviews 6-7 s, subtitles, near-silent chapter breaks, -22 LUFS. Trailer: ASL 1.1-1.4 s, a flash burst of 0.16-0.25 s shots, a 7 s confession with a 1 s drop, two cards on black, a held final image, -14.7 to -15.1 LUFS.
- **Founder / company mini-doc (Stripe Press).** Publisher mark only. Archive trailer: aged-paper world, photos as framed objects, magnifier over documents, ASL 2 s, small serif title at the end, -21.4 LUFS. Observational short: silent open, place tag on colour ribbons, first interview 17.7 s, title at 43.5 s, serif context cards 8 s, explainer graphic 21.6 s, ASL 3.9 s, -22.2 LUFS. 60 s promo: one remote interview (pull back to reveal it on a monitor), two inserts, a flat brand-colour packshot card, ASL 6 s.
