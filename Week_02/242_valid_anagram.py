def sort_method(s, t):
    """Sort two strings first, then compare. Very baoli

    Time complexity: O(nlog) --> sorting
    Space complexity: O(n)
    """
    return sorted(s) == sorted(t)


def one_hashmap_method(s, t):
    """Use hashmap, key is the element and value is element occurrance
    For example, for s = "anagram", the hashmap will look like: { 'a': 3, 'n': 1, 'g': 1, 'm': 1, 'r': 1},

    1. Construct hashmap by iterate through s, for element a, count++
    2. Update hashmap by iterate through t, for element a, count++
    3. If s and t are anagram, the hashmap will be empty

    Time complexity: O(n)
    Space complexity: O(n)

    """
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    for c in t:
        if c in d:
            d[c] -= 1
        else:
            return False
    for v in d.values():
        if v != 0:
            return False
    return True


def two_hashmap_method(s, t):
    """Use hashmap, key is the element and value is element occurrance
    For example, for s = "anagram", the hashmap will look like: { 'a': 3, 'n': 1, 'g': 1, 'm': 1, 'r': 1},

    1. Construct hashmap by iterate through s
    2. Construct hashmap by iterate through t
    3. Compare two hashmaps

    Time complexity: O(n)
    Space complexity: O(n)

    """
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        t_dict[t[i]] = t_dict.get(t[i], 0) + 1
    return s_dict == t_dict


def set_method(s, t):
    """Use set, since set is a type of hashtable in Python, if s and t are anagrams,
    Their elements order in set should identical. Then we compare the element counts.

    1. Convert s and t to set, then compare
    2. If #1 is true, we compare the element counts

    Time complexity: O(n)
    Space complexity: O(n)
    """
    temp_set = set(s)
    if temp_set == set(t):
        # Count element
        for c in temp_set:
            if s.count(c) != t.count(c):
                return False
    else:
        return False
    return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return one_hashmap_method(s, t)