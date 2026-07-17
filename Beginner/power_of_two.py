"""
Problem: Power of Two

Given an integer n,
return True if it is a power of two.

Example:

Input:
16

Output:
True

Input:
18

Output:
False
"""


def is_power_of_two(n):

    if n <= 0:
        return False

    return (n & (n - 1)) == 0


# Test Cases
print(is_power_of_two(1))
print(is_power_of_two(16))
print(is_power_of_two(18))
print(is_power_of_two(64))