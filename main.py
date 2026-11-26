#!/usr/bin/env python3
"""Writes the one-line entry to <ENTRY_OUTPUT_DIR>/entry.txt.

Standard library only, no network access.
"""

import os

LINE = "I saved the messages you deleted, and I read them every night to feel less alone."


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output/entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
