# Finding real footage that is good enough

Good stock is real (not AI), sharp at native resolution, licensed for the use, free of other brands, and it fits the story. Search for what is *in* the picture, not for what the shot means.

## Hard rules
1. **Floor 1920×1080, prefer 4K** (3840×2160+). 4K gives room to reframe, punch in and stabilise. Photos: long side ≥ 2400 px.
2. **One frame rate for the film.** Choose it first (25p Europe, 24/23.976p film look, 30p US web). Double rate (50/60p) = 2× slow motion or drop frames. Avoid 30p↔25p mixes; never use interlaced material.
3. **No AI-generated stock** unless the client agrees. Use the site's AI label, then look yourself (hands, text, signs, physics, morphing, too-perfect light).
4. **No third-party logos or readable brands**, and nobody who seems to endorse the product. Blur, crop or drop.
5. **No editorial-only or non-commercial content in an ad** (news photos, ESA Standard Licence, Mixkit "Restricted", CC BY-NC/ND).
6. **Licence log line for every clip you use.** No line, no clip.

## Workflow
1. **Shot list first.** One row per shot: purpose in the story, length, framing, camera move, light, fps.
2. **3–5 queries per shot:** subject + action + framing + move + light (`tower crane aerial`, `crane lifting steel beam`, `construction site drone sunrise`). Add synonyms and `close up`, `macro`, `drone`, `tracking`, `slow motion`. Commons wants short literal queries.
3. **Search + download + gate:** `node scripts/stock_find.mjs "<query>" --n 8 --out <dir>` (see `scripts/README.md`). It searches Pexels, Pixabay, Mixkit and Wikimedia Commons without keys, takes the largest file by real pixel size, drops < 1080p, vertical, AI-labelled, Restricted and off-topic hits, runs the quality gate on each download, and writes a ranked `MANIFEST.md` with licence lines.
4. **Gate one file:** `python scripts/stock_qc.py clip.mp4 [--json]`. Verdicts:
   - **REJECT:** < 1080p, vertical, < 24 fps, < 4 s, interlaced, starved bitrate, letterbox leaving < 1080 lines, watermark band across the middle, out of focus, very shaky.
   - **ACCEPT-WITH-NOTES:** 1080p only, low bitrate (target ≈ 8 Mbit/s 1080p, 20 Mbit/s 4K H.264), soft, little native detail (possible upscale), handheld shake, clipped/crushed, cuts inside, VFR, HDR.
   - **ACCEPT:** no notes.
5. **Look at every pick yourself** at 100 %, full length: watermarks (the check is weak on locked-off shots), AI artefacts, logos, faces, fit to the story, fake 4K.
6. **Selects:** copy to the project as `<shot>_<source>_<id>.<ext>`, note trim in/out (stock often starts or ends on a bump), transcode webm/VP9 to an edit codec.
7. **Log:** shot, file, source page, author, licence + URL, credit needed, AI checked, logos/people checked, date.

Test result (Oct 2026, 5 queries, no keys): 287 hits → 25 downloads → 7 ACCEPT, 17 with notes, 1 reject; 24 of 25 were 4K. Aerial and wide shots pass clean; dark close-up "tech" shots almost always get notes ("soft", "low detail"), so check them by eye.

## Sources (checked Oct 2026; licences change, save the licence page with hero clips)

| Source | Licence in one line | Max res | AI risk |
|---|---|---|---|
| Pexels | Free commercial, no credit; no implied endorsement | 4K (4096×2160 seen) | Low (AI uploads banned) |
| Pixabay | Free commercial, no credit; trademark + people limits | ~4K | Medium-high: AI allowed with a badge; tech topics hit hardest |
| Mixkit | Per clip: "Free" = commercial OK; "Restricted" = personal 720p only | 2160p on some | Low |
| Wikimedia Commons | Per file PD / CC0 / CC BY (credit) / CC BY-SA (credit + share-alike) | as uploaded, 4K webm exists | Low; filter `-hastemplate:PD-algorithm` |
| NASA Image Library / SVS | Mostly public domain; credit NASA, no endorsement, no logo | up to 4K | Low |
| Unsplash | Photos, free commercial | full camera size | Low |
| Coverr, Freepik/Videvo | Mixed human + AI clips | HD–4K | High: avoid when you need real footage |
| ESA | Non-commercial unless stated | — | Low, but licence blocks ads |
| Artgrid/Artlist | Paid; filmmaker-shot sequences, graded + LOG, up to 8K | 8K | Medium: check each clip |
| Storyblocks | Paid volume B-roll, "human-made" promise | 4K | Lowest |
| Adobe Stock | Paid; always filter out generative AI | 4K | High unless filtered |
| Getty/iStock, Shutterstock | Paid; editorial ≠ advertising | 4K | Low |

## Other real material
| Material | Use | Notes |
|---|---|---|
| News headlines/articles | Quotation for commentary only | Crop to the line you discuss, show publication + date, remove banners and ads, don't reproduce whole articles. National quotation law differs (e.g. DE §51 UrhG, US fair use). |
| A company's own videos (YouTube, product pages) | Internal only (pitch to a jury, private review) unless permission | Never in a public post; mark the cut as internal. |
| Your own or the client's filming | Anything | Best source. Ask for 3–5 specific shots per scene: wide, medium, detail, action, reaction. |
| Music and SFX | Licensed libraries (Pixabay, Artlist, Epidemic, Musicbed, Freesound CC0) | Log every file. Offer 2–3 music options with one mood line each; never pick music alone for a client. |
| Fonts | Installed or OFL (Google Fonts) | Embed with `@font-face`; check the licence before shipping files. |
