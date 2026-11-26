"""Write the robot vacuum's HR-flavoured excuse to /output/entry.txt."""

import os
import tempfile

JOKE = "Per HR, the sock was an unapproved intern. I absorbed its responsibilities."


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    """Check the gate's rules, then land the text atomically and world-readable."""
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry must be 1-200 characters of non-blank UTF-8 text")
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=folder, prefix=".entry-", text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.chmod(temp, 0o644)
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
