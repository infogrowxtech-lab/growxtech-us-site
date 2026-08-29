# Weekly blog workflow (growxtech-it.us)

This is the runbook a fresh Claude session follows once a week to publish
3 new blog posts safely. It assumes only this repo (cloned) and normal
internet/browser access — no memory of any past session.

## Why this exists

Netlify Drop deploys are atomic full-site replacements: whatever files you
upload become the entire live site, and anything you don't include is
deleted. A fresh session with no copy of the current site could wipe pages
by accident. This repo is the safety net: it is always a complete, current
mirror of the live site, so cloning it gives a fresh session everything it
needs to add 3 posts and redeploy without losing anything.

## Steps

1. **Clone the repo** to a scratch working directory.
2. **Check `scripts/posts_registry.json`** for the slugs/titles/categories
   already published, so the 3 new topics don't repeat one.
3. **Research 3 new topics.** Same standard as every post so far: real,
   named, credible, current sources only (BLS, Jobscan, LinkedIn Economic
   Graph, HBS, ZipRecruiter, CompTIA, etc. are all fair game — find fresh
   ones too). No fabricated statistics, no invented studies. If a claim
   can't be traced to a real source, cut it. Good categories to rotate
   through: Resume & ATS, Job Market, LinkedIn, Interviewing, Salary &
   Negotiation, Referrals & Networking, Remote Work, Career Change,
   Certifications, Visa/H1B-adjacent (general market facts only, no legal
   advice — Growx does not give immigration advice).
4. **Write each post** as 1000-1400 words of real prose, following the
   structure of the 3 existing posts (h2 sections, one `.pullout` callout
   with a caveat or myth-buster, a closing paragraph that links to
   `/services` or `/pricing` naturally, a numbered sources list of every
   citation used).
5. **Render the HTML** using `scripts/blog_template.py`'s `render_post()` —
   do not hand-write the HTML shell, only supply the per-post fields. Write
   the output to `<slug>.html` at the repo root.
6. **Insert the 3 new posts at the START of `scripts/posts_registry.json`**
   (the registry is newest-first) with slug, title, category, date_iso
   (today), date_display, read_time (~200 words/min), excerpt (1-2 sentence
   card blurb, hand-written, not copy-pasted from the lede).
7. **Regenerate the hub page:** `python3 scripts/gen_hub.py`
8. **Update sitemap.xml:** `python3 scripts/update_sitemap.py`
9. **Update llms.txt:** `python3 scripts/update_llms.py`
10. **Validate everything:** `python3 scripts/validate.py` — must print
    `ALL CHECKS PASSED` before continuing. Fix anything it flags.
11. **Zip the deploy set** — every file at the repo root and in `assets/`
    and `netlify/`, EXCLUDING `.git/`, `report/`, `apps-script/`, and
    `scripts/` itself (those aren't part of the live site).
12. **Deploy via Netlify Drop**, using Chrome browser automation:
    - Navigate to `https://app.netlify.com/projects/steady-pixie-171422/deploys`
      (NOT the generic netlify.com/drop — that would create a new site).
    - Use `find` to locate the "browse files to upload" file input in the
      drop zone.
    - Upload the zip via `file_upload` (the file must first be somewhere
      shared with the session, e.g. `/mnt/user-data/outputs/`).
    - Wait for "Your deploy completed successfully" and check the deploy
      summary shows the expected file count changed.
13. **Verify live:** fetch `/blog` and at least one new post URL, confirm
    they render (title, dates, sources list all present).
14. **Commit and push back to GitHub** so next week's session has this
    week's posts as its starting point:
    `git add -A && git commit -m "Add 3 blog posts: <slugs>" && git push`

## Files in this directory

- `blog_template.py` — the post-page HTML template + `render_post()`.
- `posts_registry.json` — canonical list of every published post
  (newest first). Source of truth for the hub page, sitemap, and llms.txt.
- `gen_hub.py` — rebuilds `blog.html` from the registry.
- `update_sitemap.py` — idempotently adds missing sitemap entries.
- `update_llms.py` — regenerates the `## Blog` section of `llms.txt`.
- `validate.py` — the pre-deploy validation suite.
