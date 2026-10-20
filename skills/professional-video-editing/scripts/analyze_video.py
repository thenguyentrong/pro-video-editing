#!/usr/bin/env python3
"""Measure the edit of a finished video: cuts, shot lengths, loudness, silences, hits.

    python analyze_video.py <video> --out <dir> [--name <slug>] [--detector scene|adaptive]
                            [--threshold 0.3] [--end S] [--add-cuts 3.2,7.9] [--drop-cuts 5.04]
                            [--cut-sheet] [--no-sync] [--no-sheet]

Writes into --out:
  metrics.json  duration, fps, shot list (start/end/len), cut count, ASL (average shot length),
                median, % shots < 1 s, shots per minute, ASL per quarter, longest/shortest shots,
                cuts per 10 s, black flashes/holds, soft-transition candidates (dissolves, fades),
                integrated loudness (LUFS), loudness range (LU) and true peak (dBTP) via ebur128,
                silences and relative drop-outs >= 0.3 s with times, biggest loudness hits,
                loudest 0.5 s, and cut-to-onset sync (% of cuts within +-0.1 s of an audio onset,
                against the chance rate for the same number of random cuts).
  sheet.jpg     contact sheet, 1 frame per second, 8 columns. Tile n shows the frame that is on
                screen at n seconds (the last frame with pts <= n: exactly n.00 s at 25/50 fps,
                up to one frame earlier at 23.976/29.97) and is labelled with that frame's own
                source timestamp, so the label is always the time of the picture you see.
                Videos longer than --sheet-max seconds get sheet_p01.jpg, sheet_p02.jpg ... instead.
  cuts_01.jpg   (only with --cut-sheet) last frame before | first frame after every cut,
                to spot false cuts by eye.

Cut detection
  scene     (default) ffmpeg's scene score > --threshold (0.3). Fast and good on normal footage.
            LIMIT: it MISSES CUTS IN DARK OR LOW-CONTRAST FOOTAGE (night shots, trailers, smoke,
            black-and-white), because the score is an absolute pixel difference. Test: a
            5-cut clip dimmed to mean luma 0.12 -> scene 0.3 found 0 cuts, scene 0.15 found 4,
            adaptive found all 5. Lower --threshold (0.15-0.2) or use --detector adaptive there;
            near-black footage (mean luma < 0.02) also needs --min-diff 0.1. It can also fire on flashes,
            whip pans and fast text changes: check with --cut-sheet.
  adaptive  contrast-normalised, shift-tolerant frame difference on a 48x27 copy, compared with
            the 8 neighbouring frames (--ratio 3.0, --min-diff 0.25). Finds dark cuts; slower.
  The other detector always runs too; metrics.json reports its cut count as a cross-check.
  Black flashes shorter than 0.5 s between two shots are folded into the transition.
  Dissolves and fades are NOT counted as cuts; they are listed as soft-transition candidates.
  Add verified ones with --add-cuts, remove false ones with --drop-cuts (times in seconds).

Requirements: Python 3.8+, standard library only; ffmpeg + ffprobe 5.1+ on PATH (with
libfreetype for the sheet labels; without it the sheet is written unlabelled).
"""
import argparse
import array
import json
import math
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile

GW, GH = 48, 27          # analysis frame for the adaptive detector, luma and soft transitions
SR = 16000               # audio analysis sample rate
WIN = 0.05               # audio window, s (50 ms RMS)
LABEL_EXPR = r"%{eif\:floor(round(t*100)/100)\:d}.%{eif\:mod(round(t*100)\,100)\:d\:2}s"


# ---------------------------------------------------------------- helpers

def run(args, binary=False):
    p = subprocess.run(args, capture_output=True)
    if binary:
        return p.stdout, p.stderr.decode("utf-8", "replace"), p.returncode
    return p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace"), p.returncode


def need(tool):
    if not shutil.which(tool):
        sys.exit(f"error: {tool} not found on PATH")


