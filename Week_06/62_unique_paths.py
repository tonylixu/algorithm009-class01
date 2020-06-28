"""
Leetcode good solutions:
  - Java 简单明了动态规划 https://leetcode-cn.com/problems/unique-paths/solution/java-jian-dan-ming-liao-de-dong-tai-gui-hua-qiu-ji/
  - 递归 https://leetcode-cn.com/problems/unique-paths/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-20/

Clarificcation:
  - 1 <= m, n <= 100
  - The answer will be less than or equal to 2 * 10 ^ 9
Possible solutions:
  - Recursive
  - Dynamic programming
Coding:
Testing:
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.recursive_solution_optimized(m, n)

    def recursive_solution_optimized(self, m, n):
        """
            Similar to recursive solution, we can do some optimizations. To calculate
        solutions of (1, 0), we need to calculate solutions of (1, 1), and to calculate solutions
        of (0, 1), we also need to calculate solutions of (1, 1). So we can use a "visited" hashmap
        to speedup
        """

        def helper(x, y, m, n, visited):
            if x == m and y == n:
                return 1
            n1 = n2 = 0
            k1 = str(x + 1) + '@' + str(y)
            if k1 in visited:
                n1 = visited[k1]
            else:
                # Recursive right
                if x + 1 <= m:
                    n1 = helper(x + 1, y, m, n, visited)
            k2 = str(x) + '@' + str(y + 1)
            if k2 in visited:
                n2 = visited[k2]
            else:
                # Recursive down
                if y + 1 <= n:
                    n2 = helper(x, y + 1, m, n, visited)
            visited[str(x) + '@' + str(y)] = n1 + n2
            return n1 + n2

        visited = {}
        return helper(0, 0, m - 1, n - 1, visited)

    def recursive_solution(self, m, n):
        """
        To calculate (0, 0) to (m-1, n-1) solutions, you need to calculate:
            - solutions of (1, 0) to (m-1, n-1) + solutions of (0, 1) to (m-1, n-1)
            - solutions of (1, 0) = solutions of (2, 0) + solutions of (1, 1)
            - solutions of (0, 1) = solutions of (1, 1) + solutions of (0, 2)
            ...
        """

        def helper(x, y, m, n, num):
            if x == m and y == n:
                return 1
            n1 = n2 = 0
            # Recursive right
            if x + 1 <= m:
                n1 = helper(x + 1, y, m, n, num)
            # Recursive down
            if y + 1 <= n:
                n2 = helper(x, y + 1, m, n, num)
            return n1 + n2

        return helper(0, 0, m - 1, n - 1, 0)

    def dp(self, m, n):
        """
        Time complexity: O(m*n)
        Space complexity: O(m*n)
        """
        status = [[0] * n for _ in range(m)]
        for i in range(n): status[0][i] = 1
        for j in range(m): status[j][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                status[i][j] = status[i - 1][j] + status[i][j - 1]
        return status[m - 1][n - 1]

    def dp2(self, m, n):
        """
        Time complexity: O(m*n)
        Space complexity: O(n)
        """
        status = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                status[j] += status[j - 1]
        return status[n - 1]