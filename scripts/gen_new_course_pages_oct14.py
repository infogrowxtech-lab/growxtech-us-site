#!/usr/bin/env python3
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from course_template import render_course

SLUGS = [
    "course-go-programming-basics", "course-machine-learning-fundamentals",
    "course-mongodb-nosql-basics", "course-vuejs-basics", "course-system-design-fundamentals",
    "course-negotiating-job-offer-beyond-salary", "course-portfolio-website-job-search",
    "course-emotional-intelligence-at-work", "course-adaptability-resilience-at-work",
    "course-ceh-certification-overview", "course-six-sigma-certification-overview",
    "course-real-estate-careers-101", "course-pharma-biotech-careers",
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
