"""
Problem: Pacific Atlantic Water Flow

There is an m x n grid of heights.

The Pacific Ocean touches the left and top edges.

The Atlantic Ocean touches the right and bottom edges.

Return all coordinates where water can flow
to both the Pacific and Atlantic oceans.

Example:

Input:

[
 [1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]
]

Output:

[
 [0,4],
 [1,3],
 [1,4],
 [2,2],
 [3,0],
 [3,1],
 [4,0]
]
"""

def pacific_atlantic(heights):

    if not heights:
        return []

    rows = len(heights)
    cols = len(heights[0])

    pacific = set()
    atlantic = set()

    directions = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    def dfs(r, c, visited):

        visited.add((r, c))

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (
                nr < 0 or
                nr >= rows or
                nc < 0 or
                nc >= cols
            ):
                continue

            if (nr, nc) in visited:
                continue

            if heights[nr][nc] < heights[r][c]:
                continue

            dfs(nr, nc, visited)

    for r in range(rows):
        dfs(r, 0, pacific)
        dfs(r, cols - 1, atlantic)

    for c in range(cols):
        dfs(0, c, pacific)
        dfs(rows - 1, c, atlantic)

    result = []

    for r in range(rows):
        for c in range(cols):
            if (r, c) in pacific and (r, c) in atlantic:
                result.append([r, c])

    return result


heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

print(pacific_atlantic(heights))