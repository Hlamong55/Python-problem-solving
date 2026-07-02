"""
Problem: Evaluate Reverse Polish Notation

You are given an array of strings tokens
representing an arithmetic expression in Reverse Polish Notation.

Return the value of the expression.

Example:

tokens = ["2","1","+","3","*"]

Output:
9

Explanation:
(2 + 1) * 3 = 9
"""

def eval_rpn(tokens):
    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))

    return stack[0]


# Test Cases
print(eval_rpn(["2","1","+","3","*"]))      # 9
print(eval_rpn(["4","13","5","/","+"]))     # 6