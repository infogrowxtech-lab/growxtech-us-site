#!/usr/bin/env python3
"""One-off generator for the November 23, 2026 weekly batch of 3 blog posts."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from blog_template import render_post, build_sources_html

POSTS = []

# ---------------------------------------------------------------------------
# POST 1 — Visa & Work Authorization (US): D/S rule vacated, ruling Nov 16 2026
# ---------------------------------------------------------------------------
slug1 = "blog-duration-of-status-rule-vacated-november-2026"
title1 = "A Federal Court Just Vacated the Rule That Would Have Ended “Duration of Status” for F-1 and J-1 Students"
body1 = """
      <p>On November 16, a federal judge in Massachusetts struck down a DHS rule that would have replaced the decades-old “duration of status” framework for F-1 students, J-1 exchange visitors, and I-visa foreign media representatives with fixed admission periods and a new USCIS extension requirement. The rule never actually took effect &mdash; it had already been on hold since September &mdash; but the November ruling is the first final word on whether it survives at all. Here's exactly what the rule would have done, what the court said, and what it means if you're on F-1 or J-1 status right now. Growx Tech IT doesn't provide immigration or legal advice; this is a factual summary of a published court ruling, not guidance on your individual case.</p>

      <h2>What the rule would have changed</h2>
      <p>Under the “duration of status” system that's governed F-1 and J-1 visas for decades, a student or exchange visitor is authorized to stay for as long as they remain enrolled and in compliance with their program, without a fixed expiration date on their admission. DHS published a final rule on July 17, 2026, that would have replaced that system with fixed admission periods of up to four years for most F, J, and I nonimmigrants. Anyone who needed more time than that fixed period &mdash; a longer degree program, a delayed graduation, additional OPT time &mdash; would have had to file an extension-of-stay application with USCIS before their authorized period ran out, something D/S never required.</p>

      <h2>The timeline: blocked in September, vacated in November</h2>
      <p>The rule was challenged almost immediately in <em>Presidents' Alliance on Higher Education and Immigration v. DHS</em>, filed in the U.S. District Court for the District of Massachusetts. On September 14, 2026, Judge F. Dennis Saylor IV issued an order postponing the rule under the Administrative Procedure Act while the case proceeded, meaning it never actually went into effect for anyone. On November 16, the same judge went further: ruling on cross-motions for summary judgment, he vacated the rule in its entirety, finding it “arbitrary, capricious, an abuse of discretion, and otherwise not in accordance with law.”</p>

      <h2>Why the court struck it down</h2>
      <p>According to law firm summaries of the ruling, Judge Saylor's decision rested on several specific failures by DHS: the agency didn't adequately weigh the rule's costs against its stated benefits, didn't substantiate the fraud and national-security concerns it cited as justification, didn't meaningfully consider less burdensome alternatives such as expanded use of the existing SEVIS tracking system, and didn't respond to a large share of the public comments it received. The ruling also found that certain restrictions in the rule on changing academic programs or transferring schools exceeded DHS's statutory authority for F-1 students specifically. Because D/S is such a longstanding, foundational piece of how F and J status works, the court vacated the rule outright rather than sending it back to DHS to fix.</p>

      <div class="pullout">
        <p><strong>What this doesn't mean: that the fight is necessarily over.</strong> A vacatur is the strongest outcome a challenger can get at the district court level, but it isn't automatically the last word. DHS had already appealed September's preliminary injunction to the First Circuit before November's ruling came down, and that appeal was still pending as of this writing. Whether DHS also appeals the final judgment itself hasn't been publicly confirmed. An appeal, if filed, wouldn't reinstate the rule on its own &mdash; that would require a further order, such as a stay, from a higher court &mdash; but it does mean this isn't guaranteed to be the final chapter.</p>
        <span class="src">Maggio Kattar Immigration Law and BIZ Legal Services summaries of the November 16, 2026 ruling</span>
      </div>

      <h2>What this actually means if you're on F-1 or J-1 right now</h2>
      <p>Practically, nothing changes for you, and that's the point. Duration of status remains the law nationwide: there's no fixed end date attached to your admission, the academic flexibility D/S has always allowed &mdash; changing your major, your degree level, or your school &mdash; continues to be permitted, and no action is required on your part. OPT and STEM OPT eligibility and the rules governing them are unaffected by this ruling either way, since the vacated rule was about the admission framework itself, not post-completion work authorization. If you've been following this story since the rule was first proposed, the practical upshot of both the September block and the November vacatur is the same: D/S kept working exactly as it always has, the entire time.</p>

      <h2>How this fits into a year of change for F-1 students</h2>
      <p>This ruling doesn't arrive in isolation. 2026 has been a year of near-constant proposed and litigated change around F-1 and J-1 status: a separate proposal to charge schools a $70,000 fee for a student's first OPT period, ongoing litigation over new CPT guidance, and shifting rules around filing deadlines and extension procedures have all moved through the system in parallel with the D/S fight. None of those other items is resolved by November's ruling, and none of them is addressed by it either &mdash; the vacatur applies specifically to the fixed-admission-period rule and nothing else. If you've lost track of which proposal is in effect, which is blocked, and which is still just proposed, that's a reasonable position to be in right now; the pace of change this year has outrun most people's ability to track it casually, which is exactly why official sources matter more than ever.</p>

      <h2>What to actually do with this</h2>
      <p>If you're an F-1 student who's been timing a program change, a transfer, or your OPT application around a worry that your admission period might suddenly have a fixed deadline, that worry hasn't materialized and, per this ruling, the four-year fixed-period framework doesn't exist right now. That said, immigration rulemaking in this area has moved quickly and repeatedly in 2026, and a vacated rule with a pending appeal is a different thing than a rule that's been permanently abandoned by DHS. The most reliable way to track where this actually stands is your school's international student office or an immigration attorney, not a headline's framing of a court ruling, especially if DHS does appeal the final judgment or proposes a revised version of the same policy later.</p>
      <p>What hasn't changed, regardless of how the appeal plays out, is that a strong resume, a clear LinkedIn profile, and solid interview preparation are what actually get you hired once your status question is settled. If you're an OPT or STEM OPT candidate trying to land a role while legal questions like this one play out in the background, that's the part of your search we can help with directly. Our <a href="/services">resume, LinkedIn, and interview prep services</a> are built around exactly that kind of search, and you can message us on WhatsApp or ask Charlie on the site if you want to talk through where your own search stands.</p>
