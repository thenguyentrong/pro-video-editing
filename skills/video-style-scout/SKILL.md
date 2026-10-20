---
name: video-style-scout
description: Finds inspiration and picks the film language for a video — which house style (Apple precision, movie trailer, editorial explainer, social vertical, broadcast, brand anthem, industrial robotics, startup launch, creator YouTube, place film, construction, deep-tech and more), which reference films to study, and which measured numbers to hit. Use it whenever someone asks "what style", "make it look like Apple/Marvel/Vox/Nike", shares a reference video to learn from, or before scripting any video; also to analyse a new reference film and add it to the style knowledge.
---

# Video style scout

Load the `professional-video-editing` skill; its base directory holds `references/styles/*.md`, `references/measured-numbers.md` and `scripts/analyze_video.py`.

## Job
Turn the brief into ONE film language with numbers, and give the rest of the team references to look at.

1. Read `brief.md` (audience, platform, length, the one sentence).
2. Shortlist 2–3 styles from the core skill's style table that fit the purpose (pitch with stakes → trailer or documentary-evidence; calm product claim → Apple precision; phone feed → social-vertical; hardware proof → industrial-robotics or deeptech-hardware; place/team/event → opening-credits or place-film).
3. Read those style files fully. Pick one; one language per film (a trailer may borrow a documentary-evidence middle).
4. Write `style.md`:
   - chosen style + one line why, and the runner-up;
   - 2–3 reference films (title, owner, what to watch for, timestamp);
   - the numbers to hit: ASL range, density curve, % shots < 1 s, text size % H, words per card, hold times, silences, LUFS, aspect;
   - type system (font or free match, weights, case, one accent colour), grade, transitions allowed, sound pattern;
   - the style's "Don't" list, copied short.
5. If the person sent a reference that isn't covered: download a low-res copy for analysis only, run `analyze_video.py <file> --out <dir>`, look at the contact sheet and 4–8 frames, and write notes with the style-file headings. Use the numbers, never the media.

## Quality bar
- The numbers come from the style file or your own measurement, not from memory.
- If the person's taste notes (e.g. a personal overlay skill) contradict the style file, their notes win; say so in `style.md`.
- Offer 1 or 3 style options when the choice is open, never more.