def probe(path):
    out, err, rc = run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", path])
    if rc != 0:
        sys.exit("ffprobe failed: " + err.strip()[:300])
    info = json.loads(out)
    v = next((s for s in info["streams"] if s.get("codec_type") == "video"
              and not (s.get("disposition") or {}).get("attached_pic")), None)
    has_audio = any(s.get("codec_type") == "audio" for s in info["streams"])
    dur = float(info["format"].get("duration") or (v or {}).get("duration") or 0)

    def frac(x):
        try:
            a, b = str(x).split("/")
            return float(a) / float(b) if float(b) else 0.0
        except ValueError:
            return 0.0
    fps = frac(v.get("avg_frame_rate")) or frac(v.get("r_frame_rate")) if v else 0.0
    return v, has_audio, dur, fps


def find_font(user_font):
    if user_font:
        return user_font if os.path.isfile(user_font) else None
    windir = os.environ.get("WINDIR", r"C:\Windows")
    cands = [os.path.join(windir, "Fonts", f) for f in ("arial.ttf", "segoeui.ttf", "calibri.ttf")] + [
        "/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc", "/System/Library/Fonts/SFNS.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/liberation-sans/LiberationSans-Regular.ttf", "/usr/share/fonts/noto/NotoSans-Regular.ttf"]
    return next((c for c in cands if os.path.isfile(c)), None)


def drawtext(font, text, size=20, color="yellow", x=6, y=6):
    """drawtext filter string; text is used verbatim (may contain %{...} expansions)."""
    f = ""
    if font:
        f = "fontfile='" + font.replace("\\", "/").replace(":", "\\:") + "':"
    return (f"drawtext={f}text='{text}':x={x}:y={y}:fontsize={size}:fontcolor={color}:"
            "box=1:boxcolor=black@0.7:boxborderw=3")


def has_filter(name):
    out, _, _ = run(["ffmpeg", "-hide_banner", "-filters"])
    return re.search(rf"^\s*\S+\s+{name}\s", out, re.M) is not None


# ---------------------------------------------------------------- video pass

def video_pass(path):
    """One decode: ffmpeg scene score + pts per frame (stderr), 48x27 gray frames (stdout)."""
    vf = (r"scale=426:-2,select='gte(scene\,0)',metadata=print,"
          f"scale={GW}:{GH}:flags=area,format=gray")
    args = ["ffmpeg", "-hide_banner", "-nostats", "-loglevel", "info", "-i", path, "-map", "0:v:0", "-an",
            "-fps_mode", "passthrough", "-vf", vf, "-f", "rawvideo", "-pix_fmt", "gray", "pipe:1"]
    frames = []
    size = GW * GH
    with tempfile.TemporaryFile() as errf:
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=errf)
        buf = b""
        while True:
            chunk = p.stdout.read(size * 64)
            if not chunk:
                break
            buf += chunk
            n = len(buf) // size
            frames.extend(buf[i * size:(i + 1) * size] for i in range(n))
            buf = buf[n * size:]
        p.wait()
        errf.seek(0)
        err = errf.read().decode("utf-8", "replace")
    pts, scores = [], []
    for line in err.splitlines():
        m = re.search(r"\bframe:\s*\d+\s+pts:\s*\S+\s+pts_time:\s*(-?[\d.]+)", line)
        if m:
            pts.append(float(m.group(1)))
            scores.append(0.0)
            continue
        m = re.search(r"lavfi\.scene_score=([\d.]+)", line)
        if m and scores:
            scores[-1] = float(m.group(1))
    return frames, pts, scores


def frame_stats(frames):
    lum, std = [], []
    for f in frames:
        n = len(f)
        s = sum(f)
        s2 = sum(v * v for v in f)
        m = s / n
        lum.append(m / 255.0)
        std.append(math.sqrt(max(0.0, s2 / n - m * m)) / 255.0)
    return lum, std


def sdiff(a, b, s=1):
    """Shift-tolerant mean absolute difference (0..1) of two GWxGH gray frames."""
    best = 1e9
    for dy in range(-s, s + 1):
        for dx in range(-s, s + 1):
            tot = 0
            cnt = 0
            x0, x1 = max(0, dx), GW + min(0, dx)
            for y in range(max(0, dy), GH + min(0, dy)):
                ra = y * GW
                rb = (y - dy) * GW - dx
                tot += sum(map(abs, map(int.__sub__, a[ra + x0:ra + x1], b[rb + x0:rb + x1])))
                cnt += x1 - x0
            v = tot / cnt
            if v < best:
                best = v
    return best / 255.0


