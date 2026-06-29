"""
Problem: Search in Rotated Sorted Array

Given a rotated sorted array nums
and an integer target,
return the index of target.

If target does not exist,
return -1.

Example 1:

nums = [4,5,6,7,0,1,2]
target = 0

Output:
4
"""

def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Test Cases
print(search([4,5,6,7,0,1,2], 0))   # 4
print(search([4,5,6,7,0,1,2], 3))   # -1
print(search([1], 0))               # -1
print(search([1,3], 3))             # 1