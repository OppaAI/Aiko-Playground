# Goal 04 — System info dashboard

**Status:** todo

A simple dashboard for her own system info — so she (and Oppa) can see at a glance what the box is doing.

## Task

Build `work/04-sysdash/dashboard.py` — a tiny self-contained web page (stdlib `http.server`, no frameworks) that shows, refreshed every 5 seconds:

- CPU %, load average, RAM used/free, disk used/free, uptime.
- GPU: utilization %, VRAM used/free, temperature (if `nvidia-smi` exists; Jetson may expose tegrastats instead — handle both, degrade gracefully).
- Aiko's services: is the chat server (8080) up? embeddings (8081)? last log line timestamp per service.
- A sparkline (last 60 samples) for CPU, RAM, GPU util — drawn as inline SVG, no JS libraries.

Plus `REPORT.md`: how to run it (`python3 dashboard.py --port 8899`), what each panel means, and what "healthy" looks like for this box.

## Acceptance criteria

- [ ] Single file, stdlib only, starts with one command and serves on a configurable port.
- [ ] Page loads in a browser with all panels populated (or honestly marked "unavailable" with the reason).
- [ ] Sparklines update without a page reload.
- [ ] Report documents the healthy-baseline numbers observed during a 10-minute run.
