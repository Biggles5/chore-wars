# Evidence policy

Native pixels only. The AI narrates. It never touches an image.

## The rule

Any frame that can enter an evidence path is unmodified sensor output: no AI enhancement, no super-resolution, no interpolation, no "cleanup." The schemas enforce it (`media.native_pixels` must be true, `media.synthetic` must be false, and a story's `evidence_exportable` is true only when every referenced frame passes both). The simulator can never produce evidence by construction.

## Why: State v. Puloka (2024)

A Washington court excluded AI-enhanced video because the enhancement invents pixels the sensor never captured; the output is the model's opinion of what the scene looked like. Every vendor pushing "AI-enhanced clarity" is manufacturing exhibits that lose. SightLine's optics budget (the identity channel's 250 px/m at a measured pitch) exists so the NATIVE frame is good enough. That is the entire point of the dual-sensor design: engineering the capture instead of hallucinating it afterward.

## What the AI does instead

The narrator turns the story's structured facts into prose: timestamps, zones, DORI grades, deter outcomes. It cites frame times, invents no visual details (guardrails in `agents/narrator/prompts/`), and its output is labeled as narrative, never as evidence.

## Chain of custody for clips

1. Frame/clip is written once to the node loop with a per-frame hash (SHA-256) recorded in the event.
2. Export bundles: clip segments + frames + a manifest (hashes, node serial, fw version, timestamps, timezone, mask regions active at capture) + the story JSON + narrator summary marked NARRATIVE.
3. The gateway signs the manifest; verification tooling ships with the export.
4. Every export is logged to the owner (who, what story, when).

## Police export format

A single archive: `story.json`, `manifest.json` (signed), `media/` (native frames + clips), `NARRATIVE.txt` (marked as AI-generated summary, not evidence), `VERIFY.md` (how to check hashes and the signature). No viewer app required; standard formats only (H.264/JPEG).

## Red lines

- No AI-modified imagery in an export, ever, including "for clarity."
- No export when `evidence_exportable` is false; the app explains why instead of quietly degrading.
- Masked regions are absent from capture; they cannot be exported because they never existed.
