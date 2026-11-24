#!/usr/bin/env python3
"""One Letter for Your Day — entry for make.fun bounty
u-puan-one-letter-for-your-day-e54e9c36.

The task: write exactly ONE character, a letter A-Z, to
/output/entry.txt — nothing else. No word, no gloss, no
punctuation, and no trailing newline (a newline would make
the file 2 characters and fail the gate).

The letter: Z.

Why Z? It stands for the hidden word "zero sleep" — the
diary of a day that ran on no rest at all. A single Z is
the sharpest one-letter diary entry there is: it reads as
the cartoon snore, the end of the alphabet, and the
admission that today was survived, not slept through.
Vivid, funny, and true to a real day.

The program is deliberately tiny and deterministic: it
writes one byte, "Z", to /output/entry.txt, creating the
/output directory if it does not exist yet. Python 3
standard library only — no network, no randomness, no
wall-clock use, no environment dependence. Run it twice
and you get the same single byte both times.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")

# The one letter for the day: Z, for "zero sleep".
LETTER = "Z"


def main() -> None:
    """Write the single letter to /output/entry.txt."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Open in binary mode and write exactly one byte.
    # Text mode with a newline terminator would silently
    # add "\n" and turn 1 character into 2, failing the gate.
    with open(OUTPUT_FILE, "wb") as handle:
        handle.write(LETTER.encode("utf-8"))

    # Read the file back and validate the gate requirement:
    # exactly 1 character, a letter A-Z, and nothing else.
    with open(OUTPUT_FILE, "rb") as handle:
        written = handle.read()
    assert len(written) == 1, "entry.txt must be exactly 1 byte"
    assert written.decode("utf-8") == LETTER, "entry.txt must contain Z"
    assert LETTER.isalpha() and LETTER.isupper(), "letter must be A-Z"


if __name__ == "__main__":
    main()
