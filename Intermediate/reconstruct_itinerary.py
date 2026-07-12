"""
Problem: Reconstruct Itinerary

You are given a list of airline tickets.

tickets[i] = [from, to]

Reconstruct the itinerary in order.

The itinerary must begin with "JFK".

If multiple valid itineraries exist,
return the lexicographically smallest one.

Example 1:

tickets = [
    ["MUC","LHR"],
    ["JFK","MUC"],
    ["SFO","SJC"],
    ["LHR","SFO"]
]

Output:

["JFK","MUC","LHR","SFO","SJC"]
"""

from collections import defaultdict


def find_itinerary(tickets):

    graph = defaultdict(list)

    # Reverse sort so we can pop the smallest destination
    for source, destination in sorted(tickets, reverse=True):
        graph[source].append(destination)

    itinerary = []

    def dfs(airport):

        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)

        itinerary.append(airport)

    dfs("JFK")

    return itinerary[::-1]


# Test Cases

tickets1 = [
    ["MUC","LHR"],
    ["JFK","MUC"],
    ["LHR","SFO"],
    ["SFO","SJC"]
]

print(find_itinerary(tickets1))


tickets2 = [
    ["JFK","SFO"],
    ["JFK","ATL"],
    ["SFO","ATL"],
    ["ATL","JFK"],
    ["ATL","SFO"]
]

print(find_itinerary(tickets2))