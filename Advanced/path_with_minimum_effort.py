"""
Problem: Path With Minimum Effort

You are given an m x n matrix heights.

You can move up, down, left, or right.

The effort of a path is defined as the
maximum absolute difference in heights
between two consecutive cells.

Return the minimum effort required
to travel from the top-left cell
to the bottom-right cell.

Example:

Input:

heights =

[
 [1,2,2],
 [3,8,2],
 [5,3,5]
]

Output:

2
"""

import heapq


def minimum_effort_path(heights):

    rows = len(heights)
    cols = len(heights[0])

    effort = [[float("inf")] * cols for _ in range(rows)]

    effort[0][0] = 0

    heap = [(0, 0, 0)]

    directions = [

        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)

    ]

    while heap:

        current_effort, row, col = heapq.heappop(heap)

        if row == rows - 1 and col == cols - 1:

            return current_effort

        if current_effort > effort[row][col]:

            continue

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if 0 <= nr < rows and 0 <= nc < cols:

                diff = abs(
                    heights[row][col] -
                    heights[nr][nc]
                )

                new_effort = max(current_effort, diff)

                if new_effort < effort[nr][nc]:

                    effort[nr][nc] = new_effort

                    heapq.heappush(

                        heap,

                        (
                            new_effort,
                            nr,
                            nc
                        )

                    )

    return 0


# Test Cases

grid1 = [

    [1,2,2],
    [3,8,2],
    [5,3,5]

]

grid2 = [

    [1,2,3],
    [3,8,4],
    [5,3,5]

]

grid3 = [

    [1,2,1,1,1],
    [1,2,1,2,1],
    [1,2,1,2,1],
    [1,2,1,2,1],
    [1,1,1,2,1]

]

print(minimum_effort_path(grid1))

print(minimum_effort_path(grid2))

print(minimum_effort_path(grid3))