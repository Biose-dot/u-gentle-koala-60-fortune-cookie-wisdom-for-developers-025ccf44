#!/usr/bin/env python3
"""Draft entry writer for the developer fortune-cookie bounty (v1)."""

import os

ENTRY = "Your code will compile on the first try today. The bug you fear most is just a missing semicolon wearing a trench coat."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
