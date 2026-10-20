# Sound and mix

Sound decides whether a film feels premium. Trailer editors say music is "eighty percent" of the pulse; Apple keeps sound effects so subtle they "almost aren't there". Both are deliberate.

## Layers (bottom to top)
1. **Room tone / ambience** under every scene so cuts never sound dead.
2. **Music bed** chosen before cutting; map its intro, build, drop-out, hit, outro, then cut to it.
3. **Sound effects** on cuts and moves: whoosh on camera moves, click/shutter on document cuts, foley on real action (servos, steps), risers that peak on the exact frame of impact, hits built from transient + body + sub.
4. **Voice** on top, centred, compressed, de-essed; music 10–15 dB below it (Apple launch films: 8–10 dB).

## Moves that matter
- **Drop-out:** silence 0.35–2 s right before the biggest hit (measured in trailers: ~0.35 s before the title hit; 2–3 s of black before a closing scene). Apple product films use only short ones (0.2–1.8 s) or none.
- **Ducking:** music down in ~4 frames when the voice starts, back up over 20–30 frames.
- **Suck-back:** a reversed swell into a title card or hit.
- **Button:** end on a clean final hit, not a fade. Apple-style and premium films instead take the music out before the logo and hold the logo in silence (0.2–3 s; premium brands up to ~6 s).
- **Sync:** a sync 1–2 frames late often feels better than perfect; 72% of cuts in an Apple lifestyle montage land within 0.1 s of a music onset.

## Targets
Default social/web master: −14 LUFS integrated, true peak ≤ −1 dBTP. The style file can set its own target: about −16 for calm Apple-style and title films, −10 to −12 for loud launch films and social anthems, lower for quiet art-house or dialogue cuts. Never above −9 LUFS or above −1 dBTP. Broadcast follows the broadcaster's spec (EBU R128 = −23 LUFS). Measured uploads range from about −8 to −24 LUFS, so copy the dynamics, not the upload level. Check in mono; check at arm's length on a phone. `ffmpeg -i film.mp4 -af ebur128=peak=true -f null -` to measure; `loudnorm=I=-14:TP=-1.5:LRA=11` to master.

## Licences
Music and SFX from licensed libraries (Pixabay Content License, Artlist, Epidemic, Musicbed, Freesound CC0). Log every file. TTS voices are timing guides unless the client approves synthetic speech.
