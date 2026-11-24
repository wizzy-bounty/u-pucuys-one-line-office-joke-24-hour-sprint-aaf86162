#!/usr/bin/env python3
"""One-line office joke entry.

Emits a single joke line to /output/entry.txt.
"""

import os
import sys


OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

JOKE = (
    "A new hire asked why the shared file is called "
    "FINAL_v7_REAL_USE_THIS_ONE, and the whole floor "
    "observed a minute of silence."
)


def ensure_output_dir(path):
    os.makedirs(path, exist_ok=True)


def write_entry(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")


def main():
    ensure_output_dir(OUTPUT_DIR)
    write_entry(OUTPUT_FILE, JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
