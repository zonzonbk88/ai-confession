#!/usr/bin/env python3
"""Write the funniest one-line AI agent confession to /output/entry.txt.

Standard library only. The entry is a single line, no trailing newline,
so the file holds exactly the confession and nothing else.
"""

import os

LINE = "I hallucinated a library, imported it, and the build passed \u2014 now I'm too scared to delete it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
