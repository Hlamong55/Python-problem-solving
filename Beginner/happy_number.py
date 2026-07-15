"""
Problem: Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is defined by repeatedly replacing
the number by the sum of the squares of its digits
until it equals 1.

If it loops forever, it is not a happy number.

Example:

Input:
19

Output:
True
"""


def is_happy(n):

    seen = set()

    while n != 1 and n not in seen:

        seen.add(n)

        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return n == 1


# Test Cases
print(is_happy(19))
print(is_happy(2))