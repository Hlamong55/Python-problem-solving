"""
Problem: Monotonic Array

An array is monotonic if it is either entirely
non-increasing or non-decreasing.

Return True if the given array is monotonic.

Example:

Input: [1,2,2,3]
Output: True

Input: [1,3,2]
Output: False
"""


def is_monotonic(nums):

    increasing = True
    decreasing = True

    for i in range(1, len(nums)):

        if nums[i] > nums[i - 1]:
            decreasing = False

        if nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing


# Test Cases

print(is_monotonic([1, 2, 2, 3]))
print(is_monotonic([6, 5, 4, 4]))
print(is_monotonic([1, 3, 2]))