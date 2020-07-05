"""
My Gitbook:
https://app.gitbook.com/@tonylixu/s/leetcode/dynamic-programming/127-1.-word-ladder
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return self.bi_bfs(beginWord, endWord, wordList)

    def bi_bfs(self, beginWord, endWord, wordList):
        import string
        # Edge case
        if endWord not in wordList: return 0

        dist = 1  # The distance
        front, back = {beginWord}, {endWord}
        wordList, L = set(wordList), len(beginWord)

        # Bi-BFS starts here, front is always the small set
        while front:
            dist += 1
            next_front = set()

            # Go through all the words in front set
            for word in front:
                for i in range(L):
                    for c in string.ascii_lowercase:  # 'a' --> 'z'
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            # next_front is ready
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return 0

    def bfs_one(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        # Build the helper dict
        L = len(beginWord)
        wordList += [beginWord]
        from collections import defaultdict
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # Build graph
        graph = defaultdict(list)
        for words in all_combo_dict.values():
            for i in range(len(words)):
                graph[words[i]].extend(words[:i] + words[i + 1:])

        ans, visited, queue = [], set(), []
        queue.append((beginWord, 1))
        while queue:
            curr_word, level = queue.pop(0)
            for word in graph[curr_word]:
                if word == endWord:
                    return level + 1
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level + 1))
        return 0

    def bfs_two(self, beginWord, endWord, wordList):
        from collections import defaultdict
        if endWord not in wordList:
            return 0

        # Since all the words are of same length
        L = len(beginWord)

        # Build dictionary to hold combination of words that can be formed
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # BFS queue
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            curr_word, level = queue.pop(0)
            for i in range(L):
                # Build intermedite word
                inter_word = curr_word[:i] + '*' + curr_word[i + 1:]

                # Next states are all the words which share the same intermediate word
                for word in all_combo_dict[inter_word]:
                    # If we find the endWord
                    if word == endWord:
                        return level + 1
                    # Otherwise add to the queue, and mark it visited
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[inter_word] = []
        return 0

    def bfs_three(self, beginWord, endWord, wordList):
        from collections import defaultdict
        if endWord not in wordList:
            return 0

        # Since all the words are of same length
        L = len(beginWord)

        # Build dictionary to hold combination of words that can be formed
        wordList += [beginWord]
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # Build graph for further optimization
        graph = defaultdict(list)
        for words in all_combo_dict.values():
            for i in range(len(words)):
                graph[words[i]].extend(words[:i] + words[i + 1:])

        # BFS queue
        queue = [(beginWord, 1)]
        visited = set()
        while queue:
            curr_word, level = queue.pop(0)
            for word in graph[curr_word]:
                # If we find the endWord
                if word == endWord:
                    return level + 1
                # Otherwise add to the queue, and mark it visited
                if word not in visited:
                    visited.add(word)
                    queue.append((word, level + 1))
        return 0
