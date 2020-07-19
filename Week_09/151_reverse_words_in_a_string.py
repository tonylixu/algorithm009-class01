"""
My gitbook analysis:
  - https://app.gitbook.com/@tonylixu/s/leetcode/dynamic-programming/strings/151-1.-reverse-words-in-a-string
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return self.use_recursive(s)

    def use_split(self, s):
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
        return ' '.join(s.split()[::-1])

    def use_regex(self, s):
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
        import re
        result = reversed(list(filter(None, re.split(r'\s+', s))))
        return ' '.join(result)

    def use_recursive(self, s):
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """

        def helper(a, ans):
            if len(a) <= 0: return ''
            return a[len(a) - 1] + ' ' + helper(a[:len(a) - 1], ans)

        return helper(s.split(), '').strip()
