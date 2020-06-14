"""
Leetcode good solution:
https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        self.backtracking(nums, visited, [], ans)
        return ans

    def dfs(self, nums, subset, ans):
        """
            For N numbers, we habe N! permutations. For example, given [1, 2, 3]
        permutation start with 1: [1, 2, 3], [1, 3, 2]
        permutation start with 2: [2, 1, 3], [2, 3, 1]
        permutation start with 3: [3, 1, 2], [3, 2, 1]

        This is actually solving a dfs for a N-ary tree.
        []
        [1]             [2]             [3]
        [1,2] [1,3]     [2,1] [2,3]     [3,1] [3,2]
        [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]

        Each leaf node is an answer.

        Time complexity: O(NxN!)
        Space complexity: O(NxN!) = O(logN) + O(NxN!) = O(NxN!)
        """
        # Recursion terminator
        if not nums:
            ans.append(subset)
            return
        # Process current level logic, drill down
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], subset + [nums[i]], ans)

    def backtracking(self, nums, visited, subset, ans):
        if len(subset) == len(nums):
            ans.append(subset)
            return
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(nums, visited, subset + [nums[i]], ans)
                visited.remove(i)
