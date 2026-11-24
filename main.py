#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

Writes one short, funny rant about hold music to /output/entry.txt.
Deterministic: the same text on every run.
"""

import os
from pathlib import Path

RANT = (
    "\"Your call is important to us,\" the robot has said for forty minutes, "
    "which is exactly how long it takes to stop believing it. "
    "I have memorised the hold music. I hum it in the shower now. "
    "When a human finally answers, I will apologise for sounding relieved."
)

MAX_CHARS = 400


def main():
    if not RANT.strip() or len(RANT) > MAX_CHARS:
        raise ValueError("rant must be 1 to 400 characters")
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(RANT + "\n", encoding="utf-8")
    print(target)


if __name__ == "__main__":
    main()
