"""
1. Clarification:
    - 0 <= k <= arr.length <= 10000
    - 0 <= arr[i] <= 10000
    - Empty array? Return []
    - Array with same elements? Return array[i] * k
2. Possible solutions:
    - Sort: T: O(nlogn) S:O(n)
    - MinHeap: O(nlogk) S:O(n)
"""


def sort_method(arr, k):
    if not arr:
        return []
    arr = sorted(arr)
    return arr[:k]


def heap_method(nums, k):
    import heapq
    if k == 0:
        return []
    hp = [-x for x in nums[:k]]
    heapq.heapify(hp)
    for i in range(k, len(nums)):
        if -hp[0] > nums[i]:
            heapq.heappop(hp)
            heapq.heappush(hp, -nums[i])
    return [-x for x in hp]


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return heap_method(arr, k)