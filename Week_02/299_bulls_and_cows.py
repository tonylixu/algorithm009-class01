def hash_map_of_str_and_int(secret, guess):
    """The idea is to use a hashmap of the following format
    count = {'0':[i, j], '1':[i, j]...}
    key range is from 0~9
    i: number of occurrance in secret
    j: number of occurrance in guess
    The purpose of the hashmap is to store cow type guesses

        We iterate the secret and guess at the same time, construct the hashmap,
    at the end of hashmap, we calculate the sum of cow guesses. The bull guess will be
    calculated in the hashmap construction on the fly

    Time complexity: O(n)
    Space complexity: O(n)
    """
    count = {str(i): [0, 0] for i in range(10)}
    bulls = cows = 0
    for i in range(len(secret)):
        vs, vg = secret[i], guess[i]
        if vs == vg:
            bulls += 1
        else:
            count[vs][0] += 1
            count[vg][1] += 1
    cows = sum(min(count[i][0], count[i][1]) for i in count)
    return f'{bulls}A{cows}B'


def counter_solution(secret, guess):
    """User collections counter
    Less recommended since implementation details are hidden
    Suppose s = ['1', '2', '3'] and g = ['0', '1', '1']
    Counter(s) = Counter({'1': 1, '2': 1, '3': 1})
    Counter(g) = Counter({'1': 2, '0': 1})
    and
    Counter(s)&Counter(g) = Counter({'1': 1})

    Time complexity: O(n)
    Space complexity: O(n)
    """
    from collections import Counter
    s_list, g_list, i = list(secret), list(guess), 0
    while i < len(s_list):
        if g_list[i] == s_list[i]:
            del g_list[i], s_list[i]
            i -= 1
        i += 1
    return (f'{len(secret) - len(s_list)}A'
            f'{sum((Counter(s_list) & Counter(g_list)).values())}B')


def counter_solution2(s, g):
    """Iterate through s and g once, calculate bulls
    Then use Counter to build a frequence hashmap for both s and g, for example:
    s = '1123'
    g = '0111'
    counter_s = {'1': 2, '2': 1, '3': 1}
    counter_g = {'0': 1, '1': 3}
    Then we only consider the common key of two dicts, and for each key, the minimum value of two key's value
    will be the cow
    Since we already count the bulls, so we need to substract nulls from the cows

    Time complexity: O(n)
    Space complexity: O(3n) = O(n)
    """
    from collections import Counter
    bulls = cows = 0
    # Calculate bulls first
    for i in range(len(s)):
        if s[i] == g[i]:
            bulls += 1
    counter_s = dict(Counter(s))
    counter_g = dict(Counter(g))
    for key in counter_s:
        if key in counter_g:
            cows += min(counter_s[key], counter_g[key])
    cows -= bulls
    return (f'{bulls}A{cows}B')


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        return counter_solution2(secret, guess)
