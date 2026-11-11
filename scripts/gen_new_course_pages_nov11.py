#!/usr/bin/env python3
"""One-off: render HTML pages for this week's (2026-11-11) new courses."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from course_template import render_course

REG = os.path.join(ROOT, "scripts", "courses_registry.json")

SLUGS = [
    "course-pyspark-big-data-basics",
    "course-elasticsearch-basics",
    "course-ansible-basics",
    "course-prometheus-grafana-monitoring",
    "course-snowflake-basics",
    "course-microservices-fastapi-basics",
    "course-cloud-security-fundamentals",
    "course-ux-ui-design-career-path",
    "course-data-science-career-path",
    "course-cka-certification-overview",
    "course-first-90-days-new-job",
    "course-video-interview-tips",
]

with open(REG) as f:
    registry = json.load(f)

by_slug = {c["slug"]: c for c in registry}

for slug in SLUGS:
    entry = by_slug[slug]
    html = render_course(entry)
    out_path = os.path.join(ROOT, f"{slug}.html")
    with open(out_path, "w") as f:
        f.write(html)
    print(f"wrote {slug}.html")
