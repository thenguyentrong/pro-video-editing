# I don't get democracy  (Johnny Harris, 2026-09-10, 51:11 full / first 90 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=O7LvhSQ5Te4
Purpose: explainer / personal essay (creator-led, conversational, "I'm figuring this out with you")
One-sentence point: Everyone says democracy is "in trouble", but Johnny admits he can't define it — so he and his producer go find out what it actually means.

Data note: reused the earlier analysis `d1_jharris` (first 90 s only). Key frames were re-extracted from a fresh 480p download; times can be ~0.5 s off around 32 s.

Structure (first 90 s):
- 0.0–4.1 moody cold open: dim office (desk lamp, model ship), slow push, JH at the desk; ambience, no talk.
- 4.1–8.3 JH fiddling with the model ship; word-by-word yellow caption "DEMOCRATIC BACKSLIDE" typed under him.
- 8.3–14.8 JH lying on a couch under a wall of maps, caption "NOT A…".
- 14.8–21.1 walks into a red-walled booth with headphones, scrolls news on a phone; caption builds "DEMOCRACY → DEMOCRACY IS → DEMOCRACY IS IN TROUBLE".
- 21.1–28.5 evidence of the cliché: JH at his computer, then a full YouTube page screen capture of another creator's "Why Democracy Doesn't Work" (its own captions, word "voter" highlighted), then two 0.4–0.7 s flashes of that creator, one bleached to white.
- 28.5–32.6 JH at the desk in teal window light; 3 × 0.4–0.5 s inserts of keyboard and mouse (31.2–32.6 s); sound drops 3 s (29–32 s, −15 → −41 LUFS).
- 32.6–39.5 his producer joins: two webcam frames placed on off-white paper with a soft border, label "ADAM / Producer"; JH's own earlier videos shown as YouTube cards ("Is Fascism Back? 7.4M views", "Oligarchy is worse than you think").
- 39.5–58.4 conversation cut fast: JH webcam / Adam webcam / B-camera of JH at a studio mic, 1–2.5 s per shot. 1.6 s near-silence at 45.4 s (−63 dBFS) then a +36 dB jump at 47.5 s (comic beat).
- 58.4–62.5 archive talk-show clip (Doris Kearns Goodwin, Late Show) with Johnny's subtitles + source credit bar; 62.5–70.5 split-screen talk; 70.5–76.9 campaign rally footage with subtitles; 76.9–84.8 split screen; 84.8–90 another expert clip (webcam) with subtitles + credit.

Cut rhythm: 41 shots in 90 s, ASL 2.20 s, median 1.54 s. ASL by quarter 3.21 / 1.32 / 1.61 / 3.75 s. 27 % of shots under 1 s, 24 % over 3 s. Longest 6.5 s (8.3 s, couch) and 6.3 s (70.5 s, rally); shortest 0.33–0.38 s (inserts at 28.2, 32.2, 58.1 s). Cuts per 10 s: 2 2 8 8 5 8 3 3 1. Slow cinematic open (4–6 s shots), very fast middle (8 cuts per 10 s from 20 to 60 s), slows again on archive clips. Cuts on onsets = chance (48 % vs 52 %): cut on speech, not on music.

Typography:
- Spoken-word captions: yellow #FFFF4C caps in an Optima-like flared humanist sans, small (cap height ~3.8 % H), centred at ~77 % H, typed on letter by letter in sync with the words (karaoke build, not a full subtitle). Only on key phrases.
- Subtitles on third-party clips: sentence case, pale yellow, same flared face, ~4 % H, lower-centre.
- Source credit for clips: one line, white sans ~2.2 % H on a dark translucent bar bottom left: "Name, *Programme in italics*, Month D, YYYY".
- Person label on the paper layout: "ADAM / Producer" — name in caps, role in small caps, black on off-white, under the webcam frame.
- Closest free for the flared sans: Belleza or Linux Biolinum (guess; it reads like Optima).

Colour/grade: two looks cut together. (1) "Film" look: warm tungsten practicals vs teal window light, deep shadows, shallow focus, slight halation, lots of texture (maps, posters, model ship, film reel) — a lived-in set. (2) "Desk" look: flat webcam captures and screen grabs laid on an off-white paper ground (#EEEDEA-ish) with soft drop shadow/grey border. Archive and talk-show clips untouched.

Camera/shots: cinema camera on a gimbal/handheld for the cold open (push-ins, over-the-shoulder, extreme close-ups of hands on keyboard); B-cam at the podcast mic; webcams for the conversation; screen captures of YouTube pages and phones. Insert shots of hands/objects of 0.3–0.5 s as punctuation.

Transitions: hard cuts only; one white "bleach" flash (27 s) on the other creator's face; split-screens and paper layouts are cut in, not animated in. Soft detector found one soft change (16.1 s, booth door).

Sound: louder, dry YouTube-native mix: integrated −15.1 LUFS, loudest −10.4 LUFS momentary at 42 s. 50 ms RMS median −20.9 dBFS, p10 −40.4 dBFS → pauses drop ~20 dB below the voice, so the bed is quiet. Uses silence as a joke and as a breath: 3 s drop while he types (29–32 s), 1.6 s near-silence at 45.4 s then +36 dB, small 0.15–0.6 s gaps throughout. Biggest rises 27–31 dB in 50 ms at 1.2, 2.5, 24.9, 49.1, 70.8 s (clip entries and reactions).

What makes it premium:
- The "film" layer (lit set, objects, slow push-ins) makes a talking podcast feel like a documentary.
- Evidence is the internet itself: other creators' YouTube pages, his own past videos with view counts, a talk-show clip with a full citation.
- Captions only on the words that carry the idea, typed in sync, small and yellow — never full subtitles of his own voice.
- Honest process: the producer's webcam, "I don't get it" admission, raw conversation.

Recipe (real footage + HTML/GSAP):
- Paper desk layout: `background:#EEEDEA` + subtle noise (SVG feTurbulence at 6 % opacity); webcam `<video>` frames at 41 % W, `border:6px solid #d9d8d4; box-shadow:0 2px 18px rgba(0,0,0,.18)`; label under the right frame `font:500 2.6vh 'Belleza'` "ADAM" + `/ Producer` at 2.2vh. Cut the layout in on a hard cut.
- YouTube card evidence: real screenshot (title + views + age) on the same paper, `scale 1→1.04` over 2.5 s, ease none; place two side by side, second one cut on 1 s later.
- Typed key-phrase caption: `font:600 3.8vh 'Belleza'; color:#FFFF4C; letter-spacing:.04em; text-transform:uppercase; bottom:21vh; text-shadow:0 1px 6px rgba(0,0,0,.45)`; reveal characters in sync with the word timestamps (`gsap.set(char,{opacity:1}, wordStart + i*charDur)`), hold 0.5 s after the phrase, cut off.
- Clip citation bar: `background:rgba(20,20,20,.55); color:#fff; font:400 2.2vh Inter; padding:.3em .6em; left:5vw; bottom:6vh` — "Name, <i>Programme</i>, Month D, YYYY".
- Rhythm: open on 3–4 slow, lit, wordless shots (4–6 s, push-in `scale 1→1.06`), then talk at 1–2.5 s per shot with 0.3–0.5 s object inserts; give quotes/archive 4–6 s.
- Mix: dialogue −16…−14 LUFS short-term, bed 20 dB under, drop everything to room tone for 1.5–3 s before a punchline or after a question.
