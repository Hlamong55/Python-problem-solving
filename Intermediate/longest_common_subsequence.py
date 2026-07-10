"""
Problem: Longest Common Subsequence

Given two strings,
return the length of their longest common subsequence.

Example:

text1 = "abcde"
text2 = "ace"

Output:
3
"""

def longest_common_subsequence(text1, text2):
    rows = len(text1) + 1
    cols = len(text2) + 1

    dp = [[0] * cols for _ in range(rows)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):

            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


# Test Cases
print(longest_common_subsequence("abcde", "ace"))   # 3
print(longest_common_subsequence("abc", "abc"))     # 3
print(longest_common_subsequence("abc", "def"))     # 0