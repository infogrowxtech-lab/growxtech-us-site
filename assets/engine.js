/* Growx Career Engine — free resume check.
   Runs entirely in the visitor's browser. The resume text is never uploaded
   anywhere. Only the score and the role they type are ever sent, and only
   when they choose to hand their details over. */
(function () {
  var box = document.getElementById('engine');
  if (!box) return;

  var ta      = document.getElementById('rzText');
  var fileEl  = document.getElementById('rzFile');
  var fileLbl = document.getElementById('rzFileLabel');
  var fileBtn = document.querySelector('.rz-file-btn');
  var goBtn   = document.getElementById('rzGo');
  var intro   = document.getElementById('engineIntro');
  var result  = document.getElementById('engineResult');
  var scoreEl = document.getElementById('rzScore');
  var ringEl  = document.getElementById('rzRing');
  var verdict = document.getElementById('rzVerdict');
  var listEl  = document.getElementById('rzList');
  var againBt = document.getElementById('rzAgain');
  var fixBtn  = document.getElementById('rzFix');

  var ACTION_VERBS = ['built','led','shipped','designed','launched','delivered','owned','drove','grew',
    'reduced','improved','automated','migrated','scaled','architected','implemented','optimized',
    'optimised','created','developed','managed','negotiated','resolved','streamlined','cut','raised',
    'trained','mentored','rebuilt','deployed','integrated','achieved','increased','decreased','saved',
    'generated','established','launched','coordinated','analyzed','analysed','initiated','restructured'];

  var WEAK = ['responsible for','duties included','worked on','helped with','involved in',
    'assisted with','tasked with','participated in','was part of','in charge of','handled various'];

  var FLUFF = ['hardworking','hard working','team player','go-getter','go getter','synergy',
    'think outside the box','result oriented','results oriented','self motivated','self-motivated',
    'detail oriented','detail-oriented','dynamic professional','passionate about','proven track record',
    'excellent communication skills','fast learner','multitasking','win-win','thought leader'];

  function count(hay, needles) {
    var n = 0;
    for (var i = 0; i < needles.length; i++) {
      var re = new RegExp('\\b' + needles[i].replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&') + '\\b', 'g');
      var m = hay.match(re);
      if (m) n += m.length;
    }
    return n;
  }

  function analyse(raw) {
    var text  = raw.toLowerCase();
    var words = raw.trim().split(/\s+/).filter(Boolean);
    var wc    = words.length;
    var lines = raw.split(/\n+/).map(function (l) { return l.trim(); }).filter(Boolean);
    var items = [];
    var score = 0;

    /* 1. contact details, 10 */
    var hasEmail = /[^\s@]+@[^\s@]+\.[^\s@]{2,}/.test(raw);
    var hasPhone = /(\+?\d[\d\s().-]{7,}\d)/.test(raw);
    if (hasEmail && hasPhone) {
      score += 10;
      items.push(['ok', 'Contact details', 'Email and phone are both there. Recruiters can actually reach you.']);
    } else {
      score += hasEmail || hasPhone ? 5 : 0;
      items.push(['bad', 'Contact details',
        'Missing ' + (!hasEmail && !hasPhone ? 'email and phone' : (!hasEmail ? 'an email address' : 'a phone number')) +
        '. Put both at the very top, on one line.']);
    }

    /* 2. length, 10 */
    if (wc < 180) {
      items.push(['bad', 'Length', 'Only ' + wc + ' words. That is too thin to survive a screen. Aim for 400 to 800.']);
    } else if (wc > 1200) {
      score += 4;
      items.push(['warn', 'Length', wc + ' words is long. Recruiters skim for 7 seconds. Cut to the last 10 years and the strongest work.']);
    } else if (wc < 350) {
      score += 6;
      items.push(['warn', 'Length', wc + ' words is on the short side. Add detail on outcomes, not more job titles.']);
    } else {
      score += 10;
      items.push(['ok', 'Length', wc + ' words. That is a sensible length for a screen.']);
    }

    /* 3. quantified results, 20, the single biggest signal */
    var UNITS = '%|percent|k\\b|m\\b|bn|million|billion|lakh|crore|x\\b|' +
      'users|customers|clients|members|people|employees|engineers|students|candidates|' +
      'requests|transactions|records|tickets|calls|queries|orders|leads|accounts|' +
      'projects|releases|deploys|reports|articles|campaigns|stores|sites|servers|services|' +
      'hours?|days?|weeks?|months?|years?|minutes?|seconds?|qtr|quarters?';
    var numbers = (raw.match(new RegExp('\\b\\d[\\d,]*(\\.\\d+)?\\s?(' + UNITS + ')', 'gi')) || []).length;
    var money   = (raw.match(/[$₹£€]\s?\d/g) || []).length;
    /* a big bare number in a resume is almost always a result, but a year is not */
    var bigNums = (raw.match(/\b\d[\d,]{2,}\b/g) || []).filter(function (n) {
      return !/^(19|20)\d{2}$/.test(n.replace(/,/g, ''));
    }).length;
    var plusNums = (raw.match(/\b\d+\+/g) || []).length;
    var metrics = numbers + money + bigNums + plusNums;
    if (metrics >= 6) {
      score += 20;
      items.push(['ok', 'Measurable results', metrics + ' quantified results found. This is what separates a strong resume from a job description.']);
    } else if (metrics >= 2) {
      score += 11;
      items.push(['warn', 'Measurable results',
        'Only ' + metrics + ' numbers in the whole resume. Put a figure on your work: "cut load time 40%", "handled 200 tickets a month".']);
    } else {
      items.push(['bad', 'Measurable results',
        'No measurable results. This is the biggest single fix here. Every role should carry at least two numbers, a percentage, an amount, a volume or a timeframe.']);
    }

    /* 4. action verbs, 15 */
    var verbs = count(text, ACTION_VERBS);
    if (verbs >= 8) {
      score += 15;
      items.push(['ok', 'Strong verbs', 'Good use of action verbs. Your bullets read as things you did, not things you were near.']);
    } else if (verbs >= 3) {
      score += 8;
      items.push(['warn', 'Strong verbs', 'Some action verbs, but not enough. Start every bullet with one: built, led, cut, shipped, negotiated.']);
    } else {
      items.push(['bad', 'Strong verbs', 'Almost no action verbs. Rewrite bullets to open with what you did, not what you were assigned.']);
    }

    /* 5. weak phrasing, 15 */
    var weak = count(text, WEAK);
    if (weak === 0) {
      score += 15;
      items.push(['ok', 'Phrasing', 'No "responsible for" style filler. Good.']);
    } else if (weak <= 2) {
      score += 8;
      items.push(['warn', 'Phrasing', weak + ' weak phrase' + (weak > 1 ? 's' : '') + ' like "responsible for" or "worked on". Swap them for the actual verb.']);
    } else {
      score += 2;
      items.push(['bad', 'Phrasing', weak + ' weak phrases such as "responsible for" and "involved in". These describe a job description, not your contribution.']);
    }

    /* 6. skills section, 10 */
    /* must look like a section heading, "excellent communication skills" is not one */
    var skillsHead = /^\s*[•\-*]?\s*(technical\s+|core\s+|key\s+|professional\s+)?(skills|competencies|technologies|tech\s+stack|toolset|tools\s*&?\s*technologies)\s*:?\s*$/im.test(raw)
      || /^\s*[•\-*]?\s*(technical\s+)?(skills|technologies|tech\s+stack)\s*[:\-–]/im.test(raw);
    if (skillsHead) {
      score += 10;
      items.push(['ok', 'Skills section', 'A skills section is present. This is what most keyword filters read first.']);
    } else {
      items.push(['bad', 'Skills section', 'No skills section found. ATS filters match against this. Add one near the top with the exact terms from your target job ads.']);
    }

    /* 7. education, 5 */
    if (/\b(education|academics|qualification|bachelor|master|doctorate|phd|diploma|b\.?tech|m\.?tech|b\.?e\.?|m\.?e\.?|b\.?sc|m\.?sc|b\.?com|m\.?com|b\.?a\.?|m\.?a\.?|mba|bba|bca|mca|degree|university|college|institute)\b/i.test(raw)) {
      score += 5;
      items.push(['ok', 'Education', 'Education is listed.']);
    } else {
      items.push(['warn', 'Education', 'No education section found. Even a single line matters, many filters check for it.']);
    }

    /* 8. dates, 10 */
    var years = (raw.match(/\b(19|20)\d{2}\b/g) || []).length;
    if (years >= 4) {
      score += 10;
      items.push(['ok', 'Timeline', 'Clear dates on your roles. Recruiters can follow your history.']);
    } else if (years >= 2) {
      score += 6;
      items.push(['warn', 'Timeline', 'Only a few dates. Give every role a month and year range, gaps look worse when the dates are vague.']);
    } else {
      items.push(['bad', 'Timeline', 'No clear dates. A resume without a timeline reads as something to hide, even when there is nothing to hide.']);
    }

    /* 9. fluff, 5 */
    var fluff = count(text, FLUFF);
    if (fluff === 0) {
      score += 5;
      items.push(['ok', 'No filler', 'No "team player" style filler. Every line is earning its space.']);
    } else {
      score += 1;
      items.push(['warn', 'Filler words', fluff + ' filler phrase' + (fluff > 1 ? 's' : '') + ' like "team player" or "hardworking". Nobody writes the opposite, so they say nothing. Delete them and use the space for a result.']);
    }

    /* extra observations, no score attached */
    var allCaps = lines.filter(function (l) { return l.length > 25 && l === l.toUpperCase(); }).length;
    if (allCaps > 2) {
      items.push(['warn', 'Formatting', 'Several lines are in full capitals. It reads as shouting and some parsers mangle it.']);
    }
    if (/\bi\s+am\b|\bmy\s+objective\b|\bcareer\s+objective\b/i.test(raw)) {
      items.push(['warn', 'Objective statement', 'An "objective" paragraph mostly wastes the best space on the page. Replace it with a two-line summary of what you deliver.']);
    }

    /* order: problems first, that is what they came for */
    var rank = { bad: 0, warn: 1, ok: 2 };
    items.sort(function (a, b) { return rank[a[0]] - rank[b[0]]; });

    return { score: Math.max(0, Math.min(100, Math.round(score))), items: items, words: wc };
  }

  function verdictFor(s) {
    if (s >= 80) return ['Strong', 'This would survive most screens. The gap is likely reach, not the resume, our recruiters are the fix for that.'];
    if (s >= 60) return ['Decent, with real gaps', 'The bones are fine. Fix the items marked red and this moves up a tier.'];
    if (s >= 40) return ['Needs work', 'This is probably why applications go quiet. The problems below are all fixable.'];
    return ['This is costing you interviews', 'Not a comment on your ability. It is a presentation problem, and it is the easiest one to fix.'];
  }

  function render(res) {
    var v = verdictFor(res.score);
    scoreEl.textContent = res.score;
    verdict.innerHTML = '<b>' + v[0] + '</b><span>' + v[1] + '</span>';

    var hue = res.score >= 80 ? 152 : res.score >= 60 ? 45 : res.score >= 40 ? 32 : 8;
    ringEl.style.setProperty('--pct', res.score);
    ringEl.style.setProperty('--hue', hue);

    listEl.innerHTML = res.items.map(function (it) {
      return '<li class="rz-' + it[0] + '"><span class="rz-dot"></span>' +
             '<div><b>' + it[1] + '</b><span>' + it[2] + '</span></div></li>';
    }).join('');

    intro.hidden = true;
    result.hidden = false;
    box.dataset.state = 'result';

    /* carry the score into the chat so an advisor has context, the resume text never leaves */
    fixBtn.setAttribute('data-grobo',
      'Hi, I ran the free resume check and scored ' + res.score + ' out of 100. I would like it rewritten.');

    try { localStorage.setItem('gx_rz_score', String(res.score)); } catch (e) {}
  }

  /* Direct file upload for the resume text. Everything happens in the browser:
     .txt is read locally with FileReader, .pdf/.docx are parsed locally with
     pdf.js / mammoth.js (fetched from a CDN only for the library code itself,
     never for the resume). The extracted text never leaves the device. */
  var LIB_URLS = {
    pdfjs:       'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js',
    pdfjsWorker: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js',
    mammoth:     'https://cdnjs.cloudflare.com/ajax/libs/mammoth/1.6.0/mammoth.browser.min.js'
  };
  var loadedLibs = {};

  function loadScript(url) {
    if (loadedLibs[url]) return loadedLibs[url];
    loadedLibs[url] = new Promise(function (resolve, reject) {
      var s = document.createElement('script');
      s.src = url;
      s.onload = resolve;
      s.onerror = function () { reject(new Error('Could not load ' + url)); };
      document.head.appendChild(s);
    });
    return loadedLibs[url];
  }

  function setFileHint(msg, isError) {
    var hint = document.getElementById('rzHint');
    if (!hint) return;
    hint.textContent = msg;
    hint.classList.toggle('rz-hint-error', !!isError);
  }

  function setFileState(label, ok) {
    if (fileLbl) fileLbl.textContent = label;
    if (fileBtn) fileBtn.classList.toggle('has-file', !!ok);
  }

  function readAsText(file) {
    return new Promise(function (resolve, reject) {
      var r = new FileReader();
      r.onload = function () { resolve(r.result); };
      r.onerror = function () { reject(r.error); };
      r.readAsText(file);
    });
  }

  function readAsArrayBuffer(file) {
    return new Promise(function (resolve, reject) {
      var r = new FileReader();
      r.onload = function () { resolve(r.result); };
      r.onerror = function () { reject(r.error); };
      r.readAsArrayBuffer(file);
    });
  }

  function extractPdf(file) {
    return loadScript(LIB_URLS.pdfjs).then(function () {
      window.pdfjsLib.GlobalWorkerOptions.workerSrc = LIB_URLS.pdfjsWorker;
      return readAsArrayBuffer(file);
    }).then(function (buf) {
      return window.pdfjsLib.getDocument({ data: buf }).promise;
    }).then(function (pdf) {
      var pages = [];
      var chain = Promise.resolve();
      var _loop = function (i) {
        chain = chain.then(function () {
          return pdf.getPage(i).then(function (page) {
            return page.getTextContent();
          }).then(function (content) {
            pages.push(content.items.map(function (it) { return it.str; }).join(' '));
          });
        });
      };
      for (var i = 1; i <= pdf.numPages; i++) _loop(i);
      return chain.then(function () { return pages.join('\n\n'); });
    });
  }

  function extractDocx(file) {
    return loadScript(LIB_URLS.mammoth).then(function () {
      return readAsArrayBuffer(file);
    }).then(function (buf) {
      return window.mammoth.extractRawText({ arrayBuffer: buf });
    }).then(function (res) { return res.value; });
  }

  if (fileEl) {
    fileEl.addEventListener('change', function () {
      var file = fileEl.files && fileEl.files[0];
      if (!file) return;

      var name = file.name || '';
      var ext = (name.split('.').pop() || '').toLowerCase();
      setFileState('Reading ' + name + '…', false);
      if (fileBtn) fileBtn.classList.add('is-busy');

      var task;
      if (ext === 'txt') {
        task = readAsText(file);
      } else if (ext === 'pdf') {
        task = extractPdf(file);
      } else if (ext === 'doc' || ext === 'docx') {
        task = extractDocx(file);
      } else {
        task = Promise.reject(new Error('unsupported'));
      }

      task.then(function (text) {
        text = (text || '').trim();
        if (!text) throw new Error('empty');
        ta.value = text;
        setFileState(name, true);
        setFileHint('🔒 Loaded from ' + name + ', still only on your device. Nothing was uploaded.', false);
      }).catch(function (err) {
        setFileState('Or upload a file (.pdf, .docx, .txt)', false);
        var msg = (err && err.message === 'unsupported')
          ? 'That file type is not supported, please paste the text instead.'
          : 'Could not read that file automatically, please paste the resume text instead.';
        setFileHint('⚠️ ' + msg, true);
      }).finally(function () {
        if (fileBtn) fileBtn.classList.remove('is-busy');
        fileEl.value = '';
      });
    });
  }

  goBtn.addEventListener('click', function () {
    var raw = (ta.value || '').trim();
    if (raw.split(/\s+/).filter(Boolean).length < 40) {
      ta.focus();
      ta.classList.add('rz-shake');
      setTimeout(function () { ta.classList.remove('rz-shake'); }, 500);
      var hint = document.getElementById('rzHint');
      if (hint) hint.textContent = 'Paste a bit more of it, at least a few lines, or the score will not mean anything.';
      return;
    }
    goBtn.disabled = true;
    goBtn.textContent = 'Reading it…';
    setTimeout(function () {
      render(analyse(raw));
      goBtn.disabled = false;
      goBtn.textContent = 'Check my resume';
    }, 650);
  });

  ta.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key === 'Enter') goBtn.click();
  });

  againBt.addEventListener('click', function () {
    result.hidden = true;
    intro.hidden = false;
    box.dataset.state = 'intro';
    ta.value = '';
    ta.focus();
  });
})();
