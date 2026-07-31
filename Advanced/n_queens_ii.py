"""
Problem: N-Queens II

The n-queens puzzle is the problem of placing n queens
on an n × n chessboard such that no two queens attack each other.

Return the total number of distinct solutions.

Example:

Input:
n = 4

Output:
2
"""


def total_n_queens(n):

    columns = set()
    diagonal1 = set()  # row - col
    diagonal2 = set()  # row + col

    count = 0

    def backtrack(row):

        nonlocal count

        if row == n:
            count += 1
            return

        for col in range(n):

            if (
                col in columns or
                (row - col) in diagonal1 or
                (row + col) in diagonal2
            ):
                continue

            columns.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)

            backtrack(row + 1)

            columns.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)

    backtrack(0)

    return count


# Test Cases

print(total_n_queens(1))
print(total_n_queens(4))
print(total_n_queens(5))
print(total_n_queens(8))