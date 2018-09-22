class BfsWithoutPQ:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]:
            return -1
        
        m = len(maze)
        n = len(maze[0])
        shortest = [[-1 for _ in range(m)]
                    for _ in range(n)]
        startX, startY = start
        shortest[startX][startY] = 0
        

