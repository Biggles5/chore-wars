// SightLine app data layer: correlator REST + websocket, sim site map.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import { useEffect, useRef, useState } from "react";

export async function fetchJson(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`${url}: ${r.status}`);
  return r.json();
}

export function thumbUrl(ref) {
  if (!ref) return null;
  if (ref.startsWith("http")) {
    // rewrite absolute sim URLs through the dev proxy so it works when the
    // phone frame is opened from another device on the LAN
    try {
      const u = new URL(ref);
      if (u.pathname.startsWith("/run/")) return "/sim" + u.pathname;
    } catch { /* fall through */ }
    return ref;
  }
  return "/sim/run/" + ref;
}

// Live connection to the correlator: stories keyed by id, recent events,
// connection state. Reconnects forever.
export function useLive() {
  const [stories, setStories] = useState({});
  const [events, setEvents] = useState([]);
  const [connected, setConnected] = useState(false);
  const wsRef = useRef(null);

  useEffect(() => {
    let alive = true;
    let retry = null;

    function connect() {
      if (!alive) return;
      const proto = location.protocol === "https:" ? "wss" : "ws";
      const ws = new WebSocket(`${proto}://${location.host}/ws`);
      wsRef.current = ws;
      ws.onopen = () => setConnected(true);
      ws.onmessage = (m) => {
        const msg = JSON.parse(m.data);
        if (msg.kind === "story") {
          setStories(s => ({ ...s, [msg.payload.story_id]: msg.payload }));
        } else if (msg.kind === "event") {
          const p = msg.payload;
          if (p.type && p.type !== "detection.update") {
            setEvents(e => [p, ...e].slice(0, 120));
          }
        }
      };
      ws.onclose = () => {
        setConnected(false);
        retry = setTimeout(connect, 1500);
      };
      ws.onerror = () => ws.close();
    }

    connect();
    // seed from REST in case the ws misses history
    fetchJson("/api/stories").then(list => {
      setStories(s => {
        const out = { ...s };
        for (const st of list) if (!out[st.story_id]) out[st.story_id] = st;
        return out;
      });
    }).catch(() => {});

    return () => { alive = false; clearTimeout(retry); wsRef.current?.close(); };
  }, []);

  const list = Object.values(stories).sort((a, b) =>
    (b.started_ts || "").localeCompare(a.started_ts || ""));
  return { stories: list, byId: stories, events, connected };
}

export function useSite() {
  const [site, setSite] = useState(null);
  useEffect(() => {
    fetchJson("/sim/site").then(setSite).catch(() => setSite(null));
  }, []);
  return site;
}

export function deterNow(siteId) {
  return fetch(`/api/deter/${siteId}`, { method: "POST" }).then(r => r.json());
}

// Times render in the HOUSE's clock (the ISO string's own offset), never the
// viewing browser's timezone. A 2:14 AM event reads 2:14 AM from anywhere.
export const clock = ts => (ts || "").slice(11, 19);
export const ampm = (ts) => {
  if (!ts || ts.length < 16) return "";
  const h24 = parseInt(ts.slice(11, 13), 10);
  const mm = ts.slice(14, 16);
  const h12 = h24 % 12 === 0 ? 12 : h24 % 12;
  return `${h12}:${mm} ${h24 < 12 ? "AM" : "PM"}`;
};
