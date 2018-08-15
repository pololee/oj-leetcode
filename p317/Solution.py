import collections
import sys

class Solution:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        row_size = len(grid)
        col_size = len(grid[0])

        distance = [[0 for _ in range(col_size)]
                    for _ in range(row_size)]
        reaches = [[0 for _ in range(col_size)]
                   for _ in range(row_size)]
        num_of_buildings = 0
        
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 1:
                    num_of_buildings += 1

                    self.bfs(grid, distance, reaches, i, j)

        shortest = sys.maxsize
        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == 0 and reaches[i][j] == num_of_buildings:
                    shortest = min(shortest, distance[i][j])
        
        if shortest == sys.maxsize:
            return -1
        return shortest

    
    def bfs(self, grid, distance, reaches, istart, jstart):
        row_size = len(grid)
        col_size = len(grid[0])
        visited = [[False for _ in range(col_size)]
                   for _ in range(row_size)]

        queue = collections.deque()
        queue.append((istart, jstart))
        visited[istart][jstart] = True
        level = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                row, col = queue.popleft()
                if grid[row][col] == 0:
                    distance[row][col] += level
                    reaches[row][col] += 1
                
                for drow, dcol in self.DIRECTIONS:
                    new_row = row + drow
                    new_col = col + dcol

                    if new_row >= 0 and new_row < row_size and new_col >= 0 and new_col < col_size and grid[new_row][new_col] == 0 and not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        queue.append((new_row, new_col))
            level += 1

def main():
    test = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    sol = Solution()
    print(sol.shortestDistance(test))

if __name__ == '__main__':
    main()
