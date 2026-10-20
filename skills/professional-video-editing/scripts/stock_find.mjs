// Stock footage finder with a quality gate.
//
//   node stock_find.mjs "<query>" [--out DIR] [--n 5] [--per-source 16] [--min-height 1080]
//                 [--sources pexels,pixabay,mixkit,commons] [--photos] [--allow-ai]
//                 [--max-mb 300] [--excerpt-s 30] [--no-download]
//
// Searches Pexels + Pixabay + Mixkit + Wikimedia Commons without API keys, picks the
// highest-resolution rendition of each hit, drops what fails on metadata (below --min-height,
// default 1080p; vertical; < 4 s; < 24 fps; AI-labelled; Mixkit Restricted / NC / ND licences;
// off-topic), ranks 4K above 2K above 1080p, downloads the top N into --out
// (default ./stock_downloads/<query-slug>), runs stock_qc.py (next to this file) on each file
// and writes a ranked MANIFEST.md with verdicts and licence log lines, plus candidates.json
// (every hit, also the dropped ones) and results.json.
//
// Environment (all optional):
//   PEXELS_API_KEY   use api.pexels.com instead of the website's embedded JSON
//   PIXABAY_API_KEY  use pixabay.com/api instead of a headless-Chromium scrape (pixabay.com blocks curl)
//   STOCK_PY         Python command for stock_qc.py, e.g. "python3.11" or "py -3.11"
//                    (default: "python" on Windows, "python3" elsewhere)
//   STOCK_CONTACT    contact URL or e-mail for the Wikimedia User-Agent (their API etiquette asks for one)
// Mixkit and Commons need no key. Playwright ("npm install" next to this file; it also fetches
// Chromium) is only used for keyless Pixabay and as a fallback when the
// Pexels page does not return its JSON. Needs Node 20+ and ffmpeg/ffprobe on PATH.

import fs from 'node:fs';
import path from 'node:path';
import { spawnSync, spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { Readable } from 'node:stream';
import { pipeline } from 'node:stream/promises';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const BROWSER_UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36';
const WIKI_UA = `stock-finder/1.0 (${process.env.STOCK_CONTACT || 'https://www.mediawiki.org/wiki/API:Etiquette'}; footage research)`;
const AI_RE = /\b(ai[- ]?generated|generated (by|with) ai|generative ai|midjourney|dall-?e|stable diffusion|sora|runway ?(gen|ml)|veo ?\d|kling|hailuo|firefly|text[- ]to[- ]video|ai[- ]created|ai art)\b/i;
const STOP = new Set(['a', 'an', 'the', 'of', 'in', 'on', 'at', 'and', 'with', 'for', 'to', '4k', 'hd', 'uhd', 'video', 'footage', 'stock', 'close', 'up']);

// ------------------------------------------------------------------ args
const argv = process.argv.slice(2);
const opt = { n: 5, perSource: 16, sources: 'pexels,pixabay,mixkit,commons', photos: false, allowAi: false, maxMb: 300, excerptS: 30, download: true, out: null, minH: 1080 };
const pos = [];
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (a === '--n') opt.n = +argv[++i];
  else if (a === '--per-source') opt.perSource = +argv[++i];
  else if (a === '--sources') opt.sources = argv[++i];
  else if (a === '--photos') opt.photos = true;
  else if (a === '--allow-ai') opt.allowAi = true;
  else if (a === '--max-mb') opt.maxMb = +argv[++i];
  else if (a === '--excerpt-s') opt.excerptS = +argv[++i];
  else if (a === '--no-download') opt.download = false;
  else if (a === '--out') opt.out = argv[++i];
  else if (a === '--min-height') opt.minH = +argv[++i];
  else if (a === '--help' || a === '-h') opt.help = true;
  else if (a.startsWith('--')) { console.error(`unknown option ${a} (see --help)`); process.exit(2); }
  else pos.push(a);
}
const query = pos.join(' ').trim();
if (!query || opt.help) {
  const head = [];
  for (const l of fs.readFileSync(fileURLToPath(import.meta.url), 'utf8').split(/\r?\n/)) { if (!l.startsWith('//')) break; head.push(l.slice(3)); }
  console.log(head.join('\n'));
  process.exit(opt.help ? 0 : 1);
}
const slug = query.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') + (opt.photos ? '-photos' : '');
const OUT = path.resolve(opt.out || path.join(process.cwd(), 'stock_downloads', slug));
fs.mkdirSync(OUT, { recursive: true });
const sources = opt.sources.split(',').map((s) => s.trim()).filter(Boolean);
const words = query.toLowerCase().split(/[^a-z0-9]+/).filter((w) => w && !STOP.has(w));
const log = (...a) => console.log(...a);

