"""
Problem: Minimum Number of Refueling Stops

You have a car with some initial fuel.
You need to travel to a target distance.

Each station is represented as:

[position, fuel]

Return the minimum number of refueling stops
needed to reach the target.

If it is impossible, return -1.

Example:

target = 100
startFuel = 10

stations = [
    [10,60],
    [20,30],
    [30,30],
    [60,40]
]

Output:
2
"""

import heapq


def min_refuel_stops(target, start_fuel, stations):

    max_heap = []

    fuel = start_fuel
    stops = 0
    index = 0

    stations.sort()

    while fuel < target:

        # Add all reachable stations
        while (
            index < len(stations)
            and stations[index][0] <= fuel
        ):

            position, station_fuel = stations[index]

            heapq.heappush(
                max_heap,
                -station_fuel
            )

            index += 1

        # No reachable station
        if not max_heap:
            return -1

        # Refuel from the station
        fuel += -heapq.heappop(max_heap)

        stops += 1

    return stops


# Test Case 1

print(
    min_refuel_stops(
        100,
        10,
        [
            [10,60],
            [20,30],
            [30,30],
            [60,40]
        ]
    )
)


# Test Case 2

print(
    min_refuel_stops(
        100,
        50,
        [
            [25,25],
            [50,50]
        ]
    )
)


# Test Case 3

print(
    min_refuel_stops(
        100,
        1,
        [
            [10,100]
        ]
    )
)


# Test Case 4

print(
    min_refuel_stops(
        100,
        100,
        []
    )
)