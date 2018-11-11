import unittest

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = [[0 for _ in range(n)] for _ in range(m)]
        DP[0][0] = 1

        for i in range(1, n):
            DP[0][i] = 1
        
        for i in range(1, m):
            DP[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i-1][j] + DP[i][j-1]
        return DP[m-1][n-1]

class SolutionTest(unittest.TestCase):
    def testUniquePaths(self):
        sol = Solution()
        self.assertEqual(3, sol.uniquePaths(3, 2))
        self.assertEqual(28, sol.uniquePaths(7, 3))

unittest.main()
