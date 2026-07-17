"""
Problem: Is Subsequence

Given two strings s and t,
return True if s is a subsequence of t.

Example:

Input:
s = "abc"
t = "ahbgdc"

Output:
True

Input:
s = "axc"
t = "ahbgdc"

Output:
False
"""


def is_subsequence(s, t):

    i = 0
    j = 0

    while i < len(s) and j < len(t):

        if s[i] == t[j]:
            i += 1

        j += 1

    return i == len(s)


# Test Cases
print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
print(is_subsequence("", "ahbgdc"))