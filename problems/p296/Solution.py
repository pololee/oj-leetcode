class Solution:
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x_coords = []
        y_coords = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x_coords.append(i)
                    y_coords.append(j)
        
        x_coords = sorted(x_coords)
        x_meet = x_coords[len(x_coords) // 2]
        x_sum = 0
        for x in x_coords:
            x_sum += abs(x_meet - x)
        y_coords = sorted(y_coords)
        y_meet = y_coords[len(y_coords) // 2]
        y_sum = 0
        for y in y_coords:
            y_sum += abs(y_meet - y)
        
        return x_sum + y_sum

