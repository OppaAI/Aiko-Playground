# Goal 01 — Neuron signal simulation

**Status:** todo

Simulate how signals move through Aiko's fly-inspired circuits and draw it with matplotlib, so the abstract module names become something you can *see*.

## Background

Aiko's fly brain is a set of modulatory circuits around her LLM core: antennal lobe (smell preprocessing), mushroom body (associative memory vote), central complex (heading/urgency integration), giant fiber (startle interrupt), lateral horn, and descending-neuron drive. The real dynamics live in `cognition/fly_behavior/` (Phases 7, 10A, 11):

- Heading: `heading(t+1) = clip2(heading(t)·D_H + cue(t)·G_H)`
- Urgency: `urgency(t+1) = clip01(urgency(t)·D_U + fresh(t)·G_U)`
- Drive: `drive(t+1) = clip01(drive(t)·D_d + input(t)·G_d)`
- Dopamine-gated learning (10A): `E ← clip(E + α(r−E), −1, 1)`, `da ← clip(da·0.6 + RISE·pe, −1, 1)`, `e ← e·0.5^(1/6)`, `Δ = clip(da·e·LR, −1, 1)`

## Task

Write a self-contained Python script (`work/01-neuron-signals/sim.py`) that:

1. Simulates a small network: cue input → antennal-lobe-ish preprocessing → mushroom body vote (MB, CX, DN, GF weights 0.40/0.20/0.20/0.20) → central-complex heading/urgency integration → descending-neuron drive output, with a giant-fiber interrupt that fires on a startle cue and resets the drive.
2. Runs it over ~200 timesteps with a scripted cue sequence (calm → interesting cue → startle → calm).
3. Draws with matplotlib: one figure with stacked time-series (cue, heading, urgency, drive, dopamine), and a second figure showing the network as a simple directed graph with edge thickness ∝ mean signal over the run.
4. Saves both figures as PNGs plus a short `REPORT.md` explaining in plain words what the simulation shows.

## Acceptance criteria

- [ ] `sim.py` runs in the sandbox with no errors and finishes in under 60 seconds.
- [ ] Both PNGs are produced and are readable (axes labeled, title, legend).
- [ ] The giant-fiber interrupt visibly resets drive in the plots when the startle cue fires.
- [ ] `REPORT.md` explains the signal path in plain language, one paragraph per circuit.
- [ ] No imports beyond the standard library, numpy, and matplotlib (check what's on the Jetson first; if matplotlib is missing, note it in the report and fall back to a pure-Python SVG plot — still counts if the fallback is readable).