// ------------------------------------------------------------------ helpers
async function getText(url, headers = {}, tries = 2) {
  for (let t = 0; t < tries; t++) {
    try {
      const r = await fetch(url, { headers: { 'User-Agent': BROWSER_UA, 'Accept-Language': 'en-US,en;q=0.9', ...headers }, redirect: 'follow' });
      if (r.ok) return await r.text();
      if (r.status === 404) return null;
    } catch (e) { /* retry */ }
    await new Promise((res) => setTimeout(res, 1500));
  }
  return null;
}
async function getJson(url, headers = {}) {
  const r = await fetch(url, { headers: { 'User-Agent': BROWSER_UA, ...headers } });
  if (!r.ok) throw new Error(`${r.status} ${url.replace(/key=[^&]+/, 'key=***')}`);
  return r.json();
}
let browser = null;
async function browserPage() {
  if (!browser) {
    const { chromium } = await import('playwright');
    browser = await chromium.launch({ args: ['--disable-blink-features=AutomationControlled'] });
    browser._ctx = await browser.newContext({ viewport: { width: 1600, height: 1000 }, userAgent: BROWSER_UA, locale: 'en-US' });
    await browser._ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  }
  return browser._ctx.newPage();
}
const strip = (s) => String(s || '').replace(/<[^>]+>/g, ' ').replace(/&[a-z#0-9]+;/gi, ' ').replace(/\s+/g, ' ').trim();
function relevance(c) {
  if (!words.length) return 0.5;
  const hay = `${c.title} ${(c.tags || []).join(' ')} ${c.desc || ''}`.toLowerCase();
  return words.filter((w) => hay.includes(w) || hay.includes(w.replace(/s$/, ''))).length / words.length;
}
// "a b c d" -> ["a b c d", "a b c", "a b"] (minWords..all), without "4k"/"hd" filler words
function shorterQueries(minWords) {
  const ws = query.split(/\s+/).filter((w) => w && !/^(4k|uhd|hd|footage|video|stock)$/i.test(w));
  const out = [];
  for (let n = ws.length; n >= Math.min(minWords, ws.length); n--) out.push(ws.slice(0, n).join(' '));
  return out.length ? out : [query];
}
function aiCheck(c, extra = '') {
  if (c.ai) return;
  const hay = `${c.title} ${(c.tags || []).join(' ')} ${c.desc || ''} ${extra}`;
  const m = hay.match(AI_RE);
  if (m) { c.ai = true; c.aiReason = `text mentions "${m[0]}"`; }
}

// ------------------------------------------------------------------ sources
const LIC = {
  pexels: { licence: 'Pexels License', licenceUrl: 'https://www.pexels.com/license/', attribution: null, terms: 'free commercial use, no credit required; do not sell unaltered copies; identifiable people/brands must not imply endorsement' },
  pixabay: { licence: 'Pixabay Content License', licenceUrl: 'https://pixabay.com/service/license-summary/', attribution: null, terms: 'free commercial use, no credit required; no standalone resale; trademarks/people/property may need extra rights' },
  mixkit: { licence: 'Mixkit Restricted License (free 720p, personal use only)', licenceUrl: 'https://mixkit.co/license/#videoRestricted', attribution: null, terms: 'free download is 720p and personal-use only; 4K + commercial via Envato Elements subscription' },
};

async function searchPexels() {
  const out = [];
  const key = process.env.PEXELS_API_KEY;
  if (key) {
    const ep = opt.photos ? 'https://api.pexels.com/v1/search' : 'https://api.pexels.com/v1/videos/search'; // old /videos/ path is being phased out
    const j = await getJson(`${ep}?${new URLSearchParams({ query, orientation: 'landscape', size: 'large', per_page: String(Math.min(80, opt.perSource)) })}`, { Authorization: key });
    for (const v of (opt.photos ? j.photos : j.videos) || []) {
      if (opt.photos) {
        out.push({ source: 'pexels', id: v.id, title: v.alt || '', page: v.url, author: v.photographer, w: v.width, h: v.height, fileUrl: v.src?.original, fileW: v.width, fileH: v.height, ext: '.jpg' });
      } else {
        const f = pickPexelsFile(v.video_files);
        out.push({ source: 'pexels', id: v.id, title: (v.url || '').split('/').filter(Boolean).pop()?.replace(/-\d+$/, '').replace(/-/g, ' '), page: v.url, author: v.user?.name, w: v.width, h: v.height, duration: v.duration, fps: f?.fps, fileUrl: f?.link, fileW: f?.width, fileH: f?.height, ext: '.mp4' });
      }
    }
    out.forEach((c) => (c.mode = 'api'));
    return out;
  }
  const base = opt.photos ? 'https://www.pexels.com/search/' : 'https://www.pexels.com/search/videos/';
  for (let page = 1; out.length < opt.perSource && page <= 3; page++) {
    const url = `${base}${encodeURIComponent(query)}/?orientation=landscape${page > 1 ? `&page=${page}` : ''}`;
    let h = await getText(url);
    if (!h || !h.includes('__NEXT_DATA__')) {
      const p = await browserPage();
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await p.waitForTimeout(4000);
      h = await p.content();
      await p.close();
    }
    const m = h && h.match(/<script id="__NEXT_DATA__"[^>]*>(.*?)<\/script>/s);
    if (!m) break;
    const data = JSON.parse(m[1]).props?.pageProps?.initialData?.data || [];
    if (!data.length) break;
    for (const d of data) {
      const a = d.attributes;
      if (!a) continue;
      const base = { source: 'pexels', mode: 'web', id: a.id, title: a.title || a.alt || '', desc: a.description || '', tags: (a.tags || []).map((t) => t.name || t), author: `${a.user?.first_name || ''} ${a.user?.last_name || ''}`.trim(), w: a.width, h: a.height };
      if (opt.photos) {
        if (!a.image) continue;
        out.push({ ...base, page: `https://www.pexels.com/photo/${a.slug}-${a.id}/`, fileUrl: `https://images.pexels.com/photos/${a.id}/pexels-photo-${a.id}.jpeg`, fileW: a.width, fileH: a.height, ext: '.jpg' });
      } else {
        if (!a.video) continue;
        const f = pickPexelsFile(a.video.video_files);
        out.push({ ...base, page: `https://www.pexels.com/video/${a.slug}-${a.id}/`, duration: a.duration, fps: f?.fps || a.fps, fileUrl: f?.link, fileW: f?.width, fileH: f?.height, ext: '.mp4' });
      }
    }
  }
  return out.slice(0, opt.perSource);
}
function pickPexelsFile(files = []) {
  const land = files.filter((f) => f.link && f.width && f.height && (f.file_type || 'video/mp4').includes('mp4'));
  land.sort((x, y) => (y.width * y.height - x.width * x.height) || ((y.fps || 0) - (x.fps || 0)));
  return land[0];
}

async function searchPixabay() {
  const key = process.env.PIXABAY_API_KEY;
  if (key) {
    const ep = opt.photos ? 'https://pixabay.com/api/' : 'https://pixabay.com/api/videos/';
    const j = await getJson(`${ep}?${new URLSearchParams({ key, q: query.slice(0, 100), per_page: String(Math.max(3, Math.min(200, opt.perSource))), safesearch: 'true', ...(opt.photos ? { image_type: 'photo', orientation: 'horizontal' } : {}) })}`);
    return (j.hits || []).map((v) => {
      const tags = String(v.tags || '').split(',').map((s) => s.trim());
      const aiFlag = Object.entries(v).find(([k, val]) => /ai/i.test(k) && /generat/i.test(k) && val === true);
      if (opt.photos) {
        return { source: 'pixabay', mode: 'api', id: v.id, title: tags.slice(0, 4).join(', '), tags, page: v.pageURL, author: v.user, w: v.imageWidth, h: v.imageHeight, fileUrl: v.imageURL || v.fullHDURL || v.largeImageURL, fileW: v.imageURL ? v.imageWidth : 1920, fileH: v.imageURL ? v.imageHeight : Math.round(1920 * v.imageHeight / v.imageWidth), ext: '.jpg', ai: !!aiFlag, aiReason: aiFlag ? `API field ${aiFlag[0]}` : undefined };
      }
      const r = ['large', 'medium', 'small'].map((k) => v.videos?.[k]).filter((x) => x && x.url && x.width)[0];
      return { source: 'pixabay', mode: 'api', id: v.id, title: tags.slice(0, 4).join(', '), tags, page: v.pageURL, author: v.user, w: r?.width, h: r?.height, duration: v.duration, fileUrl: r?.url, fileW: r?.width, fileH: r?.height, sizeBytes: r?.size, ext: '.mp4', ai: !!aiFlag, aiReason: aiFlag ? `API field ${aiFlag[0]}` : undefined };
    });
  }
  // keyless: render the search grid in headless Chromium. Each cell carries the quality badge,
  // duration, original size (style max-width/max-height) and an AI badge (role=img aria-label="AI").
  const p = await browserPage();
  const url = `https://pixabay.com/${opt.photos ? 'photos' : 'videos'}/search/${encodeURIComponent(query)}/`;
  await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForTimeout(4500);
  for (let i = 0; i < 4; i++) { await p.mouse.wheel(0, 1400); await p.waitForTimeout(600); }
  const rows = await p.evaluate((photos) => {
    const out = [];
    const re = photos ? /^\/photos\/([a-z0-9-]+)-(\d+)\/$/ : /^\/videos\/([a-z0-9-]+)-(\d+)\/$/;
    for (const a of document.querySelectorAll(`a[href^="/${photos ? 'photos' : 'videos'}/"]`)) {
      const m = (a.getAttribute('href') || '').match(re);
      if (!m) continue;
      const cell = a.closest('[class*="cell"]') || a.parentElement;
      const sizeEl = cell.querySelector('[style*="max-width"]');
      const st = sizeEl?.getAttribute('style') || '';
      const mw = +(st.match(/max-width:\s*(\d+)px/) || [])[1] || null;
      const mh = +(st.match(/max-height:\s*(\d+)px/) || [])[1] || null;
      const canva = cell.querySelector('a[href*="canva.com"]')?.getAttribute('href') || '';
      const fu = decodeURIComponent((canva.match(/file-url=([^&]+)/) || [])[1] || '');
      const img = cell.querySelector('img');
      const texts = [...cell.querySelectorAll('span, div')].map((e) => (e.children.length ? '' : e.textContent.trim())).filter(Boolean);
      const dur = texts.find((t) => /^\d+:\d\d$/.test(t));
      out.push({
        id: m[2], slug: m[1], page: 'https://pixabay.com' + a.getAttribute('href'), title: img?.getAttribute('alt') || m[1].replace(/-/g, ' '),
        thumb: img?.getAttribute('src') || '', fileUrl: fu || '', w: mw, h: mh, badge: texts.find((t) => /^(4K|HD|SD|8K)$/.test(t)) || '',
        duration: dur ? (+dur.split(':')[0] * 60 + +dur.split(':')[1]) : null,
        ai: !!cell.querySelector('[role="img"][aria-label="AI"]'), author: cell.querySelector('a[href^="/users/"]')?.textContent?.trim() || '',
      });
    }
    const seen = new Set();
    return out.filter((r) => !seen.has(r.id) && seen.add(r.id));
  }, opt.photos);
  await p.close();
  return rows.slice(0, opt.perSource).map((r) => {
    let fileUrl = r.fileUrl;
    if (!fileUrl && !opt.photos && /cdn\.pixabay\.com\/video\//.test(r.thumb)) fileUrl = r.thumb.replace(/_(tiny|small|medium)\.(jpg|webp)$/, '_large.mp4');
    if (!opt.photos && fileUrl) fileUrl = fileUrl.replace(/_(tiny|small|medium)\.mp4/, '_large.mp4');
    return { source: 'pixabay', mode: 'web', id: r.id, title: r.title, page: r.page, author: r.author, w: r.w, h: r.h, badge: r.badge, duration: r.duration, fileUrl, fileW: r.w, fileH: r.h, ext: opt.photos ? '.jpg' : '.mp4', ai: r.ai, aiReason: r.ai ? 'Pixabay "AI generated" badge' : undefined, resNote: opt.photos ? 'web mode gets the 1280-1920 px preview only; set PIXABAY_API_KEY for originals' : undefined };
  });
}

async function searchMixkit() {
  if (opt.photos) return [];
  // Mixkit only has "discover" pages for tag-like phrases: shorten the query until a page has clips.
  const ids = [];
  let used = null;
  for (const q of shorterQueries(1)) {
    const s = q.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    const h = await getText(`https://mixkit.co/free-stock-video/discover/${s}/`);
    if (!h) continue;
    for (const m of h.matchAll(/href="\/free-stock-video\/([a-z0-9-]+)-(\d+)\/"/g)) {
      if (!ids.find((x) => x.id === m[2])) ids.push({ slug: m[1], id: m[2] });
    }
    if (ids.length >= 3) { used = q; break; }
  }
  if (!ids.length) return [];
  // The licence is per clip: data-license="videoFree" (commercial OK, -1080/-2160 files open) or
  // "videoRestricted" (free 720p for personal use only; 4K sold via Envato). The JSON-LD "license"
  // field says videoFree even on restricted clips, so read data-license / copyrightNotice instead.
  const head = async (u) => { try { return (await fetch(u, { method: 'HEAD', headers: { 'User-Agent': BROWSER_UA } })).status === 200; } catch { return false; } };
  const one = async (it) => {
    const page = `https://mixkit.co/free-stock-video/${it.slug}-${it.id}/`;
    const ph = await getText(page);
    if (!ph) return null;
    let vo = null;
    for (const m of ph.matchAll(/<script type="application\/ld\+json"[^>]*>(.*?)<\/script>/gs)) {
      try { const j = JSON.parse(m[1]); vo = (j['@graph'] || [j]).find((x) => x['@type'] === 'VideoObject') || vo; } catch { /* skip */ }
    }
    const restricted = /data-license="videoRestricted"/.test(ph) || /Restricted/i.test(vo?.copyrightNotice || '') || /Personal Use only/i.test(ph);
    let res = 720;
    if (!restricted) for (const r of [2160, 1080]) if (await head(`https://assets.mixkit.co/videos/${it.id}/${it.id}-${r}.mp4`)) { res = r; break; }
    const dm = (vo?.duration || '').match(/(\d+)M(\d+)S/);
    const lic = restricted ? {} : { licence: 'Mixkit Free License (video)', licenceUrl: 'https://mixkit.co/license/#videoFree', terms: 'free commercial use, no credit required; do not redistribute/resell the clip as stock' };
    return { source: 'mixkit', mode: 'web', queryUsed: used, id: it.id, title: vo?.name || it.slug.replace(/-/g, ' '), desc: vo?.description || '', page, author: (vo?.description || '').match(/created by ([\w.-]+)/)?.[1] || '', w: Math.round(res * 16 / 9), h: res, duration: dm ? +dm[1] * 60 + +dm[2] : null, fileUrl: `https://assets.mixkit.co/videos/${it.id}/${it.id}-${res}.mp4`, fileW: Math.round(res * 16 / 9), fileH: res, ext: '.mp4', restricted, ...lic };
  };
  const list = ids.slice(0, opt.perSource);
  const out = [];
  for (let i = 0; i < list.length; i += 4) out.push(...(await Promise.all(list.slice(i, i + 4).map(one))).filter(Boolean));
  return out;
}

async function searchCommons() {
  const minW = opt.photos ? 2399 : 1899;
  const ft = opt.photos ? 'bitmap' : 'video';
  const api = async (params) => (await fetch('https://commons.wikimedia.org/w/api.php?' + new URLSearchParams({ format: 'json', ...params }), { headers: { 'User-Agent': WIKI_UA } })).json();
  const prop = opt.photos ? { prop: 'imageinfo', iiprop: 'url|size|mime|extmetadata' } : { prop: 'videoinfo', viprop: 'url|size|mime|extmetadata|derivatives' };
  // Commons ANDs every word of the file name/description: shorten the query until it finds >= 3 files.
  let pages = [];
  let used = null;
  for (const q of shorterQueries(2)) {
    const j = await api({ action: 'query', generator: 'search', gsrsearch: `${q} filetype:${ft} filew:>${minW}${opt.allowAi ? '' : ' -hastemplate:PD-algorithm'}`, gsrnamespace: '6', gsrlimit: String(Math.min(50, opt.perSource)), ...prop });
    pages = Object.values(j.query?.pages || {}).sort((a, b) => (a.index || 0) - (b.index || 0));
    used = q;
    if (pages.length >= 3) break;
  }
  return pages.map((p) => {
    const v = (p.videoinfo || p.imageinfo || [])[0];
    if (!v) return null;
    const em = v.extmetadata || {};
    const g = (k) => strip(em[k]?.value);
    const lic = g('LicenseShortName') || 'unknown';
    const pd = /public domain|cc0|pdm/i.test(lic);
    const artist = g('Artist').slice(0, 120);
    const cats = g('Categories');
    const c = {
      source: 'commons', mode: 'api', queryUsed: used, id: p.pageid, title: p.title.replace(/^File:/, '').replace(/\.[a-z0-9]+$/i, ''), desc: g('ImageDescription').slice(0, 300), tags: cats.split('|').slice(0, 20),
      page: `https://commons.wikimedia.org/wiki/${encodeURIComponent(p.title.replace(/ /g, '_'))}`, author: artist, w: v.width, h: v.height, duration: v.duration ? Math.round(v.duration * 10) / 10 : null,
      fileUrl: (v.url || '').split('?')[0], fileW: v.width, fileH: v.height, sizeBytes: v.size, ext: path.extname(new URL(v.url || 'https://x/a.webm').pathname).toLowerCase() || '.webm', mime: v.mime,
      licence: lic, licenceUrl: g('LicenseUrl') || 'https://commons.wikimedia.org/wiki/Commons:Licensing',
      attribution: pd ? null : `${artist || 'unknown author'} / ${lic} / via Wikimedia Commons (${p.title})`,
      terms: pd ? 'public domain / CC0: no conditions (still check people, trademarks)' : (/sa/i.test(lic) ? 'credit author + licence; share-alike applies to the clip itself if you redistribute an edited version of it; check Commons "restrictions"' : 'credit author + licence'),
      restrictions: g('Restrictions'), ua: WIKI_UA,
    };
    if (/AI[- ]generated|created with (midjourney|dall-e|stable diffusion|sora)/i.test(cats)) { c.ai = true; c.aiReason = 'Commons category says AI-generated'; }
    return c;
  }).filter(Boolean);
}

// ------------------------------------------------------------------ pre-gate + rank
function preGate(c) {
  const r = [];
  const W = c.fileW || c.w, H = c.fileH || c.h;
  if (W && H) {
    if (H > W && !opt.photos) r.push(`vertical ${W}x${H}`);
    const minLong = Math.round(opt.minH * 16 / 9) - 10, minShort = opt.minH - 5;
    if (opt.photos ? Math.max(W, H) < 2400 : (Math.max(W, H) < minLong || Math.min(W, H) < minShort)) r.push(`metadata resolution ${W}x${H} below ${opt.photos ? '2400 px long side' : `${minLong + 10}x${opt.minH}`}`);
  }
  if (!opt.photos && c.duration != null && c.duration < 4) r.push(`duration ${c.duration}s below 4s`);
  if (!opt.photos && c.fps && c.fps < 23.9) r.push(`${c.fps} fps below 24`);
  if (c.ai && !opt.allowAi) r.push(`AI-generated (${c.aiReason})`);
  if (c.restricted) r.push('free tier is personal-use only (Mixkit Restricted License)');
  if (/\b(NC|ND)\b/.test(c.licence || '')) r.push(`licence ${c.licence} not usable commercially / no edits`);
  if (!c.fileUrl) r.push('no direct file URL found');
  c.relevance = Math.round(relevance(c) * 100) / 100;
  if (words.length && c.relevance === 0) r.push('no query word in title/tags/description (off-topic hit)');
  return r;
}
function preScore(c, idx, n) {
  const W = c.fileW || c.w || 0, H = c.fileH || c.h || 0;
  const px = W * H;
  let s = px >= 3840 * 2160 * 0.95 ? 40 : px >= 2560 * 1440 * 0.95 ? 28 : px >= 1920 * 1080 * 0.95 ? 15 : 0;
  if (opt.photos) s = Math.max(W, H) >= 5000 ? 40 : Math.max(W, H) >= 3840 ? 30 : 15;
  if (!opt.photos && c.duration >= 6 && c.duration <= 90) s += 5;
  if (!c.attribution) s += 10; else if (/^CC BY \d/.test(c.licence || '')) s += 6; else s += 3;
  s += 20 * relevance(c);
  s += 10 * (1 - idx / Math.max(1, n));
  if (c.fps >= 47) s += 2;
  if (!opt.photos && c.duration > 300) s -= 10; // talks/tours: rarely clean b-roll
  if (c.ai) s -= 20;
  return Math.round(s * 10) / 10;
}

// ------------------------------------------------------------------ download + qc
function findPython() {
  const def = process.platform === 'win32' ? 'python' : 'python3';
  const c = (process.env.STOCK_PY || def).trim().split(/\s+/);
  const r = spawnSync(c[0], [...c.slice(1), '-I', '-c', 'import sys;print(sys.version_info[:2])'], { encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`Python not runnable as "${c.join(' ')}": set STOCK_PY to your Python 3.8+ command`);
  return c;
}
function runCmd(cmd, args, opts = {}) {
  return new Promise((resolve) => {
    const p = spawn(cmd, args, { ...opts });
    let out = '', err = '';
    p.stdout.on('data', (d) => (out += d));
    p.stderr.on('data', (d) => (err += d));
    p.on('close', (code) => resolve({ code, out, err }));
  });
}
async function download(c, file) {
  const ua = c.ua || BROWSER_UA;
  let size = c.sizeBytes || null;
  if (!size) {
    try { const h = await fetch(c.fileUrl, { method: 'HEAD', headers: { 'User-Agent': ua }, redirect: 'follow' }); size = +h.headers.get('content-length') || null; } catch { /* ignore */ }
  }
  c.fileSizeMb = size ? Math.round(size / 1e5) / 10 : null;
  if (!opt.photos && size && size > opt.maxMb * 1e6) {
    // big original: keep the first N seconds only (stream copy, no re-encode) for QC/preview
    const r = await runCmd('ffmpeg', ['-hide_banner', '-v', 'error', '-y', '-user_agent', ua, '-t', String(opt.excerptS), '-i', c.fileUrl, '-map', '0:v:0', '-map', '0:a?', '-c', 'copy', file]);
    if (r.code !== 0 || !fs.existsSync(file)) throw new Error('excerpt failed: ' + r.err.slice(0, 200));
    c.partial = `first ${opt.excerptS}s of a ${c.fileSizeMb} MB original (download the full file from the page)`;
    return;
  }
  const r = await fetch(c.fileUrl, { headers: { 'User-Agent': ua }, redirect: 'follow' });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  await pipeline(Readable.fromWeb(r.body), fs.createWriteStream(file));
}

// ------------------------------------------------------------------ main
const t0 = Date.now();
log(`query "${query}"  sources ${sources.join(',')}  ${opt.photos ? 'PHOTOS' : 'VIDEO'}  -> ${OUT}`);
const fns = { pexels: searchPexels, pixabay: searchPixabay, mixkit: searchMixkit, commons: searchCommons };
const all = [];
const srcStatus = {};
for (const s of sources) {
  if (!fns[s]) { srcStatus[s] = 'unknown source'; continue; }
  try {
    const rows = await fns[s]();
    rows.forEach((c, i) => {
      Object.assign(c, { ...(LIC[s] || {}), ...Object.fromEntries(Object.entries(c).filter(([, v]) => v !== undefined)) });
      aiCheck(c);
      c.pre = preGate(c);
      c.preScore = preScore(c, i, rows.length);
    });
    all.push(...rows);
    srcStatus[s] = `${rows.length} hits (${rows[0]?.mode || 'n/a'}${rows[0]?.queryUsed && rows[0].queryUsed !== query ? `, query shortened to "${rows[0].queryUsed}"` : ''})`;
    log(`  ${s.padEnd(8)} ${rows.length} hits, ${rows.filter((c) => !c.pre.length).length} pass metadata, ${rows.filter((c) => c.ai).length} AI-flagged`);
  } catch (e) {
    srcStatus[s] = 'error: ' + String(e.message || e).slice(0, 120);
    log(`  ${s.padEnd(8)} ERROR ${e.message || e}`);
  }
}
if (browser) await browser.close();

// pick top N with a per-source cap so one site cannot fill the list
const ok = all.filter((c) => !c.pre.length).sort((a, b) => b.preScore - a.preScore);
const cap = Math.max(2, Math.ceil(opt.n * 0.6));
const pick = [];
const per = {};
for (const c of ok) { if (pick.length >= opt.n) break; if ((per[c.source] || 0) < cap) { pick.push(c); per[c.source] = (per[c.source] || 0) + 1; } }
for (const c of ok) { if (pick.length >= opt.n) break; if (!pick.includes(c)) pick.push(c); }

const py = opt.download ? findPython() : null;
const qcPath = path.join(HERE, 'stock_qc.py');
for (const [i, c] of pick.entries()) {
  c.rankPre = i + 1;
  if (!opt.download) continue;
  const file = path.join(OUT, `${String(i + 1).padStart(2, '0')}_${c.source}_${c.id}${c.ext || '.mp4'}`);
  c.localFile = file;
  try {
    log(`  [${i + 1}/${pick.length}] ${c.source} ${c.id} ${c.fileW}x${c.fileH} ${c.title.slice(0, 50)}`);
    if (!fs.existsSync(file) || fs.statSync(file).size < 1000) await download(c, file);
    const args = [...py.slice(1), '-I', qcPath, file, '--json'];
    if (c.duration && !opt.photos) args.push('--meta-duration', String(c.duration));
    if (opt.photos) args.push('--photo');
    const r = await runCmd(py[0], args);
    c.qc = JSON.parse(r.out);
    log(`        -> ${c.qc.verdict} (score ${c.qc.score ?? '-'}) ${[...(c.qc.reasons || [])].join('; ').slice(0, 140)}`);
  } catch (e) {
    c.qc = { verdict: 'REJECT', reasons: [`download/qc failed: ${String(e.message || e).slice(0, 160)}`], notes: [], info: [] };
    log(`        -> FAILED ${e.message || e}`);
  }
}

// final ranking
const vOrder = { ACCEPT: 0, 'ACCEPT-WITH-NOTES': 1, REJECT: 2 };
const ranked = [...pick].sort((a, b) => (vOrder[a.qc?.verdict] ?? 3) - (vOrder[b.qc?.verdict] ?? 3) || (b.qc?.score ?? 0) - (a.qc?.score ?? 0) || b.preScore - a.preScore);
fs.writeFileSync(path.join(OUT, 'candidates.json'), JSON.stringify(all, null, 1));
fs.writeFileSync(path.join(OUT, 'results.json'), JSON.stringify({ query, date: new Date().toISOString(), options: opt, sources: srcStatus, ranked }, null, 1));

// MANIFEST.md
const esc = (s) => String(s ?? '').replace(/\|/g, '/').replace(/\n/g, ' ');
const res = (c) => `${c.qc?.width || c.fileW || '?'}x${c.qc?.height || c.fileH || '?'}`;
const counts = ranked.reduce((m, c) => ((m[c.qc?.verdict || 'not checked'] = (m[c.qc?.verdict || 'not checked'] || 0) + 1), m), {});
let md = `# Stock search: "${query}"${opt.photos ? ' (photos)' : ''}\n\n`;
md += `Date: ${new Date().toISOString().slice(0, 16).replace('T', ' ')} UTC. Sources: ${Object.entries(srcStatus).map(([k, v]) => `${k} ${v}`).join('; ')}.\n`;
md += `Candidates: ${all.length}, passed metadata gate: ${ok.length}, downloaded + checked: ${ranked.filter((c) => c.qc).length}. `;
md += `Verdicts: ${Object.entries(counts).map(([k, v]) => `${k} ${v}`).join(', ') || 'none'}.\n\n`;
md += `Verdict rules: see stock_qc.py (REJECT below 1080p, < 24 fps, < 4 s, interlaced, starved bitrate, letterboxed below 1080, strong watermark signal, very soft/shaky). Check every ACCEPT by eye before use.\n\n`;
md += `## Ranked selects\n\n| # | Verdict | Score | Source | Resolution | fps | Dur s | Mbit/s | Licence | Credit needed | File | Page |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n`;
ranked.forEach((c, i) => {
  md += `| ${i + 1} | ${c.qc?.verdict || '-'} | ${c.qc?.score ?? '-'} | ${c.source} | ${res(c)} | ${c.qc?.fps ?? c.fps ?? '?'} | ${c.duration ?? c.qc?.duration_s ?? '?'} | ${c.qc?.video_bitrate_mbps ?? '-'} | [${esc(c.licence)}](${c.licenceUrl}) | ${c.attribution ? 'yes' : 'no'} | ${c.localFile ? `\`${path.basename(c.localFile)}\`` : '-'} | [${esc(c.title).slice(0, 50)}](${c.page}) |\n`;
});
md += `\n## Why (per clip)\n\n`;
ranked.forEach((c, i) => {
  md += `**${i + 1}. ${esc(c.title).slice(0, 80)}** (${c.source} ${c.id}, by ${esc(c.author) || '?'})  \n`;
  for (const r of c.qc?.reasons || []) md += `- REJECT: ${esc(r)}\n`;
  for (const r of c.qc?.notes || []) md += `- note: ${esc(r)}\n`;
  for (const r of c.qc?.info || []) md += `- info: ${esc(r)}\n`;
  if (c.partial) md += `- info: file is an excerpt: ${c.partial}\n`;
  if (c.restrictions) md += `- licence restriction tag on Commons: ${esc(c.restrictions)}\n`;
  md += `- file URL: ${c.fileUrl}\n\n`;
});
const rej = all.filter((c) => c.pre.length);
md += `## Dropped on metadata (not downloaded): ${rej.length}\n\n| Source | Title | Res | Reason | Page |\n|---|---|---|---|---|\n`;
rej.slice(0, 60).forEach((c) => (md += `| ${c.source} | ${esc(c.title).slice(0, 45)} | ${c.fileW || c.w || '?'}x${c.fileH || c.h || '?'} | ${esc(c.pre.join('; '))} | [link](${c.page}) |\n`));
md += `\n## Licence log lines (paste the ones you use into the project licence log)\n\n| Clip | Source | Author | Licence | Terms | Credit line | Downloaded |\n|---|---|---|---|---|---|---|\n`;
ranked.filter((c) => c.qc && c.qc.verdict !== 'REJECT').forEach((c) => (md += `| ${c.localFile ? path.basename(c.localFile) : c.id} / [page](${c.page}) | ${c.source} | ${esc(c.author)} | ${esc(c.licence)} | ${esc(c.terms)} | ${esc(c.attribution || 'not required (optional credit)')} | ${new Date().toISOString().slice(0, 10)} |\n`));
fs.writeFileSync(path.join(OUT, 'MANIFEST.md'), md);
log(`done in ${Math.round((Date.now() - t0) / 1000)}s: ${Object.entries(counts).map(([k, v]) => `${k} ${v}`).join(', ')}  ->  ${path.join(OUT, 'MANIFEST.md')}`);
