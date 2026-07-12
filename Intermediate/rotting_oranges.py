"""
Problem: Rotting Oranges

You are given an m x n grid.

0 = Empty Cell
1 = Fresh Orange
2 = Rotten Orange

Every minute, any fresh orange adjacent
(up, down, left, right) to a rotten orange
becomes rotten.

Return the minimum number of minutes
until no fresh orange remains.

If impossible, return -1.

Example:

Input:
[
[2,1,1],
[1,1,0],
[0,1,1]
]

Output:
4
"""

from collections import deque


def oranges_rotting(grid):

    rows = len(grid)
    cols = len(grid[0])

    queue = deque()
    fresh = 0
    minutes = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 2:
                queue.append((r, c))

            elif grid[r][c] == 1:
                fresh += 1

    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while queue and fresh > 0:

        for _ in range(len(queue)):

            row, col = queue.popleft()

            for dr, dc in directions:

                nr = row + dr
                nc = col + dc

                if (
                    nr < 0 or
                    nr >= rows or
                    nc < 0 or
                    nc >= cols or
                    grid[nr][nc] != 1
                ):
                    continue

                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc))

        minutes += 1

    if fresh == 0:
        return minutes

    return -1


grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

print(oranges_rotting(grid))