def cuts_scene(pts, scores, th, fps):
    min_gap = 2.5 / (fps or 25)
    cuts = []
    for t, s in zip(pts, scores):
        if t < 0.05 or s <= th:
            continue
        if cuts and t - cuts[-1] < min_gap:
            continue
        cuts.append(round(t, 3))
    return cuts


def cuts_adaptive(frames, pts, std, ratio, abs_min):
    n = len(frames)
    d = [0.0] * n
    for i in range(1, n):
        d[i] = sdiff(frames[i - 1], frames[i]) / (0.5 * (std[i - 1] + std[i]) + 0.04)
    cuts = []
    last = -10
    for i in range(1, n):
        nb = d[max(1, i - 4):i] + d[i + 1:i + 5]
        ref = sum(nb) / len(nb) if nb else 0.0
        if d[i] > abs_min and d[i] > ratio * (ref + 0.02) and i - last >= 3 and pts[i] >= 0.05:
            cuts.append(round(pts[i], 3))
            last = i
    return cuts


def soft_and_dips(frames, pts, lum, std, hard, soft_th=0.10):
    """Dissolve/fade candidates (difference across +-0.4 s at 10 samples/s) and black dips."""
    if not frames:
        return [], []
    dur = pts[-1]
    idx, j = [], 0
    for k in range(int(dur * 10) + 1):
        t = k / 10.0
        while j + 1 < len(pts) and abs(pts[j + 1] - t) <= abs(pts[j] - t):
            j += 1
        idx.append(j)
    K = 4
    D = [0.0] * len(idx)
    for k in range(K, len(idx) - K):
        a, b = idx[k - K], idx[k + K]
        D[k] = sdiff(frames[a], frames[b], 0) / (0.5 * (std[a] + std[b]) + 0.03)
    soft = []
    for k in range(K, len(idx) - K):
        t = k / 10.0
        if D[k] < soft_th or D[k] < max(D[max(0, k - 5):k + 6]):
            continue
        if any(abs(t - h) < 0.6 for h in hard):
            continue
        soft.append({"t": round(t, 1), "score": round(D[k], 3)})
    dips = []
    s_l = [lum[i] for i in idx]
    k = 0
    while k < len(s_l):
        if s_l[k] < 0.025:
            m = k
            while m + 1 < len(s_l) and s_l[m + 1] < 0.025:
                m += 1
            before, after = s_l[max(0, k - 10):k], s_l[m + 1:m + 11]
            if before and after and max(before) > 0.05 and max(after) > 0.05:
                dips.append({"start": round(k / 10, 1), "end": round((m + 1) / 10, 1)})
            k = m + 1
        else:
            k += 1
    return soft, dips


def shot_stats(cuts, end, lum, pts):
    """stats2 logic: fold black flashes < 0.5 s, then shot statistics."""
    def seg_lum(s0, s1):
        return [l for t, l in zip(pts, lum) if s0 + 0.02 < t < s1 - 0.02]
    b = [0.0] + cuts + [end]
    keep, flashes, holds = [], [], []
    for i in range(len(b) - 1):
        s0, s1 = b[i], b[i + 1]
        seg = seg_lum(s0, s1)
        black = bool(seg) and max(seg) < 0.03
        if black and (s1 - s0) < 0.5 and 0 < i < len(b) - 2:
            flashes.append(round(s0, 2))
            continue
        if black:
            holds.append({"start": round(s0, 2), "len": round(s1 - s0, 2)})
        if i + 1 < len(b) - 1:
            keep.append(s1)
    b = [0.0] + keep + [end]
    shots = [{"i": k + 1, "start": round(b[k], 3), "end": round(b[k + 1], 3), "len": round(b[k + 1] - b[k], 3)}
             for k in range(len(b) - 1)]
    lens = [s["len"] for s in shots]
    q = []
    for k in range(4):
        a0, a1 = end * k / 4, end * (k + 1) / 4
        nn = sum(1 for s in shots if s["start"] < a1 and s["end"] > a0)
        q.append(round((a1 - a0) / nn, 2) if nn else None)
    win = {f"{w0}-{w0 + 10}": sum(1 for t in keep if w0 <= t < w0 + 10) for w0 in range(0, int(math.ceil(end)), 10)}
    top = lambda key, rev: [{"start": s["start"], "len": s["len"]}
                            for s in sorted(shots, key=lambda s: s["len"], reverse=rev)[:3]]
    return {
        "cut_count": len(keep), "shot_count": len(shots),
        "asl_s": round(end / len(shots), 2), "median_s": round(statistics.median(lens), 2),
        "pct_shots_under_1s": round(100 * sum(1 for x in lens if x < 1) / len(lens), 1),
        "pct_shots_over_3s": round(100 * sum(1 for x in lens if x > 3) / len(lens), 1),
        "shots_per_minute": round(60 * len(shots) / end, 1) if end else None,
        "asl_quarters_s": q, "longest": top(None, True), "shortest": top(None, False),
        "cuts_per_10s": win, "black_flashes_folded": flashes, "black_holds": holds,
    }, shots, keep


