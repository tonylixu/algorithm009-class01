from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        """
        Initialize TrieNode
        """
        self.nodes = defaultdict(TrieNode)
        self.is_word = False


class Trie1(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into Trie
        """
        curr = self.root
        for c in word:
            curr = curr.nodes[c]
        curr.is_word = True

    def search(self, word):
        """
        Search a word in Trie
        """
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix
        """
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return True


# Simplified version
class Trie2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for c in word:
            t = t.setdefault(c, {})
        t['-'] = True

    def _search(self, word: str, is_prefix: bool = False):
        """
        Search word or prefix
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        if is_prefix:
            return True
        return '-' in t

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self._search(word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self._search(prefix, True)