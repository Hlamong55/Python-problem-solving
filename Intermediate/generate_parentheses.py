"""
Problem: Generate Parentheses

Given n pairs of parentheses,
generate all combinations of well-formed parentheses.

Example:

n = 3

Output:
['((()))', '(()())', '(())()', '()(())', '()()()']
"""

def generate_parentheses(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == n * 2:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)

    return result


# Test Cases
print(generate_parentheses(3))
print(generate_parentheses(2))