"""One-Liner Laughs — make.fun bounty u-coral-404-one-liner-laughs-aa872d41.

Writes exactly one joke: a single funny line of at most 200 characters,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic by design: the line is a fixed string, no clock, no random
numbers, no network, no model call, standard library only. The grader runs
this as `python3 -P -s /bot/main.py` with no network and a read-only
repository, so everything the entry needs lives in this one file.
"""

import os
import sys

JOKE = (
    "I bought noise-cancelling headphones to finally hear myself think; "
    "turns out I have nothing to say."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Refuse anything that is not one single line of at most 200 chars."""
    if not line:
        raise ValueError("joke must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "joke is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )


def main() -> int:
    validate(JOKE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
