"""
Clarification:
  - What's the range of N: [1, 200]
  - Any invalid characters other than 0 or 1?
  - If M[i][j] = 1, then M[j][i] = 1

Possible solutions:
  - DFS:
    You can treat M as a graph,
M= [1 1 0 0 0 0
    1 1 0 0 0 0
    0 0 1 1 1 0
    0 0 1 1 0 0
    0 0 1 0 1 0
    0 0 0 0 0 1]
    M[i][j] = 1 means i and j has a connection
    DFS solution:
      - Start from each node, and use visited[N] to keep visted node
      - We search any adjacent node, set as current node, then keep on searching adjacent nodes of
        the current node, until the current node has no more adjacent node, then backtracing
    Time complexity: O(N^2), we need to visited every node in M
    Space complextiy: O(N), the length of visited array
    https://leetcode-cn.com/problems/friend-circles/solution/peng-you-quan-by-leetcode/
  - BFS: Similar to DSF, instead of search one adjacent node, we search all adjacent nodes first
    Time complexity: O(N^2), we need to visited every node in M
    Space complextiy: O(N), the length of visited array
    https://leetcode-cn.com/problems/friend-circles/solution/peng-you-quan-by-leetcode/
  - Union Find:
    Time complexity: O(N^2), we need to visited every node in M
    Space complextiy: O(N), parent size is N.
    https://leetcode-cn.com/problems/friend-circles/solution/union-find-suan-fa-xiang-jie-by-labuladong/
"""


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        return self.union_find(M)

    def dfs(self, M):
        def helper(M, visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    helper(M, visited, j)

        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                helper(M, visited, i)
                count += 1
        return count

    def bfs(self, M):
        count, length = 0, len(M)
        visited = [0] * length
        queue = []
        for i in range(length):
            if visited[i] == 0:
                queue.append(i)
                while queue:
                    s = queue.pop()
                    visited[s] = 1
                    for j in range(length):
                        if M[s][j] == 1 and visited[j] == 0:
                            queue.append(j)
                count += 1
        return count

    def union_find(self, M):
        f, s = {}, {}
        count = len(M)

        def find(x):
            f.setdefault(x, x)
            # Compress path
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            nonlocal count
            x_father, y_father = find(x), find(y)
            if x_father == y_father: return
            # Attach small subtree to the root of large subtree
            if s.setdefault(x_father, 1) < s.setdefault(y_father, 1):
                f[x_father] = y_father
                s[y_father] += s[x_father]
            else:
                f[y_father] = x_father
                s[x_father] += s[y_father]
            count -= 1

        for i in range(len(M) - 1):
            for j in range(i + 1, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        return count