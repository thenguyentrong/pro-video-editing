# Create & launch LinkedIn Ads without leaving Canva  (Canva, 2026-09-23, 42.7 s, 9:16, YouTube Shorts)
URL: https://www.youtube.com/shorts/nAZD57mN78I
Purpose: B2B feature explainer (ads creation + launch + reporting)
One-sentence point: An expert creator asks "what if" you could make, launch and measure LinkedIn ads in one tool, then the screen recording shows each of the three steps.

Structure: beats with timestamps
- 0.0-4.2 hook: talking head asks a what-if question; purple subtitle pill from frame 1; name tag at ≈2.5-4.2 s (name pill + "verified expert" highlight).
- 4.2-20.3 create + launch: zoomed screen recording of the product (menus, prompt box, generated ads, campaign form); each UI step 1.3-3.9 s, subtitle pill continues over the UI.
- 20.3-23.5 turn: back to the talking head for the pain point (wasting ad money).
- 23.5-35.4 learn: reporting UI (dashboard, charts, top creatives) 1.4-5.5 s per step.
- 35.4-38.7 CTA: talking head, connect and try it.
- 38.7-42.7 end: Canva / Design School logo animation on white (≈4 s), then 0.4 s silence.

Cut rhythm
- 14 shots, ASL 3.05 s, median 3.25 s, 0 % < 1 s, ≈20 shots/min. Quarters 2.67 / 2.14 / 2.14 / 3.56 s.
- 69 % of cuts on audio onsets vs 54 % chance: cuts on the VO's step words (create, launch, learn).
- Zooms and pans inside the screen recording replace many cuts.

Typography
- Subtitle pills: white sentence case on a purple rounded box (≈#7D2AE8), cap ≈1.6 % H, 1-2 lines, 3-7 words, centred at ≈80-85 % H (low, inside the bottom UI zone on TikTok/Reels).
- Name tag: small purple pill with the first name + a grey-highlighted "Canva Verified Expert" line, cap ≈2.8 % H, at 65-71 % H.
- UI headlines come from the product at native size (e.g. "Create ads in seconds" ≈33 % H).
- Closest free: Figtree 500 (Canva Sans look).

Colour/grade
- Talking head: dark blue-violet room, red cap, warm key, shallow focus. UI: white with Canva purple and blue-cyan gradients.

Camera/shots
- Locked medium close-up with a studio mic; full-frame screen recordings with animated zoom, cursor and typing.

Transitions
- Hard cuts; animated zoom/pan inside the UI; logo animation at the end.

Sound
- VO + upbeat bed; -10.9 LUFS (loud), LRA 3.5 LU, true peak +0.5 dBTP. Hits +52 dB at 11.05 s and +44 dB at 32.35 s on music accents.

What makes it premium
- One question hook, then a strict 3-step structure that matches the product's own words.
- An external creator with a credential tag gives trust (expert, not brand).
- Subtitles in brand-colour pills keep the design system on screen even over a busy UI.

Recipe (real footage + HTML/GSAP, 1080x1920)
- 40-45 s: 4 s question hook, 3 steps of 8-12 s each as zoomed screen recordings, 3 s talking-head turn between steps 2 and 3, 3 s CTA, 3-4 s logo.
- Pill: `background:#7D2AE8; color:#fff; font:500 34px Figtree; border-radius:18px; padding:10px 22px`; place at y 1250-1400 px (not Canva's ≈1590 px) to clear the platform UI.
- UI zoom: `gsap.to(ui,{scale:1.6, x:-180, y:-240, duration:0.6, ease:"power2.inOut"})` per step.
