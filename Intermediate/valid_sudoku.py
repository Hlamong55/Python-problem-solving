"""
Problem: Valid Sudoku

Determine if a 9x9 Sudoku board is valid.

Empty cells are represented by '.'.
"""

def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            value = board[r][c]

            if value == ".":
                continue

            box = (r // 3) * 3 + (c // 3)

            if value in rows[r] or value in cols[c] or value in boxes[box]:
                return False

            rows[r].add(value)
            cols[c].add(value)
            boxes[box].add(value)

    return True


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

print(is_valid_sudoku(board))