"""
my gitbook analysis:
  - https://app.gitbook.com/@tonylixu/s/leetcode/dynamic-programming/strings/541-1.-reverse-string-ii
Clarification:
  - k is >= len(s), reverse all
  - k is positive
  - only lower case English letters
  - length of s is in [1, 10000]

Possible solutions:
  - Brute force, go through array 2k at a time
  - Recursive
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return self.recursive(s, k)

    def brute_force(self, s, k):
        length = len(s)
        if length == 0: return None
        a = list(s)
        for i in range(0, length, 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return ''.join(a)

    def recursive(self, s, k):
        def helper(s, k):
            if not s: return ''
            return s[:k][::-1] + s[k:2 * k] + helper(s[2 * k:], k)

        return '' + helper(s, k)

