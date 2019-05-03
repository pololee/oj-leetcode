# ### [407\. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/)

# Difficulty: **Hard**


# Given an `m x n` matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

# **Note:**

# Both _m_ and _n_ are less than 110\. The height of each unit cell is greater than 0 and is less than 20,000.

# **Example:**

# ```
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]

# Return 4.
# ```

# ![](https://assets.leetcode.com/uploads/2018/10/13/rainwater_empty.png)

# The above image represents the elevation map `[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]` before the rain.

# ![](https://assets.leetcode.com/uploads/2018/10/13/rainwater_fill.png)

# After the rain, water is trapped between the blocks. The total volume of water trapped is 4.


# #### Solution

# Language: **Python3**

# ```python3
# class Solution:
#     def trapRainWater(self, heightMap: List[List[int]]) -> int:
#         
# ```

from typing import List
import heapq


class Cell:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.height == other.height

    def __gt__(self, other):
        return self.height > other.height


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        heap = []
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for _ in range(n)]
                   for _ in range(m)]

        for i in range(n):
            visited[0][i] = True
            heapq.heappush(heap, Cell(0, i, heightMap[0][i]))
            visited[m-1][i] = True
            heapq.heappush(heap, Cell(m-1, i, heightMap[m-1][i]))

        for i in range(m):
            visited[i][0] = True
            heapq.heappush(heap, Cell(i, 0, heightMap[i][0]))
            visited[i][n-1] = True
            heapq.heappush(heap, Cell(i, n - 1, heightMap[i][n-1]))

        ans = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while heap:
            cell = heapq.heappop(heap)
            for dx, dy in directions:
                x = cell.x + dx
                y = cell.y + dy

                if x < 0 or x >= m or y < 0 or y >= n:
                    continue

                if visited[x][y]:
                    continue

                # if the neightbor is lower, it can trap water
                # the cell is lowest one on the entire border, so we don't need to worry 
                # the trapped water may flow to outside through some other border
                ans += max(0, cell.height - heightMap[x][y])

                # when add to heap, 
                # if its height than cell, then the height is itself height
                # if not, then then height is the cell's height, because it trapped water
                visited[x][y] = True
                heapq.heappush(
                    heap,
                    Cell(x, y, max(cell.height, heightMap[x][y]))
                )

        return ans


if __name__ == "__main__":
    sol = Solution()
    heightM = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    print(sol.trapRainWater(heightM))
