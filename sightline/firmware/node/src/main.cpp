// SightLine node firmware skeleton (ESP32-S3).
//
// What is real here: MQTT event publishing that matches sightline.event.v1
// and sightline.telemetry.v1 exactly, heartbeat cadence, watchdog, OTA
// hook, captive-portal config entry point, and the motion->event state
// machine. What is stubbed: the camera pipeline (bench OV5640 behind
// SIGHTLINE_HAS_CAMERA) and motion detection (frame-diff placeholder that
// synthesizes no events unless the camera is present).
//
// Compiles with `pio run` and no hardware attached.
//
// Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.

#include <Arduino.h>
#include <WiFi.h>
#include <ArduinoOTA.h>
#include <esp_task_wdt.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>
#include <Preferences.h>

#ifndef SIGHTLINE_FW_VERSION
#define SIGHTLINE_FW_VERSION "0.3.0-dev"
#endif

// ---------- configuration (captive portal writes these to NVS) ----------
struct Config {
  String wifi_ssid;
  String wifi_pass;
  String mqtt_host;
  uint16_t mqtt_port = 1883;
  String site_id = "site-unset";
  String node_id = "node-unset";
};
static Config cfg;
static Preferences prefs;

static void loadConfig() {
  prefs.begin("sightline", true);
  cfg.wifi_ssid = prefs.getString("ssid", "");
  cfg.wifi_pass = prefs.getString("pass", "");
  cfg.mqtt_host = prefs.getString("mqtt", "gateway.local");
  cfg.mqtt_port = prefs.getUShort("mqtt_port", 1883);
  cfg.site_id = prefs.getString("site", "site-unset");
  cfg.node_id = prefs.getString("node", String("node-") + String((uint32_t)ESP.getEfuseMac(), HEX));
  prefs.end();
}

// Captive portal: if no stored SSID, come up as an AP named after the node
// serial so the installer app can push config. Full portal UI ships with
// the provisioning sprint; the entry point and NVS layout are final.
static void maybeStartProvisioningAP() {
  if (cfg.wifi_ssid.length() > 0) return;
  WiFi.mode(WIFI_AP);
  WiFi.softAP((String("SightLine-") + cfg.node_id).c_str());
  Serial.println("[prov] no config: provisioning AP up");
}

// ---------- camera (bench OV5640, gated) ----------
#ifdef SIGHTLINE_HAS_CAMERA
#include "esp_camera.h"
static bool cameraInit() {
  camera_config_t cc = {};  // pin map for the bench carrier lands with the CAD
  cc.frame_size = FRAMESIZE_QSXGA;
  cc.pixel_format = PIXFORMAT_JPEG;
  cc.jpeg_quality = 12;
  cc.fb_count = 2;
  return esp_camera_init(&cc) == ESP_OK;
}
#else
static bool cameraInit() { return false; }  // no sensor on CI builds
#endif

// ---------- motion -> event state machine ----------
enum TrackState { IDLE, TRACKING };
static TrackState trackState = IDLE;
static uint32_t trackStartMs = 0;
static uint32_t trackSeq = 0;
static uint32_t lastUpdateMs = 0;

// Frame-diff placeholder: returns true while motion is present. On CI
// builds (no camera) it never fires; the perimeter simulator stands in for
// this whole path end to end.
static bool motionDetected() {
#ifdef SIGHTLINE_HAS_CAMERA
  // TODO(bench): luma delta over a 16x16 grid on the wide channel
  return false;
#else
  return false;
#endif
}

// ---------- MQTT ----------
static WiFiClient net;
static PubSubClient mqtt(net);

static String topic(const char* leaf) {
  return String("sightline/") + cfg.site_id + "/" + cfg.node_id + "/" + leaf;
}

static String isoTimestamp() {
  // Real builds sync SNTP during provisioning; skeleton emits uptime-based
  // placeholder timestamps that the gateway rewrites on ingest if unset.
  char buf[40];
  uint32_t s = millis() / 1000;
  snprintf(buf, sizeof(buf), "1970-01-01T%02u:%02u:%02u+00:00",
           (unsigned)(s / 3600 % 24), (unsigned)(s / 60 % 60), (unsigned)(s % 60));
  return String(buf);
}

