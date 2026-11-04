#!/usr/bin/env python3
"""One-off: append this week's (2026-11-04) new course entries to courses_registry.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "scripts", "courses_registry.json")

NEW = [
    {
        "slug": "course-flutter-dart-basics",
        "course_id": "flutter-dart-basics",
        "title": "Flutter and Dart for Beginners",
        "title_tag": "Free Flutter Course with Certificate",
        "meta_desc": "Free course on Flutter and Dart fundamentals for beginners: building cross-platform iOS and Android apps from one codebase, with a free certificate.",
        "og_desc": "Learn Flutter and Dart fundamentals for building iOS and Android apps. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Flutter lets one Dart codebase ship to iOS, Android, and the web, and it shows up constantly in mobile developer job postings. This course covers Dart basics and building your first Flutter app.",
        "item_desc": "Learn Flutter and Dart fundamentals for building cross-platform mobile apps.",
        "time_label": "~3.5 hrs",
        "h1_lead": "Learn Flutter,",
        "h1_grad": "and ship iOS and Android apps from one codebase.",
        "lede": "Flutter is Google's toolkit for building iOS, Android, and web apps from a single Dart codebase, and it's one of the most requested skills in mobile developer job postings. This course walks through Dart fundamentals and building your first cross-platform Flutter app.",
        "outcomes": [
            "Write and run basic Dart programs",
            "Build a simple Flutter app with widgets and layouts",
            "Understand how Flutter targets iOS, Android, and web from one codebase",
            "Explain why companies choose Flutter for mobile development in an interview"
        ],
        "youtube_id": "pTJJsmejUOQ",
        "video_title": "Flutter Course - Full Tutorial for Beginners (Build iOS and Android Apps)",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Flutter and Dart for Beginners course, what's next?"
    },
    {
        "slug": "course-nextjs-basics",
        "course_id": "nextjs-basics",
        "title": "Next.js for Beginners",
        "title_tag": "Free Next.js Course with Certificate",
        "meta_desc": "Free course on Next.js fundamentals for beginners: routing, server rendering, and building a full-stack React app, with a free certificate.",
        "og_desc": "Learn Next.js fundamentals: routing, rendering, and full-stack React apps. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Next.js is the most requested React framework in frontend job postings. This course covers routing, server rendering, and building a full-stack app.",
        "item_desc": "Learn Next.js fundamentals including routing, server rendering, and full-stack React app basics.",
        "time_label": "~4 hrs",
        "h1_lead": "Learn Next.js,",
        "h1_grad": "the React framework behind most frontend job postings.",
        "lede": "Next.js has become the default way companies build production React apps, adding routing, server rendering, and full-stack features on top of plain React. This course walks through the fundamentals so you understand how a modern Next.js app fits together.",
        "outcomes": [
            "Set up and structure a Next.js project",
            "Use file-based routing and server-side rendering",
            "Fetch and display data in a Next.js app",
            "Explain why companies choose Next.js over plain React in an interview"
        ],
        "youtube_id": "1WmNXEVia8I",
        "video_title": "Next.js for Beginners - Full Course",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Next.js for Beginners course, what's next?"
    },
    {
        "slug": "course-spring-boot-basics",
        "course_id": "spring-boot-basics",
        "title": "Spring Boot for Java Web Applications",
        "title_tag": "Free Spring Boot Course with Certificate",
        "meta_desc": "Free course on Spring Boot fundamentals for beginners: building Java web applications and REST APIs, with a free certificate on completion.",
        "og_desc": "Learn Spring Boot fundamentals for building Java web apps and REST APIs. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Spring Boot is the standard framework behind most enterprise Java job postings. This course covers building a Java web application and a REST API from scratch.",
        "item_desc": "Learn Spring Boot fundamentals for building Java web applications and REST APIs.",
        "time_label": "~5 hrs",
        "h1_lead": "Learn Spring Boot,",
        "h1_grad": "the framework behind most enterprise Java jobs.",
        "lede": "Spring Boot is the framework most companies use to build Java web applications and APIs, and it shows up constantly in backend and enterprise job postings. This course walks through building a web application and a REST API with Spring Boot.",
        "outcomes": [
            "Set up a Spring Boot project and understand its structure",
            "Build a REST API with Spring Boot",
            "Connect a Spring Boot app to a database",
            "Explain how Spring Boot fits into enterprise Java development in an interview"
        ],
        "youtube_id": "31KTdfRH6nY",
        "video_title": "Building web applications in Java with Spring Boot 3 – Tutorial",
        "upload_date": "2024-03-18",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Spring Boot for Java Web Applications course, what's next?"
    },
    {
        "slug": "course-apache-kafka-basics",
        "course_id": "apache-kafka-basics",
        "title": "Apache Kafka Fundamentals",
        "title_tag": "Free Apache Kafka Course with Certificate",
        "meta_desc": "Free beginner course on Apache Kafka fundamentals: topics, producers, consumers, and real-time data streaming, with a free certificate.",
        "og_desc": "Learn Apache Kafka fundamentals: topics, producers, and consumers. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Kafka powers real-time data pipelines at most large tech companies and shows up often in data engineering job postings. This course covers topics, producers, and consumers.",
        "item_desc": "Learn Apache Kafka fundamentals including topics, producers, and consumers for real-time data streaming roles.",
        "time_label": "~4 hrs",
        "h1_lead": "Learn Apache Kafka,",
        "h1_grad": "the backbone of real-time data pipelines.",
        "lede": "Apache Kafka is the standard tool for moving real-time data between systems at scale, and it shows up often in data engineering and backend job postings. This course introduces Kafka's core concepts: topics, producers, and consumers.",
        "outcomes": [
            "Explain what Kafka is and why companies use it for streaming data",
            "Understand topics, producers, and consumers",
            "Set up a basic Kafka producer and consumer",
            "Describe common Kafka use cases in an interview"
        ],
        "youtube_id": "MsnHKOyTN_0",
        "video_title": "Apache Kafka Complete Course - Build Real-Time Data Pipelines (Full Tutorial for Beginners)",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Apache Kafka Fundamentals course, what's next?"
    },
    {
        "slug": "course-windows-server-administration",
        "course_id": "windows-server-administration",
        "title": "Windows Server Administration Basics",
        "title_tag": "Free Windows Server Admin Course with Certificate",
        "meta_desc": "Free beginner course on Windows Server administration: Active Directory, user management, and core server roles, with a free certificate.",
        "og_desc": "Learn Windows Server administration basics: Active Directory and core server roles. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Windows Server administration still shows up constantly in IT support and sysadmin job postings. This course covers Active Directory, user management, and core server roles.",
        "item_desc": "Learn Windows Server administration basics including Active Directory and core server roles for IT support and sysadmin roles.",
        "time_label": "~6 hrs",
        "h1_lead": "Learn Windows Server administration,",
        "h1_grad": "a core skill in IT support job postings.",
        "lede": "Most mid-size and large companies still run Windows Server somewhere in their infrastructure, and administering it is a core skill in IT support, help desk, and sysadmin job postings. This course covers Active Directory, user management, and core server roles.",
        "outcomes": [
            "Install and configure core Windows Server roles",
            "Manage users and groups with Active Directory",
            "Understand basic network and file-sharing configuration",
            "Explain common Windows Server admin tasks in an interview"
        ],
        "youtube_id": "r6EDUTU0ppo",
        "video_title": "Complete Windows Server Administration Course",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Windows Server Administration Basics course, what's next?"
    },
    {
        "slug": "course-salesforce-admin-basics",
        "course_id": "salesforce-admin-basics",
        "title": "Salesforce Administrator Basics",
        "title_tag": "Free Salesforce Admin Course with Certificate",
        "meta_desc": "Free beginner course on Salesforce administration: objects, fields, security, and workflow automation, with a free certificate on completion.",
        "og_desc": "Learn Salesforce administration basics: objects, fields, and automation. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Salesforce Administrator is one of the most in-demand non-coding IT roles. This course covers objects, fields, security settings, and basic workflow automation.",
        "item_desc": "Learn Salesforce administration basics including objects, fields, security, and workflow automation.",
        "time_label": "~5 hrs",
        "h1_lead": "Learn Salesforce administration,",
        "h1_grad": "one of the most in-demand non-coding IT roles.",
        "lede": "Salesforce Administrator roles are consistently in demand and don't require a coding background, making Salesforce one of the most accessible entry points into enterprise IT. This course covers objects, fields, security settings, and basic workflow automation.",
        "outcomes": [
            "Navigate the Salesforce platform and set up objects and fields",
            "Manage users, profiles, and basic security settings",
            "Build a simple workflow or automation rule",
            "Explain core Salesforce admin concepts in an interview"
        ],
        "youtube_id": "qcTDDMYWm8E",
        "video_title": "Salesforce Full Course 2025 | Salesforce Course For Beginners | Salesforce Training | Intellipaat",
        "upload_date": "2024-12-27",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Salesforce Administrator Basics course, what's next?"
    },
    {
        "slug": "course-thank-you-email-interview",
        "course_id": "thank-you-email-interview",
        "title": "Writing a Thank-You Email After an Interview",
        "title_tag": "Free Interview Follow-Up Course with Certificate",
        "meta_desc": "Free course on writing a strong thank-you email after a job interview: timing, tone, and what to include, with a free certificate on completion.",
        "og_desc": "Learn how to write a thank-you email after an interview that stands out. Free course, free certificate.",
        "category": "Job Search Strategy",
        "card_desc": "A good thank-you email can keep you top of mind after an interview, and a bad one can hurt you. This course covers timing, tone, and exactly what to include.",
        "item_desc": "Learn how to write an effective thank-you email after a job interview, including timing and tone.",
        "time_label": "~30 min",
        "h1_lead": "Write a thank-you email,",
        "h1_grad": "that actually helps you get the offer.",
        "lede": "Most candidates either skip the post-interview thank-you email or send a generic one that adds nothing. This short course covers when to send it, what tone to use, and what details make it memorable to a hiring manager.",
        "outcomes": [
            "Understand why a thank-you email matters to hiring managers",
            "Know the right timing and tone for a follow-up email",
            "Write a thank-you email that references specifics from the interview",
            "Avoid the most common thank-you email mistakes"
        ],
        "youtube_id": "jYH0UBvf55E",
        "video_title": "Thank You Email After Interview",
        "upload_date": "2024-01-01",
        "cta_h2": "Want feedback on your own follow-up emails?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Writing a Thank-You Email After an Interview course, what's next?"
    },
    {
        "slug": "course-finding-a-mentor",
        "course_id": "finding-a-mentor",
        "title": "Finding a Mentor at Work",
        "title_tag": "Free Workplace Mentorship Course with Certificate",
        "meta_desc": "Free course on finding and working with a workplace mentor: where to look, how to ask, and how to make the relationship useful, with a free certificate.",
        "og_desc": "Learn how to find and work with a mentor at work. Free course, free certificate.",
        "category": "Career Skills",
        "card_desc": "A good mentor can speed up your career more than almost anything else, but most people never ask for one. This course covers where to look and how to approach someone.",
        "item_desc": "Learn how to find a workplace mentor, where to look, and how to build a useful mentoring relationship.",
        "time_label": "~30 min",
        "h1_lead": "Find a mentor,",
        "h1_grad": "and actually make the relationship useful.",
        "lede": "Mentorship is one of the most reliable ways to accelerate a career, but most people don't know where to find a mentor or how to ask. This course covers where to look inside and outside your company, how to approach someone, and how to keep the relationship valuable for both sides.",
        "outcomes": [
            "Identify where to look for a mentor inside and outside your company",
            "Know how to approach someone and ask for mentorship",
            "Set clear goals for a mentoring relationship",
            "Keep a mentoring relationship useful over time"
        ],
        "youtube_id": "SItt_8r6j1s",
        "video_title": "How to Find a Mentor [4 Places to Start]",
        "upload_date": "2024-01-01",
        "cta_h2": "Want help building your professional network?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Finding a Mentor at Work course, what's next?"
    },
    {
        "slug": "course-azure-administrator-az104-overview",
        "course_id": "azure-administrator-az104-overview",
        "title": "Microsoft Azure Administrator (AZ-104) Certification Overview",
        "title_tag": "Free AZ-104 Certification Overview with Certificate",
        "meta_desc": "Free overview of the Microsoft Azure Administrator (AZ-104) certification: what it covers, who it's for, and how to prepare, with a free certificate.",
        "og_desc": "Understand what the AZ-104 Azure Administrator certification covers and how to prepare. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "AZ-104 is one of the most requested Azure certifications in cloud job postings. This overview covers what it tests, who it's for, and how to start preparing.",
        "item_desc": "Understand what the Microsoft Azure Administrator (AZ-104) certification covers and how to prepare for it.",
        "time_label": "~1 hr",
        "h1_lead": "Understand AZ-104,",
        "h1_grad": "the Azure Administrator certification employers ask for.",
        "lede": "The AZ-104 Microsoft Azure Administrator certification confirms you can manage identities, storage, networking, and compute in Azure, and it's one of the most commonly requested cloud certifications in IT job postings. This overview explains what it covers and how to approach preparing for it.",
        "outcomes": [
            "Understand what the AZ-104 exam covers",
            "Know who the certification is designed for",
            "Identify the Azure skills tested: identity, storage, networking, and compute",
            "Know how to start preparing for the exam"
        ],
        "youtube_id": "urAOSAsaXUE",
        "video_title": "Microsoft Azure Administrator (AZ-104) Full Crash Course | Part 1",
        "upload_date": "2024-01-01",
        "cta_h2": "Want help building toward a cloud career?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This overview introduces the exam. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the AZ-104 Certification Overview course, what's next?"
    },
    {
        "slug": "course-google-it-support-certificate-overview",
        "course_id": "google-it-support-certificate-overview",
        "title": "Google IT Support Professional Certificate Overview",
        "title_tag": "Free Google IT Support Certificate Overview",
        "meta_desc": "Free overview of the Google IT Support Professional Certificate: what it covers, who it's for, and how it can help you break into IT, with a free certificate.",
        "og_desc": "Understand what the Google IT Support Professional Certificate covers and who it's for. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "The Google IT Support Professional Certificate is one of the most common entry points into IT help desk roles. This overview covers what it teaches and who it's for.",
        "item_desc": "Understand what the Google IT Support Professional Certificate covers and how it helps with entry-level IT roles.",
        "time_label": "~1 hr",
        "h1_lead": "Understand the Google IT Support Certificate,",
        "h1_grad": "a common path into entry-level IT roles.",
        "lede": "The Google IT Support Professional Certificate is one of the most widely recognized entry points into help desk and IT support careers, covering troubleshooting, networking, operating systems, and customer service. This overview explains what the program teaches and who it's a good fit for.",
        "outcomes": [
            "Understand what the Google IT Support certificate covers",
            "Know who the program is designed for",
            "Identify the core IT support skills it teaches",
            "Know what roles this certificate typically leads to"
        ],
        "youtube_id": "R5MbQq-W1PQ",
        "video_title": "Google IT Support Professional Certificate in 2023",
        "upload_date": "2023-01-01",
        "cta_h2": "Want help turning a certificate into a job?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This overview introduces the program. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Google IT Support Professional Certificate Overview course, what's next?"
    },
    {
        "slug": "course-marketing-advertising-careers",
        "course_id": "marketing-advertising-careers",
        "title": "Marketing and Advertising Careers",
        "title_tag": "Free Marketing Careers Course with Certificate",
        "meta_desc": "Free overview of marketing and advertising careers: common entry-level roles, day-to-day work, and how to break in, with a free certificate.",
        "og_desc": "Learn about common marketing and advertising career paths and roles. Free course, free certificate.",
        "category": "Industry Career Guides",
        "card_desc": "Marketing and advertising hire across a wide range of entry-level roles, from content to analytics to campaign management. This guide covers what the day-to-day actually looks like.",
        "item_desc": "Learn about common marketing and advertising career paths, roles, and how to break into the industry.",
        "time_label": "~30 min",
        "h1_lead": "Explore marketing careers,",
        "h1_grad": "and what the day-to-day actually looks like.",
        "lede": "Marketing and advertising cover a wide range of roles, from content and social media to campaign management and analytics, and most don't require a specialized technical background to start. This guide walks through what a typical marketing role looks like day to day and where entry-level candidates usually start.",
        "outcomes": [
            "Understand the range of roles inside marketing and advertising",
            "See what a typical day looks like in a marketing role",
            "Identify common entry points for candidates without marketing experience",
            "Know which skills matter most for breaking into the field"
        ],
        "youtube_id": "wymUxwWJKyE",
        "video_title": "Day in the Life of a Marketing Manager | Inside a Marketing Career",
        "upload_date": "2024-01-01",
        "cta_h2": "Want help positioning yourself for a marketing role?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This guide covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Marketing and Advertising Careers course, what's next?"
    },
]

with open(REG, encoding="utf-8") as f:
    registry = json.load(f)

existing_slugs = {c["slug"] for c in registry}
existing_ids = {c["youtube_id"] for c in registry}
for c in NEW:
    assert c["slug"] not in existing_slugs, f"duplicate slug {c['slug']}"
    assert c["youtube_id"] not in existing_ids, f"duplicate youtube_id {c['youtube_id']}"

registry.extend(NEW)

with open(REG, "w", encoding="utf-8") as f:
    json.dump(registry, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Appended {len(NEW)} new courses. Registry now has {len(registry)} entries.")