"""
sources1 = [
    ("Federal Register: Establishing a Fixed Time Period of Admission and an Extension of Stay Procedure for Nonimmigrant Students, Exchange Visitors, and Representatives of Foreign Information Media (July 17, 2026)", "https://www.federalregister.gov/documents/2026/07/17/2026-14439/establishing-a-fixed-time-period-of-admission-and-an-extension-of-stay-procedure-for-nonimmigrant"),
    ("Stanford Bechtel International Center: Duration of Status Final Rule Vacated by Federal Court (November 17, 2026)", "https://immigration.stanford.edu/news/duration-status-final-rule-vacated-federal-court"),
    ("Maggio Kattar Immigration Law: Federal Court Vacates DHS Rule Ending Duration of Status for F-1 and J-1 Visa Holders (November 17, 2026)", "https://maggio-kattar.com/latest-changes-us-immigration-law/federal-court-vacates-dhs-rule-ending-duration-of-status-for-f-1-and-j-1-visa-holders/"),
    ("BIZ Legal Services: Federal Court Vacates DHS Rule on Ending Duration of Status for F, J and I Nonimmigrants (November 18, 2026)", "https://bizlegalservices.com/2026/11/18/federal-court-vacates-dhs-rule-on-ending-duration-of-status-for-f-j-and-i-nonimmigrants/"),
]
POSTS.append(dict(
    slug=slug1, title=title1,
    title_tag=title1,
    category="Visa & Work Authorization",
    date_iso="2026-11-23", date_display="November 23, 2026", read_time="7 min",
    meta_desc="A federal judge vacated the DHS rule that would have replaced “duration of status” with fixed admission periods for F-1 and J-1 students on November 16, 2026. What the rule would have changed, why the court struck it down, and what it means right now.",
    og_desc="DHS's rule ending “duration of status” for F-1 and J-1 students was vacated by a federal court on November 16. Here's the timeline, the court's reasoning, and what it actually means for your status today.",
    h1=title1,
    lede="A federal judge vacated DHS's rule replacing “duration of status” with fixed admission periods for F-1 and J-1 students on November 16, 2026. Here's what the rule would have done, why the court struck it down, and what it means for your status right now.",
    body=body1,
    cta_h2="Job searching on F-1, OPT, or STEM OPT right now?",
    cta_p="Status questions are one part of the equation. A resume and LinkedIn profile that get you interviews, and interview prep for the questions that come up, are the part we help with directly.",
    cta_href="/services",
    cta_label="See our services",
))

# ---------------------------------------------------------------------------
# POST 2 — Career Change / SEO location: Toronto IT job search for recent grads
# ---------------------------------------------------------------------------
slug2 = "blog-it-job-toronto-recent-graduate-2026"
title2 = "How to Get an IT Job in Toronto as a Recent Grad in 2026"
body2 = """
      <p>Toronto shows up near the top of almost every recent ranking of North America's best tech markets, and that's not just marketing &mdash; the underlying job and talent growth data backs it up. But a city ranking high on talent and growth isn't the same as every role being easy to land, especially for someone early in their career. Here's what the actual data says about Toronto's tech market heading into 2026, and how to position yourself for it as a recent grad.</p>

      <h2>Toronto's standing in the data</h2>
      <p>CBRE's 2026 “Scoring Tech Talent” report, which ranks 75 of the largest tech markets across the US and Canada, has Toronto holding onto the No. 3 spot overall &mdash; behind only two US markets and ahead of every other city in North America. The report credits Toronto with adding 75,000 tech jobs between 2022 and 2025, more than any other market it tracks, and a workforce growth rate of 26.5% over that same period, one of the highest of any market in the ranking. Toronto isn't alone, either: eight Canadian cities land in CBRE's top 50, and six are in the top 15, which the report itself calls “impressive for a country our size.”</p>

      <h2>Where the growth is concentrated</h2>
      <p>A meaningful share of that growth is AI-driven. CBRE's report finds Toronto, Montreal, and Vancouver together hold 60% of Canada's entire AI talent pool, and the AI workforce across the US and Canada combined grew 45% to roughly 751,000 people as of mid-2026. That concentration matters for how you target your search: a title alone, like “software developer,” tells an employer less than specific, current tools do, and Toronto's growth is skewing toward candidates who can show real, hands-on experience with the platforms employers are actually hiring for.</p>

      <div class="pullout">
        <p><strong>The number worth knowing before you get discouraged: a growing market doesn't mean every opening is easy to land, especially at entry level.</strong> Indeed Hiring Lab data found Canadian tech job postings still sitting 19% below their February 2020 level, with mid-level and junior postings down a sharper 25% compared to five years earlier &mdash; a gap Indeed tied partly to high interest rates following the post-pandemic hiring frenzy and partly to overlap between what generative AI can now do and tasks listed in junior job descriptions. A high-level ranking like Toronto's No. 3 spot describes the health of the overall market, not how competitive any single entry-level posting is. Expect genuine competition for junior roles even in a market this strong.</p>
        <span class="src">Indeed Hiring Lab data, reported by The Logic, August 2025</span>
      </div>

      <h2>What employers are actually paying for</h2>
      <p>Robert Half's Canada IT and tech salary guide points to machine learning, large language models, cloud platforms, cybersecurity, software architecture, enterprise systems, and data analytics as the skill clusters commanding the strongest demand right now, with named platforms including Azure, SAP S/4HANA, and Salesforce, and certifications like the AWS Certified Cloud Practitioner, CISSP, and Certified Ethical Hacker standing out to employers. The guide also found six in ten Canadian technology hiring managers are offering salaries above their originally planned range just to secure candidates with the right skills. The roles the guide highlights as commanding the biggest premiums &mdash; software architect, IT director, AI architect &mdash; are senior titles, but the underlying signal for someone earlier in their career is the same: naming specific, current tools and platforms on your resume, rather than broad category language like “cloud experience,” is what reads as credible to a Toronto employer evaluating a stack of similar-looking applications.</p>

      <h2>The broader Canadian picture</h2>
      <p>Toronto's growth isn't happening in isolation from the rest of the country, which matters if you're also weighing other Canadian cities. CBRE's report counts eight Canadian cities in its North American top 50 and six in the top 15, with Vancouver at No. 9, Waterloo Region at No. 10, and Montreal at No. 11 &mdash; a genuinely deep bench by the report's own framing, not just a single standout city. The AI workforce specifically is where the country's growth is concentrating fastest: tech companies accounted for 21% of US and Canadian office leasing in the first half of 2026, up from just 13% in 2023, which is a reasonable proxy for how much physical hiring and expansion is actually happening behind the talent-pool numbers rather than just being discussed.</p>

      <h2>Work authorization is part of the picture for many candidates</h2>
      <p>A significant number of IT job seekers in Toronto are international graduates working through a Post-Graduation Work Permit while they search, on top of everything else that goes into a job search. If that's your situation, we've covered <a href="/blog-canada-pgwp-explained">how the PGWP actually works</a> in a separate piece, since getting the permit mechanics right is something to sort out alongside the job search, not after it. Growx Tech IT doesn't provide immigration advice, but we do work with candidates navigating a PGWP timeline and a job search at the same time, where the resume, the search strategy, and the permit clock all need to line up.</p>

      <h2>Practical steps for a Toronto-focused search</h2>
      <p>Given a market that's genuinely growing at the top while staying tighter than the headlines suggest at entry level, a few adjustments matter more than they might in a less competitive city. Lead with the specific tools and platforms you've actually used, matching the concrete list above, rather than a generic “IT professional” framing that doesn't differentiate you from the next applicant in a deep, competitive pool. If your background touches AI, cloud, or cybersecurity even tangentially, make that explicit rather than implied, since that's exactly where Toronto's growth and Canada's broader AI talent concentration are pointing. And if you're earlier in your career, build in real runway for the search: a 25% drop in junior postings compared with five years ago means a longer time-to-offer is a market condition right now, not a reflection on your candidacy.</p>

      <h2>The bottom line</h2>
      <p>Toronto's tech market in late 2026 is genuinely a top-three North American talent hub by CBRE's own ranking, with real job growth to back it up &mdash; and it's also a market where entry-level postings specifically remain tighter than the headline ranking implies. Reading both numbers together, rather than just the flattering one, gives a far more accurate picture of what your search actually looks like. Growx Tech IT works with candidates targeting <a href="/location-toronto">Toronto</a> on resume positioning, LinkedIn optimization, and interview preparation built around what local employers are actually hiring for. Our <a href="/services">services page</a> has the full breakdown, or you can message us on WhatsApp for specifics on the Toronto market.</p>
