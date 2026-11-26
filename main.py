#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes one museum placard line for an ordinary office object, treated
as an ancient artifact, to /output/entry.txt. Deterministic: the same
entry on every run.
"""
import os

ENTRY = (
    "Stapler, c. 2019. Steel and quiet resentment. Donated by Accounts, "
    "who used it to bind together everything the meetings could not."
)


def main():
    # Gate self-check: the entry must be 1-180 characters of real text.
    assert 1 <= len(ENTRY) <= 180, "entry outside the 1-180 character gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
