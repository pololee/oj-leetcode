class DfsSolution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs_util(grid, i, j)
        return count

    def dfs_util(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return

        if grid[x][y] == "0":
            return

        grid[x][y] = "0"
        self.dfs_util(grid, x - 1, y)
        self.dfs_util(grid, x, y - 1)
        self.dfs_util(grid, x + 1, y)
        self.dfs_util(grid, x, y + 1)


class BfsSolution:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    queue = collections.deque()
                    queue.append((i, j))
                    grid[i][j] = "0"

                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in self.DIRECTIONS:
                            new_x = x + dx
                            new_y = y + dy
                            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                                continue
                            if grid[new_x][new_y] == "1":
                                queue.append((new_x, new_y))
                                grid[new_x][new_y] = "0"
        return count
