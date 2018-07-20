import collections

class Solution:
    INF = 2147483647

    def walls_and_gates(self, rooms):
        """
        :rooms type: list
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0 or len(rooms[0]) == 0:
            return

        num_of_rows = len(rooms)
        num_of_cols = len(rooms[0])
        queue = collections.deque()
        # enqueue all the gates postions
        for i in range(num_of_rows):
            for j in range(num_of_cols):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()

            # move up
            if row - 1 >= 0 and rooms[row - 1][col] == self.INF:
                rooms[row - 1][col] = rooms[row][col] + 1
                queue.append((row - 1, col))
            
            # move down
            if row + 1 < num_of_rows and rooms[row + 1][col] == self.INF:
                rooms[row + 1][col] = rooms[row][col] + 1
                queue.append((row + 1, col))
            
            # move left
            if col - 1 >= 0 and rooms[row][col - 1] == self.INF:
                rooms[row][col - 1] = rooms[row][col] + 1
                queue.append((row, col - 1))
            
            # move right
            if col + 1 < num_of_cols and rooms[row][col + 1] == self.INF:
                rooms[row][col + 1] = rooms[row][col] + 1
                queue.append((row, col + 1))

class DFSSolution:
    def walls_and_gates(self, rooms):
        if len(rooms) == 0 or len(rooms[0]) == 0:
            return
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)
    
    def dfs(self, rooms, row, col, distance):
        # distance > rooms[row][col] is very important here
        # 1. do not update walls and gates (-1 and 0s)
        # 2. distinguish the visited and non-visited nodes (the visited can only have smaller distance)
        # when you make dfs call, the distance you provide is distance + 1. so the visited nodes much
        # have smaller distance
        # 3. stop earlier when you find the previous gate has given shorter distance than the current one
        if row < 0 or row >= len(rooms) or col < 0 or col >= len(rooms[0]) or distance > rooms[row][col]:
            return
        
        rooms[row][col] = distance
        self.dfs(rooms, row - 1, col, distance + 1)
        self.dfs(rooms, row + 1, col, distance + 1)
        self.dfs(rooms, row, col - 1, distance + 1)
        self.dfs(rooms, row, col + 1, distance + 1)

if __name__ == '__main__':
    test = [[Solution.INF, -1, 0, Solution.INF],
            [Solution.INF, Solution.INF, Solution.INF, -1],
            [Solution.INF, -1, Solution.INF, -1],
            [0, -1, Solution.INF, Solution.INF]]
    sol = DFSSolution()
    sol.walls_and_gates(test)
    print(test)