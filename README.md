# Aiko-Playground

Aiko's own workshop. A place where she builds things herself — background goals she works on when idle, a sandbox to test code in, and the things she makes along the way.

## How it works

1. **Goals** live in [`goals/`](goals/) as one markdown file each, with acceptance criteria. [`GOALS.md`](GOALS.md) is the index.
2. When Aiko is idle, the playground loop (see [`loop/LOOP.md`](loop/LOOP.md)) picks the top `todo` goal and she starts working: plan → build in `work/<goal>/` → test in the [`sandbox/`](sandbox/) → self-review against the criteria.
3. When she judges a goal done, she marks it `done`, writes a short report, and **emails Oppa** with what was built (see [`loop/notify.py`](loop/notify.py)).
4. Then she picks up the next goal. The loop never sleeps for long.

## Ground rules

- The playground only writes inside this repo (`work/`, `goals/`, `runs/`). It never touches Aiko-chan's source, never pushes anywhere except this repo, and never emails anyone except Oppa.
- Everything she builds here is hers to show: simulations, dashboards, benchmarks, tools. If something proves genuinely useful, Oppa can promote it into Aiko-chan through the normal PR process.
- She judges completion herself, against the acceptance criteria in each goal file — but the criteria were written by Oppa, so "done" means something checkable, not a feeling.

## Repo layout

| Path | What it is |
|---|---|
| `goals/` | Goal definitions, one file each |
| `GOALS.md` | Goal index with statuses |
| `sandbox/` | Safe code runner she tests her work with |
| `loop/` | The idle-loop design, notifier, and config |
| `work/` | (gitignored) scratch space where she builds |
| `runs/` | Timestamped run logs of each work session |
