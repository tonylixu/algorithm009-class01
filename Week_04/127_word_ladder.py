class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return self.bfs(beginWord, endWord, wordList)

    def bfs(self, beginWord, endWord, wordList):
        """
        1. classification:
            - If not beginWord/endWord/wordList and endWord not in wordList
            - All words same length?
            - All words lower case?
            - Any duplications?
            - What if beginWord and endWord the same? Return 0
            - Any empty strings in wordList?
        2. Possible solutions:
            - BFS to find shortest path
            - ?
        3. Coding
        4. Test cases

        Analysis: Since one letter can be changed at a time, if we start from "hit",
        we can only change to those words which has exactly one letter different from it.
        Putting in graph-theoretic terms, "hot" is a neighbor of "hit". The idea is simply
        to start from the "beginWord", then visit its neighbors, then the non-visisted
        neighbors of its neighbours until we arrive at the "endWord".

        Imagine the following graph:

        hit - hot   dog - log
               |  /  |  /  |
              dot   cog   lot

        To help we found word more efficiently, we also built a "all_combo_dict" to help.

        Time complexity: O(NxM), M is the length of the word, and N is the number of words.
        Space complexity: O(NxM), need to hold N words in helper dict.
        """
        from collections import defaultdict

        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0

        # Since all the words are the same length
        L = len(endWord)

        # Hashmap to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        #
        # {
        #     '*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'],
        #     'ho*': ['hot'], 'd*t': ['dot'], 'do*': ['dot', 'dog'],
        # }
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # BFS queue
        queue = [(beginWord, 1)]
        # Visisted to make sure we don't repeat processing same word
        visited = set()
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                # Define intermediate wrod i.e. h*t
                inter_word = current_word[:i] + '*' + current_word[i + 1:]

                # Check values in all_combo_dict
                for word in all_combo_dict[inter_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0