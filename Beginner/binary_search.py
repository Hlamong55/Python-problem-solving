"""
Problem: Binary Search

Given a sorted array of integers nums and an integer target,
return the index of target if it exists in the array.

If target does not exist, return -1.

"""

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# Test Cases
nums = [-1, 0, 3, 5, 9, 12]

print(binary_search(nums, 9))   # 4
print(binary_search(nums, 2))   # -1
print(binary_search(nums, 12))  # 5
print(binary_search(nums, -1))  # 0