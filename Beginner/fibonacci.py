"""
Problem: Fibonacci Number

The Fibonacci numbers are defined as:

F(0) = 0
F(1) = 1

F(n) = F(n-1) + F(n-2)

Return F(n).

Example:

Input:
4

Output:
3
"""


def fibonacci(n):

    if n <= 1:
        return n

    first = 0
    second = 1

    for _ in range(2, n + 1):

        first, second = second, first + second

    return second


# Test Cases
print(fibonacci(2))
print(fibonacci(4))
print(fibonacci(8))