"""
Clarification:
  - If grid is empty, reurn 0
  - All non-negative numbers
  - What if a number is 0? No impact
Possible solutions:
  - Recursive
  - Dynamic programming
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.recursive_optimized(grid)

    def recursive_optimized(self, grid):
        """
            Recursive with optimization. Similar to recursive solution, we use a hashmap visited to store
        already visted (i, j).

        Time complexity: O(2^(m+n))
        Space complexity: O(m+n)
        """

        def helper(grid, i, j, m, n, v):
            if (i, j) in v: return v[(i, j)]
            # Check valid index
            if i >= m or j >= n: return float('inf')
            # Recursion terminator
            if i == m - 1 and j == n - 1: return grid[i][j]
            # Process current logic and return
            v[(i, j)] = grid[i][j] + min(helper(grid, i + 1, j, m, n, v), helper(grid, i, j + 1, m, n, v))
            return v[(i, j)]

        m, n, visited = len(grid), len(grid[0]), {}
        return helper(grid, 0, 0, m, n, visited)

    def recursive(self, grid):
        """
        Recursive without optimization. For each (i, j), you have two options:
            - (i, j) -> (i+1, j)
            - (i, j) -> (i, j+1)
        So the minimum total cost = grid[i][j] + min(cost(grid, i + 1, j), cost(grid, i, j + 1))
        Based on above, we can write the recursive solution

        Time complexity: O(2^(m+n))
        Space complexity: O(m+n)
        """

        def helper(grid, i, j, m, n):
            # Check valid index
            if i >= m or j >= n: return float('inf')
            # Recursion terminator
            if i == m - 1 and j == n - 1: return grid[i][j]
            # Process current logic and return
            return grid[i][j] + min(helper(grid, i + 1, j, m, n), helper(grid, i, j + 1, m, n))

        m, n = len(grid), len(grid[0])
        return helper(grid, 0, 0, m, n)

    def dynamic_p(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0 and j != 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]