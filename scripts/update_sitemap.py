#!/usr/bin/env python3
"""
Idempotently ensures sitemap.xml has an entry for /blog and for every post
slug in scripts/posts_registry.json. Safe to re-run; skips entries that
already exist (matched by <loc>). Run from repo root: python3 scripts/update_sitemap.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, "sitemap.xml")

with open(os.path.join(ROOT, "scripts", "posts_registry.json")) as f:
    posts = json.load(f)

with open(SITEMAP, encoding="utf-8") as f:
    content = f.read()

existing_locs = set(re.findall(r"<loc>(https://growxtech-it\.us/[^<]*)</loc>", content))

new_entries = []

blog_loc = "https://growxtech-it.us/blog"
newest_date = max(p["date_iso"] for p in posts)
if blog_loc not in existing_locs:
    new_entries.append(f"""  <url>
    <loc>{blog_loc}</loc>
    <lastmod>{newest_date}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")
else:
    # bump the /blog hub's lastmod to the newest post date whenever it changes
    content = re.sub(
        r"(<loc>https://growxtech-it\.us/blog</loc>\s*<lastmod>)[^<]*(</lastmod>)",
        rf"\g<1>{newest_date}\g<2>",
        content,
    )

for p in posts:
    loc = f"https://growxtech-it.us/{p['slug']}"
    if loc in existing_locs:
        continue
    new_entries.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{p['date_iso']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""")

if not new_entries:
    print("sitemap.xml already up to date, no changes")
else:
    block = "\n" + "\n".join(new_entries)
    content = content.replace("</urlset>", block + "\n</urlset>")
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"added {len(new_entries)} new sitemap entries")
