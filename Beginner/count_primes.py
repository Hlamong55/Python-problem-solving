"""
Problem: Count Primes

Given an integer n,
return the number of prime numbers
less than n.

Example:

Input: 10

Output: 4

Explanation:
The prime numbers less than 10 are:
2, 3, 5, 7
"""


def count_primes(n):

    if n <= 2:
        return 0

    prime = [True] * n
    prime[0] = prime[1] = False

    p = 2

    while p * p < n:

        if prime[p]:

            for i in range(p * p, n, p):
                prime[i] = False

        p += 1

    return sum(prime)


# Test Cases
print(count_primes(10))
print(count_primes(20))
print(count_primes(100))