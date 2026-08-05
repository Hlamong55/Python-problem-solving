"""
Problem: Number of Islands II

You are given an empty m x n grid.

Initially all cells are water.

Each operation adds land at a position.

Return the number of islands after each operation.

Example:

Input:

m = 3
n = 3

positions =

[
    [0,0],
    [0,1],
    [1,2],
    [2,1],
    [1,1]
]

Output:

[1,1,2,3,1]
"""


class UnionFind:

    def __init__(self, size):

        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:

            self.parent[root_x] = root_y

        elif self.rank[root_x] > self.rank[root_y]:

            self.parent[root_y] = root_x

        else:

            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def num_islands2(m, n, positions):

    uf = UnionFind(m * n)

    land = set()

    count = 0

    result = []

    directions = [

        (1,0),
        (-1,0),
        (0,1),
        (0,-1)

    ]

    for row, col in positions:

        if (row, col) in land:

            result.append(count)
            continue

        land.add((row, col))

        count += 1

        current = row * n + col

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if (
                0 <= nr < m and
                0 <= nc < n and
                (nr, nc) in land
            ):

                neighbor = nr * n + nc

                if uf.union(current, neighbor):

                    count -= 1

        result.append(count)

    return result


# Test Cases

print(
    num_islands2(
        3,
        3,
        [
            [0,0],
            [0,1],
            [1,2],
            [2,1],
            [1,1]
        ]
    )
)

print(
    num_islands2(
        2,
        2,
        [
            [0,0],
            [1,1],
            [0,1]
        ]
    )
)