# ---------------------------------------------------------------- audio

def ebur128(path):
    _, err, _ = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-map", "0:a:0", "-vn",
                     "-af", "ebur128=peak=true", "-f", "null", "-"])
    tail = err[err.rfind("Summary:"):] if "Summary:" in err else err
    g = lambda rx: (float(m.group(1)) if (m := re.search(rx, tail)) else None)
    return {"integrated_lufs": g(r"I:\s*(-?[\d.]+|-inf) LUFS"),
            "loudness_range_lu": g(r"LRA:\s*(-?[\d.]+) LU"),
            "true_peak_dbtp": g(r"Peak:\s*(-?[\d.]+|-inf) dBFS")}


def rms_db(path):
    data, _, rc = run(["ffmpeg", "-v", "error", "-i", path, "-map", "0:a:0", "-vn", "-ac", "1", "-ar", str(SR),
                       "-f", "s16le", "-acodec", "pcm_s16le", "pipe:1"], binary=True)
    x = array.array("h")
    x.frombytes(data[:len(data) // 2 * 2])
    if sys.byteorder == "big":
        x.byteswap()
    w = int(WIN * SR)
    out = []
    for k in range(len(x) // w):
        seg = x[k * w:(k + 1) * w]
        ms = sum(v * v for v in seg) / w / (32768.0 ** 2)
        out.append(round(10 * math.log10(ms + 1e-12), 1))
    return out


def audio_events(db, min_gap, end):
    nw = min(len(db), int(end / WIN) + 1)
    db = db[:nw]
    silences, dropouts = [], []
    i = 0
    while i < nw:  # absolute silence: below -50 dBFS
        if db[i] < -50:
            j = i
            while j + 1 < nw and db[j + 1] < -50:
                j += 1
            if (j - i + 1) * WIN >= min_gap - 1e-9:
                silences.append({"start": round(i * WIN, 2), "end": round((j + 1) * WIN, 2),
                                 "len": round((j - i + 1) * WIN, 2)})
            i = j + 1
        else:
            i += 1
    i = 20
    while i < nw:  # drop-out: >= 18 dB under the median of the previous 3 s, then back within 0.6 s
        ref = statistics.median(db[max(0, i - 60):i])
        if db[i] < ref - 18 and ref > -45:
            j = i
            while j + 1 < nw and db[j + 1] < ref - 18:
                j += 1
            ln = (j - i + 1) * WIN
            after = db[j + 1:j + 13]
            if ln >= min_gap - 1e-9 and after and max(after) >= ref - 6:
                k = j + 1 + after.index(max(after))
                dropouts.append({"start": round(i * WIN, 2), "end": round((j + 1) * WIN, 2), "len": round(ln, 2),
                                 "level_before_db": round(ref, 1), "floor_db": min(db[i:j + 1]),
                                 "next_peak_db": db[k], "next_peak_t": round(k * WIN, 2)})
            i = j + 1
            continue
        i += 1
    hits = []
    for i in range(10, nw):
        rise = db[i] - min(db[i - 10:i])
        if rise >= 15:
            hits.append((db[i], round(rise, 1), round(i * WIN, 2)))
    def one_per_second(hs):
        out = []
        for h in hs:
            if all(abs(h[2] - o[2]) > 1.0 for o in out):
                out.append(h)
        return out
    sel = one_per_second(sorted(hits, key=lambda h: (-h[0], -h[1], h[2])))
    rises = one_per_second(sorted(hits, key=lambda h: (-h[1], -h[0], h[2])))
    loud = None
    if nw >= 10:
        sm = [sum(db[k:k + 10]) / 10 for k in range(nw - 9)]
        kk = max(range(len(sm)), key=sm.__getitem__)
        loud = {"t": round(kk * WIN, 2), "rms_dbfs": round(sm[kk], 1)}
    return {"silences": silences, "dropouts": dropouts,
            "hits": [{"t": t, "level_dbfs": lv, "rise_db": r} for lv, r, t in sel[:15]],
            "biggest_rises": [{"t": t, "level_dbfs": lv, "rise_db": r} for lv, r, t in rises[:5]],
            "loudest_0_5s": loud, "median_rms_dbfs": round(statistics.median(db), 1) if db else None}


def onset_sync(db, cuts, end, tol=0.1):
    on = []
    for i in range(4, len(db) - 1):
        if db[i] - min(db[i - 4:i]) >= 6 and db[i] >= db[i + 1] - 1 and db[i] > -40:
            if not on or (i * WIN - on[-1]) > 0.15:
                on.append(i * WIN)
    if not cuts or not on or end <= 1:
        return {"onsets_per_s": round(len(on) / end, 2) if end else None, "cuts_on_onset_pct": None,
                "chance_pct": None, "note": "no cuts or no onsets"}
    hit = sum(1 for t in cuts if any(abs(t - o) <= tol for o in on))
    # chance = share of the timeline within +-tol of an onset (where a random cut would count as on-beat)
    cov, cur0, cur1 = 0.0, None, None
    for o in on:
        a, b = max(0.0, o - tol), min(end, o + tol)
        if cur1 is None or a > cur1:
            if cur1 is not None:
                cov += cur1 - cur0
            cur0, cur1 = a, b
        else:
            cur1 = max(cur1, b)
    cov += (cur1 - cur0) if cur1 is not None else 0
    return {"onsets_per_s": round(len(on) / end, 2), "cuts_on_onset_pct": round(100 * hit / len(cuts)),
            "chance_pct": round(100 * cov / end), "tolerance_s": tol}


# ---------------------------------------------------------------- sheets

def contact_sheet(path, out_dir, dur, font, labels, cols, sheet_max):
    """1 frame/s. The fps filter rounds every frame's pts to whole seconds and keeps the LAST frame
    per slot. round=down (old tool) therefore put the frame from just before n+1 s (0.96 s at 25 fps)
    into slot n while the label, drawn after fps from the slot time, said n: labels ~0.96 s early.
    round=up keeps the last frame with pts <= n, i.e. the frame on screen at n s. The label is drawn
    BEFORE the fps filter from the source frame's own pts, so it always names the frame shown."""
    lab = (drawtext(font, LABEL_EXPR) + ",") if labels else ""
    total = int(math.floor(dur)) + 1
    parts = [(0, total)] if total <= sheet_max else [(s, min(total, s + sheet_max)) for s in range(0, total, sheet_max)]
    files = []
    for k, (s0, s1) in enumerate(parts):
        rows = int(math.ceil((s1 - s0) / cols))
        trim = f"trim=start={s0}:end={s1 if s1 < total else dur + 1}," if len(parts) > 1 else ""
        vf = f"{trim}scale=320:-2,{lab}fps=1:round=up,tile={cols}x{rows}:padding=2:color=gray"
        name = "sheet.jpg" if len(parts) == 1 else f"sheet_p{k + 1:02d}.jpg"
        _, err, rc = run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", path, "-an", "-vf", vf,
                          "-frames:v", "1", "-q:v", "4", os.path.join(out_dir, name)])
        if rc != 0:
            raise RuntimeError(err.strip()[:300])
        files.append(name)
    return files


def cut_sheets(path, out_dir, pts, cuts, font, labels):
    """Pairs: last frame before | first frame after each cut, 6 pairs per row, 48 per image."""
    idx = []
    for c in cuts:
        i = min(range(len(pts)), key=lambda k: abs(pts[k] - c))
        idx.append((max(0, i - 1), i))
    files = []
    for k in range(0, len(idx), 48):
        chunk = idx[k:k + 48]
        sel = "+".join(f"eq(n\\,{a})+eq(n\\,{b})" for a, b in chunk)
        rows = int(math.ceil(len(chunk) / 6))
        lab = (drawtext(font, LABEL_EXPR, size=16) + ",") if labels else ""
        vf = f"scale=240:-2,{lab}select='{sel}',tile=12x{rows}:padding=4:color=gray"
        name = f"cuts_{k // 48 + 1:02d}.jpg"
        run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", path, "-an", "-fps_mode", "passthrough",
             "-vf", vf, "-frames:v", "1", "-q:v", "4", os.path.join(out_dir, name)])
        files.append(name)
    return files


