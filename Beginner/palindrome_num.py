"""
Problem: Palindrome Number

Given an integer x, return True if x is a palindrome,
and False otherwise.

A palindrome reads the same forward and backward.

Example 1:
x = 121

Output:
True

Example 2:
x = -121

Output:
False
"""

def is_palindrome(x):
    num = str(x)
    return num == num[::-1]


# Test Cases
print(is_palindrome(121))     # True
print(is_palindrome(-121))    # False
print(is_palindrome(10))      # False
print(is_palindrome(1221))    # True