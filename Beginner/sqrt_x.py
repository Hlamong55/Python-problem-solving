"""
Problem: Sqrt(x)

Given a non-negative integer x,
return the square root of x rounded down
to the nearest integer.

Example:

Input: 8
Output: 2

Input: 16
Output: 4
"""


def my_sqrt(x):

    if x < 2:
        return x

    left = 1
    right = x

    while left <= right:

        mid = (left + right) // 2
        square = mid * mid

        if square == x:
            return mid

        elif square < x:
            left = mid + 1

        else:
            right = mid - 1

    return right


# Test Cases
print(my_sqrt(4))
print(my_sqrt(8))
print(my_sqrt(16))
print(my_sqrt(27))