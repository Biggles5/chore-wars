# SightLine node firmware (ESP32-S3)

PlatformIO project. Builds with no hardware attached:

```bash
pio run
```

## What is real

- MQTT publishing that matches `sightline.event.v1` and `sightline.telemetry.v1` byte for byte (the schemas in `gateway/schemas/` are the contract).
- 30 s telemetry heartbeat, 10 s task watchdog with panic reboot, OTA entry point (signature check hook marked for the signed-OTA rollout), NVS-backed config with a provisioning AP when unconfigured.
- The motion -> detection.start/update/end state machine.
- `media.native_pixels` is always true and `synthetic` always false: firmware never modifies frames. That is the evidence policy in code.

## What is stubbed

- Camera pipeline: bench OV5640 gated behind `-DSIGHTLINE_HAS_CAMERA` so CI builds need no sensor stack. The production dual-sensor path runs on the edge-AI SoC, not the S3; the S3 build is the bench rig and the deter/telemetry sidecar.
- Motion detection: frame-diff placeholder, fires nothing without a camera. The perimeter simulator stands in for this whole path end to end.
- Timestamps: uptime-based until SNTP lands with provisioning.

## Pinned versions

`espressif32@6.7.0`, PubSubClient 2.8, ArduinoJson 7. Pinning is deliberate: the "compiles in CI" claim dies the day an unpinned platform update breaks the build.
