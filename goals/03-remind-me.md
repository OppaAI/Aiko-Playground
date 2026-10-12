# Goal 03 — "Remind me in X" natural-language reminders

**Status:** todo

"Remind me in 20 minutes to check the oven" should just work: parse the delay, plant a schedule job, fire once. Small, high-utility, sharply verifiable.

## Background

Aiko has persistent schedule jobs with reminders, but setting one requires structured fiddling. Oppa thinks in "in 20 minutes" / "tomorrow at 9" / "every weekday at 8". A thin parser bridging casual phrasing to one-shot schedule records closes the gap.

## Task

Build `work/03-remind-me/parse.py` that:

1. Parses relative ("in 20 minutes", "in 3 hours"), absolute ("tomorrow at 9am", "Friday evening"), and recurring ("every weekday at 8") phrasings into a fire time (+ recurrence rule or null).
2. Exposes `parse_reminder(text) -> {fire_at, recurrence, task}` with clear errors for unparseable input (never guess a time silently).
3. Includes a test battery of ≥20 phrasings (including 5 adversarial/ambiguous ones that must return errors, not guesses).
4. Writes `REPORT.md` with the supported grammar, the 20-case battery and results.

## Acceptance criteria

- [ ] Runs in the sandbox; 20-case battery passes (15 parse correctly, 5 correctly refuse).
- [ ] No silent guessing: ambiguous input returns an error naming what's missing.
- [ ] REPORT.md documents the grammar + battery results.
- [ ] `PLAN.md` exists first: research (existing schedule-record format, datetime handling), design, test and verification steps.
