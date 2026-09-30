#!/usr/bin/env python3
"""Aiko-Playground sandbox runner.

Usage:
    python3 sandbox/run.py <script.py> [--timeout SECS] [--cwd DIR] [-- <script args...>]

Runs <script.py> with a wall-clock timeout, captures stdout/stderr/returncode,
and prints a JSON summary. Refuses to run anything outside the playground root.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

PLAYGROUND_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_TIMEOUT = 120


def inside_root(path: str) -> bool:
    real = os.path.realpath(path)
    return real == PLAYGROUND_ROOT or real.startswith(PLAYGROUND_ROOT + os.sep)


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        return 2

    script = os.path.abspath(args[0])
    rest = args[1:]
    timeout = DEFAULT_TIMEOUT
    cwd = os.path.dirname(script) or PLAYGROUND_ROOT
    script_args: list[str] = []

    i = 0
    while i < len(rest):
        if rest[i] == "--timeout" and i + 1 < len(rest):
            timeout = int(rest[i + 1]); i += 2
        elif rest[i] == "--cwd" and i + 1 < len(rest):
            cwd = os.path.abspath(rest[i + 1]); i += 2
        elif rest[i] == "--":
            script_args = rest[i + 1:]; break
        else:
            script_args = rest[i:]; break

    if not inside_root(script):
        print(json.dumps({"ok": False, "error": "script is outside the playground root"}))
        return 1
    if not inside_root(cwd):
        print(json.dumps({"ok": False, "error": "cwd is outside the playground root"}))
        return 1
    if not os.path.isfile(script):
        print(json.dumps({"ok": False, "error": "script not found"}))
        return 1

    env = dict(os.environ)
    env["PYTHONSAFEPATH"] = "1"
    env["PYTHONDONTWRITEBYTECODE"] = "1"

    start = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, script, *script_args],
            cwd=cwd, env=env, capture_output=True, text=True,
            timeout=timeout,
        )
        elapsed = time.time() - start
        summary = {
            "ok": proc.returncode == 0,
            "returncode": proc.returncode,
            "elapsed_s": round(elapsed, 2),
            "timeout_s": timeout,
            "timed_out": False,
            "stdout": proc.stdout[-8000:],
            "stderr": proc.stderr[-8000:],
        }
    except subprocess.TimeoutExpired as e:
        elapsed = time.time() - start
        summary = {
            "ok": False, "returncode": None,
            "elapsed_s": round(elapsed, 2),
            "timeout_s": timeout, "timed_out": True,
            "stdout": (e.stdout or b"").decode(errors="replace")[-8000:] if isinstance(e.stdout, bytes) else (e.stdout or "")[-8000:],
            "stderr": (e.stderr or b"").decode(errors="replace")[-8000:] if isinstance(e.stderr, bytes) else (e.stderr or "")[-8000:],
        }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
