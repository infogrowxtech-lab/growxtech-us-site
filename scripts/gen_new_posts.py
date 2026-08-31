#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from blog_template import render_post, build_sources_html

posts = []

# ---------- POST 1: AI-attributed layoffs, Challenger report ----------
slug1 = "blog-ai-layoffs-challenger-report"
title1 = "AI Has Now Led Every Layoff Reason for 5 Straight Months. Here's What That Means for You"
body1 = """
      <p>For five months running, "AI" has topped the list of reasons employers give for cutting jobs, according to outplacement firm Challenger, Gray &amp; Christmas &mdash; and July 2026 was no exception. The monthly report, one of the most-watched gauges of the US labor market, found that AI was cited in 10,970 of the 33,429 job cuts announced in July: exactly a third of everything that month.</p>

      <p>That's a striking number, but the fuller picture in the same report is more complicated &mdash; and more useful &mdash; than the headline suggests. Overall layoffs actually fell sharply in July, and hiring announcements jumped. Understanding both halves of that story matters more than reacting to either one alone.</p>

      <h2>The numbers, in context</h2>
      <p>Challenger's July 2026 report recorded 33,429 total job cuts, down 27% from June's 45,849 and down 46% from July 2025. That's the lowest monthly total in two years. At the same time, employers announced 16,095 hiring plans in July &mdash; up 47% from June and the highest July hiring total since 2022.</p>

      <p>So the labor market picture for July wasn't "AI is wiping out jobs." It was: fewer layoffs overall, more hiring announced, and a full third of the layoffs that did happen specifically attributed to AI adoption. Year-to-date, AI has been cited in 112,713 cuts, about 24% of all 2026 layoffs tracked so far. Since Challenger started tracking AI as a stated reason in 2023, the cumulative total is 184,538 job cuts.</p>

      <h2>It's concentrated in one sector</h2>
      <p>The detail that matters most for job seekers reading this: Challenger's own report notes that "AI-related cutting has been limited outside of the Tech sector," with the technology industry accounting for the overwhelming majority of AI-attributed cuts. The report found essentially no comparable pattern in health care and named only isolated cuts in other industries.</p>

      <p>This lines up with what's visible elsewhere in the market. Separate tracking of 2026 tech-sector layoffs &mdash; Apple trimming around 200 roles from its Siri, Vision Pro, and gaming teams; TikTok cutting roughly 325 positions across e-commerce and content moderation in two waves; Netflix closing two internal gaming studios; LinkedIn reducing R&amp;D headcount in Tel Aviv &mdash; puts total 2026 tech job losses at roughly 127,000 across 281 companies as of late August, already close to matching all of 2025 combined.</p>

      <div class="pullout">
        <p><strong>Myth to retire:</strong> "AI is replacing workers across the economy" isn't what the data shows. AI-attributed layoffs are heavily concentrated in tech itself &mdash; companies restructuring engineering, support, and content-moderation teams around AI tooling and automation, not a broad economy-wide substitution of AI for human labor. If you work outside tech, this specific trend is not (yet) your trend.</p>
        <span class="src">Challenger, Gray &amp; Christmas, July 2026 Job Cut Report</span>
      </div>

      <h2>What this actually means if you're job hunting in tech</h2>
      <p>Three practical takeaways follow from the data rather than the headlines:</p>

      <h2>1. The market is not uniformly bad</h2>
      <p>Hiring announcements rising 47% month-over-month while layoffs fell 27% is not the profile of a market in free-fall. It's a market reallocating: certain roles and teams are being cut specifically because of AI-driven restructuring, while overall hiring intent is recovering. If your search feels harder than the "labor market is fine" headlines suggest, it may be because you're competing in exactly the segment where the AI-related cuts are concentrated &mdash; not because the whole market has turned.</p>

      <h2>2. Know which roles are actually exposed</h2>
      <p>The companies cutting AI-attributed jobs this year have specific patterns: content moderation, certain support functions, some mid-level engineering roles being consolidated around AI coding tools, and teams tied to underperforming AI-adjacent products (like Apple's Vision Pro division). If your current or target role sits in one of those categories, it's worth explicitly asking, in interviews, how the team plans to use AI tooling internally &mdash; the answer tells you whether you're joining a team being built up or one already being resized.</p>

      <h2>3. Being "AI-literate" is now a baseline expectation, not a differentiator</h2>
      <p>When a third of a sector's layoffs are attributed to AI-driven restructuring, the flip side is that the surviving and newly created roles increasingly assume comfort working alongside AI tools &mdash; using them, evaluating their output, and building processes around them. That's shifted from a "nice to have" bullet point to something worth demonstrating concretely: a project where you used an AI tool to ship something faster, or evaluated one for your team.</p>

      <h2>The bottom line</h2>
      <p>Headlines compress a five-month trend and a one-sector concentration into "AI is taking jobs." The Challenger data says something more specific: hiring is actually picking up, layoffs are actually falling, and the AI-attributed cuts that are happening are heavily clustered in tech companies restructuring around AI products and tooling. If you're job hunting in tech right now, that's a market to navigate with real information, not a reason to panic based on a headline number.</p>

      <p>If you want a second opinion on whether your resume and interview story hold up in a market where "AI-literate" has quietly become table stakes, that's exactly the kind of positioning work our <a href="/services">career coaching and resume services</a> are built around.</p>
"""
sources1 = build_sources_html([
    ("Challenger, Gray & Christmas — July 2026 Job Cut Report: \"Layoffs Fall, Hiring Picks Up; AI Leads For Fifth Straight Month\"", "https://www.challengergray.com/blog/challenger-report-layoffs-fall-hiring-picks-up-ai-leads-for-fifth-straight-month/"),
    ("Fast Company — Tech layoffs August 2026 update: Apple, TikTok, LinkedIn, Netflix join the list", "https://www.fastcompany.com/91594345/tech-layoffs-list-august-2026-apple-tiktok-linkedin-slash-jobs"),
])
posts.append({
    "slug": slug1,
    "post": {
        "slug": slug1,
        "title": title1,
        "title_tag": "AI Now Leads All Layoff Reasons for 5 Straight Months",
        "category": "Job Market",
        "date_iso": "2026-08-31",
        "date_display": "August 31, 2026",
        "read_time": "8 min",
        "meta_desc": "Challenger's July 2026 report found AI cited in a third of all layoffs, a fifth straight month atop the list. Here's what the data shows about where it's concentrated and what it means for tech job seekers.",
        "og_desc": "AI led layoff reasons again in July 2026, but hiring also rose sharply. Here's the real, sector-specific picture behind the headline.",
        "h1": title1,
        "lede": "Challenger's July 2026 report put AI atop layoff reasons for a fifth straight month &mdash; but the same report shows hiring plans jumping 47% and total layoffs falling. Here's the fuller, more useful picture.",
        "body": body1,
        "cta_h2": 'Not sure if your target role is AI-exposed? <span class="grad">Let\'s find out together.</span>',
        "cta_p": "Our career coaches track which roles and teams are actually being restructured around AI tooling right now, and how to position yourself either way.",
        "cta_href": "/services",
        "cta_label": "Talk to a career coach",
    },
    "sources": sources1,
})

