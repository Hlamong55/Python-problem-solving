"""
Problem:

Given two strings s and t,

return the minimum window substring of s
such that every character in t is included.

Example:

Input:

s = "ADOBECODEBANC"

t = "ABC"

Output:

"BANC"
"""


from collections import Counter


def min_window(s, t):

    if not s or not t:
        return ""

    need = Counter(t)

    missing = len(t)

    left = 0

    start = end = 0

    for right in range(len(s)):

        if need[s[right]] > 0:
            missing -= 1

        need[s[right]] -= 1

        while missing == 0:

            if end == 0 or right - left + 1 < end - start:

                start = left
                end = right + 1

            need[s[left]] += 1

            if need[s[left]] > 0:
                missing += 1

            left += 1

    return s[start:end]


print(min_window("ADOBECODEBANC", "ABC"))

print(min_window("a", "a"))

print(min_window("a", "aa"))