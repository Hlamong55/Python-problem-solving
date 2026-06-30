"""
Problem: Daily Temperatures

Given an array temperatures,
return an array such that answer[i]
is the number of days until
a warmer temperature.

Example:

temperatures = [73,74,75,71,69,72,76,73]

Output:
[1,1,4,2,1,1,0,0]
"""

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):

        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index

        stack.append(i)

    return result


# Test Cases
print(daily_temperatures([73,74,75,71,69,72,76,73]))
print(daily_temperatures([30,40,50,60]))
print(daily_temperatures([30,60,90]))