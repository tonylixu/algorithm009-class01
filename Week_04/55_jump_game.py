"""
Leetcode: https://leetcode.com/problems/jump-game/
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.greedy(nums)

    def greedy(self, nums):
        """
            Greedy method, form reversed order.
        max reach from poistion i is nums[i] + i

        Time complexity: O(N)
        Space complexity: O(1)
        """
        if not nums: return False
        L = len(nums)
        end = L - 1
        for i in range(L - 2, -1, -1):
            if nums[i] + i >= end:
                end = i
        return end == 0

    def calculate_max(self, nums):
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True