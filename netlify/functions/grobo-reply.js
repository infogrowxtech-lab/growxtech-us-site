/* ============================================================================
   Charlie -> human handoff, step 2: the Power Automate flow calls this
   after RV types a reply into the Adaptive Card in Teams and hits Submit.
   It writes the reply onto the matching ticket, which the website is
   polling for in grobo-poll.js.

   Must be called with the SAME value as GROBO_ESCALATE_SECRET in the
   JSON body's "secret" field, or it is rejected. This stops anyone who
   isn't your Power Automate flow from injecting fake replies.
   ========================================================================== */

const { getStore } = require('@netlify/blobs');

function json(status, body) {
  return {
    statusCode: status,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'no-store',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': 'Content-Type',
      'Access-Control-Allow-Methods': 'POST, OPTIONS'
    },
    body: JSON.stringify(body)
  };
}

exports.handler = async function (event) {
  if (event.httpMethod === 'OPTIONS') return json(204, {});
  if (event.httpMethod !== 'POST') return json(405, { ok: false, error: 'method' });

  let payload;
  try { payload = JSON.parse(event.body || '{}'); }
  catch (e) { return json(400, { ok: false, error: 'bad-json' }); }

  const secret = process.env.GROBO_ESCALATE_SECRET || '';
  if (!secret || payload.secret !== secret) {
    return json(401, { ok: false, error: 'bad-secret' });
  }

  const sessionId = String(payload.sessionId || '').slice(0, 80).trim();
  const reply = String(payload.reply || '').slice(0, 2000).trim();
  if (!sessionId || !reply) return json(400, { ok: false, error: 'missing-fields' });

  const store = getStore('grobo-tickets');
  const ticket = await store.get(sessionId, { type: 'json' }).catch(function () { return null; });
  if (!ticket) return json(404, { ok: false, error: 'no-such-ticket' });

  ticket.status = 'answered';
  ticket.reply = reply;
  ticket.answeredAt = Date.now();
  await store.setJSON(sessionId, ticket);

  return json(200, { ok: true });
};
