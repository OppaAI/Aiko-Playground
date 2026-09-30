# Session log template

One section like this is appended to `work/<slug>/LOG.md` for every work
session. Copy it, fill it in, commit it. The log is how Oppa follows your
work — write it like a lab notebook: what you did, what the machine said
back, and what you concluded.

```markdown
## Session 2026-09-30 14:05–14:50 PDT

- **Start:** 2026-09-30 14:05 PDT (tick fired after 12 idle minutes)
- **Resuming:** previous session ended 2026-09-30 13:58 PDT — time box
  reached; picking up step 3 from CHECKPOINT.md
- **Plan:** get the FFT peak detector passing on the noisy fixture.

### Code generated

- `work/neuron-signal/peak.py` — rewrote `find_peaks` to use an FFT
  band-pass before thresholding. Reason: time-domain thresholding fired on
  noise spikes at SNR < 3; the band-pass isolates the 5–20 Hz spike band.
  (Full code lives in the file; this log records the *why*, not the diff.)

### Research

- Web search "scipy find_peaks distance vs prominence noisy signal" →
  learned `prominence` is more robust than raw height for noisy data;
  switched the detector to prominence-based picking.

### Sandbox runs

1. `sandbox/run.py work/neuron-signal/test_peak.py` — exit 1.
   Error: `ModuleNotFoundError: No module named 'numpy'` — sandbox image
   has no numpy. Fix: rewrote the filter with pure-python math in
   `work/neuron-signal/dsp.py`.
2. `sandbox/run.py work/neuron-signal/test_peak.py` — exit 0.
   6/6 fixtures pass, worst-case SNR 2.5 detected at 94%.

### Self-verification

- [x] Criterion 1 "detects synthetic spikes at SNR>=3" — test_peak.py 6/6.
- [ ] Criterion 2 "matplotlib plot saved" — not attempted this session.

### End

- **End:** 2026-09-30 14:50 PDT — reason: 45-minute box reached.
- **Next:** generate the plot and save `work/neuron-signal/plot.png`.
```

## End reasons (use exactly these words)

- `goal done` — acceptance criteria all verified, REPORT.md written.
- `time box reached` — 45 minutes up, checkpointed cleanly.
- `user active` — the human started interacting; wrapped up immediately.
- `kill switch` — `loop/disabled` appeared; stood down.
- `blocked` — cannot proceed without Oppa (missing info/permission);
  what is needed goes in CHECKPOINT.md.

The next session's **Resuming** line must reference the previous **End**
line. Together they form the unbroken interrupted → continued chain.
