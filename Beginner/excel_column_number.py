"""
Problem: Excel Sheet Column Number

Given a column title as it appears in Excel,
return its corresponding column number.

Example:

A -> 1
AB -> 28
ZY -> 701
"""


def title_to_number(column):

    result = 0

    for ch in column:
        result = result * 26 + (ord(ch) - ord("A") + 1)

    return result


# Test Cases
print(title_to_number("A"))
print(title_to_number("AB"))
print(title_to_number("ZY"))