/* ============================================================================
   Charlie -> human handoff, step 1: the website calls this when Charlie
   (rules or AI) can't answer. It saves a "ticket" and pings a Microsoft
   Teams channel through a Power Automate flow. RV's reply comes back later
   through grobo-reply.js; the widget finds it by polling grobo-poll.js.

   Needs these Netlify environment variables (Project configuration ->
   Environment variables):
     GROBO_FLOW_URL        the Power Automate "When an HTTP request is
                            received" trigger URL (see scripts/TEAMS_HANDOFF.md)
     GROBO_ESCALATE_SECRET any password you make up - it proves a reply
                            claiming to come from the flow really does

   If GROBO_FLOW_URL isn't set yet, this safely returns {ok:false} and the
   website falls back to its normal WhatsApp/Call buttons - the chat never
   breaks for a customer because Teams isn't wired up yet.
   ========================================================================== */

const { getStore } = require('@netlify/blobs');

const TICKET_TTL_MS = 30 * 60 * 1000; // 30 minutes - after this a ticket is stale

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

  const sessionId = String(payload.sessionId || '').slice(0, 80).trim();
  const message = String(payload.message || '').slice(0, 1000).trim();
  const page = String(payload.page || '/').slice(0, 120);
  const history = Array.isArray(payload.history) ? payload.history.slice(-12) : [];

  if (!sessionId || !message) return json(400, { ok: false, error: 'missing-fields' });

  const store = getStore('grobo-tickets');
  const now = Date.now();

  let ticket = await store.get(sessionId, { type: 'json' }).catch(function () { return null; });

  if (ticket && ticket.status === 'pending' && (now - ticket.createdAt) < TICKET_TTL_MS) {
    /* already escalated and still waiting on this same conversation - add
       this message as extra context instead of opening a second Teams card */
    ticket.extra = (ticket.extra || []).concat([message]);
    await store.setJSON(sessionId, ticket);
    return json(200, { ok: true, status: 'pending', appended: true });
  }

  ticket = {
    sessionId: sessionId,
    status: 'pending',
    question: message,
    history: history,
    page: page,
    createdAt: now,
    reply: null
  };
  await store.setJSON(sessionId, ticket);

  const flowUrl = process.env.GROBO_FLOW_URL;
  const secret = process.env.GROBO_ESCALATE_SECRET || '';

  if (!flowUrl) {
    return json(200, { ok: false, error: 'not-configured' });
  }

  const siteUrl = process.env.URL || ('https://' + (event.headers.host || 'growxtech-it.us'));
  const transcript = history.map(function (h) {
    return (h.role === 'assistant' ? 'Charlie' : 'Visitor') + ': ' + h.text;
  }).join('\n');

  try {
    const ctrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
    const timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, 8000);
    await fetch(flowUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        secret: secret,
        sessionId: sessionId,
        page: page,
        question: message,
        transcript: transcript,
        replyUrl: siteUrl + '/.netlify/functions/grobo-reply'
      }),
      signal: ctrl ? ctrl.signal : undefined
    });
    clearTimeout(timer);
  } catch (e) {
    console.error('grobo-escalate: could not reach the Teams flow:', e && e.message);
    return json(200, { ok: false, error: 'teams-unreachable' });
  }

  return json(200, { ok: true, status: 'pending' });
};
