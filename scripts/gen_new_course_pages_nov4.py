#!/usr/bin/env python3
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from course_template import render_course

SLUGS = [
    "course-flutter-dart-basics", "course-nextjs-basics", "course-spring-boot-basics",
    "course-apache-kafka-basics", "course-windows-server-administration",
    "course-salesforce-admin-basics", "course-thank-you-email-interview",
    "course-finding-a-mentor", "course-azure-administrator-az104-overview",
    "course-google-it-support-certificate-overview", "course-marketing-advertising-careers",
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
