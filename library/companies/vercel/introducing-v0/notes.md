# Introducing v0: Generative UI  (Vercel, 2023-10-11, 47.5 s, 16:9, YouTube / X)
URL: https://www.youtube.com/watch?v=By9wCB9IZp0
Purpose: launch film (software product, screen-recording-style motion demo)
One-sentence point: Type what you want to ship, get a working UI and its code, and refine it by asking.

Structure: beats with timestamps (by eye; there are no hard cuts)
- 0.0-3.0 product logo builds from scattered lines on white (≈2 s), holds 1 s.
- 3.0-13.5 the question: a large black prompt pill with a bold question; it shrinks to a normal input and example prompts cycle in place (≈1.2 s each, the next one rolls in from below, faded neighbours above and below).
- 13.5-16 the generated UI fades up full screen (white app UI, small).
- 16-28.5 refine: the camera zooms into the UI, the cursor selects an element, an edit prompt is typed, the element updates; zoom back out.
- 28.5-31 code: the code panel swings in with a 3-D tilt and flattens.
- 31-37.5 privacy menu: zoom into a dropdown, a choice is clicked, zoom out.
- 37.5-40 a grid of many generated UIs pans past.
- 40-46 end: URL in small bold type (1 s) → product logo (1 s) → company mark grows, wordmark slides out (≈4 s). 1.35 s silence at the end.

Cut rhythm (verified)
- Both detectors find 0 cuts: the film is one continuous motion-graphics take with camera zooms and fades. By eye ≈12 beats, ≈3.8 s per beat (range 1-10.5 s).
- Measured: 1 shot, 47.5 s.

Typography
- Prompt pill: black (#111) rounded pill ≈75 % W × 13 % H centred at y ≈50 %; white bold sans, cap ≈7 % H, then it shrinks into the real input size.
- UI text is the product's own small type; never enlarged into captions.
- End: URL bold ≈4 % H; product logo ≈7 % H; company wordmark ≈7 % H, black on white.
- Closest free font: Geist (Bold) or Inter Bold.

Colour/grade
- White world (#fff, mean luma 0.95), black ink, the only colours are inside the UI (a blue select state, a dark code panel). No grain, no shadows except soft UI shadows.

Camera/shots
- 100 % UI: real product screens rebuilt as motion graphics; virtual camera zooms 1.5-3× into details and back; one 3-D swing of the code panel. Cursor clicks are shown.

Transitions
- Zoom in/out, scale-down of the hero pill into the real UI, crossfades, roll-up text swaps. No hard cuts at all.

Sound
- No voice. One electronic music bed that grows steadily (RMS ≈−31 dBFS at the start to ≈−20 dBFS at 28-32 s) then falls under the logo; a hit at 0.5 s on the logo build. No drop-outs.
- Integrated −16.6 LUFS, loudness range 4.7 LU.

What makes it premium
- One question as the hook ("what will you ship?") turned into the actual input field: the title IS the UI.
- No cuts: the virtual camera guides the eye from prompt to result to code.
- White, black and the product's own UI only; nothing decorative.

Recipe (Hyperframes, 1920×1080)
- `background:#fff`. Hero pill: `div` 1440×140 px, `border-radius:70px`, `background:#111`, text `700 76px Geist`; after 1.5 s tween `width/height/fontSize` to the real input size (0.8 s `power3.inOut`).
- Prompt cycling: a column of 3-5 strings, `y` step every 1.2 s (`power2.inOut` 0.4 s), neighbours at `opacity .25`.
- UI scenes: real screenshots or live HTML; camera = a wrapper with `scale` 1 → 2.2 and `x/y` to the target (1.2 s `power3.inOut`), hold 3-5 s, back out.
- Code panel: `rotateY(-25deg) → 0` + `scale .9 → 1` (0.8 s) on a `perspective:1400px` parent.
- End: URL 1 s → product logo 1 s → company mark scale 0 → 1 then wordmark `clip-path` reveal to the right (0.6 s). Music swell to ≈−14 LUFS-S at 60 %, 1.3 s silence at the end; master −16 LUFS.