# ---------------------------------------------------------------- main

def floats(s):
    return [float(x) for x in s.split(",") if x.strip()] if s else []


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video")
    ap.add_argument("--out", required=True, help="output folder (created if missing)")
    ap.add_argument("--name", help="slug stored in metrics.json (default: file name)")
    ap.add_argument("--detector", choices=("scene", "adaptive"), default="scene")
    ap.add_argument("--threshold", type=float, default=0.3,
                    help="scene-score threshold (default 0.3; 0.15-0.2 for dark/low-contrast footage)")
    ap.add_argument("--ratio", type=float, default=3.0, help="adaptive: diff must be this many times its neighbours")
    ap.add_argument("--min-diff", type=float, default=0.25, help="adaptive: minimum normalised diff")
    ap.add_argument("--end", type=float, help="ignore everything after this time (trailing black, end card)")
    ap.add_argument("--add-cuts", help="comma-separated cut times to add (verified soft transitions)")
    ap.add_argument("--drop-cuts", help="comma-separated cut times to remove (false positives, +-0.05 s)")
    ap.add_argument("--min-gap", type=float, default=0.3, help="shortest silence/drop-out to report, s")
    ap.add_argument("--no-sync", action="store_true", help="skip the cut-to-onset sync measure")
    ap.add_argument("--no-sheet", action="store_true", help="skip the contact sheet")
    ap.add_argument("--cut-sheet", action="store_true", help="also write cuts_NN.jpg before/after pairs")
    ap.add_argument("--cols", type=int, default=8, help="contact-sheet columns")
    ap.add_argument("--sheet-max", type=int, default=480, help="max tiles (seconds) per sheet image")
    ap.add_argument("--font", help="TTF/OTF file for labels (auto-detected otherwise)")
    a = ap.parse_args()

    need("ffmpeg")
    need("ffprobe")
    if not os.path.isfile(a.video):
        sys.exit(f"error: no such file: {a.video}")
    os.makedirs(a.out, exist_ok=True)
    name = a.name or re.sub(r"[^a-z0-9]+", "-", os.path.splitext(os.path.basename(a.video))[0].lower()).strip("-")
    v, has_audio, dur, fps = probe(a.video)
    if v is None:
        sys.exit("error: no video stream")
    font = find_font(a.font)
    labels = has_filter("drawtext")
    res = {"name": name, "file": os.path.basename(a.video), "duration_s": round(dur, 3), "fps": round(fps, 3),
           "width": v.get("width"), "height": v.get("height"), "detector": a.detector,
           "threshold": a.threshold if a.detector == "scene" else None}
    warnings = []

    print(f"[1/4] video pass ({dur:.1f} s)...", file=sys.stderr)
    frames, pts, scores = video_pass(a.video)
    n = min(len(frames), len(pts))
    if n == 0:
        sys.exit("error: could not decode video frames")
    if len(frames) != len(pts):
        warnings.append(f"frame/pts count mismatch ({len(frames)} vs {len(pts)}); used first {n}")
    frames, pts, scores = frames[:n], pts[:n], scores[:n]
    lum, std = frame_stats(frames)
    end = min(a.end, dur) if a.end else dur

    c_scene = cuts_scene(pts, scores, a.threshold, fps)
    c_adapt = cuts_adaptive(frames, pts, std, a.ratio, a.min_diff)
    raw = c_scene if a.detector == "scene" else c_adapt
    other = c_adapt if a.detector == "scene" else c_scene
    drop = floats(a.drop_cuts)
    cuts = sorted(set(t for t in raw if t < end - 0.05 and not any(abs(t - d) < 0.05 for d in drop))
                  | set(floats(a.add_cuts)))
    stats, shots, final_cuts = shot_stats(cuts, end, lum, pts)
    res.update(stats)
    res["cross_check"] = {"other_detector": "adaptive" if a.detector == "scene" else "scene",
                          "other_cut_count": len([t for t in other if t < end - 0.05]),
                          "only_in_other": [t for t in other if t < end - 0.05 and not any(abs(t - c) < 0.1 for c in raw)],
                          "only_in_this": [t for t in raw if t < end - 0.05 and not any(abs(t - c) < 0.1 for c in other)]}
    if res["cross_check"]["only_in_other"]:
        warnings.append(f"the {res['cross_check']['other_detector']} detector also finds cuts at "
                        f"{res['cross_check']['only_in_other'][:10]} s: check them (--cut-sheet) and use --add-cuts")
    if a.detector == "scene" and len(c_adapt) > 1.5 * len(c_scene) + 2:
        warnings.append(f"adaptive detector finds {len(c_adapt)} cuts vs {len(c_scene)}: dark/low-contrast "
                        "footage? try --detector adaptive or a lower --threshold, and check --cut-sheet")
    mean_lum = sum(lum) / len(lum)
    res["mean_luma"] = round(mean_lum, 3)
    if mean_lum < 0.15 and a.detector == "scene":
        warnings.append("dark footage (mean luma < 0.15): scene detection misses cuts here")
    soft, dips = soft_and_dips(frames, pts, lum, std, final_cuts)
    res["soft_transition_candidates"] = soft
    res["black_dips"] = dips
    res["shots"] = shots
    res["cuts"] = [round(t, 3) for t in final_cuts]
    del frames

    print("[2/4] audio...", file=sys.stderr)
    if has_audio:
        res["loudness"] = ebur128(a.video)
        db = rms_db(a.video)
        res["audio"] = audio_events(db, a.min_gap, end)
        res["sync"] = None if a.no_sync else onset_sync(db, final_cuts, end)
        tp = res["loudness"].get("true_peak_dbtp")
        if tp is not None and tp > -1.0:
            warnings.append(f"true peak {tp} dBTP above -1 dBTP: clipping risk after platform encoding")
    else:
        res["loudness"] = res["audio"] = res["sync"] = None
        warnings.append("no audio stream")

    print("[3/4] sheets...", file=sys.stderr)
    if not labels:
        warnings.append("ffmpeg has no drawtext filter (libfreetype): sheets are unlabelled")
    res["sheets"] = []
    if not a.no_sheet:
        try:
            res["sheets"] = contact_sheet(a.video, a.out, dur, font, labels, a.cols, a.sheet_max)
        except RuntimeError as e:
            if labels:
                warnings.append(f"labelled sheet failed ({e}); wrote it without labels")
                res["sheets"] = contact_sheet(a.video, a.out, dur, font, False, a.cols, a.sheet_max)
            else:
                raise
    if a.cut_sheet and final_cuts:
        res["cut_sheets"] = cut_sheets(a.video, a.out, pts, final_cuts, font, labels)
    res["warnings"] = warnings

    print("[4/4] write", file=sys.stderr)
    with open(os.path.join(a.out, "metrics.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)
    lo = res["loudness"] or {}
    sy = res["sync"] or {}
    print(f"{name}: {dur:.2f} s  {res['shot_count']} shots  {res['cut_count']} cuts  ASL {res['asl_s']} s  "
          f"median {res['median_s']} s  <1 s {res['pct_shots_under_1s']}%  {res['shots_per_minute']} shots/min")
    print(f"  ASL per quarter {res['asl_quarters_s']}  longest {res['longest'][0]}")
    if has_audio:
        print(f"  loudness {lo.get('integrated_lufs')} LUFS  LRA {lo.get('loudness_range_lu')} LU  "
              f"true peak {lo.get('true_peak_dbtp')} dBTP  silences {len(res['audio']['silences'])}  "
              f"drop-outs {len(res['audio']['dropouts'])}  cuts on onset {sy.get('cuts_on_onset_pct')}% "
              f"(chance {sy.get('chance_pct')}%)")
    for w in warnings:
        print("  warning:", w)
    print("  ->", os.path.join(a.out, "metrics.json"))


if __name__ == "__main__":
    main()
