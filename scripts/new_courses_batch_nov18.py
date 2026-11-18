#!/usr/bin/env python3
"""One-off: append this week's (2026-11-18) new course entries to courses_registry.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "scripts", "courses_registry.json")

NEW = [
    {
        "slug": "course-active-listening-at-work",
        "course_id": "active-listening-at-work",
        "title": "Active Listening at Work",
        "title_tag": "Free Active Listening Course with Certificate",
        "meta_desc": "Free course on active listening skills for the workplace: full attention, better questions, and avoiding the habits that make people feel unheard, with a free certificate on completion.",
        "og_desc": "Learn active listening skills for the workplace and better conversations. Free course, free certificate.",
        "category": "Career Skills",
        "card_desc": "Most workplace friction traces back to someone feeling unheard. This course covers the habits of genuinely good listeners and the small mistakes that quietly undermine trust.",
        "item_desc": "Learn active listening habits that build trust and avoid common workplace miscommunication.",
        "time_label": "~10 min",
        "h1_lead": "Learn active listening,",
        "h1_grad": "the skill behind almost every strong working relationship.",
        "lede": "Being a good listener is one of the most underrated career skills there is: it builds trust with managers, smooths conflict with coworkers, and makes you the person people actually want on their team. This course breaks down what good listeners do differently.",
        "outcomes": [
            "Recognize the habits that make people feel unheard",
            "Practice giving full attention without interrupting or planning your reply",
            "Ask better follow-up questions in work conversations",
            "Apply active listening in 1-on-1s, feedback, and team meetings"
        ],
        "youtube_id": "cSohjlYQI2A",
        "video_title": "5 ways to listen better | Julian Treasure | TED",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more help building workplace skills?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Active Listening at Work course, what's next?"
    },
    {
        "slug": "course-workplace-stress-management",
        "course_id": "workplace-stress-management",
        "title": "Workplace Stress Management",
        "title_tag": "Free Workplace Stress Management Course with Certificate",
        "meta_desc": "Free course on managing workplace stress: recognizing burnout early, practical coping techniques, and turning pressure into focus, with a free certificate on completion.",
        "og_desc": "Learn practical techniques for managing workplace stress and avoiding burnout. Free course, free certificate.",
        "category": "Career Skills",
        "card_desc": "A demanding job doesn't have to mean constant burnout. This course covers how to recognize stress building up early and practical ways to manage it before it affects your work or health.",
        "item_desc": "Learn practical techniques for managing workplace stress and avoiding burnout.",
        "time_label": "~12 min",
        "h1_lead": "Manage workplace stress,",
        "h1_grad": "before it turns into burnout.",
        "lede": "Pressure at work is normal; letting it build unmanaged until it becomes burnout is not. This course covers how to recognize the early signs of work stress and practical, realistic techniques for handling it day to day.",
        "outcomes": [
            "Recognize the early signs of work-related stress and burnout",
            "Apply practical techniques for managing pressure day to day",
            "Separate productive stress from the kind that needs addressing",
            "Build habits that protect your focus and energy at work"
        ],
        "youtube_id": "yrwWvdM_Yns",
        "video_title": "How to channel your stress to help you succeed | Heidi Hanna | TEDxSDSU",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more support once you're hired?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Workplace Stress Management course, what's next?"
    },
    {
        "slug": "course-using-ai-tools-in-job-search",
        "course_id": "using-ai-tools-in-job-search",
        "title": "Using AI Tools in Your Job Search",
        "title_tag": "Free AI Job Search Tools Course with Certificate",
        "meta_desc": "Free course on using AI tools like ChatGPT in your job search: tailoring resumes, drafting outreach, and prepping for interviews faster, with a free certificate on completion.",
        "og_desc": "Learn how to use AI tools like ChatGPT to speed up your job search. Free course, free certificate.",
        "category": "Job Search Strategy",
        "card_desc": "AI tools can genuinely speed up a job search when used well, and just as easily produce generic junk when used badly. This course covers the practical, responsible way to use them.",
        "item_desc": "Learn how to use AI tools like ChatGPT to speed up and improve your job search.",
        "time_label": "~15 min",
        "h1_lead": "Use AI tools well,",
        "h1_grad": "to speed up your job search without sounding like a robot.",
        "lede": "Tools like ChatGPT can help tailor a resume to a job posting, draft outreach messages, and prep for interview questions in a fraction of the time it used to take. This course covers how to use them effectively without losing the personal, honest voice that actually gets you hired.",
        "outcomes": [
            "Use AI tools to tailor a resume and cover letter to a specific job",
            "Draft outreach and networking messages faster without sounding generic",
            "Prep for interview questions using AI as a practice partner",
            "Avoid the common mistakes that make AI-assisted applications obvious"
        ],
        "youtube_id": "pmnY5V16GSE",
        "video_title": "Land a Job using ChatGPT: The Definitive Guide!",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more help landing the offer?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Using AI Tools in Your Job Search course, what's next?"
    },
    {
        "slug": "course-elevator-pitch-for-job-seekers",
        "course_id": "elevator-pitch-for-job-seekers",
        "title": "Elevator Pitch for Job Seekers",
        "title_tag": "Free Elevator Pitch Course with Certificate",
        "meta_desc": "Free course on building a strong 30-second elevator pitch for interviews, networking events, and LinkedIn outreach, with a free certificate on completion.",
        "og_desc": "Learn how to build a strong elevator pitch for interviews and networking. Free course, free certificate.",
        "category": "Job Search Strategy",
        "card_desc": "\"Tell me about yourself\" trips up more candidates than almost any other question. This course covers how to build a tight, natural pitch you can use in interviews, networking events, and cold outreach.",
        "item_desc": "Learn how to build a strong, natural elevator pitch for interviews and networking.",
        "time_label": "~10 min",
        "h1_lead": "Build your elevator pitch,",
        "h1_grad": "so you're never caught flat by \"tell me about yourself.\"",
        "lede": "A strong elevator pitch is the difference between rambling through \"tell me about yourself\" and opening an interview or networking conversation with confidence. This course covers how to build a tight, natural 30-second pitch and adapt it to interviews, events, and cold outreach.",
        "outcomes": [
            "Structure a clear 30-second pitch that highlights your strengths",
            "Adapt the pitch for interviews, networking events, and LinkedIn messages",
            "Avoid sounding rehearsed or overly rehearsed-sounding",
            "Practice delivering it naturally under pressure"
        ],
        "youtube_id": "lwuk7vq8Yfo",
        "video_title": "The PERFECT Elevator Pitch - Introduce Yourself In 30 Seconds Or Less",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more help landing the offer?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Elevator Pitch for Job Seekers course, what's next?"
    },
    {
        "slug": "course-apache-spark-basics",
        "course_id": "apache-spark-basics",
        "title": "Apache Spark Basics",
        "title_tag": "Free Apache Spark Course with Certificate",
        "meta_desc": "Free course on Apache Spark fundamentals for beginners: distributed processing, RDDs, and running big data jobs, with a free certificate on completion.",
        "og_desc": "Learn Apache Spark fundamentals for distributed big data processing. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Apache Spark is the engine behind most large-scale data processing in the industry today. This course covers the fundamentals: distributed processing, RDDs/DataFrames, and running real jobs.",
        "item_desc": "Learn Apache Spark fundamentals for distributed big data processing.",
        "time_label": "~3 hrs",
        "h1_lead": "Learn Apache Spark,",
        "h1_grad": "the engine behind most large-scale data processing.",
        "lede": "Apache Spark is what most companies actually run when they need to process data too large for a single machine, and it shows up constantly in data engineering and data analyst job postings. This course covers the fundamentals of distributed processing, DataFrames, and running real Spark jobs.",
        "outcomes": [
            "Understand how Spark distributes data processing across a cluster",
            "Work with RDDs and DataFrames to transform large datasets",
            "Run basic Spark jobs and understand the execution model",
            "Explain why companies use Spark for big data in an interview"
        ],
        "youtube_id": "528ojyDmJTk",
        "video_title": "Apache Spark Full Course | Apache Spark Tutorial For Beginners",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Apache Spark Basics course, what's next?"
    },
    {
        "slug": "course-postman-api-testing-basics",
        "course_id": "postman-api-testing-basics",
        "title": "Postman API Testing Basics",
        "title_tag": "Free Postman API Testing Course with Certificate",
        "meta_desc": "Free course on API testing with Postman for beginners: requests, collections, and automating API tests, with a free certificate on completion.",
        "og_desc": "Learn API testing with Postman: requests, collections, and test automation. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Postman is the tool most QA and backend teams actually use to test APIs day to day. This course covers building requests, collections, and basic automated API tests.",
        "item_desc": "Learn API testing with Postman: requests, collections, and test automation.",
        "time_label": "~2 hrs",
        "h1_lead": "Learn Postman,",
        "h1_grad": "the tool most teams use to test APIs.",
        "lede": "Postman is the de facto standard for testing and documenting APIs across QA, backend, and DevOps teams. This course covers building requests, organizing them into collections, and writing basic automated tests on top of an API.",
        "outcomes": [
            "Build and send API requests using Postman",
            "Organize requests into collections and environments",
            "Write basic automated tests on API responses",
            "Explain API testing fundamentals in a technical interview"
        ],
        "youtube_id": "VywxIQ2ZXw4",
        "video_title": "Postman Beginner's Course - API Testing",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Postman API Testing Basics course, what's next?"
    },
    {
        "slug": "course-site-reliability-engineering-basics",
        "course_id": "site-reliability-engineering-basics",
        "title": "Site Reliability Engineering (SRE) Fundamentals",
        "title_tag": "Free Site Reliability Engineering Course with Certificate",
        "meta_desc": "Free course on Site Reliability Engineering (SRE) fundamentals: uptime, incident response, and how SRE differs from traditional ops, with a free certificate on completion.",
        "og_desc": "Learn Site Reliability Engineering (SRE) fundamentals: uptime, monitoring, and incident response. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "SRE is one of the fastest-growing roles in infrastructure, and the concepts behind it (SLOs, error budgets, incident response) show up in interviews across DevOps and platform teams. This course covers the fundamentals.",
        "item_desc": "Learn Site Reliability Engineering (SRE) fundamentals: SLOs, monitoring, and incident response.",
        "time_label": "~30 min",
        "h1_lead": "Learn SRE fundamentals,",
        "h1_grad": "the discipline behind keeping systems reliable at scale.",
        "lede": "Site Reliability Engineering grew out of Google's approach to running software reliably at massive scale, and its core ideas (SLOs, error budgets, structured incident response) now show up across DevOps, platform, and infrastructure job postings. This course covers what SRE actually is and how it differs from traditional ops.",
        "outcomes": [
            "Explain what Site Reliability Engineering is and where it came from",
            "Understand SLOs, SLAs, and error budgets at a working level",
            "Describe how SRE teams approach monitoring and incident response",
            "Discuss SRE concepts credibly in a DevOps or platform interview"
        ],
        "youtube_id": "NJsjrXgsBYo",
        "video_title": "What is SRE? Explained in 6 minutes",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Site Reliability Engineering (SRE) Fundamentals course, what's next?"
    },
    {
        "slug": "course-scala-programming-basics",
        "course_id": "scala-programming-basics",
        "title": "Scala Programming Basics",
        "title_tag": "Free Scala Course with Certificate",
        "meta_desc": "Free course on Scala programming fundamentals for beginners: syntax, functional programming basics, and where Scala is used, with a free certificate on completion.",
        "og_desc": "Learn Scala programming fundamentals and functional programming basics. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Scala powers a lot of the big data and backend infrastructure behind Spark and large-scale JVM systems. This course covers the core syntax and functional programming ideas that make Scala distinct.",
        "item_desc": "Learn Scala programming fundamentals and functional programming basics.",
        "time_label": "~2.5 hrs",
        "h1_lead": "Learn Scala,",
        "h1_grad": "the language behind Apache Spark and a lot of JVM infrastructure.",
        "lede": "Scala blends object-oriented and functional programming on the JVM, and it's the language Apache Spark itself is written in, which makes it common in data engineering and backend infrastructure teams. This course covers the core syntax and functional programming ideas that set Scala apart.",
        "outcomes": [
            "Write and run basic Scala programs",
            "Understand core functional programming concepts in Scala",
            "Work with Scala's collections and pattern matching",
            "Explain where and why companies use Scala in an interview"
        ],
        "youtube_id": "OfngvXKNkpM",
        "video_title": "Scala Tutorial for Beginners",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Scala Programming Basics course, what's next?"
    },
    {
        "slug": "course-cissp-certification-overview",
        "course_id": "cissp-certification-overview",
        "title": "CISSP Certification Overview",
        "title_tag": "Free CISSP Certification Overview Course",
        "meta_desc": "Free overview course on the CISSP certification: what it covers, who it's for, and whether it's worth pursuing for a cybersecurity career, with a free certificate on completion.",
        "og_desc": "An honest overview of the CISSP certification: what it covers and who it's for. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "CISSP is one of the most recognized credentials in cybersecurity, but it's not an entry-level cert. This overview covers what it actually tests, who it's realistically for, and what to expect.",
        "item_desc": "An honest overview of what the CISSP certification covers and who it's for.",
        "time_label": "~25 min",
        "h1_lead": "What is CISSP,",
        "h1_grad": "and is it the right certification for you right now?",
        "lede": "CISSP (Certified Information Systems Security Professional) is one of the most respected credentials in cybersecurity, but it's aimed at experienced security professionals, not beginners. This overview covers the eight domains it tests, the experience requirements, and whether it's the right next step for your career stage.",
        "outcomes": [
            "Understand what the CISSP certification tests and who issues it",
            "Know the experience requirements before you commit to studying",
            "Recognize the eight CISSP domains at a high level",
            "Decide whether CISSP fits your current career stage or if another cert fits better"
        ],
        "youtube_id": "i6vKjSa20iw",
        "video_title": "CISSP Full Training Masterclass In 3 Hours | CISSP Tutorial | Simplilearn",
        "upload_date": "2024-01-01",
        "cta_h2": "Want help planning your certification path?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course is an overview, not full certification prep. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the CISSP Certification Overview course, what's next?"
    },
    {
        "slug": "course-google-project-management-cert-overview",
        "course_id": "google-project-management-cert-overview",
        "title": "Google Project Management Certificate Overview",
        "title_tag": "Free Google Project Management Certificate Overview Course",
        "meta_desc": "Free overview course on the Google Project Management Certificate: what it covers, who it's for, and how it compares to PMP, with a free certificate on completion.",
        "og_desc": "An honest overview of the Google Project Management Certificate and who it's for. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "The Google Project Management Certificate is a popular, beginner-friendly way into project management roles. This overview covers what it actually teaches and how it compares to credentials like PMP.",
        "item_desc": "An honest overview of what the Google Project Management Certificate covers and who it's for.",
        "time_label": "~15 min",
        "h1_lead": "What is the Google PM Certificate,",
        "h1_grad": "and is it a real path into project management?",
        "lede": "The Google Project Management Certificate is one of the most accessible ways to break into project management, with no prior experience required and a curriculum built around real PM tools and frameworks. This overview covers what it teaches, how long it takes, and how it compares to credentials like PMP for someone earlier in their career.",
        "outcomes": [
            "Understand what the Google Project Management Certificate covers",
            "Know the time commitment and prerequisites (there aren't many)",
            "See how it compares to PMP and other PM credentials",
            "Decide whether it fits your career stage and goals"
        ],
        "youtube_id": "rck3MnC7OXA",
        "video_title": "Intro to Project Management | Google Project Management Certificate",
        "upload_date": "2024-01-01",
        "cta_h2": "Want help planning your certification path?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course is an overview, not the full certificate program. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Google Project Management Certificate Overview course, what's next?"
    },
    {
        "slug": "course-aerospace-defense-careers",
        "course_id": "aerospace-defense-careers",
        "title": "Aerospace and Defense Careers",
        "title_tag": "Free Aerospace and Defense Careers Overview Course",
        "meta_desc": "Free overview course on building a career in aerospace and defense: common roles, required clearances, and how IT skills fit in, with a free certificate on completion.",
        "og_desc": "Learn what building a career in aerospace and defense actually looks like. Free course, free certificate.",
        "category": "Industry Career Guides",
        "card_desc": "Aerospace and defense hires far more than engineers: IT, cybersecurity, logistics, and program roles are all in demand. This guide covers what the industry actually looks like day to day.",
        "item_desc": "A real intro to building a career in aerospace and defense, including IT-adjacent roles.",
        "time_label": "~20 min",
        "h1_lead": "Explore aerospace and defense careers,",
        "h1_grad": "an industry that runs on more than engineers.",
        "lede": "Aerospace and defense is a massive, stable employer that needs far more than aerospace engineers: IT, cybersecurity, supply chain, and program management roles all have a place in it, often with security clearance requirements that add their own process. This guide covers what the industry actually looks like and where non-engineering candidates fit in.",
        "outcomes": [
            "Understand the range of roles in aerospace and defense beyond engineering",
            "Learn how security clearances affect hiring and timelines",
            "See where IT and cybersecurity skills fit into the industry",
            "Know what a typical day looks like in a core aerospace/defense role"
        ],
        "youtube_id": "U3a4cM3Y1AA",
        "video_title": "A Day in the Life - Aerospace Engineer",
        "upload_date": "2024-01-01",
        "cta_h2": "Curious if this industry is a fit for you?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "Growx places candidates across aerospace and defense alongside IT. A recruiter can help you figure out where your background actually fits.",
        "grobo_msg": "I finished the Aerospace and Defense Careers course, what's next?"
    },
    {
        "slug": "course-agriculture-agtech-careers",
        "course_id": "agriculture-agtech-careers",
        "title": "Agriculture and AgTech Careers",
        "title_tag": "Free Agriculture and AgTech Careers Overview Course",
        "meta_desc": "Free overview course on careers in agriculture and AgTech: how technology is reshaping farming jobs and where IT skills fit in, with a free certificate on completion.",
        "og_desc": "Learn how technology is reshaping agriculture careers and where IT skills fit in. Free course, free certificate.",
        "category": "Industry Career Guides",
        "card_desc": "Modern agriculture runs on sensors, data, and automation as much as it runs on fieldwork. This guide covers how AgTech is changing the industry and where tech and IT skills fit in.",
        "item_desc": "A real intro to agriculture and AgTech careers, including where IT skills fit in.",
        "time_label": "~15 min",
        "h1_lead": "Explore agriculture and AgTech careers,",
        "h1_grad": "an industry being rebuilt around data and automation.",
        "lede": "Agriculture today runs on sensors, drones, data platforms, and automated equipment nearly as much as it runs on fieldwork, which has opened the industry up to a wave of tech and IT-adjacent roles. This guide covers how AgTech is changing farming careers and where candidates with technical backgrounds fit in.",
        "outcomes": [
            "Understand how technology is reshaping modern agriculture",
            "See the range of roles in AgTech beyond traditional farming",
            "Learn where data, IoT, and software skills fit into the industry",
            "Know what a career path in AgTech can realistically look like"
        ],
        "youtube_id": "SW6W1e6Zr6Q",
        "video_title": "Careers in AgTech | Spill The Greens - Episode 2",
        "upload_date": "2024-01-01",
        "cta_h2": "Curious if this industry is a fit for you?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "Growx places candidates across agriculture and AgTech alongside IT. A recruiter can help you figure out where your background actually fits.",
        "grobo_msg": "I finished the Agriculture and AgTech Careers course, what's next?"
    },
]

with open(REG) as f:
    registry = json.load(f)

existing_slugs = {c["slug"] for c in registry}
for c in NEW:
    if c["slug"] in existing_slugs:
        raise SystemExit(f"Duplicate slug, aborting: {c['slug']}")

# Insert each new course after the last existing course of its category,
# keeping registry order grouped by category (display order within category).
for c in NEW:
    cat = c["category"]
    last_idx = -1
    for i, existing in enumerate(registry):
        if existing["category"] == cat:
            last_idx = i
    registry.insert(last_idx + 1, c)

with open(REG, "w") as f:
    json.dump(registry, f, indent=2)
    f.write("\n")

print(f"Appended {len(NEW)} new courses. Registry now has {len(registry)} total.")
