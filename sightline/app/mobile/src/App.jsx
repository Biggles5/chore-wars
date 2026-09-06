// SightLine app shell: 390px phone frame, top bar, tab bar, view switch.
// Sprint 2: Home + Verified Event live. Ask, Scenes, Setup land in Sprint 3.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import React, { useState } from "react";
import { useLive, useSite } from "./api.js";
import Home from "./screens/Home.jsx";
import EventScreen from "./screens/Event.jsx";
import Ask from "./screens/Ask.jsx";
import Scenes from "./screens/Scenes.jsx";
import Setup from "./screens/Setup.jsx";
import { t } from "./i18n.js";

const TABS = [
  { id: "home", label: t("tab.home"), ico: "⌂" },
  { id: "ask", label: t("tab.ask"), ico: "?" },
  { id: "scenes", label: t("tab.scenes"), ico: "◧" },
  { id: "setup", label: t("tab.setup"), ico: "✚" },
];

export default function App() {
  const { stories, byId, events, connected } = useLive();
  const site = useSite();
  const [tab, setTab] = useState("home");
  const [storyId, setStoryId] = useState(null);

  const inStory = (tab === "home" || tab === "ask") && storyId;
  const armed = site ? site.scenario.armed : false;

  return (
    <div className="phone">
      <div className="topbar">
        {inStory
          ? <button className="back" aria-label="Back" onClick={() => setStoryId(null)}>‹</button>
          : null}
        <span className="brand">SIGHTLINE</span>
        <span style={{ flex: 1 }} />
        <span className={"chip " + (armed ? "armed" : "disarmed")} role="status">
          {armed ? t("chip.armed") : t("chip.home")}
        </span>
        <span className={"chip " + (connected ? "live" : "offline")} role="status">
          {connected ? t("chip.live") : t("chip.offline")}
        </span>
      </div>

      {tab === "home" && !inStory &&
        <Home site={site} stories={stories} events={events}
          openStory={id => setStoryId(id)} />}
      {inStory && <EventScreen site={site} story={byId[storyId]} />}
      {tab === "ask" && !inStory && <Ask openStory={id => setStoryId(id)} />}
      {tab === "scenes" && <Scenes site={site} />}
      {tab === "setup" && <Setup />}

      <nav className="tabbar">
        {TABS.map(t => (
          <button key={t.id} className={tab === t.id ? "active" : ""}
            onClick={() => { setTab(t.id); setStoryId(null); }}>
            <span className="ico" aria-hidden="true">{t.ico}</span>{t.label}
          </button>
        ))}
      </nav>
    </div>
  );
}
