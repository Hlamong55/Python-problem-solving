"""
Problem: Kth Largest Element in an Array

Given an integer array nums and an integer k,
return the kth largest element in the array.

Example:

nums = [3,2,1,5,6,4]
k = 2

Output:
5
"""

import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


# Test Cases
print(find_kth_largest([3,2,1,5,6,4], 2))   # 5
print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4))   # 4