#!/usr/bin/env python3
"""
One-off generator for the 3 GEO/decision-content blog posts (Oct 2026).
Uses blog_template.py's render_post(), writes each post HTML to the repo
root, and prepends a matching entry to scripts/posts_registry.json (newest
first, per gen_hub.py's documented order). Run once from repo root:
    python3 scripts/make_geo_posts.py
Then run gen_hub.py, update_sitemap.py, update_llms.py as usual.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from blog_template import render_post, build_sources_html

DATE_ISO = "2026-10-03"
DATE_DISPLAY = "October 3, 2026"

CTA_HREF = "/services"
CTA_LABEL = "See how Growx works"

posts = []

# ---------------------------------------------------------------------------
# POST 1
# ---------------------------------------------------------------------------
post1 = {
    "slug": "blog-choosing-it-job-placement-agency-opt-h1b",
    "title": "How to Choose an IT Job Placement Service If You're on OPT or H-1B",
    "title_tag": "How to Choose an IT Job Placement Service on OPT or H-1B",
    "category": "Career Change",
    "date_iso": DATE_ISO,
    "date_display": DATE_DISPLAY,
    "read_time": "7 min",
    "meta_desc": "OPT participation grew 21% in a single year, and the number of agencies competing for that search grew with it. A sourced checklist for telling a real placement service apart from a resume-marketing shop.",
    "og_desc": "OPT participation grew 21% in a single year. Here's how to tell a real IT placement service apart from a resume-marketing shop, sourced from SEVIS and DHS data.",
    "h1": "How to Choose an IT Job Placement Service If You're on OPT or H-1B",
    "lede": "Search “IT job placement for OPT” and you'll get dozens of nearly identical landing pages. Here's what actually separates them, based on how these businesses are structured, not how their homepage reads.",
    "cta_h2": "Want the version where you can see who you're paying?",
    "cta_p": "Real U.S. office addresses, E-Verify participation, and a resume/LinkedIn/interview process you can see before you commit — that's the whole pitch.",
    "cta_href": CTA_HREF,
    "cta_label": CTA_LABEL,
    "body": """      <p>If you're on OPT, you've almost certainly been pitched by more than one company promising to get you placed. The number of people in that search grew fast: 194,554 F-1 students held OPT employment authorization in 2024, up 21.1% from the year before, and 165,524 of them were on the STEM OPT extension specifically, built for exactly the technical fields most of these agencies target. Nearly half of all STEM OPT participants come from India, another fifth from China.</p>

      <p>More demand brought more agencies. Not all of them do the same job, even when their websites use identical language.</p>

      <h2>Three different businesses, one marketing page</h2>
      <p>"IT job placement" covers at least three distinct business models, and knowing which one you're talking to changes what you should expect to pay and what you're actually buying.</p>
      <ul>
        <li><strong>Career services, direct to employer.</strong> Resume rebuild, LinkedIn optimization, interview prep, and recruiters who apply on your behalf to employers' own open roles. You're typically a W-2 hire of whichever company extends the offer, not the agency.</li>
        <li><strong>Bench sales / C2C staffing.</strong> The agency itself becomes your employer of record and "markets" you, often as a contractor, to other staffing firms and end clients in a chain. You may be paid hourly only when "on a project," with gaps unpaid.</li>
        <li><strong>Resume marketing only.</strong> Your profile gets sent out in bulk with limited visibility into where, how often, or with what success rate.</li>
      </ul>
      <p>None of these is automatically the wrong choice, but they're not interchangeable, and a company that doesn't clearly say which one it is should be your first question, not your last.</p>

      <h2>Questions worth asking before you pay anyone</h2>
      <ul>
        <li>Will I be a W-2 employee of an actual employer, or a 1099/C2C contractor passed between vendors?</li>
        <li>Who is the employer of record, and can I see their actual office address?</li>
        <li>Is the company enrolled in E-Verify? (Relevant directly to STEM OPT, where your training-plan employer is required to be.)</li>
        <li>What exactly am I paying for — training, resume marketing, active recruiting, or a mix — and what happens if I don't get placed?</li>
        <li>Can I see a real, current job description and the employer's name before my resume is submitted?</li>
      </ul>

      <h2>Why this is under more scrutiny than it used to be</h2>
      <p>This isn't just due diligence for its own sake. DHS's Student and Exchange Visitor Program has said it is actively investigating fraud tied to STEM OPT employment, and it specifically named IT recruitment firms, consulting companies, and staffing agencies as the business types most often involved — not because every company in those categories is problematic, but because that's where the pattern has shown up. We've written a separate, more detailed breakdown of exactly what DHS flagged and what you legally cannot be charged for.</p>

      <h2>The bottom line</h2>
      <p>A legitimate placement service should be able to answer every question above in plain language, in writing, before you sign anything. If a company is vague about who employs you, what model it runs, or where its office actually is, that vagueness is the answer. Our own <a href="/services">process</a> is built to survive exactly this kind of question: real W-2 placement, named offices in Sheridan, Wyoming, Sydney, and Ahmedabad, and a resume-to-offer process you can see before you pay for it.</p>
