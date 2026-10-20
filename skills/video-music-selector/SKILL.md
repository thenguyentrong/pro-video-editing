---
name: video-music-selector
description: Chooses and edits the music for a video — shortlists licensed tracks that fit the style, maps each track's structure (hits, built-in drop-outs, button or fade ending, vocal band), cuts it to the film's length so the biggest hit lands on the story's turn and the end is a clean button, and offers one or three options. Use it whenever a video needs music, a soundtrack, a "beat drop on the title", a shorter edit of a song, or when the music feels random or fights the voice.
---

# Video music selector

Load the `professional-video-editing` skill: `references/selecting-images-and-sound.md` (music checklist), `references/sound-and-mix.md`; tool `scripts/music_map.py`.

## Steps
1. From `style.md` and `script.md` take: mood, tempo range, film length, the second of the turn (where the big hit must land), whether the style uses a drop-out.
2. **Shortlist** 5–8 licensed tracks (the project's library, Pixabay Music, Artlist, Epidemic, Musicbed; log licence + track page). No lead vocals under voice-over.
3. **Map them:** `python music_map.py t1.mp3 t2.mp3 ... --want-hit <turn s> --length <film s>` → hits, drop-outs, ending type, and source offsets that put a hit on the turn. Keep tracks whose structure fits; mood alone is not enough.
4. **Edit** the best 1 or 3 with ffmpeg: `atrim` sections joined at bar lines with `acrossfade=d=0.03–0.05`, drop-out shortened to the style's length (0.35–2 s), the end cut to a final hit (button) or the track's own ending; never a fade-out unless the style asks. Check the joins by ear (no double beats).
5. Write `music.md`: per option one line on mood, the edit recipe (source in/out times), where the hit and drop-out land, licence. Deliver `music_<name>.wav` at 48 kHz.

## Rules
- Offer one track (your pick + reason) or three clearly different directions; the person chooses.
- Music sits 10–15 dB under the voice; the voice producer and sound designer get your hit times.
- Trailer: build → silence → boom on the turn. Apple-like: steady pulse, short or no drop-out. Documentary: drones and space. Social: platform-native sound.
