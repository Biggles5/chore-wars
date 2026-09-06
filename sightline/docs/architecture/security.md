# Security architecture

TLS everywhere, per-node identity, signed everything, and a threat model that assumes the node gets stolen.

## Transport

- MQTT over TLS on the gateway broker; per-node client certificates issued at provisioning (gateway CA, offline root).
- App to gateway: TLS with certificate pinning in the app.
- Cloud (Plus/Shield): mTLS gateway-to-cloud; monitoring webhooks signed (HMAC) on top of mTLS.
- Dev mode (this repo's compose) runs open on localhost and says so; production config templates ship locked.

## Identity and keys

- Every node: unique serial (NVS + etched), per-node keypair generated on first boot, certificate bound to serial and site at provisioning.
- Gateway: site CA plus its own cloud identity. Compromise of one node never yields another node's credentials.

## Signed OTA and secure boot roadmap

- Ship: signed OTA images (ed25519 (est.)), A/B slots, auto-rollback (docs/ota-pipeline.md). Version floor: nodes refuse downgrades below the security floor.
- Next: ESP32-S3/edge-SoC secure boot + flash encryption at EVT; measured boot attestation reported in telemetry as the stretch goal.

## Threat model

| Threat | Response |
|---|---|
| Stolen node | microSD loop is encrypted with a per-node key sealed to the device (est. XTS); credentials are device-bound certs the gateway revokes on tamper event; the node is a brick with a lens off its site |
| Wi-Fi jam | reflex deter is local and keeps working; bus pair carries control; jam detection (sudden RSSI floor + heartbeat gap) raises a tamper story itself |
| Cloud breach | Core users lose nothing (no data there); Plus/Shield: 60-day scoped data, per-site encryption keys, no cross-site identity to steal, no face databases exist |
| Insider (SightLine employee) | no standing access to customer video; support access is owner-granted, time-boxed, logged to the owner; cloud stores what the plan syncs, nothing more |
| Malicious app on the LAN | gateway API requires the paired app's token; deter and mask changes require owner auth; masks can narrow only with the owner PIN |
| Supply chain | NDAA-clean silicon lineage documented (docs/compliance/); firmware builds reproducible from pinned CI |

## What we refuse to build

No backdoor access to video, for anyone, including us. No silent firmware features. No remote mask changes without owner-visible audit. These are commitments, and the Core architecture (nothing leaves the house) makes the biggest one structural.
