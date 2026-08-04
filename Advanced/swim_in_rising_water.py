"""
Problem: Swim in Rising Water

You are given an n x n integer matrix grid where
each value represents the elevation.

Rain starts falling.

At time t, you can enter cells with elevation <= t.

Return the minimum time required to travel
from the top-left corner to the bottom-right corner.

Example:

Input:

grid =

[
 [0,2],
 [1,3]
]

Output:

3
"""

import heapq


def swim_in_water(grid):

    n = len(grid)

    directions = [

        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)

    ]

    min_heap = [

        (grid[0][0], 0, 0)

    ]

    visited = set()

    while min_heap:

        time, row, col = heapq.heappop(min_heap)

        if (row, col) in visited:
            continue

        visited.add((row, col))

        if row == n - 1 and col == n - 1:

            return time

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if (
                0 <= nr < n and
                0 <= nc < n and
                (nr, nc) not in visited
            ):

                heapq.heappush(

                    min_heap,

                    (
                        max(time, grid[nr][nc]),
                        nr,
                        nc
                    )

                )

    return -1


# Test Cases

grid1 = [

    [0,2],
    [1,3]

]

grid2 = [

    [0,1,2,3,4],
    [24,23,22,21,5],
    [12,13,14,15,16],
    [11,17,18,19,20],
    [10,9,8,7,6]

]

print(swim_in_water(grid1))

print(swim_in_water(grid2))