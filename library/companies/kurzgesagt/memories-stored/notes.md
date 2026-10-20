# How Are Memories Stored Inside Your Brain?  (Kurzgesagt – In a Nutshell, 2026-06-16, 13:56 full / first 300 s analysed, 16:9, YouTube)
URL: https://www.youtube.com/watch?v=PqtggjVAi8M
Purpose: animated science explainer (biology / neuroscience, narrator-led)
One-sentence point: A memory is not a stored picture but a pattern of neurons firing together that the brain chooses to make physical — and it changes every time you recall it.

Data note: first 300 s analysed (trimmed after download). Cuts measured with `--detector adaptive` (21 cuts; scene detector 16, all inside the adaptive list). No sponsor inside the first 300 s. The film changes idea mostly by camera moves and morphs inside one shot; set-up counts are by eye (≈).

## First 30 s (hook)
- 0.0–0.3 picture already moving; narration starts at 0.3 s (no silent intro, no logo, no ad).
- 0.0–3.0 slow push-in on a sleeping girl character's forehead; a small dark hole opens and grows into a glowing portal (zoom-through begins).
- 3.0–4.0 the camera flies through the portal (dark purple bubble frame).
- 4.0–7.0 reveal: her open eyes under water, manta rays swim across her face (the face becomes the window of the memory).
- 7.0–11.0 the memory itself: a bright coral reef with a diver, full-frame turquoise.
- 11.0–15.7 pull-back: the reef shrinks into a glowing bubble; more memory bubbles float around the girl (her at a desk, a child at a beach).
- 15.7 the only hard cut in the first 30 s: a wax diorama of the reef in a bowl on black.
- 18–30 two huge spotlight "eyes" lean in from the top corners; the diorama melts and shifts colour as they look (the metaphor of recall changing the memory).
- 30–35 the diorama spirals away in a swirl of shapes; 35–45 back on the girl's face while the question is posed (≈35–43 s: what is a memory, how is a moment stored).
- 45 burst transition into the first chapter title "Your Brain is Weird Madness" (script type on a glowing brain), 45–50 s.
- Shape of the hook: concrete sensory moment → metaphor (wax diorama) → stake (it is what makes you you, ≈25 s) → question (≈35–43 s) → chapter title (45 s). ≈8 set-ups in 30 s (≈3.7 s each) with 1 hard cut.

Structure (first 300 s):
- 0–45 hook as above.
- 45–50 chapter title 1.
- 50–100 the brain explodes into a starfield of neurons; a forest of neurons with a cyan label box "86 Billion Neurons" (≈66 s); synapse close-ups; neurons vs galaxies comparison (96–100 s).
- 100 0.37 s flash shot, back to the girl's eye (101–104 s).
- 104–135 neurons firing together "become buddies"; white full-frame card "LOCAL COLUMNS" (125–127 s); macro of the eye.
- 135–170 senses as columns (sound, image, touch icons in coloured circles), white card "CEREBRAL CORTEX" (149–151 s), the girl's head becomes a machine of gears.
- 170–183 brain regions on a dark silhouette with white hairline callouts ("Motor Cortex", "Limbic System" ...).
- 184–228 network concert, white card "ASSEMBLY" (202 s), assemblies as coloured blobs with small labels.
- 228–247 pond ripples (nothing remains), memory bubbles.
- 247–251 chapter title 2 "How to Store the Past" (same script style).
- 251–300 competing assemblies, the girl reading, white card "HIPPOCAMPUS" with a cute two-lobed character (294–296 s).

Cut rhythm: 22 shots in 300 s, ASL 13.6 s, median 9.35 s. ASL by quarter 18.8 / 7.5 / 18.8 / 10.7 s. 4.5 % under 1 s (one 0.37 s flash), 86 % over 3 s. Longest 54.7 s (15.7 s), 49.4 s (191.7 s), 34.3 s (134.1 s). Cuts per 10 s: 0–2. By eye ≈1 new set-up every 3–5 s. Cuts on onsets 48 % vs 52 % chance.

Typography:
- Chapter title: retro brush/script, cream #FFF3C8 with a soft shadow, two lines, slight upward slant, cap ≈10 % H, centred on a glowing object (brain). Closest free: Pacifico or Yellowtail (guess).
- Term cards: full-frame white #FDFDFD with one illustration and a tracked caps label under it in dark indigo #3A2A6A, cap ≈4 % H, letter-spacing ≈0.12 em, ≈2 s hold. Used 4 times in 300 s (125, 149, 202, 294 s) as "definitions".
- Number label: white bold sans in a flat cyan box #17C8F0, cap ≈3.3 % H, bottom centre at ≈79 % H.
- Anatomy callouts: white medium sans ≈3 % H on a 1–2 px white leader line with one elbow.
- Closest free for the sans: Outfit / Nunito Sans (guess).

Colour/grade: deep purple-black ground #0A022E / #2E034D, violet #6A0177 / #54036B, skin orange #E98208, accents electric cyan #12F0FC, neuron yellow-gold glows, magenta. White "definition" cards as a hard contrast against the dark film. Flat shapes, no outlines, soft inner gradients on round objects, bloom on everything that "fires".

Camera/shots: 100 % 2D animation. Zoom-through into a body part, push-ins, pull-outs into bubbles, swirl transitions, slow parallax drift on every hold.

Transitions: hard cuts between worlds (every ≈14 s); morphs (reef → bubble), zoom-throughs (forehead → portal → eyes), swirl wipe (30 s), burst into the chapter title (45 s), white card cuts.

Sound: integrated −15.4 LUFS, LRA 2.3 LU, true peak −2.6 dBTP. 50 ms RMS median −20.0 dBFS, p10 −29.0 dBFS → score ≈9 dB under the voice, no drop-outs at all (0.2 % of windows below −45 dBFS). Rises of 17–26 dB on sound-effect accents (pops, sparkles, whooshes), e.g. 160 s +25.7 dB.

What makes it premium:
- The hook is a single camera journey through one character into one memory: no text, no logo, story from frame 1.
- One strong physical metaphor (melting wax diorama) carries the abstract idea.
- Recurring characters give a human face to the brain science.
- White term cards are the only "slide"; everything else is a living world.

Recipe (HTML/GSAP):
- Zoom-through: SVG face, a circle mask grows from 0 to 160 % of the frame (`r` 0 → 1.6×W over 3 s, `power2.in`), the next scene is inside the mask; on arrival `scale 1.3 → 1` over 1 s.
- Morph to bubble: the full scene inside `clip-path: circle(75% at 50% 50%)` → `circle(18% at 50% 45%)` over 3 s `power2.inOut`, plus a ring `stroke:#12F0FC; filter:drop-shadow(0 0 10px #12F0FC)`.
- Term card: `background:#FDFDFD`; label `font:700 4vh "Outfit"; letter-spacing:.12em; color:#3A2A6A; text-transform:uppercase`, illustration `scale .9 → 1` 0.4 s `back.out(1.6)`, hold 2 s, hard cut out.
- Chapter title: `font:400 10vh "Pacifico"; color:#FFF3C8; transform:rotate(-6deg)`, glow behind (radial gradient #2EE6FF → transparent), letters scale in 0.03 s stagger.
- Mix: voice −15 LUFS short-term, score 9 dB under with no gaps; SFX accent on every pop and sparkle.
