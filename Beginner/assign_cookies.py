"""
Problem: Assign Cookies

Assume you are an awesome parent and want to give
your children cookies.

Each child has a greed factor g[i].
Each cookie has a size s[j].

A child is satisfied if cookie_size >= greed_factor.

Return the maximum number of satisfied children.

Example:

Input:
g = [1,2,3]
s = [1,1]

Output:
1
"""


def find_content_children(g, s):

    g.sort()
    s.sort()

    child = 0
    cookie = 0

    while child < len(g) and cookie < len(s):

        if s[cookie] >= g[child]:
            child += 1

        cookie += 1

    return child


# Test Cases

print(find_content_children([1, 2, 3], [1, 1]))
print(find_content_children([1, 2], [1, 2, 3]))