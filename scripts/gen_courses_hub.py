#!/usr/bin/env python3
"""
Regenerates courses.html (the /courses hub page) from
scripts/courses_registry.json, mirroring gen_hub.py's approach for /blog.

Registry order = display order within each category. To add new courses,
append entries to courses_registry.json (grouped under the right
"category") and re-run this script — it rebuilds the hero chip counts,
the BreadcrumbList/ItemList JSON-LD, and the card grid from scratch.
Run from the repo root: python3 scripts/gen_courses_hub.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "scripts", "courses_registry.json")) as f:
    courses = json.load(f)

CATEGORY_ORDER = [
    "Career Skills",
    "Job Search Strategy",
    "IT Technical Skills",
    "Certifications Overview",
    "Industry Career Guides",
]
CATEGORY_ANCHOR = {
    "Career Skills": "cat-career",
    "Job Search Strategy": "cat-jobsearch",
    "IT Technical Skills": "cat-techskills",
    "Certifications Overview": "cat-certs",
    "Industry Career Guides": "cat-industry",
}
CATEGORY_INTRO = {
    "Career Skills": "The fundamentals that decide whether you get hired: resume, LinkedIn, interviews, workplace culture and communication.",
    "Job Search Strategy": "How to actually find and land the role: outreach, referrals, getting past the ATS, and negotiating the offer.",
    "IT Technical Skills": "Beginner-friendly crash courses in the technical skills IT employers ask for most.",
    "Certifications Overview": "Not full prep courses: quick, honest overviews of popular IT and PM certifications so you know what you're signing up for.",
    "Industry Career Guides": "Growx places candidates across 11 non-IT industries too. Short, real intros to what building a career in each one looks like.",
}

by_category = {c: [] for c in CATEGORY_ORDER}
for course in courses:
    by_category[course["category"]].append(course)

total = len(courses)

# ---- ItemList + BreadcrumbList JSON-LD (registry order = position order) ----
def _course_instance(c):
    inst = {"@type": "CourseInstance", "courseMode": "online"}
    if c.get("workload_iso"):
        inst["courseWorkload"] = c["workload_iso"]
    return inst


item_list = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "Growx Tech IT free courses",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": i + 1,
            "item": {
                "@type": "Course",
                "name": c["title"],
                "description": c["item_desc"],
                "provider": {"@id": "https://growxtech-it.us/#organization"},
                "url": f"https://growxtech-it.us/{c['slug']}",
                "hasCourseInstance": _course_instance(c),
                "isAccessibleForFree": True,
            },
        }
        for i, c in enumerate(courses)
    ],
}

breadcrumb = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://growxtech-it.us/"},
        {"@type": "ListItem", "position": 2, "name": "Free Courses", "item": "https://growxtech-it.us/courses"},
    ],
}

# ---- hero chip row ----
chips_html = "\n".join(
    f'      <a href="#{CATEGORY_ANCHOR[cat]}">{cat} <span class="chip-count">{len(by_category[cat])}</span></a>'
    for cat in CATEGORY_ORDER
)

# ---- category sections with their course-card grids ----
sections_html = []
for cat in CATEGORY_ORDER:
    cards = []
    for c in by_category[cat]:
        cards.append(f'''      <a class="course-card" href="/{c['slug']}">
        <img class="cthumb" loading="lazy" src="https://i.ytimg.com/vi/{c['youtube_id']}/hqdefault.jpg" alt="">
        <span class="clabel">{cat}</span>
        <h3>{c['title']}</h3>
        <p>{c['card_desc']}</p>
        <div class="cmeta"><span>{c['time_label']}</span><span>Free certificate</span></div>
      </a>''')
    cards_html = "\n\n".join(cards)
    sections_html.append(f'''  <div class="cat-section" id="{CATEGORY_ANCHOR[cat]}">
    <div class="cat-head">
      <h2>{cat}</h2>
      <p>{CATEGORY_INTRO[cat]}</p>
    </div>
    <div class="courses-grid">
{cards_html}
    </div>
  </div>''')
sections_html = "\n\n".join(sections_html)

PAGE = f'''<!doctype html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-ZEXZVDKPTV"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-ZEXZVDKPTV');
  </script>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{total} Free Career &amp; IT Courses with Certificates | Growx Tech IT</title>
<meta name="description" content="{total} free, self-paced courses across career skills, job search strategy, IT technical skills, certifications overviews and 10+ industries. No payment, free certificate on completion.">
<link rel="canonical" href="https://growxtech-it.us/courses">
  <link rel="alternate" hreflang="en-us" href="https://growxtech-it.us/courses">
  <link rel="alternate" hreflang="en-ca" href="https://growxtech-it.us/courses">
  <link rel="alternate" hreflang="en-au" href="https://growxtech-it.us/courses">
  <link rel="alternate" hreflang="en" href="https://growxtech-it.us/courses">
  <link rel="alternate" hreflang="x-default" href="https://growxtech-it.us/courses">
<meta property="og:type" content="website">
<meta property="og:title" content="{total} Free Career &amp; IT Courses with Certificates | Growx Tech IT">
<meta property="og:description" content="Free, self-paced courses across career skills, job search strategy, IT technical skills, certifications and industries. Free certificate on completion.">
<meta property="og:url" content="https://growxtech-it.us/courses">
<meta property="og:site_name" content="Growx Tech IT">
<meta property="og:image" content="https://growxtech-it.us/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Growx Tech IT - U.S. IT Job Placement &amp; Career Services">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://growxtech-it.us/assets/og-image.jpg">
<meta name="theme-color" content="#070B14">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">
{json.dumps(breadcrumb, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(item_list, indent=2)}
</script>
</head>
<body>

<div class="aurora" aria-hidden="true"></div>

<nav>
  <div class="nav-inner">
    <a class="logo" href="/" aria-label="Growx Tech IT home"><img src="/assets/logo-white.png" alt=""><span class="logo-txt"><b>GROW<i>X</i></b><em>TECH IT</em></span></a>
    <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navmenu"><span></span><span></span><span></span></button>
    <ul class="nav-links" id="navmenu">
      <li><a href="/services">Services</a></li>
      <li><a href="/jobs">Jobs</a></li>
      <li><a href="/courses" aria-current="page">Free Courses</a></li>
      <li><a href="/locations">Locations</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/referral">Referral</a></li>
    </ul>
    <div class="nav-cta">
      <a class="btn btn-call" href="tel:+17198389991" aria-label="Call +1 (719) 838-9991"><span class="ci">&#128222;</span><span class="ct">Call</span></a>
      <button class="btn btn-grobo" data-grobo=""><img src="/assets/grobo-avatar.webp" alt="" class="gbtn-face">Ask Charlie</button>
    </div>
  </div>
</nav>

<header class="page-hero">
  <div class="container">
    <img src="/assets/grobo-solve.webp" alt="Charlie teaching a course" class="page-mascot" loading="lazy">
    <p class="crumb"><a href="/">Home</a> · Free Courses</p>
    <span class="label">100% free · No payment · Certificate included</span>
    <h1>{total} free courses. <span class="grad">Every one ends in a certificate.</span></h1>
    <p>Career skills, job search strategy, IT technical basics, certification overviews, and career guides for the industries Growx places candidates into. Anyone can take them: no payment, no account, just watch and get certified.</p>
    <div class="cat-chips">
{chips_html}
    </div>
  </div>
</header>

<section class="tight">
  <div class="container">

{sections_html}

  </div>
</section>

<section style="padding-top:10px;">
  <div class="container">
    <div class="ctaband sr">
      <div>
        <h2>Finished a course? <span class="grad">Let's get you placed.</span></h2>
        <p>These courses cover the fundamentals. For a recruiter working your file, mock interviews and profile marketing, see what Growx does end to end.</p>
      </div>
      <div class="actions">
        <a class="btn btn-grobo" href="/services">See services</a>
        <button class="btn btn-ghost" data-grobo="Hi, I'd like to know about pricing"><img src="/assets/grobo-avatar.webp" alt="" class="gbtn-face">Ask about pricing</button>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="container">
    <div class="foot-grid">
      <div>
        <a class="logo" href="/" aria-label="Growx Tech IT home"><img src="/assets/logo-white.png" alt=""><span class="logo-txt"><b>GROW<i>X</i></b><em>TECH IT</em></span></a>
        <p class="foot-tag">Career services and job placement across every industry we serve. Empower. Enable. Elevate.</p>
        <img src="/assets/grobo-build.webp" alt="Charlie, the Growx growth buddy" class="foot-mascot" loading="lazy" width="120">
        <div class="trust-badges">
          <img src="/assets/badge-dhs.png" alt="U.S. Department of Homeland Security" loading="lazy">
          <img src="/assets/badge-ssa.png" alt="Social Security Administration" loading="lazy">
          <img src="/assets/badge-everify.png" alt="E-Verify" loading="lazy">
        </div>
      </div>
      <div>
        <h4>Offices</h4>
        <ul class="offices">
          <li><span class="flag"><img src="/assets/flag-us.svg" alt="USA" class="flagimg"></span><span><b>USA</b><br>Growx Tech IT LLC<br>30 N Gould St, Sheridan, Wyoming 82801</span></li><li><span class="flag"><img src="/assets/flag-au.svg" alt="Australia" class="flagimg"></span><span><b>Australia</b><br>Growx Tech IT LLC<br>Level 36, Gateway, 1 Macquarie Place, Sydney, 2000</span></li>
          <li><span class="flag"><img src="/assets/flag-in.svg" alt="India" class="flagimg"></span><span><b>India</b><br>Growx Tech IT LLC<br>C-706, Siddhi Vinayak Towers, Sarkhej &#8211; Gandhinagar Hwy, Makarba, Ahmedabad, Gujarat 380051</span></li>
        </ul>
      </div>
      <div>
        <h4>Explore</h4>
        <ul><li><a href="/services">Services</a></li><li><a href="/jobs">Jobs</a></li><li><a href="/courses">Free Courses</a></li><li><a href="/locations">Locations</a></li><li><a href="/blog">Blog</a></li><li><a href="/referral">Referral</a></li><li><a href="/contact">Contact</a></li><li><a href="/privacy-policy">Privacy Policy</a></li></ul>
      </div>
      <div>
        <h4>Reach us</h4>
        <ul>
          <li><a href="tel:+17198389991">&#128222; +1 (719) 838-9991</a></li>
          <li><a href="https://wa.me/13026831622" target="_blank" rel="noopener">&#128172; WhatsApp +1 (302) 683-1622</a></li>
          <li><a href="mailto:hi@growxtech-it.us">&#9993; hi@growxtech-it.us</a></li>
        </ul>
        <h4 style="margin-top:18px;">Follow</h4>
        <ul><li><a href="https://www.linkedin.com/company/growx-tech-it/" rel="noopener">LinkedIn</a></li><li><a href="https://www.instagram.com/growxtechit" rel="noopener">Instagram</a></li><li><a href="https://x.com/growxtechit" rel="noopener">Twitter / X</a></li></ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 Growx Tech IT LLC. All rights reserved.</span>
      <span class="mono">growxtech-it.us</span>
    </div>
  </div>
</footer>

<script src="/assets/config.js"></script>
<script src="/assets/app.js" defer></script>
<script src="/assets/grobo-kb.js" defer></script>
<script src="/assets/grobo.js" defer></script>
<script src="/assets/intro.js" defer></script>
</body>
</html>
'''

out_path = os.path.join(ROOT, "courses.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(PAGE)
print(f"wrote {out_path} ({len(PAGE)} chars, {total} courses across {len(CATEGORY_ORDER)} categories)")
