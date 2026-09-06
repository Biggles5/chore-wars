// Onboarding / Scan-to-Quote: roofline ft + corners + eave heights + brand
// in, kit + price + DORI plan out, drawn as coverage rings.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React, { useState } from "react";

const BRANDS = [
  ["gemstone", "Gemstone (12V)"], ["trimlight", "Trimlight (12V)"],
  ["jellyfish", "JellyFish (48V)"], ["everlights", "EverLights (24V)"],
  ["govee", "Govee (24V)"], ["oelo", "Oelo (36V)"],
  ["sightline48", "No lights yet: SightLine 48V rail"],
];

function Field({ label, children }) {
  return (
    <label style={{ display: "block", marginBottom: 10 }}>
      <div style={{ fontSize: 12, fontWeight: 600, marginBottom: 4 }}>{label}</div>
      {children}
    </label>
  );
}

const inputStyle = {
  width: "100%", border: "1px solid var(--line)", borderRadius: 8,
  padding: "11px 10px", fontSize: 14, fontFamily: "var(--font-body)",
  background: "#fff", minHeight: 44,
};

function CoverageRings({ plan }) {
  // simple to-scale plan view: identify ring and aim window per eave height
  const W = 340, H = 130;
  const maxFt = Math.max(...plan.map(p => p.identity_channel.identify_ring_ft), 40);
  const s = (W / 2 - 12) / maxFt;
  return (
    <svg viewBox={`0 0 ${W} ${H}`} width="100%" role="img" aria-label="DORI coverage">
      <rect x={W / 2 - 30} y={4} width={60} height={12} fill="var(--ink)" rx={2} />
      <text x={W / 2} y={13} textAnchor="middle" fontSize="8" fill="#fff" fontFamily="monospace">NODE</text>
      {plan.map((p, i) => {
        const r = p.identity_channel.identify_ring_ft * s;
        const win = p.identity_channel.aim_window_ft;
        return (
          <g key={i}>
            <circle cx={W / 2} cy={10} r={r} fill="none"
              stroke={i === 0 ? "var(--blue)" : "var(--green)"} strokeWidth="1.6" strokeDasharray="5 3" />
            {win && (
              <path d={`M ${W / 2} 10 m 0 ${win[0] * s} l 0 ${(win[1] - win[0]) * s}`}
                stroke={i === 0 ? "var(--blue)" : "var(--green)"} strokeWidth="6" opacity="0.35" />
            )}
            <text x={8} y={H - 8 - i * 12} fontSize="9" fontFamily="monospace" fill="var(--ink)">
              {p.eave_ft} ft eave: identify to {p.identity_channel.identify_ring_ft} ft
              {win ? `, aim ${win[0]} to ${win[1]} ft` : ", identity marginal"}
            </text>
          </g>
        );
      })}
    </svg>
  );
}