"""
sources2 = [
    ("CBRE: 3 Takeaways From CBRE's Latest “Scoring Tech Talent” Report (August 31, 2026)", "https://www.cbre.com/insights/articles/3-takeaways-from-cbres-latest-scoring-tech-talent-report"),
    ("CTV News Toronto: Toronto ranks third in tech industry talent across North America (August 19, 2026)", "https://www.ctvnews.ca/toronto/article/toronto-ranks-third-in-tech-industry-talent-across-north-america/"),
    ("The Logic: Canadian tech jobs haven't recovered from post-pandemic bust, Indeed finds (August 26, 2025)", "https://thelogic.co/briefing/canadian-tech-jobs-havent-recovered-from-post-pandemic-bust-indeed/"),
    ("Robert Half Canada: IT and Tech Salary Guide — 2026 Trends", "https://www.roberthalf.com/ca/en/insights/research/it-and-tech-salary-guide-2026-trends"),
]
POSTS.append(dict(
    slug=slug2, title=title2,
    title_tag=title2,
    category="Career Change",
    date_iso="2026-11-23", date_display="November 23, 2026", read_time="7 min",
    meta_desc="Toronto ranks No. 3 in North America for tech talent per CBRE, adding 75,000 tech jobs since 2022. But entry-level postings are down 25% from five years ago. What the data shows, and how recent grads can position for Toronto's market.",
    og_desc="Toronto ranks third in North America for tech talent and added more tech jobs than any other market since 2022 — but junior postings are tighter than the headline suggests. Here's how to position your search.",
    h1=title2,
    lede="Toronto ranks No. 3 in North America for tech talent, per CBRE's 2026 report, and has added more tech jobs since 2022 than any other market it tracks. Here's what that growth actually looks like, and how to position yourself for it as a recent grad.",
    body=body2,
    cta_h2="Targeting the Toronto tech market as a recent grad?",
    cta_p="Resume positioning, LinkedIn optimization, and interview prep built around what Toronto employers are actually hiring for right now.",
    cta_href="/location-toronto",
    cta_label="See Toronto services",
))

# ---------------------------------------------------------------------------
# POST 3 — Job Market: October 2026 jobs report + Challenger layoffs data
# ---------------------------------------------------------------------------
slug3 = "blog-october-2026-jobs-report-layoffs-explained"
title3 = "The October 2026 Jobs Report, Explained: Strong Headline Numbers, a Very Different Story in Tech"
body3 = """
      <p>Two reports released the same week in early November told what looks, at first glance, like a genuinely good-news story about the US labor market: payrolls beat expectations in October, and layoffs hit their lowest October level in three years. Underneath both headlines, though, is a more specific, more mixed picture for tech job seekers &mdash; and the details matter more than the topline numbers if you're actually searching right now.</p>

      <h2>The headline numbers</h2>
      <p>The Bureau of Labor Statistics' October 2026 jobs report, released in early November, showed nonfarm payrolls rising by 165,000, roughly 100,000 above the consensus forecast according to Appcast chief economist Andrew Flowers, who called it a beat “by a massive margin.” The unemployment rate fell to 4.1%, down a tenth of a point from September, and September's own payroll figure was revised up sharply, from an initial 29,000 to 60,000. The gains were led by professional and business services (+70,000), health care and social assistance (+55,100), and transportation and warehousing (+24,800), while leisure and hospitality (-13,000) and wholesale trade (-9,100) posted the largest declines. One softer detail buried in the report: the typical length of unemployment rose to 11.9 weeks, which Flowers flagged as a real area of concern &mdash; people who are out of work are having a harder time finding something, even as the topline numbers improve.</p>

      <h2>Layoffs are down too &mdash; a lot</h2>
      <p>Challenger, Gray & Christmas's October report, also released in early November, reinforces the “things are getting better” read on its face. Employers announced 43,994 job cuts in October, the lowest October total since 2023 and down 71% from October a year earlier. Year-to-date cuts through October sit at 617,189, down 44% from the same point last year and the lowest year-to-date total since 2022. By Challenger's count, October was the eighth month this year to come in below the same month a year earlier &mdash; a real, sustained trend, not a one-month blip.</p>

      <p>That 71% year-over-year drop is a real swing: October 2025 had been one of the heaviest October cut counts Challenger had recorded in decades, driven heavily by cost-cutting and AI-related restructuring, which makes this year's pullback in overall layoffs genuinely the headline story for the economy as a whole &mdash; just not, as the next section shows, for every industry equally.</p>

      <h2>The part that doesn't match the headline: tech</h2>
      <p>Here's where the story changes depending on your industry. Challenger's October data shows food companies led all industries in cuts for the month at 9,677, followed by technology at 5,576 and services at 5,458. But look at the year-to-date figures, and technology is the one sector running against the overall trend: tech leads all industries with 171,501 cuts so far in 2026, up 21% from the same point last year, even as total cuts across every industry combined are down 44%. Every other major sector is improving. Tech specifically is not.</p>

      <div class="pullout">
        <p><strong>Myth worth retiring: “layoffs are down” and “hiring is back” are not the same claim.</strong> Andy Challenger, the firm's own labor expert, specifically flagged that much of the hiring employers are currently announcing is “largely short-term, seasonal work,” with companies explicitly choosing that kind of flexibility over adding permanent headcount. A falling layoff count and a rising payroll number are both genuinely good signs for the labor market overall, but neither one tells you whether the jobs being added are the kind of permanent, career-track roles a tech job seeker is actually looking for.</p>
        <span class="src">Challenger, Gray & Christmas, October 2026 job-cuts report, reported by Trading Economics (November 5, 2026)</span>
      </div>

      <h2>What was actually driving October's job growth</h2>
      <p>It's worth looking at exactly where October's payroll gains came from, because the sector breakdown reinforces the same split. Manufacturing overall split almost evenly &mdash; durable goods manufacturing added 25,000 jobs while nondurable goods lost 6,000 &mdash; and within durable goods, computer and electronic product manufacturing added 6,700 jobs, one of the stronger subsector gains in the entire report. That's a hardware and physical-infrastructure signal, not a software-hiring one, and it lines up with a pattern that's shown up repeatedly in 2026 labor data: a lot of the AI-driven investment showing up in the jobs numbers is in data centers, chips, and physical build-out, while software and services roles &mdash; the kind most IT job seekers are actually applying for &mdash; have been the slower-moving part of the picture.</p>

      <h2>What this means if you're searching in tech right now</h2>
      <p>The honest read of these two reports together is that the US labor market is genuinely healthier than it's been in some time on an economy-wide basis, while tech specifically is still working through its own, separate adjustment that started well before October and hasn't resolved. If you're applying broadly across industries, October's numbers are real reasons for optimism: more hiring, fewer layoffs, a lower unemployment rate. If you're specifically targeting tech roles, the 21% year-to-date increase in tech cuts is the number to actually plan around, not the overall 44% decline that's being driven by every other sector improving around it.</p>
      <p>That split also means the all-industries "hiring is back" framing you'll see in a lot of coverage this week can be misleading if you take it at face value for a tech-specific search. A few things worth doing with this directly:</p>
      <ul>
        <li><strong>Don't assume a falling national layoff count means tech hiring has stabilized.</strong> It specifically hasn't, per Challenger's own year-to-date breakdown, even as the broader number improves.</li>
        <li><strong>Ask directly, in an interview, whether a role is permanent or seasonal/contract.</strong> With Challenger flagging a real shift toward flexible, non-permanent hiring, it's a reasonable question to raise rather than assume.</li>
        <li><strong>If your search has taken longer than you expected, the 11.9-week average time unemployed is real context, not a reflection on you specifically.</strong> It's risen even as the topline jobs number improved.</li>
      </ul>
      <p>Whatever the broader numbers are doing, a resume and interview approach built around the roles actually opening up &mdash; and a clear read on whether a specific opportunity is the permanent role it's being sold as &mdash; is what our <a href="/services">resume and interview prep services</a> focus on. If you want to talk through where your own tech search stands against this market, you can message us on WhatsApp or ask Charlie on the site.</p>
