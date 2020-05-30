def method_one(nums):
    # Time complexity: O(n)
    # Space complexity: n
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
        j += 1
    return nums


def method_two(nums):
    # Time complexity: O(n^2)
    # Space complexity: n
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i + 1, len(nums)):
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
    return nums


def method_three(nums):
    # Time complexity: O(n)
    # Space complexity: n
    for n in nums:
        if n == 0:
            nums.remove(0)
            nums.append(0)
    return nums


def method_four(nums):
    # Time complexity: O(n)
    # Space complexity: n
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    while j < len(nums):
        nums[j] = 0
        j += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
