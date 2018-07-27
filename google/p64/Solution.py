import collections

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        # DP[i][j] represent the minimum path from 0,0 to i,j
        DP = [[0 for _ in range(n)] for _ in range(m)]
        DP[0][0] = grid[0][0]

        # the left-most column
        # The only path is going down
        for i in range(1, m):
            DP[i][0] = DP[i-1][0] + grid[i][0]
        
        for j in range(1, n):
            DP[0][j] = DP[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]
        return DP[m-1][n-1]
    
    def stupid_min_path_sum(self, grid):
        m = len(grid)
        n = len(grid[0])
        DP = [[0 for _ in range(m)] for _ in range(n)]

        DP[0][0] = grid[0][0]
        queue = collections.deque()
        queue.append((1, 0))
        queue.append((0, 1))
        while queue:
            i, j = queue.popleft()
            if i >= m or j >= n:
                continue

            upper = DP[i-1][j] if i-1 >= 0 else 10000
            left = DP[i][j-1] if j-1 >= 0 else 10000
            DP[i][j] = min(upper, left) + grid[i][j]
            
            queue.append((i+1, j))
            queue.append((i, j + 1))
        print(DP)
        return DP[m-1][n-1]


def main():
    sol = Solution()
    test = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(sol.minPathSum(test))
    print(sol.stupid_min_path_sum(test))

if __name__ == '__main__':
    main()
