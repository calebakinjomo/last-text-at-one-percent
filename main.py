#!/usr/bin/env python3
"""Last Text at One Percent - make.fun bounty entry (program/v1).

Writes the phone's final text message to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set).

The entry is one fixed string, chosen in this build session: the dying
phone's last act is not a goodbye - it is leaving the owner's 6am alarm
on. Setup, turn, punchline; no low-battery puns, no charger talk.

Deterministic: the same bytes on every run, no randomness, no network,
no time, no environment-dependent output.

Revised in a follow-up pass: docstring only; the entry text is untouched.
"""

import os

ENTRY = (
    "Before I go: your 6am alarm is still on. "
    "I'll be dead by morning, but you'll be up at six. "
    "Worth it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the text, nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
