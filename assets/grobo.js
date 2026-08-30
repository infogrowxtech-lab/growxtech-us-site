/* Charlie — the Growx Tech IT growth buddy.
   Knowledge lives in grobo-kb.js. This file is the matcher, the memory
   and the widget. No dependencies, no network calls except lead delivery. */
(function () {
  var C = window.GX || {};
  var KBD = window.GROBO_KB || { KB: [], RULES: [], FALLBACK: [], CLARIFY: [], SYN: {} };

  var WA_NUM = C.WA || '13026831622';
  var TEL    = C.TEL || '+17198389991';
  var TEL_D  = C.TEL_DISPLAY || '+1 (719) 838-9991';
  var EMAIL  = C.EMAIL || 'hi@growxtech-it.us';
  var AVATAR = '/assets/grobo-avatar.webp';
  var BODY   = '/assets/grobo-hero.webp';

  /* ============================================================ helpers */
  function wa(text) {
    return 'https://wa.me/' + WA_NUM + (text ? '?text=' + encodeURIComponent(text) : '');
  }
  function waBtn(text, label) {
    return '<a class="gact wa" href="' + wa(text) + '" target="_blank" rel="noopener">&#128172; ' + (label || 'WhatsApp us') + '</a>';
  }
  function telBtn(label) {
    return '<a class="gact call" href="tel:' + TEL + '">&#128222; ' + (label || 'Call ' + TEL_D) + '</a>';
  }
  function bothBtns(text) {
    return '<div class="gacts">' + waBtn(text) + telBtn() + '</div>';
  }
  function esc(s) {
    return String(s).replace(/[<>&]/g, function (c) { return { '<': '&lt;', '>': '&gt;', '&': '&amp;' }[c]; });
  }
  function hash(s) {
    var h = 0, i;
    for (i = 0; i < s.length; i++) { h = ((h << 5) - h + s.charCodeAt(i)) | 0; }
    return h;
  }

  /* Expand {{wa:...}} {{call}} {{both:...}} {{lead}} inside an answer */
  function expand(text, ctx) {
    var startLead = false;
    text = text.replace(/\{\{lead\}\}/g, function () { startLead = true; return ''; });
    text = text.replace(/\{\{both:([^}]*)\}\}/g, function (m, t) {
      return '<br><br>' + bothBtns(t + (ctx && ctx.tail ? ' ' + ctx.tail : ''));
    });
    text = text.replace(/\{\{wa:([^}]*)\}\}/g, function (m, t) {
      return '<br><br><div class="gacts">' + waBtn(t) + '</div>';
    });
    text = text.replace(/\{\{call\}\}/g, function () {
      return '<br><br><div class="gacts">' + telBtn() + '</div>';
    });
    return { html: text, lead: startLead };
  }

  /* ============================================================ memory */
  var mem = {
    open: false,
    greeted: false,
    flow: null,
    step: 0,
    data: {},
    lastIntent: null,
    lastUserText: '',
    usedAnswer: {},      // intentId -> [indexes already used]
    saidHashes: {},      // every bot line already sent this session
    missStreak: 0,
    turns: 0,
    offerLead: null,     // topic that offered to take the visitor's details
    ai: null,            // null = untested, true = live, false = fell back to rules
    transcript: [],      // what the AI brain remembers
    profile: {}          // name / role / country picked up along the way
  };

  /* ========================================================== matching */
  var STOP = {
    'a':1,'an':1,'the':1,'is':1,'are':1,'am':1,'was':1,'were':1,'be':1,'been':1,'to':1,'of':1,'in':1,
    'on':1,'at':1,'for':1,'and':1,'or':1,'but':1,'it':1,'this':1,'that':1,'my':1,'your':1,'me':1,
    'i':1,'we':1,'do':1,'does':1,'did':1,'can':1,'could':1,'would':1,'should':1,'will':1,'shall':1,
    'have':1,'has':1,'had':1,'please':1,'just':1,'so':1,'if':1,'about':1,'with':1,'from':1,'want':1,
    'need':1,'get':1,'give':1,'tell':1,'know':1,'there':1,'here':1,'any':1,'some':1,'much':1,'many':1
  };

  function normalise(s) {
    return String(s).toLowerCase()
      .replace(/[^a-z0-9%.\s+-]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function tokens(s) {
    var raw = normalise(s).split(' ');
    var out = [];
    for (var i = 0; i < raw.length; i++) {
      var t = raw[i];
      if (!t) continue;
      if (KBD.SYN[t]) t = KBD.SYN[t];
      out.push(t);
    }
    return out;
  }

  /* cheap edit-distance-1 check so small typos still land */
  function near(a, b) {
    if (a === b) return true;
    if (Math.abs(a.length - b.length) > 1) return false;
    if (a.length < 6 || b.length < 6) return false;   // short words are too easy to confuse
    var i = 0, j = 0, diff = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { i++; j++; continue; }
      diff++;
      if (diff > 1) return false;
      if (a.length > b.length) i++;
      else if (b.length > a.length) j++;
      else { i++; j++; }
    }
    return true;
  }

  function scoreEntry(entry, text, toks) {
    var score = 0;
    var weight = entry.w || 1;
    if (entry.re && entry.re.test(text)) score += 8 * weight;
    for (var i = 0; i < entry.k.length; i++) {
      var key = entry.k[i];
      if (key.indexOf(' ') !== -1) {
        if (text.indexOf(key) !== -1) score += 4 * weight;   // phrase hit, strong
        continue;
      }
      for (var j = 0; j < toks.length; j++) {
        if (toks[j] === key) { score += 2 * weight; break; }
        if (near(toks[j], key)) { score += 1.7 * weight; break; }
      }
    }
    /* `exact` entries (greetings) should not fire inside a long sentence */
    if (entry.exact && toks.length > 4) score = 0;
    return score;
  }

  function match(input) {
    var text = ' ' + normalise(input) + ' ';
    var toks = tokens(input);

    /* hard rules win over everything */
    for (var r = 0; r < KBD.RULES.length; r++) {
      var rule = KBD.RULES[r];
      if (rule.re && rule.re.test(text)) return { rule: rule };
      for (var q = 0; q < rule.k.length; q++) {
        if (text.indexOf(rule.k[q]) !== -1) return { rule: rule };
      }
    }

    var best = null, bestScore = 0, second = 0;
    for (var i = 0; i < KBD.KB.length; i++) {
      var s = scoreEntry(KBD.KB[i], text, toks);
      if (s > bestScore) { second = bestScore; bestScore = s; best = KBD.KB[i]; }
      else if (s > second) { second = s; }
    }

    /* very short follow-ups lean on the previous topic:
       "how much?" right after training should stay on training */
    if (bestScore === 0 && toks.length <= 4 && mem.lastIntent) {
      var carry = null;
      for (var c = 0; c < KBD.KB.length; c++) {
        if (KBD.KB[c].id === mem.lastIntent) { carry = KBD.KB[c]; break; }
      }
      if (carry && /\b(price|how|what|why|when|more|else|explain|detail|ok|yes|sure)\b/.test(text)) {
        return { entry: carry, confidence: 'carry' };
      }
    }

    if (!best || bestScore < 2) return { entry: null, confidence: 'none' };
    if (bestScore < 3.5) return { entry: best, confidence: 'low' };
    return { entry: best, confidence: 'high' };
  }

  /* ================================================= answer selection */
  function pickAnswer(entry) {
    var used = mem.usedAnswer[entry.id] || [];
    var pool = [];
    for (var i = 0; i < entry.a.length; i++) {
      if (used.indexOf(i) === -1) pool.push(i);
    }

    if (!pool.length) {
      /* every variant of this topic already used this session */
      return {
        html: 'I have already covered that one above, and I do not want to just repeat myself.<br><br>' +
              'If it did not fully answer your question, a human will do a better job of it than a second paste from me.' +
              bothBtns('Hi Growx Tech IT, I have a follow-up question about: ' + (mem.lastUserText || 'your services')),
        exhausted: true
      };
    }

    var idx = pool[Math.floor(Math.random() * pool.length)];
    used.push(idx);
    mem.usedAnswer[entry.id] = used;
    return { html: entry.a[idx], index: idx };
  }

  function alreadySaid(html) {
    var h = hash(html.replace(/<[^>]+>/g, '').slice(0, 220));
    if (mem.saidHashes[h]) return true;
    mem.saidHashes[h] = 1;
    return false;
  }

  /* ============================================================ markup */
  var launcher = document.createElement('button');
  launcher.className = 'grobo-launch';
  launcher.type = 'button';
  launcher.setAttribute('aria-label', 'Chat with Charlie');
  launcher.innerHTML = '<img src="' + BODY + '" alt="" class="gl-body"><span class="gl-ring"></span>';

  var hello = document.createElement('div');
  hello.className = 'grobo-hello';
  hello.innerHTML = '<b>Hi, I\'m Charlie</b><span>Question about jobs, pricing or visas? Ask me.</span>';

  var panel = document.createElement('div');
  panel.className = 'grobo-panel';
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', 'Chat with Charlie');
  panel.innerHTML =
    '<div class="grobo-head">' +
      '<img src="' + AVATAR + '" alt="" class="gh-face">' +
      '<div class="gh-txt"><b>Charlie</b><span><i class="gdot"></i>Growx Tech IT &middot; online</span></div>' +
      '<div class="gh-quick">' +
        '<a class="gq" href="tel:' + TEL + '" title="Call us" aria-label="Call us">&#128222;</a>' +
        '<a class="gq wa" href="' + wa('Hi Growx Tech IT, I have a question.') + '" target="_blank" rel="noopener" title="WhatsApp" aria-label="WhatsApp">&#128172;</a>' +
      '</div>' +
      '<button class="grobo-close" type="button" aria-label="Close chat">&#10005;</button>' +
    '</div>' +
    '<div class="grobo-msgs" id="groboMsgs" aria-live="polite"></div>' +
    '<div class="grobo-chips" id="groboChips"></div>' +
    '<form class="grobo-inputrow" id="groboForm">' +
      '<input id="groboInput" type="text" autocomplete="off" placeholder="Ask me anything..." aria-label="Message Charlie">' +
      '<button class="grobo-send" type="submit" aria-label="Send">&#10148;</button>' +
    '</form>';

  document.body.appendChild(launcher);
  document.body.appendChild(hello);
  document.body.appendChild(panel);

  var msgs  = panel.querySelector('#groboMsgs');
  var chips = panel.querySelector('#groboChips');
  var form  = panel.querySelector('#groboForm');
  var input = panel.querySelector('#groboInput');

  function push(html, who) {
    var d = document.createElement('div');
    d.className = 'gm ' + (who || 'bot');
    d.innerHTML = (who === 'bot' ? '<img src="' + AVATAR + '" alt="" class="gm-face">' : '') +
                  '<div class="gm-b">' + html + '</div>';
    msgs.appendChild(d);
    msgs.scrollTop = msgs.scrollHeight;
    return d;
  }

  function typing() {
    var d = document.createElement('div');
    d.className = 'gm bot';
    d.innerHTML = '<img src="' + AVATAR + '" alt="" class="gm-face"><div class="gm-b gtyping"><i></i><i></i><i></i></div>';
    msgs.appendChild(d);
    msgs.scrollTop = msgs.scrollHeight;
    return d;
  }

  var queue = [], draining = false;

  function drain() {
    if (draining || !queue.length) return;
    draining = true;
    var job = queue.shift();
    var t = typing();
    var plain = job.html.replace(/<[^>]+>/g, '');
    var delay = Math.min(380 + plain.length * 5, 1400);
    setTimeout(function () {
      t.remove();
      push(job.html, 'bot');
      if (job.after) job.after();
      draining = false;
      drain();
    }, delay);
  }

  function botSay(html, after) {
    queue.push({ html: html, after: after });
    drain();
  }

  function setChips(list) {
    chips.innerHTML = '';
    (list || []).forEach(function (c) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'gchip';
      b.textContent = c;
      b.addEventListener('click', function () { send(c); });
      chips.appendChild(b);
    });
  }

  var DEFAULT_CHIPS = ['Live jobs', 'Pricing', 'Resume help', 'Refer a friend', 'Talk to a human'];

  /* ============================================================= flows */
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  var PHONE_RE = /^[+()\-\s\d]{7,20}$/;

  /* people answer "what is your name?" with all sorts of things */
  function looksLikeName(s) {
    var t = s.trim();
    if (t.length < 2 || t.length > 60) return false;
    if (t.split(/\s+/).length > 5) return false;
    if (/\d/.test(t)) return false;
    if (/\b(i am|im|i'm|my name is|this is|hi|hello|fresher|job|resume|price|help|yes|no|ok)\b/i.test(t)) {
      return /\b(my name is|this is|i am|im|i'm)\s+[a-z]/i.test(t);   // allow "my name is Rahul"
    }
    return true;
  }
  function cleanName(s) {
    return s.replace(/^\s*(my name is|this is|i am|i'm|im)\s+/i, '').replace(/[.,!]+$/, '').trim();
  }

  function startReferral() {
    mem.flow = 'referral'; mem.step = 1; mem.data = { type: 'referral' };
    botSay('Love it, referrals are the best compliment you can give us. One thing to be clear about up front: <b>the reward goes to you, the referrer</b>. Your friend just gets our normal service at our normal price, nothing extra and nothing hidden.<br><br>So, what is <b>your friend\'s full name</b>?');
    setChips([]);
  }

  function startApply(job, url) {
    mem.flow = 'apply'; mem.step = 1;
    mem.data = { type: 'job-application', job: job || '', link: url || '' };
    botSay('Good pick' + (job ? ': <b>' + esc(job) + '</b>' : '') + '. I will pass your details to a recruiter who works that market. Four quick questions.<br><br>What is your <b>full name</b>?');
    setChips([]);
  }

  function startComplaint() {
    mem.flow = 'complaint'; mem.step = 1; mem.data = { type: 'complaint', priority: 'high' };
    botSay('I am sorry it has gone this way, and I am not going to argue with you about it. Let me get this in front of a person who can actually do something.<br><br>First, tell me in your own words <b>what happened</b>.');
    setChips([]);
  }

  function startLead(note) {
    mem.flow = 'lead'; mem.step = 1;
    mem.data = { type: 'enquiry', note: note || '' };
    var opener = mem.profile.name
      ? 'Right ' + esc(mem.profile.name) + ', let me get an advisor onto this. What <b>role and country</b> are you targeting?'
      : 'Happy to get that moving. A few quick questions and an advisor takes it from there.<br><br>What is your <b>name</b>?';
    if (mem.profile.name) { mem.data.name = mem.profile.name; mem.step = 2; }
    botSay(opener);
    setChips([]);
  }

  function deliver(summary, waText) {
    if (window.GX && GX.submitLead) {
      mem.data.transcriptHint = mem.lastUserText;
      GX.submitLead(mem.data);
    }
    botSay(summary + '<br><br>' + bothBtns(waText), function () {
      setChips(DEFAULT_CHIPS);
    });
    mem.flow = null; mem.step = 0;
  }

  function handleFlow(text) {
    var t = text.trim();

    if (mem.flow === 'referral') {
      if (mem.step === 1) {
        if (!looksLikeName(t)) { botSay('Sorry, I need just their name for this one. What are they called?'); return true; }
        t = cleanName(t);
        mem.data.referredName = t; mem.step = 2;
        botSay('Thanks. What is <b>' + esc(t) + '\'s email address</b>?'); return true;
      }
      if (mem.step === 2) {
        if (!EMAIL_RE.test(t)) { botSay('That does not look like a working email, mind checking it? Something like name@example.com.'); return true; }
        mem.data.referredEmail = t; mem.step = 3;
        botSay('Got it. And their <b>phone number</b> with the country code?'); return true;
      }
      if (mem.step === 3) {
        if (!PHONE_RE.test(t)) { botSay('That number looks off to me. Try it with the country code, like +1 555 123 4567.'); return true; }
        mem.data.referredPhone = t; mem.step = 4;
        botSay('Last one. What is <b>your own name and email</b>, so we know where the reward goes? Both on one line is fine.'); return true;
      }
      if (mem.step === 4) {
        mem.data.referrer = t;
        var m = t.match(/[^\s@]+@[^\s@]+\.[^\s@]{2,}/);
        mem.data.referrerEmail = m ? m[0] : '';
        deliver('Done, that is with our team now. &#9989;<br><br><b>' + esc(mem.data.referredName) + '</b> will hear from a career advisor within one working day. Your reward is credited once they start a paid service, and the team will confirm the amount with you directly, I am not going to quote a figure I cannot stand behind.',
                'Hi Growx Tech IT, I just referred ' + mem.data.referredName + ' through Charlie. Referrer: ' + t);
        return true;
      }
    }

    if (mem.flow === 'apply') {
      if (mem.step === 1) {
        if (!looksLikeName(t)) { botSay('Just your name for this bit, then I will get to the rest. What should I put down?'); return true; }
        t = cleanName(t);
        mem.data.name = t; mem.profile.name = t.split(' ')[0]; mem.step = 2;
        botSay('Thanks ' + esc(mem.profile.name) + '. What is your <b>email address</b>?'); return true;
      }
      if (mem.step === 2) {
        if (!EMAIL_RE.test(t)) { botSay('That email does not look right, could you check it?'); return true; }
        mem.data.email = t; mem.step = 3;
        botSay('And your <b>phone number</b> with the country code?'); return true;
      }
      if (mem.step === 3) {
        if (!PHONE_RE.test(t)) { botSay('Try that number again with the country code, like +1 555 123 4567.'); return true; }
        mem.data.phone = t; mem.step = 4;
        botSay('Last thing, what <b>role and country</b> are you targeting?'); return true;
      }
      if (mem.step === 4) {
        mem.data.target = t; mem.profile.role = t;
        var extra = mem.data.link
          ? '<br><br>Here is the original posting if you want to read it in full: <a href="' + mem.data.link + '" target="_blank" rel="noopener nofollow">open the listing</a>.'
          : '';
        deliver('You are in. &#9989; A recruiter will review your details and come back within one working day with roles that actually match' +
                (mem.data.job ? ', alongside <b>' + esc(mem.data.job) + '</b>' : '') +
                '.<br><br>To set expectations honestly: this puts you in front of the right people, it is not an offer. Sending your resume across now speeds it up a lot.' + extra,
                'Hi Growx Tech IT, I applied through Charlie.\nName: ' + mem.data.name + '\nEmail: ' + mem.data.email + '\nPhone: ' + mem.data.phone + '\nTarget: ' + t + (mem.data.job ? '\nJob: ' + mem.data.job : ''));
        return true;
      }
    }

    if (mem.flow === 'complaint') {
      if (mem.step === 1) {
        if (t.length < 5) { botSay('Give me a bit more than that so the team knows what they are looking at. What went wrong?'); return true; }
        mem.data.issue = t; mem.step = 2;
        botSay('Understood, and thank you for spelling it out. What is <b>your name</b>?');
        return true;
      }
      if (mem.step === 2) {
        if (!looksLikeName(t)) { botSay('Just your name here, so they can find your file.'); return true; }
        t = cleanName(t);
        mem.data.name = t; mem.profile.name = t.split(' ')[0]; mem.step = 3;
        botSay('Thanks ' + esc(mem.profile.name) + '. What is your <b>phone number</b>, with the country code? That is how the team will reach you on this.');
        return true;
      }
      if (mem.step === 3) {
        if (!PHONE_RE.test(t)) { botSay('That number looks off to me. Try it with the country code, like +1 555 123 4567.'); return true; }
        mem.data.phone = t; mem.step = 4;
        botSay('Got it. And an <b>email</b> too, in case that is easier for them to reach you on? (Optional, you can say "skip".)');
        return true;
      }
      if (mem.step === 4) {
        if (!/^skip$/i.test(t.trim())) {
          if (EMAIL_RE.test(t)) mem.data.email = t;
        }
        deliver('Logged and marked <b>urgent</b>. &#9989; Someone will come back to you on this.<br><br>I am not going to promise you an outcome, because that is not mine to promise. What I can tell you is it is no longer sitting in a chat window.<br><br>If you want to push it faster, go straight to the team, it is the same people either way.',
                'Hi Growx Tech IT, I raised a complaint through Charlie.\nName: ' + mem.data.name + '\nPhone: ' + mem.data.phone + (mem.data.email ? '\nEmail: ' + mem.data.email : '') + '\nIssue: ' + mem.data.issue);
        return true;
      }
    }

    if (mem.flow === 'lead') {
      if (mem.step === 1) {
        if (!looksLikeName(t)) { botSay('Let me start with just your name, what should I call you?'); return true; }
        t = cleanName(t);
        mem.data.name = t; mem.profile.name = t.split(' ')[0]; mem.step = 2;
        botSay('Good to meet you, ' + esc(mem.profile.name) + '. What <b>role and country</b> are you aiming for?'); return true;
      }
      if (mem.step === 2) {
        mem.data.target = t; mem.profile.role = t; mem.step = 3;
        botSay('Noted. What is your <b>phone number</b>, with the country code, so an advisor can reach you?'); return true;
      }
      if (mem.step === 3) {
        if (!PHONE_RE.test(t)) { botSay('That number looks off to me. Try it with the country code, like +1 555 123 4567.'); return true; }
        mem.data.phone = t; mem.step = 4;
        botSay('And your <b>email</b>? (Optional, you can say "skip".)'); return true;
      }
      if (mem.step === 4) {
        if (!/^skip$/i.test(t.trim())) {
          if (EMAIL_RE.test(t)) mem.data.email = t;
        }
        deliver('Perfect, an advisor has your details and will reach out within one working day. &#9989;<br><br>The first conversation is free and there is no obligation, worst case you get an honest read on where you stand.',
                'Hi Growx Tech IT, I spoke to Charlie.\nName: ' + mem.data.name + '\nPhone: ' + mem.data.phone + (mem.data.email ? '\nEmail: ' + mem.data.email : '') + '\nTarget: ' + mem.data.target);
        return true;
      }
    }

    return false;
  }

  /* cancel a flow if the person clearly changes the subject */
  function wantsOut(text) {
    return /^(stop|cancel|never ?mind|forget it|no|not now|later|skip|wait|change)/i.test(text.trim());
  }

  /* ============================================================== AI */
  var AI_URL = '/.netlify/functions/grobo';
  var AI_TIMEOUT = 12000;

  function askAI(text) {
    if (mem.ai === false) return Promise.resolve(null);

    var ctrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, AI_TIMEOUT);

    return fetch(AI_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: text,
        history: mem.transcript.slice(-12),
        page: location.pathname
      }),
      signal: ctrl ? ctrl.signal : undefined
    })
      .then(function (r) { return r.json(); })
      .then(function (d) {
        clearTimeout(timer);
        if (!d || !d.ok || !d.reply) { mem.ai = false; return null; }
        mem.ai = true;
        return d;
      })
      .catch(function () {
        clearTimeout(timer);
        mem.ai = false;
        return null;
      });
  }

  function aiReply(d, userText) {
    mem.transcript.push({ role: 'user', text: userText });
    mem.transcript.push({ role: 'assistant', text: d.reply.replace(/<[^>]+>/g, ' ') });
    if (mem.transcript.length > 24) mem.transcript = mem.transcript.slice(-24);

    var html = d.reply;
    if (d.action === 'human') {
      html += '<br><br>' + bothBtns('Hi Growx Tech IT, I was chatting with Charlie: ' + userText);
    }

    botSay(html, function () {
      if (d.action === 'lead')     { startLead('ai'); return; }
      if (d.action === 'referral') { startReferral(); return; }
      setChips(DEFAULT_CHIPS);
    });
  }

  /* ============================================================ reply */
  function respond(text) {
    mem.turns++;
    mem.lastUserText = text;

    var res = match(text);

    /* hard rule */
    if (res.rule) {
      mem.missStreak = 0;
      mem.lastIntent = null;
      var rr = expand(res.rule.a, {});
      botSay(rr.html, function () { setChips(DEFAULT_CHIPS); });
      return;
    }

    var entry = res.entry;

    if (!entry) {
      mem.missStreak++;
      if (mem.missStreak === 1) {
        var cl = KBD.CLARIFY[Math.floor(Math.random() * KBD.CLARIFY.length)];
        botSay(cl, function () { setChips(['Find me a job', 'Pricing', 'How it works', 'Talk to a human']); });
      } else {
        var fi = Math.min(mem.missStreak - 2, KBD.FALLBACK.length - 1);
        var fb = expand(KBD.FALLBACK[fi], { tail: text });
        botSay(fb.html, function () { setChips(DEFAULT_CHIPS); });
      }
      return;
    }

    mem.missStreak = 0;
    mem.lastIntent = entry.id;

    /* special flows */
    if (entry.a[0] === '__REFERRAL_FLOW__') { startReferral(); return; }
    if (entry.a[0] === '__LEAD_FLOW__')     { startLead(''); return; }
    if (entry.a[0] === '__COMPLAINT_FLOW__'){ startComplaint(); return; }

    var picked = pickAnswer(entry);

    if (!picked.exhausted && alreadySaid(picked.html)) {
      picked = pickAnswer(entry);          // try once more for a fresh line
    }

    var out = expand(picked.html, { tail: text });

    botSay(out.html, function () {
      if (out.lead) {
        mem.offerLead = entry.id;
        setChips(['Yes, take my details'].concat(entry.chips || DEFAULT_CHIPS));
      } else {
        mem.offerLead = null;
        setChips(entry.chips || DEFAULT_CHIPS);
      }
    });
  }

  /* ============================================================== io */
  function send(text) {
    if (!text || !text.trim()) return;
    push(esc(text), 'user');
    input.value = '';

    if (mem.flow && wantsOut(text)) {
      mem.flow = null; mem.step = 0;
      botSay('No problem, dropped it. What would you rather talk about?', function () { setChips(DEFAULT_CHIPS); });
      return;
    }

    if (handleFlow(text)) return;

    if (mem.offerLead && /^(yes|yeah|yep|ok|okay|sure|please|go ahead|take my details|yes take my details|do it)\b/i.test(text.trim())) {
      var seedId = mem.offerLead;
      mem.offerLead = null;
      startLead(seedId);
      return;
    }
    mem.offerLead = null;

    /* hard rules are enforced locally too, so a model can never talk past them */
    var pre = match(text);
    if (pre.rule) {
      mem.transcript.push({ role: 'user', text: text });
      mem.transcript.push({ role: 'assistant', text: pre.rule.a.replace(/<[^>]+>/g, ' ') });
      var pr = expand(pre.rule.a, {});
      botSay(pr.html, function () { setChips(DEFAULT_CHIPS); });
      return;
    }

    /* upset customers and complaints stay on the scripted path, an AI improvising
       at someone who is already angry is exactly how this goes wrong */
    if (pre.entry && (pre.entry.id === 'complaint' || pre.entry.id === 'delay' ||
                      pre.entry.id === 'escalate'  || pre.entry.id === 'existing_client' ||
                      pre.entry.id === 'invoice'   || pre.entry.id === 'cancel_service')) {
      respond(text);
      return;
    }

    if (mem.ai === false) { respond(text); return; }

    var thinking = typing();
    askAI(text).then(function (d) {
      thinking.remove();
      if (d) aiReply(d, text);
      else respond(text);
    });
  }

  form.addEventListener('submit', function (e) { e.preventDefault(); send(input.value); });

  function open(seed) {
    mem.open = true;
    document.body.classList.add('grobo-open');
    panel.classList.add('on');
    hello.classList.remove('on');
    if (!mem.greeted) {
      mem.greeted = true;
      var g = 'Hi, I\'m <b>Charlie</b> &#128075; the growth buddy at Growx Tech IT. I know our services, pricing and process inside out, so ask me anything.<br><br>Two things I will always do: give you a straight answer, and tell you when a human should take over instead of guessing.';
      alreadySaid(g);
      push(g, 'bot');
      setChips(DEFAULT_CHIPS);
    }
    if (seed) setTimeout(function () { send(seed); }, 320);
    setTimeout(function () { input.focus(); }, 360);
  }

  function close() {
    mem.open = false;
    document.body.classList.remove('grobo-open');
    panel.classList.remove('on');
  }

  launcher.addEventListener('click', function () { mem.open ? close() : open(); });
  panel.querySelector('.grobo-close').addEventListener('click', close);
  hello.addEventListener('click', function () { open(); });

  document.addEventListener('click', function (e) {
    var el = e.target.closest ? e.target.closest('[data-grobo]') : null;
    if (!el) return;
    e.preventDefault();
    open(el.getAttribute('data-grobo') || '');
  });

  addEventListener('keydown', function (e) { if (e.key === 'Escape' && mem.open) close(); });

  window.Charlie = {
    open: open,
    apply: function (job, url) { open(); setTimeout(function () { startApply(job, url); }, 340); }
  };

  /* peek once per session */
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var peeked = false;
  try { peeked = sessionStorage.getItem('gx_grobo_peek') === '1'; } catch (e) {}
  if (!peeked && !reduce) {
    setTimeout(function () {
      if (!mem.open) {
        hello.classList.add('on');
        try { sessionStorage.setItem('gx_grobo_peek', '1'); } catch (e) {}
        setTimeout(function () { hello.classList.remove('on'); }, 7000);
      }
    }, 6500);
  }
})();
