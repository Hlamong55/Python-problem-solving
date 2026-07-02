"""
Problem: Car Fleet

Given the target, position and speed arrays,
return the number of car fleets that arrive at the destination.

Example:

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

Output:
3
"""

def car_fleet(target, position, speed):
    cars = sorted(zip(position, speed), reverse=True)

    stack = []

    for pos, spd in cars:
        time = (target - pos) / spd
        stack.append(time)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


# Test Cases
print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))  # 3
print(car_fleet(10, [3], [3]))                   # 1