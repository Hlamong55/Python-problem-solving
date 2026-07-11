"""
Problem: Permutations

Given an array nums of distinct integers,
return all possible permutations.

Example:

Input:
nums = [1,2,3]

Output:
[
[1,2,3],
[1,3,2],
[2,1,3],
[2,3,1],
[3,1,2],
[3,2,1]
]
"""

def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return

        for i in range(len(remaining)):
            backtrack(
                path + [remaining[i]],
                remaining[:i] + remaining[i+1:]
            )

    backtrack([], nums)

    return result


print(permute([1,2,3]))