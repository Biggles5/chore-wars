# OTA Update Pipeline

Design for firmware delivery and rollback across the SightLine fleet. Applies to node firmware (ESP32-S3 class at the bench, edge-AI SoC in production) and gateway software. The firmware OTA hook and signature-check point already exist in the node codebase.

## Pipeline stages

### 1. Build
- CI builds every release candidate from a tagged commit on a pinned platform (locked toolchain, locked dependency hashes).
- Build output: firmware image + manifest (version, target hardware ID, minimum-compatible hardware rev, security floor version, SHA-256 of image).
- Reproducibility check: two independent CI runners must produce byte-identical images before a candidate can advance.

### 2. Sign
- Offline signing key, ed25519 (est.). Key never touches CI or any network-connected host.
- Signing is a manual, logged step: release engineer takes the manifest + image hash to the signing station, produces a detached signature over (image hash, version, target, security floor).
- Public verification key is baked into node firmware at manufacture. Key rotation requires a signed rotation record chained from the prior key.

### 3. Stage (canary rings)
- Ring 0: employee homes. Minimum soak 72 h.
- Ring 1: 5% of fleet, selected across hardware revs, climates, and Wi-Fi conditions. Minimum soak 72 h.
- Ring 2: full fleet.
- Advancement criteria per ring: zero auto-rollbacks attributable to the image, telemetry health (temp_c, power.draw_w, wifi_rssi_dbm, uptime) within one standard deviation of pre-update baseline, no new crash signatures.
- Any ring failure halts the release. Restart requires a new build.

### 4. Deliver
- Gateway pulls the release from the update service, verifies the signature and hash locally before offering anything downstream.
- Gateway offers the update to nodes over the MQTT ota topic. Nodes download in chunks from the gateway (LAN, no per-node WAN pull).
- Node writes the image to the inactive slot of its A/B partition scheme, verifies the signature and hash again on-device at the marked signature-check point, then marks the new slot bootable-pending.
- Reboot is scheduled, not immediate. See "What can never happen."

### 5. Verify
- Node boots the new slot in pending state.
- Within 5 min the node must publish healthy telemetry (sightline.telemetry.v1: sane uptime, expected fw_version, rail voltage and draw in range, MQTT session established).
- On success the node commits the slot as primary.
- On failure (no telemetry, watchdog trip, self-test fail) the bootloader auto-rolls back to the previous slot on next boot.

### 6. Rollback
- Automatic: watchdog boot loop (3 failed boots) or failed 5 min health check reverts to the previous slot and reports fw_version of the old image with a rollback flag in telemetry.
- Manual: fleet-wide halt switch at the update service. Halt stops all gateway offers immediately; nodes already committed stay put, nodes pending revert at next check-in.
- Rolled-back nodes are quarantined from re-offer of the same version.

## Update state machine (node)

1. IDLE: running committed slot, no update in progress.
2. OFFERED: gateway has advertised a version newer than fw_version.
3. DOWNLOADING: chunked transfer to inactive slot, resumable.
4. VERIFYING: on-device signature + hash check of the inactive slot.
5. STAGED: inactive slot verified, reboot scheduled.
6. BOOT_PENDING: rebooted into new slot, health check running (5 min window).
7. COMMITTED: health passed, new slot is primary. Return to IDLE.
8. ROLLED_BACK: health or boot failed, previous slot restored, event reported. Return to IDLE.
9. HALTED: fleet halt active, all transitions frozen except rollback.

Illegal transitions (anything skipping VERIFYING, or entering BOOT_PENDING without STAGED) hard-fail to ROLLED_BACK.

## What can never happen

- No unsigned or badly signed image ever executes. Signature verification happens at the gateway and again on the node. A hash match alone is not sufficient.
- No downgrade below the security floor. The manifest carries a floor version; nodes refuse any image whose version is below their stored floor, even if correctly signed. The floor only ratchets up.
- No update during an active deter or open story. If the node is running a zone-follow strobe, or the gateway correlator has an open Event Story involving the node, the reboot is deferred until the deter ends and the story closes. Security function always outranks maintenance.
- No silent version changes. Every slot commit and rollback appears in telemetry and the fleet dashboard.
- No single-actor release. Build (CI) and sign (offline key holder) are separate parties; neither alone can ship an image.

Proprietary. (c) 2026 Ryan Brown / SightLine. All rights reserved.
