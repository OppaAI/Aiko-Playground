# Goal 03 — ASR/TTS latency benchmark

**Status:** todo

Find the fastest reliable speech path: measure ASR (speech-to-text) and TTS (text-to-speech) options on the Jetson and pick the optimum speed with the least latency.

## Background

Voice has been flaky — TTS cutouts that may be GPU contention (cudaMalloc OOM warnings in the MioTTS logs), and the general question of which engine/settings give the best latency without dropping quality. Stop guessing; measure.

## Task

Build `work/03-voice-bench/bench.py` that:

1. Discovers which ASR/TTS mechanisms are actually installed/available on the box (check imports, binaries, running servers — don't assume).
2. For each available mechanism, measures over N=10 runs with a fixed test sentence:
   - Time to first audio byte (TTFB) and total synthesis time (TTS).
   - Transcription time for a fixed test clip (ASR).
   - Peak GPU memory / obvious contention signals if observable.
3. Writes results to `results.json` and draws a bar chart (mechanism × latency, with error bars) to `bench.png`.
4. Writes `REPORT.md`: ranked table (fastest → slowest), the recommended default with reasons, and any mechanism that should be disabled or avoided.

## Acceptance criteria

- [ ] Benchmark runs in the sandbox; each mechanism gets ≥10 timed runs; results saved as JSON.
- [ ] Chart shows mean latency with error bars per mechanism.
- [ ] Report names one recommended ASR and one recommended TTS with measured numbers, plus one mechanism to avoid and why.
- [ ] Nothing is *changed* in Aiko-chan's config — this goal only measures and recommends. Applying the recommendation is Oppa's call.
