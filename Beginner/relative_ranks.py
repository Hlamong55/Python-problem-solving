"""
Problem: Relative Ranks

You are given an integer array score where score[i]
is the score of the ith athlete.

Return an array of strings where:

- "Gold Medal" for the highest score
- "Silver Medal" for the second highest
- "Bronze Medal" for the third highest
- The placement number for the rest

Example:

Input:
score = [5,4,3,2,1]

Output:
["Gold Medal","Silver Medal","Bronze Medal","4","5"]
"""


def find_relative_ranks(score):

    sorted_scores = sorted(score, reverse=True)

    ranks = {}

    for i, value in enumerate(sorted_scores):

        if i == 0:
            ranks[value] = "Gold Medal"

        elif i == 1:
            ranks[value] = "Silver Medal"

        elif i == 2:
            ranks[value] = "Bronze Medal"

        else:
            ranks[value] = str(i + 1)

    result = []

    for value in score:
        result.append(ranks[value])

    return result


# Test Cases

print(find_relative_ranks([5, 4, 3, 2, 1]))
print(find_relative_ranks([10, 3, 8, 9, 4]))
