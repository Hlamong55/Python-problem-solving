"""
Problem: Swim in Rising Water

Return the minimum time required
to reach the bottom-right cell.

Example:

grid = [
    [0,2],
    [1,3]
]

Output:
3
"""

import heapq


def swim_in_water(grid):

    rows = len(grid)
    cols = len(grid[0])

    heap = [(grid[0][0], 0, 0)]
    visited = set()

    directions = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    while heap:

        time, r, c = heapq.heappop(heap)

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if r == rows - 1 and c == cols - 1:
            return time

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows
                and
                0 <= nc < cols
                and
                (nr, nc) not in visited
            ):
                heapq.heappush(
                    heap,
                    (
                        max(time, grid[nr][nc]),
                        nr,
                        nc
                    )
                )


grid = [
    [0,2],
    [1,3]
]

print(swim_in_water(grid))