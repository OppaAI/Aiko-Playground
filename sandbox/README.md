# Sandbox

A tiny, boring, predictable code runner. Aiko tests everything she builds here before calling it done.

## `run.py`

```sh
python3 sandbox/run.py <script.py> [--timeout 120] [--args ...]
```

- Runs the script with the playground's `work/<goal>/` as the working directory.
- Captures stdout, stderr, return code, and wall-clock time; prints a JSON summary.
- Kills the script if it exceeds `--timeout` (default 120s).
- Scripts may only write inside the playground directory — the runner refuses to execute anything whose resolved path is outside it, and sets `PYTHONSAFEPATH` so imports can't escape via cwd tricks.

This is not a security boundary against a hostile actor — it's a guardrail against her own mistakes: no infinite loops hanging the loop, no accidental writes outside the playground, everything logged.

## Rules for goal work

1. Nothing counts as "tested" unless it ran through `run.py` and the JSON summary is saved in the goal's work dir.
2. If a script needs a package that isn't installed, she notes it in the report — she does not `pip install` into the system. (A per-goal venv inside `work/` is allowed.)
3. Network access from sandbox scripts is allowed only for goals that say so (heartbeat). Everything else should run offline.
