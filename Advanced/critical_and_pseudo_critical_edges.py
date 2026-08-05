"""
Problem:

Find Critical and Pseudo-Critical Edges
in Minimum Spanning Tree

Given a weighted undirected graph,
return:

1. Critical edges
2. Pseudo-Critical edges

Example:

Input:

n = 5

edges = [

[0,1,1],
[1,2,1],
[2,3,2],
[0,3,2],
[0,4,3],
[3,4,3],
[1,4,6]

]

Output:

[[0,1],[2,3,4,5]]
"""


class UnionFind:

    def __init__(self, n):

        self.parent = list(range(n))
        self.rank = [0] * n

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


def find_critical_and_pseudo_critical_edges(n, edges):

    indexed_edges = []

    for index, edge in enumerate(edges):

        indexed_edges.append(edge + [index])

    indexed_edges.sort(key=lambda x: x[2])

    def kruskal(skip_edge=None, force_edge=None):

        uf = UnionFind(n)

        weight = 0

        used = 0

        if force_edge:

            u, v, w, _ = force_edge

            if uf.union(u, v):

                weight += w
                used += 1

        for edge in indexed_edges:

            if edge == skip_edge:
                continue

            u, v, w, _ = edge

            if uf.union(u, v):

                weight += w
                used += 1

        if used == n - 1:

            return weight

        return float("inf")

    mst_weight = kruskal()

    critical = []

    pseudo = []

    for edge in indexed_edges:

        if kruskal(skip_edge=edge) > mst_weight:

            critical.append(edge[3])

        elif kruskal(force_edge=edge) == mst_weight:

            pseudo.append(edge[3])

    return [critical, pseudo]


# Test

n = 5

edges = [

[0,1,1],
[1,2,1],
[2,3,2],
[0,3,2],
[0,4,3],
[3,4,3],
[1,4,6]

]

print(find_critical_and_pseudo_critical_edges(n, edges))