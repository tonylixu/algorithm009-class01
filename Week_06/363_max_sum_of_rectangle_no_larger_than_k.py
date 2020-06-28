"""
Leetcode good solutions:
  - https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/javacong-bao-li-kai-shi-you-hua-pei-tu-pei-zhu-shi/
  - https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/gu-ding-zuo-you-bian-jie-qian-zhui-he-er-fen-by-po/
"""

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        return self.bisect_solution(matrix, k)

    def bisect_solution(self, matrix, k):
        """
            We use left and right bars, left bar start from 0, right bar start from left,
        Then we use a row_sum array to store each columns' sum. Then for a give left bar, we
        iterate right bar from [left, len(matrix[0])), the area of any rectanle between left bar
        and righr bar, is stored in row_sum.
        """
        m, n, ans = len(matrix), len(matrix[0]), float('-inf')
        for left in range(n):
            # Calculate sum of each row
            row_sum = [0] * m
            for right in range(left, n):
                for j in range(m):
                    row_sum[j] += matrix[j][right]
                # Calculate sub rectangle in [left, right]
                cur, arr = 0, [0]
                for t in row_sum:
                    cur += t
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr): ans = max(cur - arr[loc], ans)
                    bisect.insort(arr, cur)
        return ans
