"""
Leetcode good solution:
  - https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/qiang-fang-zi
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.rob_range(nums)

    def rob_range(self, nums):
        """
            Similar to "House Robber I", the only difference is that we can't rob
        the first house and the last house at the same time. So we can reuse the function
        that we defined in "House Robber I" and only need to specify the rob range.
        1. If you rob house[0], you need to skip house[-1], so your rob range is [0, len-2]
        2. If you don't rob house[0], you can rob house[-1], so your rob range is [1, len-1]
        3. Or you don't rob house[0] and house[-1], which obvisouly don't need to consider

        Time complexity: O(N)
        Space complexity: O(1)
        """

        # Dynamic function
        def dp(nums, start, end):
            dp_cur = dp_one = dp_two = 0
            for i in range(end, start - 1, -1):
                dp_cur = max(dp_one, nums[i] + dp_two)
                dp_two, dp_one = dp_one, dp_cur
            return dp_cur

        length = len(nums)
        if length == 1: return nums[0]
        return max(
            dp(nums, 0, length - 2),  # Rob first house
            dp(nums, 1, length - 1))  # Rob last house