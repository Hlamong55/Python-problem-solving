"""
Problem: Island Perimeter

You are given a grid where:

- 1 represents land
- 0 represents water

There is exactly one island.

Return the perimeter of the island.

Example:

Input:
grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]

Output:
16
"""


def island_perimeter(grid):

    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == 1:

                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter


# Test Cases

grid1 = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]

grid2 = [
    [1]
]

grid3 = [
    [1,0]
]

print(island_perimeter(grid1))
print(island_perimeter(grid2))
print(island_perimeter(grid3))