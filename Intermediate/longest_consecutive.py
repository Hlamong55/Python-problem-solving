"""
Problem: Longest Consecutive Sequence

Given an unsorted array of integers nums,
return the length of the longest consecutive sequence.

Example:

nums = [100,4,200,1,3,2]

Output:
4

Explanation:
The longest consecutive sequence is
[1,2,3,4]
"""

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            length = 1

            while num + length in num_set:
                length += 1

            longest = max(longest, length)

    return longest


# Test Cases
print(longest_consecutive([100,4,200,1,3,2]))
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))