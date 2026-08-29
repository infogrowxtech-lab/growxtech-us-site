/* Growx Tech IT, intro splash + mascot greeting */
(function () {
  var intro = document.getElementById('intro');
  if (!intro) return;

  var KEY = 'gx_intro_seen';
  var seen = false;
  try { seen = sessionStorage.getItem(KEY) === '1'; } catch (e) {}

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (seen || reduce) { intro.parentNode.removeChild(intro); return; }

  document.documentElement.classList.add('intro-lock');

  var vid   = document.getElementById('introVid');
  var skip  = document.getElementById('introSkip');
  var sound = document.getElementById('introSound');
  var prog  = document.getElementById('introProg');
  var greet = document.getElementById('greet');
  var done  = false;

  function finish() {
    if (done) return;
    done = true;
    try { sessionStorage.setItem(KEY, '1'); } catch (e) {}
    intro.classList.add('out');
    document.documentElement.classList.remove('intro-lock');
    setTimeout(function () {
      if (intro.parentNode) intro.parentNode.removeChild(intro);
      showGreeting();
    }, 620);
  }

  function showGreeting() {
    if (!greet) return;
    greet.hidden = false;
    requestAnimationFrame(function () { greet.classList.add('in'); });
    setTimeout(function () {
      greet.classList.remove('in');
      greet.classList.add('tuck');
      setTimeout(function () { if (greet.parentNode) greet.parentNode.removeChild(greet); }, 900);
    }, 4200);
  }

  if (vid) {
    vid.addEventListener('ended', finish);
    vid.addEventListener('error', finish);
    vid.addEventListener('timeupdate', function () {
      if (prog && vid.duration) prog.style.width = (vid.currentTime / vid.duration * 100) + '%';
    });
    var p = vid.play();
    if (p && p.catch) p.catch(function () { /* autoplay blocked, poster stays up */ });
  }

  if (skip) skip.addEventListener('click', finish);

  if (sound && vid) {
    sound.addEventListener('click', function () {
      vid.muted = !vid.muted;
      sound.textContent = vid.muted ? '🔇 Sound on' : '🔊 Sound off';
      if (!vid.muted) { var q = vid.play(); if (q && q.catch) q.catch(function () {}); }
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' || e.key === 'Enter') finish();
  });

  /* hard stop so nobody is ever trapped behind the video */
  setTimeout(finish, 13000);
})();
