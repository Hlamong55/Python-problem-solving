"""
Problem: Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements.

Example:

nums = [1,1,1,2,2,3]
k = 2

Output:
[1,2]
"""

from collections import Counter


def top_k_frequent(nums, k):
    frequency = Counter(nums)
    sorted_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    result = []

    for num, count in sorted_items[:k]:
        result.append(num)

    return result


# Test Cases
print(top_k_frequent([1,1,1,2,2,3], 2))
print(top_k_frequent([1], 1))
print(top_k_frequent([4,4,4,5,5,6], 2))