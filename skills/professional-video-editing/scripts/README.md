# Scripts

Command-line helpers for measuring edits, sourcing stock footage and finishing audio. They need
ffmpeg + ffprobe 5.1 or newer on PATH (a "full" build with libfreetype, vidstab and blurdetect).
The Python scripts use the standard library only (Python 3.8+). The finder needs Node 20+.
Every script prints its usage with `--help`. Use `python3` on macOS/Linux and `python` (or `py`) on Windows.

## analyze_video.py: measure how a video is cut and mixed

Point it at a finished film (a reference you want to learn from, or your own cut) to get numbers
instead of impressions. It writes `metrics.json`: the shot list with start/end times, cut count,
average and median shot length (ASL), % of shots under 1 s, shots per minute, ASL per quarter
(does the edit speed up?), longest/shortest shots, black flashes, dissolve candidates, integrated
loudness (LUFS), loudness range and true peak, silences and drop-outs of 0.3 s or more, the
biggest loudness hits, and how many cuts land on an audio onset compared with chance. It also
writes `sheet.jpg`, a 1-frame-per-second contact sheet in which each tile is labelled with the
real timestamp of the frame shown. Default cut detection is ffmpeg's scene score, which **misses
cuts in dark or low-contrast footage**. Use `--detector adaptive` (or a lower `--threshold`) for
trailers and night scenes, and `--cut-sheet` to check every detected cut by eye.

```
python3 analyze_video.py reference.mp4 --out analysis/reference --cut-sheet
python3 analyze_video.py trailer.mp4 --out analysis/trailer --detector adaptive --end 118.5
```

## stock_qc.py: quality gate for one stock clip or photo

Decides ACCEPT, ACCEPT-WITH-NOTES or REJECT from the file itself, not from the site's labels. It
rejects clips below 1080p, vertical, under 24 fps, under 4 s, interlaced, with a starved bitrate,
with letterbox bars that leave under 1080 lines, with a stock-preview watermark band, or very soft
or shaky. It adds notes for 1080p-only clips, low bitrate, soft or upscaled-looking detail, shake,
clipped highlights, crushed blacks, cuts inside the clip, VFR and HDR. It works on local files and
on URLs (it reads them with range requests). Use `--json` for the full metrics.

```
python3 stock_qc.py clip.mp4
python3 stock_qc.py https://example.org/clip.mp4 --json --out clip_qc.json
```

## stock_find.mjs: find, download and rank stock footage (no API keys)

Searches Pexels, Pixabay, Mixkit and Wikimedia Commons for a query and keeps the
highest-resolution file of each hit. Before downloading, it drops hits below `--min-height`
(default 1080), vertical clips, clips under 4 s or 24 fps, AI-labelled clips, Mixkit "Restricted"
(personal-use) clips, NC/ND licences and off-topic hits. It prefers 4K over 2K over 1080p. It
downloads the top `--n` clips into `--out`, runs `stock_qc.py` on each one, and writes
`MANIFEST.md`: a ranked table with each verdict, the reasons, and a licence-log line for every
usable clip. Run `npm install` next to the script once; this installs Playwright and its
Chromium, which only keyless Pixabay needs. Set `STOCK_PY` if your Python command is not
`python3` (`python` on Windows). `PEXELS_API_KEY` and `PIXABAY_API_KEY` are optional, and
`STOCK_CONTACT` sets the contact address that Wikimedia asks for. Look at every ACCEPT yourself:
the gate cannot see logos, faces, AI artefacts, or whether a clip fits the story.

```
npm install
node stock_find.mjs "tower crane aerial" --n 8 --out footage/crane
node stock_find.mjs "robot arm close up" --sources pexels,commons --min-height 2160 --out footage/robot
node stock_find.mjs "steel beam" --photos --n 5 --out footage/stills
```

## loudness.sh: measure, master and add a poster frame

`measure` prints integrated loudness, loudness range and true peak (EBU R128). `master` runs
two-pass `loudnorm` with a linear gain to -14 LUFS, -1.5 dBTP true peak and LRA 11 (the targets
can be changed). It copies the video stream unchanged, writes AAC 320k / 48 kHz audio and
measures the result again. Use -14 LUFS for web/social and -23 LUFS for EBU broadcast. `poster`
puts a poster image on frame 0 only, scaled and padded to the video size. Platforms that use the
first frame as the thumbnail then show the poster, and duration and sync stay the same. The
script's header lists the plain ffmpeg one-liners for each step.

```
bash loudness.sh measure final.mp4
bash loudness.sh master final.mp4 final_-14.mp4            # or: ... final_-23.mp4 -23 -1 15
bash loudness.sh poster final_-14.mp4 poster.png final_upload.mp4
```

## select_media.py
Rank candidate images/clips for one shot by how they will really look on screen: give the crop the shot will use (`file.jpg@x,y,w,h`, fractions of the source), the output frame and the largest push-in. Reports upscale factor, sharpness at output size, background clutter, exposure and a HERO / USE / WEAK / REJECT verdict, and writes a labelled contact sheet. It judges technique only; check meaning on the sheet.
```
python select_media.py robot1.jpg@0.28,0.08,0.6,0.6 robot2.jpg clip.mp4 --frame 1920x1080 --zoom 1.07 --look dark --sheet selects.jpg
```

## music_map.py
Map candidate music before cutting: loudness strip, hits, built-in drop-outs, button vs fade ending, a rough vocal hint, and (with `--want-hit`) the source offsets that land a hit on your story's turn.
```
python music_map.py track1.mp3 track2.mp3 --want-hit 10.3 --length 20
```
