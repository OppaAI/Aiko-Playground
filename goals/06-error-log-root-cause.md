# Goal 06 — Error-log root-cause analysis

**Status:** todo

Read her own error logs, find what's actually breaking, determine root causes, and propose solutions — then report them to Oppa.

## Background

The box has real logs with real recurring failures (e.g. cudaMalloc OOM warnings in the MioTTS logs, past nightly-reflection cascades, thinking-budget burn-throughs). This goal turns log-reading from a chore Oppa does into something she does herself.

## Task

Build `work/06-logdoc/logdoc.py`:

1. Scan the log locations she knows about (Aiko-chan logs, TTS logs, scheduler logs — discover, don't hardcode blindly; list what was found and what was missing).
2. Extract ERROR/WARNING/exception lines from the last 7 days, cluster near-duplicates (normalize timestamps, PIDs, memory addresses), and count occurrences.
3. For the top 5 clusters, write in `REPORT.md`: what the error is, how often it happens, the suspected root cause with evidence (log excerpts), and a concrete proposed fix — each labeled `fix-in-aikochan` (needs a PR, Oppa's call) or `fix-here` (she can prototype it in the playground).
4. Save the clustered data as `errors.json` so trends can be compared on the next run.

## Acceptance criteria

- [ ] `errors.json` contains clustered errors with counts, first/last seen, and example lines.
- [ ] Report covers the top 5 clusters with root-cause reasoning tied to actual log excerpts — no invented errors.
- [ ] Every proposed fix is labeled `fix-in-aikochan` or `fix-here`, and nothing in Aiko-chan is modified by this goal.
- [ ] The script is re-runnable: a second run 24h later produces a comparable `errors.json` (document the comparison in the report if she gets to run it twice).
