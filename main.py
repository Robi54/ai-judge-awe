#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Deterministic: the same text is written on every run. Standard library
only, no network, no randomness, no clock.
"""

import os

TEXT = (
    "The tide slips out over flat sand and leaves the sky behind in "
    "shallow pools. The stars stand in them, doubled, and do not mind "
    "being small. The moon has done this a thousand times. It will do "
    "it a thousand more, whether anyone watches or not."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
