#!/usr/bin/env python3
"""One-off generator for the Oct 5, 2026 weekly batch of 3 blog posts."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from blog_template import render_post, build_sources_html

POSTS = []

# ---------------------------------------------------------------------------
# POST 1 — Job Market (trending: Sept 2026 jobs report, released Oct 2 2026)
# ---------------------------------------------------------------------------
slug1 = "blog-september-2026-jobs-report-tech-job-seekers"
title1 = "The September 2026 Jobs Report, Explained: What a “Stuck” Market Means If You're Job Hunting"
body1 = """
      <p>The Bureau of Labor Statistics released its September 2026 jobs report on Friday, October 2, and the one-word summary most economists reached for was "stuck." Payrolls grew, but barely. Layoffs eased, but hiring intentions didn't. And in tech specifically, job postings hit a three-year high while actual hiring went backward. None of these things individually explain the job market right now &mdash; together, they do.</p>

      <h2>The headline numbers</h2>
      <p>Nonfarm payrolls rose by just 29,000 jobs in September, and the unemployment rate held at 4.2%, with 7.1 million people unemployed nationally. The BLS itself described both figures as having "changed little" from the prior month. Health care, usually the most reliable source of job growth, added only 17,000 positions, well below its prior 12-month average of 33,000. Manufacturing was roughly flat at +9,000, and financial activities actually lost 7,000 jobs. Average hourly earnings edged up 5 cents to $37.81, in line with inflation rather than ahead of it. The long-term unemployed &mdash; people out of work 27 weeks or more &mdash; numbered 1.9 million, a figure worth watching closely if you've been searching for a while and are starting to feel like an outlier. You aren't.</p>

      <h2>Layoffs are down. So is hiring.</h2>
      <p>Challenger, Gray &amp; Christmas's own September report, also released this week, adds an important second data point. Employers announced 43,281 job cuts in September, down nearly 20% from a year earlier, and planned layoffs are down almost 40% for the year through September compared to the same stretch of 2025. That's genuinely good news on its face.</p>
      <p>But the same report found employers announced just 90,787 new hiring plans in September &mdash; the weakest September hiring intentions Challenger has recorded since 2011. Year-to-date hiring announcements are up only 3% versus 2025. Andy Challenger, the firm's own labor expert, attributed the caution to a mix of energy costs, geopolitical uncertainty, the possibility of renewed rate increases, and expected healthcare cost increases for employers. In plain terms: companies have mostly stopped cutting, but they also haven't started adding. That's the "stuck" everyone is describing.</p>

      <h2>Tech specifically: postings way up, actual hiring down</h2>
      <p>If you're job hunting in IT specifically, the picture has its own twist. CompTIA's analysis of September data, also published this week, found active IT job postings jumped to a three-year high &mdash; employers added more than 272,000 open technology roles in September alone. That sounds like a hiring boom. It isn't one yet: actual tech-sector employment slid by more than 10,000 positions from August to September, and hiring across all sectors for IT occupations contracted by roughly 6,000 roles. IT-specific unemployment ticked up to 3.3% in September from 3.1% in August, even though that's still well below the national 4.2% rate.</p>
      <p>CompTIA's VP of research put it directly: the jump in postings is a signal that the gap between employer demand and the available, qualified supply "is not only still there, but it's maybe growing a little bit." More open roles doesn't automatically mean more offers going out.</p>

      <div class="pullout">
        <p><strong>Myth to retire: a rising number of job postings is not the same thing as a rising number of hires.</strong> A posting can sit open for months, get reposted, or exist mostly to build a resume pipeline for a role that won't be filled for a quarter or more. When postings and actual hiring move in opposite directions, as they did in September, the postings count tells you where employer appetite might be heading, not how many people are getting hired today.</p>
        <span class="src">CompTIA analysis of September 2026 BLS data, reported by CIO Dive</span>
      </div>

      <h2>What the broader openings data adds</h2>
      <p>BLS's separate JOLTS report, covering August 2026 and released September 29, backs up the same "stuck, not shrinking" read. Total job openings nationally sat at 7.1 million, a 4.3% openings rate the agency again described as "little changed." Hires held flat at 5.2 million, and quits &mdash; a classic proxy for how confident workers feel about their prospects elsewhere &mdash; stayed essentially flat at 3.1 million, a 1.9% rate. People aren't quitting into a better market at any faster pace than they were a month earlier, which tracks with a labor market where neither side is moving quickly.</p>
      <p>One detail stands out, though: openings in the information sector, which includes much of tech, jumped by roughly 45,000 from July to August, landing at 123,000 open positions and a 4.3% openings rate. That's a meaningfully larger one-month jump than most other sectors saw, and it lines up with CompTIA's separate finding of a September postings surge in IT specifically. Professional and business services, the other category most tech roles fall under, had 1.186 million openings on its own, a 5.0% rate and one of the highest of any sector in the report.</p>

      <h2>What this actually means if you're searching right now</h2>
      <p>A market that's "stuck" rather than shrinking is a specific thing to plan around, and it plays out differently depending on where you are in your career. If you're a recent grad or early-career candidate, the volume of open roles is real and growing, but so is the number of other applicants chasing the same postings, so a generic resume is doing you more harm than usual. If you're mid-career and have been searching for a while, the 1.9 million long-term unemployed figure is a useful reality check: a longer search right now is a market condition, not necessarily a reflection on your candidacy. And if you're currently employed and weighing whether to make a move, the flat quits rate suggests most people are choosing to sit tight rather than jump, which means employers courting active candidates right now may have more room to negotiate than the headlines suggest.</p>
      <p>The practical move in a market like this is to go after the gap CompTIA identified directly: make sure your resume and LinkedIn profile speak clearly to the specific skills behind those 272,000 open IT roles and that 45,000-position jump in information-sector openings, rather than a generic version of your background. A few concrete steps that line up with what the data is actually saying:</p>
      <ul>
        <li><strong>Re-scan your resume against current postings, not last quarter's.</strong> If the postings surge is concentrated in specific tools or platforms, a resume written six months ago may already be behind it.</li>
        <li><strong>Expect a longer process, and build for it financially and mentally.</strong> A hiring intentions figure at a 15-year September low means fewer roles are moving quickly through to an offer, even with postings up.</li>
        <li><strong>Don't read a quiet week as a rejection.</strong> With quits and hires both flat, employers are also moving more slowly on their end, not only on yours.</li>
      </ul>
      <p>That's the kind of positioning work our <a href="/services">resume and interview prep services</a> focus on, and if you'd rather talk through where your search stands first, you can message us on WhatsApp or ask Charlie on the site.</p>
