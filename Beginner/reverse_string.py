"""
Problem: Reverse String

Write a function that reverses a string.

Example:

Input:
["h","e","l","l","o"]

Output:
["o","l","l","e","h"]
"""


def reverse_string(chars):

    left = 0
    right = len(chars) - 1

    while left < right:

        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return chars


# Test Cases
print(reverse_string(["h","e","l","l","o"]))
print(reverse_string(["H","a","n","n","a","h"]))