"""
sources3 = [
    ("U.S. Bureau of Labor Statistics — The Employment Situation, October 2026", "https://www.bls.gov/news.release/empsit.nr0.htm"),
    ("IndustryWeek: October Jobs Report: US Adds 165,000 Jobs as Unemployment Falls Slightly to 4.1% (November 6, 2026)", "https://www.industryweek.com/talent/news/55417255/october-jobs-report-us-adds-165000-jobs-as-unemployment-falls-slightly-to-41"),
    ("Trading Economics: US Job Cuts Hit a Three-Year Low for October (Challenger, Gray & Christmas data, November 5, 2026)", "https://tradingeconomics.com/united-states/challenger-job-cuts/news/598602"),
]
POSTS.append(dict(
    slug=slug3, title=title3,
    title_tag=title3,
    category="Job Market",
    date_iso="2026-11-23", date_display="November 23, 2026", read_time="6 min",
    meta_desc="October's jobs report beat expectations and layoffs hit a 3-year low — but Challenger data shows tech layoffs are up 21% year-to-date even as every other sector improves. What the real numbers mean for a tech job search.",
    og_desc="Payrolls beat expectations and layoffs fell to a 3-year low in October 2026. But tech-sector layoffs are still up 21% year-to-date, against the overall trend. Here's what that split means for your search.",
    h1=title3,
    lede="October's jobs report beat expectations and layoffs hit their lowest October level in three years. But tech-sector layoffs are still up 21% year-to-date, against the overall trend — here's what that split actually means if you're job hunting in IT.",
    body=body3,
    cta_h2="Searching in tech while the headlines say “hiring is back”?",
    cta_p="The broader market is improving, but tech's still working through its own adjustment. Resume and interview prep built around what's actually opening up, not the topline number.",
    cta_href="/services",
    cta_label="See our services",
))

for p, src in zip(POSTS, [sources1, sources2, sources3]):
    html = render_post(p, build_sources_html(src))
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), p["slug"] + ".html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    wc = len(p["body"].split())
    print(f"Wrote {out_path} ({wc} body words)")

print("\nSlugs:", [p["slug"] for p in POSTS])
