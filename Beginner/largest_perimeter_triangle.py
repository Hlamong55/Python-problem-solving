"""
Problem: Largest Perimeter Triangle

Given an integer array nums,
return the largest perimeter of a triangle
with non-zero area formed from three lengths.

If no triangle can be formed, return 0.

Example:

Input: [2,1,2]

Output: 5
"""


def largest_perimeter(nums):

    nums.sort(reverse=True)

    for i in range(len(nums) - 2):

        if nums[i] < nums[i + 1] + nums[i + 2]:
            return nums[i] + nums[i + 1] + nums[i + 2]

    return 0


# Test Cases

print(largest_perimeter([2, 1, 2]))
print(largest_perimeter([1, 2, 1]))
print(largest_perimeter([3, 6, 2, 3]))