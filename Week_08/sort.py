# Ref: https://www.cnblogs.com/onepixel/p/7674659.html
arr = [9, 10, 100, 4, 6, 5, 2, 1, 0]


def bubble_sort(arr):
    """
        Use two layer loops, for each a[i], iterate from a[j:len(a) - i - 1] (i, j start from 0). If a[j] > a[j+1], swap
    two elements.
    Steps:
        - Compare a[j] and a[j + 1], swap if a[j] > a[j + 1]
        - Repeat for all js
        - Repeat for all is
    Time complexity: O(N^2)
    Space complexity: O(1)
    """
    if len(arr) == 1: return arr
    for i in range(len(arr)):
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """
        Find the min(max) element, store it to the sorted array, and repeat this process for the rest of
    elements, and store it to the  sorted array

    Steps:
        - Outer Loop given arr , index i, range(0, len(arr) - 1)
            - Inner loop given arr, index j, range(i + 1, len(arr))
                - Find the min element index
            - Swap arr[i] with arr[min_index
    Time complexity: O(N^2)
    Space complexity: O(1)
    """
    if len(arr) == 1: return arr
    length = len(arr)
    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:  # Search for the minnimum element
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    """
        We can split the given array into two part:
            - arr[0]: sorted
            - arr[1:]: unsorted
    We just need to go through arr[1:], and insert new element into sorted arr[0:] while keeping the order
    Time complexity: O(N^2)
    Space complexity: O(1)
    Example:
    arr = [100, 3, 2]
    i = 1, pre = 0, cur = arr[1] = 3
    arr[pre] = 100
    while pre >=0 (0) and arr[pre] (100) > cur (3):
        arr[pre+1] = arr[pre] -> arr[1] = 100 [100, 100, 2]
        pre = -1 -> pre = -1
    arr[pre + 1] = cur -> arr[0] = 3 -> arr = [3, 100, 2]

    i = 2, pre = 1, cur = arr[2] = 2
    arr[pre] = arr[1] = 100
    while pre >= 0 and arr[pre] > cur:
        arr[pre+1] = arr[pre] -> arr[2] = arr[1] -> [3, 100, 100]
        pre -= 1 -> pre = 0
    while pre >= 0 and arr[pre] (3) > cur (2):
        arr[pre+1] = arr[pre] -> arr[1] = arr[0] -> [3, 3, 100]
        pre -= 1 -> pre = -1
    arr[pre + 1] = cur -> arr[0] = 2 -> [2, 3, 100]
    """
    if len(arr) == 1: return arr
    length = len(arr)
    for i in range(1, length):    # Since arr[0] can be considered sorted already
        pre, cur = i - 1, arr[i]  # Pre element index and current element value
        while pre >= 0 and arr[pre] > cur:
            arr[pre + 1] = arr[pre]
            pre -= 1
        arr[pre + 1] = cur
    return arr


def merge_sort(arr):
    """
        Use divide and conquer method, keep splitting the given array into subarrays, until there is only one element
    in the subarray (Sorted already), then merge subarrarys back to one.
    Time complexity: O(NlogN)
    Space complexity: O(N)
    """
    def merge(arr1, arr2):
        if not arr1 or not arr2:
            return []
        ans, i, j = [], 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]: ans.append(arr1[i]); i += 1
            else: ans.append(arr2[j]); j += 1
        if i < len(arr1): ans.extend(arr1[i:])
        else: ans.extend(arr2[j:])
        return ans

    if len(arr) == 1: return arr
    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def quick_sort(arr):
    """
    Video link: https://www.youtube.com/watch?v=CB_NCoxzQnk

    Time complexity: O(NlogN)
    Space complexity: O(NlogN)
    """
    def quick_sort2(arr, low, high):
        if low < high:
            p = partition(arr, low, high)
            quick_sort2(arr, low, p - 1)
            quick_sort2(arr, p + 1, high)

    def get_pivot(arr, low, high):
        #mid = (low + high) // 2
        pivot = high
        #if arr[low] < arr[mid] < arr[high]:
        #    pivot = mid
        #elif arr[mid] < arr[low] < arr[high]:
        #    pivot = low
        return pivot

    def partition(arr, low, high):
        pivot_index = get_pivot(arr, low, high)  # Always pick the last element as pivot
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
        border = low
        for i in range(low, high + 1):
            if arr[i] < pivot_value:
                border += 1
                arr[i], arr[border] = arr[border], arr[i]
        # Switch pivot value with the border
        arr[low], arr[border] = arr[border], arr[low]
        return border
    quick_sort2(arr, 0, len(arr) - 1)


print(arr)
quick_sort(arr)
print(arr)