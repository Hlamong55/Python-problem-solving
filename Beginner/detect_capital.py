"""
Problem: Detect Capital

We define the usage of capitals in a word to be correct when one of
the following cases holds:

1. All letters are uppercase.
2. All letters are lowercase.
3. Only the first letter is uppercase.

Return True if the capitalization is correct, otherwise False.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False
"""


def detect_capital_use(word):

    return (
        word.isupper()
        or word.islower()
        or word.istitle()
    )


# Test Cases

print(detect_capital_use("USA"))
print(detect_capital_use("leetcode"))
print(detect_capital_use("Google"))
print(detect_capital_use("FlaG"))