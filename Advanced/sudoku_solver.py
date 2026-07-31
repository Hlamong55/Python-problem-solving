"""
Problem: Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

Rules:
- Each row must contain digits 1-9 exactly once.
- Each column must contain digits 1-9 exactly once.
- Each 3x3 sub-box must contain digits 1-9 exactly once.

Empty cells are represented by '.'.
"""


def solve_sudoku(board):

    def is_valid(row, col, num):

        # Check row
        for c in range(9):
            if board[row][c] == num:
                return False

        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3

        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def backtrack():

        for r in range(9):

            for c in range(9):

                if board[r][c] == ".":

                    for num in "123456789":

                        if is_valid(r, c, num):

                            board[r][c] = num

                            if backtrack():
                                return True

                            board[r][c] = "."

                    return False

        return True

    backtrack()


board = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(board)

for row in board:
    print(row)