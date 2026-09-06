// Ask: chat over event memory. Mock answers are deterministic and cited;
// Claude mode is a gateway-side switch, the UI is identical.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React, { useRef, useState } from "react";

const SUGGESTED = [
  "What happened last night?",
  "Any cars I should know about?",
  "Did the lights fire?",
  "Who came to the door?",
];

export default function Ask({ openStory }) {
  const [msgs, setMsgs] = useState([
    { role: "sys", text: "Ask about anything the perimeter has seen. Answers cite the stories they come from." },
  ]);
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  const boxRef = useRef(null);

  async function send(q) {
    const question = (q || text).trim();
    if (!question || busy) return;
    setText("");
    setBusy(true);
    setMsgs(m => [...m, { role: "me", text: question }]);
    try {
      const r = await fetch("/api/ask", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const d = await r.json();
      setMsgs(m => [...m, { role: "ai", text: d.answer, sources: d.sources || [] }]);
    } catch {
      setMsgs(m => [...m, { role: "ai", text: "Gateway unreachable." }]);
    }
    setBusy(false);
    setTimeout(() => boxRef.current?.scrollTo(0, 1e6), 50);
  }

  return (
    <main style={{ display: "flex", flexDirection: "column", height: "calc(100vh - 140px)" }}>
      <div ref={boxRef} style={{ flex: 1, overflowY: "auto", paddingBottom: 8 }}>
        {msgs.map((m, i) => (
          <div key={i} style={{
            margin: "6px 0", display: "flex",
            justifyContent: m.role === "me" ? "flex-end" : "flex-start",
          }}>
            <div style={{
              maxWidth: "82%", padding: "9px 12px", borderRadius: 12, fontSize: 13.5,
              lineHeight: 1.45,
              background: m.role === "me" ? "var(--ink)" : m.role === "sys" ? "transparent" : "#fff",
              color: m.role === "me" ? "var(--paper)" : m.role === "sys" ? "var(--muted)" : "var(--ink)",
              border: m.role === "ai" ? "1px solid var(--line)" : "none",
              fontStyle: m.role === "sys" ? "italic" : "normal",
            }}>
              {m.text}
              {m.sources && m.sources.length > 0 && (
                <div style={{ marginTop: 6, display: "flex", flexWrap: "wrap", gap: 6 }}>
                  {m.sources.map(s => (
                    <button key={s.story_id} onClick={() => openStory(s.story_id)}
                      style={{
                        fontFamily: "var(--font-mono)", fontSize: 10, cursor: "pointer",
                        border: "1px solid var(--line)", borderRadius: 999,
                        background: "var(--paper)", padding: "2px 8px", color: "var(--blue)",
                      }}>
                      {s.title || s.story_id.slice(0, 8)}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
        {busy && <div className="empty">thinking...</div>}
      </div>
      <div className="scene-row" style={{ marginBottom: 8 }}>
        {SUGGESTED.map(s => (
          <button key={s} className="scene" onClick={() => send(s)}>{s}</button>
        ))}
      </div>
      <div style={{ display: "flex", gap: 8 }}>
        <input value={text} onChange={e => setText(e.target.value)}
          onKeyDown={e => e.key === "Enter" && send()}
          placeholder="Ask about your perimeter"
          aria-label="Question"
          style={{
            flex: 1, border: "1px solid var(--line)", borderRadius: 10,
            padding: "12px 12px", fontSize: 14, fontFamily: "var(--font-body)",
            background: "#fff", minHeight: 44,
          }} />
        <button className="btn" onClick={() => send()} disabled={busy}
          style={{ minWidth: 70 }}>Ask</button>
      </div>
    </main>
  );
}
