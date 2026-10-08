#!/usr/bin/env python3
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from course_template import render_course

SLUGS = [
    "course-react-basics", "course-power-bi-basics", "course-software-testing-basics",
    "course-google-cloud-fundamentals", "course-agile-scrum-basics", "course-remote-work-skills",
    "course-behavioral-interview-star", "course-personal-branding", "course-comptia-network-plus",
    "course-itil-foundation-overview", "course-google-data-analytics-cert", "course-nonprofit-careers",
]

with open(os.path.join(ROOT, "scripts", "courses_registry.json"), encoding="utf-8") as f:
    registry = {c["slug"]: c for c in json.load(f)}

for slug in SLUGS:
    entry = registry[slug]
    html = render_course(entry)
    out_path = os.path.join(ROOT, f"{slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", out_path)