# ---------- POST 2: Return-to-office mandates ----------
slug2 = "blog-return-to-office-2026-job-search"
title2 = "The 2026 Return-to-Office Wave: What It Means If You're Job Hunting"
body2 = """
      <p>If it feels like every other week brings news of another company tightening its office policy, that's not a perception problem &mdash; it's the pattern. Through 2026, a steady stream of large employers have moved from hybrid schedules back toward full-time, in-office work: Instagram, Home Depot, Ubisoft, PNC Financial, Stellantis, UBS Americas, and Paramount Skydance have all announced five-day-a-week mandates this year, while others like Microsoft (Seattle), Ernst &amp; Young, Airbus, and Infosys have raised their required in-office days without going all the way to five.</p>

      <p>For job seekers, this isn't just background noise about corporate culture. It changes what to ask about in an interview, how to evaluate an offer, and how much weight to put on a job posting's stated "hybrid" policy versus what's actually enforced six months later.</p>

      <h2>The pattern: escalation, not a one-time reset</h2>
      <p>What stands out in the 2026 tracking isn't a single wave of RTO announcements &mdash; it's that companies keep escalating existing policies rather than settling into a stable hybrid norm. Patreon moved from two office days a week to three. Airbus went from three days to four. Microsoft set a three-day floor specifically for its Seattle-area workforce. The direction of travel, company after company, has been toward more required office time, not less.</p>

      <p>Even government employers are part of this. California Governor Gavin Newsom's executive order took state workers from two required office days to four, effective July 1, 2026 &mdash; a move significant enough that SEIU Local 1000, representing roughly 96,000 state workers, filed an unfair labor practice charge over it.</p>

      <h2>The cost argument cuts both ways</h2>
      <p>The financial case for RTO mandates is genuinely contested, not settled. A California State Auditor analysis found that 19 state departments across seven large buildings spent nearly $117 million on underutilized office space in fiscal year 2024-25, and estimated the state could save roughly $225 million annually by moving to a two-day office, three-day remote schedule instead &mdash; because a four-or-more-day in-office requirement obligates the state to provide dedicated workstations, eliminating the space savings that come from desk-sharing.</p>

      <p>In other words, the same data being used to justify office-space investment can also be read as an argument for the opposite policy. CASE, the union representing California state legal professionals, put it directly: the mandate "would hurt recruitment and retention while increasing costs," and "the Governor has provided zero data supporting his arbitrary mandate."</p>

      <div class="pullout">
        <p><strong>Worth knowing before you sign an offer:</strong> a "hybrid, 2 days in office" line in a job posting is a snapshot of today's policy, not a commitment. Multiple companies that expanded RTO requirements in 2026 (Patreon, Airbus, Microsoft) had already been through at least one prior policy increase. If flexibility matters to you, ask directly in the interview whether the current policy has changed in the last 12 months, and how it's been enforced &mdash; not just what the handbook says.</p>
        <span class="src">Archie RTO Tracker, 2026; California State Auditor report via Inc.</span>
      </div>

      <h2>What to actually do with this if you're searching now</h2>

      <h2>Ask about enforcement, not just policy</h2>
      <p>Two companies can both say "hybrid, three days" and mean very different things in practice &mdash; one tracking badge swipes and following up on absences, another leaving it to manager discretion. Ask specifically how the policy is enforced today, and whether it's changed in the past year. A recent tightening is a signal the trend line, not just the current state, may keep moving toward more required office time.</p>

      <h2>Factor commute into total compensation math</h2>
      <p>A move from two to four required office days can add real weekly cost and time that a base salary comparison misses entirely. When comparing offers, it's worth pricing that difference explicitly rather than treating "same salary" as "same deal."</p>

      <h2>Remote-first employers are now a more distinct signal</h2>
      <p>As more large, brand-name employers escalate in-office requirements, a genuinely remote-first employer becomes a more meaningful differentiator in a job search than it might have been a year or two ago, when hybrid was closer to the industry default. If remote flexibility is a priority, it's worth weighting that in your target list rather than assuming most postings will eventually offer it.</p>

      <h2>The bottom line</h2>
      <p>The direction of the 2026 RTO trend has been toward more required office time at a wide range of large employers, even as the cost-benefit case for those mandates remains genuinely disputed by researchers, auditors, and the unions representing affected workers. Treat any stated hybrid or remote policy as a starting point for a direct question in your interview process, not a settled fact.</p>

      <p>If you're weighing offers with different in-office requirements and want help thinking through the full picture &mdash; not just salary, but schedule, commute, and how a policy has trended over time &mdash; that's the kind of conversation our <a href="/services">career coaching team</a> has with candidates every week.</p>
"""
sources2 = build_sources_html([
    ("Archie — Companies Returning to Office: RTO Tracker (July 2026)", "https://archieapp.co/blog/rto-companies-tracker/"),
    ("Inc. — The $225 Million Hidden Cost Behind California's Latest Return-to-Office Mandate", "https://www.inc.com/georgia-fearn/225-million-hidden-cost-behind-californias-lastest-return-to-office-mandate/91368502"),
    ("SEIU Local 1000 — Governor Newsom's Return-to-Office Mandate", "https://www.seiu1000.org/rto/"),
])
posts.append({
    "slug": slug2,
    "post": {
        "slug": slug2,
        "title": title2,
        "title_tag": "The 2026 Return-to-Office Wave, Explained",
        "category": "Remote Work",
        "date_iso": "2026-08-31",
        "date_display": "August 31, 2026",
        "read_time": "8 min",
        "meta_desc": "Instagram, Home Depot, PNC, and California state government all tightened office mandates in 2026. Here's the real pattern behind the headlines and what to ask before accepting an offer.",
        "og_desc": "A wave of 2026 RTO mandates keeps escalating rather than settling into hybrid norms. Here's what job seekers should ask about before signing.",
        "h1": title2,
        "lede": "From Instagram to California's state government, 2026 has brought a steady escalation of in-office requirements &mdash; not a one-time reset. Here's what the pattern actually looks like and how to factor it into a job search.",
        "body": body2,
        "cta_h2": 'Comparing offers with different office policies? <span class="grad">Let\'s map out the real trade-offs.</span>',
        "cta_p": "Our coaches help candidates weigh commute, schedule, and policy trends alongside salary &mdash; not just the number on the offer letter.",
        "cta_href": "/services",
        "cta_label": "Get offer-evaluation help",
    },
    "sources": sources2,
})

