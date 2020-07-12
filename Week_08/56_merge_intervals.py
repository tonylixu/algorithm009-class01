class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.use_sort(intervals)

    def use_sort(self, intervals):
        if not intervals: return []
        res = []

        # Sort the intervals by x[0]
        intervals.sort(key=lambda x: x[0])
        for inter in intervals:
            # Second element of the last element of result set is less than
            # the left element of the new set
            if len(res) == 0 or res[-1][1] < inter[0]:
                res.append(inter)
            else:
                res[-1][1] = max(res[-1][1], inter[1])
        return res
