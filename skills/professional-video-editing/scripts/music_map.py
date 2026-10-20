#!/usr/bin/env python3
"""Map a music track before you cut to it: loudness curve, hits, drop-outs, ending type.

Usage:
  python music_map.py <track> [<track> ...] [--step 0.25] [--want-hit 10.3] [--length 20]

For each track it prints:
  curve      loudness (dBFS RMS) every --step seconds, as a compact text strip
  hits       moments where the level jumps >= 10 dB within 0.5 s (booms, drops, chorus entries)
  dropouts   stretches >= 0.3 s that fall >= 18 dB under the track's median (built-in silences)
  ending     "button" (ends on a hit / stops within 0.6 s) or "fade" (decays over > 2 s)
  vocals     a rough hint only (energy in 1-4 kHz vs the rest); listen before using under a voice
With --want-hit T and --length L it also suggests source offsets: start points where one of the
track's hits lands exactly at T seconds of an L-second edit, ranked by whether a drop-out sits
right before the hit (the trailer pattern) and whether the track can end on a button by L.

Use it to choose between candidate tracks (structure, not only mood) and to find the edit points.
Needs ffmpeg on PATH. Standard library only.
"""
import argparse, array, math, statistics, subprocess


def levels(path, step, sr=8000):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                         capture_output=True).stdout
    a = array.array("h", raw)
    n = max(1, int(sr * step))
    out = []
    for i in range(0, len(a) - n + 1, n):
        s = 0
        for x in a[i:i + n]:
            s += x * x
        out.append(20 * math.log10(math.sqrt(s / n) / 32768 + 1e-9))
    return out


def band_ratio(path):
    """Share of energy between 1 and 4 kHz (voices live there)."""
    def energy(af):
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-t", "60", "-af", af, "-ac", "1", "-ar", "16000",
                              "-f", "s16le", "-"], capture_output=True).stdout
        a = array.array("h", raw)
        return sum(x * x for x in a[::4]) + 1
    mid = energy("highpass=f=1000,lowpass=f=4000")
    full = energy("anull")
    return mid / full


def analyse(path, a):
    lv = levels(path, a.step)
    st = a.step
    med = statistics.median(lv)
    hits = []
    k = int(0.5 / st)
    for i in range(k, len(lv)):
        if lv[i] - min(lv[i - k:i]) >= 10 and lv[i] > med - 6:
            if not hits or i * st - hits[-1] > 1.0:
                hits.append(round(i * st, 2))
    drops, run = [], None
    for i, v in enumerate(lv):
        if v < med - 18:
            run = i if run is None else run
        else:
            if run is not None and (i - run) * st >= 0.3:
                drops.append((round(run * st, 2), round(i * st, 2)))
            run = None
    tail = lv[-int(3 / st):] if len(lv) > int(3 / st) else lv
    last_loud = max(i for i, v in enumerate(lv) if v > med - 10) * st if lv else 0
    dur = len(lv) * st
    ending = "button" if dur - last_loud < 0.6 or (max(tail) - tail[-1] > 25 and len(tail) > 2 and tail[-2] - tail[-1] > 15) else "fade"
    vr = band_ratio(path)
    res = {"track": path, "duration": round(dur, 1), "median_db": round(med, 1), "hits": hits, "dropouts": drops,
           "ending": ending, "vocal_hint": "possible vocals/lead in voice band" if vr > 0.35 else "mostly outside voice band",
           "voice_band_share": round(vr, 2), "curve": lv}
    if a.want_hit is not None:
        sug = []
        for h in hits:
            off = h - a.want_hit
            if off < 0 or off + a.length > dur + 2.0:  # up to 2 s of silence can be padded at the end
                continue
            pre = any(h - 1.0 <= d1 <= h + 0.1 for d0, d1 in drops)
            sug.append({"source_start": round(off, 2), "hit_at_source": h, "dropout_before": pre,
                        "track_left_after_edit_s": round(dur - (off + a.length), 1)})
        sug.sort(key=lambda s: (not s["dropout_before"], s["source_start"]))
        res["suggested_offsets"] = sug[:5]
    return res


def strip(lv, step, width=100):
    chars = " .:-=+*#%@"
    lo, hi = -50, -6
    per = max(1, int(len(lv) / width) or 1)
    s = ""
    for i in range(0, len(lv), per):
        v = max(lv[i:i + per])
        s += chars[min(len(chars) - 1, max(0, int((v - lo) / (hi - lo) * (len(chars) - 1))))]
    return s, per * step


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("tracks", nargs="+")
    p.add_argument("--step", type=float, default=0.25)
    p.add_argument("--want-hit", type=float, default=None, help="where the big hit must land in your edit (s)")
    p.add_argument("--length", type=float, default=20.0, help="edit length for offset suggestions (s)")
    a = p.parse_args()
    for t in a.tracks:
        r = analyse(t, a)
        s, per = strip(r["curve"], a.step)
        print(f"\n== {t}  ({r['duration']} s, median {r['median_db']} dBFS, ending: {r['ending']}, {r['vocal_hint']})")
        print(f"curve (1 char = {per:.2f} s): |{s}|")
        print("hits:", ", ".join(f"{h:.2f}" for h in r["hits"]) or "none")
        print("drop-outs:", ", ".join(f"{d0:.2f}-{d1:.2f}" for d0, d1 in r["dropouts"]) or "none")
        if "suggested_offsets" in r:
            for sgg in r["suggested_offsets"]:
                print(f"  start at {sgg['source_start']:>6.2f} s -> hit at {a.want_hit} s"
                      f"{'  (drop-out before it)' if sgg['dropout_before'] else ''}; {sgg['track_left_after_edit_s']} s of track left")
            if not r["suggested_offsets"]:
                print("  no hit fits that position; edit the track (join sections at bar lines) or pick another")


if __name__ == "__main__":
    main()
