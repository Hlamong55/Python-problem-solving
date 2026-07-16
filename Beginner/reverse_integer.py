"""
Problem: Reverse Integer

Given a signed 32-bit integer x,
return x with its digits reversed.

If reversing causes overflow,
return 0.

Example:

123 -> 321
-123 -> -321
120 -> 21
"""


def reverse_integer(x):

    sign = -1 if x < 0 else 1
    x = abs(x)

    reverse = 0

    while x > 0:
        digit = x % 10
        reverse = reverse * 10 + digit
        x //= 10

    reverse *= sign

    if reverse < -(2 ** 31) or reverse > (2 ** 31 - 1):
        return 0

    return reverse


# Test Cases
print(reverse_integer(123))
print(reverse_integer(-123))
print(reverse_integer(120))