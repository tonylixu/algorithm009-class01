"""
Clarification
  - All words contain small letters
  - The values of words are distinct
  - If not board, return []
Possible Solutions
  - Iterative words, based on https://leetcode.com/problems/word-search/
    - Time complexity: O(N*m*m*4^k), N is the number of words, m is the board size, k is the average length
  - Tire, construct prefix tree, then DFS search the board
    - Time complexity: O(m*m*(4*3^(L-1))), L is the maximum length of the word, m is the length of the board
    - Space complexity: O(N), N is the total letters in Trie.
"""
from collections import defaultdict


# Define TrieNode
class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.word = None


# Define Trie
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        tn = self.root
        for c in word:
            tn = tn.nodes[c]
        tn.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board == 0:
            return []
        # Construct Trie and insert all words into Trie
        trie = Trie()
        for w in words:
            trie.insert(w)
        # Trie looks like, use eat as an example
        # defaultdict(<class '__main__.TrieNode'>,
        # {'e': defaultdict(TrieNode, {'a': defaultdict(TrieNode, {'t': defaultdict(TrieNode', {}, 'eat')})}),
        # 'o': <__main__.TrieNode object>,
        # 'p': <__main__.TrieNode object>,
        # 'r': <__main__.TrieNode object>})

        # DFS search the board
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, trie.root, res)
        return res

    def dfs(self, i, j, board, tn, res):
        # If we found a word, append and trim the Trie
        if tn.word:
            res.append(tn.word)
            tn.word = None

        if 0 <= i < len(board) and 0 <= j < len(board[0]) \
                and board[i][j] in tn.nodes:
            c = board[i][j]
            board[i][j] = '#'
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.dfs(i + x, j + y, board, tn.nodes[c], res)
            board[i][j] = c
