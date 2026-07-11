"""
Problem: Subsets

Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution must not contain duplicate subsets.

Example:

Input:
nums = [1,2,3]

Output:
[
    [],
    [1],
    [2],
    [3],
    [1,2],
    [1,3],
    [2,3],
    [1,2,3]
]
"""

def subsets(nums):
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            return

        # Include current number
        current.append(nums[index])
        backtrack(index + 1, current)

        # Exclude current number
        current.pop()
        backtrack(index + 1, current)

    backtrack(0, [])

    return result


# Test Cases
print(subsets([1,2,3]))
print(subsets([0]))
print(subsets([1,2]))