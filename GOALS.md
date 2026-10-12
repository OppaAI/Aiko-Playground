# Goals — small, user-shaped, three at a time

Aiko works these top-down when idle. Status is one of `todo`, `in_progress`, `done`.

**The three-active rule:** at most 3 goals are active (`todo`/`in_progress`)
at any time. Small goals only — one goal must fit in a few sessions, help
Oppa directly, and be verifiable. When an active goal completes, the refill
rule below tops the table back up to 3.

**Refill rule (Aiko picks, Oppa approves by silence):** when fewer than 3
goals are active, Aiko proposes replacements from her memory of Oppa —
his preferences, what he lacks, what features would help him — and appends
them with status `todo` (plus a fresh `goals/<slug>.md` file each). Small
user-facing features only: no infra rewrites, no benchmarks-for-benchmarks.
Oppa can strike or replace any proposal by editing this file.

| # | Goal | Status |
|---|---|---|
| 01 | [Morning voice briefing](goals/01-morning-briefing.md) | todo |
| 02 | [Overnight mentions digest](goals/02-overnight-digest.md) | todo |
| 03 | ["What did I miss?" catch-up](goals/03-what-did-i-miss.md) | todo |

## How a goal gets done (per-goal lifecycle)

1. **Research** — her own knowledge first, then web search for what she
   doesn't know. Log queries + takeaways.
2. **Plan** — `work/<slug>/PLAN.md`: spec, design, implementation steps,
   testing steps, and verification steps (how she proves the goal is met).
   No code before the plan exists.
3. **Implement** — code in `work/<slug>/`, sandbox runs only.
4. **Test + debug** — run, read output, fix, re-run. Keep the debug
   history (what broke, what fixed it) — it goes in the report.
5. **Verify** — walk the acceptance criteria one by one with evidence.
6. **Mark complete** — status `done` here + in the goal file, REPORT.md
   with what was built, test evidence, debug history, and how to run it.
7. **Email Oppa** — one completion email (per WORKER.md rule 8), then the
   next goal. Never start a second goal in the same session.

## Parked backlog (too large as written — split before activating)

Earlier system-oriented goals, kept for parts. Any of these may return
split into small user-facing pieces, proposed through the refill rule —
never reactivated whole.

| # | Goal | Status |
|---|---|---|
| — | [Neuron signal simulation](/home/oppa-ai/jetson/Aiko-chan/archive/playground/parked-01-neuron-signal-simulation.md) | parked |
| — | [Prompt-to-response pipeline visualization](/home/oppa-ai/jetson/Aiko-chan/archive/playground/parked-02-prompt-pipeline-visualization.md) | parked |
| — | [ASR/TTS latency benchmark](/home/oppa-ai/jetson/Aiko-chan/archive/playground/parked-03-asr-tts-latency-benchmark.md) | parked |
| — | [System info dashboard](/home/oppa-ai/jetson/Aiko-chan/archive/playground/parked-04-system-info-dashboard.md) | parked |
| — | [Heartbeat / internet availability monitor](/home/oppa-ai/jetson/Aiko-chan/archive/playground/parked-05-heartbeat-monitor.md) | parked |
| — | [Error-log root-cause analysis](/home/oppa-ai/jetson/Aiko-chan/archive/playground/parked-06-error-log-root-cause.md) | parked |

## Done

| Goal | Completed | Report |
|---|---|---|
| *(none yet)* | | |
