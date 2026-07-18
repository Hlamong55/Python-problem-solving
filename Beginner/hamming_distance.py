"""
Problem: Hamming Distance

The Hamming distance between two integers
is the number of positions at which
the corresponding bits are different.

Example:

Input:
x = 1
y = 4

Output:
2
"""


def hamming_distance(x, y):

    xor = x ^ y
    distance = 0

    while xor:
        distance += xor & 1
        xor >>= 1

    return distance


# Test Cases
print(hamming_distance(1, 4))
print(hamming_distance(3, 1))
print(hamming_distance(7, 15))