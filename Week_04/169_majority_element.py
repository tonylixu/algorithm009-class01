# Clarification:
#   - No majority element?
#   - Empty array?
#   - Max array length?
#   - All int?
#
# Possible solutions:
#   - Iterate array and use hashmap to count O(N)
#   - Sort array and return mid element O(NlogN)
#   - Divide and conquer
#
# Coding
#
# Test cases:
#   - []: Error
#   - [3, 3, 3]: 3
#   - [1, 2, 3]: No majority element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.divide_and_conquer(nums)

    def sort_method(self, nums):
        return sorted(nums)[len(nums) // 2]

    def divide_and_conquer(self, nums):
        if len(nums) == 1:
            return nums[0]
        a = self.divide_and_conquer(nums[:len(nums) // 2])
        b = self.divide_and_conquer(nums[len(nums) // 2:])
        if a == b:
            return a
        return [b, a][nums.count(a) > len(nums) // 2]

    def hashmap_method(self, nums):
        L, d = len(nums) // 2, {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > L:
                return n
