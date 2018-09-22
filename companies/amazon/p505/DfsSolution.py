import sys


class DfsSolution:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def shortestDistance(self, maze, start, destination):
        self.destination = destination
        self.shortest = sys.maxsize

        self.m = len(maze)
        self.n = len(maze[0])

    def dfsUtil(self, maze, visited, x, y, curDistance):
        if x == self.destination[0] and y == self.destination[1]:
            self.shortest = min(self.shortest, curDistance)
            return

        if visited[x][y]:
            return

        visited[x][y] = True
        for dx, dy in self.DIRECTIONS:
            nx = x
            ny = y
            dist = curDistance

            while not self.hitTheWall(maze, nx, ny):
                nx += dx
                ny += dy
                dist += 1

            nx -= dx
            ny -= dy
            dist -= 1
            self.dfsUtil(maze, visited, nx, ny, dist)

        visited[x][y] = False

    def hitTheWall(self, maze, x, y):
        m = len(maze)
        n = len(maze[0])

        if x < 0 or x >= m or y < 0 or y >= n:
            return True

        if maze[x][y] == 1:
            return True

        return False
