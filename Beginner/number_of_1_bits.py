"""
Problem: Number of 1 Bits

Given a positive integer, return the number
of '1' bits in its binary representation.

Example:

Input: 11
Binary: 1011

Output: 3
"""


def hamming_weight(n):

    count = 0

    while n:

        count += n & 1
        n >>= 1

    return count


# Test Cases
print(hamming_weight(11))
print(hamming_weight(128))
print(hamming_weight(255))