"""
Problem description:
https://leetcode.com/problems/word-ladder-ii/

Solutions:

Analysis: Since one letter can be changed at a time, if we start from "hit",
we can only change to those words which has exactly one letter different from it.
Putting in graph-theoretic terms, "hot" is a neighbor of "hit". The idea is simply
to start from the "beginWord", then visit its neighbors, then the non-visisted
neighbors of its neighbours until we arrive at the "endWord".

    Imagine the following graph:

    hit - hot   dog - log
           |  /  |  /  |
          dot   cog   lot

Basic idea:
1. Start from beginWord, we go through wordList one letter at a time. Skip the visited word
2. We use and (list) to store final answers, final answers are [[answer1], [answer2]] format.
    - [answer1] = [hit, hot, ...cog]
    - [answer2] = [hit, hot, ...cog]
3. We use a hashmap to build answers dynamic as we go through wordList.
"""


def solution_one(begin_word, end_word, word_list):
    """
    Simple solution, no optimization, just to find all the paths

    Time limit exceed
    Time complexity: O(N^2*M*k) = O(MN^2) = O(N^3), M is the length of word, k is the char_set length
    Time complexity: O(N)
    """
    from collections import defaultdict
    # Edge case
    if end_word not in word_list:
        return []
    # Setups
    char_set = 'abcdefghijklmnopqrstuvwxyz'
    ans, level_d, visited = [], {}, set()
    level_d[begin_word] = [[begin_word]]
    while level_d:
        new_level_d = defaultdict(list)
        for word in level_d:
            if word not in visited:
                visited.add(word)
                if word == end_word:
                    return level_d[word]
                else:
                    for i in range(len(word)):
                        for c in char_set:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in word_list:
                                new_level_d[new_word] += [w + [new_word] for w in level_d[word]]
        level_d = new_level_d
    return ans


def solution_two(begin_word, end_word, word_list):
    """
    Simple solution, no optimization, just to find all the paths

    500 ms
    Time complexity: O(N^2)
    Time complexity: O(N)
    """
    from collections import defaultdict
    # Edge case
    if end_word not in word_list:
        return []
    # Optimization
    char_set = ''
    for c in ''.join(word_list):
        if c not in char_set:
            char_set += c
    word_list = set(word_list)
    ans, level_d, visited = [], {}, set()
    level_d[begin_word] = [[begin_word]]
    while level_d:
        new_level_d = defaultdict(list)
        for word in level_d:
            if word not in visited:
                visited.add(word)
                if word == end_word:
                    return level_d[word]
                else:
                    for i in range(len(word)):
                        for c in char_set:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in word_list:
                                new_level_d[new_word] += [w + [new_word] for w in level_d[word]]
        word_list -= set(new_level_d.keys())
        level_d = new_level_d
    return ans


def solution_three(begin_word, end_word, word_list):
    """
    Most optimized solution

    150 ms
    Time complexity: O(N^2)
    Time complexity: O(N)
    """
    from collections import defaultdict
    # Edge case
    if end_word not in word_list:
        return []
    # Optimization
    L = len(begin_word)
    all_combo_dict = defaultdict(set)
    word_list += [begin_word]
    for i in range(L):
        for word in word_list:
            all_combo_dict[word[:i] + '*' + word[i+1:]].add(word)

    graph = defaultdict(list)
    for words in all_combo_dict.values():
        words = list(words)
        for i in range(len(words)):
            graph[words[i]].extend(words[:i] + words[i+1:])

    word_list = set(word_list)
    ans, level_d, visited = [], {}, set()
    level_d[begin_word] = [[begin_word]]
    while level_d:
        new_level_d = defaultdict(list)
        for word in level_d:
            if word not in visited:
                visited.add(word)
                if word == end_word:
                    return level_d[word]
                for new_word in graph[word]:
                    if new_word in word_list:
                        new_level_d[new_word] += [w + [new_word] for w in level_d[word]]
        word_list -= set(new_level_d.keys())
        level_d = new_level_d
    return ans


if __name__ == '__main__':
    b = "hit"
    e = "cog"
    w = ["hot", "dot", "dog", "lot", "log", "cog"]
    ans = solution_three(b, e, w)
    print(ans)