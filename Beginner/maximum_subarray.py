"""
Problem: Maximum Subarray

Given an integer array nums,
find the contiguous subarray with the largest sum,
and return its sum.

Example 1:
nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:
6
"""

def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Test Cases
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(max_subarray([1]))                       # 1
print(max_subarray([5,4,-1,7,8]))             # 23
print(max_subarray([-1,-2,-3,-4]))            # -1