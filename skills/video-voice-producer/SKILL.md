---
name: video-voice-producer
description: Produces the voice-over for a video — a recording script and direction sheet for a human speaker, timed guide takes with a local TTS voice, cleaning (silence trim, de-click, loudness), timing each line to the beats and checking that voice and music don't fight. Use it whenever a video needs narration, a voice-over, a guide voice, a re-record, or someone says the voice sounds robotic, too slow, too quiet or "AI".
---

# Video voice producer

Load the `professional-video-editing` skill (`references/sound-and-mix.md`, `references/selecting-images-and-sound.md` → Voice).

## Steps
1. From `script.md`, write `voice.md`: each line with its target start time, max duration, emphasis words, pace (≈2.5 words/s), tone in two words ("calm, certain").
2. **Guide takes** for timing only: a local TTS voice (e.g. Kokoro via `npx hyperframes tts "<line>" --voice bm_george --speed 1.05 -o L1.wav`), one file per line. Label them "guide voice" in every handoff; a synthetic voice ships only if the person approves it.
3. **Human recording sheet:** quiet soft room, phone or USB mic 15–20 cm off-axis, 48 kHz WAV, 3 takes per line, 1 s of room tone at start; the lines with timing marks. Ask the person to record it — their own voice usually wins.
4. **Clean:** trim silences (`silenceremove` start and end at −45 dB), remove clicks/breaths that distract, light compression, de-ess; normalise lines to ≈ −18 LUFS before the mix.
5. **Fit:** if a line is longer than its slot, rewrite it shorter with the script writer; speed-up only up to ~1.1×.
6. Hand the editor `voice/L*.wav` + a timing table.

## Rules
- Voice is the most important sound: intelligible on a phone speaker at arm's length.
- One voice per film unless the style uses dialogue or testimonials.
- No cloned voices of real people without their written consent.
