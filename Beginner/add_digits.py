"""
Problem: Add Digits

Given an integer num,
repeatedly add all its digits until
the result has only one digit.

Example:

Input: 38
Output: 2

Explanation:
3 + 8 = 11
1 + 1 = 2
"""


def add_digits(num):

    while num >= 10:

        total = 0

        while num > 0:
            total += num % 10
            num //= 10

        num = total

    return num


# Test Cases
print(add_digits(38))
print(add_digits(0))
print(add_digits(999))