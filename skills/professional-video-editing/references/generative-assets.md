# AI-generated images and video (when, how, and when not)

Generated material is a tool for what you cannot film or license: an establishing shot of a place that does not exist yet, a stillomatic to test timing, an abstract texture, a background plate. It is the wrong tool for anything the viewer must believe is real: a real product, a real person, a real event, a real document. Many clients and audiences reject a film the moment one shot "looks AI". Ask before using it, label it internally, and never mix a generated shot into a sequence that claims to be documentary.

## Decision table

| Need | Use | Why |
|---|---|---|
| Real product, real robot, real people, real place | Real footage / licensed stock / the client's own filming | Credibility; generated versions drift (extra fingers, bent joints, wrong logos) |
| Evidence (headlines, studies, laws, numbers) | Screenshots / documents treated physically | Must be verifiable |
| Timing test before a shoot (stillomatic) | Generated stills, clearly temporary | Cheap, fast, replaced later |
| Concept frames for a pitch deck or storyboard | Generated stills | Communicates intent, not fact |
| Abstract textures, backgrounds, light leaks, skies | Generated or procedural (CSS/GLSL noise) | Nobody fact-checks a texture |
| A shot that is physically impossible to film (future city, giant scale) | Generated video, only if the style is openly speculative | Say so on screen or in the brief |

## Workflow that keeps generated shots believable
1. **Still first, motion second.** Generate the start frame (cheap), inspect it at 100% for hands, joints, grippers, text and logos, then animate only clean frames.
2. **Reference real shapes.** Give a real product photo or render as a reference image; invented machines look "AI".
3. **Keep tools and hands visible** in the start frame; a hidden gripper gets reinvented by the video model.
4. **Say what you don't want:** "unbranded, no text, no logos, no watermark, no phone interface, rigid metal, no morphing".
5. **Cut around errors.** Keep the clean 2–3 seconds of a 6 s clip; review frame by frame.
6. **Resolution:** generate at the highest native resolution (2K/4K stills, ≥1080p video) and never upscale a soft clip into a hero shot. Apply the same grade and grain as the real footage so it sits in the film.
7. **People and faces:** never let a model redraw a real person's face; use their real photo. Don't upload third parties from group photos.

## Tools that have worked (2026)
- **Images:** Nano Banana Pro / 2.1 (Gemini image models, via the Gemini API or Higgsfield), GPT Image, Soul 2 (photo-real people). Pick 2K for frames, 4K for hero stills.
- **Video:** Minimax Hailuo 2.3 at 1080p (keeps rigid machines rigid from a clean start frame), Kling 3.0 (pro tier for quality), Veo 3.1, Seedance 2.5 (expensive). Expect ~3 min per clip and concurrency limits (submit ≤ 2–4 at once).
- **Speech:** TTS (ElevenLabs/Minimax voices) is only a timing guide unless the client approves a synthetic voice. Music and SFX come from licensed libraries.
- Always run a cost preflight and log what each shot cost.

## Code-built visuals (the honest alternative)
Typography, maps, charts, document shots, UI recordings, light sweeps, grain and letterbox can be built in code (HTML/CSS/GSAP via Hyperframes, see `hyperframes-recipes.md`). Do not draw characters or fake product UIs in code: they read as cheap animation, not film.
