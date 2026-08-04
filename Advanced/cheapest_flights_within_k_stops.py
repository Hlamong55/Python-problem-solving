"""
Problem: Cheapest Flights Within K Stops

There are n cities connected by flights.

Each flight is represented as:

[from, to, price]

Return the cheapest price from src to dst
with at most k stops.

If no route exists, return -1.

Example:

Input:

n = 4

flights =

[
    [0,1,100],
    [1,2,100],
    [2,3,100],
    [0,2,500]
]

src = 0
dst = 3
k = 1

Output:

600
"""

from collections import defaultdict
import heapq


def find_cheapest_price(n, flights, src, dst, k):

    graph = defaultdict(list)

    for start, end, price in flights:

        graph[start].append((end, price))

    heap = [(0, src, 0)]

    visited = {}

    while heap:

        cost, city, stops = heapq.heappop(heap)

        if city == dst:
            return cost

        if stops > k:
            continue

        if (city, stops) in visited and visited[(city, stops)] <= cost:
            continue

        visited[(city, stops)] = cost

        for next_city, price in graph[city]:

            heapq.heappush(
                heap,
                (
                    cost + price,
                    next_city,
                    stops + 1
                )
            )

    return -1


# Test Cases

flights1 = [
    [0,1,100],
    [1,2,100],
    [2,3,100],
    [0,2,500]
]

flights2 = [
    [0,1,100],
    [1,2,100],
    [0,2,500]
]

print(find_cheapest_price(4, flights1, 0, 3, 1))

print(find_cheapest_price(3, flights2, 0, 2, 1))

print(find_cheapest_price(3, flights2, 0, 2, 0))