"""
Problem: Network Delay Time

You are given a network of n nodes numbered from 1 to n.

You are also given times, a list of travel times as directed edges.

times[i] = (u, v, w)

where

u -> source
v -> destination
w -> travel time

Return the minimum time needed for all nodes
to receive the signal.

If impossible, return -1.

Example:

Input:

times = [
    [2,1,1],
    [2,3,1],
    [3,4,1]
]

n = 4

k = 2

Output:

2
"""

from collections import defaultdict
import heapq


def network_delay_time(times, n, k):

    graph = defaultdict(list)

    for source, destination, weight in times:

        graph[source].append((destination, weight))

    min_heap = [(0, k)]

    visited = set()

    max_time = 0

    while min_heap:

        current_time, node = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        max_time = current_time

        for neighbor, weight in graph[node]:

            if neighbor not in visited:

                heapq.heappush(
                    min_heap,
                    (current_time + weight, neighbor)
                )

    if len(visited) == n:
        return max_time

    return -1


# Test Cases

times1 = [
    [2,1,1],
    [2,3,1],
    [3,4,1]
]

times2 = [
    [1,2,1]
]

times3 = [
    [1,2,1],
    [2,3,2],
    [1,3,4]
]

print(network_delay_time(times1, 4, 2))
print(network_delay_time(times2, 2, 1))
print(network_delay_time(times3, 3, 1))