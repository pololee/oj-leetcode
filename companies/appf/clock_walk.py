import unittest

class Solution:
    SIZE = 12

    def shortestDist(self, start, finish):
        clockwise = self._clockwiseDist(start, finish)
        counterClockwise = self._counterClockwiseDist(start, finish)

        if clockwise < counterClockwise:
            return ('clockwise', clockwise)
        return ('counter clockwise', counterClockwise)

    def _clockwiseDist(self, start, finish):
        return (self.SIZE + finish - start) % self.SIZE

    def _counterClockwiseDist(self, start, finish):
        return self.SIZE - self._clockwiseDist(start, finish)


class SolutionTest(unittest.TestCase):
    def testShortestDist(self):
        sol = Solution()

        self.assertEqual(('clockwise', 0), sol.shortestDist(1, 1))
        self.assertEqual(('clockwise', 5), sol.shortestDist(2, 7))
        self.assertEqual(('counter clockwise', 5), sol.shortestDist(7, 2))
        self.assertEqual(('counter clockwise', 4), sol.shortestDist(2, 10))
        self.assertEqual(('clockwise', 4), sol.shortestDist(10, 2))
        self.assertEqual(('clockwise', 3), sol.shortestDist(12, 3))

if __name__=="__main__":
    unittest.main()
