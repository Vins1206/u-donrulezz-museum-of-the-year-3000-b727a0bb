#!/usr/bin/env python3
"""Museum of the Year 3000 - entry program (Python stdlib only).

Writes a single museum label, one line of plain text, to
/output/entry.txt. The label is the one a museum in the year 3000
places next to an ordinary object from today: the group chat.

The humour is the misreading: future curators take the chat at face
value, a crowd that met every day inside a glowing rectangle, talked
over each other, read nothing, and still called it friendship.
"""

import os

# One fixed label, 133 characters. No randomness, no I/O besides the
# single output file, so every run produces byte-identical output.
ENTRY = (
    "Group chat, c. 2025. Forty-seven humans gathered daily in a "
    "glowing rectangle to speak at once, read nothing, and call it "
    "friendship."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
