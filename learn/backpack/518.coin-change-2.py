import unittest


class Solution:
    def cmbChange(self, coins, amount):
        DP = [0 for _ in range(amount + 1)]
        DP[0] = 1

        for coin in coins:
            print(coin)
            for i in range(1, amount + 1):
                if i >= coin:
                    DP[i] += DP[i-coin]
            print(DP)
        return DP[amount]

class SolutionTest(unittest.TestCase):
    def testCmbChange(self):
        sol = Solution()
        sol.cmbChange([1, 2, 5], 5)

if __name__ == "__main__":
    unittest.main()
