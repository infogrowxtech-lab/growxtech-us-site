#!/usr/bin/env python3
"""One-off: append this week's new course entries to courses_registry.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "scripts", "courses_registry.json")

NEW = [
    {
        "slug": "course-react-basics",
        "course_id": "react-basics",
        "title": "React Programming for Beginners",
        "title_tag": "Free React.js Course with Certificate",
        "meta_desc": "Free course on React.js fundamentals for beginners: components, props, state, and hooks, with a free certificate on completion.",
        "og_desc": "Learn React.js fundamentals: components, props, state, and hooks. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "React powers a huge share of front-end job postings. This course covers components, props, state, and hooks so you can start building real interfaces.",
        "item_desc": "Learn React.js fundamentals including components, props, state, and hooks for front-end development roles.",
        "time_label": "~3 hrs",
        "h1_lead": "Learn React,",
        "h1_grad": "the library behind most front-end job listings.",
        "lede": "React shows up in a huge share of U.S. front-end and full-stack job postings. This course walks through components, props, state, and hooks so you understand how modern web interfaces are actually built.",
        "outcomes": [
            "Build and reuse React components",
            "Pass data between components with props",
            "Manage component state with useState and useEffect",
            "Understand how React fits into a typical front-end job stack"
        ],
        "youtube_id": "bMknfKXIFA8",
        "video_title": "React Course - Beginner's Tutorial for React JavaScript Library [2022]",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the React Programming for Beginners course, what's next?"
    },
    {
        "slug": "course-power-bi-basics",
        "course_id": "power-bi-basics",
        "title": "Power BI for Data Analysis",
        "title_tag": "Free Power BI Course with Certificate",
        "meta_desc": "Free course on Power BI fundamentals: connecting data, building visuals, and dashboards, with a free certificate on completion.",
        "og_desc": "Learn Power BI fundamentals: data modeling, visuals, and dashboards. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Power BI is one of the most requested data analysis tools in U.S. job postings. This course covers connecting data, building visuals, and simple dashboards.",
        "item_desc": "Learn Power BI fundamentals including data connections, visuals, and dashboards for data analyst roles.",
        "time_label": "~4 hrs",
        "h1_lead": "Learn Power BI,",
        "h1_grad": "a top skill on data analyst job postings.",
        "lede": "Power BI shows up constantly in U.S. data analyst and business analyst job listings. This course covers connecting to data sources, building visuals, and putting together a dashboard someone could actually use.",
        "outcomes": [
            "Connect Power BI to common data sources",
            "Build charts, tables, and visuals from raw data",
            "Assemble a working dashboard",
            "Explain Power BI basics confidently in an interview"
        ],
        "youtube_id": "3u7MQz1EyPY",
        "video_title": "Power BI Full Course - Learn Power BI in 4 Hours | Power BI Tutorial for Beginners | Edureka",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Power BI for Data Analysis course, what's next?"
    },
    {
        "slug": "course-software-testing-basics",
        "course_id": "software-testing-basics",
        "title": "Software Testing and QA Fundamentals",
        "title_tag": "Free Software Testing (QA) Course with Certificate",
        "meta_desc": "Free course on software testing and QA fundamentals: manual testing, test cases, and the SDLC, with a free certificate on completion.",
        "og_desc": "Learn software testing and QA fundamentals: test cases, bug reports, and the SDLC. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "QA and software testing is a common entry point into IT. This course covers manual testing, writing test cases, and where QA fits in the development lifecycle.",
        "item_desc": "Learn software testing and QA fundamentals including manual testing, test cases, and the SDLC for QA analyst roles.",
        "time_label": "~3 hrs",
        "h1_lead": "Learn software testing,",
        "h1_grad": "a common way into your first IT role.",
        "lede": "QA and software testing roles are often more approachable for career-changers than pure development roles. This course covers manual testing, writing test cases, bug reports, and where QA fits into the software development lifecycle.",
        "outcomes": [
            "Explain the difference between manual and automated testing",
            "Write a clear test case and bug report",
            "Understand where QA fits in the SDLC",
            "Describe common testing types (functional, regression, UAT) in an interview"
        ],
        "youtube_id": "VQEJJifXqhQ",
        "video_title": "Software Testing Full Course | Software Testing Tutorial For Beginners | Intellipaat",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Software Testing and QA Fundamentals course, what's next?"
    },
    {
        "slug": "course-google-cloud-fundamentals",
        "course_id": "google-cloud-fundamentals",
        "title": "Google Cloud Platform Fundamentals",
        "title_tag": "Free Google Cloud Platform (GCP) Course with Certificate",
        "meta_desc": "Free course on Google Cloud Platform fundamentals: core services, compute, and storage, with a free certificate on completion.",
        "og_desc": "Learn Google Cloud Platform fundamentals: core services, compute, and storage. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Cloud job postings aren't just AWS. This course is an introduction to Google Cloud Platform's core services, compute, and storage options.",
        "item_desc": "Learn Google Cloud Platform fundamentals including core services, compute, and storage for cloud support roles.",
        "time_label": "~3 hrs",
        "h1_lead": "Learn Google Cloud,",
        "h1_grad": "the other major cloud platform employers ask about.",
        "lede": "Not every cloud job posting asks for AWS. This course introduces Google Cloud Platform's core infrastructure, compute, and storage services, so you can speak to GCP basics alongside whatever other cloud skills you're building.",
        "outcomes": [
            "Describe GCP's core infrastructure and regions",
            "Explain the basics of compute and storage options on GCP",
            "Compare GCP's services to AWS/Azure equivalents",
            "Discuss GCP fundamentals confidently in a technical screen"
        ],
        "youtube_id": "6VRatA0SAwE",
        "video_title": "Google Cloud Platform Full Course | Google Cloud Platform Tutorial | Cloud Computing | Simplilearn",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Google Cloud Platform Fundamentals course, what's next?"
    },
    {
        "slug": "course-agile-scrum-basics",
        "course_id": "agile-scrum-basics",
        "title": "Agile and Scrum Fundamentals",
        "title_tag": "Free Agile and Scrum Course with Certificate",
        "meta_desc": "Free course on Agile and Scrum fundamentals: sprints, standups, and team roles, with a free certificate on completion.",
        "og_desc": "Learn Agile and Scrum fundamentals: sprints, standups, and team roles. Free course, free certificate.",
        "category": "Career Skills",
        "card_desc": "Almost every IT team runs on some version of Agile. This course covers sprints, standups, backlogs, and team roles so you can walk into any team already speaking the language.",
        "item_desc": "Learn Agile and Scrum fundamentals including sprints, standups, and team roles for IT and project roles.",
        "time_label": "~4 hrs",
        "h1_lead": "Learn Agile and Scrum,",
        "h1_grad": "the way most IT teams actually work.",
        "lede": "Nearly every IT job posting mentions Agile or Scrum somewhere. This course covers sprints, standups, backlogs, and the core team roles, so you can walk into a new team already speaking the language instead of learning it on day one.",
        "outcomes": [
            "Explain the difference between Agile and Scrum",
            "Describe a sprint cycle and daily standup",
            "Identify the core Scrum team roles",
            "Talk through Agile basics confidently in an interview"
        ],
        "youtube_id": "VFQtSqChlsk",
        "video_title": "Agile Scrum Full Course In 4 Hours | Agile Scrum Master Training | Agile Training Video | Simplilearn",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more than a certificate?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Agile and Scrum Fundamentals course, what's next?"
    },
    {
        "slug": "course-remote-work-skills",
        "course_id": "remote-work-skills",
        "title": "Remote Work Skills for IT Job Seekers",
        "title_tag": "Free Remote Work Skills Course with Certificate",
        "meta_desc": "Free course on finding and succeeding in remote IT jobs: where to look, how to stand out, and staying productive, with a free certificate.",
        "og_desc": "Learn how to find and succeed in remote IT jobs. Free course, free certificate.",
        "category": "Career Skills",
        "card_desc": "Remote roles are some of the most competitive postings out there. This course covers where to find legitimate remote IT jobs and how to stand out once you apply.",
        "item_desc": "Learn how to find legitimate remote job opportunities and build the habits that make a remote hire successful.",
        "time_label": "~20 min",
        "h1_lead": "Find and succeed in",
        "h1_grad": "remote IT roles.",
        "lede": "Remote postings get flooded with applicants, so standing out takes more than a generic resume. This course covers where legitimate remote IT roles actually get posted and what makes an employer trust a candidate to work unsupervised.",
        "outcomes": [
            "Identify where legitimate remote IT jobs are actually posted",
            "Spot red flags of remote job scams",
            "Build a routine that signals reliability to a remote employer",
            "Position your application for remote-specific requirements"
        ],
        "youtube_id": "ztG-GNT0pWQ",
        "video_title": "10 Remote Jobs You Can Work From Home - No Experience Needed! | Indeed Career Tips",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more than a certificate?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Remote Work Skills for IT Job Seekers course, what's next?"
    },
    {
        "slug": "course-behavioral-interview-star",
        "course_id": "behavioral-interview-star",
        "title": "Behavioral Interview Questions (STAR Method)",
        "title_tag": "Free Behavioral Interview (STAR Method) Course with Certificate",
        "meta_desc": "Free course on answering behavioral interview questions with the STAR method, with a free certificate on completion.",
        "og_desc": "Learn to answer behavioral interview questions with the STAR method. Free course, free certificate.",
        "category": "Job Search Strategy",
        "card_desc": "\"Tell me about a time...\" questions trip up a lot of candidates. This course breaks down the STAR method so your answers have structure instead of rambling.",
        "item_desc": "Learn to structure behavioral interview answers using the STAR method (Situation, Task, Action, Result).",
        "time_label": "~15 min",
        "h1_lead": "Answer \"tell me about a time...\"",
        "h1_grad": "with a structure that works.",
        "lede": "Behavioral questions catch a lot of candidates off guard, even strong ones. This course walks through the STAR method - Situation, Task, Action, Result - so you can turn a vague memory into a tight, confident answer.",
        "outcomes": [
            "Break any behavioral question into Situation, Task, Action, Result",
            "Prepare 3-4 stories that cover most common behavioral questions",
            "Avoid rambling or vague answers under pressure",
            "Tie your answer back to the role you're interviewing for"
        ],
        "youtube_id": "_IiNubuNY1E",
        "video_title": "STAR METHOD ANSWERS TO BEHAVIOURAL INTERVIEW QUESTIONS! (100% PASS!) JOB INTERVIEW TIPS!",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to practice this live?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Behavioral Interview Questions (STAR Method) course, what's next?"
    },
    {
        "slug": "course-personal-branding",
        "course_id": "personal-branding",
        "title": "Personal Branding for Job Seekers",
        "title_tag": "Free Personal Branding Course with Certificate",
        "meta_desc": "Free course on building a personal brand for your job search: LinkedIn, resume, and online presence, with a free certificate.",
        "og_desc": "Learn to build a personal brand for your job search. Free course, free certificate.",
        "category": "Job Search Strategy",
        "card_desc": "Recruiters look you up before they call you. This course covers how to build a consistent, professional personal brand across LinkedIn, your resume, and the rest of your online presence.",
        "item_desc": "Learn to build a consistent personal brand across LinkedIn, resume, and online presence for a job search.",
        "time_label": "~15 min",
        "h1_lead": "Build a personal brand",
        "h1_grad": "that holds up when a recruiter Googles you.",
        "lede": "Most recruiters check LinkedIn and search your name before they ever call you. This course covers how to build a consistent, professional personal brand across your profile, resume, and online presence so that first impression works for you.",
        "outcomes": [
            "Define the one or two things you want to be known for professionally",
            "Make your LinkedIn, resume, and online presence tell the same story",
            "Clean up anything that could hurt a background search",
            "Use your personal brand to stand out in a crowded applicant pool"
        ],
        "youtube_id": "sKmIDas35l8",
        "video_title": "Personal Branding 101: FUTUREPROOF Yourself and Launch Your Career",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more than a certificate?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Personal Branding for Job Seekers course, what's next?"
    },
    {
        "slug": "course-comptia-network-plus",
        "course_id": "comptia-network-plus",
        "title": "CompTIA Network+ Certification Overview",
        "title_tag": "Free CompTIA Network+ Overview Course with Certificate",
        "meta_desc": "Free overview course on the CompTIA Network+ certification: exam objectives, cost, and career value, with a free certificate.",
        "og_desc": "Learn what the CompTIA Network+ certification covers and whether it's worth pursuing. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "Network+ is one of the most common entry-level networking certifications employers recognize. This course covers what the exam tests and who it's actually useful for.",
        "item_desc": "Overview of the CompTIA Network+ certification including exam objectives, cost, and career value.",
        "time_label": "~20 min",
        "h1_lead": "Is CompTIA Network+",
        "h1_grad": "worth it for your career path?",
        "lede": "Network+ comes up constantly in entry-level IT and help desk job postings. This course walks through what the exam actually covers, roughly what it costs, and the kinds of roles it tends to open doors for.",
        "outcomes": [
            "Describe what the Network+ exam covers at a high level",
            "Estimate the cost and time commitment to prepare for it",
            "Identify which job roles value this certification most",
            "Decide whether it fits your own career plan"
        ],
        "youtube_id": "rJTpSM4Cb98",
        "video_title": "Overview CompTIA Network+ - (Exam Objectives, Resources, Job Market)",
        "upload_date": "2024-01-01",
        "cta_h2": "Not sure which certification to chase?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the CompTIA Network+ Certification Overview course, what's next?"
    },
    {
        "slug": "course-itil-foundation-overview",
        "course_id": "itil-foundation-overview",
        "title": "ITIL 4 Foundation Certification Overview",
        "title_tag": "Free ITIL 4 Foundation Overview Course with Certificate",
        "meta_desc": "Free overview course on the ITIL 4 Foundation certification: what it covers, cost, and career value, with a free certificate.",
        "og_desc": "Learn what the ITIL 4 Foundation certification covers and whether it's worth pursuing. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "ITIL shows up often in IT service management job postings. This course is a quick overview of what the ITIL 4 Foundation certification covers and who benefits from it.",
        "item_desc": "Overview of the ITIL 4 Foundation certification including core concepts, cost, and career value.",
        "time_label": "~15 min",
        "h1_lead": "Is ITIL 4 Foundation",
        "h1_grad": "worth it for an IT service role?",
        "lede": "ITIL comes up frequently in IT service management, help desk, and operations job postings. This course gives a quick overview of what the ITIL 4 Foundation framework and certification actually cover.",
        "outcomes": [
            "Explain what ITIL 4 is and what problem it solves",
            "Describe the basic structure of the ITIL 4 framework",
            "Estimate the cost and time commitment to get certified",
            "Decide whether ITIL fits your career direction"
        ],
        "youtube_id": "YOiC70Kg6yA",
        "video_title": "What Is ITIL 4? Learn the ITIL Framework in Just 8 Minutes!",
        "upload_date": "2024-01-01",
        "cta_h2": "Not sure which certification to chase?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the ITIL 4 Foundation Certification Overview course, what's next?"
    },
    {
        "slug": "course-google-data-analytics-cert",
        "course_id": "google-data-analytics-cert",
        "title": "Google Data Analytics Certificate Overview",
        "title_tag": "Free Google Data Analytics Certificate Overview Course",
        "meta_desc": "Free overview course on the Google Data Analytics Certificate: what it covers, cost, and whether it's worth it, with a free certificate.",
        "og_desc": "Learn what the Google Data Analytics Certificate covers and whether it's worth pursuing. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "Google's Data Analytics Certificate is one of the most searched-for entry points into data roles. This course covers what it actually teaches and who it's a good fit for.",
        "item_desc": "Overview of the Google Data Analytics Certificate including what it covers and its career value.",
        "time_label": "~15 min",
        "h1_lead": "Is the Google Data Analytics Certificate",
        "h1_grad": "actually worth it?",
        "lede": "The Google Data Analytics Certificate is one of the most recommended entry points into data roles, but it isn't right for everyone. This course covers what the program actually teaches, roughly what it costs, and who tends to benefit most from it.",
        "outcomes": [
            "Describe what the Google Data Analytics Certificate covers",
            "Estimate the cost and time commitment to complete it",
            "Identify what kinds of roles it realistically prepares you for",
            "Decide whether it's a good next step for your situation"
        ],
        "youtube_id": "N7a4yMziXo0",
        "video_title": "Is The Google Data Analytics Certificate ACTUALLY Worth It? (Review)",
        "upload_date": "2024-01-01",
        "cta_h2": "Not sure which certification to chase?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Google Data Analytics Certificate Overview course, what's next?"
    },
    {
        "slug": "course-nonprofit-careers",
        "course_id": "nonprofit-careers",
        "title": "Nonprofit Sector Careers 101",
        "title_tag": "Free Nonprofit Careers Course with Certificate",
        "meta_desc": "Free course on breaking into nonprofit careers: common roles, required skills, and realistic expectations, with a free certificate.",
        "og_desc": "Learn about common roles and realistic expectations for nonprofit sector careers. Free course, free certificate.",
        "category": "Industry Career Guides",
        "card_desc": "Nonprofit work covers far more than fundraising. This course walks through the common paid roles in the sector and what it actually takes to land one.",
        "item_desc": "Learn about common paid roles in the nonprofit sector and what it takes to break into one.",
        "time_label": "~20 min",
        "h1_lead": "Nonprofit careers,",
        "h1_grad": "beyond just fundraising.",
        "lede": "Nonprofit work covers operations, program management, communications, IT, finance, and more, not just fundraising. This course walks through the common paid roles in the sector and what it realistically takes to land one.",
        "outcomes": [
            "Identify the main categories of paid nonprofit roles",
            "Understand typical pay and growth expectations in the sector",
            "Know what nonprofit hiring managers tend to prioritize",
            "Decide if a nonprofit career path fits your goals"
        ],
        "youtube_id": "2EhHN1HTfPw",
        "video_title": "22 Types of Paid Nonprofit Jobs & Careers",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more than a certificate?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Nonprofit Sector Careers 101 course, what's next?"
    },
]

def main():
    with open(REG, "r", encoding="utf-8") as f:
        registry = json.load(f)
    existing_slugs = {c["slug"] for c in registry}
    existing_ids = {c["youtube_id"] for c in registry}
    for c in NEW:
        if c["slug"] in existing_slugs:
            raise SystemExit(f"duplicate slug: {c['slug']}")
        if c["youtube_id"] in existing_ids:
            raise SystemExit(f"duplicate youtube_id: {c['youtube_id']} ({c['slug']})")
        registry.append(c)
    with open(REG, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Appended {len(NEW)} new courses. Registry now has {len(registry)} total.")

if __name__ == "__main__":
    main()
