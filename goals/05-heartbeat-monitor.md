# Goal 05 — Heartbeat / internet availability monitor

**Status:** todo

A small heartbeat system that tests whether the box can reach the internet, and keeps a log so outages are visible instead of mysterious.

## Task

Build `work/05-heartbeat/heartbeat.py`:

1. Every 60 seconds: DNS-resolve two hosts, TCP-connect (port 443) to two endpoints, and HTTPS-GET one small URL — with short timeouts (5s each).
2. Append one JSON line per check to `heartbeat.log`: timestamp, per-target ok/fail + latency ms, and an overall `up: true/false`.
3. Keep a 24-hour summary in `summary.json`: uptime %, longest outage, last 10 state changes.
4. Handle "no network at all" without crashing or spinning (back off, keep logging).
5. `REPORT.md`: what it checks and why those targets, how to read the log, and the uptime % measured over its first 24 hours of running.

## Acceptance criteria

- [ ] Runs for 24 hours unattended without crashing; log has no gaps larger than 3 minutes except during real outages (which must themselves be logged).
- [ ] `summary.json` is valid JSON with uptime %, longest outage, and recent state changes.
- [ ] A simulated outage (e.g. blocking egress briefly, or pointing one target at an unroutable IP in a test run) is detected and appears in the log — prove the detector actually detects.
- [ ] Pure stdlib, one file, one command to start.
