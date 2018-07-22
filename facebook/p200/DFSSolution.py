class DFSSolution:
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        visited_land = set()
        num_of_rows = len(grid)
        num_of_cols = len(grid[0])
        count = 0

        for row in range(num_of_rows):
            for col in range(num_of_cols):
                if grid[row][col] == '1' and (row, col) not in visited_land:
                    count += 1
                    self.dfs(grid, row, col, visited_land)
        return count

    def dfs(self, grid, row, col, visited_land):
        if (row, col) in visited_land:
            return
        if self.out_of_grid(row, col, grid):
            return
        if grid[row][col] == '0':
            return

        visited_land.add((row, col))
        for x, y in self.DIRECTIONS:
            self.dfs(grid, row + x, col + y, visited_land)

    def out_of_grid(self, row, col, grid):
        num_of_rows = len(grid)
        num_of_cols = len(grid[0])

        return row < 0 or row >= num_of_rows or col < 0 or col >= num_of_cols
