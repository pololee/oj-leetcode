from sys import maxsize
from collections import deque


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        dist = [[maxsize for _ in range(n)]
                for _ in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]

                if xx >= 0 and xx < m and yy >= 0 and yy < n:
                    if dist[xx][yy] > dist[x][y] + 1:
                        dist[xx][yy] = dist[x][y] + 1
                        queue.append((xx, yy))
        return dist
