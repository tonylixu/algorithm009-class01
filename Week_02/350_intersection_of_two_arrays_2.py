def two_pointers_method(nums1, nums2):
    """Use two pointers, p1 points to index 0 of nums1,
    p2 points to index 0 of nums2. Move two pointers towards
    the end of both arrays.
    1. Sort two arrays: O(nlogn)
    2. If nums1[p1] = nums2[p2], add into ans array, p1++ and p2++
    3. If nums1[p1] <= nums2[p2], p1++, else p2++
    4. Return ans

    Time complexity: O(n)
    Space complexity: O(2n) = O(n)
    """
    # Sort two arrays
    nums1.sort()
    nums2.sort()
    p1 = p2 = 0
    ans = []
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            ans.append(nums1[p1])
            p1 += 1
            p2 += 1
    return ans


def hashmap_method(nums1, nums2):
    """Use two dictionaries to hold the frequency of each list, then use
    dictionary keys to find out intersections, then save into an array

    Time complexity: O(n)
    Space complexity: O(3n) = O(n)
    """
    ans = []
    nums1_d = {}
    nums2_d = {}
    for n in nums1:
        nums1_d[n] = nums1_d.get(n, 0) + 1
    for n in nums2:
        nums2_d[n] = nums2_d.get(n, 0) + 1
    keys = nums1_d.keys()
    for k in keys:
        if k in nums2_d:
            counter = min(nums1_d[k], nums2_d[k])
            ans += [k]*counter
    return ans


def collection_counter_method(nums1, nums2):
    """Similar to hashmap_method, instead use Python collections counter"""
    import collections
    nums1_collection = collections.Counter(nums1)
    nums2_collection = collections.Counter(nums2)
    ans = []
    for key in nums1_collection.keys() & nums2_collection.keys():
        ans.extend([key] * min(nums1_collection[key], nums2_collection[key]))
    return ans


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return hashmap_method(nums1, nums2)