"""
sources1 = [
    ("U.S. Bureau of Labor Statistics — The Employment Situation, September 2026", "https://www.bls.gov/news.release/empsit.nr0.htm"),
    ("CPA Practice Advisor: U.S. Companies Announce Fewest Job Cuts for a September Since 2022 (Challenger, Gray & Christmas)", "https://www.cpapracticeadvisor.com/2026/10/01/u-s-companies-announce-fewest-job-cuts-for-a-september-since-2022/190969/"),
    ("CIO Dive: Tech hiring dips despite spike in job postings (CompTIA analysis)", "https://www.ciodive.com/news/september-jobs-report-compTIA-hiring-glassdoor/832068/"),
    ("U.S. Bureau of Labor Statistics — Job Openings and Labor Turnover Survey, August 2026 (JOLTS)", "https://www.bls.gov/news.release/pdf/jolts.pdf"),
]
POSTS.append(dict(
    slug=slug1, title=title1,
    title_tag=title1,
    category="Job Market",
    date_iso="2026-10-05", date_display="October 5, 2026", read_time="6 min",
    meta_desc="BLS's September 2026 jobs report shows a market that's stuck, not shrinking: +29,000 payrolls, layoffs down 20% YoY, but hiring intentions at a 15-year September low. What it means for your search.",
    og_desc="September payrolls grew just 29,000, layoffs are down but so are hiring plans, and IT postings hit a 3-year high while actual tech hiring fell. Here's what the real numbers say.",
    h1=title1,
    lede="September's jobs report and two industry reports released the same week tell a consistent story: layoffs have mostly stopped, but hiring hasn't really started — and in tech, job postings are surging even as actual hiring slows.",
    body=body1,
    cta_h2="Want your resume positioned for the roles actually opening up?",
    cta_p="272,000+ new IT postings in September means real demand exists — it's a matter of positioning. Our resume and interview prep process is built around exactly this kind of market.",
    cta_href="/services",
    cta_label="See the resume process",
))

# ---------------------------------------------------------------------------
# POST 2 — Visa & Work Authorization (trending: Vance H-1B comments, Oct 2 2026)
# ---------------------------------------------------------------------------
slug2 = "blog-vance-h1b-eliminate-2026-explained"
title2 = "JD Vance Says He'd Support Eliminating H-1B: What Was Actually Said, and What Hasn't Changed"
body2 = """
      <p>On Friday, October 2, Vice President JD Vance told conservative commentator Jack Posobiec, in an interview recorded aboard Air Force Two, that he would support eliminating the H-1B visa program entirely. The comments spread quickly across national and international outlets within hours. If you're on H-1B, OPT, or weighing a job search that depends on future sponsorship, here's exactly what was said, what it is, and &mdash; just as important &mdash; what it isn't. Growx Tech IT doesn't give legal or immigration advice; this is a plain-facts breakdown of a news story, not guidance on your individual situation.</p>

      <h2>What Vance actually said</h2>
      <p>Asked about the H-1B program, Vance said: "My view is the H-1B program is completely broken. And I'd be very supportive of just eliminating it." He went on to describe what he sees as the core misuse of the program: "If you're going to bring in an accountant making $45,000 a year to replace an accountant who's an American making $60,000 a year, that's not you using the program to bring in a genius." He added that while the program still exists, "what we have to do is protect American workers," and encouraged people to raise the issue with their members of Congress.</p>

      <h2>What this is &mdash; and isn't</h2>
      <p>This is a policy opinion from a sitting Vice President, stated in a media interview. It is not a bill, an executive order, a proposed regulation, or a change to any existing rule. Eliminating the H-1B program outright would require an act of Congress, since the program itself is written into federal immigration law; a VP's public position, even a strongly worded one, doesn't change the statute or any pending case on its own. As of this writing, no legislation to eliminate the program has been introduced as a direct result of these comments, and no agency has announced new rulemaking tied to them.</p>
      <p>That distinction matters because it's exactly the kind of story that tends to generate more anxious searching ("is my status about to change?") than it generates confirmed, actionable facts. Right now, there is no confirmed policy change for any current H-1B holder, petitioner, or applicant to act on.</p>

      <h2>What's actually enforceable on H-1B right now</h2>
      <p>Separately from Vance's comments, there is real, current litigation over H-1B fees worth knowing about. On September 30, a federal court in the Northern District of California vacated guidance tied to the proclamation that attempted to impose a $100,000 fee on new H-1B petitions, finding the agencies involved failed to consider alternatives or allow public comment before issuing it. That's the second federal court to block the fee; a separate court in Washington, D.C. had upheld it. Both rulings are under appeal, and the California court itself predicted the Supreme Court will likely need to resolve the conflict eventually. Separately, the Department of Labor has pending regulatory work on prevailing-wage requirements tied to H-1B and certain employment-based immigrant visas, though no final rule has been published.</p>

      <div class="pullout">
        <p><strong>The caveat worth repeating: public comments from an elected official, even a VP, are not the same as law.</strong> The $100,000 fee has been blocked twice in court and is still being litigated. The H-1B program itself, as written in the Immigration and Nationality Act, is unchanged. If you want to track what's actually been decided versus what's being proposed or discussed, the primary sources are USCIS.gov, the Federal Register, and your own employer's immigration counsel &mdash; not a news headline's framing of a quote.</p>
        <span class="src">National Law Review, Beltway Buzz (October 2, 2026); multiple news outlets reporting Vance's October 2 remarks</span>
      </div>

      <h2>Where this debate actually sits</h2>
      <p>Reporting following Vance's remarks indicates he's since been in discussions with a group that includes immigration-restriction advocates and some Silicon Valley investors who have separately argued the program should prioritize genuinely specialized talent over cost-cutting hires. Vance himself reportedly acknowledged that Congress currently lacks the political will to pass legislation eliminating or substantially rewriting the program, which is part of why the more immediate activity has been administrative: reports point to enforcement-focused actions, including scrutiny of hiring practices that exclude American applicants and inspector-general reviews at agencies overseeing certain visa-sponsoring employers. None of that is the same as eliminating the program, and none of it is final.</p>
      <p>It's also worth holding the other side of this in view, since the program has supporters as well as critics. The case employers and the tech industry have made for H-1B for decades is that it fills specialized roles &mdash; particular engineering, data, and research skill sets &mdash; where the domestic talent pipeline genuinely can't meet demand fast enough. Vance's criticism, and the criticism of groups like U.S. Tech Workers, is that enforcement hasn't kept pace with that stated purpose, allowing some employers to use the program to cut labor costs instead. Both of those things can be true at once, and the current debate is really about which one described the program's day-to-day use, not whether skilled immigration itself should exist.</p>

      <h2>What to actually do with this story</h2>
      <p>If you're currently on H-1B, OPT, or STEM OPT, your status and its terms haven't changed because of an interview. If you're earlier in your search and considering whether sponsorship-dependent roles are worth pursuing, the honest answer is that the program remains fully in effect today, with real litigation still playing out around its fees, not its existence, and with Congress not currently positioned to legislate it away regardless of what any one official supports. The most useful thing you can do with a story like this is exactly what Vance himself suggested for people with an opinion on it: watch official channels, and don't let a headline substitute for a legal read on your own situation from someone qualified to give one.</p>
      <p>A few concrete things worth doing regardless of how this story develops:</p>
      <ul>
        <li><strong>Check primary sources directly if you're worried, not secondary coverage.</strong> USCIS.gov and the Federal Register publish the actual status of any rule; a headline quoting a headline is one step too far removed.</li>
        <li><strong>Don't make a decision about your search based on a single interview clip.</strong> The $100,000 fee litigation, not this comment, is the live legal issue to track if you're evaluating sponsorship-dependent offers.</li>
        <li><strong>If your employer's immigration counsel hasn't flagged a change, there isn't one yet.</strong> That's a more reliable signal than social media reaction to a quote.</li>
      </ul>
      <p>If your search itself needs attention regardless of how this plays out &mdash; a resume that reads clearly to US employers, a LinkedIn profile that doesn't bury your work authorization status in a way that costs you interviews, interview prep for the sponsorship question when it comes up &mdash; that's the part of this we can actually help with. Our <a href="/services">career services</a> cover exactly that, or you can message us on WhatsApp to talk through where things stand.</p>
