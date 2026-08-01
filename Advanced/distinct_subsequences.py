"""
Problem: Distinct Subsequences

Given two strings s and t,
return the number of distinct subsequences of s
which equals t.

Example:

Input:
s = "rabbbit"
t = "rabbit"

Output:
3

Explanation:

There are 3 different ways to delete one 'b'
from "rabbbit" to get "rabbit".
"""


def num_distinct(s, t):

    m = len(s)
    n = len(t)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Empty target can always be formed
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if s[i - 1] == t[j - 1]:

                dp[i][j] = (
                    dp[i - 1][j - 1]
                    + dp[i - 1][j]
                )

            else:

                dp[i][j] = dp[i - 1][j]

    return dp[m][n]


# Test Cases

print(num_distinct("rabbbit", "rabbit"))

print(num_distinct("babgbag", "bag"))

print(num_distinct("abc", "abc"))

print(num_distinct("abc", "abcd"))