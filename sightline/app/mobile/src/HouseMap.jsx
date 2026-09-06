// Mini top-down house map rendered from the scan, shared by Home and Event.
// Pure SVG, no canvas: cheap, crisp, printable.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React from "react";

const CLASS_COLOR = {
  person: "var(--red)", vehicle: "var(--amber)", animal: "var(--green)",
  package: "var(--blue)", unknown: "var(--ink)",
};

export default function HouseMap({ site, height = 190, highlightZones = [], deterSegs = [], marks = [] }) {
  if (!site) return <div className="map-wrap empty" style={{ height }}>map offline (start the sim)</div>;
  const xs = [], ys = [];
  for (const z of site.zones) for (const p of z.poly) { xs.push(p[0]); ys.push(p[1]); }
  for (const p of site.footprint) { xs.push(p[0]); ys.push(p[1]); }
  const pad = 1.5;
  const x0 = Math.min(...xs) - pad, x1 = Math.max(...xs) + pad;
  const y0 = Math.min(...ys) - pad, y1 = Math.max(...ys) + pad;
  const W = 360, H = height;
  const s = Math.min(W / (x1 - x0), H / (y1 - y0));
  const X = x => (x - x0) * s + (W - s * (x1 - x0)) / 2;
  const Y = y => H - ((y - y0) * s + (H - s * (y1 - y0)) / 2);
  const pts = arr => arr.map(p => `${X(p[0])},${Y(p[1])}`).join(" ");

  return (
    <div className="map-wrap">
      <svg viewBox={`0 0 ${W} ${H}`} width="100%" role="img" aria-label="House map">
        {site.zones.map(z => (
          <polygon key={z.id} points={pts(z.poly)}
            fill={highlightZones.includes(z.id) ? "rgba(194,69,69,0.12)" : "#F2F0E9"}
            stroke="#E4E1D8" strokeWidth="1" />
        ))}
        <polygon points={pts(site.footprint)} fill="#fff" stroke="var(--ink)" strokeWidth="2" />
        {site.segments.map(seg => (
          <line key={seg.id}
            x1={X(seg.from[0])} y1={Y(seg.from[1])} x2={X(seg.to[0])} y2={Y(seg.to[1])}
            stroke={deterSegs.includes(seg.id) ? "var(--red)" : "var(--amber)"}
            strokeWidth={deterSegs.includes(seg.id) ? 5 : 3} strokeLinecap="round">
            {deterSegs.includes(seg.id) &&
              <animate attributeName="opacity" values="1;0.25;1" dur="0.5s" repeatCount="indefinite" />}
          </line>
        ))}
        {site.nodes.map(n => (
          <g key={n.id}>
            <circle cx={X(n.pos[0])} cy={Y(n.pos[1])} r="5"
              fill={n.kind === "door" ? "var(--green)" : "var(--blue)"} stroke="#fff" strokeWidth="1.5" />
          </g>
        ))}
        {marks.map((m, i) => (
          <circle key={i} cx={X(m.x)} cy={Y(m.y)} r="5.5"
            fill={CLASS_COLOR[m.cls] || "var(--ink)"} stroke="#fff" strokeWidth="1.5" />
        ))}
      </svg>
    </div>
  );
}
