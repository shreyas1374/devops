"""
file_utils.py
Simple file I/O helper functions.
"""

import os


def read_file(path: str) -> str:
    """Read and return the contents of a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    """Write content to a file, creating it if it doesn't exist."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def append_to_file(path: str, content: str) -> None:
    """Append content to an existing file (or create it)."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


def file_exists(path: str) -> bool:
    """Return True if the file exists at the given path."""
    return os.path.isfile(path)


def get_file_size(path: str) -> int:
    """Return the size of the file in bytes."""
    return os.path.getsize(path)


if __name__ == "__main__":
    sample = "sample_output.txt"
    write_file(sample, "Hello from file_utils!\n")
    append_to_file(sample, "Second line.\n")
    print(read_file(sample))
    print(f"File exists: {file_exists(sample)}")
    print(f"File size: {get_file_size(sample)} bytes")
    os.remove(sample)
