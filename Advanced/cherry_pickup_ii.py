"""
Problem: Cherry Pickup II

You are given a rows x cols grid.

Two robots start at:

Robot 1 -> top-left cell
Robot 2 -> top-right cell

Robot 1 starts at (0, 0)
Robot 2 starts at (0, cols - 1)

Both robots move one row down at each step.

From a cell, each robot can move:

- Down-left
- Down
- Down-right

If both robots are on the same cell,
the cherries from that cell are counted only once.

Return the maximum number of cherries
the two robots can collect.

Example:

Input:

[
    [3,1,1],
    [2,5,1],
    [1,5,5],
    [2,1,1]
]

Output:

24
"""


def cherry_pickup(grid):

    rows = len(grid)
    cols = len(grid[0])

    # dp[col1][col2]
    # represents the maximum cherries collected
    # when robot 1 is at col1 and robot 2 is at col2
    dp = [[0] * cols for _ in range(cols)]

    # Initial positions
    dp[0][cols - 1] = grid[0][0]

    if cols > 1:
        dp[0][cols - 1] += grid[0][cols - 1]

    for row in range(1, rows):

        new_dp = [
            [-1] * cols
            for _ in range(cols)
        ]

        for col1 in range(cols):

            for col2 in range(cols):

                if dp[col1][col2] == -1:
                    continue

                # Each robot can move -1, 0, +1 columns
                for move1 in (-1, 0, 1):

                    new_col1 = col1 + move1

                    if not (0 <= new_col1 < cols):
                        continue

                    for move2 in (-1, 0, 1):

                        new_col2 = col2 + move2

                        if not (0 <= new_col2 < cols):
                            continue

                        cherries = dp[col1][col2]

                        if new_col1 == new_col2:

                            cherries += grid[row][new_col1]

                        else:

                            cherries += (
                                grid[row][new_col1]
                                + grid[row][new_col2]
                            )

                        new_dp[new_col1][new_col2] = max(
                            new_dp[new_col1][new_col2],
                            cherries
                        )

        dp = new_dp

    return max(
        max(row)
        for row in dp
    )


# Test Case 1

grid1 = [
    [3, 1, 1],
    [2, 5, 1],
    [1, 5, 5],
    [2, 1, 1]
]

print(cherry_pickup(grid1))


# Test Case 2

grid2 = [
    [1, 0, 0, 0, 0, 0, 1],
    [2, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 1]
]

print(cherry_pickup(grid2))


# Test Case 3

grid3 = [
    [1, 1],
    [1, 1]
]

print(cherry_pickup(grid3))