#!/usr/bin/env python3
"""
Full local validation suite for the site. Run from repo root before every
deploy: python3 scripts/validate.py
Exits non-zero (and prints failures) if anything is wrong. A clean run
prints "ALL CHECKS PASSED".
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

files = sorted(glob.glob("*.html"))
problems = []

# 1. JSON-LD validity
for f in files:
    content = open(f, encoding="utf-8").read()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.S)
    for b in blocks:
        try:
            json.loads(b)
        except Exception as e:
            problems.append(f"[json-ld] {f}: {e}")

# 2. internal link resolution
existing = set(f[:-5] for f in files)
for f in files:
    content = open(f, encoding="utf-8").read()
    hrefs = re.findall(r'href="(/[a-zA-Z0-9\-_/#]*)"', content)
    for h in hrefs:
        path = h.split("#")[0]
        if path in ("", "/"):
            continue
        slug = path.lstrip("/")
        if slug and slug not in existing and not slug.startswith("assets") and not slug.startswith(".netlify"):
            problems.append(f"[broken-link] {f}: {h}")

# 3. literal backslash-u OUTSIDE ld+json blocks (the \\u2014 bug class)
for f in files:
    content = open(f, encoding="utf-8").read()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.S)
    in_block = sum(b.count(chr(92) + "u") for b in blocks)
    total = content.count(chr(92) + "u")
    if total > in_block:
        problems.append(f"[literal-backslash-u] {f}: {total - in_block} occurrence(s) outside JSON-LD (likely a double-escaped unicode bug - use &mdash; or a real \\u escape, not \\\\u)")

# 4. duplicate titles / meta descriptions
titles, descs = {}, {}
for f in files:
    content = open(f, encoding="utf-8").read()
    t = re.search(r"<title>(.*?)</title>", content)
    d = re.search(r'<meta name="description" content="(.*?)"', content)
    if t:
        titles.setdefault(t.group(1), []).append(f)
    if d:
        descs.setdefault(d.group(1), []).append(f)
for k, v in titles.items():
    if len(v) > 1:
        problems.append(f"[dup-title] {k!r}: {v}")
for k, v in descs.items():
    if len(v) > 1:
        problems.append(f"[dup-description] {k!r}: {v}")

# 5. sitemap vs filesystem cross-check
sitemap = open("sitemap.xml", encoding="utf-8").read()
urls = re.findall(r"<loc>https://growxtech-it\.us/([^<]*)</loc>", sitemap)
url_slugs = set(u for u in urls if u)
fs_slugs = set(f[:-5] for f in files if f != "index.html")
if fs_slugs - url_slugs:
    problems.append(f"[sitemap-missing] files not in sitemap: {sorted(fs_slugs - url_slugs)}")
if url_slugs - fs_slugs:
    problems.append(f"[sitemap-stale] sitemap entries with no matching file: {sorted(url_slugs - fs_slugs)}")

if problems:
    print(f"{len(problems)} PROBLEM(S) FOUND:\n")
    for p in problems:
        print("  " + p)
    sys.exit(1)
else:
    print(f"ALL CHECKS PASSED ({len(files)} html files, {len(urls)} sitemap urls)")
