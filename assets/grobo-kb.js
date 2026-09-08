/* Charlie knowledge base — Growx Tech IT
   -----------------------------------------------------------------
   Every topic carries several phrasings of the same answer so Charlie
   never repeats itself word for word inside one conversation.
   RULES block below is what Charlie is NOT allowed to promise.
   ----------------------------------------------------------------- */
window.GROBO_KB = (function () {

  var TEL_D = '+1 (719) 838-9991';
  var WA_D  = '+1 (302) 683-1622';
  var MAIL  = 'hi@growxtech-it.us';

  /* Shorthands used inside answers.
     {{wa:text}}    -> WhatsApp button with a prefilled message
     {{call}}       -> call button
     {{both:text}}  -> both buttons
     {{lead}}       -> starts the "leave your details" flow after the answer  */

  var KB = [

  /* ---------------------------------------------------------- basics */
  { id:'greeting', w:3,
    k:['hi','hii','hiii','hello','hey','heyy','yo','hola','namaste','greetings','morning','afternoon','evening','sup','helo','hlo'],
    exact:true,
    a:[
      'Hey there. 👋 I\'m <b>Charlie</b>, the growth buddy at Growx Tech IT. Ask me about openings, pricing, resumes, training, visas or referrals, whatever is on your mind.',
      'Hello! Good to see you. I\'m <b>Charlie</b>. I can talk you through our services, prices, live openings or the referral program. Where do you want to start?',
      'Hi! 👋 Charlie here. Tell me where you are in your job search and I\'ll point you at the right thing.',
      'Hey. I\'m Charlie, the AI teammate here at Growx Tech IT. What brings you in today?'
    ],
    chips:['Live jobs','Pricing','Resume help','I need a job','Talk to a human'] },

  { id:'howareyou', w:3,
    k:['how are you','how r u','hows it going','how you doing','whats up','kaise ho','how do you do'],
    a:[
      'Doing well, thanks for asking. More importantly, how is your job search going?',
      'All good on my end. What about you, where are you stuck right now?',
      'I\'m good. Tell me what you are working towards and I\'ll see how we can help.'
    ] },

  { id:'identity', w:4,
    k:['who are you','you human','you a human','you a bot','you a robot','you real','you a real person','you ai','you an ai','robot','what are you','your name','who am i talking','real person or bot','human or bot'],
    re:/\b(are|r)\s+(you|u)\s+(a\s+)?(real|human|person|bot|robot|ai|machine|computer)\b/,
    a:[
      'I\'m <b>Charlie</b>, an AI assistant, not a person. I know our services, prices and process inside out, and the moment you want a real career advisor I can put you through in one tap.',
      'Fair question. I\'m an AI, Growx Tech IT\'s assistant. I handle the quick answers so you don\'t wait, and a human advisor takes over whenever you want.',
      'Charlie, the AI teammate here. I\'m not human, so for anything about your specific file or a decision on your case, a real advisor should be the one to answer.'
    ],
    chips:['Talk to a human','Pricing','How it works'] },

  { id:'about', w:2,
    k:['company','growx','who is growx','what do you do','what does growx do','about your company','about growx'],
    a:[
      '<b>Growx Tech IT</b> is a career services and placement company. We rebuild resumes and LinkedIn profiles, run technical training, prepare people for interviews, and our recruiters market candidate profiles directly to employers.<br><br>800+ placements so far, 100+ career experts on staff, across 11 industries in the US, India and Australia.',
      'We are a career services firm. In short: we fix how you present yourself, close your skill gaps, and then actively push your profile in front of hiring teams instead of leaving you to apply alone.<br><br>Offices in Sheridan, Wyoming and Ahmedabad, India.',
      'Growx Tech IT takes people from "I keep applying and hearing nothing" to a signed offer. Resume, LinkedIn, training, interview prep, recruiter-led marketing and mentorship after you are placed, all under one team.'
    ],
    chips:['Services','Pricing','Success stories'] },

  /* ---------------------------------------------------------- services */
  { id:'services', w:2,
    k:['service','services','what do you offer','offerings','help me','what can you do','packages','programs','process','how it works','how does it work','stages'],
    a:[
      'Six stages, one team:<br>1. <b>Free consultation</b>, 1 to 2 days<br>2. <b>Resume and LinkedIn rebuild</b>, 7 to 10 days<br>3. <b>Recruiter-led profile marketing</b>, ongoing<br>4. <b>Technical training</b>, about 20 days<br>5. <b>Interview preparation</b> and mock interviews<br>6. <b>Mentorship</b> after you are placed<br><br>Full detail on the <a href="/services">services page</a>. Which stage are you at?',
      'We run the whole journey: consultation, resume and LinkedIn makeover, daily profile marketing by a dedicated recruiter, hands-on technical training, structured interview prep, and mentorship once you are hired.<br><br>Most people start with the free consultation. Want me to set that up?',
      'Think of it as four things: <b>presentation</b> (resume, LinkedIn), <b>skills</b> (training), <b>reach</b> (recruiters marketing you), and <b>conversion</b> (interview prep). We also do OPT clock hold, background guidance and STEM payroll support.<br><br>What do you need most right now?'
    ],
    chips:['Resume','Training','Profile marketing','Pricing'] },

  { id:'resume', w:2,
    k:['resume','cv','resumee','resum','ats','rewrite my resume','fix my resume','resume writing'],
    a:[
      'Our writers rebuild your resume so it clears ATS filters and actually reads well to a human recruiter. Turnaround is <b>7 to 10 days</b>, from <b>$200</b>.<br><br>Send your current one over and an advisor will review it free, no obligation. {{wa:Hi Growx Tech IT, please review my resume. Attaching it here.}}',
      'Resume work starts at <b>$200</b>. That gets you a full professional rewrite, ATS-friendly formatting and a personal branding kit. At $400 you also get a career strength assessment, and $600 adds the full LinkedIn makeover.<br><br>The free review comes first, so you know what needs fixing before you pay anything.',
      'Most people who "keep applying and hear nothing" have a resume problem, not a market problem. We rebuild yours around what recruiters in your target roles actually screen for.<br><br>Want an advisor to look at your current version first? {{wa:Hi, I would like a free resume review.}}'
    ],
    chips:['Pricing','LinkedIn too','Send my resume'] },

  { id:'linkedin', w:2,
    k:['linkedin','linked in','profile optimization','optimise my profile','social profile'],
    a:[
      'LinkedIn optimization is part of the <b>$600</b> complete package, along with the resume and the career session. We rewrite the headline, About section, experience and skills so U.S. recruiters searching for your role actually surface you.',
      'We rebuild your LinkedIn so it works as a search result, not a CV copy. Keywords, headline, About, experience, skills, the lot. It comes bundled at the <b>$600</b> tier with the resume rewrite.',
      'Yes, LinkedIn is covered. It is included in the complete <b>$600</b> resume and profile package. A good profile is what makes recruiters come to you instead of the other way round.'
    ],
    chips:['Resume too','Pricing','Get started'] },

  { id:'training', w:2,
    k:['training','course','learn','skill','upskill','bootcamp','classes','teach','study','technical training'],
    a:[
      'Training runs about <b>20 days</b>, hands-on projects and assessments rather than slide decks. Three formats:<br>• Group, <b>$600</b><br>• One-on-one, <b>$800</b><br>• One-on-one with recorded mock interviews, <b>$1,000</b><br><br>Which suits how you learn?',
      'We close the specific gaps that are costing you interviews, not a generic syllabus. About 20 days, real projects, assessments at the end. From <b>$600</b> for group, up to <b>$1,000</b> for one-on-one with recorded mocks.',
      'Technical training is built around your target role. Group sessions are $600, one-on-one is $800, and $1,000 adds recorded mock interviews you can rewatch. Roughly 20 days either way.'
    ],
    chips:['Interview prep','Pricing','Sign me up'] },

  { id:'interview', w:2,
    k:['interview','mock','mock interview','interview prep','preparation','nervous','interview support','hr round','technical round'],
    a:[
      'Interview prep is structured, not a pep talk: mock interviews against your actual target role, behavioural coaching, and scheduling support until you feel ready. It is bundled into the training and placement packages.',
      'We run mock interviews, record them where useful, and go through what landed and what did not. Plus behavioural coaching and interview scheduling handled for you.<br><br>The one-on-one training tier at <b>$1,000</b> includes recorded mocks.',
      'Yes, interview support is a core part of what we do, right through to offer stage. Mocks, feedback, coaching, and our team coordinates the scheduling so you are not chasing anyone.'
    ],
    chips:['Training','Pricing','Talk to a human'] },

  { id:'marketing', w:2,
    k:['profile marketing','marketing','recruiter','apply for me','applications','submit my profile','market my profile','dedicated recruiter','100 applications'],
    a:[
      'This is the part most people cannot do alone. A <b>dedicated recruiter</b> markets your profile every day to targeted employers, staffing partners and hiring networks, and coordinates every interview.<br><br>From <b>$2,500</b>. Extended reach is $3,500, and the placement track aimed at 10 final-round interviews is $4,000.',
      'Recruiter-led marketing means someone on our side is actively pushing your profile out, up to 100 targeted applications a day, with daily activity reports and interview scheduling handled.<br><br>Starts at <b>$2,500</b>. There is also the all-in plan: $1,000 enrollment plus <b>8.5% of first-year salary</b>, that 8.5% billed only after you accept an offer.',
      'A personal recruiter takes over the outreach: targeted applications, employer follow-ups, interview coordination and daily reports to you. From <b>$2,500</b>, or bundled into the Placement Partner plan ($1,000 enrollment + 8.5% after you are placed).'
    ],
    chips:['8.5% plan','Pricing','Get a recruiter'] },

  { id:'mentorship', w:2,
    k:['mentor','mentorship','after placement','after joining','post placement','career guidance','career advice'],
    a:[
      'Mentorship carries on after you sign the offer. Career tracking, guidance on the first months, and help planning the next move. It is not a hand-off at the offer letter.',
      'We stay with you after placement, that is deliberate. Ongoing mentorship and career tracking so the first role becomes a career, not just a job.',
      'Post-placement mentorship is included in the full packages. The first ninety days in a new role matter, and having someone to check in with makes a difference.'
    ] },

  { id:'opt', w:3,
    k:['opt','cpt','opt clock','clock hold','f1','student visa','stem opt','day 1 cpt','unemployment days'],
    a:[
      'We do offer <b>OPT clock hold support with zero fees applied</b>, that is one of our services. What it involves in your specific case depends on your status and dates, so I will not guess here.<br><br>Let me get an advisor on this with you, it is worth getting right. {{both:Hi Growx Tech IT, I have a question about OPT clock hold. My status is:}}',
      'OPT and CPT questions come up a lot and we support OPT clock hold at no fee. But the details are case by case and I am not the right one to interpret your dates or paperwork.<br><br>An advisor can walk you through it properly. {{both:Hi, I need help with my OPT situation.}}',
      'Yes, OPT clock hold is something we help with, zero fees applied. I would rather an advisor answer the specifics than have me give you a half answer on something this important. {{both:Hi, I want to discuss OPT clock hold.}}'
    ],
    guard:true },

  { id:'payroll', w:3,
    k:['payroll','stem payroll','w2','c2c','corp to corp','employer of record','1099'],
    a:[
      'We do offer <b>STEM payroll</b> support. The right structure depends on your status and the employer, so an advisor should confirm what applies to you rather than me generalising. {{both:Hi, I want to ask about STEM payroll.}}',
      'STEM payroll is on our service list, yes. Terms vary by case, so let me put you through to someone who can look at your situation properly. {{both:Hi Growx Tech IT, question about payroll options.}}'
    ],
    guard:true },

  { id:'background', w:2,
    k:['background check','background verification','bgv','verification','employment check','reference check'],
    a:[
      'We provide <b>placement and background guidance</b>, meaning we help you understand what employers verify and how to prepare your documentation honestly.<br><br>To be clear about what we will not do: we do not fabricate experience or falsify records, ever. If that is what you are after, we are not the right fit.',
      'Background guidance is part of what we do, helping you present a verifiable, accurate history and be ready for what employers check.<br><br>We only work with real experience and real documents. Anything else puts your career at risk, not just your application.'
    ],
    guard:true },

  /* ---------------------------------------------------------- pricing */
  { id:'pricing', w:2,
    k:['price','pricing','cost','fee','fees','charge','charges','how much','rate','rates','payment','expensive','cheap','budget','kitna','paisa','package','packages','which package','package fits','plan','plans','tiers'],
    a:[
      'Here is the whole thing, no hidden numbers:<br>• <b>Resume and LinkedIn</b>, $200 / $400 / $600<br>• <b>Technical training</b>, $600 / $800 / $1,000<br>• <b>Recruiter-led marketing</b>, $2,500 / $3,500 / $4,000<br>• <b>All-in Placement Partner</b>, $1,000 enrollment fee plus 8.5% of first-year salary (that 8.5% billed only after an offer)<br><br>Full breakdown on the <a href="/pricing">pricing page</a>. Where are you in your search? I can tell you which one actually fits.',
      'Four tracks:<br><b>01</b> Resume and profile, from $200<br><b>02</b> Training, from $600<br><b>03</b> Recruiter marketing, from $2,500<br><b>04</b> Everything in one, $1,000 enrollment fee plus 8.5% of your annual pay package, that 8.5% paid only after you accept an offer<br><br>The initial consultation is free either way, and honestly, sometimes the cheapest option is enough. Tell me your situation.',
      'Prices start at <b>$200</b> for a resume rebuild and go up to full recruiter-led placement. There is also the all-in plan: a $1,000 enrollment fee, then 8.5% more only once you have an offer in hand.<br><br>Rather than guess, tell me your target role and where you are stuck and I will say which track makes sense.'
    ],
    chips:['8.5% plan','Resume price','Training price','Payment terms'] },

  { id:'price_allin', w:3,
    k:['8.5','8.5%','eight point five','percentage','percent','annual pay','salary based','no upfront','nothing upfront','success fee','pay after job','placement partner','enrollment fee','enrollment'],
    a:[
      'That is the <b>All-in Placement Partner</b> plan. You get everything: resume rebuild, LinkedIn makeover, full technical training, unlimited mock interviews, a dedicated recruiter marketing you daily, interview scheduling, offer negotiation and post-placement mentorship.<br><br>It is $1,000 enrollment at sign-up to unlock all of that, plus <b>8.5% of your first-year salary</b>, and that 8.5% only once you accept an offer.',
      'The Placement Partner plan bundles every service into one: $1,000 to enroll, then 8.5% of your first-year salary once you have accepted an offer.<br><br>It suits people who want the full engine behind them without paying package by package.',
      '$1,000 enrollment fee upfront, plus 8.5% of your annual pay package billed after you sign, covering the complete service from resume through to mentorship after joining. The exact terms get confirmed in writing before anything starts, so nothing is a surprise. {{both:Hi, tell me more about the Placement Partner plan.}}'
    ],
    chips:['Other packages','Payment terms','I am interested'] },

  { id:'payment_terms', w:2,
    k:['payment terms','installment','emi','instalment','advance','upfront','when do i pay','30%','how to pay','pay in parts'],
    a:[
      'For the fixed-price packages it is <b>30% at registration</b> and the balance after the initial delivery milestones. So you see work before you pay the rest.<br><br>The Placement Partner plan works differently: $1,000 enrollment upfront, then <b>8.5%</b> of your first-year salary only once an offer is accepted.',
      'Standard terms: 30% to start, the rest once the first deliverables are in your hands. On the all-in Placement Partner plan it is $1,000 to enroll, then 8.5% after you are placed, nothing more before that.<br><br>Anything beyond that, an advisor confirms in writing before you commit.',
      '30% at registration, remainder after delivery milestones. Currency is USD. The consultation before all of that is free.'
    ] },

  { id:'payment_method', w:2,
    k:['payment method','card','credit card','debit','upi','bank transfer','paypal','razorpay','stripe','wire','how do i pay you'],
    a:[
      'Payment options get confirmed by your advisor when you enrol, and everything goes through a proper invoice, never through this chat.<br><br>One thing I will always say: <b>never share card numbers, passwords or ID numbers with me or in any chat</b>. A real advisor will send you a secure invoice instead. {{both:Hi, I would like to know the payment options.}}',
      'An advisor will send you a formal invoice with the available payment methods. I deliberately do not handle payment details here, and you should never type card or bank details into a chat window, ours or anyone else\'s. {{both:Hi, please share payment details for enrolment.}}'
    ],
    guard:true },

  { id:'discount', w:2,
    k:['discount','offer','deal','cheaper','negotiate','reduce price','lower price','student discount','concession','free service'],
    a:[
      'I am not able to authorise discounts or quote a custom price, that has to come from an advisor who can look at your case.<br><br>What I can tell you is that the consultation is genuinely free, and we will tell you honestly if a cheaper package is enough for you. {{both:Hi, can we discuss pricing for my situation?}}',
      'Pricing decisions sit with the team, not with me, so I would be making something up if I promised you a number. Talk to an advisor and ask directly, they can look at what you actually need. {{both:Hi, I want to discuss the price for my case.}}'
    ],
    guard:true },

  { id:'refund', w:2,
    k:['refund','money back','cancel','cancellation','guarantee money','return my money'],
    a:[
      'Refund and cancellation terms are set out in the agreement you sign before anything starts, and I am not going to paraphrase a contract at you.<br><br>Ask an advisor to walk you through the exact terms before you commit, that is the right way to do it. {{both:Hi, please explain the refund and cancellation terms.}}',
      'That is a contractual question, and it deserves the actual document rather than my summary. An advisor will go through the terms with you before you pay anything. {{both:Hi, I have a question about refunds.}}'
    ],
    guard:true },

  /* ---------------------------------------------------------- jobs */
  { id:'jobs', w:2,
    k:['job','jobs','vacancy','vacancies','opening','openings','hiring','position','role','naukri','work','employment','apply'],
    a:[
      'We pull <b>live openings</b> from several job boards every day and you can filter by USA, Canada, Australia or remote on the <a href="/jobs">jobs page</a>.<br><br>But honestly, applying alone is slow. Tell me your target role and country and I will get a recruiter to shortlist matches for you.{{lead}}',
      'Two ways to go about it. Browse the <a href="/jobs">live jobs board</a>, refreshed daily, and apply yourself. Or let our recruiters market your profile so employers approach you instead.<br><br>What role and country are you targeting?{{lead}}',
      'There are live openings on the <a href="/jobs">jobs page</a> right now, filterable by country. If you want the faster route, a recruiter can run targeted applications for you daily.<br><br>Which are you leaning towards?'
    ],
    chips:['See live jobs','Get a recruiter','My target role is...'] },

  { id:'remote', w:2,
    k:['remote','work from home','wfh','anywhere','online job','virtual'],
    a:[
      'Remote roles are on the <a href="/jobs">jobs board</a>, there is a Remote filter right at the top. A good share of what we pull in is remote or hybrid.',
      'Yes, plenty of remote openings. Use the Remote filter on the <a href="/jobs">jobs page</a>. Worth saying though, remote roles get far more applicants, so how your profile reads matters even more there.'
    ] },

  { id:'fresher', w:2,
    k:['fresher','freshers','no experience','entry level','graduate','just graduated','student','beginner','first job','starting out'],
    a:[
      'We work with people at the start of their career, that is a big part of what we do, our mascot is literally a fresh graduate. Training plus a properly built resume is usually the right starting combination.<br><br>What did you study, and what kind of role are you aiming for?',
      'Freshers are welcome. The honest picture: with little experience, skills and presentation carry the weight, so training plus a strong resume is where we would start you.<br><br>Tell me your background and target role and I will suggest a track.'
    ],
    chips:['Training','Resume','Pricing'] },

  { id:'experienced', w:2,
    k:['experienced','years of experience','senior','lead','manager','mid level','switch job','change job','career change'],
    a:[
      'For experienced candidates the bottleneck is usually reach, not ability. That is where recruiter-led marketing earns its keep, your profile gets in front of hiring teams instead of sitting in a queue.<br><br>How many years, and what role are you targeting?',
      'With real experience behind you, we normally focus on positioning and reach: sharpen the resume and LinkedIn, then have a recruiter push you to the right employers.<br><br>What is your current role and what are you moving towards?'
    ] },

  /* ---------------------------------------------------------- guarded */
  { id:'guarantee', w:4,
    k:['guarantee','guaranteed','100%','surety','assured','promise me','will i get a job','confirm job','definitely get','sure job','job pakka'],
    a:[
      'I am going to be straight with you: <b>nobody can guarantee you a job</b>, and I will not pretend otherwise. Anyone promising a guaranteed offer is selling you something.<br><br>What we do guarantee is the work: the resume gets rebuilt, the training happens, the recruiter markets you daily, the interviews get coordinated. 800+ people have been placed that way. The hiring decision is always the employer\'s. {{both:Hi, I would like to understand what results I can realistically expect.}}',
      'No guarantees on offers, and I would rather lose your business than promise you something I cannot deliver.<br><br>Our track record is 800+ placements, and we commit fully to the work: presentation, skills, reach and interview prep. Employers still make the final call, always.',
      'Honest answer: no. No agency can guarantee a job, a salary, or a visa outcome. What we commit to is effort and process, and those we deliver in writing.<br><br>If you want a realistic read on your specific profile, an advisor will give you one, including if the answer is "this will be hard". {{both:Hi, I want an honest assessment of my profile.}}'
    ],
    guard:true },

  { id:'visa', w:4,
    k:['visa','h1b','h-1b','h1','sponsor','sponsorship','green card','gc','immigration','work permit','work authorization','ead','lottery','uscis'],
    a:[
      'We work with citizens, green card holders, H-1B, OPT and CPT candidates, and we are upfront when a target role is unlikely to sponsor.<br><br>What I will not do is give you immigration advice or predict a visa outcome, I am not qualified and neither is any recruiter. For anything legal, an immigration attorney is the right person.<br><br>Tell me your status and target role and an advisor will give you a realistic read on the job market side. {{both:Hi, my work authorization status is:}}',
      'Sponsorship depends entirely on the employer, and no one here can promise it. We can tell you which roles and employers in your space tend to sponsor, and we are honest when the odds are poor.<br><br>Immigration questions themselves need an attorney, not us. {{both:Hi, I want to discuss sponsorship for my target roles.}}',
      'Straight answer: we cannot influence or guarantee any visa outcome, and we do not give legal advice. What we can do is market you to employers realistically open to your status, and tell you plainly when a path is unlikely.<br><br>What is your current status?'
    ],
    guard:true },

  { id:'salary', w:3,
    k:['salary','how much will i earn','ctc','compensation','how much can i get','expected salary','salary range','what salary','earn per year','annual pay i will get'],
    a:[
      'Salary depends on the role, your experience, the location and the employer, so any number I threw out would be a guess.<br><br>What I can say is we handle offer negotiation as part of the full packages, and an advisor can give you a realistic band for your specific profile. {{both:Hi, what salary range is realistic for my profile?}}',
      'I will not quote you a figure, that would be dishonest without knowing your profile. An advisor who has seen your resume can give you a real range for your target market. {{both:Hi, I would like a realistic salary read on my profile.}}'
    ],
    guard:true },

  { id:'timeline', w:2,
    k:['how long','duration','timeline','how fast','when will i get','how many days','time frame','quickly','urgent','fast'],
    a:[
      'Realistic timings: consultation 1 to 2 days, resume and LinkedIn 7 to 10 days, training around 20 days. Profile marketing and interviews then run until you land an offer.<br><br>How long that last part takes depends on your profile and the market, so nobody should give you a fixed date for an offer.',
      'The parts we control have clear timelines: 1 to 2 days for the consultation, 7 to 10 for the resume and LinkedIn, about 20 days of training.<br><br>The offer itself has no fixed timeline, and I would be lying if I gave you one. What I can say is the recruiter keeps working until it happens.',
      'Deliverables are quick, the resume is with you inside 7 to 10 days. The job search itself varies person to person. If you are on a deadline, tell an advisor, they can prioritise accordingly. {{both:Hi, I am working to a deadline. My situation is:}}'
    ] },

  /* ---------------------------------------------------------- company info */
  { id:'industries', w:2,
    k:['industry','industries','sector','sectors','field','only tech','non tech','non-tech','healthcare','finance','banking','engineering','retail','logistics','legal','hospitality','manufacturing','construction','education'],
    a:[
      'We are not tech-only, that is a common assumption. Eleven industries: information technology, healthcare, banking and finance, engineering, education, retail and e-commerce, legal and compliance, logistics and supply chain, hospitality and travel, manufacturing, and construction and real estate.<br><br>Which one are you in?',
      'Across 11 industries, IT is just one of them. Healthcare, banking and finance, engineering, education, retail, legal, logistics, hospitality, manufacturing and construction are all covered too.<br><br>Tell me your field and I will tell you honestly how much depth we have there.'
    ],
    chips:['My industry is...','Live jobs','Pricing'] },

  { id:'countries', w:2,
    k:['country','countries','usa','us','united states','america','canada','australia','india','uk','europe','which country','where do you place','abroad','overseas'],
    a:[
      'We serve candidates in the <b>United States, India and Australia</b>, and the live jobs board also carries Canada and remote roles.<br><br>Which country are you targeting?',
      'US, India and Australia are our main markets, with Canadian and remote openings on the jobs board as well. Where do you want to work?'
    ] },

  { id:'offices', w:2,
    k:['where','address','office','location','located','based','headquarters','hq','come to office','visit'],
    a:[
      '🇺🇸 <b>USA</b>: Growx Tech IT LLC, 30 N Gould St, Sheridan, Wyoming 82801<br>🇮🇳 <b>India</b>: Growx Tech IT LLC, C-706, Siddhi Vinayak Towers, Sarkhej , Gandhinagar Hwy, Makarba, Ahmedabad, Gujarat 380051<br><br>Most of the work happens remotely, so wherever you are is fine.',
      'Two offices: Sheridan in Wyoming for the US, and Ahmedabad in Gujarat for India. Everything we do works remotely though, candidates across the US, India and Australia.'
    ] },

  { id:'hours', w:2,
    k:['timing','timings','hours','open','available','office hours','when can i call','what time','24/7','weekend'],
    a:[
      'I am here <b>24/7</b>, so ask me anything any time. The phone line and WhatsApp are answered during business hours across our US and India teams, and WhatsApp usually gets the fastest reply.<br><br>Leave your question here and it reaches an advisor either way.',
      'Me, always on. Humans, business hours, though with teams in both the US and India the window is wide. WhatsApp is normally the quickest way through: {{wa:Hi Growx Tech IT, I have a question.}}'
    ] },

  { id:'trust', w:2,
    k:['legit','scam','fraud','real company','trust','trustworthy','reviews','review','testimonial','proof','genuine','registered','is this fake','company fake'],
    a:[
      'Fair thing to check, and you should check it. We are <b>Growx Tech IT LLC</b>, registered in Wyoming with an office in Ahmedabad. Client reviews are on the <a href="/#reviews">homepage</a> and we are on <a href="https://www.linkedin.com/company/growx-tech-it/" rel="noopener" target="_blank">LinkedIn</a>.<br><br>Also, healthy scepticism is right: be wary of anyone guaranteeing you a job. We do not, and we will not.',
      'Please do check us out. Registered as Growx Tech IT LLC in Wyoming, second office in Ahmedabad, reviews from client companies on the site, and a LinkedIn presence you can look through.<br><br>And if anything I say sounds too good, push back on it. Nothing here should sound like a guarantee.'
    ] },

  { id:'success', w:2,
    k:['success','placements','800','track record','result','results','how many people','case study','stories'],
    a:[
      '<b>800+ successful placements</b> so far, across 11 industries, with 100+ career experts on staff in the US, India and Australia.<br><br>What that does not mean is that every single person gets placed. It means the process works often enough to be worth your time.',
      'Over 800 placements to date. Reviews from partner companies are on the <a href="/#reviews">homepage</a>.<br><br>I would rather you judge us on the process than the number though, ask an advisor what they would actually do with your profile. {{both:Hi, what would you do with a profile like mine?}}'
    ] },

  { id:'privacy', w:2,
    k:['privacy','data','my information','safe','secure','share my resume','confidential','gdpr','delete my data'],
    a:[
      'Your resume and details are used to deliver the service and, where you have engaged us for profile marketing, shared with prospective employers and staffing partners. That is the point of the service.<br><br>We do not sell your information, and you can ask us to delete it at any time. The full <a href="/privacy-policy">privacy policy</a> spells it out.',
      'Short version: we use your information to do the work and to market you to employers when you have asked us to, we do not sell it, and you can have it deleted on request. Details are in the <a href="/privacy-policy">privacy policy</a>.'
    ] },

  /* ---------------------------------------------------------- actions */
  { id:'referral', w:3,
    k:['refer','referral','refer a friend','reward','refer someone','commission','bonus for referring'],
    a:['__REFERRAL_FLOW__'] },

  { id:'start', w:2,
    k:['start','begin','sign up','signup','register','enrol','enroll','join','get going','book','consultation','free consultation','onboard','how do i start','next step',
       'take my details','yes take my details','share my details','here are my details','call me back','contact me','reach out to me','leave my details','my details','get in touch with me','someone call me'],
    a:['__LEAD_FLOW__'] },

  { id:'human', w:3,
    k:['human','advisor','agent','person','someone','representative','talk to someone','speak to someone','real person','counsellor','counselor','manager','call me','contact me'],
    a:[
      'Of course. Here are both routes, WhatsApp is usually answered fastest and the phone line is live during business hours. {{both:Hi Growx Tech IT, I would like to speak to a career advisor.}}',
      'Happy to hand you over. Pick whichever suits you. {{both:Hi, please connect me with a career advisor.}}',
      'Absolutely, a person will serve you better on this. {{both:Hi Growx Tech IT, I would like to talk to an advisor.}}'
    ] },

  { id:'contact', w:2,
    k:['contact','phone','number','call','whatsapp','email','mail','reach you','get in touch','telephone'],
    a:[
      '📞 Call <b>' + TEL_D + '</b><br>💬 WhatsApp <b>' + WA_D + '</b><br>✉️ <a href="mailto:' + MAIL + '">' + MAIL + '</a><br><br>Or just tell me here and I will pass it on. {{both:Hi Growx Tech IT, I would like to get in touch.}}',
      'Phone is ' + TEL_D + ', WhatsApp is ' + WA_D + ', and email is <a href="mailto:' + MAIL + '">' + MAIL + '</a>. There is also the <a href="/contact">contact page</a> with everything in one place. {{both:Hi, I would like to talk to someone.}}'
    ] },

  { id:'send_resume', w:2,
    k:['send my resume','share resume','upload resume','attach','how do i send','where do i send','email my cv'],
    a:[
      'WhatsApp is easiest, you can attach the file directly and an advisor picks it up. Or email it to <a href="mailto:' + MAIL + '">' + MAIL + '</a>.<br><br>I cannot receive files here myself. {{wa:Hi Growx Tech IT, attaching my resume for a free review. My target role is:}}',
      'Send it on WhatsApp with your target role in the message, that gets you the quickest review. Email to <a href="mailto:' + MAIL + '">' + MAIL + '</a> works too. {{wa:Hi, here is my resume for a free review.}}'
    ] },

  { id:'employer', w:3,
    k:['hire','hiring for my company','c2c','staffing','employer','recruit for us','we are hiring','bulk hiring','need candidates','vendor','partner with you'],
    a:[
      'If you are hiring rather than job hunting, we do that side too, C2C and direct staffing across the industries we cover.<br><br>Let me put you with the team that handles employer accounts. {{both:Hi Growx Tech IT, we are hiring and would like to discuss staffing.}}',
      'Employer side, understood. We supply candidates across all 11 industries and handle C2C arrangements.<br><br>An account person should take this rather than me. {{both:Hi, we would like to discuss hiring through Growx.}}'
    ] },

  { id:'careers', w:3,
    k:['work at growx','job at growx','join your team','careers at','hire me as recruiter','vacancy in your company','work for you'],
    a:[
      'Interested in working <b>at</b> Growx rather than through us? Send your resume to <a href="mailto:' + MAIL + '">' + MAIL + '</a> with "Careers" in the subject and the team will look at it.',
      'For roles inside Growx Tech IT, email <a href="mailto:' + MAIL + '">' + MAIL + '</a> with your resume and mention it is a careers enquiry.'
    ] },

  { id:'existing_client', w:3,
    k:['already paid','i am a client','my file','my recruiter','no response','not responding','complaint','delay','status of my','follow up','nobody replied'],
    a:[
      'If you are already with us, I do not have access to individual files, so I cannot look up your status, and I do not want to guess at it.<br><br>Please go straight to a human on this, and mention that it is an existing file so it gets prioritised. {{both:Hi, I am an existing client and I need an update on my file.}}',
      'For an existing client matter I am the wrong stop, I cannot see your file. Let me get you to the team directly, and say it is a follow-up so it is routed properly. {{both:Hi, existing client here, I need a follow-up on my file.}}'
    ],
    guard:true },

  /* ---------------------------------------------------------- social */
  { id:'thanks', w:2,
    k:['thank','thanks','thankyou','thx','ty','appreciate','great','awesome','cool','perfect','nice','helpful','good'],
    a:[
      'Anytime. 😊 Anything else you want to know?',
      'Glad that helped. What else can I dig into for you?',
      'Happy to help. Anything else on your mind?',
      'You are welcome. Ask away if something else comes up.'
    ] },

  { id:'bye', w:2,
    k:['bye','goodbye','see you','later','thats all','that is all','no thanks','nothing else','done','exit','quit'],
    a:[
      'Take care. 👋 I am here whenever you need me, and the team is one tap away. {{both:Hi Growx Tech IT, I was chatting with Charlie and would like to continue.}}',
      'All the best with the search. Come back any time, I do not sleep. 👋',
      'Good luck out there. If you want a human to pick this up later, the WhatsApp line is always open. 👋'
    ] },

  { id:'praise_bot', w:2,
    k:['you are good','smart bot','nice bot','you are helpful','love this','impressive','well made'],
    a:[
      'Thanks. 😄 Credit to the team who fed me everything, I just remember it well. What else can I help with?',
      'Appreciate that. Now let us get you something useful, what is the next question?'
    ] },

  { id:'confused', w:2,
    k:['what','huh','i dont understand','dont get it','confusing','unclear','explain again','repeat'],
    a:[
      'My fault, let me try that differently. Which part do you want me to unpack, the <b>process</b>, the <b>pricing</b>, or what happens <b>first</b>?',
      'Let me back up. Tell me in your own words what you are trying to sort out, and I will aim at that instead.'
    ],
    chips:['How it works','Pricing','Where do I start'] },

  /* ------------------------------------------------ customer handling */
  { id:'complaint', w:4,
    k:['complaint','complain','unhappy','not happy','disappointed','bad service','poor service','waste of money','waste of time','frustrated','angry','upset','worst','terrible','cheated','scammed me','no results','nothing happened','fed up'],
    re:/\b(not|no)\s+(happy|satisfied|good)\b|\bvery\s+(bad|poor|disappointed)\b/,
    a:['__COMPLAINT_FLOW__'] },

  { id:'escalate', w:4,
    k:['manager','supervisor','escalate','senior person','someone in charge','owner','higher up','speak to your boss','complaint department'],
    a:[
      'Understood, and that is a fair ask. I cannot escalate inside the system myself, but I can take the details right now and flag them so the right person picks it up, or you can go straight to the team on WhatsApp or the phone.<br><br>Which do you prefer?',
      'Fair enough. Let me get this to a senior person rather than have you repeat yourself. I will take the details and mark it urgent, or you can call directly and ask for a team lead.' 
    ],
    chips:['Take my details','Talk to a human'] },

  { id:'delay', w:3,
    k:['delay','delayed','late','taking too long','still waiting','no update','not delivered','been weeks','been days','when will i get my resume','where is my'],
    a:['__COMPLAINT_FLOW__'] },

  { id:'invoice', w:3,
    k:['invoice','receipt','bill','billing','payment not reflected','paid but','double charged','charged twice','payment failed','transaction'],
    a:[
      'Billing questions need someone who can actually open your account, and I cannot. Let me get your details to the team so they can look it up properly.<br><br>Do not share any card or bank details with me, they will not need them to find your record.',
      'I have no access to payment records, so anything I said would be a guess. The team can pull up your invoice directly.<br><br>Send them your name and the email you registered with, nothing more than that. {{both:Hi Growx Tech IT, I have a billing question. My registered email is:}}'
    ],
    chips:['Take my details','Talk to a human'] },

  { id:'cancel_service', w:3,
    k:['cancel my service','stop the service','want to quit','discontinue','opt out','stop marketing my profile','remove my profile','delete my account'],
    a:[
      'You can ask us to stop at any time, including stopping profile marketing or deleting your information. That request should go to a human so it is recorded properly, not left in a chat log.<br><br>What the cancellation means for fees already paid depends on your agreement, and an advisor will walk you through it. {{both:Hi Growx Tech IT, I would like to discuss stopping my service.}}',
      'That is your call to make and we will honour it. Let me put you through to the team so it gets actioned and documented. They will also explain where you stand on anything already paid. {{both:Hi, I want to stop my service. Please advise on next steps.}}'
    ] },

  /* ---------------------------------------------------- more coverage */
  { id:'career_break', w:2,
    k:['career break','gap','employment gap','been out of work','unemployed','laid off','layoff','fired','sabbatical','maternity','returning to work'],
    a:[
      'A gap is not the dealbreaker people think it is, but it does need to be handled properly on the resume rather than hidden. We reframe it honestly and prepare you for the question, because it will come up.<br><br>How long is the gap, and what were you doing in that time?',
      'Career breaks are common and we work with them a lot. What matters is the story you tell and how current your skills look, and both of those we can fix.<br><br>Tell me roughly how long the break has been and what role you are going back to.'
    ],
    chips:['Resume','Training','Talk to a human'] },

  { id:'documents', w:2,
    k:['documents','what do you need from me','what should i send','paperwork','which papers','details required'],
    a:[
      'To start, three things: your current resume, the job title and country you are targeting, and your work authorization status. That is enough for a real conversation.<br><br>Nothing sensitive at this stage. No ID numbers, no bank details.',
      'Just your resume, your target role and country, and your work authorization. We ask for anything else only when it is actually needed, and never through this chat.'
    ],
    chips:['Send my resume','Take my details'] },

  { id:'cover_letter', w:2,
    k:['cover letter','covering letter','sop','statement of purpose','personal statement'],
    a:[
      'Cover letters are part of the profile work, tailored to the roles you are actually applying for rather than one generic template.<br><br>They come bundled with the resume packages from $200. Want an advisor to look at what you have now?',
      'Yes, we handle cover letters alongside the resume rewrite. A good one is short, specific to that employer, and does not just repeat the resume.'
    ] },

  { id:'portfolio', w:2,
    k:['portfolio','github','projects','certifications','certificate','certified','courses i did','aws certified'],
    a:[
      'Certifications and a real project portfolio genuinely move the needle, especially if your experience is thin. We help you decide which ones are worth the time for your target role, and the training programme builds real projects you can show.<br><br>What are you working towards?',
      'Projects and certifications count, but only the ones that match what employers in your target role actually screen for. Part of the consultation is telling you which are worth it and which are not.'
    ],
    chips:['Training','Talk to a human'] },

  { id:'notice_period', w:2,
    k:['notice period','when can i join','joining date','currently working','serving notice','how soon can i start'],
    a:[
      'Notice period is normal and employers plan around it. Tell your recruiter upfront so they only put you forward for roles where the timeline works.<br><br>How long is your notice?',
      'That is worth flagging early. We set expectations with employers from the start so a notice period does not cost you an offer late in the process.'
    ] },

  { id:'contract', w:2,
    k:['contract role','contract job','part time','freelance','temporary','short term','w2 or c2c','full time only'],
    a:[
      'We place into contract, C2C and full-time roles. Contract work often gets you in the door faster and can convert, so it is worth staying open to.<br><br>What is your preference, and is that a hard preference or a flexible one?',
      'Both are on the table. Contract roles usually move quicker, full-time takes longer but gives more stability. Tell your recruiter which you want and they will target accordingly.'
    ] },

  { id:'how_many_jobs', w:2,
    k:['how many jobs','how many applications','how many interviews','how many companies','number of applications'],
    a:[
      'On the recruiter-led packages, up to <b>100 targeted applications a day</b>, with daily activity reports so you can see exactly what went out.<br><br>Interviews depend on your profile and the market. Nobody can promise you a number of interviews, and I will not.',
      'Application volume we control and report on daily. The $4,000 placement track is built around targeting 10 final-round interviews.<br><br>To be straight with you, that is a target we work towards, not a guarantee. Employers decide who they interview.'
    ] },

  { id:'apply_on_behalf', w:4,
    k:['do you apply for me','apply on my behalf','who applies','will you apply','you apply or i apply','do i apply','apply myself'],
    re:/\b(do|will|can)\s+(you|u)\s+apply\b|\bapply\b[^.]{0,12}\b(for|on behalf of)\s+me\b|\bwho\s+(does the )?appl(y|ies|ying)\b/,
    a:[
      'On the recruiter packages, yes, a dedicated recruiter applies on your behalf and coordinates the interviews. You just show up prepared.<br><br>On the resume-only packages you apply yourself, with a much stronger profile.',
      'Depends on the package. From $2,500 a recruiter runs the applications for you daily. Below that we fix your resume and profile and you drive the applications.'
    ],
    chips:['Pricing','Get a recruiter'] },

  { id:'past_client', w:4,
    k:['talk to past client','speak to someone placed','someone you placed','someone placed','placed candidate','past candidate','reference','testimonial from','proof of placement','can i verify'],
    re:/\b(talk|speak|contact|connect|meet)\b[^.]{0,26}\b(placed|past|previous|existing|another|other)\b|\b(someone|anyone|somebody)\b[^.]{0,14}\b(you|u)\s+(have\s+)?placed\b/,
    a:[
      'Reasonable thing to ask before paying anyone. I cannot share client contact details, that would be a privacy breach on them, but the team can talk you through case studies for your industry.<br><br>Client reviews are on our <a href="/#reviews">homepage</a> too. {{both:Hi, can you share case studies for candidates in my field?}}',
      'I will not hand out anyone else\'s details, and you would not want us doing that with yours either. What the team can do is walk you through anonymised examples in your industry. Ask them directly. {{both:Hi, I would like to hear about placements in my field.}}'
    ] },

  { id:'language', w:2,
    k:['hindi','gujarati','telugu','tamil','do you speak','language','english nahi','regional language'],
    a:[
      'I answer in English, but our team speaks Hindi, Gujarati and English, so on a call or WhatsApp you can talk in whichever is comfortable.<br><br>Type your question here in any language and I will do my best. {{both:Hi, I would prefer to talk in Hindi.}}',
      'I stick to English here, but the human team is comfortable in Hindi and Gujarati too. Give them a call and speak however suits you.'
    ] },

  { id:'age', w:2,
    k:['too old','my age','age limit','over 40','over 50','age discrimination','am i too old'],
    a:[
      'There is no age limit on our side. What matters is how current your skills look and how the resume is positioned, and both are fixable.<br><br>I will not pretend age bias does not exist in the market. What we do is put your recent, relevant work front and centre so it is not the first thing anyone sees.',
      'We work with candidates at every stage of their career. Positioning matters more than the number, and that is exactly what the resume and profile work addresses.'
    ] }

  ];

  /* ------------------------------------------------------- hard limits
     Charlie must never do any of these, regardless of how it is asked. */
  var RULES = [
    { id:'credentials',
      k:['my password','card number','cvv','credit card number','ssn','social security','passport number','aadhaar','pan number','otp','bank account number','account number','pin number'],
      a:'Stop right there, please do not type card numbers, passwords, OTPs or ID numbers into any chat, including this one. I do not need them and I will never ask for them.<br><br>Anything involving payment goes through a proper invoice from an advisor. If someone claiming to be from Growx asks you for these in a chat, it is not us.' },

    { id:'legal',
      k:['legal advice','lawyer','attorney','sue','court','lawsuit','is it legal','illegal','contract review'],
      a:'That is a legal question and I am not qualified to answer it, nor is any recruiter. For anything legal, especially immigration, please speak to a licensed attorney.<br><br>On the career side I am happy to help. {{both:Hi, I have a question for an advisor.}}' },

    { id:'fake',
      k:['fake experience','fake resume','fake documents','false experience','lie on resume','make up experience','forged','fake certificate','dummy experience','proxy interview','someone else attend','fake exp','add fake','show fake','fake company','fake project'],
      re:/\b(fake|forge|forged|fabricate|fabricated|falsify|made?\s*up|dummy|bogus)\b.{0,24}\b(experience|exp|resume|cv|document|documents|certificate|certificates|company|project|projects|reference|references|history)\b|\b(experience|resume|cv|document|certificate)\b.{0,16}\b(fake|forged|fabricated)\b|\bproxy\s*(interview|candidate)\b|\b(lie|lying)\b.{0,16}\b(resume|cv|interview|experience)\b/,
      a:'No, we do not do that, and I would not help with it even if you asked differently. Fabricated experience, fake documents and proxy interviews get people fired, blacklisted, and in immigration cases far worse.<br><br>What we do instead is make your <b>real</b> experience land properly. That works, and it does not blow up later. {{both:Hi, I want to strengthen my real profile.}}' },

    { id:'other_company',
      k:['better than','compare with','vs ','which is better','other consultancy','another agency','competitor'],
      a:'I am not going to run down other companies, I only really know ours.<br><br>What I would say is judge any of us on the same test: do they promise you a guaranteed job? If yes, walk away. Ask what they actually commit to in writing.' },

    { id:'personal',
      k:['are you married','your age','where do you live','your family','date me','love you','girlfriend','boyfriend'],
      a:'Ha, I am software, so none of the above. 😄 Back to work though, what can I help you with on the career side?' }
  ];

  /* --------------------------------------------------- fallback ladder */
  var FALLBACK = [
    'I want to get that right rather than guess. Ask me about <b>jobs</b>, <b>pricing</b>, <b>resumes</b>, <b>training</b>, <b>visas</b> or <b>referrals</b>, or let me hand you to a person.{{both:Hi Growx Tech IT, I have a question: }}',
    'That one is outside what I know well. Rather than make something up, let me get a human on it. {{both:Hi, I have a question Charlie could not answer: }}',
    'Still not something I can answer properly, and I would rather say so than fumble it. An advisor will sort it out quickly. {{both:Hi, I need help with something specific: }}'
  ];

  var CLARIFY = [
    'Just so I point you at the right thing, is this about <b>finding a job</b>, <b>our services and prices</b>, or <b>something on your existing file</b>?',
    'Quick check so I do not waste your time, are you asking about <b>openings</b>, <b>what we charge</b>, or <b>how the process works</b>?'
  ];

  /* Synonym expansion, keeps matching forgiving without a huge keyword list */
  var SYN = {
    'cv':'resume', 'resumee':'resume', 'resum':'resume', 'biodata':'resume',
    'job':'job', 'jobs':'job', 'naukri':'job', 'vacancy':'job', 'vacancies':'job', 'opening':'job', 'openings':'job',
    'cost':'price', 'fees':'price', 'fee':'price', 'charges':'price', 'charge':'price', 'rate':'price', 'rates':'price',
    'kitna':'price', 'paisa':'price', 'paise':'price', 'kitne':'price',
    'placement':'placements', 'placed':'placements',
    'usa':'us', 'america':'us', 'united':'us', 'states':'us',
    'h1':'h1b', 'h-1b':'h1b', 'h1-b':'h1b',
    'wfh':'remote', 'workfromhome':'remote',
    'pls':'please', 'plz':'please', 'u':'you', 'ur':'your', 'r':'are', 'thx':'thanks', 'ty':'thanks',
    'hii':'hi', 'hiii':'hi', 'helo':'hello', 'hlo':'hello', 'heyy':'hey',
    'wat':'what', 'wht':'what', 'hw':'how', 'y':'why',
    'trainings':'training', 'course':'training', 'courses':'training', 'classes':'training',
    'interviews':'interview', 'mocks':'mock',
    'sponsorship':'sponsor', 'sponsoring':'sponsor',
    'guaranteed':'guarantee', 'guarantees':'guarantee', 'pakka':'guarantee', 'sure':'guarantee',
    'refering':'refer', 'referring':'refer', 'referal':'referral', 'refrral':'referral',
    'contactno':'contact', 'phoneno':'phone', 'mobile':'phone', 'whatsup':'whatsapp', 'wapp':'whatsapp'
  };

  return { KB: KB, RULES: RULES, FALLBACK: FALLBACK, CLARIFY: CLARIFY, SYN: SYN };
})();
