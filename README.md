# Pro Video Editing for Claude

A professional video editing team for Claude Code: a director plus specialists for style, script, images, footage, music, voice, sound, editing and quality control, built on editing styles measured from 358 published films by 114 brands, studios, publishers, broadcasters, creators and hardware companies.

The goal is simple: videos made with Claude should look like they were made by people with taste, not stitched together by a machine. Every rule here comes from studying how professional teams actually cut: shot lengths, where the fastest cutting sits, how long text stays on screen, where the silence goes before the big hit, how loud the master is.

## What's inside

**Skills** (`skills/`)

| Skill | Role |
|---|---|
| `professional-video-editing` | Shared knowledge base: workflow, 18 style guides, cutting, sound, stock sourcing, QC, scripts |
| `video-director` | Runs the team, checks every handoff, delivers one or three variations |
| `video-style-scout` | Finds inspiration and picks the film language with the numbers to hit |
| `video-script-writer` | One-sentence point, argument chain, timed voice lines, on-screen text |
| `video-image-selector` | Photos and documents, checked at their real on-screen crop |
| `video-footage-selector` | Real ≥1080p (prefer 4K) footage with an automatic quality gate |
| `video-music-selector` | Maps track structure so the hit lands on the story's turn |
| `video-voice-producer` | Voice-over direction, guide takes, recording sheet, cleaning |
| `video-sound-designer` | Sound effects, room tone, ducking, loudness master |
| `video-editor` | Assembles and renders (NLE or code with HTML/GSAP) |
| `video-qc-reviewer` | Fresh-eyes review with pass/fail, evidence and owner per fix |

**Agents** (`agents/`): one subagent per role, so the director can run image, footage, music and voice selection in parallel.

**Style guides** (`skills/professional-video-editing/references/styles/`): `apple-precision`, `brand-documentary`, `broadcast-tv`, `cinematic-brand-anthem`, `construction-aec`, `creator-youtube`, `deeptech-hardware`, `design-tech`, `documentary-evidence`, `editorial-explainer`, `human-demo-warm`, `industrial-robotics`, `movie-trailer`, `opening-credits`, `place-film`, `social-vertical`, `startup-launch`, `tech-launch-loud`. Each has measured numbers (shot length ranges, cut-density curve, text sizes as % of frame height, hold times, silences, loudness), structure by % of runtime, type with the closest free fonts, transitions, sound, do/don't and a step-by-step recipe.

**Scripts** (`skills/professional-video-editing/scripts/`, ffmpeg + Python standard library + Node):
- `analyze_video.py`: cuts, shot lengths, density over time, loudness, silences, hits, contact sheet
- `select_media.py`: ranks candidate images/clips by real on-screen resolution, sharpness, background clutter, exposure
- `music_map.py`: hits, built-in drop-outs, ending type, and where to start a track so its hit lands on your turn
- `stock_find.mjs` + `stock_qc.py`: keyless search of free stock libraries, ≥1080p real footage only (AI-labelled and restricted clips dropped), quality gate, licence manifest
- `loudness.sh`: measure, master to −14 LUFS / −1.5 dBTP, bake the poster as frame 0

**Library** (`library/`): the notes and measurements behind the style guides, one folder per company and film.

## Install

As a Claude Code plugin:
```
/plugin marketplace add thenguyentrong/pro-video-editing
/plugin install pro-video-editing@pro-video-editing
```
Or copy the folders in `skills/` to `~/.claude/skills/` and the files in `agents/` to `~/.claude/agents/`.

Requirements for the scripts: ffmpeg/ffprobe on PATH, Python 3.9+, Node 18+ (stock finder; `npm install` in the scripts folder for Playwright). Building films in code uses [Hyperframes](https://github.com/heygen-com/hyperframes).

## Use

Ask for a video ("make a 30 s launch film for …", "cut this like a trailer", "find 4K footage of …", "why does this look cheap?"). The director skill splits the job into roles; single roles can be used on their own.

## Principles
- Real material for real claims. Generated imagery only where nothing can be filmed and nothing pretends to be real.
- One sentence, one film language, one accent colour.
- Selects before editing: the opener gets the best image you have.
- Music first, then cut; one measured silence, one big hit.
- One or three variations, never twelve.

## Notes
The library describes and measures published films to learn editing craft. It contains notes and numbers only, no media. All films and trademarks belong to their owners; this project is not affiliated with or endorsed by any of them.

MIT licence.
