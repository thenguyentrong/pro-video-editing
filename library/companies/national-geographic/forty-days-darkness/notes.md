# For 40 Days of the Year, These People Live in Complete Darkness | Short Film Showcase  (National Geographic, 2018-01-07, 4:19 = 224.6 s film + 20 s credits + 14 s channel end screen, 16:9 file with ≈2.35:1 picture, YouTube / National Geographic channel)
URL: https://www.youtube.com/watch?v=C_HNPVi_uZQ
Purpose: independent short documentary presented in the brand's "Short Film Showcase" (film title on screen: "Return of the Sun")
One-sentence point: after 40 days without sun, an Inuit fisherman's family in East Greenland watches it return, while the sea ice they live from is changing.

Structure (0–224.6 s, credits excluded):
- 0–4.6 BLACK with "a film by / [two names]" in small caps (italic eyebrow), centred.
- 4.6–17.4 BLIZZARD: a white-out village wide (5.1 s), two figures walking in snow (7.7 s); title "RETURN OF THE SUN" in small sans caps centred low in the frame (≈11–17).
- 17.4–25 a figure on a stormy shore with the brand laurel "NATIONAL GEOGRAPHIC / SHORT FILM SHOWCASE / OFFICIAL SELECTION" (≈19–21.5).
- 25–33 tight portraits: an old man's glasses, a child in a fur hood, subtitles for the spoken language.
- 33.2–52.7 SUN: an 11.7 s hold of the sun at the horizon under heavy cloud (the longest shot) and a 7.9 s pink-ice shot, voice over them.
- 52.7–66.4 6.3 s CONTEXT TEXT on black (60.1–66.4): two lines of small white sans about sea ice changing; level drops to -26/-27 dBFS.
- 66–125 FISHING BY DOGSLED: sled dogs, the fisherman, hands and ropes, a husky portrait, sea ice textures, a sled seen from the back with the dog team ahead (3–7 s shots).
- 125–153 WAITING: binoculars macro reflecting the dusk (5 s), icebergs, the boat on ice, the sun under the edge; loudest hits at 153.2 (+22.9 dB) and 97.5.
- 153–186 FAMILY AND TOWN: children in a classroom, the school at night, a boy drawing a sun with crayons, sun drawings on a wall.
- 186–224.6 RETURN: snow storm, the coloured village under snow, figures walking out on the ice, the sun rising over the sea, a final portrait of the fisherman in his fur hood (fade out, level to -35 dBFS).

Cut rhythm (0–224.6 s): 51 shots, ASL 4.40 s, median 4.08 s (adaptive detector; the scene detector found far fewer cuts in the white-out snow). ASL per quarter 5.62 / 3.74 / 4.01 / 3.74 s. Only 2 % of shots under 1 s, 76.5 % over 3 s; longest 11.7 s (sun), 8.4 s (binoculars), 7.9 s and 7.7 s. Cuts per 10 s: 2, 1, 2, 1, 1, 2, 2, 3, 3, 2, 3, 3, 2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 1. Black holds 4.6 s (open) and 6.3 s (context text). Cut-on-onset 22 % (chance value broken in this clipped run).

Typography:
- Credit: italic serif eyebrow "a film by" ≈1.3 % H over names in small sans caps ≈2 % H, centred on black.
- Title: clean geometric sans caps (closest free: Josefin Sans 400 / Montserrat 400), dark grey on the white snow, cap ≈3 % H, centred at y ≈59 %, held ≈6 s.
- Showcase laurel: the brand's yellow frame + wordmark + two lines of small caps, white, inside two laurel branches, ≈25 % H tall, centred on footage.
- Context text: small white sans ≈2 % H, 2 lines, centred on black, 6 s.
- Subtitles: white sans ≈2.5 % H, inside the picture near its bottom (y ≈80 %).

Colour/grade: cold, desaturated blue-white snow and grey sea; warm orange only for the sun and sunsets (the story's colour); interiors warm and dim. ≈2.35:1 letterbox throughout.

Camera/shots: locked and slow tripod wides in blizzards, tight portraits, observational fishing on the ice, macro (binoculars, hands, crayons), a POV from the sled behind the dogs. Almost no drone.

Transitions: hard cuts; fades from and to black for the credit, the context card and the end.

Sound: (I could not listen; from level data.) Integrated -16.6 LUFS, LRA 12.1 LU, true peak +1.8 dBTP (clips). Quiet start (-24…-26 dBFS), wind and voice at -15…-18 in the body, a dip to -26/-27 under the context text, peaks at 97.5 and 153.2 s, fade to -35 at the end. No silences or drop-outs (wind is always there).

What makes it premium:
- Slow, confident holds (median 4.1 s) with one 11.7 s sun shot at the centre of the story.
- One colour idea: cold blue world, warm orange only for the sun (and the child's drawing of it).
- The brand appears as a festival-style laurel ("official selection"), not a logo sting.
- Context is given once, on black, in two lines; the rest is the people's own words.

Recipe (real footage + HTML/GSAP, Hyperframes, 1920x1080, picture 1920x818):
- 0–4.6 s black with credit `italic 400 1.3vh "Cormorant Garamond"` + `500 2vh Montserrat; text-transform:uppercase`.
- Blizzard wides 5–8 s each; title `400 3vh "Josefin Sans"; letter-spacing:.08em; color:#333` on white snow, fade 1 s, hold 6 s.
- Laurel badge 2.5 s on a wide (SVG laurels + brand mark + 2 lines `500 1.8vh`).
- Body ASL 4–4.5 s, nothing under 1 s; one 10–12 s hero hold on the story's symbol.
- Context card 6 s on black, `400 2vh Inter`, 2 lines; music down 8–10 dB.
- Grade: `saturate(.7)` on cold shots, keep the warm source untouched. Master -16 to -18 LUFS, true peak ≤ -1 dBTP.
- Stock queries: `greenland dog sled sea ice`, `arctic village snow storm`, `sun on horizon arctic winter`, `inuit fisherman portrait`.
