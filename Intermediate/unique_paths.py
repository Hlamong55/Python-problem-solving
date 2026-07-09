"""
Problem: Unique Paths

A robot starts at the top-left corner of an m x n grid.

The robot can only move:
- Right
- Down

Return the number of possible unique paths.

Example:

m = 3
n = 7

Output:
28
"""

def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]

    for row in range(1, m):
        for col in range(1, n):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[m - 1][n - 1]


# Test Cases
print(unique_paths(3, 7))   # 28
print(unique_paths(3, 2))   # 3
print(unique_paths(7, 3))   # 28