class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.use_dp(s)

    def use_dp(self, s):
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res

    def use_stack(self, s):
        """
            We found all the matching indexes, then choose the maximum continuous one.
        For example, given s = ")(()())", the matching indexes are:
        s = ") ( ( ) ( ) )"
             0 1 2 3 4 5 6
        1. index 2 and 3
        2. index 4 and 5
        3. index 1 and 6
        The answer array is: [2, 3, 4, 5, 1, 6], the maxium continuous sequence is [1, 2, 3, 4, 5, 6]
        So the answer is 6.
        Time complexity: O(NlogN), need to sort
        Space complexity: O(N)
        """
        if not s: return 0
        res, stack = [], []
        for i in range(len(s)):
            if stack and s[i] == ')':
                res.append(stack.pop())
                res.append(i)
            if s[i] == '(':
                stack.append(i)
        res.sort()
        i = ans = 0
        while i < len(res):
            j = i
            while j < len(res) - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans

    def use_stack_optimized(self, s):
        """
            stack[-1] always store the start index of the longest sequence
)(()())
i = 0, s[i] = ), pop, stack=[]
i = 0, s[i] = ), append, stack=[0]
i = 1, s[i] = (, append, stack=[0, 1]
i = 2, s[i] = (, append, stack=[0, 1, 2]
i = 3, s[i] = ), pop, stack=[0, 1]
i = 3, res = 0
i = 4, s[i] = (, append, stack=[0, 1, 4]
i = 5, s[i] = ), pop, stack=[0, 1]
i = 5, res = 2
i = 6, s[i] = ), pop, stack=[0]
i = 6, res = 4
6
        """
        if not s: return 0
        res, stack = 0, [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res