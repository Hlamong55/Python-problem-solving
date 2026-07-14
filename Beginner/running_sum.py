"""
Problem: Running Sum of 1D Array

Given an array nums,
return the running sum of nums.

Running Sum:

runningSum[i] = sum(nums[0] ... nums[i])

Example:

Input:
nums = [1,2,3,4]

Output:
[1,3,6,10]
"""


def running_sum(nums):

    result = []
    current_sum = 0

    for number in nums:
        current_sum += number
        result.append(current_sum)

    return result


# Test Cases

print(running_sum([1,2,3,4]))
print(running_sum([1,1,1,1,1]))
print(running_sum([3,1,2,10,1]))