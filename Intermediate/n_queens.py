"""
Problem: N Queens

Given n,
return all distinct solutions.

Example:

Input:
n=4

Output:
[
[".Q..",
 "...Q",
 "Q...",
 "..Q."],

["..Q.",
 "Q...",
 "...Q",
 ".Q.."]
]
"""

def solve_n_queens(n):

    board = [["."] * n for _ in range(n)]

    columns = set()
    positive = set()
    negative = set()

    result = []

    def backtrack(row):

        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):

            if (
                col in columns or
                row + col in positive or
                row - col in negative
            ):
                continue

            columns.add(col)
            positive.add(row + col)
            negative.add(row - col)

            board[row][col] = "Q"

            backtrack(row + 1)

            board[row][col] = "."

            columns.remove(col)
            positive.remove(row + col)
            negative.remove(row - col)

    backtrack(0)

    return result


print(solve_n_queens(4))