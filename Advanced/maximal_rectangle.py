"""
Problem: Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return
its area.

Example:

Input:

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

Output:

6
"""


def largest_rectangle_area(heights):

    stack = []
    max_area = 0

    for i, h in enumerate(heights):

        start = i

        while stack and stack[-1][1] > h:

            index, height = stack.pop()

            max_area = max(max_area, height * (i - index))

            start = index

        stack.append((start, h))

    n = len(heights)

    while stack:

        index, height = stack.pop()

        max_area = max(max_area, height * (n - index))

    return max_area


def maximal_rectangle(matrix):

    if not matrix or not matrix[0]:
        return 0

    cols = len(matrix[0])

    heights = [0] * cols

    answer = 0

    for row in matrix:

        for col in range(cols):

            if row[col] == "1":

                heights[col] += 1

            else:

                heights[col] = 0

        answer = max(answer, largest_rectangle_area(heights))

    return answer


# Test Cases

matrix1 = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

matrix2 = [
    ["0","1"],
    ["1","0"]
]

matrix3 = [
    ["1"]
]

matrix4 = [
    ["1","1","1"],
    ["1","1","1"]
]

print(maximal_rectangle(matrix1))
print(maximal_rectangle(matrix2))
print(maximal_rectangle(matrix3))
print(maximal_rectangle(matrix4))