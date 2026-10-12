# Goal 01 — Morning voice briefing

**Status:** todo

When Oppa starts the day, one spoken summary: today's schedule, overnight mentions count, and anything due. Small, daily-visible, verifiable.

## Background

Aiko already has all the parts: schedule records, social monitor daemons that count overnight mentions, and TTS. Nobody wires them into a single "good morning" turn. Oppa starts most days by asking what's on — this answers before he asks.

## Task

Build `work/01-morning-briefing/brief.py` that:

1. Reads today's schedule records (title + time) for Oppa's user id.
2. Counts overnight social mentions/replies since 22:00 (per-platform counts only, no content fetch).
3. Lists items due today (anything with today's date in schedule records).
4. Renders one short spoken script (≤120 words, greeting + schedule + mentions + due items, skip empty sections silently).
5. Writes the script to `brief.txt` plus a `REPORT.md` with a sample script from test fixtures.

## Acceptance criteria

- [ ] Runs in the sandbox using fixture data (no live services needed for the test).
- [ ] Script stays under 120 words and skips empty sections without awkward gaps.
- [ ] REPORT.md shows a sample briefing and documents the real-data wiring points.
- [ ] `PLAN.md` exists first: research (how schedule records + mention counts are read), design, test and verification steps.
