"""
My gitbook:
  - https://app.gitbook.com/@tonylixu/s/leetcode/dynamic-programming/sorting/1122-1.-relative-sort-array
"""


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return self.use_counter(arr1, arr2)

    def count_sort(self, arr1, arr2):
        """
        Time complexity: O(N)
        Space complexity: O(N)
        """
        ans, arr = [], [0] * 1001
        # Save the count of arr1 element in arr
        for i in range(len(arr1)): arr[arr1[i]] += 1
        # Iterate arr2 and insert element
        for v in arr2:
            if arr[v] > 0: ans.extend(v for x in range(arr[v]))
            arr[v] = 0
        # Add the rest of arr1
        for i in range(len(arr)):
            if arr[i] > 0: ans.extend(i for x in range(arr[i]))
            arr[i] = 0
        return ans

    def simplified_count_sort(self, arr1, arr2):
        """
        Time complexity: O(N)
        Space complexity: O(N), extra array and dict
        """
        ans, bins = [], [0] * 1001
        for i in arr1: bins[i] += 1
        for i in arr2:
            ans += [i] * bins[i]
            bins[i] = 0
        for i in range(len(bins)): ans += [i] * bins[i]
        return ans

    def use_counter(self, arr1, arr2):
        """
        Time complexity: O(N)
        Space complexity: O(N), extra array and dict
        """
        import collections
        ans = []
        count_d = collections.Counter(arr1)
        # Insert element into ans based on arr2
        for v in arr2:
            ans += [v] * count_d[v]
            del count_d[v]
        ans += sorted(list(count_d.elements()))
        return ans

    def use_lambda(self, arr1, arr2):
        return sorted(arr1, key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))
