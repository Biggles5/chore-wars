// Guardian tab: what the brain watched, dismissed, and did, with the
// cost-of-protection meter as a trust feature, plus jurisdiction flags.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React, { useEffect, useState } from "react";
import { fetchJson, clock } from "../api.js";

const ACTION_LABEL = {
  dismiss: ["Dismissed", "var(--muted)"],
  watch: ["Watched", "var(--blue)"],
  notify: ["Notified you", "var(--amber)"],
  intervene: ["Intervened", "var(--red)"],
  handoff: ["Central station", "var(--red)"],
};

function InsuranceCard({ report }) {
  const [note, setNote] = useState("");
  return (
    <div className="card" style={{ fontSize: 12.5 }}>
      <div style={{ marginBottom: 6 }}>
        Many carriers discount monitored, verified perimeters 5 to 15% (est.).
        Export the documentation pack: system specs, armed-hours attestation,
        verified-event summary. No video, no images, aggregates only.
      </div>
      <button className="btn" style={{ width: "100%" }}
        onClick={() => setNote("Documentation pack prepared: coverage attestation, "
          + `${report ? report.events_processed : 0} events summarized, deter outcomes included. `
          + "Share it with your carrier from the files app (demo stub).")}>
        Export for my insurer
      </button>
      {note && <div className="empty" role="status" style={{ padding: "10px 4px 0" }}>{note}</div>}
    </div>
  );
}

export default function Guardian({ stories, openStory }) {
  const [report, setReport] = useState(null);
  const [log, setLog] = useState([]);
  const [flags, setFlags] = useState(null);

  useEffect(() => {
    const load = () => {
      fetchJson("/api/guardian/report").then(setReport).catch(() => {});
      fetchJson("/api/guardian/log").then(setLog).catch(() => {});
      fetchJson("/api/flags").then(setFlags).catch(() => {});
    };
    load();
    const t = setInterval(load, 5000);
    return () => clearInterval(t);
  }, []);

  const guardedHours = 9.4; // armed window last night; live calc in Sprint+1
  const nightCost = report ? Math.max(report.cost_total_usd, 0.001) : 0;

  return (
    <main>
      <div className="narrator">
        <span className="label">Guardian</span>
        {report && report.events_processed > 0
          ? `Your home was guarded ${guardedHours} hours for $${nightCost.toFixed(2)}. ` +
            `${report.events_processed} events reviewed, ` +
            `${(report.actions && report.actions.dismiss) || 0} dismissed quietly, ` +
            `${report.handoffs} sent to the monitoring center.`
          : "Standing watch. Nothing has needed a decision yet."}
      </div>

      <div className="section-title">Cost of protection</div>
      <div className="card" style={{ display: "flex", gap: 14, alignItems: "baseline" }}>
        <span style={{ fontFamily: "var(--font-display)", fontSize: 30, fontWeight: 700, color: "var(--green)" }}>
          ${report ? report.cost_per_home_month_usd_est.toFixed(2) : "0.00"}
        </span>
        <span style={{ fontSize: 12, color: "var(--muted)" }}>
          est. per month at this pace. Incumbent human monitoring: $30 to $80.
          {report && report.under_target ? " Under our $6 target." : ""}
        </span>
      </div>

      <div className="section-title">Decisions</div>
      {log.length === 0 && <div className="empty">No decisions yet tonight.</div>}
      {log.slice().reverse().slice(0, 12).map((e, i) => {
        const [label, color] = ACTION_LABEL[e.action] || [e.action, "var(--ink)"];
        return (
          <div className="card story-row" key={i}
            onClick={() => e.story_id && openStory(e.story_id)}>
            <div className="sev" style={{ background: color }} />
            <div className="body">
              <div className="title" style={{ fontSize: 13 }}>
                {label} <span style={{ color: "var(--muted)", fontWeight: 400 }}>
                  · AVS-{e.avs}</span>
              </div>
              <div className="sub">{clock(e.ts)} · cost ${e.cost_usd.toFixed(4)}</div>
            </div>
          </div>
        );
      })}

      <div className="section-title">Insurance savings</div>
      <InsuranceCard report={report} />

      <div className="section-title">What Guardian may never do</div>
      <div className="card" style={{ fontSize: 12.5, lineHeight: 1.6, color: "var(--muted)" }}>
        Call 911 itself. Claim a crime occurred. Describe anything not in the
        native frames. Deter animals or guests. Keep a face database. The
        licensed central station holds dispatch authority; you always see what
        it saw.
      </div>

      {flags && (
        <>
          <div className="section-title">Your jurisdiction ({flags.jurisdiction})</div>
          <div className="card" style={{ fontSize: 12.5 }}>
            <div style={{ marginBottom: 6 }}>
              Face recognition:{" "}
              <b style={{ color: flags.face_recognition.enabled ? "var(--green)" : "var(--red)" }}>
                {flags.face_recognition.enabled ? "available (local labels only)" : "disabled by law"}
              </b>
              {flags.face_recognition.gated_reason &&
                <div style={{ color: "var(--muted)", marginTop: 2 }}>{flags.face_recognition.gated_reason}</div>}
            </div>
            <div>
              Audio: <b>off by default.</b>{" "}
              <span style={{ color: "var(--muted)" }}>{flags.audio.warning}</span>
            </div>
          </div>
        </>
      )}
    </main>
  );
}
