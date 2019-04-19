#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (40.73%)
# Total Accepted:    321.4K
# Total Submissions: 789.1K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#
from typing import List

class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        cnt = 0
        rootIds = [0 for _ in range(m * n)]
        weights = [0 for _ in range(m * n)]

        for row in range(m):
            for col in range(n):
                idx = row * n + col
                if grid[row][col] == '1':
                    cnt += 1
                    rootIds[idx] = idx
                    weights[idx] += 1
                else:
                    rootIds[idx] = -1

        self.count = cnt
        self.rootIds = rootIds
        self.weights = weights

    def root(self, x):
        if self.rootIds[x] == -1:
            return -1

        if self.rootIds[x] != x:
            self.rootIds[x] = self.root(self.rootIds[x])
        return self.rootIds[x]

    def union(self, x, y):
        rootX = self.root(x)
        rootY = self.root(y)

        if rootX == rootY:
            return

        self.count -= 1
        if self.weights[rootX] < self.weights[rootY]:
            self.rootIds[rootX] = rootY
            self.weights[rootY] += self.weights[rootX]
        else:
            self.rootIds[rootY] = rootX
            self.weights[rootX] += self.weights[rootY]

    def getCount(self):
        return self.count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        uf = UnionFind(grid)
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    idx = x * n + y
                    grid[x][y] = '0'

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if self.inGrid(nx, ny, grid) and grid[nx][ny] == '1':
                            uf.union(idx, nx * n + ny)
        return uf.getCount()

    def inGrid(self, x, y, grid):
        m, n = len(grid), len(grid[0])

        return x >= 0 and x < m and y >= 0 and y < n

