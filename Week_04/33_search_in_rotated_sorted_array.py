class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.direct_binary_search(nums, target)

    def direct_binary_search(self, nums, target):
        """
            No rotated:
            1 2 3 4 5 6 7
                 mid

            left rotated: pivot at the left side of the origin sorted array, A[mid] >= A[left]
            3 4 5 6 7 1 2
                 mid
            search in A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side

            right rotated: pivot at the right side of the origin sorted array, A[mid] < A[left]
            6 7 1 2 3 4 5
                 mid
            search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # left rotated
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right rotated
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def baoli_search(self, nums, target):
        """
            Time complexity: O(N)
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def indirect_binary_search(self, nums, target):
        # First binary search to sort array in O(longN)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                pivot = mid
                break
            else:
                right = mid - 1
        # Reorder nums
        nums[:] = nums[mid + 1:] + nums[:mid + 1]
        print(nums)
