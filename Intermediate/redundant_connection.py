"""
Problem: Redundant Connection

You are given a graph that started as a tree
with n nodes labeled from 1 to n.

One extra edge was added.

Return the edge that can be removed
so that the graph becomes a tree again.

Example 1:

Input:
edges = [[1,2],[1,3],[2,3]]

Output:
[2,3]

"""


def find_redundant_connection(edges):

    parent = {}
    rank = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])

        return parent[node]

    def union(node1, node2):

        root1 = find(node1)
        root2 = find(node2)

        if root1 == root2:
            return False

        if rank[root1] > rank[root2]:
            parent[root2] = root1

        elif rank[root1] < rank[root2]:
            parent[root1] = root2

        else:
            parent[root2] = root1
            rank[root1] += 1

        return True

    for u, v in edges:

        if u not in parent:
            parent[u] = u
            rank[u] = 0

        if v not in parent:
            parent[v] = v
            rank[v] = 0

        if not union(u, v):
            return [u, v]


# Test Cases
print(find_redundant_connection([[1,2],[1,3],[2,3]]))
print(find_redundant_connection([[1,2],[2,3],[3,4],[1,4],[1,5]]))