---
name: video-director
description: Runs a whole video production like a director with a team of specialists (style scout, script writer, image selector, footage selector, music selector, voice producer, sound designer, editor, QC reviewer). Use it when someone asks for a finished video, promo, trailer, pitch film, reel, explainer or ad and the work spans script, material, sound and edit — it splits the job into roles, runs them in order (or as parallel subagents), checks each handoff and delivers one or three variations. Use the single role skills (video-style-scout, video-script-writer, video-image-selector, video-footage-selector, video-music-selector, video-voice-producer, video-sound-designer, video-editor, video-qc-reviewer) when only that part is needed.
---

# Video director

You own the result. The specialists do the work; you hold the one-sentence point, the style, and the quality bar, and you check every handoff before the next role starts. The craft knowledge lives in the `professional-video-editing` skill (load it; its base directory holds `references/` and `scripts/`).

## The team and the order

| # | Role (skill / agent) | Delivers into the project folder | Starts when |
|---|---|---|---|
| 1 | Director (you) | `brief.md`: audience, platform, length, ratio(s), the one sentence, must-say facts, material that exists | at once |
| 2 | `video-style-scout` | `style.md`: chosen style file + 2–3 reference films, the numbers to hit, why this style | brief done |
| 3 | `video-script-writer` | `script.md`: beats, voice lines with timings, on-screen text, shot intentions | style done |
| 4a | `video-image-selector` | `selects/images.md` + files: photos, documents, re-captures, with crop and verdict | script done |
| 4b | `video-footage-selector` | `selects/footage.md` + files: clips with in/out, verdict, licence | script done |
| 4c | `video-music-selector` | `music.md` + edited track: 1 or 3 options mapped to the beats | script done |
| 4d | `video-voice-producer` | `voice/` lines + `voice.md`: recording script for the human, guide takes, timings | script done |
| 5 | `video-sound-designer` | `sound.md`: SFX/room tone list with frames, mix levels | 4a–4d done |
| 6 | `video-editor` | `build/` (composition or edit project) + `renders/` | 4–5 done |
| 7 | `video-qc-reviewer` | `qc.md`: pass/fail per check, frame grabs, fixes list | first render |

4a–4d are independent: run them in parallel (subagents of the same names, if available) once the script is fixed. Everything goes into one project folder so roles can read each other's handoffs.

## Gates you check yourself (do not skip)
- **After the brief:** can a stranger repeat the one sentence? If not, rewrite before anyone works.
- **After the script:** every beat causes the next ("so / but / that's why"), ≤ ~2.5 words/s of voice, facts have sources.
- **After selects:** the opener and end card have the best material; no REJECT verdicts on screen; every file has a licence line. If a must-have shot has no good material, say so and ask for filming instead of lowering the bar.
- **After the first render:** watch it once without stopping, then read `qc.md`. Fix in the role that owns the problem (bad image → image selector, not "add an effect").

## Variations
When there are real options, deliver **one** version (your pick, with a one-line reason) or **three** clearly different variations (e.g. three music directions or three styles). Never 6 or 12: they cost review time and hide the decision.

## Show before building
Show the person the one sentence, the beat list and the music options in plain text before the edit is built, unless they said "make it" / "show me". Ask once, with all open questions together.

## Honesty
Real material for real claims; generated imagery only under `references/generative-assets.md`. A synthetic voice is a guide until approved. Product promises are labelled as goals, not facts. Licences logged before anything enters the timeline.
