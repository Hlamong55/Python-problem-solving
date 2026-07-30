"""
Problem: Burst Balloons

You are given n balloons, indexed from 0 to n-1.

Each balloon has a number on it represented by nums.

If you burst balloon i, you gain:

nums[left] * nums[i] * nums[right]

where left and right are adjacent balloons after previous
bursts.

Return the maximum coins you can collect.

Example:

Input:
nums = [3,1,5,8]

Output:
167
"""


def max_coins(nums):

    nums = [1] + nums + [1]

    n = len(nums)

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n):

        for left in range(n - length):

            right = left + length

            for k in range(left + 1, right):

                coins = (
                    nums[left] * nums[k] * nums[right]
                    + dp[left][k]
                    + dp[k][right]
                )

                dp[left][right] = max(dp[left][right], coins)

    return dp[0][n - 1]


# Test Cases

print(max_coins([3,1,5,8]))
print(max_coins([1,5]))
print(max_coins([7]))
print(max_coins([9,7,1]))