"""
Problem: Reconstruct Itinerary

You are given a list of airline tickets where
tickets[i] = [from, to].

Reconstruct the itinerary in order.

Rules:

- Begin from "JFK".
- Use all tickets exactly once.
- If multiple valid itineraries exist,
  return the lexicographically smallest one.

Example:

Input:

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

    # Sort in reverse so we can pop the smallest destination
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

tickets2 = [
    ["JFK","SFO"],
    ["JFK","ATL"],
    ["SFO","ATL"],
    ["ATL","JFK"],
    ["ATL","SFO"]
]

print(find_itinerary(tickets1))
print(find_itinerary(tickets2))