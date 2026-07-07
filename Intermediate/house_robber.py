"""
Problem: House Robber

You are a professional robber planning to rob houses.

Each house has a certain amount of money.

You cannot rob two adjacent houses.

Return the maximum amount of money
you can rob without alerting the police.

Example 1:

nums = [1,2,3,1]

Output:
4

Explanation:
Rob house 1 and house 3.

1 + 3 = 4
"""

def rob(nums):
    if len(nums) == 1:
        return nums[0]

    prev_two = 0
    prev_one = 0

    for money in nums:
        current = max(prev_one, prev_two + money)
        prev_two = prev_one
        prev_one = current

    return prev_one


# Test Cases
print(rob([1,2,3,1]))      # 4
print(rob([2,7,9,3,1]))    # 12
print(rob([2,1,1,2]))      # 4
print(rob([5]))            # 5