export default function Setup({ enterInstaller }) {
  const [form, setForm] = useState({
    roofline_ft: 160, corners: 4, eaves: "20, 10", brand: "gemstone", run: 50,
  });
  const [q, setQ] = useState(null);
  const [err, setErr] = useState("");

  async function getQuote() {
    setErr("");
    try {
      const r = await fetch("/api/quote", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({
          roofline_ft: Number(form.roofline_ft),
          corners: Number(form.corners),
          eave_heights_ft: form.eaves.split(",").map(x => Number(x.trim())).filter(x => x > 0),
          brand: form.brand,
          node_run_ft: Number(form.run),
        }),
      });
      if (!r.ok) throw new Error((await r.json()).detail || r.status);
      setQ(await r.json());
    } catch (e) {
      setErr(String(e.message || e));
    }
  }

  const injections = q && q.power.injection_kits;

  return (
    <main>
      {enterInstaller && (
        <div className="card" style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div>
            <div style={{ fontWeight: 600, fontSize: 13 }}>Certified installer?</div>
            <div style={{ fontSize: 11, color: "var(--muted)" }}>
              Guided runbook with QC gates for today's job
            </div>
          </div>
          <button className="btn" onClick={enterInstaller}>Installer mode</button>
        </div>
      )}
      <div className="section-title">Scan your roofline</div>
      <div className="card">
        <Field label="Roofline length (ft)">
          <input style={inputStyle} type="number" value={form.roofline_ft}
            onChange={e => setForm({ ...form, roofline_ft: e.target.value })} />
        </Field>
        <Field label="Corners">
          <input style={inputStyle} type="number" value={form.corners}
            onChange={e => setForm({ ...form, corners: e.target.value })} />
        </Field>
        <Field label="Eave heights (ft, comma separated)">
          <input style={inputStyle} value={form.eaves}
            onChange={e => setForm({ ...form, eaves: e.target.value })} />
        </Field>
        <Field label="Existing lighting">
          <select style={inputStyle} value={form.brand}
            onChange={e => setForm({ ...form, brand: e.target.value })}>
            {BRANDS.map(([v, l]) => <option key={v} value={v}>{l}</option>)}
          </select>
        </Field>
        <button className="btn primary" style={{ width: "100%" }} onClick={getQuote}>
          Get my kit and price
        </button>
        {err && <div className="empty" role="alert">{err}</div>}
      </div>

      {q && (
        <>
          <div className="section-title">Your kit</div>
          <div className="card">
            {q.kit.map((k, i) => (
              <div key={i} style={{ display: "flex", justifyContent: "space-between", fontSize: 13, padding: "4px 0" }}>
                <span>{k.qty} x {k.item}</span>
                <span style={{ fontFamily: "var(--font-mono)" }}>${(k.qty * k.unit).toFixed(0)}</span>
              </div>
            ))}
            <div style={{ display: "flex", justifyContent: "space-between", fontSize: 13, padding: "4px 0", color: "var(--muted)" }}>
              <span>Professional install ({q.install_time_hr} hr est.)</span>
              <span style={{ fontFamily: "var(--font-mono)" }}>${q.install.toFixed(0)}</span>
            </div>
            <div style={{
              display: "flex", justifyContent: "space-between", fontWeight: 700,
              borderTop: "1px solid var(--line)", marginTop: 6, paddingTop: 8,
            }}>
              <span>Total installed (est.)</span>
              <span style={{ fontFamily: "var(--font-mono)" }}>${q.total_installed.toFixed(0)}</span>
            </div>
            <div style={{ fontSize: 11, color: "var(--muted)", marginTop: 6 }}>
              No contracts. Core plan is $0 forever and nothing leaves your house.
            </div>
          </div>

          <div className="section-title">Power check ({q.power.rail_v}V)</div>
          <div className="card" style={{ fontSize: 12 }}>
            {q.power.terminals ? (
              <>
                {q.power.terminals.map((t, i) => (
                  <div key={i} style={{ padding: "3px 0", display: "flex", gap: 8 }}>
                    <span style={{ fontFamily: "var(--font-mono)" }}>T{t.terminal}</span>
                    <span style={{ flex: 1 }}>{t.node}</span>
                    <span style={{ color: t.needs_injection ? "var(--red)" : "var(--green)", fontWeight: 600 }}>
                      {t.needs_injection ? "inject" : `${t.v_at_node}V ok`}
                    </span>
                  </div>
                ))}
                {injections > 0 &&
                  <div style={{ color: "var(--red)", marginTop: 4 }}>
                    {injections} injection kit(s) included above.</div>}
              </>
            ) : (
              <div>
                48V rail: {q.power.budget.total_w}W of {q.power.budget.supply_w}W,
                headroom {q.power.budget.headroom_pct}%
                {q.power.budget.meets_45pct_target ? " (meets 45% target)" : ""}.
              </div>
            )}
          </div>

          <div className="section-title">Identity coverage</div>
          <div className="card">
            <CoverageRings plan={q.dori_plan} />
            <div style={{ fontSize: 11, color: "var(--muted)" }}>
              {q.dori_plan[0].identity_channel.verdict}
            </div>
          </div>
        </>
      )}
    </main>
  );
}