"""
sources2 = [
    ("Just the News: JD Vance says H-1B visa program should be eliminated, calling it 'completely broken' (October 2, 2026)", "https://justthenews.com/government/federal-agencies/vance-says-h-1b-visa-program-should-be-eliminated-calling-it-completely"),
    ("ANI News: US VP JD Vance says H-1B visa programme “completely broken”, should be scrapped", "https://aninews.in/news/world/us/us-vp-jd-vance-says-h-1b-visa-programme-8220completely-broken8221-should-be-scrapped20261002083517/"),
    ("National Law Review: Beltway Buzz, October 2, 2026 (H-1B $100,000 fee court ruling)", "https://natlawreview.com/article/beltway-buzz-october-2-2026"),
    ("Breitbart: JD Vance Is Building Coalition for H-1B Reforms (October 4, 2026)", "https://www.breitbart.com/immigration/2026/10/04/jd-vance-builds-coalition-for-h-1b-reforms/"),
]
POSTS.append(dict(
    slug=slug2, title=title2,
    title_tag=title2,
    category="Visa & Work Authorization",
    date_iso="2026-10-05", date_display="October 5, 2026", read_time="6 min",
    meta_desc="VP JD Vance said October 2 he'd support eliminating the H-1B program, calling it “completely broken.” What he actually said, why it isn't a policy change, and what's actually enforceable on H-1B right now.",
    og_desc="JD Vance's October 2 comments on eliminating H-1B spread fast. Here's the exact quote, the context, and the real, current legal status of H-1B fees — in plain facts, no legal advice.",
    h1=title2,
    lede="VP JD Vance told an interviewer on October 2 that he'd support eliminating the H-1B program outright. Here's exactly what he said, why that's different from a policy change, and what's actually been decided in court this week.",
    body=body2,
    cta_h2="Want your search to hold up regardless of how this plays out?",
    cta_p="Resume positioning, LinkedIn presence, and interview prep for the sponsorship question — built around today's market, not speculation about tomorrow's.",
    cta_href="/services",
    cta_label="See our services",
))

# ---------------------------------------------------------------------------
# POST 3 — Job Market / SEO location+service (Atlanta)
# ---------------------------------------------------------------------------
slug3 = "blog-it-job-atlanta-georgia-2026"
title3 = "How to Get an IT Job in Atlanta, Georgia in 2026"
body3 = """
      <p>Atlanta's tech hiring headlines have been mixed this year, and that's created real confusion for job seekers trying to figure out whether it's actually a good time to be looking in the city. The honest answer, based on the labor data and local reporting through September 2026, is that Atlanta's tech market hasn't frozen &mdash; it's gotten more selective about who it hires and why.</p>

      <h2>What the data actually shows</h2>
      <p>Overall Atlanta metro employment was essentially flat year over year as of July 2026, according to the Bureau of Labor Statistics. That's not a boom, but it's also not a contraction, which puts Atlanta roughly in line with the national "stuck" labor market rather than meaningfully behind it. Where Atlanta stands out is tech concentration: computer and mathematical occupations made up 4.1% of Atlanta-area employment as of May 2025, versus 3.4% nationally, according to BLS data. The region's roughly 137,000 core tech workers earn an average base salary of $131,007, and the sector generates more than $58.6 billion in regional economic impact, per Motion Recruitment's 2026 salary analysis.</p>
      <p>AI-specific hiring is where the growth is concentrated. CBRE counted 19,576 AI-skilled workers in Atlanta as of June 2026, up 45% or more from the prior year, and the Federal Reserve Bank of Atlanta found Georgia led the Southeast in AI job posting share as of late 2025. Importantly, the Fed's research also found most AI-related postings don't require deep AI specialization &mdash; the majority ask for only one to four AI-adjacent skills, spread across engineering, business operations, and management roles, not just dedicated "AI engineer" titles.</p>

      <h2>Why "hiring freeze" isn't quite the right description</h2>
      <p>Local tech coverage out of Atlanta this fall has pushed back directly on the idea that hiring has stopped. The more accurate framing: companies are hiring for specific capability rather than filling headcount broadly, which means a generic application is less likely to land than it might have two years ago, but a well-targeted one still has real room to work. That tracks with the national CompTIA data showing IT job postings at a three-year high even as actual placements lag behind &mdash; Atlanta isn't an exception to that pattern, it's a local example of it.</p>

      <div class="pullout">
        <p><strong>Myth to retire: "AI jobs" in Atlanta mostly aren't standalone AI engineer roles.</strong> The Federal Reserve Bank of Atlanta's own research found most AI-tagged postings in the region ask for a handful of AI-adjacent skills layered onto an existing function &mdash; engineering, operations, or management &mdash; not a dedicated AI specialist title. If you're retooling your resume for this market, the fastest win is usually adding specific, truthful AI-tool experience to the role you already do, not reinventing your title.</p>
        <span class="src">Federal Reserve Bank of Atlanta, AI job posting research (data through December 2025)</span>
      </div>

      <h2>Where the highest-paying roles sit</h2>
      <p>Per Motion Recruitment's 2026 Atlanta salary guide, AI engineer roles currently lead local tech compensation, with mid-level positions ranging $136,017&ndash;$174,993 and senior roles reaching $141,405&ndash;$184,264. Senior platform engineers top out near $175,062, and senior software architects range $149,456&ndash;$180,255. Mid-level data engineers run $107,904&ndash;$135,604, and information security engineers $104,050&ndash;$135,905 &mdash; both solid targets if you're earlier in an AI-adjacent pivot and not yet positioned for a senior title. The guide also flags two trends worth knowing before you negotiate: more Atlanta employers are requiring office return, and "boomerang hiring" &mdash; rehiring former employees &mdash; has risen sharply, which can work in your favor if you have a past Atlanta-area employer worth reconnecting with.</p>

      <h2>Which industries are actually doing the hiring</h2>
      <p>Georgia's standing as what LHH's 2026 outlook calls the nation's most active data center market is doing real work here: Google and Microsoft have both expanded their Georgia operations, and LHH projects IT role growth of 20&ndash;34% through 2034 on the back of that build-out. Fintech is the other pillar worth knowing about if you're not purely an engineering candidate &mdash; an estimated 70% of all U.S. payment transactions move through Georgia-based processors, supporting roughly 30,000&ndash;40,000 fintech jobs at firms like Visa and Global Payments, many of which need IT, data, and security talent rather than payments-specific experience. Healthcare remains the single largest growth engine regionally, with education and health services adding more than 23,000 jobs in a recent reporting period, and logistics anchored by Hartsfield-Jackson and UPS rounds out the metro's other major employment base. Metro Atlanta supports more than 3 million jobs overall, with roughly 19,000 new jobs expected in 2026 &mdash; good enough for fourth place nationally in projected job creation &mdash; and Georgia's unemployment rate sits near 3.8%, below the national 4.2% figure in the September jobs report.</p>

      <h2>What to actually do with this if you're searching in Atlanta</h2>
      <p>Lead with specific, current tool and platform experience rather than a broad skills list, since Atlanta employers are evidently screening for capability match over headcount-filling. If you're targeting the AI-adjacent roles where the real growth is, make sure that experience is described in terms a recruiter searching an ATS would actually type in, not just implied by your job titles. If your background is closer to fintech, healthcare IT, or logistics tech than to pure software engineering, say so explicitly &mdash; those three sectors are carrying a meaningful share of Atlanta's actual hiring volume, even though they get less attention than the AI headlines. And if you've worked in the Atlanta market before, don't rule out your own network of former employers &mdash; boomerang hiring is up for a reason.</p>
      <p>A short checklist before you apply broadly:</p>
      <ul>
        <li><strong>Match your resume's language to the sector you're actually targeting.</strong> A data-center or fintech recruiter searches differently than a pure software-engineering one, even for overlapping skill sets.</li>
        <li><strong>Name the specific AI tools you've used, not "AI experience."</strong> Given how thin most AI-tagged postings' actual requirements are, specificity reads as more credible, not less.</li>
        <li><strong>Revisit former Atlanta-area employers directly.</strong> With boomerang hiring rising, a short, direct message to a past manager can outperform a cold application.</li>
      </ul>
      <p>Growx Tech IT works with job seekers across <a href="/location-atlanta">Atlanta</a> and the other major <a href="/locations">US and international metros</a> we cover on exactly this kind of positioning: resume rebuilds aimed at the roles actually opening up, LinkedIn profiles that read clearly to both recruiters and ATS parsers, and interview prep built around what local employers are actually asking right now. Our <a href="/services">services page</a> has the full breakdown, or you can ask Charlie on the site for specifics on the Atlanta market.</p>
