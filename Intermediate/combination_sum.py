"""
Problem: Combination Sum

Given an array of distinct integers candidates
and a target integer target,
return all unique combinations where
the chosen numbers sum to target.

The same number may be chosen
an unlimited number of times.

Example:

candidates = [2,3,6,7]
target = 7

Output:
[[2,2,3],[7]]
"""

def combination_sum(candidates, target):
    result = []

    def backtrack(index, current, total):
        if total == target:
            result.append(current[:])
            return

        if total > target or index >= len(candidates):
            return

        current.append(candidates[index])
        backtrack(index, current, total + candidates[index])

        current.pop()
        backtrack(index + 1, current, total)

    backtrack(0, [], 0)

    return result


# Test Cases
print(combination_sum([2,3,6,7], 7))
print(combination_sum([2,3,5], 8))