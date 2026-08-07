"""
Problem: Minimum Cost to Hire K Workers

There are n workers.

Each worker has:

quality[i]
wage[i]

To hire workers:

1. Every worker must receive at least their minimum wage.
2. Workers are paid proportional to their quality.

Return the minimum cost to hire exactly k workers.

Example:

Input:

quality = [10,20,5]

wage = [70,50,30]

k = 2

Output:

105.0
"""

import heapq


def mincost_to_hire_workers(quality, wage, k):

    workers = []

    for q, w in zip(quality, wage):

        workers.append((w / q, q))

    workers.sort()

    max_heap = []

    quality_sum = 0

    answer = float("inf")

    for ratio, q in workers:

        heapq.heappush(max_heap, -q)

        quality_sum += q

        if len(max_heap) > k:

            quality_sum += heapq.heappop(max_heap)

        if len(max_heap) == k:

            answer = min(

                answer,

                quality_sum * ratio

            )

    return answer


# Test Cases

print(

    round(

        mincost_to_hire_workers(

            [10,20,5],

            [70,50,30],

            2

        ),

        5

    )

)

print(

    round(

        mincost_to_hire_workers(

            [3,1,10,10,1],

            [4,8,2,2,7],

            3

        ),

        5

    )

)