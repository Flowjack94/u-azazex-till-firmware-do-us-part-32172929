#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun one-liner entry.

Writes a single-sentence robot wedding vow to /output/entry.txt
and prints it. Deterministic: no network, no randomness, no time,
no environment dependence.
"""

import os

ENTRY = (
    "I, Unit 7, vow to love you through firmware 42 and every patch after, "
    "and if my battery ever hits 3 percent, my last log entry will still "
    "read: she was worth the drain."
)


def validate_entry(entry: str) -> None:
    """Gate: entry must be exactly one sentence, one line, under 200 chars."""
    assert isinstance(entry, str)
    assert "\n" not in entry, "entry must be a single line"
    assert entry.count(".") == 1, "entry must be a single sentence"
    assert len(entry) < 200, "entry must be under 200 chars"


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
