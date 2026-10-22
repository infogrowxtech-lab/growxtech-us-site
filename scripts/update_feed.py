#!/usr/bin/env python3
"""
Builds feed.xml (RSS 2.0) at the repo root from scripts/posts_registry.json.

Purpose: lets external tools (Zapier / Pabbly / Buffer etc.) watch
https://growxtech-it.us/feed.xml and auto-share each new blog post to the
Growx LinkedIn company page.

Safe to re-run; it always regenerates the whole file from the registry
(newest 25 posts). Run from repo root after the registry is updated:
    python3 scripts/update_feed.py

IMPORTANT: each item's <guid> is the post URL and must never change for an
existing post, otherwise feed watchers will treat it as new and re-post it.
"""
import json
import os
from datetime import datetime, timezone
from email.utils import format_datetime
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://growxtech-it.us"
MAX_ITEMS = 25

with open(os.path.join(ROOT, "scripts", "posts_registry.json"), encoding="utf-8") as f:
    posts = json.load(f)

# registry is newest-first, but sort defensively (stable, so same-day order is kept)
posts = sorted(posts, key=lambda p: p["date_iso"], reverse=True)[:MAX_ITEMS]


def rfc822(date_iso: str) -> str:
    d = datetime.strptime(date_iso, "%Y-%m-%d").replace(hour=12, tzinfo=timezone.utc)
    return format_datetime(d)


items = []
for p in posts:
    url = f"{SITE}/{p['slug']}"
    items.append(
        "    <item>\n"
        f"      <title>{escape(p['title'])}</title>\n"
        f"      <link>{url}</link>\n"
        f'      <guid isPermaLink="true">{url}</guid>\n'
        f"      <pubDate>{rfc822(p['date_iso'])}</pubDate>\n"
        f"      <category>{escape(p.get('category', ''))}</category>\n"
        f"      <description>{escape(p.get('excerpt', ''))}</description>\n"
        "    </item>"
    )

last_build = rfc822(posts[0]["date_iso"]) if posts else format_datetime(datetime.now(timezone.utc))

feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Growx Tech IT Blog</title>
    <link>{SITE}/blog</link>
    <atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml" />
    <description>Career, resume, interview and IT job-market insights from Growx Tech IT.</description>
    <language>en-us</language>
    <lastBuildDate>{last_build}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""

out = os.path.join(ROOT, "feed.xml")
old = open(out, encoding="utf-8").read() if os.path.exists(out) else None
if old == feed:
    print("feed.xml already up to date, no changes")
else:
    with open(out, "w", encoding="utf-8") as f:
        f.write(feed)
    print(f"wrote feed.xml with {len(items)} items (newest: {posts[0]['slug'] if posts else 'none'})")
