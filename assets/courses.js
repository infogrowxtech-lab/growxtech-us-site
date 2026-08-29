/* Growx Tech IT — Free Courses engine.
   ------------------------------------------------------------------
   Curates real, existing YouTube lessons (we do not host or claim to
   have produced the video content) and wraps them with:
     - a watch-progress bar, tracked via the YouTube IFrame Player API
     - a free certificate, unlocked once the watch threshold is hit
   Certificates are generated entirely client-side on a <canvas> and
   downloaded as a PNG. No account, no payment, no upload of anything
   except (optionally) a name + email, which is passed into the same
   lead pipeline every other form on this site uses.
   ------------------------------------------------------------------ */
window.GX = window.GX || {};

GX.Courses = (function () {
  var THRESHOLD = 0.75; // 75% watched unlocks the certificate

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

  function drawCertificate(canvas, opts) {
    var ctx = canvas.getContext('2d');
    var W = canvas.width, H = canvas.height;

    var bgGrad = ctx.createLinearGradient(0, 0, W, H);
    bgGrad.addColorStop(0, '#0B1220');
    bgGrad.addColorStop(1, '#070B14');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, W, H);

    // border
    ctx.strokeStyle = 'rgba(243,159,27,.55)';
    ctx.lineWidth = 3;
    ctx.strokeRect(28, 28, W - 56, H - 56);
    ctx.strokeStyle = 'rgba(255,255,255,.14)';
    ctx.lineWidth = 1;
    ctx.strokeRect(42, 42, W - 84, H - 84);

    // top accent glow
    var glow = ctx.createRadialGradient(W / 2, 0, 10, W / 2, 0, W * 0.6);
    glow.addColorStop(0, 'rgba(243,159,27,.20)');
    glow.addColorStop(1, 'rgba(243,159,27,0)');
    ctx.fillStyle = glow;
    ctx.fillRect(0, 0, W, H * 0.5);

    ctx.textAlign = 'center';

    // wordmark
    ctx.fillStyle = '#EAF0FA';
    ctx.font = '700 30px Sora, sans-serif';
    ctx.fillText('GROWX TECH IT', W / 2, 118);
    ctx.fillStyle = '#F39F1B';
    ctx.font = '700 30px Sora, sans-serif';
    var wm = ctx.measureText('GROWX TECH IT').width;
    ctx.fillText('X', W / 2 + wm / 2 - 26, 118);

    ctx.fillStyle = '#93A1B8';
    ctx.font = '600 13px "JetBrains Mono", monospace';
    ctx.textTransform = 'uppercase';
    ctx.fillText('FREE COURSE PROGRAM', W / 2, 146);

    ctx.fillStyle = '#EAF0FA';
    ctx.font = '400 22px "JetBrains Mono", monospace';
    ctx.fillText('Certificate of Completion', W / 2, 210);

    ctx.fillStyle = '#93A1B8';
    ctx.font = '400 15px Sora, sans-serif';
    ctx.fillText('This certifies that', W / 2, 258);

    ctx.fillStyle = '#F5C36B';
    ctx.font = '800 46px Sora, sans-serif';
    ctx.fillText(opts.name, W / 2, 322);

    ctx.fillStyle = '#93A1B8';
    ctx.font = '400 15px Sora, sans-serif';
    ctx.fillText('has successfully completed', W / 2, 362);

    ctx.fillStyle = '#EAF0FA';
    ctx.font = '700 26px Sora, sans-serif';
    wrapText(ctx, opts.course, W / 2, 402, W - 220, 32);

    ctx.fillStyle = '#93A1B8';
    ctx.font = '400 13px "JetBrains Mono", monospace';
    ctx.fillText('a free program by Growx Tech IT — growxtech-it.us', W / 2, H - 92);

    // footer row: date / id / signature
    ctx.textAlign = 'left';
    ctx.fillStyle = '#93A1B8';
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillText('ISSUED', 90, H - 56);
    ctx.fillStyle = '#EAF0FA';
    ctx.font = '600 14px "JetBrains Mono", monospace';
    ctx.fillText(opts.date, 90, H - 36);

    ctx.textAlign = 'center';
    ctx.fillStyle = '#93A1B8';
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillText('CERTIFICATE ID', W / 2, H - 56);
    ctx.fillStyle = '#EAF0FA';
    ctx.font = '600 14px "JetBrains Mono", monospace';
    ctx.fillText(opts.id, W / 2, H - 36);

    ctx.textAlign = 'right';
    ctx.fillStyle = '#93A1B8';
    ctx.font = '600 11px "JetBrains Mono", monospace';
    ctx.fillText('VERIFY', W - 90, H - 56);
    ctx.fillStyle = '#4FD8FF';
    ctx.font = '600 14px "JetBrains Mono", monospace';
    ctx.fillText('growxtech-it.us/courses', W - 90, H - 36);
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
          ? 'Unlocked — you can generate your certificate below.'
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

    if (certForm) {
      certForm.addEventListener('submit', function (ev) {
        ev.preventDefault();
        var name = document.getElementById('gxCertName').value.trim();
        var email = document.getElementById('gxCertEmail').value.trim();
        if (!name || !email) return;

        var id = certId(course.title, name);
        var date = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });

        drawCertificate(certCanvas, { name: name, course: course.title, date: date, id: id });

        if (window.GX && GX.submitLead) {
          GX.submitLead({
            type: 'course-certificate',
            name: name,
            email: email,
            target: course.title,
            note: 'Completed free course "' + course.title + '", certificate ' + id
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
      });
    }
  }

  return { init: init };
})();
