#!/usr/bin/env python3
"""
Idempotently ensures sitemap.xml has an entry for /courses and for every
course slug in scripts/courses_registry.json, mirroring update_sitemap.py's
approach for blog posts. Safe to re-run; skips entries that already exist
(matched by <loc>). Run from repo root: python3 scripts/update_courses_sitemap.py
"""
import json
import os
import re
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITEMAP = os.path.join(ROOT, "sitemap.xml")
TODAY = datetime.date.today().isoformat()

with open(os.path.join(ROOT, "scripts", "courses_registry.json")) as f:
    courses = json.load(f)

with open(SITEMAP, encoding="utf-8") as f:
    content = f.read()

existing_locs = set(re.findall(r"<loc>(https://growxtech-it\.us/[^<]*)</loc>", content))

new_entries = []

hub_loc = "https://growxtech-it.us/courses"
if hub_loc not in existing_locs:
    new_entries.append(f"""  <url>
    <loc>{hub_loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>""")
else:
    # bump the /courses hub's lastmod whenever new courses are added
    content = re.sub(
        r"(<loc>https://growxtech-it\.us/courses</loc>\s*<lastmod>)[^<]*(</lastmod>)",
        rf"\g<1>{TODAY}\g<2>",
        content,
    )

for c in courses:
    loc = f"https://growxtech-it.us/{c['slug']}"
    if loc in existing_locs:
        continue
    new_entries.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>""")

if not new_entries:
    print("sitemap.xml already up to date, no changes")
else:
    block = "\n" + "\n".join(new_entries)
    content = content.replace("</urlset>", block + "\n</urlset>")
    with open(SITEMAP, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"added {len(new_entries)} new sitemap entries")
