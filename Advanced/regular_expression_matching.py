"""
Problem: Regular Expression Matching

Given an input string s and a pattern p,
implement regular expression matching with support for:

'.'  Matches any single character.
'*'  Matches zero or more of the preceding element.

The matching should cover the entire input string.

Example:

Input:
s = "aab"
p = "c*a*b"

Output:
True
"""


def is_match(s, p):

    m = len(s)
    n = len(p)

    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for j in range(2, n + 1):

        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if p[j - 1] == "." or p[j - 1] == s[i - 1]:

                dp[i][j] = dp[i - 1][j - 1]

            elif p[j - 1] == "*":

                dp[i][j] = dp[i][j - 2]

                if p[j - 2] == "." or p[j - 2] == s[i - 1]:

                    dp[i][j] = dp[i][j] or dp[i - 1][j]

    return dp[m][n]


# Test Cases

print(is_match("aa", "a"))
print(is_match("aa", "a*"))
print(is_match("ab", ".*"))
print(is_match("aab", "c*a*b"))