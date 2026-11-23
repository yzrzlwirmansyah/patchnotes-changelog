"""Real-Life Patch Notes: The Comedy Changelog -- make.fun entry.

Writes a single-line patch note to /output/entry.txt.
Python 3.13, standard library only, deterministic.
"""

import os

LINE = "v5.0.2: fixed a bug where the body set a 3 a.m. alarm for every embarrassing thing you did in 2009."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
