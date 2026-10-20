---
name: professional-video-editing
description: Plan, source, cut, sound-design and finish videos the way professional editors at Apple, Marvel, Nike, the New York Times or the BBC do. Covers the full workflow (brief → story → style → footage → cut → sound → grade → text → QC → delivery), eighteen measured house styles (Apple precision, movie trailer, editorial explainer, social vertical, broadcast promo, brand anthem, industrial robotics demo, design-tech launch, startup launch, creator YouTube, place film, construction, deep-tech hardware, brand documentary and more), a team of role skills (director, style scout, script, image/footage/music selection, voice, sound, editor, QC), finding high-resolution licensed stock footage with an automatic quality gate, building films in code (HTML/GSAP via Hyperframes) and deciding when AI image/video generation is acceptable. Use this skill whenever the user wants to make, edit, cut, re-cut, review or improve any video, trailer, promo, ad, launch film, explainer, reel, TikTok, brag video, pitch video or title sequence, asks how a brand or studio edits, wants stock footage, or says a video looks cheap, amateur or "like AI", even if they don't say "editing".
---

# Professional video editing

A professional film is not "clips plus music". It is one clear point, told as a chain of beats, in one consistent visual language, cut to the music, with sound doing half the work and nothing on screen that the viewer would read as cheap, template-made or fake. This skill gives you the process and the measured numbers to get there.

Viewers judge in the first 2–3 seconds whether a film was made by people with taste. They don't count cuts; they notice when the rhythm, type, grade or sound is off, and they notice instantly when something "looks AI".

## The workflow (do it in this order)

1. **Brief.** Who watches, where (phone feed, cinema, jury, website), how long, which aspect ratio(s), what they should do after. Ask what material exists (their own footage, product, people).
2. **One sentence.** What should a stranger repeat after one viewing? Write it down. If you can't, you are not ready to cut.
3. **Argument chain.** Hook → tension/question → evidence → turn → payoff → call to action. Each beat causes the next ("so", "but", "that's why"). ~8 beats for 60 s. Voice budget ≈ 2.5 words/s.
4. **Pick ONE style** from the table below and read its file. Mixing two film languages is the fastest way to look cheap. (A trailer with a documentary-evidence middle is one language with a borrowed section, not two.)
5. **Script + shot plan before building.** For every beat: the shot, its source and licence, its length, and where text will sit in that frame. Show this to the user and let them choose music and voice before you render anything.
6. **Source real material** (`references/stock-sourcing.md`, `scripts/stock_find.mjs`): own footage first, then licensed 4K stock, then documents/screenshots as quotation. Generated imagery only under the rules in `references/generative-assets.md`.
7. **Selects: choose images and sound deliberately** (`references/selecting-images-and-sound.md`). 5–10 candidates per shot; run `scripts/select_media.py` with the crop that will really be on screen; look at the labelled sheet for meaning; map candidate tracks with `scripts/music_map.py`. The opener and end card get the best material. If nothing passes, get better material instead of lowering the bar.
8. **Music first, then cut.** Map the track (intro, build, drop-out, hit, outro), put the story's turn on the biggest musical moment, cut on beats or on action. Read `references/cutting-craft.md`.
9. **Sound design + mix** (`references/sound-and-mix.md`): room tone, music, one effect per meaningful cut, voice on top, one big hit; master to −14 LUFS unless the style file sets another target.
10. **Grade + texture:** one look for the whole film, matched exposure, light grain if the style uses it.
11. **Type and graphics** per the style file: one family, ≤ 2 weights, one accent colour, text placed in negative space.
12. **Build** in an editor or in code (`references/hyperframes-recipes.md`).
13. **QC** (`references/qc.md`): ten-frame test, story test, numbers vs the style, sound, safe zones, honesty.
14. **Deliver:** master + cutdowns (60/30/15/6 s) and ratios (16:9, 9:16, 4:5, 1:1) re-framed per ratio, not just cropped; poster as frame 0; licence log.

