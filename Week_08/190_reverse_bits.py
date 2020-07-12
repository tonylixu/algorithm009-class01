"""
My gitbook:
  - https://app.gitbook.com/@tonylixu/s/leetcode/dynamic-programming/bit-operations/190-1.-reverse-bits
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        return self.bit_move(n)

    def bit_move(self, n):
        """
        Time complexity: O(32) = O(1)
        Space complexity: O(1)
        """
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans

    def bit_move2(self, n):
        """
        Time complexity: O(32) = O(1)
        Space complexity: O(1)
        """
        ans = 0
        for i in range(32):
            ans += (n & 1) << (31 - i)
            n >>= 1
        return ans

    def use_int(self, n):
        """
        Time complexity: O(N)
        Space complexity: O(32) = O(1)
        """
        bit_str = '{0:032b}'.format(n)
        return int(bit_str[::-1], base=2)

    def use_int2(self, n):
        """
        Time complexity: O(N)
        Space complexity: O(32) = O(1)
        """
        b = bin(n)[:1:-1]
        return int(b + '0' * (32 - len(b)), 2)