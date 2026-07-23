"""
Problem: Squares of a Sorted Array

Given a sorted integer array nums,
return an array of the squares of each number,
sorted in non-decreasing order.

Example:

Input:
[-4,-1,0,3,10]

Output:
[0,1,9,16,100]
"""


def sorted_squares(nums):

    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)

    index = len(nums) - 1

    while left <= right:

        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1

        index -= 1

    return result


# Test Cases

print(sorted_squares([-4, -1, 0, 3, 10]))
print(sorted_squares([-7, -3, 2, 3, 11]))