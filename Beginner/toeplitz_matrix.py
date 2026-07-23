"""
Problem: Toeplitz Matrix

A matrix is Toeplitz if every diagonal
from top-left to bottom-right has
the same element.

Return True if the matrix is Toeplitz.

Example:

Input:
[
 [1,2,3,4],
 [5,1,2,3],
 [9,5,1,2]
]

Output:
True
"""


def is_toeplitz(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        for j in range(1, cols):

            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False

    return True


# Test Cases

matrix1 = [
    [1,2,3,4],
    [5,1,2,3],
    [9,5,1,2]
]

matrix2 = [
    [1,2],
    [2,2]
]

print(is_toeplitz(matrix1))
print(is_toeplitz(matrix2))