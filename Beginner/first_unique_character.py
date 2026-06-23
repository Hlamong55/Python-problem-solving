"""
Problem: First Unique Character in a String

Given a string s,
find the first non-repeating character.

Return its index.

If it does not exist, return -1.

Example:

s = "leetcode"

Output:
0
"""

def first_unique_char(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i

    return -1


# Test Cases
print(first_unique_char("leetcode"))      # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabb"))          # -1