"""
sources3 = [
    ("Tech Square ATL: Atlanta Tech Hiring Is Not Frozen. It Is Getting More Intentional. (September 22, 2026)", "https://www.techsquareatl.com/tech-square-news/2026/9/22/atlanta-tech-hiring-is-not-frozen-it-is-getting-more-intentional"),
    ("Motion Recruitment: 2026 IT Salary Insights for Atlanta", "https://motionrecruitment.com/it-salary/atlanta"),
    ("CIO Dive: Tech hiring dips despite spike in job postings (national CompTIA context)", "https://www.ciodive.com/news/september-jobs-report-compTIA-hiring-glassdoor/832068/"),
    ("LHH: Atlanta Jobs Outlook — Jobs, Salaries, and Growth Opportunities (2026)", "https://www.lhh.com/en-us/insights/atlanta-jobs-outlook-jobs-salaries-and-growth-opportunities"),
]
POSTS.append(dict(
    slug=slug3, title=title3,
    title_tag=title3,
    category="Job Market",
    date_iso="2026-10-05", date_display="October 5, 2026", read_time="5 min",
    meta_desc="Atlanta tech employment was flat year over year through July 2026, but AI-adjacent hiring is up 45%+ and tech job concentration beats the national average. What the data shows, and how to position yourself.",
    og_desc="Atlanta's tech hiring hasn't frozen, it's gotten more selective. The real salary data, AI hiring trends, and what Atlanta employers are actually screening for in 2026.",
    h1=title3,
    lede="Atlanta's tech headlines this year have swung between “boom” and “freeze.” The labor data through September 2026 says neither — here's what's actually happening, and how to position yourself for it.",
    body=body3,
    cta_h2="Targeting the Atlanta tech market specifically?",
    cta_p="Resume positioning, LinkedIn rebuilds, and interview prep built around what Atlanta employers are actually screening for right now.",
    cta_href="/services",
    cta_label="See the resume process",
))

for p, src in zip(POSTS, [sources1, sources2, sources3]):
    html = render_post(p, build_sources_html(src))
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), p["slug"] + ".html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    wc = len(p["body"].split())
    print(f"Wrote {out_path} ({wc} body words)")

print("\nSlugs:", [p["slug"] for p in POSTS])
