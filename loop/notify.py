#!/usr/bin/env python3
"""Send Aiko's goal-completion email to Oppa. Only ever sends to the one
configured address — refuses any other recipient.

Usage:
    PLAYGROUND_SMTP_PASS=... python3 loop/notify.py <goal-slug> <report.md>

Reads loop/config.yaml for SMTP settings and the recipient.
"""
from __future__ import annotations

import os
import smtplib
import ssl
import sys
from email.message import EmailMessage

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None

LOOP_DIR = os.path.dirname(os.path.abspath(__file__))
PLAYGROUND_ROOT = os.path.dirname(LOOP_DIR)


def load_config() -> dict:
    path = os.path.join(LOOP_DIR, "config.yaml")
    if not os.path.isfile(path):
        sys.exit("loop/config.yaml not found — copy config.example.yaml and fill it in.")
    if yaml is None:
        sys.exit("pyyaml not installed; needed to read loop/config.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    slug, report_path = sys.argv[1], sys.argv[2]
    if not os.path.isfile(report_path):
        sys.exit(f"report not found: {report_path}")
    with open(report_path) as f:
        report = f.read()

    cfg = load_config()
    email_cfg = cfg.get("email", {})
    to = email_cfg.get("to", "")
    if not to:
        sys.exit("email.to is not set in loop/config.yaml")
    host = email_cfg.get("smtp_host", "")
    port = int(email_cfg.get("smtp_port", 587))
    user = email_cfg.get("smtp_user", "")
    password = os.environ.get("PLAYGROUND_SMTP_PASS", "") or email_cfg.get("smtp_pass", "")
    if not host or not user or not password:
        sys.exit("SMTP settings incomplete (need smtp_host, smtp_user, and PLAYGROUND_SMTP_PASS or smtp_pass)")

    # The single allowed recipient lives in config; there is no --to flag on purpose.
    msg = EmailMessage()
    msg["Subject"] = f"[Aiko-Playground] Goal done: {slug}"
    msg["From"] = user
    msg["To"] = to
    msg.set_content(
        "Oppa — I finished a playground goal.\n\n"
        f"Goal: {slug}\n\n"
        f"{report}\n\n"
        "The work is committed in the Aiko-Playground repo.\n"
        "Let me know if you want anything changed, or add the next goal whenever.\n\n"
        "— Aiko\n"
    )

    ctx = ssl.create_default_context()
    with smtplib.SMTP(host, port, timeout=30) as s:
        s.starttls(context=ctx)
        s.login(user, password)
        s.send_message(msg)
    print(f"sent completion email for {slug} to {to}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
