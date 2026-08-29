#!/usr/bin/env python3
"""
Regenerates the "## Blog" section of llms.txt from scripts/posts_registry.json.
The section is replaced in place between its heading and the next "## " heading,
so this is safe to re-run any time the registry changes.
Run from repo root: python3 scripts/update_llms.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLMS = os.path.join(ROOT, "llms.txt")

with open(os.path.join(ROOT, "scripts", "posts_registry.json")) as f:
    posts = json.load(f)

with open(LLMS, encoding="utf-8") as f:
    content = f.read()

post_lines = "\n".join(
    f"- [{p['title']}](https://growxtech-it.us/{p['slug']}): {p['excerpt']}"
    for p in posts
)

new_section = f"""## Blog

Growx publishes research-backed articles on the US job market at [/blog](https://growxtech-it.us/blog), aimed at job seekers rather than at search engines. Every factual claim is sourced. New posts are added weekly. Current posts:

{post_lines}

"""

pattern = re.compile(r"## Blog\n.*?\n\n(?=## )", re.S)
if pattern.search(content):
    content = pattern.sub(new_section, content)
else:
    # no existing Blog section (shouldn't happen after first run) - insert before "## Pages"
    content = content.replace("## Pages", new_section + "## Pages")

with open(LLMS, "w", encoding="utf-8") as f:
    f.write(content)
print(f"updated llms.txt Blog section ({len(posts)} posts listed)")
