"""
Problem: Making A Large Island

You are given an n x n binary grid.

You may change at most one 0 into 1.

Return the size of the largest island.

Example:

Input:

[
 [1,0],
 [0,1]
]

Output:

3
"""


def largest_island(grid):

    n = len(grid)

    island_id = 2

    island_size = {}

    directions = [

        (1,0),
        (-1,0),
        (0,1),
        (0,-1)

    ]

    def dfs(r, c, island):

        if (
            r < 0 or
            c < 0 or
            r >= n or
            c >= n or
            grid[r][c] != 1
        ):
            return 0

        grid[r][c] = island

        size = 1

        for dr, dc in directions:

            size += dfs(r + dr, c + dc, island)

        return size

    # Label every island

    for r in range(n):

        for c in range(n):

            if grid[r][c] == 1:

                size = dfs(r, c, island_id)

                island_size[island_id] = size

                island_id += 1

    answer = max(island_size.values(), default=0)

    # Try converting each 0 into 1

    for r in range(n):

        for c in range(n):

            if grid[r][c] == 0:

                seen = set()

                current = 1

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < n:

                        idx = grid[nr][nc]

                        if idx > 1 and idx not in seen:

                            seen.add(idx)

                            current += island_size[idx]

                answer = max(answer, current)

    return answer


# Test Cases

grid1 = [

    [1,0],
    [0,1]

]

grid2 = [

    [1,1],
    [1,0]

]

grid3 = [

    [1,1],
    [1,1]

]

print(largest_island(grid1))

print(largest_island(grid2))

print(largest_island(grid3))