// SightLine i18n stub: English strings inline, Spanish catalog in
// locales/es.json. t(key) resolves by navigator.language. Full extraction
// pass is scheduled work; this proves the mechanism and ships the catalog.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import es from "./locales/es.json";

const EN = {
  "tab.home": "Home", "tab.ask": "Ask", "tab.scenes": "Scenes", "tab.setup": "Setup",
  "chip.armed": "ARMED", "chip.home": "HOME", "chip.live": "LIVE", "chip.offline": "OFFLINE",
  "home.narrator": "Narrator", "home.perimeter": "Perimeter", "home.scenes": "Scenes",
  "home.live": "Live", "home.recent": "Recent",
  "home.quiet": "All quiet. Nothing on the perimeter needed your attention.",
  "event.deter_now": "Deter now", "event.share": "Share clip",
  "event.monitoring": "Send to monitoring", "event.timeline": "Timeline",
  "badge.verified": "Verified", "badge.live": "Live",
};

const CATALOGS = { en: EN, es: { ...EN, ...es } };

function lang() {
  try {
    return (navigator.language || "en").slice(0, 2);
  } catch {
    return "en";
  }
}

export function t(key) {
  const cat = CATALOGS[lang()] || EN;
  return cat[key] || EN[key] || key;
}