## The team (role skills and agents)
This skill is the shared knowledge base. The work can be split into roles, each a skill and an agent of the same name: `video-director` (runs the team and the gates), `video-style-scout` (inspiration + style), `video-script-writer`, `video-image-selector`, `video-footage-selector`, `video-music-selector`, `video-voice-producer`, `video-sound-designer`, `video-editor`, `video-qc-reviewer`. They hand work to each other through one project folder (`brief.md → style.md → script.md → selects/ + music.md + voice.md → sound.md → renders/ → qc.md`). For a small job, do the steps below yourself in the same order.

When there are options, deliver one version or three clearly different variations, not more.

## Choose the style

| Style file (`references/styles/`) | Use it for | Pace (ASL) | Signature |
|---|---|---|---|
| `apple-precision.md` | One product or feature, a calm confident claim; premium hardware (B&O, Leica, Sonos, Oura) | 1.1–2.3 s (premium films up to 2.5 s; vertical and keynote ≈4 s) | One idea per shot, small centred type, hard cuts, silent ending |
| `tech-launch-loud.md` | Big consumer launches, feature runs (DJI), dark engineering reveals, word-montage manifestos | 1.1–3.6 s (word montages 0.75–0.8 s) | Narrated chapters or feature runs, bold hero titles, mastered loud |
| `human-demo-warm.md` | A product shown through real people using it; warm brand docs and announcements | 1.3–3.8 s | A real person's moment solved by one feature, warm, one colour |
| `design-tech.md` | Design-led hardware, cars, objects | 1.6–7.1 s (most 2–4 s) | One world, one accent, tiny type, product withheld, long final hold |
| `movie-trailer.md` | Pitches, problem → solution stories, anything with stakes; teasers, main trailers, TV spots | 1.0–1.9 s (teasers 1.8–2.8 s) | Cold open, 4–6 cards, density peak middle-late, one measured silence, title near the end |
| `editorial-explainer.md` | Explaining news, data, a system, an argument | 2.2–5.2 s (business and data explainers up to 6.3 s; personal-map style 1.4–2.2 s) | Voice-led; every claim proven on screen; one accent colour |
| `documentary-evidence.md` | Showing headlines, studies, laws, numbers credibly | 2.2–5.2 s; proof held 6–28 s | Cropped document in light, one mark, source always on screen |
| `social-vertical.md` | TikTok / Reels / Shorts, 9:16 | memes 1.1–2.2 s; creator 1.0–4.3 s; podcast clips 7–9 s | Frame-1 hook, native look, few words, safe zones, loop |
| `broadcast-tv.md` | Title sequences, idents, channel promos, sports packages and season launches | 0.6–5.4 s (titles longer) | One brand look over all footage, one strict rule per format |
| `cinematic-brand-anthem.md` | Brand films, athletes, cars, heritage, quiet luxury | 0.8–1.3 s (car launches up to 2.3 s, luxury up to 2.6 s) | One visual device repeated faster, cut on the voice, silence, plain end card |
| `industrial-robotics.md` | Robots, machines, B2B industrial, startup demos | proof 4.3–7.1 s (some up to 11 s); spec films 1.2–4.2 s | Long real takes, labelled speed, machine's view first, datasheet specs |
| `startup-launch.md` | Software/app launches, feature films, founder announcements, launch-week sizzles | 1.15–5.6 s (feature films 3.1–5.5 s) | Real UI filmed like a product: one task, few words, silent logo |
| `creator-youtube.md` | Creator-led YouTube: tech review, vlog, challenge, animated or science explainer | 1.7–7.9 s (animated 10–14 s) | Story starts on frame 1; show the promise, then re-hook constantly |
| `place-film.md` | City reels, tourism campaigns, architecture/project films | 1.2–3.3 s (architecture 4–16 s) | A frame for the place; composed shots, little small text |
| `construction-aec.md` | Construction-tech launches, site case studies, megaproject docs, robot-on-site demos | launch 1.7–2.3 s; case 2.5–5.2 s | Real site, crew in PPE, person for scale, named voices, drone reveal |
| `deeptech-hardware.md` | Defense, aerospace, drone and autonomy reveals, manifestos, field tests | 1.05–4.17 s | Real UI, human in the loop, named facts; the proof take is longest |
| `brand-documentary.md` | Short docs paid for by a brand: activist/mission film, athlete or adventure portrait, nature doc, founder mini-doc | ≈1.1–2.0 s trailers; longer takes in the film | The brand is almost invisible; the film belongs to a real person, place or cause |
| `opening-credits.md` | Places, teams, events, recaps, brag reels | 3.25 s (measured, metronome-even) | Composed shots, small two-line credits in empty space, 2.39:1, one song |

