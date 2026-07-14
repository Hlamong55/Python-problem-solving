"""
Problem: Remove Duplicates from Sorted Array

Given a sorted integer array nums,
remove the duplicates in-place.

Return the number of unique elements.

Example:

Input:
[1,1,2]

Output:
2

Array becomes:
[1,2,_]
"""


def remove_duplicates(nums):

    if not nums:
        return 0

    left = 1

    for right in range(1, len(nums)):

        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1

    return left


# Test Cases
nums = [1,1,2]
k = remove_duplicates(nums)

print(k)
print(nums[:k])

nums = [0,0,1,1,1,2,2,3,3,4]
k = remove_duplicates(nums)

print(k)
print(nums[:k])