"""Weirdest Job Title entry.

Prints a single job title, one line, 60 characters or fewer, and nothing
else. The title is also written to output.txt inside the directory named
by MAKEFUN_OUTPUT_DIR when that variable is set, so the grader can read
it from stdout or from the output directory either way.
"""

import os

TITLE = "Senior Vice President of Apologizing to Vending Machines"


def main() -> None:
    title = TITLE.strip()
    assert title, "title must not be blank"
    assert "\n" not in title, "title must be a single line"
    assert len(title) <= 60, "title must be 60 characters or fewer"
    print(title)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "output.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(title + "\n")


if __name__ == "__main__":
    main()
