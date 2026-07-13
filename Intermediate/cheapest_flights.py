"""
Problem: Cheapest Flights Within K Stops

Return the cheapest price from src to dst
with at most k stops.

Example:

n = 4

flights = [
    [0,1,100],
    [1,2,100],
    [2,3,100],
    [0,3,500]
]

src = 0
dst = 3
k = 1

Output:
500
"""

from collections import defaultdict, deque


def find_cheapest_price(n, flights, src, dst, k):

    graph = defaultdict(list)

    for s, d, p in flights:
        graph[s].append((d, p))

    queue = deque([(src, 0)])
    prices = [float("inf")] * n
    prices[src] = 0

    stops = 0

    while queue and stops <= k:

        for _ in range(len(queue)):

            city, cost = queue.popleft()

            for neighbor, price in graph[city]:

                new_cost = cost + price

                if new_cost < prices[neighbor]:
                    prices[neighbor] = new_cost
                    queue.append((neighbor, new_cost))

        stops += 1

    return prices[dst] if prices[dst] != float("inf") else -1


print(find_cheapest_price(
    4,
    [
        [0,1,100],
        [1,2,100],
        [2,3,100],
        [0,3,500]
    ],
    0,
    3,
    1
))