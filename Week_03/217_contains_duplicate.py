class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return self.set_method(nums)

    def set_method(self, nums):
        """
        Use Python set(), to uniq all ekements of nums. Then compare the length
        of set and length of nums.
        1. If len(set) = len(nums): return False
        2. If len(set) != len(nums): return True

        Time complexity: O(N)
        Space complexity: O(N) (N is the number of elements)
        """
        return len(set(nums)) != len(nums)

    def hash_counter_method(self, nums):
        """
        Build a hashmap for nums, key is the element and value is the frequency:
        For example,
        for nums = [1,2,3,1],
        the hashmap d = {1: 2, 2: 1, 3: 1}

        Then we only need to just of any v in d.values() > 1

        Time complexity: O(N)
        Space complexity: O(2N) = O(N) - We need addition dict to hold k,v
        """
        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 1
        return False
