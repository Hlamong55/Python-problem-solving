"""
Problem: Intersection of Two Arrays

Given two integer arrays nums1 and nums2,
return their intersection.

Each element in the result must be unique.

Example:

nums1 = [1,2,2,1]
nums2 = [2,2]

Output:
[2]
"""

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


# Test Cases
print(intersection([1,2,2,1], [2,2]))      # [2]
print(intersection([4,9,5], [9,4,9,8,4]))  # [4, 9]
print(intersection([1,2,3], [4,5,6]))      # []