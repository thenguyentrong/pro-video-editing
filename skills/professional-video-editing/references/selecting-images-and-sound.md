# Selecting images, footage and sound (the "selects" stage)

A good cut cannot save a bad picture. Viewers forgive a plain edit; they do not forgive a soft, cluttered or wrong-looking hero image in the first two seconds. Editors therefore spend real time on **selects**: gather many candidates per shot, compare them side by side, and only then build. Never use the first image you found because it was there.

## The order of work for every shot
1. **Write what the shot must do** in one line: "establish the robot as real and Chinese-made", "show a hand that stops a machine". This is the yardstick for meaning.
2. **Gather 5–10 candidates** (own footage, 4K stock via `stock_find.mjs`, Commons, press kits). Download originals, never thumbnails or re-exports.
3. **Decide the real use**: output frame, the crop that will actually be on screen (the subject must fill it), and the largest push-in.
4. **Run the technical gate:** `python scripts/select_media.py a.jpg@x,y,w,h b.mp4 ... --frame 1920x1080 --zoom 1.08 --look dark --sheet selects.jpg`. Pass the crop box whenever the subject is small in a wide photo.
5. **Look at the sheet** and judge what no script can: is it the right thing, does it say the line, does it belong to this film's world? A sharp gamepad clip scored "HERO" as an e-stop candidate. Relevance is your job.
6. **Pick one, write down why** (and the runner-up). If nothing passes, say so and get better material (film it, ask for the press kit) rather than lowering the bar.

## Image and footage checklist (in priority order)
| Check | Pass | Typical fail |
|---|---|---|
| Right subject, right meaning | It shows exactly the line being said | Toy robot for "humanoid", gamepad for "stop button", CGI city for "Europe" |
| Real | Photographed/filmed, not generated or rendered | CGI/AI clips that slipped past the site's label (check hands, text, physics) |
| Resolution at the real crop | Source pixels ≥ output pixels (upscale ≤ 1.0, never > 1.15 for a hero) | A 4K photo where the robot fills 25 % of the width becomes a 2.5× blow-up once cropped |
| Sharp at output size | Subject in focus, no motion blur on the key detail | Phone frame grabs, old re-exported crops, shallow-focus misses |
| Clean background | One subject, calm or dark background, nothing competing | Patterned carpet, purple stage light, costumes, sponsor banners, crowds, QR codes |
| Light and grade fit | Same world as the other shots (bright film = bright shots) | One dim olive clip inside a bright Apple-style film |
| Composition | Room for text where the type system needs it; subject on a strong point | Subject cut by the frame edge, no negative space for the credit |
| No foreign brands / people issues | No readable third-party logos; people not endorsing anything | Brand on a shirt, identifiable faces for a negative claim |
| Licence | Logged before it enters the timeline | "Found on Google" |
| Motion > still | A real moving shot beats a still; a still needs a reason | Ken Burns on a weak still to fake motion |

Rules of thumb:
- **Subject size decides the needed resolution.** If the subject will fill the frame but fills only a third of the source width, you need ≥ 3× the output width (5760 px for 1080p).
- **The first frame is the poster.** The opener and the end card get the best material you have; weak shots go in the middle, short and small.
- **If you only have one usable photo of something, use it small or short** (an inset, a 1 s beat, behind type), not as a 3 s full-frame hero.
- **Re-capture documents** at 2–3× device scale instead of upscaling screenshots; for 9:16 re-wrap the text into a narrow column so it stays big.
- **Same moment, many frames:** burst photos of the same scene (expo series) let you pick the frame with the cleanest pose and background; they do not make convincing fake motion.

## Sound selection
### Music
| Check | Why |
|---|---|
| Structure fits the story | The film's turn needs a hit; a trailer needs a built-in drop-out before it. Map the track first: `python scripts/music_map.py track.mp3 --want-hit 10.3 --length 20` lists hits, drop-outs, ending type and the start offsets that put a hit on your turn. |
| Ending | "button" endings cut cleanly at the end card; a "fade" ending needs an edit to its final hit or a cut to silence. |
| Mood matches the style file | Trailer = build + boom; Apple = steady pulse; documentary = drones and space; social = the platform's sound; anthem = one emotional rise. |
| No lead vocals or busy melody under voice-over | Voice and melody fight in the 1–4 kHz band; `music_map.py` gives a rough hint, then listen. |
| Tempo vs cut rhythm | Faster styles need tracks whose beat supports the ASL (1 beat = 60/BPM s). |
| Licence | Logged; library and track page saved. Never use a track you can't license for the release. |

Offer 2–3 tracks with one line on mood each; the person who asked chooses.

### Sound effects
- One effect per meaningful cut or action, matched to what we see (cable click on the cable, a mechanical press on the button), not cartoon effects (vine boom, airhorn) unless the style is a meme.
- Layer hits (transient + body + sub); keep one big hit per film.
- Room tone under every scene; never dead digital silence except as a deliberate drop-out.
- Check every effect at the frame it lands: 1–2 frames late feels natural, early feels fake.

### Voice
- The voice is the most important sound. A real human recording beats any synthetic voice; synthetic is a timing guide until approved.
- Record close, in a soft room, 48 kHz; clean breaths and clicks; −14 LUFS master with music 10–15 dB under.

## Lessons from real reviews
- A cut was "better edited" but the reviewer immediately saw the opener: a soft, upscaled close-up of the robot on a red patterned carpet. The gate rejected it (sharpness 5). Four sharper 4K frames of the same robot existed in the same free collection, two of them on calm dark backgrounds.
- The stop-button clip used in every version was soft at output size; the free libraries had no sharp on-topic alternative. The fix is five minutes of own filming, not a sharper-looking but wrong clip.
- Stock searches for niche objects return off-topic but technically perfect clips; the score sheet makes them look attractive. Always check meaning first.
