from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        tn = self.root
        for c in word:
            tn = tn.nodes[c]
        tn.word = word


# import json
# import pprint
# words = ["oath", "pea", "eat", "rain"]
# trie = Trie()
# for w in words:
#     trie.insert(w)
#
# pprint.pprint(trie.root.nodes)
# pprint.pprint(trie.root.nodes['e'].nodes)
# pprint.pprint(trie.root.nodes['e'].nodes['a'].nodes)
# pprint.pprint(trie.root.nodes['e'].nodes['a'].nodes['t'].nodes)
# pprint.pprint(trie.root.nodes['e'].nodes['a'].nodes['t'].word)

def brute_force(n):
    ans = []
    stack = [('(', 1, 0)]
    while stack:
        v, l, r = stack.pop()
        if l > n or r > n:
            continue
        if l == r:
            ans.append(v)
        stack.append((v + '(', l + 1, r))
        stack.append((v + ')', l, r + 1))
    return ans

n = 3
print(brute_force(n))