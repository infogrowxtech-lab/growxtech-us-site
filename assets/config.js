/* Growx Tech IT, site config + lead delivery.
   ------------------------------------------------------------------
   Every lead (referral, job application, enquiry, complaint) is posted
   to a Google Apps Script web app owned by Growx. That script writes the
   lead into the "Growx Leads" sheet in Drive and emails a copy.
   Nothing here is secret: the endpoint only accepts leads, it never
   returns data, so it is safe to sit in front-end code.
   If the post ever fails the visitor is still handed to WhatsApp, so a
   lead is never silently lost.
   ------------------------------------------------------------------ */
window.GX = window.GX || {};

GX.WA        = '13026831622';
GX.WA_DISPLAY= '+1 (302) 683-1622';
GX.TEL       = '+17198389991';
GX.TEL_DISPLAY = '+1 (719) 838-9991';
GX.EMAIL     = 'hi@growxtech-it.us';

GX.SHEET_URL = 'https://script.google.com/macros/s/AKfycbyW-EBzKfKQWj4ZMtpZ1tSq8jnfS2lYZQu2PXpPVVY3H1vVtIJKtRSrg2hQFuOUYnOJmg/exec';
GX.MAIL_URL  = '';   // not needed, the Apps Script emails you directly

GX.waLink = function (text) {
  return 'https://wa.me/' + GX.WA + (text ? '?text=' + encodeURIComponent(text) : '');
};

/* Fire-and-forget lead delivery. Never blocks the visitor. */
GX.submitLead = function (payload) {
  payload = payload || {};
  payload.page = location.pathname;
  payload.at = new Date().toISOString();
  payload._subject = 'Growx lead: ' + (payload.type || 'enquiry');

  var jobs = [];

  if (GX.SHEET_URL) {
    jobs.push(fetch(GX.SHEET_URL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(payload)
    }).catch(function () {}));
  }

  if (GX.MAIL_URL) {
    jobs.push(fetch(GX.MAIL_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(payload)
    }).catch(function () {}));
  }

  try { localStorage.setItem('gx_last_lead', JSON.stringify(payload)); } catch (e) {}

  return Promise.all(jobs);
};
