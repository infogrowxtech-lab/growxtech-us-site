#!/usr/bin/env python3
"""
Regenerates the "## Free courses" section of llms.txt from
scripts/courses_registry.json, mirroring update_llms.py's approach for the
Blog section. The section is replaced in place between its heading and the
next "## " heading, so this is safe to re-run any time the registry changes.
Run from repo root: python3 scripts/update_courses_llms.py
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LLMS = os.path.join(ROOT, "llms.txt")

with open(os.path.join(ROOT, "scripts", "courses_registry.json")) as f:
    courses = json.load(f)

CATEGORY_ORDER = [
    "Career Skills",
    "Job Search Strategy",
    "IT Technical Skills",
    "Certifications Overview",
    "Industry Career Guides",
]

by_category = {c: [] for c in CATEGORY_ORDER}
for course in courses:
    by_category[course["category"]].append(course["title"])

total = len(courses)

lines = []
for cat in CATEGORY_ORDER:
    titles = ", ".join(by_category[cat])
    lines.append(f"- {cat} ({len(by_category[cat])}): {titles}")
cat_lines = "\n".join(lines)

new_section = f"""## Free courses

Growx also runs a free, self-paced course program at [/courses](https://growxtech-it.us/courses): {total} short courses, each built around a curated YouTube lesson, organized into five categories:

{cat_lines}

No payment and no account are required. Learners who watch a course get a free digital certificate. This is open to anyone, not only Growx clients.

"""

with open(LLMS, encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r"## Free courses\n.*?\n\n(?=## )", re.S)
if pattern.search(content):
    content = pattern.sub(new_section, content)
else:
    content = content.replace("## Free tools", new_section + "## Free tools")

# Keep the "Free Courses" entry under ## Pages in sync with the live count too.
content = re.sub(
    r"(\[Free Courses\]\(https://growxtech-it\.us/courses\): )\d+( free self-paced courses with certificates)",
    rf"\g<1>{total}\g<2>",
    content,
)

with open(LLMS, "w", encoding="utf-8") as f:
    f.write(content)
print(f"updated llms.txt Free courses section ({total} courses listed)")
