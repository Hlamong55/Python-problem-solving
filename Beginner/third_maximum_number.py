"""
Problem: Third Maximum Number

Given an integer array nums,
return the third distinct maximum number.

If the third distinct maximum does not exist,
return the maximum number.

Example 1:
Input: [3,2,1]
Output: 1
"""


def third_max(nums):

    first = second = third = None

    for num in nums:

        if num == first or num == second or num == third:
            continue

        if first is None or num > first:
            third = second
            second = first
            first = num

        elif second is None or num > second:
            third = second
            second = num

        elif third is None or num > third:
            third = num

    return third if third is not None else first


# Test Cases
print(third_max([3, 2, 1]))
print(third_max([1, 2]))
print(third_max([2, 2, 3, 1]))
print(third_max([5, 2, 2]))