import unittest


class Solution:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        DP = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.dfs(matrix, i, j, DP))
        return ans

    def dfs(self, matrix, x, y, DP):
        if DP[x][y] > 0:
            return DP[x][y]

        longest = 1
        m = len(matrix)
        n = len(matrix[0])
        for dx, dy in self.DIRECTIONS:
            xx = x + dx
            yy = y + dy

            if xx < 0 or xx >= m or yy < 0 or yy >= n:
                continue
            if matrix[xx][yy] <= matrix[x][y]:
                continue

            longest = max(longest, 1 + self.dfs(matrix, xx, yy, DP))

        DP[x][y] = longest
        return DP[x][y]


class SolutionTest(unittest.TestCase):
    def testLongest(self):
        sol = Solution()
        matrix = [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
        ]
        self.assertEqual(4, sol.longestIncreasingPath(matrix))
        matrix =[[1,2]]
        self.assertEqual(2, sol.longestIncreasingPath(matrix))

if __name__=='__main__':
    unittest.main()
