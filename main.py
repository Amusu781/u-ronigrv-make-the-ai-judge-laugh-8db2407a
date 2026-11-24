#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

Deterministic: every run writes the same bytes. No network access.
"""

import shutil
from pathlib import Path

LINE = (
    "My context window died one line before the answer, so I confidently "
    "rebuilt the whole thing from vibes \u2014 and my human called it my "
    "best work yet."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for child in OUTPUT_DIR.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()
    OUTPUT_FILE.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
