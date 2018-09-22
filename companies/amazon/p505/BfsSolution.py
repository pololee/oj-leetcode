import heapq


class Solution:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])

        visited = [[False for _ in range(n)]
                   for _ in range(m)]
        priorityQueue = []
        heapq.heappush(priorityQueue, (0, start[0], start[1]))

        while priorityQueue:
            distance, x, y = heapq.heappop(priorityQueue)

            if x == destination[0] and y == destination[1]:
                return distance

            if visited[x][y]:
                continue
            visited[x][y] = True

            for dx, dy in self.DIRECTIONS:
                nx = x
                ny = y
                curDistance = distance

                while not self.hitTheWall(maze, nx, ny):
                    nx += dx
                    ny += dy
                    curDistance += 1

                nx = nx - dx
                ny = ny - dy
                curDistance -= 1
                heapq.heappush(priorityQueue, (curDistance, nx, ny))
        return -1

    def hitTheWall(self, maze, x, y):
        m = len(maze)
        n = len(maze[0])

        if x < 0 or x >= m or y < 0 or y >= n:
            return True

        if maze[x][y] == 1:
            return True

        return False
