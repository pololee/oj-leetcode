import unittest


class Solution:
    def maxValue(self, values, sizes, totalCapacity):
        DP = self.buildDP(values, sizes, totalCapacity)
        num = len(values)

        return DP[num][totalCapacity]

    def maxValueSolutionPath(self, values, sizes, totalCapacity):
        DP = self.buildDP(values, sizes, totalCapacity)
        i = len(values)
        j = totalCapacity

        while i > 0 and j > 0:
            if DP[i-1][j] != DP[i][j]:
                print("Object {} picked, size: {}, value: {}".format(i-1, sizes[i-1], values[i-1]))
                j -= sizes[i-1]
            i -= 1

    def buildDP(self, values, sizes, totalCapacity):
        num = len(values)
        DP = [[0 for _ in range(totalCapacity + 1)]
              for _ in range(num + 1)]

        for i in range(1, num + 1):
            for j in range(1, totalCapacity + 1):
                value = values[i-1]
                size = sizes[i-1]

                if size > j:
                    DP[i][j] = DP[i-1][j]
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i-1][j-size] + value)
        return DP


class SolutionTest(unittest.TestCase):
    def test_maxValue(self):
        values = [4, 5, 6]
        sizes = [3, 4, 5]
        totalCapacity = 10
        sol = Solution()
        self.assertEqual(11, sol.maxValue(values, sizes, totalCapacity))
    
    def test_maxValueSolutionPath(self):
        values = [4, 5, 6]
        sizes = [3, 4, 5]
        totalCapacity = 10
        sol = Solution()
        sol.maxValueSolutionPath(values, sizes, totalCapacity)

if __name__ == "__main__":
    unittest.main()
