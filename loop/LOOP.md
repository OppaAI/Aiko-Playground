# The Playground Loop

How Aiko works the goals by herself, in the background, during idle time.

## The idea in one paragraph

When Aiko has nothing else to do, she picks the top unfinished goal, builds it in `work/`, tests it in the sandbox, checks her work against the goal's acceptance criteria, and — only when every box is honestly checked — marks the goal done and emails Oppa a short report with what was built and where it lives. Then she moves to the next goal. She loops like this indefinitely. She never declares a goal done because she's tired of it; "done" means the criteria check out, with the test logs to prove it.

## When does the loop run?

On the Jetson, inside Aiko-chan's scheduler. A `playground_tick()` runs every 15 minutes and asks:

1. Is there an active conversation (last 15 min)? → skip.
2. Is anything else running (agents, dream pipeline, reflection)? → skip.
3. Is system load sane (load avg < 4, GPU not mid-TTS)? → else skip.
4. Is there a `todo` goal? → work. Otherwise → rest.

Each work session is time-boxed (default 45 minutes). When the box ends, she saves state and stops mid-goal cleanly — the next tick resumes.

> **Integration note:** this loop does not exist in Aiko-chan yet. `LOOP.md` is the design; wiring `playground_tick()` into the scheduler is a change to Aiko-chan and goes through the normal PR process with Oppa's approval. Nothing here modifies Aiko-chan on its own.

## One work session

```
tick (idle confirmed)
  → read GOALS.md, pick top `todo` goal → mark `in_progress`
  → read the goal file fully
  → plan (short plan in work/<slug>/PLAN.md)
  → build → sandbox/run.py → read output → fix → repeat
  → self-review: walk the acceptance criteria one by one,
    each with the evidence (test log, PNG path, measured number)
  → if all pass:
      - write work/<slug>/REPORT.md
      - mark goal `done` in GOALS.md + goal file
      - git commit + push to Aiko-Playground
      - email Oppa (loop/notify.py): what was built, key result, links
    else:
      - write work/<slug>/NOTES.md with what's blocking
      - leave goal `in_progress` (or back to `todo` if blocked on Oppa)
  → append session log to runs/<timestamp>-<slug>.md
```

## Rules she follows

1. **Playground only.** She writes inside this repo. She never edits Aiko-chan's source, config, or logs from the loop — she only *reads* them (goals 02, 03, 06 need read access to learn).
2. **Recommend, don't apply.** Anything that would change Aiko-chan (a faster TTS engine, a log fix) goes into the report as a recommendation. Oppa decides.
3. **Honest done.** If a criterion can't be met (missing package, hardware limit), she says so in the report and marks the goal `done-with-caveats` — never silently.
4. **One email per goal.** Not per session, not per attempt. Oppa hears from her when something is finished.
5. **She may propose new goals** in her emails, but she never adds them to `goals/` herself. Oppa adds them.
6. **No secrets in the repo.** Logs she reads may contain paths or machine details — reports summarize, they don't paste raw logs. The notifier config (SMTP password) lives outside the repo, never committed.

## State files

- `GOALS.md` — the index; statuses edited by the loop.
- `goals/NN-*.md` — goal definitions; `**Status:**` line edited by the loop.
- `work/<slug>/` — build area (gitignored except `REPORT.md`, which is committed on completion).
- `runs/` — append-only session logs, committed.

## Configuration

`loop/config.yaml` (not committed; see `config.example.yaml`):

```yaml
tick_minutes: 15
session_minutes: 45
idle_minutes: 15
email:
  to: "oppa.ai.org@proton.me"   # confirm with Oppa
  smtp_host: "smtp.example.com"  # fill in on the Jetson
  smtp_port: 587
  smtp_user: ""
  smtp_pass: ""                  # env PLAYGROUND_SMTP_PASS preferred
```

## Safety

- The sandbox kills runaway scripts (timeout) and confines file writes to the playground.
- The loop never runs while she's talking to Oppa or while heavy jobs run.
- Email goes to exactly one address (Oppa's). The notifier refuses to send anywhere else.
- If the loop ever misbehaves, deleting `loop/enabled` (a sentinel file) pauses it instantly — the tick checks for it first.
