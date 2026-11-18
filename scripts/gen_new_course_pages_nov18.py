#!/usr/bin/env python3
"""One-off: render HTML pages for this week's (2026-11-18) new courses."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from course_template import render_course

SLUGS = [
    "course-active-listening-at-work",
    "course-workplace-stress-management",
    "course-using-ai-tools-in-job-search",
    "course-elevator-pitch-for-job-seekers",
    "course-apache-spark-basics",
    "course-postman-api-testing-basics",
    "course-site-reliability-engineering-basics",
    "course-scala-programming-basics",
    "course-cissp-certification-overview",
    "course-google-project-management-cert-overview",
    "course-aerospace-defense-careers",
    "course-agriculture-agtech-careers",
]

with open(os.path.join(ROOT, "scripts", "courses_registry.json")) as f:
    registry = json.load(f)

by_slug = {c["slug"]: c for c in registry}

for slug in SLUGS:
    course = by_slug[slug]
    html = render_course(course)
    out_path = os.path.join(ROOT, f"{slug}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wrote {slug}.html")
