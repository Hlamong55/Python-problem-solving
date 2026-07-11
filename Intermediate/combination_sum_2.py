"""
Problem: Combination Sum II

Each number may only be used once.

Example:

Input:
candidates=[10,1,2,7,6,1,5]
target=8

Output:
[[1,1,6],[1,2,5],[1,7],[2,6]]
"""

def combination_sum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path[:])
            return

        if total > target:
            return

        prev = -1

        for i in range(start, len(candidates)):
            if candidates[i] == prev:
                continue

            path.append(candidates[i])

            backtrack(i + 1, path, total + candidates[i])

            path.pop()

            prev = candidates[i]

    backtrack(0, [], 0)

    return result


print(combination_sum2([10,1,2,7,6,1,5],8))