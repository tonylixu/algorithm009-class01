from doctest import testmod


def find_unsorted_point(nums):
    """
    Give a half sorted array, use binary search to find the starting point of unsorted array.

    For example: For nums = [4, 5, 6, 7, 0, 1, 2]
    The unsorted point is 7, index = 3
    Time complexity: O(logn)
    Space complexity: O(1)

    >>> nums = [4, 5, 6, 7, 0, 1, 2]
    >>> find_unsorted_point(nums)
    3
    >>> nums = [6, 0, 1, 2, 3, 4, 5]
    >>> find_unsorted_point(nums)
    0
    >>> nums = [0, 1, 2, 3, 4, 5]
    >>> find_unsorted_point(nums)
    0
    """
    # Define left and right and mid
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Not necessary for Python since Python3 has no integer length limitation
        if nums[mid] > nums[mid+1]:
            return mid
        else:
            right = mid - 1
    return 0


if __name__ == '__main__':
    #testmod(verbose=True)
    nums = [4, 5, 6, 7, 0, 1, 2]
    print(nums)
    position = find_unsorted_point(nums)
    nums[:] = nums[position+1:] + nums[:position+1]
    print(nums)