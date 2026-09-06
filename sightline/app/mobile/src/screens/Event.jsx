// Verified Event: story timeline, re-ID chips, deter status, actions.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React, { useState } from "react";
import HouseMap from "../HouseMap.jsx";
import { ampm, clock, deterNow, thumbUrl } from "../api.js";

export default function EventScreen({ site, story }) {
  const [note, setNote] = useState("");
  if (!story) return <main><div className="empty">Story not found.</div></main>;
  const deter = story.deter || {};

  async function onDeter() {
    setNote("Firing deter...");
    try {
      await deterNow(story.site_id);
      setNote("Deter command sent to the gateway.");
    } catch {
      setNote("Gateway unreachable.");
    }
  }

  return (
    <main>
      <div style={{ marginBottom: 8 }}>
        <div style={{ fontFamily: "var(--font-display)", fontSize: 18, fontWeight: 700 }}>
          {story.title || "Activity"}
        </div>
        <div style={{ fontSize: 12, color: "var(--muted)", marginTop: 3 }}>
          {ampm(story.started_ts)}
          {story.ended_ts ? ` to ${ampm(story.ended_ts)}` : " · in progress"}
          {typeof story.dwell_s === "number" && story.dwell_s > 0 ? ` · ${Math.round(story.dwell_s)}s on property` : ""}
        </div>
        <div style={{ marginTop: 6 }}>
          {story.verified && <span className="badge verified">Verified</span>}{" "}
          {story.status === "open" && <span className="badge open">Live</span>}{" "}
          <span className={"badge"} style={{ background: "var(--paper)", color: "var(--muted)", border: "1px solid var(--line)" }}>
            {story.severity}
          </span>
        </div>
      </div>

      {deter.fired && (
        <div className="deter-banner">
          Deter fired at {clock(deter.ts)} on {(deter.segments || []).join(", ")}.
          {deter.outcome === "fled" ? " They left immediately." :
           deter.outcome === "stayed" ? " They did not leave." : ""}
        </div>
      )}

      {story.narrative && story.narrative.homeowner && (
        <div className="narrator">
          <span className="label">Narrator</span>
          {story.narrative.homeowner}
        </div>
      )}

      <div className="section-title">Where</div>
      <HouseMap site={site} height={150}
        highlightZones={story.zones} deterSegs={deter.fired ? (deter.segments || []) : []} />

      <div className="section-title">Who / what (re-ID)</div>
      <div className="entity-chips">
        {story.entities.map(e => (
          <div className="entity-chip" key={e.entity_id}>
            {e.best_frame && e.best_frame.thumb_ref
              ? <img src={thumbUrl(e.best_frame.thumb_ref)} alt="" />
              : <span style={{ width: 30 }} />}
            <span>
              <span className="cls">{e.class}</span>{" "}
              <span className="meta">
                {(e.node_tracks || []).length} camera{(e.node_tracks || []).length === 1 ? "" : "s"}
                {e.best_frame ? ` · ${e.best_frame.dori_level}` : ""}
              </span>
            </span>
          </div>
        ))}
      </div>

      <div className="section-title">Timeline</div>
      <div className="card">
        <ul className="timeline">
          {story.timeline.map(b => (
            <li key={b.event_id}>
              <span className="ts">{clock(b.ts)}</span>
              <span className="beat">{b.beat}</span>
              {b.thumb_ref && <img src={thumbUrl(b.thumb_ref)} alt="" />}
            </li>
          ))}
        </ul>
      </div>

      {story.narrative && story.narrative.police_summary && (
        <>
          <div className="section-title">Police export (preview)</div>
          <div className="police">{story.narrative.police_summary}</div>
        </>
      )}

      <div className="actions">
        <button className="btn primary" onClick={onDeter}>Deter now</button>
        <button className="btn" onClick={() => setNote("Clip link copied (demo).")}>Share clip</button>
        <button className="btn" onClick={() => setNote(
          story.evidence_exportable
            ? "Sent to monitoring center."
            : "Blocked: no native-pixel evidence in this story (simulated frames).")}>
          Send to monitoring
        </button>
      </div>
      {note && <div className="empty" role="status">{note}</div>}
    </main>
  );
}
