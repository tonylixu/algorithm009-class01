"""
My personal Gitbook:
https://app.gitbook.com/@tonylixu/s/leetcode/dynamic-programming/bit-operations/191-2.-number-of-1-bits
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.use_mod(n)

    def use_bin(self, n):
        return bin(n).count('1')

    def use_mod(self, n):
        """
        Time complexity: O(logn)
        Space complexity: O(1)
        """
        count = 0
        while n > 0:
            if n % 2 == 1: count += 1
            n >>= 1
        return count

    def use_loop(self, n):
        """
        Time complexity: O(32) = O(1)
        Space complexity: O(1)
        """
        mask, count = 1, 0
        for i in range(32):
            if n & mask != 0:
                count += 1
            mask <<= 1
        return count

    def use_and(self, n):
        """
        Time complexity: O(1)
        Space complexity: O(1)
        """
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count