""",
    "sources": [
        ("Study in the States: Read the 2024 SEVIS by the Numbers Report", "https://studyinthestates.dhs.gov/2025/06/read-the-2024-sevis-by-the-numbers-report"),
        ("VisaServe: DHS Issues Warning on STEM OPT Employer Fraud", "https://visaserve.com/dhs-issues-warning-on-stem-opt-employer-fraud-what-international-students-and-employers-need-to-know/"),
        ("USCIS: Optional Practical Training (OPT) for F-1 Students", "https://www.uscis.gov/working-in-the-united-states/students-and-exchange-visitors/optional-practical-training-opt-for-f-1-students"),
    ],
    "excerpt": "OPT participation grew 21% in a single year, and the number of agencies competing for that search grew with it. A sourced checklist for telling a real placement service apart from a resume-marketing shop.",
}
posts.append(post1)

# ---------------------------------------------------------------------------
# POST 2
# ---------------------------------------------------------------------------
post2 = {
    "slug": "blog-sponsorship-question-opt-candidates-resume",
    "title": "The “Will You Need Sponsorship?” Question: How to Answer It Without Hurting Your Application",
    "title_tag": "How to Answer the Sponsorship Question on OPT Without Hurting Your Application",
    "category": "Resume & ATS",
    "date_iso": DATE_ISO,
    "date_display": DATE_DISPLAY,
    "read_time": "6 min",
    "meta_desc": "The sponsorship question is legal, common, and often automated — and most OPT candidates answer it in a way that filters themselves out before a human ever sees the resume. Here's what the guidance actually allows, and a more accurate way to answer.",
    "og_desc": "Most OPT candidates answer the sponsorship question in a way that filters themselves out automatically. Here's a more accurate way to answer it.",
    "h1": "The “Will You Need Sponsorship?” Question: How to Answer It Without Hurting Your Application",
    "lede": "It shows up on page one of almost every online application, often before your resume has been looked at by a person. Here's what the question is actually allowed to ask, and why the honest answer is usually more favorable than candidates assume.",
    "cta_h2": "Want someone to position this correctly for you?",
    "cta_p": "Interview prep covers exactly this question, and our resume process makes sure your work-authorization status reads as an asset, not a question mark.",
    "cta_href": CTA_HREF,
    "cta_label": CTA_LABEL,
    "body": """      <p>"Will you now or in the future require sponsorship to work legally in the United States?" is one of the most mishandled questions on any job application. Candidates on OPT frequently answer "yes" reflexively, because they associate any work-authorization complexity with needing sponsorship, and in doing so, trip an automatic screen-out that a more precise answer wouldn't.</p>

      <h2>The question is legal, which is exactly why it's everywhere</h2>
      <p>The U.S. Department of Justice's Office of Special Counsel treats this question as permissible pre-hire screening, as long as an employer asks it the same way of every candidate. What isn't permitted is going further: detailed questions about citizenship or immigration status beyond the sponsorship question itself can cross into discrimination. Because the sponsorship question is legally safe for employers to ask, it's become close to universal on online applications, and it's frequently one of the first fields in the application form, well ahead of any human review.</p>

      <h2>Why this matters for how applications get filtered</h2>
      <p>We've written separately about how <a href="/blog-ats-resume-screening">ATS platforms mostly index resumes rather than reject them outright</a>. The sponsorship question is different: it's often a hard-coded screening field tied to a yes/no answer a recruiter configured in advance, which means it <em>can</em> auto-filter before a resume is ever opened, in a way general resume content usually doesn't.</p>

      <h2>Where OPT candidates answer this incorrectly</h2>
      <p>OPT itself is independent work authorization: an EAD card that lets you work for any employer without that employer filing anything, for up to 12 months, or up to 36 months total if you qualify for the STEM OPT extension. Sponsorship — most often an H-1B filing — is a separate, later question about long-term status, not a requirement for your first year or more of employment. If an employer is only asking about <em>current</em> authorization, "do I need sponsorship right now" and "will I ever need sponsorship" have different honest answers, and the form rarely distinguishes between them.</p>

      <h2>A more accurate way to handle it</h2>
      <ul>
        <li><strong>Read the question literally.</strong> "Now or in the future" is broad by design, but if there's a free-text field, a one-line clarification ("Currently authorized to work full-time under OPT through [date]; would require H-1B sponsorship for continued employment after that") is more accurate than a flat yes or no.</li>
        <li><strong>Put your authorization status on the resume itself</strong>, not just the application form — a short line near your contact details ("Authorized to work in the U.S. under F-1 OPT / STEM OPT through [date]") answers the question before it's asked and reads as organized, not evasive.</li>
        <li><strong>Don't guess at future sponsorship needs.</strong> If you haven't decided whether you'll pursue H-1B sponsorship, say your current status and authorization window rather than committing to an answer about a decision that isn't made yet.</li>
      </ul>

      <h2>The bottom line</h2>
      <p>The sponsorship question isn't a trap, and it isn't illegal for an employer to ask — but it rewards precision. Candidates who answer in terms of their actual authorization window, rather than a reflexive yes or no, get through more of these automated first filters than the question's reputation suggests.</p>
