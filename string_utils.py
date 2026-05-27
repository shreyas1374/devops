"""
string_utils.py
A collection of handy string utility functions.
"""


def reverse_string(s: str) -> str:
    """Return the reversed version of the given string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Return True if the string is a palindrome (case-insensitive)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    """Return the number of vowels in the given string."""
    return sum(1 for ch in s.lower() if ch in "aeiou")


def capitalize_words(s: str) -> str:
    """Capitalize the first letter of every word in the string."""
    return " ".join(word.capitalize() for word in s.split())


def truncate(s: str, max_length: int, suffix: str = "...") -> str:
    """Truncate string to max_length characters, appending suffix if truncated."""
    if len(s) <= max_length:
        return s
    return s[: max_length - len(suffix)] + suffix


if __name__ == "__main__":
    print(reverse_string("hello"))          # olleh
    print(is_palindrome("Racecar"))         # True
    print(count_vowels("Hello World"))      # 3
    print(capitalize_words("hello world"))  # Hello World
    print(truncate("This is a long text", 10))  # This is...