static void publishEvent(const char* type, float confidence) {
  JsonDocument doc;
  doc["schema"] = "sightline.event.v1";
  doc["event_id"] = String((uint32_t)esp_random(), HEX) + String((uint32_t)esp_random(), HEX);
  doc["site_id"] = cfg.site_id;
  doc["node_id"] = cfg.node_id;
  doc["ts"] = isoTimestamp();
  doc["type"] = type;
  JsonObject obj = doc["object"].to<JsonObject>();
  obj["class"] = "unknown";  // classifier lands on the edge SoC, not the S3
  obj["confidence"] = confidence;
  obj["track_id"] = cfg.node_id + ":t" + String(trackSeq);
  JsonObject media = doc["media"].to<JsonObject>();
  media["native_pixels"] = true;   // firmware never modifies frames, ever
  media["synthetic"] = false;
  String out;
  serializeJson(doc, out);
  mqtt.publish(topic("event").c_str(), out.c_str());
}

static void publishTelemetry() {
  JsonDocument doc;
  doc["schema"] = "sightline.telemetry.v1";
  doc["site_id"] = cfg.site_id;
  doc["node_id"] = cfg.node_id;
  doc["ts"] = isoTimestamp();
  doc["uptime_s"] = millis() / 1000.0;
  doc["fw_version"] = SIGHTLINE_FW_VERSION;
  doc["temp_c"] = temperatureRead();
  doc["heater_on"] = false;
  doc["wifi_rssi_dbm"] = WiFi.RSSI();
  JsonObject power = doc["power"].to<JsonObject>();
  power["rail_v"] = 12.0;   // INA219 on the bench carrier reads the real rail
  power["draw_w"] = 0.0;
  String out;
  serializeJson(doc, out);
  mqtt.publish(topic("telemetry").c_str(), out.c_str());
}

static void mqttEnsure() {
  if (mqtt.connected() || WiFi.status() != WL_CONNECTED) return;
  mqtt.setServer(cfg.mqtt_host.c_str(), cfg.mqtt_port);
  mqtt.connect(cfg.node_id.c_str());
}

// ---------- OTA ----------
static void otaSetup() {
  ArduinoOTA.setHostname(cfg.node_id.c_str());
  // Production: signed images only; verify signature in onStart before
  // accepting (docs/architecture/security.md). Hook is in place.
  ArduinoOTA.onStart([]() { Serial.println("[ota] start"); });
  ArduinoOTA.onEnd([]() { Serial.println("[ota] done"); });
  ArduinoOTA.begin();
}

// ---------- main ----------
static uint32_t lastTelemetryMs = 0;

void setup() {
  Serial.begin(115200);
  esp_task_wdt_init(10, true);       // 10 s watchdog, panic -> reboot
  esp_task_wdt_add(nullptr);

  loadConfig();
  maybeStartProvisioningAP();
  if (cfg.wifi_ssid.length() > 0) {
    WiFi.mode(WIFI_STA);
    WiFi.begin(cfg.wifi_ssid.c_str(), cfg.wifi_pass.c_str());
  }
  cameraInit();
  otaSetup();
  Serial.printf("[boot] %s fw %s\n", cfg.node_id.c_str(), SIGHTLINE_FW_VERSION);
}

void loop() {
  esp_task_wdt_reset();
  ArduinoOTA.handle();
  mqttEnsure();
  mqtt.loop();

  uint32_t now = millis();

  if (now - lastTelemetryMs >= 30000) {
    lastTelemetryMs = now;
    if (mqtt.connected()) publishTelemetry();
  }

  bool motion = motionDetected();
  if (motion && trackState == IDLE) {
    trackState = TRACKING;
    trackSeq++;
    trackStartMs = now;
    lastUpdateMs = now;
    if (mqtt.connected()) publishEvent("detection.start", 0.6f);
  } else if (motion && trackState == TRACKING && now - lastUpdateMs >= 4000) {
    lastUpdateMs = now;
    if (mqtt.connected()) publishEvent("detection.update", 0.6f);
  } else if (!motion && trackState == TRACKING && now - lastUpdateMs >= 2000) {
    trackState = IDLE;
    if (mqtt.connected()) publishEvent("detection.end", 0.6f);
  }

  delay(20);
}
