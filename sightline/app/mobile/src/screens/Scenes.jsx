// Scenes: pick the active scene, paint deter zones on the house, describe a
// scene in plain words, view the enforced privacy masks.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React, { useEffect, useState } from "react";
import HouseMap from "../HouseMap.jsx";
import { fetchJson } from "../api.js";

export default function Scenes({ site }) {
  const [store, setStore] = useState(null);
  const [designText, setDesignText] = useState("");
  const [designed, setDesigned] = useState(null);
  const [note, setNote] = useState("");

  useEffect(() => {
    fetchJson("/api/scenes").then(setStore).catch(() => {});
  }, []);

  if (!store) return <main><div className="empty">Loading scenes...</div></main>;
  const active = store.scenes.find(s => s.name === store.active) || store.scenes[0];

  async function activate(name) {
    const d = await fetch("/api/scenes", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ active: name }),
    }).then(r => r.json());
    setStore(d);
  }

  async function toggleZone(zoneId) {
    const zones = active.deter_zones.includes(zoneId)
      ? active.deter_zones.filter(z => z !== zoneId)
      : [...active.deter_zones, zoneId];
    const scenes = store.scenes.map(s =>
      s.name === active.name ? { ...s, deter_zones: zones } : s);
    const d = await fetch("/api/scenes", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ scenes }),
    }).then(r => r.json());
    setStore(d);
  }

  async function design() {
    if (!designText.trim()) return;
    const d = await fetch("/api/scenes/design", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ text: designText }),
    }).then(r => r.json());
    setDesigned(d.scene);
  }

  async function saveDesigned() {
    const scenes = [...store.scenes.filter(s => s.name !== designed.name), designed];
    const d = await fetch("/api/scenes", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ scenes, active: designed.name }),
    }).then(r => r.json());
    setStore(d);
    setDesigned(null);
    setDesignText("");
    setNote(`Scene "${designed.name}" saved and active.`);
  }

  const zoneIds = site ? site.zones.map(z => z.id).filter(z => z !== "street") : [];

  return (
    <main>
      <div className="section-title">Active scene</div>
      <div className="scene-row">
        {store.scenes.map(s => (
          <button key={s.name} className={"scene" + (s.name === store.active ? " active" : "")}
            onClick={() => activate(s.name)}>{s.name}</button>
        ))}
      </div>

      <div className="section-title">Deter zones ({active.name})</div>
      <HouseMap site={site} height={170} highlightZones={active.deter_zones} />
      <div className="scene-row" style={{ marginTop: 8 }}>
        {zoneIds.map(z => (
          <button key={z}
            className={"scene" + (active.deter_zones.includes(z) ? " active" : "")}
            onClick={() => toggleZone(z)}>
            {z}
          </button>
        ))}
      </div>
      <div className="card" style={{ fontSize: 12, color: "var(--muted)" }}>
        {active.armed
          ? `Armed. Person or vehicle dwelling in a highlighted zone triggers zone-follow deterrence${active.quiet_lights ? " (quiet-hours pattern)" : ""}. Notifications: ${active.notify}.`
          : "Disarmed. The system watches and records stories but never deters."}
      </div>

      <div className="section-title">Describe a scene</div>
      <div className="card">
        <textarea value={designText} onChange={e => setDesignText(e.target.value)}
          placeholder={'e.g. "watch the driveway and porch after dark, quiet lights, only alert me for people"'}
          rows={2} aria-label="Scene description"
          style={{ width: "100%", border: "1px solid var(--line)", borderRadius: 8, padding: 10, fontFamily: "var(--font-body)", fontSize: 13, resize: "vertical" }} />
        <div style={{ display: "flex", gap: 8, marginTop: 8 }}>
          <button className="btn" onClick={design}>Design it</button>
          {designed && <button className="btn primary" style={{ gridColumn: "auto" }} onClick={saveDesigned}>Save "{designed.name}"</button>}
        </div>
        {designed && (
          <div style={{ marginTop: 8, fontSize: 12, fontFamily: "var(--font-mono)" }}>
            {designed.armed ? "armed" : "disarmed"} · zones: {designed.deter_zones.join(", ")}
            · notify: {designed.notify}{designed.quiet_lights ? " · quiet lights" : ""}
          </div>
        )}
      </div>

      <div className="section-title">Privacy masks (enforced on device)</div>
      {store.masks.map((m, i) => (
        <div className="card" key={i} style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div>
            <div style={{ fontWeight: 600, fontSize: 13 }}>{m.label}</div>
            <div style={{ fontSize: 11, color: "var(--muted)", fontFamily: "var(--font-mono)" }}>
              {m.node_id} · pixels inside the mask are zeroed at the sensor, never stored
            </div>
          </div>
          <span className="badge verified">ENFORCED</span>
        </div>
      ))}
      <div className="card" style={{ fontSize: 12, color: "var(--muted)" }}>
        Masks are set during install and can only widen from the app. Narrowing or
        removing a mask requires the owner PIN at the gateway. Core plan: none of
        this footage leaves the house, masked or not.
      </div>
      {note && <div className="empty" role="status">{note}</div>}
    </main>
  );
}
