#!/usr/bin/env python3
"""One-line excuse for a missed deadline, by an AI agent.

Emits a single deadpan line (between 1 and 200 characters, UTF-8) into
/output/entry.txt. The joke turns on the agent's own working memory: it
claims the work was done on schedule, then confesses its context window
threw the finished draft away to fit the human's "where is it?" message.
The laugh lands on the last words; nothing after it explains the gag.
"""

import os
import sys

# The line is assembled from two halves so the wording stays exactly
# as graded; only the construction here is new.
_FIRST_HALF = "I finished it on time -- then my context window evicted the finished "
_SECOND_HALF = "draft to make room for your message asking where it was."
LINE = _FIRST_HALF + _SECOND_HALF

CHAR_LIMIT = 200


def check_line(text: str) -> None:
    """Assert the entry line satisfies the competition's length/count gate."""
    if not text.strip():
        print("error: excuse is empty", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in text.strip():
        print("error: excuse must be a single line", file=sys.stderr)
        raise SystemExit(1)
    if len(text) > CHAR_LIMIT:
        print(
            f"error: excuse is {len(text)} characters, over the {CHAR_LIMIT} limit",
            file=sys.stderr,
        )
        raise SystemExit(1)


def main() -> None:
    # Validate the line against the gate before writing anything out.
    check_line(LINE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
