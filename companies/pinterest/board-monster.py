# 一个二维的board,里面有0（表示可以通过），
# 1（wall不能通过），6（monster，可以通过但是会丢一条命）。
# input是start position, end position 和lives(有多少命)。问start到end的最短距离

from collections import deque
import unittest

class Solution:
    def minDistance(self, matrix, extraLives, start, end):
        if not matrix or not matrix[0]:
            return -1

        if extraLives <= 0:
            return -1

        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = deque()
        level = 0
        x, y = start
        queue.append((x, y, extraLives))
        visited[x][y] = True
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            size = len(queue)

            for _ in range(size):
                x, y, livesLeft = queue.popleft()

                if x == end[0] and y == end[1]:
                    return level

                for dx, dy in directions:
                    xx = x + dx
                    yy = y + dy

                    if xx < 0 or xx >= m or yy < 0 or yy >= n:
                        continue

                    if matrix[xx][yy] == 1:
                        continue

                    if matrix[xx][yy] == 6 and livesLeft < 1:
                        continue

                    if matrix[xx][yy] == 6:
                        livesLeft -= 1

                    queue.append((xx, yy, livesLeft))
                    visited[xx][yy] = True

            level += 1

        return -1

class SolutionTest(unittest.TestCase):
    def testMinDist(self):
        sol = Solution()
        matrix = [[0, 0, 0], [0, 6, 1], [0, 6, 0]]
        extraLives = 1
        start = (0, 0)
        end = (2, 2)
        self.assertEqual(4, sol.minDistance(matrix, extraLives, start, end))

unittest.main()
