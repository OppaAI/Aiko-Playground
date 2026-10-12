# Goal 02 — Weekly memory recap email

**Status:** todo

Every Sunday, one email: the week's highlights from Oppa's memories. Small, verifiable, uses existing memory + email paths.

## Background

Memories accumulate silently — Oppa never sees what she kept. A weekly recap (most salient pins, new facts learned, open loops still open) makes the memory system legible and gives him a natural moment to correct her ("that's wrong" / "forget that").

## Task

Build `work/02-weekly-recap/recap.py` that:

1. Reads the week's memories (last 7 days, pinned first, then by salience/importance).
2. Picks at most 7 highlights: new durable facts, completed loops, still-open loops.
3. Renders a short email (subject + ≤250-word body, warm tone, one correction invitation line at the end).
4. Writes `sample_email.md` from fixture data plus a `REPORT.md` with the selection rule documented.

## Acceptance criteria

- [ ] Runs in the sandbox on fixture data; output email ≤250 words.
- [ ] Selection rule documented and deterministic (same fixtures → same picks).
- [ ] REPORT.md includes the sample email and the send path (which email tool, whose approval).
- [ ] `PLAN.md` exists first: research (memory query paths, email send path), design, test and verification steps.