""",
    "sources": [
        ("Marks Gray: Immigration-Related Questions Employers Can Ask During the Hiring Process", "https://marksgray.com/immigration-blog/immigration-related-questions-can-employers-ask-hiring-process/"),
        ("USCIS: Optional Practical Training Extension for STEM Students (STEM OPT)", "https://www.uscis.gov/working-in-the-united-states/students-and-exchange-visitors/optional-practical-training-extension-for-stem-students-stem-opt"),
        ("Jobscan: 5 Critical ATS Formatting Mistakes", "https://www.jobscan.co/blog/ats-formatting-mistakes/"),
    ],
    "excerpt": "The sponsorship question is legal, common, and often automated — and most OPT candidates answer it in a way that filters themselves out before a human ever sees the resume. Here's a more accurate way to answer it.",
}
posts.append(post2)

# ---------------------------------------------------------------------------
# POST 3
# ---------------------------------------------------------------------------
post3 = {
    "slug": "blog-opt-placement-agency-red-flags-dhs-warning-2026",
    "title": "OPT and H-1B Placement Agency Red Flags: What DHS Is Warning About in 2026",
    "title_tag": "OPT and H-1B Placement Agency Red Flags: What DHS Is Warning About in 2026",
    "category": "Visa & Work Authorization",
    "date_iso": DATE_ISO,
    "date_display": DATE_DISPLAY,
    "read_time": "6 min",
    "meta_desc": "DHS names IT recruitment firms, consulting companies, and staffing agencies as the three business types most tied to STEM OPT fraud. The exact red flags it lists, and what you legally cannot be charged for, in plain facts.",
    "og_desc": "DHS names IT recruitment firms, consulting companies, and staffing agencies as the business types most tied to STEM OPT fraud. Here's exactly what it's warning about.",
    "h1": "OPT and H-1B Placement Agency Red Flags: What DHS Is Warning About in 2026",
    "lede": "The Department of Homeland Security has named the exact category of business this applies to — IT recruitment, consulting, and staffing firms. Here's what it actually said, and what the law says you can't be charged for, regardless of who you work with.",
    "cta_h2": "Want to check our own answers against this list?",
    "cta_p": "Named U.S., Australian, and Indian offices, W-2 placement, and E-Verify participation — ask us anything on this checklist before you decide.",
    "cta_href": "/contact",
    "cta_label": "Ask us directly",
    "body": """      <p>DHS's Student and Exchange Visitor Program (SEVP) said this year it is actively working with Homeland Security Investigations to identify and investigate fraud tied to STEM OPT employment. It didn't describe this as a general warning about bad actors somewhere out there. It named three specific business types as the pattern it keeps finding: IT recruitment firms, consulting companies, and staffing agencies — categories that have drawn scrutiny since the STEM OPT rule was finalized in 2016.</p>

      <p>Naming the category isn't the same as accusing every company in it. But if you're evaluating any agency in this space, including ours, these are the specific things worth checking.</p>

      <h2>The red flags DHS actually lists</h2>
      <p>On the employer side, investigators flagged patterns including unoccupied or non-operational business addresses, companies run out of residential locations with no real employees, offshore HR and payroll with no U.S. oversight, staff who can't describe what the business actually does, conflicting statements about employment activity, students listed as "employed" who never actually work, and business phone numbers that don't function.</p>
      <p>On the student-facing side, the warning points to vague or thin company websites, job duties that don't match what's written on your Form I-983 training plan, work locations that don't make sense for the stated role, and communication that happens almost entirely through messaging apps rather than official channels.</p>

      <h2>What you legally cannot be charged for</h2>
      <p>Separate from the fraud warning, U.S. Department of Labor Fact Sheet #62H is explicit about H-1B pay deductions. An employer cannot require a worker to pay any part of the statutory ACWIA training and processing fee, cannot deduct any part of the $500 fraud prevention and detection fee, and cannot pass along attorney fees or the premium processing fee tied to filing the H-1B petition. These are classified as employer business expenses by law, not costs that can be shifted onto the candidate under any arrangement, no matter how the contract is worded.</p>

      <h2>A short checklist before you sign anything</h2>
      <ul>
        <li>Does the company have a real, staffed, checkable U.S. office address — not a mailbox or a residential address?</li>
        <li>Will your actual day-to-day work match what's written on your I-983 training plan, if you're on STEM OPT?</li>
        <li>Is communication through a working phone number and company email, not only WhatsApp or WeChat?</li>
        <li>Is the company asking you to pay any H-1B filing-related fee directly? (If yes, that's not a judgment call — it's against the rule above.)</li>
        <li>Can you verify E-Verify enrollment, which STEM OPT training-plan employers are required to maintain?</li>
      </ul>
      <p>We covered the broader question of telling different placement business models apart in a <a href="/blog-choosing-it-job-placement-agency-opt-h1b">separate, more general guide</a> — this one is specifically about the fraud pattern DHS has called out by name.</p>

      <h2>The bottom line</h2>
      <p>None of this is a reason to be afraid of placement services generally — it's a reason to ask specific, checkable questions instead of trusting a homepage. A company with nothing to hide will answer every item on this list directly, usually within one phone call.</p>
