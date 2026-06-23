"""
Problem: Climbing Stairs

You are climbing a staircase.

It takes n steps to reach the top.

Each time you can climb either:
- 1 step
- 2 steps

Return the number of distinct ways
to climb to the top.

Example:
n = 2

Output:
2
"""

def climb_stairs(n):
    if n <= 2:
        return n

    first = 1
    second = 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second


# Test Cases
print(climb_stairs(2))  # 2
print(climb_stairs(3))  # 3
print(climb_stairs(5))  # 8
print(climb_stairs(7))  # 21