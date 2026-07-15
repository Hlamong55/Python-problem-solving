"""
Problem: Length of Last Word

Given a string consisting of words
and spaces, return the length
of the last word.

Example:

Input:
"Hello World"

Output:
5
"""


def length_of_last_word(text):

    words = text.strip().split()

    return len(words[-1])


# Test Cases
print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("Python"))