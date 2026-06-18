"""
Problem: Contains Duplicate

Given an integer array nums,
return True if any value appears at least twice in the array,
and return False if every element is distinct.

"""

def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False


# Test Cases
print(contains_duplicate([1, 2, 3, 1]))     # True
print(contains_duplicate([1, 2, 3, 4]))     # False
print(contains_duplicate([1, 1, 1, 1]))     # True
print(contains_duplicate([5, 6, 7, 8]))     # False