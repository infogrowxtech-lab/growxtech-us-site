#!/usr/bin/env python3
"""
Reusable blog-post page template for growxtech-it.us.

Import PAGE and call render_post(post, sources_html) to get the full HTML
for one post. `post` is a dict with the keys used below (see
scripts/posts_registry.json for real examples of every field except `body`,
which lives only in the generated HTML file, not the registry).
"""

PAGE = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_tag} | Growx Tech IT Blog</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="https://growxtech-it.us/{slug}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title_tag} | Growx Tech IT Blog">
<meta property="og:description" content="{og_desc}">
<meta property="og:url" content="https://growxtech-it.us/{slug}">
<meta property="og:site_name" content="Growx Tech IT">
<meta name="theme-color" content="#070B14">
<link rel="icon" type="image/png" href="/assets/favicon.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {{"@type":"ListItem","position":1,"name":"Home","item":"https://growxtech-it.us/"}},
    {{"@type":"ListItem","position":2,"name":"Blog","item":"https://growxtech-it.us/blog"}},
    {{"@type":"ListItem","position":3,"name":"{title}","item":"https://growxtech-it.us/{slug}"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"BlogPosting",
  "headline":"{title}",
  "description":"{meta_desc}",
  "datePublished":"{date_iso}",
  "dateModified":"{date_iso}",
  "author":{{"@type":"Organization","name":"Growx Tech IT","url":"https://growxtech-it.us/"}},
  "publisher":{{"@id":"https://growxtech-it.us/#organization"}},
  "mainEntityOfPage":{{"@type":"WebPage","@id":"https://growxtech-it.us/{slug}"}},
  "url":"https://growxtech-it.us/{slug}"
}}
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
      <li><a href="/pricing">Pricing</a></li>
      <li><a href="/jobs">Jobs</a></li>
      <li><a href="/courses">Free Courses</a></li>
      <li><a href="/locations">Locations</a></li>
      <li><a href="/blog" aria-current="page">Blog</a></li>
      <li><a href="/referral">Referral</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
    <div class="nav-cta">
      <a class="btn btn-call" href="tel:+17198389991" aria-label="Call +1 (719) 838-9991"><span class="ci">&#128222;</span><span class="ct">Call</span></a>
      <a class="btn btn-wa" href="https://wa.me/13026831622?text=Hi%20Growx%20Tech%20IT%2C%20I%27d%20like%20a%20free%20career%20consultation." target="_blank" rel="noopener" aria-label="WhatsApp us"><span class="ci">&#128172;</span><span class="ct">WhatsApp</span></a>
      <button class="btn btn-grobo" data-grobo=""><img src="/assets/grobo-avatar.webp" alt="" class="gbtn-face">Ask Charlie</button>
    </div>
  </div>
</nav>

<header class="page-hero">
  <div class="container narrow">
    <p class="crumb"><a href="/">Home</a> · <a href="/blog">Blog</a> · {title}</p>
    <span class="label">{category}</span>
    <h1>{h1}</h1>
    <div class="postmeta">
      <span>{date_display}</span>
      <span>&middot;</span>
      <span>{read_time} read</span>
      <span>&middot;</span>
      <span class="tag">Growx Tech IT</span>
    </div>
    <p>{lede}</p>
  </div>
</header>

<section class="tight">
  <div class="container narrow">
    <div class="article-body">
{body}
    </div>

    <div class="article-sources">
      <h4>Sources</h4>
      <ol>
{sources}
      </ol>
    </div>
  </div>
</section>

<section style="padding-top:30px;">
  <div class="container">
    <div class="ctaband sr">
      <div>
        <h2>{cta_h2}</h2>
        <p>{cta_p}</p>
      </div>
      <div class="actions">
        <a class="btn btn-grobo btn-lg" href="{cta_href}">{cta_label}</a>
        <a class="btn btn-ghost" href="/blog">More from the blog</a>
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
      </div>
      <div>
        <h4>Offices</h4>
        <ul class="offices">
          <li><span class="flag"><img src="/assets/flag-us.svg" alt="USA" class="flagimg"></span><span><b>USA</b><br>Growx Tech IT LLC<br>30 N Gould St, Sheridan, Wyoming 82801</span></li>
          <li><span class="flag"><img src="/assets/flag-in.svg" alt="India" class="flagimg"></span><span><b>India</b><br>Growx Tech IT LLC<br>C-706, Siddhi Vinayak Towers, Sarkhej &#8211; Gandhinagar Hwy, Makarba, Ahmedabad, Gujarat 380051</span></li>
        </ul>
      </div>
      <div>
        <h4>Explore</h4>
        <ul><li><a href="/services">Services</a></li><li><a href="/pricing">Pricing</a></li><li><a href="/jobs">Jobs</a></li><li><a href="/courses">Free Courses</a></li><li><a href="/locations">Locations</a></li><li><a href="/blog">Blog</a></li><li><a href="/referral">Referral</a></li><li><a href="/contact">Contact</a></li><li><a href="/privacy-policy">Privacy Policy</a></li></ul>
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


def render_post(post, sources_html):
    """post: dict with slug, title, title_tag, category, date_iso, date_display,
    read_time, meta_desc, og_desc, h1, lede, body, cta_h2, cta_p, cta_href, cta_label.
    sources_html: pre-built <li><a ...>...</a></li> string (one per line)."""
    return PAGE.format(sources=sources_html, **post)


def build_sources_html(sources):
    """sources: list of (label, url) tuples -> numbered <li> list markup."""
    lines = []
    for label, url in sources:
        lines.append(f'        <li><a href="{url}" target="_blank" rel="noopener">{label}</a></li>')
    return "\n".join(lines)
