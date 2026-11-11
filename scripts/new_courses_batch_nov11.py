#!/usr/bin/env python3
"""One-off: append this week's (2026-11-11) new course entries to courses_registry.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "scripts", "courses_registry.json")

NEW = [
    {
        "slug": "course-pyspark-big-data-basics",
        "course_id": "pyspark-big-data-basics",
        "title": "PySpark and Big Data Processing Basics",
        "title_tag": "Free PySpark Course with Certificate",
        "meta_desc": "Free course on PySpark fundamentals for beginners: distributed data processing, DataFrames, and big data basics, with a free certificate on completion.",
        "og_desc": "Learn PySpark fundamentals for big data processing and DataFrames. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Apache Spark is the standard engine behind large-scale data processing, and PySpark is how most data engineers use it. This course covers DataFrames, transformations, and running real big data jobs.",
        "item_desc": "Learn PySpark fundamentals for distributed data processing and big data basics.",
        "time_label": "~2.5 hrs",
        "h1_lead": "Learn PySpark,",
        "h1_grad": "the standard tool for processing big data at scale.",
        "lede": "Apache Spark powers large-scale data processing at most companies with real data volume, and PySpark is how data engineers and analysts drive it with Python. This course walks through DataFrames, transformations, and running real distributed jobs.",
        "outcomes": [
            "Set up a PySpark environment and load data into DataFrames",
            "Apply transformations and aggregations to large datasets",
            "Understand how Spark distributes work across a cluster",
            "Explain why companies use Spark for big data in an interview"
        ],
        "youtube_id": "_C8kWso4ne4",
        "video_title": "PySpark Tutorial",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the PySpark and Big Data Processing Basics course, what's next?"
    },
    {
        "slug": "course-elasticsearch-basics",
        "course_id": "elasticsearch-basics",
        "title": "Elasticsearch for Beginners",
        "title_tag": "Free Elasticsearch Course with Certificate",
        "meta_desc": "Free course on Elasticsearch fundamentals for beginners: indexing, searching, and building a search engine, with a free certificate on completion.",
        "og_desc": "Learn Elasticsearch fundamentals for indexing and search. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Elasticsearch is the engine behind search and log analysis at thousands of companies. This course covers indexing data, writing queries, and building a basic search feature.",
        "item_desc": "Learn Elasticsearch fundamentals for indexing, searching, and log analysis.",
        "time_label": "~3 hrs",
        "h1_lead": "Learn Elasticsearch,",
        "h1_grad": "the search and log-analysis engine companies run on.",
        "lede": "Elasticsearch shows up behind the scenes in site search, log analysis, and monitoring dashboards at companies of every size. This course covers indexing data, writing queries, and building a basic search feature from the fundamentals up.",
        "outcomes": [
            "Index documents and understand how Elasticsearch stores data",
            "Write search queries and filters",
            "Understand how Elasticsearch fits into a logging or search stack",
            "Explain what Elasticsearch is used for in an interview"
        ],
        "youtube_id": "a4HBKEda_F8",
        "video_title": "Elasticsearch Course for Beginners",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Elasticsearch for Beginners course, what's next?"
    },
    {
        "slug": "course-ansible-basics",
        "course_id": "ansible-basics",
        "title": "Ansible and IT Automation Basics",
        "title_tag": "Free Ansible Course with Certificate",
        "meta_desc": "Free course on Ansible fundamentals for beginners: playbooks, inventories, and automating IT infrastructure tasks, with a free certificate on completion.",
        "og_desc": "Learn Ansible fundamentals for IT automation and playbooks. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Ansible is one of the most common tools for automating server setup and configuration without agents. This course covers playbooks, inventories, and running your first automation tasks.",
        "item_desc": "Learn Ansible fundamentals for IT automation, playbooks, and configuration management.",
        "time_label": "~2 hrs",
        "h1_lead": "Learn Ansible,",
        "h1_grad": "the tool IT teams use to automate server setup.",
        "lede": "Ansible lets IT and DevOps teams automate server configuration and deployment tasks without installing agents on every machine, and it shows up constantly in sysadmin and DevOps job postings. This course covers playbooks, inventories, and running your first automated tasks.",
        "outcomes": [
            "Understand what Ansible is and how it differs from other automation tools",
            "Write a basic Ansible playbook and inventory file",
            "Automate a simple server configuration task",
            "Explain why companies use Ansible for IT automation in an interview"
        ],
        "youtube_id": "YI48bKykx7k",
        "video_title": "Ansible Tutorial for Beginners | What is Ansible | Intellipaat",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Ansible and IT Automation Basics course, what's next?"
    },
    {
        "slug": "course-prometheus-grafana-monitoring",
        "course_id": "prometheus-grafana-monitoring",
        "title": "Prometheus and Grafana Monitoring Basics",
        "title_tag": "Free Prometheus & Grafana Course with Certificate",
        "meta_desc": "Free course on Prometheus and Grafana fundamentals for beginners: metrics collection, dashboards, and monitoring systems, with a free certificate on completion.",
        "og_desc": "Learn Prometheus and Grafana fundamentals for monitoring and dashboards. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Prometheus and Grafana are the standard open-source pair for monitoring servers and applications. This course covers collecting metrics, writing queries, and building dashboards.",
        "item_desc": "Learn Prometheus and Grafana fundamentals for metrics collection and monitoring dashboards.",
        "time_label": "~3 hrs",
        "h1_lead": "Learn Prometheus and Grafana,",
        "h1_grad": "the standard pair for monitoring systems in production.",
        "lede": "Most companies running servers or containers in production rely on Prometheus to collect metrics and Grafana to visualize them, and both show up constantly in DevOps and SRE job postings. This course covers collecting metrics, writing basic queries, and building a monitoring dashboard.",
        "outcomes": [
            "Understand how Prometheus collects and stores metrics",
            "Write basic PromQL queries",
            "Build a Grafana dashboard from live metrics",
            "Explain how monitoring fits into a production system in an interview"
        ],
        "youtube_id": "zZcxdWJ_tRc",
        "video_title": "Prometheus FULL Course: Docker/K8s, PromQL, Grafana & MORE!",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Prometheus and Grafana Monitoring Basics course, what's next?"
    },
    {
        "slug": "course-snowflake-basics",
        "course_id": "snowflake-basics",
        "title": "Snowflake and Cloud Data Warehousing Basics",
        "title_tag": "Free Snowflake Course with Certificate",
        "meta_desc": "Free course on Snowflake fundamentals for beginners: cloud data warehousing, loading data, and running queries, with a free certificate on completion.",
        "og_desc": "Learn Snowflake fundamentals for cloud data warehousing. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Snowflake is one of the most widely adopted cloud data warehouses in enterprise data teams. This course covers loading data, running queries, and understanding how Snowflake's architecture works.",
        "item_desc": "Learn Snowflake fundamentals for cloud data warehousing and SQL-based analytics.",
        "time_label": "~1 hr",
        "h1_lead": "Learn Snowflake,",
        "h1_grad": "the cloud data warehouse behind modern analytics teams.",
        "lede": "Snowflake has become one of the default cloud data warehouses for companies running analytics at scale, and it shows up constantly in data analyst and data engineer job postings. This course covers loading data, running SQL queries, and understanding Snowflake's architecture.",
        "outcomes": [
            "Understand how Snowflake separates storage and compute",
            "Load data into Snowflake and run SQL queries",
            "Understand virtual warehouses and basic cost concepts",
            "Explain why companies choose Snowflake for analytics in an interview"
        ],
        "youtube_id": "nV1n06MAYM0",
        "video_title": "Snowflake Tutorial for Beginners [FULL COURSE in 50 Minutes]",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Snowflake and Cloud Data Warehousing Basics course, what's next?"
    },
    {
        "slug": "course-microservices-fastapi-basics",
        "course_id": "microservices-fastapi-basics",
        "title": "Microservices Architecture with FastAPI Basics",
        "title_tag": "Free Microservices Course with Certificate",
        "meta_desc": "Free course on microservices architecture fundamentals using FastAPI: service design, communication, and deployment basics, with a free certificate.",
        "og_desc": "Learn microservices architecture fundamentals with FastAPI. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Most backend job postings now expect some familiarity with microservices. This course uses FastAPI to show how independent services are designed, built, and connected.",
        "item_desc": "Learn microservices architecture fundamentals including service design and communication.",
        "time_label": "~3.5 hrs",
        "h1_lead": "Learn Microservices,",
        "h1_grad": "the architecture behind most modern backend systems.",
        "lede": "Microservices architecture has become the default way larger companies structure backend systems, breaking one big application into independent services that communicate over the network. This course uses FastAPI to build and connect real microservices from the ground up.",
        "outcomes": [
            "Understand what a microservice is and why companies adopt the pattern",
            "Build an independent service with FastAPI",
            "Connect services together over HTTP",
            "Explain microservices trade-offs versus a monolith in an interview"
        ],
        "youtube_id": "Cy9fAvsXGZA",
        "video_title": "Microservices with FastAPI – Full Course",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Microservices Architecture with FastAPI Basics course, what's next?"
    },
    {
        "slug": "course-cloud-security-fundamentals",
        "course_id": "cloud-security-fundamentals",
        "title": "Cloud Security Fundamentals",
        "title_tag": "Free Cloud Security Course with Certificate",
        "meta_desc": "Free course on cloud security fundamentals for beginners: identity and access management, data protection, and common cloud threats, with a free certificate.",
        "og_desc": "Learn cloud security fundamentals: IAM, data protection, and common threats. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "As companies move workloads to the cloud, cloud security has become one of the fastest-growing areas in IT hiring. This course covers identity and access management, data protection, and common cloud threats.",
        "item_desc": "Learn cloud security fundamentals including IAM, data protection, and common cloud threats.",
        "time_label": "~3 hrs",
        "h1_lead": "Learn Cloud Security,",
        "h1_grad": "one of the fastest-growing areas in IT hiring.",
        "lede": "As more companies move infrastructure to the cloud, securing it has become a distinct and fast-growing specialty inside cybersecurity. This course covers identity and access management, data protection, and the most common cloud security threats and misconfigurations.",
        "outcomes": [
            "Understand core cloud security concepts and the shared responsibility model",
            "Explain identity and access management (IAM) basics",
            "Recognize common cloud misconfigurations and threats",
            "Discuss cloud security fundamentals in a job interview"
        ],
        "youtube_id": "Ijkvx1u0w6o",
        "video_title": "Cloud Security Full Course | Cloud Security Fundamentals | Cloud Security Training | Intellipaat",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Cloud Security Fundamentals course, what's next?"
    },
    {
        "slug": "course-ux-ui-design-career-path",
        "course_id": "ux-ui-design-career-path",
        "title": "How to Become a UX/UI Designer",
        "title_tag": "Free UX/UI Design Career Course with Certificate",
        "meta_desc": "Free course on the UX/UI design career path for beginners: skills, tools, and portfolio basics to break into design, with a free certificate on completion.",
        "og_desc": "Learn the UX/UI design career path: skills, tools, and how to get started. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "UX/UI design is one of the more accessible ways into tech without a traditional CS background. This course covers the core skills, tools, and portfolio steps to start building toward the role.",
        "item_desc": "Learn the UX/UI design career path including core skills, tools, and portfolio basics.",
        "time_label": "~45 min",
        "h1_lead": "Learn the UX/UI design path,",
        "h1_grad": "one of the most approachable ways into tech.",
        "lede": "UX/UI design hires for problem-solving and portfolio quality as much as formal credentials, which makes it one of the more approachable entry points into tech. This course walks through the core skills, common tools, and the portfolio work that actually gets candidates interviews.",
        "outcomes": [
            "Understand the difference between UX and UI design",
            "Identify the core tools and skills UX/UI roles expect",
            "Know what a hiring-ready design portfolio needs to include",
            "Describe the UX/UI design career path in an interview"
        ],
        "youtube_id": "eNpzITfKDxs",
        "video_title": "How To Become A UI UX Designer | UI UX Designer Career Path In 2022 | UI UX Designer | Intellipaat",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the How to Become a UX/UI Designer course, what's next?"
    },
    {
        "slug": "course-data-science-career-path",
        "course_id": "data-science-career-path",
        "title": "How to Become a Data Scientist",
        "title_tag": "Free Data Science Career Course with Certificate",
        "meta_desc": "Free course on the data scientist career path for beginners: skills, tools, and roadmap to break into data science, with a free certificate on completion.",
        "og_desc": "Learn the data scientist career path: skills, tools, and roadmap. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Data science hiring rewards a clear roadmap more than any single credential. This course covers the core skills, tools, and realistic steps to start building toward a data scientist role.",
        "item_desc": "Learn the data scientist career path including core skills, tools, and a realistic roadmap.",
        "time_label": "~40 min",
        "h1_lead": "Learn the data scientist roadmap,",
        "h1_grad": "the skills and steps hiring managers actually look for.",
        "lede": "Data science is one of the most searched career paths in tech, but the roadmap is often confusing. This course breaks down the core skills, the tools employers actually expect, and a realistic path for someone starting from scratch.",
        "outcomes": [
            "Understand what a data scientist actually does day to day",
            "Identify the core skills and tools the role expects (statistics, Python, SQL)",
            "Know how to build a portfolio that demonstrates those skills",
            "Describe the data scientist career path in an interview"
        ],
        "youtube_id": "drR8bH4-itM",
        "video_title": "How To Become A Data Scientist | Data Scientist Roadmap | Data Science | Intellipaat",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the How to Become a Data Scientist course, what's next?"
    },
    {
        "slug": "course-cka-certification-overview",
        "course_id": "cka-certification-overview",
        "title": "Certified Kubernetes Administrator (CKA) Certification Overview",
        "title_tag": "Free CKA Certification Overview with Certificate",
        "meta_desc": "Free overview of the Certified Kubernetes Administrator (CKA) certification: exam format, topics covered, and how to prepare, with a free certificate.",
        "og_desc": "Overview of the CKA certification: exam format, topics, and prep. Free course, free certificate.",
        "category": "Certifications Overview",
        "card_desc": "The CKA is one of the most respected hands-on certifications in cloud infrastructure. This overview covers the exam format, what it actually tests, and how to prepare.",
        "item_desc": "Overview of the Certified Kubernetes Administrator (CKA) exam format and preparation.",
        "time_label": "~20 min",
        "h1_lead": "Understand the CKA certification,",
        "h1_grad": "before you commit time and money to it.",
        "lede": "The Certified Kubernetes Administrator exam is a hands-on, performance-based test that carries real weight in DevOps and platform engineering hiring. This overview walks through the exam format, the topics it covers, and what a realistic prep plan looks like, so you know exactly what you're signing up for.",
        "outcomes": [
            "Understand the CKA exam format and how it differs from multiple-choice certs",
            "Know the main topic areas the exam covers",
            "Understand roughly how much hands-on practice it takes to be ready",
            "Decide whether the CKA fits your career goals"
        ],
        "youtube_id": "l57xKN6OBhY",
        "video_title": "Kubernetes Course – Certified Kubernetes Administrator Exam Preparation (2026 Update)",
        "upload_date": "2026-02-10",
        "cta_h2": "Want to go from overview to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This overview covers what to expect. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the CKA Certification Overview course, what's next?"
    },
    {
        "slug": "course-first-90-days-new-job",
        "course_id": "first-90-days-new-job",
        "title": "Succeeding in Your First 90 Days at a New Job",
        "title_tag": "Free First 90 Days at Work Course with Certificate",
        "meta_desc": "Free course on succeeding in your first 90 days at a new job: onboarding, building relationships, and early wins, with a free certificate on completion.",
        "og_desc": "Learn how to succeed in your first 90 days at a new job. Free course, free certificate.",
        "category": "Career Skills",
        "card_desc": "The first 90 days at a new job often decide how the rest of your tenure goes. This course covers a practical onboarding plan: building relationships, setting expectations, and landing early wins.",
        "item_desc": "Learn how to plan and succeed through your first 90 days at a new job.",
        "time_label": "~20 min",
        "h1_lead": "Master your first 90 days,",
        "h1_grad": "the window that shapes how the rest of the job goes.",
        "lede": "Most new hires are judged, fairly or not, on how they handle their first 90 days: whether they built the right relationships, understood what their manager actually expects, and delivered a few visible early wins. This course walks through a practical, realistic plan for that window.",
        "outcomes": [
            "Set clear expectations with your manager in the first weeks",
            "Build relationships with key coworkers and stakeholders early",
            "Identify and deliver realistic early wins",
            "Avoid the most common first-90-days mistakes"
        ],
        "youtube_id": "KcTI98JWLwE",
        "video_title": "Starting a New Job? Here's a 90-Day Plan from Harvard",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more support once you're hired?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Succeeding in Your First 90 Days at a New Job course, what's next?"
    },
    {
        "slug": "course-video-interview-tips",
        "course_id": "video-interview-tips",
        "title": "Acing the Video Job Interview",
        "title_tag": "Free Video Interview Tips Course with Certificate",
        "meta_desc": "Free course on acing the video job interview: setup, body language, and common mistakes to avoid, with a free certificate on completion.",
        "og_desc": "Learn how to ace a video job interview: setup, body language, and mistakes to avoid. Free course, free certificate.",
        "category": "Job Search Strategy",
        "card_desc": "Most first-round interviews now happen over video, and the format has its own failure points. This course covers setup, body language, and the mistakes that quietly cost candidates offers.",
        "item_desc": "Learn how to prepare for and succeed in a video job interview.",
        "time_label": "~15 min",
        "h1_lead": "Master the video interview,",
        "h1_grad": "the format most first-round interviews now use.",
        "lede": "Video interviews have their own rules: lighting, eye contact with a camera instead of a person, and technical setup all shape a hiring manager's first impression before you say a word. This course covers the practical setup and delivery habits that make a video interview land as well as an in-person one.",
        "outcomes": [
            "Set up lighting, camera angle, and background correctly",
            "Maintain natural eye contact and body language on camera",
            "Handle common technical interview-call mistakes before they happen",
            "Answer questions with the same confidence as an in-person interview"
        ],
        "youtube_id": "HG68Ymazo18",
        "video_title": "Top Interview Tips: Common Questions, Nonverbal Communication & More | Indeed",
        "upload_date": "2024-01-01",
        "cta_h2": "Want more help landing the offer?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Acing the Video Job Interview course, what's next?"
    },
]

with open(REG) as f:
    registry = json.load(f)

existing_slugs = {c["slug"] for c in registry}
for c in NEW:
    if c["slug"] in existing_slugs:
        raise SystemExit(f"Duplicate slug, aborting: {c['slug']}")

registry.extend(NEW)

with open(REG, "w") as f:
    json.dump(registry, f, indent=2)
    f.write("\n")

print(f"Appended {len(NEW)} new courses. Registry now has {len(registry)} total.")
