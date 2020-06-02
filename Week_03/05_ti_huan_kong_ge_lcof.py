def regex_method(s):
    """
    Use regex sub

    :param s: String to process
    :return: Processed string

    Time complexity: O(2^M+N) = O(N). M is the size of the regex (To build a deterministic finite automaton)
    Space complexity: O(1)
    """
    import re
    return re.sub(r' ', '%20', s)


def iterative_method(s):
    """
    Use regex sub

    :param s: String to process
    :return: Processed string
    
    Time complexity: O(N)
    Space complexity: O(1)
    """
    res = ''
    for c in s:
        if c == ' ':
            c = '20%'
        res += c
    return res


def split_method(s):
    """
    Use split function

    :param s: String to process
    :return: Processed string

    Time complexity: O(N)
    Space complexity: O(1)
    """
    return '%20'.join(s.split(' '))


class Solution:
    def replaceSpace(self, s: str) -> str:
        return split_method(s)
