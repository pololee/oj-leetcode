import unittest

class Solution:
    def minNumberToFullfill(self, sizes, capacity):
        size = len(sizes)
        DP = [[None for _ in range(capacity + 1)]
              for _ in range(size + 1)]
        
        for i in range(size + 1):
            DP[i][0] = 0
        
        for i in range(1, size + 1):
            for j in range(1, capacity + 1):
                if j < sizes[i-1]:
                    DP[i][j] = DP[i-1][j]
                else:
                    a = DP[i-1][j]
                    b = DP[i-1][j-sizes[i-1]]

                    if a is not None and b is not None:
                        DP[i][j] = min(a, b + 1)
                    elif a is None and b is None:
                        DP[i][j] = None
                    elif a is None:
                        DP[i][j] = b + 1
                    elif b is None:
                        DP[i][j] = a
        return DP[size][capacity]

class SolutionTest(unittest.TestCase):
    def test_minNumberToFullfill(self):
        sol = Solution()
        self.assertEqual(2, sol.minNumberToFullfill([2, 3, 4, 7], 10))
        self.assertIsNone(sol.minNumberToFullfill([2, 3, 5, 7], 11))

unittest.main()
