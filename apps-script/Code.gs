/** Growx lead catcher - writes site leads into the "Growx Leads" sheet.
 *
 *  Anti-spam gate (added Aug 30, 2026): this URL is public by necessity
 *  (it has to be callable from the browser), so previously it was wide
 *  open to anyone who found it, no check at all before a row got written
 *  and an email got sent. Two cheap checks now filter out generic bots
 *  and scrapers before anything touches the sheet:
 *    - _k must match SITE_KEY (sent automatically by every real page)
 *    - _hp (the honeypot field) must be empty (a real visitor never
 *      fills it in; only a bot that blindly fills every field on a
 *      form does)
 *  A targeted human attacker who reads the site's JS can still find
 *  SITE_KEY, this is a spam/bot filter, not encryption, but it stops
 *  the overwhelming majority of automated abuse with zero cost and no
 *  CAPTCHA friction for real visitors.
 */

var SHEET_ID = '1c875Kxk7VxrlPOCYEWsEkTmRZbL9fzf_OBPlv4r1gFw';
var NOTIFY_TO = 'info.growxtech@gmail.com';
var BASE = ['Timestamp', 'type', 'name', 'email', 'phone', 'target', 'note', 'page', 'source'];

// Must match GX.LEAD_KEY in assets/config.js exactly.
var SITE_KEY = '6ca5024bcd3628dd5ad87924d0fd2fb2';

function doGet() {
  return ContentService.createTextOutput('Growx lead catcher is running.');
}

function doPost(e) {
  try {
    var data = {};
    if (e && e.postData && e.postData.contents) {
      try { data = JSON.parse(e.postData.contents); }
      catch (err) { data = { note: String(e.postData.contents).slice(0, 900) }; }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    // Spam gate: wrong/missing key, or the honeypot got filled in.
    // Responds ok:true either way so a bot probing the endpoint learns
    // nothing about why its request was dropped.
    if (data._k !== SITE_KEY || String(data._hp || '').trim() !== '') {
      return json({ ok: true });
    }
    delete data._k;
    delete data._hp;

    save(data);
    try { notify(data); } catch (mailErr) {}
    return json({ ok: true });
  } catch (err) {
    return json({ ok: false, error: String(err) });
  }
}

function json(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function sheet() {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sh = ss.getSheets()[0];
  if (sh.getLastRow() === 0) {
    sh.appendRow(BASE);
    sh.getRange(1, 1, 1, BASE.length).setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}

function save(data) {
  var sh = sheet();
  var width = Math.max(sh.getLastColumn(), 1);
  var header = sh.getRange(1, 1, 1, width).getValues()[0];

  var extras = [];
  for (var k in data) {
    if (!data.hasOwnProperty(k)) continue;
    if (header.indexOf(k) === -1) extras.push(k);
  }
  if (extras.length) {
    sh.getRange(1, header.length + 1, 1, extras.length).setValues([extras]).setFontWeight('bold');
    header = header.concat(extras);
  }

  var row = [];
  for (var i = 0; i < header.length; i++) {
    var key = header[i];
    if (key === 'Timestamp') { row.push(new Date()); continue; }
    var v = data[key];
    if (v === undefined || v === null) { row.push(''); continue; }
    row.push(typeof v === 'object' ? JSON.stringify(v) : String(v));
  }
  sh.appendRow(row);
}

function notify(data) {
  var lines = [];
  for (var k in data) {
    if (data.hasOwnProperty(k)) lines.push(k + ': ' + data[k]);
  }
  MailApp.sendEmail(
    NOTIFY_TO,
    'New Growx lead: ' + (data.name || data.email || data.type || 'website'),
    lines.join('\n') + '\n\nSheet: https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/edit'
  );
}

function testLead() {
  save({ type: 'editor-test', name: 'Editor Test', email: 'editor@example.com', note: 'safe to delete' });
  return 'ok';
}
