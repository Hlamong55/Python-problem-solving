"""
Problem: Shortest Path in a Grid with Obstacles Elimination

You are given an m x n grid where:

0 = Empty cell
1 = Obstacle

You may eliminate at most k obstacles.

Return the minimum number of steps required
to reach the bottom-right corner.

Return -1 if impossible.

Example:

Input:

grid =

[
 [0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]
]

k = 1

Output:

6
"""

from collections import deque


def shortest_path(grid, k):

    rows = len(grid)
    cols = len(grid[0])

    if rows == 1 and cols == 1:
        return 0

    queue = deque([(0, 0, k, 0)])

    visited = {(0, 0, k)}

    directions = [

        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)

    ]

    while queue:

        row, col, remaining, steps = queue.popleft()

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            if nr == rows - 1 and nc == cols - 1:
                return steps + 1

            new_remaining = remaining - grid[nr][nc]

            if new_remaining < 0:
                continue

            state = (nr, nc, new_remaining)

            if state in visited:
                continue

            visited.add(state)

            queue.append(

                (
                    nr,
                    nc,
                    new_remaining,
                    steps + 1
                )

            )

    return -1


# Test Cases

grid1 = [

    [0,0,0],
    [1,1,0],
    [0,0,0],
    [0,1,1],
    [0,0,0]

]

grid2 = [

    [0,1,1],
    [1,1,1],
    [1,0,0]

]

print(shortest_path(grid1, 1))

print(shortest_path(grid2, 1))