# the maximum value of full pack
import unittest


class Solution:
    def zero_one_full_pack(self, values, sizes, totalCapacity):
        size = len(sizes)

        DP = [[None for _ in range(totalCapacity + 1)]
              for _ in range(size + 1)]

        for i in range(size + 1):
            DP[i][0] = 0

        for i in range(1, size + 1):
            for j in range(1, totalCapacity + 1):
                if sizes[i-1] > j:
                    DP[i][j] = DP[i-1][j]
                else:
                    a = DP[i-1][j]
                    b = DP[i-1][j-sizes[i-1]]

                    if a is None and b is None:
                        DP[i][j] = None
                    elif a is not None and b is not None:
                        DP[i][j] = max(a, b + values[i-1])
                    elif a is not None:
                        DP[i][j] = a
                    elif b is not None:
                        DP[i][j] = b + values[i-1]
        
        for capacity in reversed(range(totalCapacity + 1)):
            if DP[size][capacity]:
                return DP[size][capacity]
        return 0


class SolutionTest(unittest.TestCase):
    def testZeroOneFullPack(self):
        sol = Solution()
        self.assertEqual(8, sol.zero_one_full_pack([3, 4, 5], [4, 5, 6], 10))

unittest.main()
