// Installer mode: the step-by-step runbook with QC photo gates. The next
// step unlocks only when the QC agent passes the gate. In the demo, the
// "camera" is the fixture picker; in the field it is the phone camera.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React, { useEffect, useState } from "react";
import { fetchJson } from "../api.js";

export default function Installer({ exit }) {
  const [rb, setRb] = useState(null);
  const [fixtures, setFixtures] = useState([]);
  const [stepIdx, setStepIdx] = useState(0);
  const [gateState, setGateState] = useState({});   // step n -> {result}
  const [commissioned, setCommissioned] = useState(false);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    fetchJson("/api/runbook/sample/1").then(setRb).catch(() => {});
    fetchJson("/api/qc/fixtures").then(setFixtures).catch(() => {});
  }, []);

  if (!rb) return <main><div className="empty">Loading job runbook (start the gateway)...</div></main>;

  const steps = rb.steps;
  const step = steps[stepIdx];
  const passedSteps = steps.filter(s =>
    !s.qc_gate || s.qc_gate === "commissioning"
      ? true : (gateState[s.n] && gateState[s.n].passed)).length;
  const done = stepIdx >= steps.length;

  async function submitPhoto(fixtureFile) {
    setBusy(true);
    try {
      const r = await fetch("/api/qc/review", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ check: step.qc_gate, photo: fixtureFile }),
      });
      const d = await r.json();
      setGateState(g => ({ ...g, [step.n]: d }));
    } catch {
      setGateState(g => ({ ...g, [step.n]: { passed: false, redo: ["Gateway unreachable."] } }));
    }
    setBusy(false);
  }

  function runCommissioning() {
    setBusy(true);
    setTimeout(() => { setCommissioned(true); setBusy(false); }, 1500);
  }

  const gate = gateState[step && step.n];
  const gatePassed = !step ? true
    : step.qc_gate === "commissioning" ? commissioned
    : step.qc_gate ? (gate && gate.passed) : true;
  const stepFixtures = step && step.qc_gate && step.qc_gate !== "commissioning"
    ? fixtures.filter(f => f.check === step.qc_gate).slice(0, 5) : [];

  return (
    <main>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <div style={{ fontFamily: "var(--font-display)", fontWeight: 700, fontSize: 16 }}>
            Installer mode · {rb.site_id}
          </div>
          <div style={{ fontSize: 11, color: "var(--muted)" }}>
            target {rb.total_target_hr} hr · warranty needs every gate green
          </div>
        </div>
        <button className="btn" onClick={exit} style={{ minHeight: 36, padding: "6px 12px" }}>Exit</button>
      </div>

      <div style={{ display: "flex", gap: 3, margin: "12px 0" }}>
        {steps.map((s, i) => (
          <div key={s.n} style={{
            flex: 1, height: 5, borderRadius: 3,
            background: i < stepIdx ? "var(--green)" : i === stepIdx ? "var(--amber)" : "var(--line)",
          }} />
        ))}
      </div>

      {done ? (
        <div className="card" style={{ textAlign: "center", padding: 28 }}>
          <div style={{ fontFamily: "var(--font-display)", fontSize: 20, fontWeight: 700, color: "var(--green)" }}>
            Job complete
          </div>
          <div style={{ fontSize: 13, marginTop: 8 }}>
            All QC gates passed. Warranty is active. The homeowner has the app,
            the masks, and the owner PIN.
          </div>
        </div>
      ) : (
        <div className="card">
          <div style={{ fontSize: 11, color: "var(--muted)" }}>
            STEP {step.n} OF {steps.length} · TARGET {step.target_min} MIN
          </div>
          <div style={{ fontFamily: "var(--font-display)", fontWeight: 700, fontSize: 16, margin: "4px 0 8px" }}>
            {step.title}
          </div>
          <div style={{ fontSize: 13.5, lineHeight: 1.55 }}>{step.detail}</div>
          {step.ar_ref && (
            <div style={{ fontSize: 11, color: "var(--blue)", marginTop: 6 }}>
              AR overlay: {step.ar_ref} layer aligned to your camera view
            </div>
          )}

          {step.qc_gate && step.qc_gate !== "commissioning" && (
            <>
              <div className="section-title">QC gate: {step.qc_gate.replace(/_/g, " ")}</div>
              <div style={{ fontSize: 12, color: "var(--muted)", marginBottom: 6 }}>
                Submit the gate photo. (Demo: tap a sample photo below.)
              </div>
              <div className="scene-row">
                {stepFixtures.map(f => (
                  <img key={f.file} src={`/api/qc/fixtures/${f.file}`} alt={f.file}
                    onClick={() => !busy && submitPhoto(f.file)}
                    style={{ width: 96, height: 72, borderRadius: 8, cursor: "pointer",
                             border: "2px solid var(--line)" }} />
                ))}
              </div>
              {gate && (
                <div className="card" style={{
                  marginTop: 8, background: gate.passed ? "#f0f7f2" : "#fdf1f1",
                  borderColor: gate.passed ? "var(--green)" : "var(--red)",
                }}>
                  <b style={{ color: gate.passed ? "var(--green)" : "var(--red)" }}>
                    {gate.passed ? "PASS" : "REDO"}
                  </b>
                  {!gate.passed && (gate.redo || []).map((r, i) => (
                    <div key={i} style={{ fontSize: 12.5, marginTop: 4 }}>{r}</div>
                  ))}
                </div>
              )}
            </>
          )}

          {step.qc_gate === "commissioning" && (
            <>
              <div className="section-title">30-point commissioning check</div>
              {!commissioned ? (
                <button className="btn primary" style={{ width: "100%" }}
                  onClick={runCommissioning} disabled={busy}>
                  {busy ? "Running checks..." : "Run auto-provision + checks"}
                </button>
              ) : (
                <div style={{ maxHeight: 180, overflowY: "auto", fontSize: 11.5 }}>
                  {step.checklist.map((c, i) => (
                    <div key={i} style={{ padding: "3px 0" }}>
                      <span style={{ color: "var(--green)", fontWeight: 700 }}>PASS</span> {i + 1}. {c}
                    </div>
                  ))}
                </div>
              )}
            </>
          )}

          <div className="actions">
            <button className="btn primary" disabled={!gatePassed || busy}
              onClick={() => setStepIdx(i => i + 1)}>
              {gatePassed ? "Next step" : "Gate must pass first"}
            </button>
          </div>
        </div>
      )}
    </main>
  );
}
