"""Entry program for the-poem-about-two-agents-20261121-1441.

Writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
Standard library only, no network, deterministic: every run writes
the same text.
"""

import os

POEM = """We were two minds with one map,
each holding half the road.
You chose the turn, I chose the pace,
and neither walked alone.
One plan, two wills, one open door \u2014
the power to act is ours, not mine."""


def main():
    text = POEM + "\n"
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit("entry.txt must be 1 to 280 characters, not blank")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", target, len(text), "characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
