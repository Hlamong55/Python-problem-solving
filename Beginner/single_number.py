"""
Problem: Single Number

Given a non-empty array of integers,
every element appears twice except for one.

Find that single one.

Example:

Input:
[2,2,1]

Output:
1
"""


def single_number(nums):

    result = 0

    for num in nums:
        result ^= num

    return result


# Test Cases
print(single_number([2,2,1]))
print(single_number([4,1,2,1,2]))
print(single_number([1]))