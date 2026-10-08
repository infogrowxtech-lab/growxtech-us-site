/* ============================================================================
   Charlie -> human handoff, step 3: the website widget polls this every
   few seconds after escalating, asking "has RV answered yet?". Once it
   reports status "answered" the ticket is deleted so a second poll (or a
   second open tab) can't deliver the same reply twice.
   ========================================================================== */

const { getStore } = require('@netlify/blobs');

const TICKET_TTL_MS = 30 * 60 * 1000; // 30 minutes

function json(status, body) {
  return {
    statusCode: status,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'no-store',
      'Access-Control-Allow-Origin': '*'
    },
    body: JSON.stringify(body)
  };
}

exports.handler = async function (event) {
  if (event.httpMethod !== 'GET') return json(405, { ok: false, error: 'method' });

  const sessionId = String((event.queryStringParameters || {}).sessionId || '').slice(0, 80).trim();
  if (!sessionId) return json(400, { ok: false, error: 'missing-sessionId' });

  const store = getStore('grobo-tickets');
  const ticket = await store.get(sessionId, { type: 'json' }).catch(function () { return null; });

  if (!ticket) return json(200, { ok: true, status: 'none' });

  if (ticket.status === 'pending' && (Date.now() - ticket.createdAt) > TICKET_TTL_MS) {
    await store.delete(sessionId).catch(function () {});
    return json(200, { ok: true, status: 'expired' });
  }

  if (ticket.status === 'answered') {
    await store.delete(sessionId).catch(function () {});
    return json(200, { ok: true, status: 'answered', reply: ticket.reply });
  }

  return json(200, { ok: true, status: 'pending' });
};
