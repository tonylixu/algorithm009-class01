from collections import defaultdict


def ladderLength(beginWord, endWord, wordList):
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
    #     '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'],
    #     'l*t': ['lot'], 'lo*': ['lot', 'log'], 'l*g': ['log'],
    #     'c*g': ['cog'], 'co*': ['cog']
    # }

    for w in wordList:
        for i in range(L):
            # Key is the generic word
            # Value is a list of words which have the same intermediate generic word
            all_combo_dict[w[:i] + '*' + w[i + 1:]].append(w)

    # Queue for BFS
    queue = [(beginWord, 1)]
    # Visited to make sure we don't repeat processing same word
    visited = {beginWord: True}
    while queue:
        current_word, level = queue.pop(0)
        for i in range(L):
            # Intermediate words for current word
            inter_word = current_word[:i] + '*' + current_word[i+1:]

            # Next states are all the words which share the same intermediate state
            for word in all_combo_dict[inter_word]:
                # If at any point if we find what we are looking for
                # i.e. The end word we are looking for
                if word == endWord:
                    return level + 1
                # Otherwise, add it to the BFS queue, and mark it visited
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            all_combo_dict[inter_word] = []
    return 0


b = "hit"
e = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]

ladderLength(b, e, w)

