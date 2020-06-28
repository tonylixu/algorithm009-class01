class Solution:
    def numDecodings(self, s: str) -> int:
        return self.dp_solution(s)

    def dp_solution(self, s):
        """
        Define status:
          - dp[i]: How many decodings for s[i]
        The number of decodings for dp[i] can come from dp[i-1] or dp[i-2], for example:
        '2 2 6'
        when i = 2, i - 1 = 1, i - 2 = 0
        dp[2] = dp[1] + dp[0] (condition: s[i] and s[i-1] and have a valid encoding)
        so we have:
        f[n] = f[n-1] + (10 <= a[n-2:] <=26) ? f[n-2]:0

        Time complexity: O(N)
        Space complexity: O(N)
        """
        if s[0] == '0': return 0
        L = len(s)
        dp = [0] * (L + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, L + 1):
            # Case '226': only has one decoding(B, Z)
            dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]
            t = int(s[i - 2:i])
            if t >= 10 and t <= 26:
                dp[i] += dp[i - 2]
        return dp[L]