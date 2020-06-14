def numIslands(grid):
    """
        Go through one element at a time in grid, if element is a 1, which means it is a piece of island.
    Then we do a DFS search based on this element. For each visited element, we set it to 0 to avoid duplication.
       ^
       |
    <- 1 ->
       |
       V

    Time complexity: O(MN), all 1s
    Space complexity: O(MN)
    """
    def dfs_method(grid, i, j):
        def dfs(g, _i, _j):
            # Check invalid index
            if _i < 0 or _j < 0 or _i >= len(g) or _j >= len(g[0]) or g[_i][_j] != '1':
                return
            g[_i][_j] = '0'
            dfs(g, _i + 1, _j)
            dfs(g, _i - 1, _j)
            dfs(g, _i, _j - 1)
            dfs(g, _i, _j + 1)

        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

    def sink(g, _i, _j):
        if 0 <= i <= len(g) and 0 <= i <= len(g[i]) and g[i][j] == '1':
            g[_i][_j] = '0'
            list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
            return 1
        return 0
    return sum(sink(g, i, j) for i in range(len(grid)) for j in range(len(grid[i])))






