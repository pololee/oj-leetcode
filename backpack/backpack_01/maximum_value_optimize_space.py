import unittest

class Solution:
    def maxValue(self, values, sizes, totalCapacity):
        DP = [0 for _ in range(totalCapacity + 1)]
        num = len(values)

        for i in range(1, num + 1):
            value = values[i - 1]
            size = sizes[i - 1]
            # it has to be the reversed direction, otherwise
            # when compute DP[j], DP[j-size] value is not the previous value,
            # it's been updated. 
            for j in reversed(range(size, totalCapacity + 1)):
                DP[j] = max(DP[j], DP[j-size] + value)
        
        return DP[totalCapacity]


class SolutionTest(unittest.TestCase):
    def test_maxValue(self):
        values = [4, 5, 6]
        sizes = [3, 4, 5]
        totalCapacity = 10
        sol = Solution()
        self.assertEqual(11, sol.maxValue(values, sizes, totalCapacity))


if __name__ == "__main__":
    unittest.main()
