"""
My gitbook analysis
  - https://app.gitbook.com/@tonylixu/s/leetcode/dynamic-programming/dynamic-programming/300-1.-longest-increasing-subsequence
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.dp(nums)

    def dp(self, nums):
        if not nums: return 0
        # dp array to store longest increasing subsequence at index i
        # Notice that we initialize arry with 1, an element itself is a
        # subsequence
        length = len(nums)
        dp = [1] * len(nums)
        for i in range(length):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
