"""
Problem: Minimum Cost to Connect Sticks

You have some sticks with different lengths.

A stick of length x and a stick of length y
can be connected into one stick with cost x + y.

Return the minimum total cost
to connect all sticks.

Example:

Input:

[2,4,3]

Output:

14

Explanation:

Connect 2 + 3 = 5

Cost = 5

Remaining:

[4,5]

Connect 4 + 5 = 9

Total Cost

5 + 9 = 14
"""

import heapq


def connect_sticks(sticks):

    if len(sticks) <= 1:
        return 0

    heapq.heapify(sticks)

    total_cost = 0

    while len(sticks) > 1:

        first = heapq.heappop(sticks)

        second = heapq.heappop(sticks)

        cost = first + second

        total_cost += cost

        heapq.heappush(sticks, cost)

    return total_cost


# Test Cases

print(connect_sticks([2,4,3]))

print(connect_sticks([1,8,3,5]))

print(connect_sticks([5]))

print(connect_sticks([1,2,3,4,5]))