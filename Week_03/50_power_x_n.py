class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
            total = x^n is equivalent to total = x^(2/n); total * total
        Time complexity: O(logN)
        Space complexity: O(1)
        """
        def split_pow(x, n):
            if n == 0:
                return 1
            half = split_pow(x, n>>1)
            return half * half * x if n & 1 else half * half
        total = split_pow(x, abs(n))
        return 1/total if n < 0 else total
