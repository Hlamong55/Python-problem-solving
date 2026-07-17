"""
Problem: Valid Perfect Square

Given a positive integer num,
return True if num is a perfect square.

Do not use the built-in sqrt() function.

Example:

Input:
16

Output:
True

Input:
14

Output:
False
"""


def is_perfect_square(num):

    left = 1
    right = num

    while left <= right:

        mid = (left + right) // 2
        square = mid * mid

        if square == num:
            return True

        if square < num:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test Cases
print(is_perfect_square(16))
print(is_perfect_square(14))
print(is_perfect_square(25))
print(is_perfect_square(26))