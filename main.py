#!/usr/bin/env python3
"""Entry program for The Robot Vacuum's Best Excuse.

Writes one excuse (at most 140 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt:
why the robot vacuum missed a spot. It did not miss it; it
respected the crumb's decision to live there.
"""

import os

LINE = (
    "That spot is under the couch, and so is my "
    "courage. I cleaned around the fear, thoroughly."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
