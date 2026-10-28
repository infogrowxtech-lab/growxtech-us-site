#!/usr/bin/env python3
"""One-off: append this week's (2026-10-28) new course entries to courses_registry.json."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "scripts", "courses_registry.json")

NEW = [
    {
        "slug": "course-kotlin-basics",
        "course_id": "kotlin-basics",
        "title": "Kotlin Programming for Beginners",
        "title_tag": "Free Kotlin Course with Certificate",
        "meta_desc": "Free course on Kotlin programming fundamentals for beginners: syntax, null safety, and why Kotlin matters for Android and backend job postings.",
        "og_desc": "Learn Kotlin fundamentals: syntax, functions, and null safety. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Kotlin is Google's preferred language for Android development and shows up in backend job postings too. This course covers syntax, functions, and null safety basics.",
        "item_desc": "Learn Kotlin programming fundamentals including syntax, functions, and null safety for Android and backend roles.",
        "time_label": "~3.5 hrs",
        "h1_lead": "Learn Kotlin,",
        "h1_grad": "the language Google prefers for Android.",
        "lede": "Kotlin is Google's recommended language for Android development and increasingly shows up in backend job postings alongside Java. This course walks through syntax, functions, and Kotlin's null-safety features so you understand what makes it different from Java.",
        "outcomes": [
            "Write and run basic Kotlin programs",
            "Use Kotlin's core data types, functions, and control flow",
            "Understand null safety and why it matters",
            "Explain why companies choose Kotlin for Android in an interview"
        ],
        "youtube_id": "F9UC9DY-vIU",
        "video_title": "Kotlin Course - Tutorial for Beginners",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Kotlin Programming for Beginners course, what's next?"
    },
    {
        "slug": "course-php-basics",
        "course_id": "php-basics",
        "title": "PHP Programming for Beginners",
        "title_tag": "Free PHP Course with Certificate",
        "meta_desc": "Free course on PHP programming fundamentals for beginners: syntax, forms, and databases, with a free certificate on completion.",
        "og_desc": "Learn PHP fundamentals: syntax, forms, and database basics. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "PHP still powers a huge share of the web and shows up constantly in backend job postings. This course covers syntax, forms, and connecting to a database.",
        "item_desc": "Learn PHP programming fundamentals including syntax, forms, and database basics for backend web roles.",
        "time_label": "~7 hrs",
        "h1_lead": "Learn PHP,",
        "h1_grad": "the language behind a huge share of the web.",
        "lede": "PHP still runs a massive share of websites and backend systems, and it shows up constantly in web developer job postings. This course covers core syntax, handling forms, and connecting to a database so you understand how PHP fits into a typical web stack.",
        "outcomes": [
            "Write and run basic PHP scripts",
            "Handle forms and user input in PHP",
            "Connect PHP to a database for basic CRUD operations",
            "Explain where PHP fits in a modern web stack in an interview"
        ],
        "youtube_id": "OK_JCtrrv-c",
        "video_title": "PHP Programming Language Tutorial - Full Course",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the PHP Programming for Beginners course, what's next?"
    },
    {
        "slug": "course-rust-basics",
        "course_id": "rust-basics",
        "title": "Rust Programming for Beginners",
        "title_tag": "Free Rust Course with Certificate",
        "meta_desc": "Free course on Rust programming fundamentals for beginners: ownership, memory safety, and why Rust shows up in systems and infrastructure job postings.",
        "og_desc": "Learn Rust fundamentals: ownership, borrowing, and memory safety basics. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Rust keeps showing up in systems, infrastructure, and security job postings because of its memory safety guarantees. This course covers syntax, ownership, and borrowing.",
        "item_desc": "Learn Rust programming fundamentals including ownership, borrowing, and memory safety basics for systems roles.",
        "time_label": "~1.5 hrs",
        "h1_lead": "Learn Rust,",
        "h1_grad": "the language built for safe, fast systems code.",
        "lede": "Rust keeps climbing developer-survey rankings and shows up more often in systems, infrastructure, and security job postings. This course introduces syntax, ownership, and borrowing — the concepts that make Rust memory-safe without a garbage collector.",
        "outcomes": [
            "Write and run basic Rust programs",
            "Explain ownership and borrowing in plain terms",
            "Use Rust's core data types and control flow",
            "Speak confidently about why Rust matters for systems roles in an interview"
        ],
        "youtube_id": "MsocPEZBd-M",
        "video_title": "Rust Programming Course for Beginners - Tutorial",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Rust Programming for Beginners course, what's next?"
    },
    {
        "slug": "course-angular-basics",
        "course_id": "angular-basics",
        "title": "Angular Fundamentals",
        "title_tag": "Free Angular Course with Certificate",
        "meta_desc": "Free course on Angular fundamentals for beginners: components, TypeScript, and data binding, with a free certificate on completion.",
        "og_desc": "Learn Angular fundamentals: components, TypeScript, and data binding. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Angular remains a top front-end framework in enterprise job postings, especially alongside TypeScript. This course covers components, data binding, and routing basics.",
        "item_desc": "Learn Angular fundamentals including components, TypeScript, and data binding for front-end roles.",
        "time_label": "~4 hrs",
        "h1_lead": "Learn Angular,",
        "h1_grad": "the framework enterprise front-end teams rely on.",
        "lede": "Angular remains a default choice for large enterprise front-end teams, and it shows up constantly alongside TypeScript in job postings. This course covers components, data binding, and basic routing so you can explain how Angular structures a front-end app.",
        "outcomes": [
            "Build and run a basic Angular application",
            "Use components, templates, and data binding",
            "Understand basic routing between views",
            "Explain how Angular differs from React in an interview"
        ],
        "youtube_id": "AAu8bjj6-UI",
        "video_title": "Angular Tutorial for Beginners - Web Framework with Typescript Course",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Angular Fundamentals course, what's next?"
    },
    {
        "slug": "course-r-programming-basics",
        "course_id": "r-programming-basics",
        "title": "R Programming for Data Analysis",
        "title_tag": "Free R Programming Course with Certificate",
        "meta_desc": "Free course on R programming fundamentals for statistical computing and data analysis, with a free certificate on completion.",
        "og_desc": "Learn R programming fundamentals for statistical computing and data analysis. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "R remains the language of choice for statisticians and many data analyst roles, especially in research-heavy industries. This course covers the basics of statistical computing in R.",
        "item_desc": "Learn R programming fundamentals for statistical computing and data analysis roles.",
        "time_label": "~1 hr",
        "h1_lead": "Learn R,",
        "h1_grad": "the language statisticians and data analysts rely on.",
        "lede": "R remains the go-to language for statisticians and shows up in data analyst job postings across healthcare, finance, and research. This course covers the basics of statistical computing in R so you understand how it differs from Python for data work.",
        "outcomes": [
            "Write and run basic R scripts",
            "Work with R's core data structures for statistical computing",
            "Perform basic data summaries and visualizations in R",
            "Explain when a team might choose R over Python in an interview"
        ],
        "youtube_id": "_V8eKsto3Ug",
        "video_title": "R Programming Tutorial - Learn the Basics of Statistical Computing",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the R Programming for Data Analysis course, what's next?"
    },
    {
        "slug": "course-data-engineering-basics",
        "course_id": "data-engineering-basics",
        "title": "Data Engineering Fundamentals",
        "title_tag": "Free Data Engineering Course with Certificate",
        "meta_desc": "Free course introducing data engineering fundamentals: pipelines, ETL, and where data engineers fit in modern IT teams.",
        "og_desc": "Learn data engineering fundamentals: pipelines, ETL, and data warehousing basics. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Data engineering job postings keep growing as companies build out their data infrastructure. This course covers pipelines, ETL, and where data engineers fit alongside analysts and scientists.",
        "item_desc": "Learn data engineering fundamentals including pipelines, ETL, and data warehousing basics.",
        "time_label": "~2 hrs",
        "h1_lead": "Learn data engineering,",
        "h1_grad": "the role that builds the pipes data teams run on.",
        "lede": "Data engineering job postings keep growing as companies invest in the infrastructure that feeds their analytics and AI teams. This course introduces pipelines, ETL concepts, and data warehousing basics so you understand where a data engineer fits alongside analysts and data scientists.",
        "outcomes": [
            "Explain what a data pipeline does in plain terms",
            "Understand the basics of ETL (extract, transform, load)",
            "Recognize common data warehousing concepts",
            "Describe how data engineering differs from data analysis in an interview"
        ],
        "youtube_id": "PHsC_t0j1dU",
        "video_title": "Data Engineering Course for Beginners",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Data Engineering Fundamentals course, what's next?"
    },
    {
        "slug": "course-redis-basics",
        "course_id": "redis-basics",
        "title": "Redis and In-Memory Databases Basics",
        "title_tag": "Free Redis Course with Certificate",
        "meta_desc": "Free course on Redis fundamentals: in-memory data structures, caching, and basic commands, with a free certificate on completion.",
        "og_desc": "Learn Redis fundamentals: caching, data structures, and basic commands. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Redis shows up constantly in backend job postings as the go-to caching and in-memory data layer. This course covers core data structures and basic commands.",
        "item_desc": "Learn Redis fundamentals including caching, data structures, and basic commands for backend roles.",
        "time_label": "~1 hr",
        "h1_lead": "Learn Redis,",
        "h1_grad": "the caching layer behind countless backend systems.",
        "lede": "Redis shows up constantly in backend job postings as the default choice for caching, session storage, and fast in-memory lookups. This course covers Redis's core data structures and basic commands so you understand why teams reach for it.",
        "outcomes": [
            "Explain what Redis is and when teams use it",
            "Use Redis's core data structures (strings, lists, hashes, sets)",
            "Run basic Redis commands",
            "Describe how caching fits into a backend architecture in an interview"
        ],
        "youtube_id": "XCsS_NVAa1g",
        "video_title": "Redis Course - In-Memory Database Tutorial",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Redis and In-Memory Databases Basics course, what's next?"
    },
    {
        "slug": "course-unity-game-development",
        "course_id": "unity-game-development",
        "title": "Unity Game Development Basics",
        "title_tag": "Free Unity Game Development Course with Certificate",
        "meta_desc": "Free beginner course on Unity game development: the editor, C# scripting basics, and building a simple game.",
        "og_desc": "Learn Unity game development basics: the editor, C# scripting, and building a simple game. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Game development and simulation roles increasingly ask for Unity experience. This course covers the Unity editor and basic C# scripting to build a simple game.",
        "item_desc": "Learn Unity game development basics including the editor and C# scripting for game dev roles.",
        "time_label": "~1 hr",
        "h1_lead": "Learn Unity,",
        "h1_grad": "the engine behind a huge share of indie and mobile games.",
        "lede": "Unity shows up not just in gaming job postings but increasingly in simulation, training, and AR/VR roles. This course introduces the Unity editor and basic C# scripting so you can build and understand a simple game from scratch.",
        "outcomes": [
            "Navigate the Unity editor and its core panels",
            "Write basic C# scripts to control game objects",
            "Understand Unity's component-based architecture",
            "Explain the basics of a Unity project in an interview"
        ],
        "youtube_id": "gB1F9G0JXOo",
        "video_title": "Learn Unity - Beginner's Game Development Tutorial",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Unity Game Development Basics course, what's next?"
    },
    {
        "slug": "course-blockchain-solidity-basics",
        "course_id": "blockchain-solidity-basics",
        "title": "Blockchain and Solidity Basics",
        "title_tag": "Free Blockchain & Solidity Course with Certificate",
        "meta_desc": "Free beginner course on blockchain fundamentals and Solidity smart contracts, with a free certificate on completion.",
        "og_desc": "Learn blockchain fundamentals and Solidity smart contract basics. Free course, free certificate.",
        "category": "IT Technical Skills",
        "card_desc": "Blockchain and smart contract roles still show up in fintech and web3 job postings. This course covers blockchain fundamentals and the basics of writing Solidity smart contracts.",
        "item_desc": "Learn blockchain fundamentals and Solidity smart contract basics for web3 and fintech roles.",
        "time_label": "Self-paced",
        "h1_lead": "Learn blockchain,",
        "h1_grad": "and the basics of writing smart contracts.",
        "lede": "Blockchain and smart-contract roles haven't disappeared — they've concentrated into fintech, payments, and specialized web3 teams. This course introduces blockchain fundamentals and the basics of writing smart contracts in Solidity so you understand how decentralized apps actually work.",
        "outcomes": [
            "Explain what a blockchain is and how it stores data",
            "Understand what a smart contract does",
            "Write and deploy a basic Solidity smart contract",
            "Describe common blockchain use cases in an interview"
        ],
        "youtube_id": "gyMwXuJrbJQ",
        "video_title": "Learn Blockchain, Solidity, and Full Stack Web3 Development with JavaScript – 32-Hour Course",
        "upload_date": "2024-01-01",
        "cta_h2": "Want to go from tutorial to job-ready?",
        "cta_h2_grad": "Talk to a recruiter.",
        "cta_p": "This course covers the fundamentals. Growx also runs recruiter-led profile marketing, 1-on-1 technical training and mock interviews for candidates ready to go further.",
        "grobo_msg": "I finished the Blockchain and Solidity Basics course, what's next?"
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
