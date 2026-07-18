"""
Problem: Pascal's Triangle

Given an integer numRows,
return the first numRows
of Pascal's Triangle.

Example:

Input: 5

Output:

[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]
"""


def generate(num_rows):

    triangle = []

    for i in range(num_rows):

        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle


# Test Cases
print(generate(1))
print(generate(5))