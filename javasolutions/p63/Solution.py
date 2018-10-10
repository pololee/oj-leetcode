class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        DP = [[0 for _ in range(n)]
              for _ in range(m)]

        DP[0][0] = 1
        for i in range(1, m):
            DP[i][0] = 0 if obstacleGrid[i][0] == 1 else DP[i-1][0]

        for j in range(1, n):
            DP[0][j] = 0 if obstacleGrid[0][j] == 1 else DP[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    DP[i][j] = 0
                else:
                    DP[i][j] = DP[i-1][j] + DP[i][j-1]

        return DP[m-1][n-1]
