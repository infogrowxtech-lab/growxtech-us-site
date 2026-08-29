/** Growx lead catcher - writes site leads into the "Growx Leads" sheet. */

var SHEET_ID = '1c875Kxk7VxrlPOCYEWsEkTmRZbL9fzf_OBPlv4r1gFw';
var NOTIFY_TO = 'info.growxtech@gmail.com';
var BASE = ['Timestamp', 'type', 'name', 'email', 'phone', 'target', 'note', 'page', 'source'];

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
