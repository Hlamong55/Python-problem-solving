"""
Problem: Graph Valid Tree

Given n nodes labeled from 0 to n - 1
and a list of undirected edges,
determine if the graph forms a valid tree.

A valid tree must:
1. Be connected
2. Contain no cycles

Example 1:

n = 5
edges = [
    [0,1],
    [0,2],
    [0,3],
    [1,4]
]

Output:
True
"""

from collections import defaultdict


def valid_tree(n, edges):

    if len(edges) != n - 1:
        return False

    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):

        if node in visited:
            return False

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor == parent:
                continue

            if not dfs(neighbor, node):
                return False

        return True

    if not dfs(0, -1):
        return False

    return len(visited) == n


# Test Cases

print(
    valid_tree(
        5,
        [
            [0,1],
            [0,2],
            [0,3],
            [1,4]
        ]
    )
)

print(
    valid_tree(
        5,
        [
            [0,1],
            [1,2],
            [2,3],
            [1,3],
            [1,4]
        ]
    )
)