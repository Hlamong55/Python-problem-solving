"""
Problem: The Skyline Problem

A city's skyline is formed by buildings.

Each building is represented as:

[left, right, height]

Return the skyline formed by these buildings.

Example:

Input:

[
 [2,9,10],
 [3,7,15],
 [5,12,12],
 [15,20,10],
 [19,24,8]
]

Output:

[
 [2,10],
 [3,15],
 [7,12],
 [12,0],
 [15,10],
 [20,8],
 [24,0]
]
"""

import heapq


def get_skyline(buildings):

    events = []

    for left, right, height in buildings:

        events.append((left, -height, right))
        events.append((right, 0, 0))

    events.sort()

    result = []

    heap = [(0, float("inf"))]

    for x, neg_height, right in events:

        while heap and heap[0][1] <= x:

            heapq.heappop(heap)

        if neg_height != 0:

            heapq.heappush(
                heap,
                (neg_height, right)
            )

        current_height = -heap[0][0]

        if (
            not result or
            result[-1][1] != current_height
        ):

            result.append(
                [x, current_height]
            )

    return result


# Test Cases

buildings1 = [

    [2,9,10],
    [3,7,15],
    [5,12,12],
    [15,20,10],
    [19,24,8]

]

buildings2 = [

    [0,2,3],
    [2,5,3]

]

print(get_skyline(buildings1))

print(get_skyline(buildings2))