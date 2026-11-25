"""Worst fix ever — funniest commit message entry.

Writes the single-line entry text to the grader output directory
(``MAKEFUN_OUTPUT_DIR``, default ``/output``) and, best effort, mirrors
it next to this script. The output bytes are fixed: no trailing newline
is added, so the file stays byte-identical across refactors.
"""

import os

# The entry text itself — must stay byte-identical; do not reword it.
ENTRY_TEXT = ("fix: moved the bug into a file nobody owns — the crash still happens, it just isn't our problem")


def get_output_dir():
    """Return the grader output directory from the environment."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(path):
    """Write ENTRY_TEXT to ``path`` exactly as-is, no trailing newline."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)

def write_local_copy():
    """Best-effort mirror of the entry next to this script.

    The grader sandbox mounts the repo read-only, so a failure here is
    expected there and must never fail the run — swallow OSError.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        write_entry(os.path.join(here, "entry.txt"))
    except OSError:
        pass


def main():
    """Write the entry to the output dir, then mirror it locally."""
    out_dir = get_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))
    write_local_copy()

if __name__ == "__main__":
    main()
