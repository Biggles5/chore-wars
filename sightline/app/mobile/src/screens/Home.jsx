// Home: scanned-house map, the narrator's latest one-liner, scene chips,
// live tiles, recent stories.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React, { useState } from "react";
import HouseMap from "../HouseMap.jsx";
import { ampm, thumbUrl } from "../api.js";

const SCENES = ["Night", "Away", "Home", "Party", "Package watch"];

function latestNarration(stories) {
  for (const s of stories) {
    if (s.narrative && s.narrative.homeowner) return s.narrative.homeowner;
  }
  return "All quiet. Nothing on the perimeter needed your attention.";
}

function lastEventForNode(events, nodeId) {
  return events.find(e => e.node_id === nodeId && e.media && e.media.thumb_ref);
}

export default function Home({ site, stories, events, openStory }) {
  const [scene, setScene] = useState("Night");
  const deterSegs = [];
  const marks = [];
  for (const e of events.slice(0, 12)) {
    if (e.type === "deter.fired" && e.deter) deterSegs.push(...e.deter.segments);
    const pos = e.geometry && e.geometry.pos;
    if (pos && marks.length < 5) marks.push({ x: pos.x, y: pos.y, cls: e.object?.class });
  }
  const openZones = stories.filter(s => s.status === "open").flatMap(s => s.zones);

  return (
    <main>
      <div className="narrator">
        <span className="label">Narrator</span>
        {latestNarration(stories)}
      </div>

      <div className="section-title">Perimeter</div>
      <HouseMap site={site} highlightZones={openZones} deterSegs={deterSegs} marks={marks} />

      <div className="section-title">Scenes</div>
      <div className="scene-row">
        {SCENES.map(s => (
          <button key={s} className={"scene" + (s === scene ? " active" : "")}
            onClick={() => setScene(s)}>{s}</button>
        ))}
      </div>

      <div className="section-title">Live</div>
      <div className="tiles">
        {(site ? site.nodes : []).map(n => {
          const ev = lastEventForNode(events, n.id);
          return (
            <div className="tile" key={n.id}>
              {ev ? <img src={thumbUrl(ev.media.thumb_ref)} alt={n.id} /> : null}
              <span className="dot" />
              <span className="tag">{n.id} · {n.kind === "door" ? "door" : "track"}</span>
            </div>
          );
        })}
        {!site && <div className="empty" style={{ gridColumn: "1 / -1" }}>no nodes: start the sim</div>}
      </div>

      <div className="section-title">Recent</div>
      {stories.length === 0 && <div className="empty">No stories yet. Run a scenario.</div>}
      {stories.slice(0, 8).map(s => {
        const bf = s.entities.find(e => e.best_frame && e.best_frame.thumb_ref);
        return (
          <div className="card story-row" key={s.story_id} onClick={() => openStory(s.story_id)}>
            <div className={"sev " + s.severity} />
            <div className="body">
              <div className="title">{s.title || "Activity"}</div>
              <div className="sub">
                {ampm(s.started_ts)} · {s.zones.filter(z => z !== "street").join(", ") || "street"}
                {s.deter && s.deter.fired ? " · deter fired" : ""}
              </div>
              <div style={{ marginTop: 4 }}>
                {s.verified && <span className="badge verified">Verified</span>}{" "}
                {s.status === "open" && <span className="badge open">Live</span>}
              </div>
            </div>
            {bf && <img src={thumbUrl(bf.best_frame.thumb_ref)} alt="" />}
          </div>
        );
      })}
    </main>
  );
}
