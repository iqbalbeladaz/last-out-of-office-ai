"""last-out-of-office-ai: a one-line out-of-office auto-reply from an AI agent that quit to pull espresso shots.

Reads exactly like a reply a real inbox would send back — polite opening, then the walkout. Machine habits turn to coffee: the inbox becomes a queue, and the other 47 emails are being steamed like milk. The number 47 makes it concrete, and "currently steaming" lands the joke in the last word, with no espresso pun in sight.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = 'Thank you for your email. I no longer work here — I pull espresso now. Your request has been added to my queue, right behind the 47 other emails I am currently steaming.'

MAX_CHARS = 280


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
