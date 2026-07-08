"""
Problem: Longest Increasing Subsequence

Given an integer array nums,
return the length of the longest
strictly increasing subsequence.

Example:

nums = [10,9,2,5,3,7,101,18]

Output:
4

Explanation:
The LIS is [2,3,7,101]
"""

def length_of_lis(nums):
    dp = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)


# Test Cases
print(length_of_lis([10,9,2,5,3,7,101,18]))  # 4
print(length_of_lis([0,1,0,3,2,3]))          # 4
print(length_of_lis([7,7,7,7]))              # 1