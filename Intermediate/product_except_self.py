"""
Problem: Product of Array Except Self

Given an integer array nums,
return an array answer such that
answer[i] is equal to the product
of all the elements except nums[i].

Example:

nums = [1,2,3,4]

Output:
[24,12,8,6]
"""

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# Test Cases
print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))