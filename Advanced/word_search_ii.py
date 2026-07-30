"""
Problem: Word Search II

Given an m x n board of characters and a list of words,
return all words on the board.

Each word must be constructed from adjacent cells
(horizontal or vertical).

A cell may not be used more than once in a word.

Example:

Input:

board =

[
 ['o','a','a','n'],
 ['e','t','a','e'],
 ['i','h','k','r'],
 ['i','f','l','v']
]

words =

["oath","pea","eat","rain"]

Output:

["oath","eat"]
"""


class TrieNode:

    def __init__(self):

        self.children = {}
        self.word = None


def build_trie(words):

    root = TrieNode()

    for word in words:

        node = root

        for ch in word:

            if ch not in node.children:

                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.word = word

    return root


def find_words(board, words):

    if not board or not words:

        return []

    rows = len(board)
    cols = len(board[0])

    root = build_trie(words)

    result = []

    def dfs(r, c, node):

        letter = board[r][c]

        if letter not in node.children:

            return

        nxt = node.children[letter]

        if nxt.word:

            result.append(nxt.word)

            nxt.word = None

        board[r][c] = "#"

        directions = [

            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)

        ]

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                board[nr][nc] != "#"
            ):

                dfs(nr, nc, nxt)

        board[r][c] = letter

    for i in range(rows):

        for j in range(cols):

            dfs(i, j, root)

    return result


board = [

    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']

]

words = [

    "oath",
    "pea",
    "eat",
    "rain"

]

print(find_words(board, words))