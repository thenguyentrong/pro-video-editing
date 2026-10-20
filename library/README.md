# Style library

Notes and measurements from published films that were studied to learn how professional teams edit
(brands, studios, publishers, broadcasters, creators and robotics companies). The cross-company
conclusions live in `skills/professional-video-editing/references/styles/`.

```
companies/<company>/
  STYLE.md            the company's editing style across its examples
  <example>/
    notes.md          what the film is, structure with timestamps, rhythm, type, colour, camera,
                      transitions, sound, what makes it premium, a recipe to rebuild the look
    metrics.json      measured numbers: cuts, shot lengths, density over time, loudness, silences
```

How the numbers were made: a 480p copy was analysed with `skills/professional-video-editing/scripts/analyze_video.py`
(scene + adaptive cut detection, EBU R128 loudness, silence and hit detection), cuts were checked by eye on
1 frame/s contact sheets, and the media was deleted afterwards. Contact sheets and key frames were used for the
analysis only and are not published. Values marked ≈ were judged by eye. Some older files use a slightly
different metrics.json layout; read them with a tolerant parser.

All films and trademarks belong to their owners. This library describes and measures them for learning; it is
not affiliated with or endorsed by any of the companies named.
