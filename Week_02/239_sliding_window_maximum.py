"""
Analysis:
1. 1 <= nums.length <= 10^5
2. -10^4 <= nums[i] <= 10^4
3. 1 <= k <= nums.length

Possible solutions:
1. Baoli
2. heap
3. deque
"""


def baoli_method(nums, k):
    """Iterate the entire nums list, and use a temp list to keep k elements (window),
    from i->i+k, find the max element and add it to result list

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    ans = []
    # Iterate nums
    for i in range(len(nums)-k+1):
        window = nums[i:i+k]
        ans.append(max(window))
    return ans


def heapq_baoli_method(nums, k):
    """Use heap, for each window, we add the window into heap O(logN), and return
    the largest element O(1).

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    import heapq
    ans = []
    for i in range(len(nums)-k+1):
        window = nums[i:i + k]
        heapq.heapify(window)
        a = heapq.nlargest(1, window)
        ans.append(a[0])
    return ans


def deque_method(nums, k):
    from collections import deque
    # Handle edge case
    if len(nums) * k == 0:
        return []
    if k == 1:
        return nums

    def clean_deque(m):
        # Remove indexes of elements not from sliding window
        if deq and deq[0] == m-k:
            deq.popleft()

        # Remove from deq indexes of all elements
        # which are smaller than current element nums[i]
        while deq and nums[m] > nums[deq[-1]]:
            deq.pop()

    # Initialize deque and output
    deq = deque()
    max_idx = 0
    for i in range(k):
        clean_deque(i)
        deq.append(i)
        # Compute max in nums[:k]
        if nums[i] > nums[max_idx]:
            max_idx = i
    output = [nums[max_idx]]

    # build output
    for i in range(k, len(nums)):
        clean_deque(i)
        deq.append(i)
        output.append(nums[deq[0]])
    return output


def deque2_method(nums, k):
    """Use deque from collections, this deque has the following characters:
        1. deque[0] always keep the index of the max element. As we moving the window, whenever we find a new
            element is larger than window[-1], we pop window[-1] out, and continue poping, this is how we keep
            deque[0] always has the max value index
        2. We need to consider one edge case, which is that the lest most element of the sliding window is the
        largest element of the rest of the list. For example:
            nums = [1, 2, 7, 5, 6, 4], k = 2
        when windows gets to [7, 5], the largest element is 7, deque = [2, 3], we add 7 to result
        now when we go to next element 6, the window will become [7,6] instead of [5, 6], we will continue
        to add 7, (i=4)
        When this will happen? This happens when i-k = window[0], which is 4-2 = 2, and window[0] = 2.
        So when this happens, we need to pop left.

    Time complexity: O(N)
    Space complexity: O(N) = deque(O(k) + res(O(N-k+1))
    """
    from collections import deque
    size = len(nums)
    if size == 0:
        return []
    if k == 1:
        return nums
    results = []
    window = deque()

    print(nums)
    for i in range(size):
        # i >= k is when the left most element starting to slide out
        # i-k == window[0] means the leftmost element in windows is the largest
        print(f'=====================')
        print(f'i = {i}, k = {k}, i-k = {i-k}, window={window}')
        print(f'window_value = {[nums[k] for k in window]}')
        if i >= k and i - k == window[0]:
            print(f'i = {i}, k = {k}, i-k = {i - k}, window={window}, we popleft')
            window.popleft()
            print(f'After popleft, window = {window}')

        # If window is not empty，and new element is large than all the numbers in deque
        # We can pop out all the existing elements
        while window and nums[window[-1]] <= nums[i]:
            print(f'i = {i}, k = {k}, new element = {nums[i]}, window = {window}'
                 f' nums[window[-1]] = {nums[window[-1]]}, we keep poping')
            window.pop()
            print(f'After pop, window = {window}')
        print(f'i = {i}, k = {k}, window={window}, we add')
        window.append(i)
        print(f'After add, window={window}')
        print(f'window_value = {[nums[k] for k in window]}')
        # The head of deque is the max element index
        if i >= k - 1:
            results.append(nums[window[0]])
    return results


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         return deque2_method(nums, k)

#nums = [1, 3, -1, -3, 5, 3, 6, 7]
nums = [1, 2, 7, 5, 6, 4]
k = 2
print(deque2_method(nums, k))