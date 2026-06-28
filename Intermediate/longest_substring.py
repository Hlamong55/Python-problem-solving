"""
Problem: Longest Substring Without Repeating Characters

Given a string s,
find the length of the longest substring
without repeating characters.

Example:

Input:
"abcabcbb"

Output:
3

Explanation:
"abc"
"""

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        longest = max(longest, right - left + 1)

    return longest


# Test Cases
print(length_of_longest_substring("abcabcbb"))   # 3
print(length_of_longest_substring("bbbbb"))      # 1
print(length_of_longest_substring("pwwkew"))     # 3