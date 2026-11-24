#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "Your code will compile on the third try \u2014 but only after you explain the bug out loud to a rubber duck."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
