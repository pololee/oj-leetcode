class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        DP = [[[None for _ in range(n)]
               for _ in range(n)]
              for _ in range(n)]

        for x1 in range(0, n):
            for y1 in range(0, n):
                for x2 in range(0, n):
                    y2 = x1 + y1 - x2  # -n < y2 < 2n

                    if y2 < 0 or y2 >= n:
                        DP[x1][y1][x2] = -1
                        continue

                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        DP[x1][y1][x2] = -1
                        continue

                    if x1 == 0 and y1 == 0:
                        DP[x1][y1][x2] = grid[0][0]
                        continue

                    uppper_12 = DP[x1-1][y1][x2-1] if x1 - 1 >= 0 and x2-1 >= 0 else -1
                    left_12 = DP[x1][y1-1][x2] if y1 - 1 >= 0 and y2 - 1 >= 0 else -1
                    upper_1_left_2 = DP[x1-1][y1][x2] if x1 - 1 >= 0 and y2 - 1 >= 0 else -1
                    left_1_upper_2 = DP[x1][y1-1][x2-1] if y1 - 1 >= 0 and x2-1 >= 0 else -1

                    total = max(uppper_12, left_12, upper_1_left_2, left_1_upper_2)
                    if total < 0:
                        DP[x1][y1][x2] = -1
                        continue
                    
                    total += grid[x1][y1]
                    if x1 != x2:
                        total += grid[x2][y2]
                    
                    DP[x1][y1][x2] = total

        return max(0, DP[n-1][n-1][n-1])

    # this is the recursive version of the above algorithm.
    # somehow it cannot pass leetcode. TLE
    def dp_util(self, x1, y1, x2):
        y2 = x1 + y1 - x2

        if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
            return -1

        if self.grid[x1][y1] == -1 or self.grid[x2][y2] == -1:
            return -1

        if x1 == 0 and y1 == 0:
            return self.grid[0][0]

        if self.DP[x1][y1][x2]:
            return self.DP[x1][y1][x2]

        total = max(self.dp_util(x1-1, y1, x2-1),  # x1, y1 comes from upper, x2, y2 comes from upper
                    # x1, y1 comes from left, x2, y2 comes from left
                    self.dp_util(x1, y1-1, x2),
                    # x1, y1 comes from upper, x2, y2 comes from left
                    self.dp_util(x1-1, y1, x2),
                    self.dp_util(x1, y1-1, x2-1))  # x1, y1 comes from left, x2, y2 comes from upper
        if total < 0:
            return -1

        total += grid[x1][y1]
        if x1 != x2:
            total += grid[x2][y2]

        return total

def main():
    sol = Solution()
    test = [[0, 1, -1],
            [1, 0, -1],
            [1, 1,  1]]
    print(sol.cherryPickup(test))

if __name__ == '__main__':
    main()
