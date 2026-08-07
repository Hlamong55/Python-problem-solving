"""
Problem: IPO

Suppose LeetCode will start its IPO.

You have:

- Initial capital (w)
- At most k projects

Each project has:

capital[i] = minimum capital needed
profits[i] = profit earned

Choose at most k projects to maximize
your final capital.

Example:

Input:

k = 2

w = 0

profits = [1,2,3]

capital = [0,1,1]

Output:

4
"""

import heapq


def find_maximized_capital(k, w, profits, capital):

    projects = list(zip(capital, profits))

    projects.sort()

    max_heap = []

    index = 0
    n = len(projects)

    current_capital = w

    for _ in range(k):

        while index < n and projects[index][0] <= current_capital:

            heapq.heappush(
                max_heap,
                -projects[index][1]
            )

            index += 1

        if not max_heap:

            break

        current_capital += -heapq.heappop(max_heap)

    return current_capital


# Test Cases

print(

    find_maximized_capital(

        2,
        0,
        [1,2,3],
        [0,1,1]

    )

)

print(

    find_maximized_capital(

        3,
        0,
        [1,2,3],
        [0,1,2]

    )

)

print(

    find_maximized_capital(

        1,
        2,
        [1,2,3],
        [1,1,2]

    )

)