""",
    "sources": [
        ("VisaServe: DHS Issues Warning on STEM OPT Employer Fraud", "https://visaserve.com/dhs-issues-warning-on-stem-opt-employer-fraud-what-international-students-and-employers-need-to-know/"),
        ("U.S. Department of Labor: Fact Sheet #62H — H-1B Pay Deductions", "https://www.dol.gov/agencies/whd/fact-sheets/62h-h1b-pay-deductions"),
        ("ICE: Completing the Form I-983 Training Plan for STEM OPT Students", "https://www.ice.gov/doclib/sevis/pdf/i983Instructions.pdf"),
    ],
    "excerpt": "DHS names IT recruitment firms, consulting companies, and staffing agencies as the three business types most tied to STEM OPT fraud. The exact red flags it lists, and what you legally cannot be charged for, in plain facts.",
}
posts.append(post3)

# ---------------------------------------------------------------------------
# Write each post HTML + prepend registry entries
# ---------------------------------------------------------------------------
registry_path = os.path.join(ROOT, "scripts", "posts_registry.json")
with open(registry_path) as f:
    registry = json.load(f)

new_registry_entries = []
for p in posts:
    sources_html = build_sources_html(p["sources"])
    post_for_template = {k: v for k, v in p.items() if k not in ("sources", "excerpt")}
    html = render_post(post_for_template, sources_html)
    out_path = os.path.join(ROOT, f"{p['slug']}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {out_path} ({len(html)} chars)")
    new_registry_entries.append({
        "slug": p["slug"],
        "title": p["title"],
        "category": p["category"],
        "date_iso": p["date_iso"],
        "date_display": p["date_display"],
        "read_time": p["read_time"],
        "excerpt": p["excerpt"],
    })

# newest first: prepend in reverse so final order is post1, post2, post3, ...rest
registry = list(reversed(new_registry_entries)) + registry
with open(registry_path, "w", encoding="utf-8") as f:
    json.dump(registry, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"updated {registry_path} ({len(registry)} total posts)")
