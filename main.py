#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "The bug you seek is in the code you swore was fine; the fix is in the log you swore you checked."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
