class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
            Create a new array, traverse nums and append elment i and i+2.
        You only need to go through half of the array.

        Time complexity: O(N/2) = O(N)
        Space complexity: O(N)
        """
        ans = []
        for i in range(len(nums)//2):
            ans.append(nums[i])
            ans.append(nums[i+n])
            # Or you can use extend
            ans.extend([nums[i], nums[i + n]])
        return ans