# ---------- POST 3: Tech layoffs wave / what laid-off workers should do ----------
slug3 = "blog-tech-layoffs-2026-next-move"
title3 = "Tech Layoffs Have Nearly Matched All of 2025 Already. Here's the Playbook If You're Affected"
body3 = """
      <p>By late August 2026, tracked tech-industry job losses for the year had reached roughly 127,000 across 281 companies &mdash; already closing in on the full-year 2025 total. August alone brought a fresh round: Apple cut around 200 roles across its Siri, Vision Pro, and gaming teams; TikTok eliminated roughly 325 positions in two separate waves spanning e-commerce and content moderation; Netflix closed two internal gaming studios (Night School Studio in Los Angeles and Moonloot in Helsinki); and LinkedIn reduced R&amp;D headcount at its Tel Aviv office.</p>

      <p>The reasons companies gave varied &mdash; Apple pointed to Vision Pro underperforming since its 2025 launch; TikTok cited "restructures to the Company's operations"; Netflix said it wanted to be "more focused in our execution"; LinkedIn framed it as "focusing our teams...on the highest impact priorities." Different words, same underlying story: companies narrowing bets and cutting the teams attached to the ones that didn't pay off.</p>

      <h2>Why this round looks different from 2022&ndash;2023</h2>
      <p>The 2022&ndash;2023 layoff wave was largely a broad correction after pandemic-era overhiring. What's showing up in 2026 reads more targeted: specific underperforming products (Vision Pro), specific functions being consolidated around AI tooling, and specific geographic offices being resized rather than blanket, company-wide cuts. That distinction matters for your job search, because it means the skills and teams affected aren't uniform across the industry &mdash; and neither is where the openings are.</p>

      <div class="pullout">
        <p><strong>Myth to retire:</strong> "Tech hiring has stopped." It hasn't &mdash; Challenger's July 2026 data separately found hiring announcements up 47% month-over-month, the highest July total since 2022. What's happening is reallocation: some teams and products are shrinking while others, particularly around AI infrastructure and tooling, are still hiring. A layoff at one company doesn't mean a frozen market everywhere.</p>
        <span class="src">Fast Company, tech layoffs tracker (August 2026); Challenger, Gray &amp; Christmas, July 2026 report</span>
      </div>

      <h2>If you've just been laid off: a practical first-30-days playbook</h2>

      <h2>1. File for unemployment insurance immediately</h2>
      <p>Don't wait to "figure out next steps" first. Unemployment benefits are typically not retroactive to your layoff date in every state, and the filing process itself can take time to process. This is a same-week task, not a someday task.</p>

      <h2>2. Get your COBRA and severance details in writing before you sign anything</h2>
      <p>Severance agreements often include a release of claims. Read the timeline for signing (many states require a review period) and understand exactly what health coverage options exist in the gap, including COBRA cost versus marketplace plans, before agreeing to anything under time pressure.</p>

      <h2>3. Audit your resume against what's actually hiring right now, not what you last updated it for</h2>
      <p>If your last resume update was targeted at a role type or company category that's currently contracting, a straight reuse of that resume may be aimed at the wrong part of the market. This is the moment to re-anchor it around where hiring announcements are actually up &mdash; which, per the Challenger data, is broad enough that this isn't a frozen search, just a search that needs re-targeting.</p>

      <h2>4. Use your network before the public postings</h2>
      <p>Layoff waves at name-brand companies also create a temporary surplus of former colleagues who are simultaneously searching and simultaneously more willing to make introductions than usual, since many are in the same position. A short, direct outreach message to former teammates and managers, asking specifically who they know that's hiring, tends to outperform cold applications in this window.</p>

      <h2>5. Separate "what happened to my team" from "what it says about you"</h2>
      <p>Every one of the August 2026 cuts described above was framed around product or organizational restructuring &mdash; not individual performance. That distinction is worth carrying into interviews: a layoff tied to a company narrowing its product bets is a straightforward, honest, and unremarkable thing to explain, and interviewers in 2026 have heard this explanation often enough that it needs no extra defense.</p>

      <h2>The bottom line</h2>
      <p>The scale of the 2026 tech layoff wave is real and worth taking seriously, but it's a reallocation story more than a collapse story: hiring plans are up even as headline-grabbing cuts continue at specific companies and teams. If you're affected, the highest-leverage moves in the first month are the practical ones &mdash; benefits, a resume re-targeted at where hiring is actually happening, and your network &mdash; not waiting for the overall market narrative to resolve itself.</p>

      <p>If you want help turning a layoff into a re-targeted, ATS-ready job search fast, that's exactly what our <a href="/services">resume and career coaching packages</a> are built for.</p>
"""
sources3 = build_sources_html([
    ("Fast Company — Tech layoffs August 2026 update: Apple, TikTok, LinkedIn, Netflix join the list of companies slashing jobs", "https://www.fastcompany.com/91594345/tech-layoffs-list-august-2026-apple-tiktok-linkedin-slash-jobs"),
    ("Challenger, Gray & Christmas — July 2026 Job Cut Report: \"Layoffs Fall, Hiring Picks Up; AI Leads For Fifth Straight Month\"", "https://www.challengergray.com/blog/challenger-report-layoffs-fall-hiring-picks-up-ai-leads-for-fifth-straight-month/"),
])
posts.append({
    "slug": slug3,
    "post": {
        "slug": slug3,
        "title": title3,
        "title_tag": "Tech Layoffs Nearly Match All of 2025 - What to Do Next",
        "category": "Career Change",
        "date_iso": "2026-08-31",
        "date_display": "August 31, 2026",
        "read_time": "8 min",
        "meta_desc": "2026 tech layoffs have hit roughly 127,000 across 281 companies, nearly matching all of 2025. Here's why this wave looks different and a practical first-30-days playbook if you're affected.",
        "og_desc": "Apple, TikTok, Netflix, and LinkedIn all cut jobs in August 2026. Here's what's different about this wave and what to do in your first 30 days.",
        "h1": title3,
        "lede": "Apple, TikTok, Netflix, and LinkedIn all announced cuts in August 2026, pushing the year's tech layoff total close to matching all of 2025. Here's why this wave looks different, and a practical playbook if you're affected.",
        "body": body3,
        "cta_h2": 'Just been laid off? <span class="grad">Let\'s re-target your search this week.</span>',
        "cta_p": "Our resume and coaching packages are built to move fast &mdash; re-anchoring your materials around where hiring is actually happening right now.",
        "cta_href": "/services",
        "cta_label": "Start your job search reset",
    },
    "sources": sources3,
})

for p in posts:
    html = render_post(p["post"], p["sources"])
    outpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), p["slug"] + ".html")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", outpath)
