/* Growx Tech IT — Resume & LinkedIn Score tool.
   Everything here runs client-side. The uploaded PDF's bytes never leave
   the browser; pdf.js (loaded from cdnjs) extracts text locally and the
   scoring below runs on that text. Only the optional follow-up form at
   the bottom sends anything over the network, and it sends an email +
   the score, never the file or its text. */
(function () {
  'use strict';

  var ACTION_VERBS = [
    'led','built','developed','designed','implemented','managed','created','improved',
    'reduced','increased','automated','architected','launched','delivered','optimized',
    'streamlined','spearheaded','collaborated','negotiated','resolved','migrated','deployed',
    'analyzed','engineered','established','executed','drove','authored','directed','mentored',
    'coordinated','integrated','configured','maintained','upgraded','refactored','debugged',
    'tested','documented','trained','onboarded','scaled','accelerated','pioneered','owned',
    'shipped','released','enhanced','simplified','standardized','consolidated','modernized',
    'secured','monitored','audited','forecasted','budgeted','presented','facilitated',
    'supervised','recruited','hired','trained','redesigned','rebuilt','transformed','grew',
    'cut','saved','generated','identified','diagnosed','troubleshot','prototyped'
  ];

  var TECH_KEYWORDS = [
    'java','python','javascript','typescript','c#','.net','c++','react','angular','vue',
    'node.js','node','express','spring','django','flask','sql','mysql','postgresql','mongodb',
    'nosql','aws','azure','gcp','docker','kubernetes','terraform','jenkins','ci/cd','git',
    'github','gitlab','linux','unix','bash','shell','rest api','graphql','microservices',
    'agile','scrum','kanban','jira','confluence','devops','sre','tableau','power bi','excel',
    'salesforce','sap','servicenow','html','css','sass','webpack','redux','spring boot',
    'hibernate','kafka','rabbitmq','elasticsearch','redis','snowflake','airflow','spark',
    'hadoop','machine learning','deep learning','tensorflow','pytorch','nlp','data engineering',
    'data analysis','etl','selenium','junit','cypress','testng','automation testing',
    'manual testing','qa','security','networking','active directory','vmware','citrix',
    'oracle','pl/sql','powershell','ansible','puppet','chef','okta','splunk','datadog',
    'new relic','grafana','prometheus'
  ];

  // ---------- PDF text extraction (client-side only) ----------

  function extractLines(arrayBuffer) {
    return pdfjsLib.getDocument({ data: arrayBuffer }).promise.then(function (pdf) {
      var pagePromises = [];
      for (var i = 1; i <= pdf.numPages; i++) {
        pagePromises.push(pdf.getPage(i).then(function (page) {
          return page.getTextContent().then(function (content) {
            var buckets = [];
            content.items.forEach(function (item) {
              var y = Math.round(item.transform[5] / 2.5);
              var bucket = buckets.filter(function (b) { return Math.abs(b.y - y) <= 1; })[0];
              if (!bucket) { bucket = { y: y, parts: [] }; buckets.push(bucket); }
              bucket.parts.push({ x: item.transform[4], str: item.str });
            });
            buckets.sort(function (a, b) { return b.y - a.y; });
            return buckets.map(function (b) {
              b.parts.sort(function (p1, p2) { return p1.x - p2.x; });
              return b.parts.map(function (p) { return p.str; }).join(' ').replace(/\s+/g, ' ').trim();
            }).filter(Boolean);
          });
        }));
      }
      return Promise.all(pagePromises).then(function (pages) {
        var lines = [];
        pages.forEach(function (p) { lines = lines.concat(p); });
        return { lines: lines, numPages: pdf.numPages };
      });
    });
  }

  function countMatches(text, list) {
    var lower = text.toLowerCase();
    var found = [];
    list.forEach(function (kw) {
      var escaped = kw.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      var re = new RegExp('(^|[^a-z0-9])' + escaped + '([^a-z0-9]|$)', 'i');
      if (re.test(lower)) found.push(kw);
    });
    return found;
  }

  function isBulletLine(line) {
    var t = line.trim();
    if (t.length < 15 || t.length > 260) return false;
    if (/@/.test(t)) return false; // contact line
    var startsVerb = startsWithVerb(t);
    // a bare year or year-range (job/education header line) is only a real
    // bullet if it also reads like an achievement statement
    if (/\b(19|20)\d{2}\b/.test(t) && !startsVerb) return false;
    // dense comma lists without a leading verb are skills/qualifications
    // lists, not achievement bullets
    if (t.split(',').length >= 4 && !startsVerb) return false;
    return true;
  }

  function startsWithVerb(line) {
    var t = line.trim().replace(/^[-•*•●▪–—]\s*/, '');
    var m = t.match(/^[A-Za-z']+/);
    if (!m) return false;
    return ACTION_VERBS.indexOf(m[0].toLowerCase()) !== -1;
  }

  function hasNumber(line) {
    return /\d|%|\$/.test(line);
  }

  function clampScore(n, max) { return Math.max(0, Math.min(max, Math.round(n))); }

  function sectionResult(name, score, max, notes) {
    return { name: name, score: clampScore(score, max), max: max, notes: notes };
  }

  // ---------- Resume scoring ----------

  function scoreResume(allLines) {
    var text = allLines.join('\n');
    var wordCount = (text.match(/\S+/g) || []).length;
    var sections = [];

    // 1. Contact & links (10)
    var hasEmail = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/i.test(text);
    var hasPhone = /(\+?\d{1,3}[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}/.test(text);
    var hasLinkedin = /linkedin\.com\/in\//i.test(text);
    var contactScore = (hasEmail ? 4 : 0) + (hasPhone ? 3 : 0) + (hasLinkedin ? 3 : 0);
    var contactNotes = [];
    contactNotes.push({ ok: hasEmail, text: hasEmail ? 'Email address found' : 'No email address found. Recruiters need a direct way to reach you' });
    contactNotes.push({ ok: hasPhone, text: hasPhone ? 'Phone number found' : 'No phone number detected' });
    contactNotes.push({ ok: hasLinkedin, text: hasLinkedin ? 'LinkedIn profile link found' : 'No LinkedIn profile link found. Add one near your contact info' });
    sections.push(sectionResult('Contact & Links', contactScore, 10, contactNotes));

    // 2. Length (10)
    var lengthScore, lengthNote;
    if (wordCount >= 350 && wordCount <= 800) { lengthScore = 10; lengthNote = { ok: true, text: wordCount + ' words, a solid, scannable length' }; }
    else if (wordCount >= 250 && wordCount < 350 || wordCount > 800 && wordCount <= 1000) { lengthScore = 7; lengthNote = { ok: false, text: wordCount + ' words, a bit ' + (wordCount < 350 ? 'short' : 'long') + ' for most recruiter skim-reading' }; }
    else { lengthScore = 4; lengthNote = { ok: false, text: wordCount + ' words. ' + (wordCount < 250 ? 'Likely too thin to show real impact' : 'Likely too long; aim for 1-2 pages') }; }
    sections.push(sectionResult('Length', lengthScore, 10, [lengthNote]));

    // bullet-like lines, shared by action verbs + quantification
    var bulletLines = allLines.filter(isBulletLine);
    var verbHits = bulletLines.filter(startsWithVerb);
    var numberHits = bulletLines.filter(hasNumber);

    // 3. Action verbs (20)
    var verbRatio = bulletLines.length ? verbHits.length / bulletLines.length : 0;
    var verbScore = bulletLines.length ? verbRatio * 20 : 0;
    sections.push(sectionResult('Action Verbs', verbScore, 20, [
      bulletLines.length
        ? { ok: verbRatio >= 0.5, text: verbHits.length + ' of ' + bulletLines.length + ' bullet-style lines start with a strong action verb (Led, Built, Reduced, ...)' }
        : { ok: false, text: 'Could not find clear bullet points to check' }
    ]));

    // 4. Quantified achievements (20)
    var numRatio = bulletLines.length ? numberHits.length / bulletLines.length : 0;
    var numScore = bulletLines.length ? numRatio * 20 : 0;
    sections.push(sectionResult('Quantified Achievements', numScore, 20, [
      bulletLines.length
        ? { ok: numRatio >= 0.4, text: numberHits.length + ' of ' + bulletLines.length + ' lines include a number, %, or $ amount' }
        : { ok: false, text: 'No measurable results detected. Numbers make impact concrete' }
    ]));

    // 5. Skills coverage (15)
    var techFound = countMatches(text, TECH_KEYWORDS);
    var skillsScore = Math.min(techFound.length, 15) / 15 * 15;
    sections.push(sectionResult('Skills Coverage', skillsScore, 15, [
      { ok: techFound.length >= 8, text: techFound.length + ' recognizable IT/tech skills found' + (techFound.length ? ' (' + techFound.slice(0, 8).join(', ') + (techFound.length > 8 ? ', ...' : '') + ')' : '') }
    ]));

    // 6. Section structure (15)
    var hasExp = /\b(work experience|professional experience|experience)\b/i.test(text);
    var hasEdu = /\beducation\b/i.test(text);
    var hasSkillsSection = /\bskills\b/i.test(text);
    var structScore = (hasExp ? 5 : 0) + (hasEdu ? 5 : 0) + (hasSkillsSection ? 5 : 0);
    sections.push(sectionResult('Section Structure', structScore, 15, [
      { ok: hasExp, text: hasExp ? 'Experience section found' : 'No clear "Experience" heading found' },
      { ok: hasEdu, text: hasEdu ? 'Education section found' : 'No clear "Education" heading found' },
      { ok: hasSkillsSection, text: hasSkillsSection ? 'Skills section found' : 'No clear "Skills" heading found' }
    ]));

    // 7. ATS extractability (10) — looks for signs of multi-column/table
    // layouts that fragment text extraction, independent of word count
    var shortLineCount = allLines.filter(function (l) { return (l.match(/\S+/g) || []).length <= 2; }).length;
    var fragRatio = allLines.length ? shortLineCount / allLines.length : 1;
    var clean = fragRatio <= 0.5;
    var atsScore = clean ? 10 : 3;
    sections.push(sectionResult('ATS Extractability', atsScore, 10, [
      clean
        ? { ok: true, text: 'Text extracted as clean, continuous lines, a good sign a real ATS can parse it too' }
        : { ok: false, text: 'Many lines extracted as just 1-2 words. Likely columns, tables, or text boxes in your layout, which often confuse real ATS parsers too' }
    ]));

    return { sections: sections, meta: { wordCount: wordCount } };
  }

  // ---------- LinkedIn PDF scoring ----------

  function sliceBetween(lines, startRe, endRes) {
    var startIdx = -1;
    for (var i = 0; i < lines.length; i++) { if (startRe.test(lines[i])) { startIdx = i; break; } }
    if (startIdx === -1) return null;
    var endIdx = lines.length;
    for (var j = startIdx + 1; j < lines.length; j++) {
      if (endRes.some(function (re) { return re.test(lines[j]); })) { endIdx = j; break; }
    }
    return lines.slice(startIdx + 1, endIdx);
  }

  function scoreLinkedin(allLines) {
    var text = allLines.join('\n');
    var sections = [];

    var HEAD_RES = {
      about: /^about$/i,
      experience: /^experience$/i,
      education: /^education$/i,
      skills: /^(skills|skills\s*&\s*endorsements)$/i,
      licenses: /^licenses?\s*&?\s*certifications?$/i
    };
    var allHeadRes = [HEAD_RES.about, HEAD_RES.experience, HEAD_RES.education, HEAD_RES.skills, HEAD_RES.licenses, /^contact$/i, /^summary$/i];

    // Headline: first few non-empty lines before "About" (name is usually line 0-1)
    var aboutIdx = allLines.findIndex(function (l) { return HEAD_RES.about.test(l); });
    var headlineCandidates = allLines.slice(1, aboutIdx > 0 ? aboutIdx : 6).filter(function (l) { return l.trim().length > 0; });
    var headline = headlineCandidates[0] || '';
    var headlineWords = (headline.match(/\S+/g) || []).length;
    var headlineTechHits = countMatches(headline, TECH_KEYWORDS);
    var genericHeadline = /^(student at|looking for|open to work|seeking)/i.test(headline.trim());
    var headlineScore = (headlineWords >= 6 && headlineWords <= 30 ? 7 : 3) + (headlineTechHits.length ? 8 : (genericHeadline ? 0 : 3));
    sections.push(sectionResult('Headline', headlineScore, 15, [
      { ok: headlineWords >= 6, text: headline ? ('Headline: "' + headline + '"') : 'No headline text detected right under your name' },
      { ok: headlineTechHits.length > 0, text: headlineTechHits.length ? 'Includes a recognizable role/skill keyword' : 'Consider adding a specific role or skill, not just a job title' },
      genericHeadline ? { ok: false, text: 'Reads as generic ("Student at...", "Looking for...") - lead with what you actually do' } : null
    ].filter(Boolean)));

    // About
    var aboutLines = sliceBetween(allLines, HEAD_RES.about, allHeadRes) || [];
    var aboutText = aboutLines.join(' ');
    var aboutWords = (aboutText.match(/\S+/g) || []).length;
    var aboutTechHits = countMatches(aboutText, TECH_KEYWORDS);
    var aboutScore = aboutWords === 0 ? 0 : (aboutWords >= 100 ? 12 : 6) + Math.min(8, aboutTechHits.length);
    sections.push(sectionResult('About', aboutScore, 20, [
      aboutWords === 0
        ? { ok: false, text: 'No "About" section found. This is one of the most-read parts of a profile' }
        : { ok: aboutWords >= 100, text: aboutWords + ' words in your About section' + (aboutWords < 100 ? ', aim for 100+ to tell a real story' : '') },
      aboutWords ? { ok: aboutTechHits.length >= 5, text: aboutTechHits.length + ' recognizable skill keyword' + (aboutTechHits.length === 1 ? '' : 's') + ' mentioned in About' } : null
    ].filter(Boolean)));

    // Experience
    var expLines = sliceBetween(allLines, HEAD_RES.experience, allHeadRes) || [];
    var expText = expLines.join('\n');
    var dateRangeHits = (expText.match(/\b(19|20)\d{2}\b/g) || []).length;
    var expBullets = expLines.filter(isBulletLine);
    var expVerbHits = expBullets.filter(startsWithVerb);
    var expNumHits = expBullets.filter(hasNumber);
    var entryEstimate = Math.max(1, Math.round(dateRangeHits / 2));
    var entryScore = Math.min(10, entryEstimate * 4);
    var expVerbRatio = expBullets.length ? expVerbHits.length / expBullets.length : 0;
    var expNumRatio = expBullets.length ? expNumHits.length / expBullets.length : 0;
    var expScore = (expLines.length === 0 ? 0 : entryScore) + expVerbRatio * 8 + expNumRatio * 7;
    sections.push(sectionResult('Experience', expScore, 25, [
      expLines.length === 0
        ? { ok: false, text: 'No "Experience" section found' }
        : { ok: entryEstimate >= 2, text: '~' + entryEstimate + ' role(s) detected with descriptions' },
      expBullets.length ? { ok: expVerbRatio >= 0.5, text: expVerbHits.length + ' of ' + expBullets.length + ' description lines start with a strong action verb' } : null,
      expBullets.length ? { ok: expNumRatio >= 0.3, text: expNumHits.length + ' of ' + expBullets.length + ' description lines include a measurable result' } : null
    ].filter(Boolean)));

    // Skills
    var skillsLines = sliceBetween(allLines, HEAD_RES.skills, allHeadRes) || [];
    var skillTokens = skillsLines.filter(function (l) { return l.trim().length >= 2 && l.trim().length <= 40; });
    var skillsCount = skillTokens.length;
    var skillsScore = skillsCount >= 15 ? 15 : skillsCount >= 10 ? 11 : skillsCount >= 5 ? 7 : skillsCount > 0 ? 3 : 0;
    sections.push(sectionResult('Skills', skillsScore, 15, [
      { ok: skillsCount >= 10, text: skillsCount ? (skillsCount + ' skills listed') : 'No Skills section detected' }
    ]));

    // Education
    var eduLines = sliceBetween(allLines, HEAD_RES.education, allHeadRes) || [];
    var eduScore = eduLines.length > 0 ? 10 : 0;
    sections.push(sectionResult('Education', eduScore, 10, [
      { ok: eduLines.length > 0, text: eduLines.length > 0 ? 'Education section found' : 'No "Education" section found' }
    ]));

    // Completeness
    var hasLicenses = HEAD_RES.licenses.test(allLines.join('|')) || allLines.some(function (l) { return HEAD_RES.licenses.test(l); });
    var completenessParts = [headline.length > 0, aboutWords > 0, expLines.length > 0, skillsCount > 0, hasLicenses];
    var completenessScore = completenessParts.filter(Boolean).length * 3;
    sections.push(sectionResult('Completeness', completenessScore, 15, [
      { ok: completenessScore >= 12, text: completenessParts.filter(Boolean).length + ' of 5 major profile sections present (Headline, About, Experience, Skills, Certifications)' }
    ]));

    return { sections: sections, meta: { headline: headline } };
  }

  function overallFrom(sections) {
    var total = 0, max = 0;
    sections.forEach(function (s) { total += s.score; max += s.max; });
    return Math.round((total / max) * 100);
  }

  function verdictFor(score) {
    if (score >= 85) return { h: 'Strong, just polish from here', s: 'Your file hits most of the marks recruiters and ATS systems look for. The notes below are refinements, not fixes.' };
    if (score >= 65) return { h: 'Good bones, but a few real gaps', s: 'You\'re most of the way there. Closing the gaps below should meaningfully improve response rates.' };
    if (score >= 40) return { h: 'Several gaps are likely costing you interviews', s: 'This is fixable, but in its current state it\'s probably losing you chances before a human even reads it.' };
    return { h: 'This needs a real rebuild', s: 'Multiple core pieces recruiters and ATS systems expect are missing or hard to detect. Worth rebuilding rather than patching.' };
  }

  // ---------- UI wiring ----------

  var mode = 'resume';
  var modeResumeBtn = document.getElementById('raModeResume');
  var modeLinkedinBtn = document.getElementById('raModeLinkedin');
  var howto = document.getElementById('raLinkedinHow');
  var dropText = document.getElementById('raDropText');
  var drop = document.getElementById('raDrop');
  var fileInput = document.getElementById('raFile');
  var statusEl = document.getElementById('raStatus');
  var resultsEl = document.getElementById('raResults');
  var ring = document.getElementById('raRing');
  var scoreEl = document.getElementById('raScore');
  var headlineEl = document.getElementById('raHeadline');
  var subEl = document.getElementById('raSub');
  var sectionsEl = document.getElementById('raSections');
  var followupForm = document.getElementById('raFollowupForm');
  var followupEmail = document.getElementById('raFollowupEmail');
  var followupNote = document.getElementById('raFollowupNote');
  var lastResult = null;

  function setMode(m) {
    mode = m;
    modeResumeBtn.classList.toggle('active', m === 'resume');
    modeResumeBtn.setAttribute('aria-selected', m === 'resume');
    modeLinkedinBtn.classList.toggle('active', m === 'linkedin');
    modeLinkedinBtn.setAttribute('aria-selected', m === 'linkedin');
    howto.hidden = m !== 'linkedin';
    dropText.textContent = m === 'linkedin' ? 'Drop your LinkedIn PDF here' : 'Drop your resume PDF here';
  }
  modeResumeBtn.addEventListener('click', function () { setMode('resume'); });
  modeLinkedinBtn.addEventListener('click', function () { setMode('linkedin'); });

  drop.addEventListener('click', function () { fileInput.click(); });
  drop.addEventListener('dragover', function (e) { e.preventDefault(); drop.classList.add('dragover'); });
  drop.addEventListener('dragleave', function () { drop.classList.remove('dragover'); });
  drop.addEventListener('drop', function (e) {
    e.preventDefault();
    drop.classList.remove('dragover');
    if (e.dataTransfer.files && e.dataTransfer.files[0]) handleFile(e.dataTransfer.files[0]);
  });
  fileInput.addEventListener('change', function () {
    if (fileInput.files && fileInput.files[0]) handleFile(fileInput.files[0]);
  });

  function showStatus(msg, isError) {
    statusEl.hidden = false;
    statusEl.textContent = msg;
    statusEl.classList.toggle('ra-error', !!isError);
    resultsEl.hidden = true;
  }

  function handleFile(file) {
    if (file.type !== 'application/pdf' && !/\.pdf$/i.test(file.name)) {
      showStatus('Please upload a PDF file.', true);
      return;
    }
    if (file.size > 15 * 1024 * 1024) {
      showStatus('That file is larger than 15MB. Please upload a standard resume/LinkedIn PDF export.', true);
      return;
    }
    if (!window.pdfjsLib) {
      showStatus('The PDF reader did not load. Please refresh the page and try again.', true);
      return;
    }
    showStatus('Reading your PDF locally in your browser...');
    var reader = new FileReader();
    reader.onload = function () {
      extractLines(reader.result).then(function (data) {
        if (data.lines.join('').trim().length < 40) {
          showStatus('We could not read enough text from this PDF. If it\'s a scanned image, try exporting a text-based PDF instead (e.g. from Word, Google Docs, or LinkedIn\'s "Save to PDF").', true);
          return;
        }
        var result = mode === 'linkedin' ? scoreLinkedin(data.lines) : scoreResume(data.lines);
        renderResults(result);
      }).catch(function (err) {
        showStatus('Something went wrong reading that PDF. Please try a different export of the file.', true);
      });
    };
    reader.onerror = function () { showStatus('Could not read that file. Please try again.', true); };
    reader.readAsArrayBuffer(file);
  }

  function renderResults(result) {
    statusEl.hidden = true;
    var score = overallFrom(result.sections);
    lastResult = { mode: mode, score: score };

    ring.style.setProperty('--pct', score);
    var hue = score >= 65 ? 150 : score >= 40 ? 32 : 4;
    ring.style.setProperty('--hue', hue);
    scoreEl.textContent = score;

    var v = verdictFor(score);
    headlineEl.textContent = v.h;
    subEl.textContent = v.s;

    sectionsEl.innerHTML = '';
    result.sections.forEach(function (s) {
      var card = document.createElement('div');
      card.className = 'ra-section';
      var pct = Math.round((s.score / s.max) * 100);
      var notesHtml = s.notes.map(function (n) {
        return '<li class="' + (n.ok ? 'ra-good' : 'ra-warn') + '">' + escapeHtml(n.text) + '</li>';
      }).join('');
      card.innerHTML =
        '<div class="ra-section-head"><h4>' + escapeHtml(s.name) + '</h4><b>' + s.score + ' / ' + s.max + '</b></div>' +
        '<div class="progress-box"><div class="progress-track"><div class="progress-fill" style="width:' + pct + '%"></div></div></div>' +
        '<ul>' + notesHtml + '</ul>';
      sectionsEl.appendChild(card);
    });

    resultsEl.hidden = false;
    resultsEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  if (followupForm) {
    followupForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = followupEmail.value.trim();
      if (!email || !lastResult) return;
      if (window.GX && GX.submitLead) {
        GX.submitLead({
          type: 'resume_linkedin_score_followup',
          email: email,
          mode: lastResult.mode,
          overall_score: lastResult.score
        });
      }
      followupForm.hidden = true;
      followupNote.hidden = false;
      followupNote.textContent = 'Got it. A real recruiter will take a look and follow up.';
    });
  }

  setMode('resume');
})();
