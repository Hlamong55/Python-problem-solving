"""
Problem: Plus One

Given an integer represented as an array of digits,
increment the integer by one.

Example:

Input:
[1,2,3]

Output:
[1,2,4]
"""


def plus_one(digits):

    for i in range(len(digits) - 1, -1, -1):

        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    return [1] + digits


# Test Cases
print(plus_one([1,2,3]))
print(plus_one([4,3,2,1]))
print(plus_one([9]))
print(plus_one([9,9,9]))