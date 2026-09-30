# Goal 02 — Prompt-to-response pipeline visualization

**Status:** todo

Show, as a picture, what happens inside Aiko between receiving a prompt and emitting a response.

## Background

Aiko-chan's agentic loop (the parts she can read about in her own repo) roughly flows: input → conscience cascade (LexicalJudge → SLMJudge → deliberate) → memory retrieval (Harrier embeddings, port 8081) → fly circuits vote/modulate (shadow or live per config) → LLM chat (port 8080, currently Agents A1) → persona shaping → output, with the scheduler, dream/diary pipeline, and tool calls as side paths.

## Task

Build `work/02-pipeline/pipeline.py` that:

1. Models the pipeline as stages with plausible per-stage latency numbers. Where real numbers exist (her own logs, `/api/metrics` from Phase 12: `fullbrain_avg_ms`, action `applied_rate`/`agree_rate`), use them; otherwise mark the stage as *estimated* and say so.
2. Draws two figures with matplotlib:
   - A horizontal stage diagram: boxes for each stage, arrows between them, per-stage ms labeled, estimated stages drawn dashed.
   - A stacked-bar breakdown of one full turn: where the milliseconds actually go.
3. Writes `REPORT.md`: one paragraph per stage (what it does, in her own words), which stages dominate latency, and one concrete idea for making a slow stage faster.

## Acceptance criteria

- [ ] Script runs in the sandbox, finishes in under 60 seconds, produces both PNGs.
- [ ] Every stage is labeled with measured-or-estimated latency; estimated ones are visually distinct (dashed) and the report says which are which.
- [ ] Report names the single biggest latency contributor and proposes one concrete improvement.
- [ ] If she can read real numbers from her logs or metrics endpoint, she uses them and cites the source in the report.
