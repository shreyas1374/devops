"""
math_utils.py
Extended math utility functions beyond the standard library.
"""

import math


def factorial(n: int) -> int:
    """Return n! (factorial of n). n must be a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list:
    """Return a list of the first n Fibonacci numbers."""
    if n <= 0:
        return []
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def gcd(a: int, b: int) -> int:
    """Return the Greatest Common Divisor of a and b."""
    return math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Return the Least Common Multiple of a and b."""
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    print(f"5! = {factorial(5)}")                   # 120
    print(f"is_prime(17) = {is_prime(17)}")         # True
    print(f"fibonacci(8) = {fibonacci(8)}")         # [0, 1, 1, 2, 3, 5, 8, 13]
    print(f"gcd(48, 18) = {gcd(48, 18)}")           # 6
    print(f"lcm(4, 6) = {lcm(4, 6)}")               # 12
