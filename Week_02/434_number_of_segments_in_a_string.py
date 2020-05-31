def counter_method(s):
    """Convert s into a word list, then count the number of words
    Edge case: s = '', or s = '       '

    Time complexity: O(N)
    Space complexity: O(N+1) = O(N)
    """
    if not s:
        return 0
    count = 0
    for w in s.split(' '):
        if w: count += 1
    return count


def regex_method(s):
    """Use regex and filter
    1. Use regex remove duplicates ' '
    2. Filter out all ' '

    Time complexity: O(N)
    Space complexity: O(N+1) = O(N)
    """
    import re
    s = re.sub(r' +', ' ', s).split(' ')
    return len(list(filter(None, s)))


class Solution:
    def countSegments(self, s: str) -> int:
        return regex_method(s)