Exact numbers (shot lengths, type sizes, hold times, loudness, silences) live in each style file and in `references/measured-numbers.md`. Use them to set timings instead of guessing. Each style file lists its reference films by title (search for them on the brand's official channel) with an internal research id (`company/example`); numbers marked ≈ were judged by eye.

## What makes a film look cheap (avoid unless the style file says otherwise)

- Drawn/vector characters or AI images standing in for real products, people or places.
- Text on every shot, centred, in heavy black-weight caps, with drop shadows or rounded caption pills.
- Highlighter boxes, emoji, neon glow, gradient backgrounds, stock "tech" particles, fake HUDs.
- Ken Burns on every still, flash frames, glitch transitions, whip pans as a habit.
- Full web pages shown flat. A screenshot is a prop: crop it to the line that matters and treat it physically.
- Music chosen at random, no sound effects, no silence anywhere, or music that ends with a fade-out instead of a button.
- Shots from different cameras with different looks; mixed frame rates; upscaled soft footage as a hero shot.
- Fake precise numbers, invented quotes, claims the source doesn't make; robot demos cut so fast that the proof disappears.

## Building the film

- **Editor (Premiere, Resolve, Final Cut, CapCut):** follow the workflow; the style files give the values.
- **Code (HTML/CSS/GSAP rendered by Hyperframes):** good for type, documents, maps, charts, letterbox, grain, and full films assembled from real footage. Recipes for grade, credits, title cards, paper-in-light documents, light sweeps, letterbox + grain, match-cut montages, audio ducking and poster frames are in `references/hyperframes-recipes.md`; a working demo is `assets/recipes-demo.html`.
- **AI generation (images/video):** only for what can't be filmed or licensed and doesn't claim to be real. Decision table, still-first workflow and tools in `references/generative-assets.md`.

## Scripts

All in `scripts/` (see `scripts/README.md`). Need ffmpeg + ffprobe 5.1+; Python 3.8+ (standard library only); Node 20+ for the finder.
- `analyze_video.py <film> --out <dir>`: cuts, ASL, shot-length curve, loudness, silences, hits, contact sheet. Use it to study a reference film or to QC your own against a style.
- `stock_find.mjs "<query>"`: search free stock sites, keep only ≥ 1080p real footage, download, gate, write a ranked licence manifest.
- `stock_qc.py <clip>`: resolution, frame rate, bitrate, interlacing, sharpness, shake, exposure, watermark heuristics → ACCEPT / ACCEPT-WITH-NOTES / REJECT.
- `select_media.py <files>[@crop] --frame 1920x1080 --zoom 1.08 --sheet s.jpg`: rank candidates for one shot by real on-screen resolution, sharpness at output size, background clutter and exposure; HERO / USE / WEAK / REJECT plus a labelled sheet. Technical only: you still judge meaning.
- `music_map.py <tracks> --want-hit 10.3 --length 20`: loudness strip, hits, built-in drop-outs, button vs fade ending, and the start offsets that land a hit on your story's turn.
- `loudness.sh measure|master|poster`: measure EBU loudness, master to −14 LUFS / −1.5 dBTP by default (two-pass; other targets as arguments), bake a poster image as frame 0.

For dark footage `analyze_video.py` can miss cuts: add `--detector adaptive` and check the contact sheet by eye.

## Studying a new reference

When the user names a brand or film that isn't covered: download a low-resolution copy for analysis only, run `analyze_video.py`, look at the contact sheet and 4–8 key frames, and write notes with the same headings as a style file (Numbers, Structure, Picture, Type, Transitions, Sound, Do/Don't, Recipe). Don't republish the downloaded film; keep only numbers, notes and a few frames for internal study.

## Working with the person who asked

- Show the one sentence, the beat list and the shot plan in plain text before building. Offer 2–3 music options with one line on mood each.
- A synthetic voice is a timing guide until they approve it; their own recorded voice usually wins.
- When they say "looks cheap" or "has no taste", don't add effects. Remove things, slow the pace where the style is calm, fix the type, and check the sound first.
