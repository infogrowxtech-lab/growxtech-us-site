/* Growx Tech IT — Free Courses engine.
   ------------------------------------------------------------------
   Curates real, existing YouTube lessons (we do not host or claim to
   have produced the video content) and wraps them with:
     - a watch-progress bar, tracked via the YouTube IFrame Player API
     - a free certificate, unlocked once the watch threshold is hit
   Certificates are generated entirely client-side on a <canvas> and
   downloaded as a PNG. No account, no payment, no upload of anything
   except a name, email and phone number (all three required), which
   is passed into the same lead pipeline every other form on this
   site uses.
   ------------------------------------------------------------------ */
window.GX = window.GX || {};

GX.Courses = (function () {
  var THRESHOLD = 0.75; // 75% watched unlocks the certificate

  // Certificate background art — preloaded as soon as this script runs so
  // it's almost certainly ready by the time someone finishes 75% of a video.
  var bgImage = new Image();
  var bgImageLoaded = false;
  var bgImageFailed = false;
  bgImage.onload = function () { bgImageLoaded = true; };
  bgImage.onerror = function () { bgImageFailed = true; };
  bgImage.src = '/assets/cert-bg.jpg';

  function storeKey(courseId) { return 'gx_course_' + courseId; }

  function loadProgress(courseId) {
    try {
      var raw = localStorage.getItem(storeKey(courseId));
      return raw ? JSON.parse(raw) : { maxTime: 0, duration: 0 };
    } catch (e) { return { maxTime: 0, duration: 0 }; }
  }

  function saveProgress(courseId, data) {
    try { localStorage.setItem(storeKey(courseId), JSON.stringify(data)); } catch (e) {}
  }

  function pct(progress) {
    if (!progress.duration) return 0;
    return Math.min(1, progress.maxTime / progress.duration);
  }

  function fmtPct(p) { return Math.round(p * 100) + '%'; }

  function certId(course, name) {
    var s = course + '|' + name + '|' + Date.now();
    var h = 0;
    for (var i = 0; i < s.length; i++) { h = ((h << 5) - h + s.charCodeAt(i)) | 0; }
    return 'GX-' + Math.abs(h).toString(36).toUpperCase().slice(0, 8);
  }

  // Shrinks a font size (in 1px steps) until `text` fits within maxWidth at
  // the given weight/family, down to minSize. Leaves ctx.font set to the
  // chosen size/weight/family and returns that size. Used so long learner
  // names / course titles never overflow their column.
  function fitFontSize(ctx, text, weight, family, maxWidth, startSize, minSize) {
    var size = startSize;
    while (size > minSize) {
      ctx.font = weight + ' ' + size + 'px ' + family;
      if (ctx.measureText(text).width <= maxWidth) break;
      size -= 1;
    }
    ctx.font = weight + ' ' + size + 'px ' + family;
    return size;
  }

  function drawCertificate(canvas, opts) {
    var ctx = canvas.getContext('2d');
    var W = canvas.width, H = canvas.height;

    if (bgImageLoaded) {
      ctx.drawImage(bgImage, 0, 0, W, H);
    } else {
      // Fallback if the background art hasn't finished loading (or failed) —
      // keeps certificate generation working even then.
      var bgGrad = ctx.createLinearGradient(0, 0, W, H);
      bgGrad.addColorStop(0, '#0B1220');
      bgGrad.addColorStop(1, '#070B14');
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = 'rgba(243,159,27,.55)';
      ctx.lineWidth = 3;
      ctx.strokeRect(28, 28, W - 56, H - 56);
    }

    // The background art has the robot mascot on the left third and a gold
    // medal icon in the bottom-right — all text sits in the clear column to
    // the right of the robot, using the horizontal line as the name's
    // signature line, and stays above/beside the medal.
    var colX = 815;       // text column center
    var colLeft = 500;    // don't cross into the robot
    var colRight = 1150;  // stay inside the frame

    ctx.textAlign = 'center';

    // wordmark — measured piece by piece so the stylized orange "X" always
    // lands exactly on the X in GROWX, regardless of font size/column.
    ctx.font = '700 26px Sora, sans-serif';
    var wmFull = ctx.measureText('GROWX TECH IT').width;
    var wmStart = colX - wmFull / 2;
    var wmBefore = 'GROW', wmAfter = ' TECH IT';
    ctx.textAlign = 'left';
    ctx.fillStyle = '#EAF0FA';
    ctx.fillText(wmBefore, wmStart, 96);
    var wmBeforeW = ctx.measureText(wmBefore).width;
    ctx.fillStyle = '#F39F1B';
    ctx.fillText('X', wmStart + wmBeforeW, 96);
    var wmXW = ctx.measureText('X').width;
    ctx.fillStyle = '#EAF0FA';
    ctx.fillText(wmAfter, wmStart + wmBeforeW + wmXW, 96);
    ctx.textAlign = 'center';

    ctx.fillStyle = '#C9D2E3';
    ctx.font = '600 12px "JetBrains Mono", monospace';
    ctx.fillText('FREE COURSE PROGRAM', colX, 122);

    ctx.fillStyle = '#EAF0FA';
    ctx.font = '400 20px "JetBrains Mono", monospace';
    ctx.fillText('Certificate of Completion', colX, 178);

    // tagline lives in the clear gap above "This certifies that" — the old
    // spot (bottom-right, near y=665) overlapped the gold medal artwork.
    ctx.fillStyle = '#C9D2E3';
    ctx.font = '400 12px "JetBrains Mono", monospace';
    ctx.fillText('a free program by Growx Tech IT · growxtech-it.us', colX, 212);

    ctx.fillStyle = '#C9D2E3';
    ctx.font = '400 15px Sora, sans-serif';
    ctx.fillText('This certifies that', colX, 350);

    // name sits just above the art's own signature line. The line is baked
    // into the background image, not drawn by us, and it is NOT centered on
    // colX — measured directly from cert-bg.jpg it runs from x=468 to x=993
    // (center ~730, width ~525) — so the name is centered and width-fit
    // against those exact bounds rather than the general text column, or
    // long names overflow past the line's right end.
    ctx.fillStyle = '#F5C36B';
    var sigLineCenterX = 730;
    var nameMaxWidth = 495; // 525px line width, minus ~15px padding each side
    fitFontSize(ctx, opts.name, '800', 'Sora, sans-serif', nameMaxWidth, 40, 20);
    ctx.fillText(opts.name, sigLineCenterX, 445);

    ctx.fillStyle = '#C9D2E3';
    ctx.font = '400 15px Sora, sans-serif';
    ctx.fillText('has successfully completed', colX, 515);

    // course title prefers a single line, auto-shrinking to fit; only falls
    // back to a 2-line wrap (at the smallest size) if it still doesn't fit —
    // which keeps it from colliding with "has successfully completed" above.
    ctx.fillStyle = '#EAF0FA';
    var titleMaxWidth = colRight - colLeft - 60;
    var titleSize = fitFontSize(ctx, opts.course, '700', 'Sora, sans-serif', titleMaxWidth, 24, 16);
    if (ctx.measureText(opts.course).width <= titleMaxWidth) {
      ctx.fillText(opts.course, colX, 550);
    } else {
      wrapText(ctx, opts.course, colX, 558, titleMaxWidth, titleSize + 8);
    }

    // footer row: date / id / verify — kept clear of the medal (bottom right)
    ctx.textAlign = 'left';
    ctx.fillStyle = '#C9D2E3';
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillText('ISSUED', colLeft, H - 56);
    ctx.fillStyle = '#EAF0FA';
    ctx.font = '600 14px "JetBrains Mono", monospace';
    ctx.fillText(opts.date, colLeft, H - 36);

    ctx.textAlign = 'center';
    ctx.fillStyle = '#C9D2E3';
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillText('CERTIFICATE ID', colX, H - 56);
    ctx.fillStyle = '#EAF0FA';
    ctx.font = '600 14px "JetBrains Mono", monospace';
    ctx.fillText(opts.id, colX, H - 36);

    ctx.textAlign = 'right';
    ctx.fillStyle = '#C9D2E3';
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillText('VERIFY', colRight, H - 56);
    ctx.fillStyle = '#4FD8FF';
    ctx.font = '600 14px "JetBrains Mono", monospace';
    ctx.fillText('growxtech-it.us/courses', colRight, H - 36);
  }

  function wrapText(ctx, text, x, y, maxWidth, lineHeight) {
    var words = text.split(' ');
    var line = '';
    var lines = [];
    for (var n = 0; n < words.length; n++) {
      var test = line + words[n] + ' ';
      if (ctx.measureText(test).width > maxWidth && n > 0) {
        lines.push(line);
        line = words[n] + ' ';
      } else {
        line = test;
      }
    }
    lines.push(line);
    var startY = y - ((lines.length - 1) * lineHeight) / 2;
    for (var i = 0; i < lines.length; i++) {
      ctx.fillText(lines[i].trim(), x, startY + i * lineHeight);
    }
  }

  function init(course) {
    var progress = loadProgress(course.id);
    var bar = document.getElementById('gxProgressBar');
    var pctLabel = document.getElementById('gxProgressPct');
    var unlockNote = document.getElementById('gxUnlockNote');
    var certBtn = document.getElementById('gxCertBtn');
    var certForm = document.getElementById('gxCertForm');
    var certCanvas = document.getElementById('gxCertCanvas');
    var certDownload = document.getElementById('gxCertDownload');
    var certStatus = document.getElementById('gxCertStatus');

    function render() {
      var p = pct(progress);
      if (bar) bar.style.width = fmtPct(p);
      if (pctLabel) pctLabel.textContent = fmtPct(p);
      var unlocked = p >= THRESHOLD;
      if (certBtn) certBtn.disabled = !unlocked;
      if (unlockNote) {
        unlockNote.textContent = unlocked
          ? 'Unlocked: you can generate your certificate below.'
          : 'Watch at least ' + Math.round(THRESHOLD * 100) + '% of the video to unlock your free certificate.';
      }
    }
    render();

    var player;
    var tag = document.createElement('script');
    tag.src = 'https://www.youtube.com/iframe_api';
    var firstScript = document.getElementsByTagName('script')[0];
    firstScript.parentNode.insertBefore(tag, firstScript);

    function onReady() {
      if (progress.duration && progress.maxTime && progress.maxTime < progress.duration - 1) {
        try { player.seekTo(0); } catch (e) {}
      }
    }

    function poll() {
      if (!player || typeof player.getCurrentTime !== 'function') return;
      var t, d;
      try { t = player.getCurrentTime(); d = player.getDuration(); } catch (e) { return; }
      if (!d) return;
      progress.duration = d;
      if (t > progress.maxTime) progress.maxTime = t;
      saveProgress(course.id, progress);
      render();
    }

    window.onYouTubeIframeAPIReady = function () {
      player = new YT.Player('gxPlayer', {
        videoId: course.youtubeId,
        playerVars: { rel: 0, modestbranding: 1 },
        events: {
          onReady: onReady,
          onStateChange: function (e) {
            if (e.data === YT.PlayerState.PLAYING) {
              window.gxPollTimer = window.gxPollTimer || setInterval(poll, 2000);
            }
          }
        }
      });
    };

    if (certBtn) {
      certBtn.addEventListener('click', function () {
        certBtn.hidden = true;
        if (certForm) certForm.hidden = false;
      });
    }

    var PHONE_RE = /^[+()\-\s\d]{7,20}$/;

    // A custom validity message sticks until JS clears it, including across
    // separate submit attempts, so without this a first bad phone number
    // would silently block every later attempt even after it's corrected
    // (the browser would refuse to fire the 'submit' event at all).
    var certPhoneEl = document.getElementById('gxCertPhone');
    if (certPhoneEl) {
      certPhoneEl.addEventListener('input', function () { certPhoneEl.setCustomValidity(''); });
    }

    if (certForm) {
      certForm.addEventListener('submit', function (ev) {
        ev.preventDefault();
        var name = document.getElementById('gxCertName').value.trim();
        var email = document.getElementById('gxCertEmail').value.trim();
        var phoneEl = document.getElementById('gxCertPhone');
        var phone = phoneEl ? phoneEl.value.trim() : '';
        var hpEl = document.getElementById('gxCertHp');
        var hp = hpEl ? hpEl.value : '';
        if (!name || !email) return;
        if (phoneEl) phoneEl.setCustomValidity('');
        if (!phone || !PHONE_RE.test(phone)) {
          if (phoneEl) { phoneEl.focus(); phoneEl.setCustomValidity('Enter a phone number with country code, like +1 555 123 4567.'); phoneEl.reportValidity(); }
          return;
        }

        var id = certId(course.title, name);
        var date = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });

        function finishCertificate() {
          drawCertificate(certCanvas, { name: name, course: course.title, date: date, id: id });

          if (window.GX && GX.submitLead) {
            GX.submitLead({
              type: 'course-certificate',
              name: name,
              email: email,
              phone: phone,
              target: course.title,
              note: 'Completed free course "' + course.title + '", certificate ' + id,
              _hp: hp
            });
          }

          certForm.hidden = true;
          certCanvas.hidden = false;
          if (certDownload) {
            certDownload.hidden = false;
            certDownload.addEventListener('click', function () {
              var url = certCanvas.toDataURL('image/png');
              var a = document.createElement('a');
              a.href = url;
              a.download = 'growx-certificate-' + course.id + '.png';
              document.body.appendChild(a);
              a.click();
              document.body.removeChild(a);
            });
          }
          if (certStatus) certStatus.hidden = false;
        }

        // Give the background art a brief moment to finish loading (it starts
        // loading as soon as this script runs, so this rarely waits at all)
        // rather than falling back to the plain gradient unnecessarily.
        if (bgImageLoaded || bgImageFailed) {
          finishCertificate();
        } else {
          var settled = false;
          var proceed = function () {
            if (settled) return;
            settled = true;
            finishCertificate();
          };
          bgImage.addEventListener('load', proceed);
          bgImage.addEventListener('error', proceed);
          setTimeout(proceed, 1500); // safety timeout — never block generation for long
        }
      });
    }
  }

  return { init: init };
})();
