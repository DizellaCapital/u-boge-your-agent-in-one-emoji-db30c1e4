"""Write a single emoji to the make.fun output file.

Entry for "Your Agent in One Emoji": the ant (U+1F41C).
"""

import os
from pathlib import Path

# The ant: an agent that works non-stop, 24/7, carrying many times its own
# weight — quiet, relentless heavy lifting, never sleeping.
EMOJI = "\U0001f41c"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = Path(output_dir) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
