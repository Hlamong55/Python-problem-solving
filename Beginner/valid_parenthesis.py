"""
Problem: Valid Parentheses

Given a string containing just the characters:
'(', ')', '{', '}', '[' and ']',

Determine if the input string is valid.

A string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

"""

def is_valid(s):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


# Test Cases
print(is_valid("()"))       # True
print(is_valid("()[]{}"))   # True
print(is_valid("(]"))       # False
print(is_valid("([)]"))     # False
print(is_valid("{[]}"))     # True