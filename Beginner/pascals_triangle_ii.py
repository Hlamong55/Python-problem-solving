"""
Problem: Pascal's Triangle II

Given an integer rowIndex,
return the rowIndex-th (0-indexed)
row of Pascal's Triangle.

Example:

Input: 3

Output:
[1,3,3,1]
"""


def get_row(row_index):

    row = [1]

    for _ in range(row_index):
        new_row = [1]

        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])

        new_row.append(1)
        row = new_row

    return row


# Test Cases
print(get_row(0))
print(get_row(3))
print(get_row(5))