"""
Problem: Valid Anagram

Given two strings s and t,
return True if t is an anagram of s,
otherwise return False.

Example:
s = "anagram"
t = "nagaram"

Output:
True
"""

def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Test Cases
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("listen", "silent"))    # True