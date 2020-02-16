import unittest


class Backpack1:
    def backpack(self, nums, M):
        col_size = M + 1
        row_size = len(nums) + 1
        DP = [[False for _ in range(col_size)]
              for _ in range(row_size)]

        for x in range(row_size):
            DP[x][0] = True

        for y in range(1, col_size):
            DP[0][y] = False

        for i in range(1, row_size):
            for j in range(1, col_size):
                if j - nums[i-1] >= 0:
                    DP[i][j] = DP[i-1][j-nums[i-1]] or DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j]

        for y in reversed(range(col_size)):
            if DP[row_size-1][y]:
                return y

        return 0


class Backpack1Test(unittest.TestCase):
    def test_backpack(self):
        backpack = Backpack1()
        self.assertEqual(10, backpack.backpack([2, 3, 5, 7], 11))
        self.assertEqual(12, backpack.backpack([2, 3, 7], 12))


if __name__ == '__main__':
    unittest.main()
