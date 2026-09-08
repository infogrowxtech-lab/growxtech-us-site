/* Growx Tech IT — Netlify Forms AJAX submit handler.
   Used by the consultation-request form (contact page) and the newsletter
   signup form (site footer, all pages). Submits via fetch so the visitor
   gets an inline confirmation instead of a full page reload. */
(function () {
  function encode(data) {
    return Object.keys(data).map(function (k) {
      return encodeURIComponent(k) + '=' + encodeURIComponent(data[k]);
    }).join('&');
  }

  function bind(form, noteEl, successMsg, baseClass) {
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = {};
      new FormData(form).forEach(function (v, k) { data[k] = v; });
      var btn = form.querySelector('button[type="submit"]');
      var prevText = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }
      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: encode(data)
      }).then(function (r) {
        if (!r.ok) throw new Error('bad status');
        form.reset();
        if (noteEl) { noteEl.hidden = false; noteEl.className = baseClass + ' ok'; noteEl.textContent = successMsg; }
      }).catch(function () {
        if (noteEl) { noteEl.hidden = false; noteEl.className = baseClass + ' err'; noteEl.textContent = 'Something went wrong — please WhatsApp or email us instead.'; }
      }).finally(function () {
        if (btn) { btn.disabled = false; btn.textContent = prevText; }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    bind(
      document.getElementById('consultForm'),
      document.getElementById('cfNote'),
      "Thanks — we've got your details. A career advisor will reach out soon, usually within one business day.",
      'cf-note'
    );
    bind(
      document.getElementById('newsForm'),
      document.getElementById('newsNote'),
      'Subscribed — welcome aboard.',
      'foot-news-note'
    );
  });
})();
