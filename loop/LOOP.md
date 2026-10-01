# The Playground Loop

How Aiko works the goals by herself, in the background, during idle time.

## The idea in one paragraph

When Aiko has nothing else to do, she picks the top unfinished goal, builds it in `work/`, tests it in the sandbox, checks her work against the goal's acceptance criteria, and — only when every box is honestly checked — marks the goal done and emails Oppa a short report with what was built and where it lives. Then she moves to the next goal. She loops like this indefinitely. She never declares a goal done because she's tired of it; "done" means the criteria check out, with the test logs to prove it.

## When does the loop run?

On the Jetson, inside Aiko-chan's scheduler, as one ordinary `interval` /
`agentic` schedule record ("Aiko-Playground idle build") seeded by
`system/playground.py`. It fires every 15 minutes but only turns into real
work when the human has been genuinely idle for at least 10 minutes (the
record is `requires_idle`; a skipped tick just advances to the next one).
It is visible in Calendar Studio like any other scheduled task — pausing
(disabling) it there pauses the loop.

Each fire runs through Aiko's normal agent loop with the worker instructions
attached. Each work session is time-boxed (default 45 minutes). When the box
ends — or the human becomes active mid-session — she checkpoints and stops
cleanly; the next tick resumes.

## One work session

```
tick (idle confirmed)
  → read GOALS.md, pick top `todo` goal → mark `in_progress`
  → read the goal file fully
  → plan (short plan in work/<slug>/PLAN.md)
  → append a new session section to work/<slug>/LOG.md (start timestamp)
  → build → sandbox/run.py → read output → fix → repeat
     (log every file written + why, every sandbox run + errors, in LOG.md)
  → self-review: walk the acceptance criteria one by one,
    each with the evidence (test log, PNG path, measured number)
   → if all pass:
       - write work/<slug>/REPORT.md
       - mark goal `done` in GOALS.md + goal file
       - git commit + push to Aiko-Playground
       - email Oppa (your own send_email tool to AIKO_EMAIL;
         loop/notify.py over SMTP is fallback-only): what was built,
         key result, links
    else:
      - write work/<slug>/NOTES.md with what's blocking
      - leave goal `in_progress` (or back to `todo` if blocked on Oppa)
  → finish the LOG.md session section (end timestamp + reason + next steps)
  → append session summary to runs/<timestamp>-<slug>.md
```

## The full coding log

Oppa reads `work/<slug>/LOG.md` to see exactly how the code came to be. It is
committed (see `.gitignore`) and append-only: one dated section per session,
in the format of `loop/SESSION_LOG_TEMPLATE.md`. Every section records:

- **Start/end timestamps** (with timezone) and the exact reason the session
  ended (`goal done` / `time box reached` / `user active` / `kill switch` /
  `blocked`).
- **Interruptions and continuations.** If a session ends early because the
  human became active, it logs the interruption time; the next session logs
  its own start time and what it resumes. The chain must be unbroken.
- **How the code was generated** — every file written or changed and *why*
  (the reasoning, not just the diff).
- **Every sandbox execution** — the exact command, exit code, key output,
  and every error, plus what was changed to fix each one.
- **Research** — web searches used when she didn't know how, hit an
  unfamiliar error, or needed background to plan; what each search changed.
- **Self-verification** — the acceptance-criteria walk with evidence,
  including the criteria that honestly don't pass yet.

She verifies her own work: nothing is called "working" unless she ran it
through `sandbox/run.py` herself and read the output. Errors are diagnosed
and fixed by her, in the log.

## Rules she follows

1. **Playground only.** She writes inside this repo. She never edits Aiko-chan's source, config, or logs from the loop — she only *reads* them (goals 02, 03, 06 need read access to learn).
2. **Recommend, don't apply.** Anything that would change Aiko-chan (a faster TTS engine, a log fix) goes into the report as a recommendation. Oppa decides.
3. **Honest done.** If a criterion can't be met (missing package, hardware limit), she says so in the report and marks the goal `done-with-caveats` — never silently.
4. **One email per goal.** Not per session, not per attempt. Oppa hears from her when something is finished. Primary path is her own send_email tool (ProtonMail) to AIKO_EMAIL; `loop/notify.py` (SMTP, `PLAYGROUND_SMTP_PASS`) is fallback-only.
5. **She may propose new goals** in her emails, but she never adds them to `goals/` herself. Oppa adds them.
6. **No secrets in the repo.** Logs she reads may contain paths or machine details — reports summarize, they don't paste raw logs. The notifier config (SMTP password) lives outside the repo, never committed.

## State files

- `GOALS.md` — the index; statuses edited by the loop.
- `goals/NN-*.md` — goal definitions; `**Status:**` line edited by the loop.
- `work/<slug>/` — build area (gitignored except `REPORT.md` and `LOG.md`,
  which are committed so Oppa can read the results and the full coding log).
- `work/<slug>/LOG.md` — the full coding log: one session section per tick,
  appended every session (format: `loop/SESSION_LOG_TEMPLATE.md`).
- `work/<slug>/CHECKPOINT.md` — resume state (gitignored; the next tick
  starts here).
- `runs/` — append-only per-session summary cards, committed.

## Configuration

`loop/config.yaml` (not committed; see `config.example.yaml`). Only needed
for the SMTP fallback — the primary send_email path reads the recipient
from AIKO_EMAIL in Aiko-chan's encrypted `.env.age`:

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
- If the loop ever misbehaves, creating a `loop/disabled` file pauses it instantly — the session checks for it first and stands down.
