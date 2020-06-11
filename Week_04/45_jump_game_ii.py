class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = steps = end = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, nums[i] + i)
            if i == end:
                end,  steps = max_reach, steps + 1
                if end >= len(nums):
                    break
        return steps