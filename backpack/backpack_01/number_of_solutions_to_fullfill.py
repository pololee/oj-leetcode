import unittest

class Solution:
    def waysToFullFill(self, sizes, capacity):
        size = len(sizes)

        DP = [[0 for _ in range(capacity + 1)]
              for _ in range(size + 1)]
        
        for i in range(size + 1):
            DP[i][0] = 1

        for i in range(1, size + 1):
            for j in range(1, capacity + 1):
                x = sizes[i-1]

                if x > j:
                    DP[i][j] = DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j] + DP[i-1][j-x]
        return DP[size][capacity]

class SolutionTest(unittest.TestCase):
    def testWaysToFullFill(self):
        sol = Solution()
        self.assertEqual(0, sol.waysToFullFill([2, 3, 5, 7], 11))
        self.assertEqual(2, sol.waysToFullFill([2, 3, 4, 5], 7))

unittest.main()
