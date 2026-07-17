"""
Problem: Nim Game

You are playing the Nim Game.

There is a pile of stones, and each turn
you can remove 1, 2, or 3 stones.

Return True if you can win assuming
both players play optimally.

Example:

Input: 4
Output: False

Input: 5
Output: True
"""


def can_win_nim(n):

    return n % 4 != 0


# Test Cases
print(can_win_nim(4))
print(can_win_nim(5))
print(can_win_nim(8))
print(can_win_nim(10))