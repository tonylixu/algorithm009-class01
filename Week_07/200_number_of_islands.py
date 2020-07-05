"""
Clarifications:
  - Island is 0?
  - Any other characters in the map
  - Max length of map
Possible solutions:
  - DFS: We can treat the map as a graph, and sacn the entire graph. If one node has 1, then we
  perform depth-first search on [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]. We also mark the 1 to 0
  to avoid duplications.
    Time complexity: O(MxN)
    Space complexity: O(MxN), worst case there are no water
  - BFS: Simiar to DFS
    Time complexity: O(MxN)
    Space complexity: O(MxN), worst case there are no water
  - Union-find
    Time complexity: O(MxN*a(MxN))
    Space complexity: O(MxN)
"""


class Solution:
    def numIslands(self, grid):
        return self.bfs(grid)

    def union_find(self, grid):
        from typing import List
        class UnionFind:
            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root, q_root = self.find(p), self.find(q)
                if p_root == q_root: return

                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1

                self.count -= 1

        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        directions = [(1, 0), (0, 1)]
        dummy_node = row * col

        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        return uf.get_count() - 1

    def dfs(self, grid):
        if not grid:
            return 0

        def helper(grid, i, j, m, n):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                for x, y in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                    helper(grid, i + x, j + y, m, n)
            return

        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    helper(grid, i, j, m, n)
                    count += 1
        return count

    def bfs(self, grid):
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'
                    neighbor = collections.deque([(i, j)])
                    while neighbor:
                        r, c = neighbor.popleft()
                        for x, y in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                            p, q = r + x, c + y
                            if 0 <= p < m and 0 <= q < n and grid[p][q] == '1':
                                neighbor.append((p, q))
                                grid[p][q] = '0'
        return count

