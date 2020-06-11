"""
Leetcode: https://leetcode.com/problems/minesweeper/
"""

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # Edge case and basic case judge
        if not board or not click:
            return []
        i, j = click
        m, n = len(board), len(board[0])
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board

        self.dfs2(board, i, j, m, n)
        return board

    def dfs2(self, board, i, j, m, n):
        if board[i][j] != 'E':
            return

        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        mine_count = 0

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != 'B':
                if board[ni][nj] == 'M':
                    mine_count += 1

        if mine_count != 0:
            board[i][j] = str(mine_count)
            return
        else:
            board[i][j] = 'B'

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs2(board, ni, nj, m, n)

    def bfs(self, board, i, j, m, n):
        if board[i][j] != 'E':
            return

        # Since we use 'B' to mark sth already visited, we don't need a visted set()
        queue = [(i, j)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            cur_click = queue.pop()
            # Set up an array of tuples for all the adjacent directions we should check
            mine_count, blank_coords = 0, []
            for d in directions:
                i, j = cur_click
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != 'B':
                    if board[ni][nj] == 'M':
                        # Found a mine, bump up mineCount
                        mine_count += 1
                    elif board[ni][nj] == 'E':
                        # Add to our array of blank coordinates for later
                        blank_coords.append((ni, nj))
            # If we found any mines adjacent, change this value to be the mine count
            if mine_count != 0:
                board[i][j] = str(mine_count)
            else:
                # We didn't find any mines, so continue to expand our search via our blankCoords
                queue.extend(blank_coords)
                # Also change this space to B, both for the final result and to mark visited
                board[i][j] = 'B'
        return board

    def dfs(self, board, i, j, m, n):
        if board[i][j] != 'E':
            return

        # 8 directions
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        mine_count = 0

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                mine_count += 1

        if mine_count == 0:
            board[i][j] = 'B'
        else:
            board[i][j] = str(mine_count)
            return

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n:
                self.dfs(board, ni, nj)
