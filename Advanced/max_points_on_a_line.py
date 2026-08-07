"""
Problem: Max Points on a Line

Given an array of points where
points[i] = [x, y],

return the maximum number of points
that lie on the same straight line.

Example:

Input:

points =

[
 [1,1],
 [2,2],
 [3,3]
]

Output:

3
"""

from collections import defaultdict
from math import gcd


def max_points(points):

    n = len(points)

    if n <= 2:
        return n

    answer = 1

    for i in range(n):

        slopes = defaultdict(int)

        duplicates = 1

        current_max = 0

        x1, y1 = points[i]

        for j in range(i + 1, n):

            x2, y2 = points[j]

            dx = x2 - x1
            dy = y2 - y1

            if dx == 0 and dy == 0:

                duplicates += 1

                continue

            g = gcd(dx, dy)

            dx //= g
            dy //= g

            # Normalize slope representation
            if dx < 0:

                dx *= -1
                dy *= -1

            elif dx == 0:

                dy = 1

            elif dy == 0:

                dx = 1

            slopes[(dy, dx)] += 1

            current_max = max(
                current_max,
                slopes[(dy, dx)]
            )

        answer = max(
            answer,
            current_max + duplicates
        )

    return answer


# Test Cases

print(

    max_points(

        [

            [1,1],
            [2,2],
            [3,3]

        ]

    )

)

print(

    max_points(

        [

            [1,1],
            [3,2],
            [5,3],
            [4,1],
            [2,3],
            [1,4]

        ]

    )

)

print(

    max_points(

        [

            [0,0],
            [0,1],
            [0,-1]

        ]

    )

)