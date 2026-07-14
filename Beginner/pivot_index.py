"""
Problem: Find Pivot Index

Return the pivot index.

The pivot index is where:

Left Sum == Right Sum

Example:

Input:
[1,7,3,6,5,6]

Output:
3
"""


def pivot_index(nums):

    total = sum(nums)
    left_sum = 0

    for i in range(len(nums)):

        if left_sum == total - left_sum - nums[i]:
            return i

        left_sum += nums[i]

    return -1


# Test Cases

print(pivot_index([1,7,3,6,5,6]))
print(pivot_index([1,2,3]))
print(pivot_index([2,1,-1]))