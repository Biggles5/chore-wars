// SightLine app dev config. Proxies the correlator and the sim view so the
// app runs same-origin at :5173 with zero CORS setup.
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": {
        target: "http://localhost:8091",
        rewrite: p => p.replace(/^\/api/, ""),
      },
      "/ws": { target: "ws://localhost:8091", ws: true },
      "/sim": {
        target: "http://localhost:8090",
        rewrite: p => p.replace(/^\/sim/, ""),
      },
    },
  },
});
