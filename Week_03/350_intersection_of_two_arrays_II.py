class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.collection_method(nums1, nums2)

    def collection_method(self, nums1, nums2):
        """
            Similar to hashmap_method, but use collection.Counter and with dynamic
        optimization.

        We only counter the larger list, then use smaller list element as key, to
        check if larger[k] exists, if it does, reduce the larger[k] count by 1, and
        append the k into answers.
        Time complexity: O(M), M is the smaller length of nums1 and nums2
        Space complexity: O(N), one counter is needed to hold key value pair.
        """
        if not nums1 or not nums2:
            return []
        from collections import Counter
        ans = []

        if len(nums1) >= len(nums2):
            larger, smaller = Counter(nums1), nums2
        else:
            larger, smaller = Counter(nums2), nums1
        for k in smaller:
            if larger.get(k, 0) > 0:
                larger[k] -= 1
                ans.append(k)
        return ans

    def hashmap_method(self, nums1, nums2):
        """
            Two hashmap method, build {index: frequence} hashmap for nums1 and nums2,
        then iterate nums1/nums2 keys, if key is in both dicts, add k*min_frequency
        into answers.

        Time complexity: O(N)
        Space complextity: O(2N) = O(N)
        """
        ans, nums1_d, nums2_d = [], {}, {}
        for n in nums1:
            nums1_d[n] = nums1_d.get(n, 0) + 1
        for n in nums2:
            nums2_d[n] = nums2_d.get(n, 0) + 1
        for k in nums1_d:
            if k in nums2_d:
                ans += [k] * min(nums1_d[k], nums2_d[k])
        return ans
