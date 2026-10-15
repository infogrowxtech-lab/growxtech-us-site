#!/usr/bin/env python3
"""One-off: append this week's (2026-10-14) new course entries to courses_registry.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "scripts", "courses_registry.json")

NEW = [
    {
        "slug": "course-go-programming-basics",
        "course_id": "go-programming-basics",
        "title": "Go Programming for Beginners",
        "title_tag": "Free Go (Golang) Course with Certificate",
        "meta_desc": "Free course on Go (Golang) programming fundamentals for beginners: syntax, concurrency basics, and where Go fits in backend job postings.",
        "og_desc": "Learn Go (Golang) fundamentals: syntax, functions, and concurrency basics. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Go is the language behind a growing share of backend and cloud infrastructure job postings. This course covers syntax, functions, and the basics of goroutines.",
        "item_desc": "Learn Go (Golang) programming fundamentals including syntax, functions, and concurrency basics for backend roles.",
        "time_label": "~7 hrs",
        "h1_lead": "Learn Go,",
        "h1_grad": "the language behind modern backend systems.",
        "lede": "Go (Golang) shows up constantly in backend, DevOps, and cloud infrastructure job postings because it's fast, simple, and built for concurrency. This course walks through syntax, functions, and the basics of goroutines so you understand how Go differs from other languages.",
        "outcomes": [
            "Write and run basic Go programs",
            "Use Go's core data types, functions, and control flow",
            "Understand goroutines and channels at a basic level",
            "Explain why companies choose Go for backend services in an interview"
        ],
        "youtube_id": "YS4e4q9oBaU",
        "video_title": "Learn Go Programming - Golang Tutorial for Beginners",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Go Programming for Beginners course, what's next?"
    },
    {
        "slug": "course-machine-learning-fundamentals",
        "course_id": "machine-learning-fundamentals",
        "title": "Machine Learning Fundamentals",
        "title_tag": "Free Machine Learning Course with Certificate",
        "meta_desc": "Free course introducing machine learning fundamentals: what ML is, common algorithm types, and where it fits in IT job postings.",
        "og_desc": "Learn machine learning fundamentals: what ML is and how it's used. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Machine learning now shows up in job postings well beyond data science. This course covers what ML actually is, common algorithm types, and how it's used in practice.",
        "item_desc": "Learn machine learning fundamentals including core concepts and algorithm types relevant to IT and data roles.",
        "time_label": "~1 hr",
        "h1_lead": "Learn machine learning,",
        "h1_grad": "the concept behind most AI job postings.",
        "lede": "Machine learning terminology now shows up in job postings far beyond data science teams. This course introduces what ML actually is, the difference between supervised and unsupervised learning, and how these systems are used in real products.",
        "outcomes": [
            "Define machine learning in plain terms",
            "Distinguish supervised, unsupervised, and reinforcement learning",
            "Recognize common ML use cases in real products",
            "Speak confidently about ML basics in a non-technical interview"
        ],
        "youtube_id": "ukzFI9rgwfU",
        "video_title": "Machine Learning | What Is Machine Learning? | Introduction To Machine Learning | Simplilearn",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Machine Learning Fundamentals course, what's next?"
    },
    {
        "slug": "course-mongodb-nosql-basics",
        "course_id": "mongodb-nosql-basics",
        "title": "MongoDB and NoSQL Databases Basics",
        "title_tag": "Free MongoDB Course with Certificate",
        "meta_desc": "Free course on MongoDB and NoSQL database fundamentals: documents, collections, and basic queries, with a free certificate on completion.",
        "og_desc": "Learn MongoDB and NoSQL fundamentals: documents, collections, and queries. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "NoSQL databases like MongoDB show up constantly alongside SQL in backend job postings. This course covers documents, collections, and basic queries.",
        "item_desc": "Learn MongoDB and NoSQL database fundamentals including documents, collections, and queries for backend roles.",
        "time_label": "~1.5 hrs",
        "h1_lead": "Learn MongoDB,",
        "h1_grad": "the NoSQL database behind countless backend stacks.",
        "lede": "Most backend job postings now expect comfort with both SQL and NoSQL databases. This course covers MongoDB's document model, collections, and basic queries so you understand how NoSQL databases differ from the relational databases you may already know.",
        "outcomes": [
            "Explain the difference between SQL and NoSQL databases",
            "Understand MongoDB's document and collection structure",
            "Write basic CRUD queries in MongoDB",
            "Describe when a team might choose MongoDB in an interview"
        ],
        "youtube_id": "-56x56UppqQ",
        "video_title": "MongoDB Crash Course",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the MongoDB and NoSQL Databases Basics course, what's next?"
    },
    {
        "slug": "course-vuejs-basics",
        "course_id": "vuejs-basics",
        "title": "Vue.js Programming for Beginners",
        "title_tag": "Free Vue.js Course with Certificate",
        "meta_desc": "Free course on Vue.js fundamentals for beginners: components, directives, and reactivity, with a free certificate on completion.",
        "og_desc": "Learn Vue.js fundamentals: components, directives, and reactivity. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Vue.js is a widely used front-end framework in U.S. job postings alongside React and Angular. This course covers components, directives, and reactivity.",
        "item_desc": "Learn Vue.js fundamentals including components, directives, and reactivity for front-end development roles.",
        "time_label": "~3 hrs",
        "h1_lead": "Learn Vue.js,",
        "h1_grad": "a popular alternative to React and Angular.",
        "lede": "Vue.js shows up regularly in front-end job postings as a lighter-weight alternative to React and Angular. This course walks through components, directives, and Vue's reactivity system so you can read and build real Vue apps.",
        "outcomes": [
            "Build and reuse Vue components",
            "Use Vue directives to control rendering and behavior",
            "Understand how Vue's reactivity system works",
            "Compare Vue to React and Angular confidently in an interview"
        ],
        "youtube_id": "FXpIoQ_rT_c",
        "video_title": "Vue.js Course for Beginners",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Vue.js Programming for Beginners course, what's next?"
    },
    {
        "slug": "course-system-design-fundamentals",
        "course_id": "system-design-fundamentals",
        "title": "System Design Fundamentals",
        "title_tag": "Free System Design Course with Certificate",
        "meta_desc": "Free course introducing system design fundamentals: scalability, load balancing, and caching, with a free certificate on completion.",
        "og_desc": "Learn system design fundamentals: scalability, load balancing, and caching. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "System design questions show up in technical interviews well before senior level. This course covers the core concepts: scalability, load balancing, and caching.",
        "item_desc": "Learn system design fundamentals including scalability, load balancing, and caching for technical interviews.",
        "time_label": "~30 min",
        "h1_lead": "Learn system design,",
        "h1_grad": "the concepts behind modern technical interviews.",
        "lede": "System design questions aren't just for senior engineers anymore; many mid-level technical interviews now touch on scalability basics. This course covers the core concepts employers expect you to recognize: load balancing, caching, and how large systems stay reliable.",
        "outcomes": [
            "Explain what horizontal and vertical scaling mean",
            "Describe how load balancers and caching improve reliability",
            "Recognize common system design building blocks",
            "Talk through a simple system design question in an interview"
        ],
        "youtube_id": "BTjxUS_PylA",
        "video_title": "8 Most Important System Design Concepts You Should Know",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the System Design Fundamentals course, what's next?"
    },
    {
        "slug": "course-negotiating-job-offer-beyond-salary",
        "course_id": "negotiating-job-offer-beyond-salary",
        "title": "Negotiating a Job Offer Beyond Salary",
        "title_tag": "Free Job Offer Negotiation Course with Certificate",
        "meta_desc": "Free course on negotiating a job offer: base salary, sign-on bonus, start date, and other terms candidates often leave on the table.",
        "og_desc": "Learn how to negotiate a job offer beyond just base salary. Free course, free certificate.",
        "category": "Job Search Strategy",
        "card_desc": "Salary isn't the only thing on the table in a job offer. This course covers sign-on bonuses, start dates, and other terms candidates often forget to negotiate.",
        "item_desc": "Learn how to negotiate a full job offer, not just base salary, including bonuses, start dates, and other terms.",
        "time_label": "~15 min",
        "h1_lead": "Negotiate the whole offer,",
        "h1_grad": "not just the base salary number.",
        "lede": "Most candidates focus every negotiation conversation on one number: base salary. This course covers the other parts of an offer that are often just as negotiable, like sign-on bonuses, start date, and title, plus how to raise them without sounding pushy.",
        "outcomes": [
            "Identify which parts of a job offer are commonly negotiable",
            "Prepare a clear, evidence-based case before a negotiation call",
            "Avoid common phrasing mistakes that weaken a counteroffer",
            "Know when to accept, counter, or walk away from an offer"
        ],
        "youtube_id": "e2_HXKNIzaM",
        "video_title": "How to Negotiate a Higher Salary: 3 Evidence-Based Tips!",
        "upload_date": "2024-01-01",
        "cta_h2": "Want feedback on an offer you've already received?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Negotiating a Job Offer Beyond Salary course, what's next?"
    },
    {
        "slug": "course-portfolio-website-job-search",
        "course_id": "portfolio-website-job-search",
        "title": "Building a Personal Portfolio Website",
        "title_tag": "Free Portfolio Website Course with Certificate",
        "meta_desc": "Free course on building a personal portfolio website for job search: structure, content, and what recruiters actually look for.",
        "og_desc": "Learn how to build a personal portfolio website that helps your job search. Free course, free certificate.",
        "category": "Job Search Strategy",
        "card_desc": "A simple portfolio website can set a candidate apart, even outside design and dev roles. This course covers structure, content, and building one from scratch.",
        "item_desc": "Learn how to build a personal portfolio website using HTML, CSS, and JavaScript to support a job search.",
        "time_label": "~2 hrs",
        "h1_lead": "Build a portfolio site,",
        "h1_grad": "a simple edge most candidates skip.",
        "lede": "A clean personal portfolio website gives recruiters a reason to remember you, whether you're in tech, design, or any field where showing your work beats just describing it. This course walks through building one from scratch with HTML, CSS, and JavaScript.",
        "outcomes": [
            "Plan the sections a portfolio website actually needs",
            "Build a simple responsive page with HTML and CSS",
            "Add basic interactivity with JavaScript",
            "Know what to include (and leave out) so recruiters find what matters fast"
        ],
        "youtube_id": "xV7S8BhIeBo",
        "video_title": "Portfolio Website Tutorial – Frontend Development with HTML, CSS, JavaScript",
        "upload_date": "2024-01-01",
        "cta_h2": "Want your portfolio and profile seen by recruiters?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Building a Personal Portfolio Website course, what's next?"
    },
    {
        "slug": "course-emotional-intelligence-at-work",
        "course_id": "emotional-intelligence-at-work",
        "title": "Emotional Intelligence at Work",
        "title_tag": "Free Emotional Intelligence Course with Certificate",
        "meta_desc": "Free course on emotional intelligence at work: self-awareness, empathy, and managing reactions under pressure, with a free certificate.",
        "og_desc": "Learn practical emotional intelligence skills for the workplace. Free course, free certificate.",
        "category": "Career Skills",
        "card_desc": "Emotional intelligence consistently ranks among the top soft skills employers screen for. This course covers self-awareness, empathy, and managing reactions under pressure.",
        "item_desc": "Learn practical emotional intelligence skills including self-awareness and empathy for the workplace.",
        "time_label": "~20 min",
        "h1_lead": "Emotional intelligence,",
        "h1_grad": "the soft skill employers can't stop asking for.",
        "lede": "Emotional intelligence shows up again and again in what employers say separates strong performers from the rest. This course covers the practical side: reading your own reactions, reading others accurately, and staying effective when a conversation gets tense.",
        "outcomes": [
            "Recognize your own emotional triggers before they affect your work",
            "Read social and emotional cues more accurately in meetings",
            "Respond instead of react in a tense workplace conversation",
            "Explain emotional intelligence in concrete terms in an interview"
        ],
        "youtube_id": "auXNnTmhHsk",
        "video_title": "The Power of Emotional Intelligence | Travis Bradberry | TEDxUCIrvine",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to practice this in a mock interview?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Emotional Intelligence at Work course, what's next?"
    },
    {
        "slug": "course-adaptability-resilience-at-work",
        "course_id": "adaptability-resilience-at-work",
        "title": "Adaptability and Resilience at Work",
        "title_tag": "Free Workplace Resilience Course with Certificate",
        "meta_desc": "Free course on adaptability and resilience at work: handling setbacks, change, and uncertainty, with a free certificate on completion.",
        "og_desc": "Learn practical adaptability and resilience skills for the modern workplace. Free course, free certificate.",
        "category": "Career Skills",
        "card_desc": "Layoffs, reorgs, and shifting priorities make adaptability one of the most practical skills to build right now. This course covers handling setbacks and change at work.",
        "item_desc": "Learn practical adaptability and resilience skills for navigating setbacks and change at work.",
        "time_label": "~20 min",
        "h1_lead": "Adaptability and resilience,",
        "h1_grad": "practical skills for an unpredictable job market.",
        "lede": "Layoffs, reorganizations, and shifting priorities are a normal part of the current job market. This course covers the practical side of resilience: how to process a setback, adjust quickly to change, and keep moving instead of freezing up.",
        "outcomes": [
            "Separate a setback from your overall trajectory",
            "Adjust to sudden change at work without losing momentum",
            "Build small habits that make resilience easier over time",
            "Talk about a past setback productively in an interview"
        ],
        "youtube_id": "NWH8N-BvhAw",
        "video_title": "The three secrets of resilient people | Lucy Hone | TEDxChristchurch",
        "upload_date": "2024-01-01",
        "cta_h2": "Dealing with a layoff or setback right now?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Adaptability and Resilience at Work course, what's next?"
    },
    {
        "slug": "course-ceh-certification-overview",
        "course_id": "ceh-certification-overview",
        "title": "Certified Ethical Hacker (CEH) Certification Overview",
        "title_tag": "Free CEH Certification Overview Course with Certificate",
        "meta_desc": "Free overview course on the Certified Ethical Hacker (CEH) certification: what it covers, who it's for, and how to start preparing.",
        "og_desc": "Learn what the CEH certification covers and whether it's worth pursuing. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "CEH is one of the most recognized credentials for cybersecurity and penetration testing roles. This course covers what it tests and who it's for.",
        "item_desc": "Learn what the Certified Ethical Hacker (CEH) certification covers and whether it fits your career path.",
        "time_label": "~25 min",
        "h1_lead": "CEH certification,",
        "h1_grad": "explained before you commit to studying for it.",
        "lede": "The Certified Ethical Hacker (CEH) certification is one of the most recognized entry points into penetration testing and offensive security roles. This course gives an honest overview of what it covers, who it's actually for, and how it compares to other security certifications.",
        "outcomes": [
            "Explain what the CEH certification tests",
            "Understand who CEH is a good fit for versus other security certs",
            "Identify the general exam structure and prerequisites",
            "Decide whether CEH fits your career goals before you start studying"
        ],
        "youtube_id": "pq0DDtN-vWk",
        "video_title": "CEH Course 2026 | Certified Ethical Hacker Certification | Ethical Hacking Course | Simplilearn",
        "upload_date": "2024-01-01",
        "cta_h2": "Want help mapping certifications to a real job plan?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Certified Ethical Hacker (CEH) Certification Overview course, what's next?"
    },
    {
        "slug": "course-six-sigma-certification-overview",
        "course_id": "six-sigma-certification-overview",
        "title": "Six Sigma Certification Overview",
        "title_tag": "Free Six Sigma Certification Overview Course with Certificate",
        "meta_desc": "Free overview course on Six Sigma certification: belt levels, what the methodology covers, and who it's useful for.",
        "og_desc": "Learn what Six Sigma certification covers and whether it's worth pursuing. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "Six Sigma certifications show up in process improvement and operations job postings across many industries, including IT. This course covers the belt levels and what each one involves.",
        "item_desc": "Learn what Six Sigma certification covers, including belt levels, and whether it fits your career path.",
        "time_label": "~30 min",
        "h1_lead": "Six Sigma certification,",
        "h1_grad": "explained before you pick a belt level.",
        "lede": "Six Sigma certifications show up in process improvement, operations, and quality roles across manufacturing, healthcare, and IT. This course explains the belt system (yellow, green, black), what the methodology actually covers, and who tends to benefit most from getting certified.",
        "outcomes": [
            "Explain what Six Sigma methodology is used for",
            "Understand the difference between yellow, green, and black belt levels",
            "Identify industries and roles where Six Sigma is commonly required",
            "Decide which belt level, if any, fits your career goals"
        ],
        "youtube_id": "KfFez57ay6E",
        "video_title": "Six Sigma Full Course in 7 Hours | Six Sigma Green Belt Training | Simplilearn",
        "upload_date": "2024-01-01",
        "cta_h2": "Want help mapping certifications to a real job plan?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Six Sigma Certification Overview course, what's next?"
    },
    {
        "slug": "course-real-estate-careers-101",
        "course_id": "real-estate-careers-101",
        "title": "Real Estate Careers 101",
        "title_tag": "Free Real Estate Careers Course with Certificate",
        "meta_desc": "Free overview course on starting a real estate career: licensing, specializations, and what the first year actually looks like.",
        "og_desc": "Learn how to start a career in real estate, from licensing to specializations. Free course, free certificate.",
        "category": "Industry Career Guides",
        "card_desc": "Real estate offers a flexible entry path with low upfront barriers. This course covers licensing basics, common specializations, and what the first year actually looks like.",
        "item_desc": "Learn the basics of starting a real estate career, including licensing and common specializations.",
        "time_label": "~20 min",
        "h1_lead": "Real estate careers,",
        "h1_grad": "a flexible path with a real learning curve.",
        "lede": "Real estate attracts career-changers because the licensing barrier is relatively low, but the first year is harder than it looks from the outside. This course covers licensing basics, common specializations like residential versus commercial, and what to realistically expect early on.",
        "outcomes": [
            "Understand the general licensing path for real estate agents",
            "Compare common specializations within real estate",
            "Set realistic expectations for income and workload in year one",
            "Identify the skills that transfer in from other careers"
        ],
        "youtube_id": "jjrh3RPTRaE",
        "video_title": "How to Launch Your Real Estate Career",
        "upload_date": "2024-01-01",
        "cta_h2": "Exploring a career change?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Real Estate Careers 101 course, what's next?"
    },
    {
        "slug": "course-pharma-biotech-careers",
        "course_id": "pharma-biotech-careers",
        "title": "Pharmaceutical and Biotech Careers",
        "title_tag": "Free Pharma & Biotech Careers Course with Certificate",
        "meta_desc": "Free overview course on pharmaceutical and biotech careers: major functional areas and non-lab roles outside bench science.",
        "og_desc": "Learn about career paths in pharma and biotech, including non-lab roles. Free course, free certificate.",
        "category": "Industry Career Guides",
        "card_desc": "Pharma and biotech need far more than bench scientists, including IT, data, regulatory, and operations roles. This course maps the major functional areas.",
        "item_desc": "Learn about career paths in pharmaceutical and biotech companies, including roles outside the lab.",
        "time_label": "~20 min",
        "h1_lead": "Pharma & biotech careers,",
        "h1_grad": "more roles than just lab scientists.",
        "lede": "Pharmaceutical and biotech companies run on far more than bench scientists: IT, data, regulatory affairs, quality, and operations teams keep everything moving. This course maps the major functional areas so you can see where your existing skills might fit.",
        "outcomes": [
            "Identify the major functional areas inside a pharma or biotech company",
            "Understand which roles require a science background and which don't",
            "Recognize common entry points for career-changers",
            "Explain how a non-lab background still adds value in this industry"
        ],
        "youtube_id": "NxAjCovfedg",
        "video_title": "Career Paths in Biotech & Pharma",
        "upload_date": "2024-01-01",
        "cta_h2": "Exploring a career change?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Pharmaceutical and Biotech Careers course, what's next?"
    },
]

def main():
    with open(REG) as f:
        reg = json.load(f)
    existing_slugs = {c["slug"] for c in reg}
    existing_yt = {c["youtube_id"] for c in reg}
    for c in NEW:
        if c["slug"] in existing_slugs:
            raise SystemExit(f"duplicate slug: {c['slug']}")
        if c["youtube_id"] in existing_yt:
            raise SystemExit(f"duplicate youtube_id: {c['youtube_id']}")
    reg.extend(NEW)
    with open(REG, "w") as f:
        json.dump(reg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Appended {len(NEW)} new courses. Registry now has {len(reg)} entries.")
    for c in NEW:
        print(" -", c["slug"], "|", c["category"], "|", c["youtube_id"])

if __name__ == "__main__":
    main()
