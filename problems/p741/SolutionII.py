class SolutionII:
    def cherry_picks(self, grid):
        n = len(grid)
        DP = [[0 for _ in range(n)] for _ in range(n)]
        DP[0][0] = grid[0][0]

        # total_steps = x1 + y1
        # 0 <= total_steps <= 2n-2
        # : 0 <= x1 + y1 <= 2n - 2
        # and 0 <= y1 <= n-1
        # so 0 <= total_steps - x1 <= n-1
        # so -n+1 <= x1 - total_steps <= 0
        # so total_steps - n + 1 <= x1 <= total_steps
        # and 0 <= x1 <= n - 1
        # so max(0, total_steps - n + 1) <= x1 <= min(n-1, total_steps)
        for t in range(1, 2*n - 1):
            for x1 in reversed(range(max(0, t - n + 1), min(n-1, t) + 1)):
                for x2 in reversed(range(max(0, t - n + 1), min(n-1, t) + 1)):
                    y1 = t - x1
                    y2 = t - x2

                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        DP[x1][x2] = -1
                        continue

                    if x1 - 1 >= 0:
                        DP[x1][x2] = max(DP[x1][x2], DP[x1-1][x2])
                    if x2 - 1 >= 0:
                        DP[x1][x2] = max(DP[x1][x2], DP[x1][x2-1])
                    if x1 - 1 >= 0 and x2 - 1 >= 0:
                        DP[x1][x2] = max(DP[x1][x2], DP[x1-1][x2-1])

                    if DP[x1][x2] < 0:
                        DP[x1][x2] = -1
                        continue

                    DP[x1][x2] += grid[x1][y1]
                    if x1 != x2:
                        DP[x1][x2] += grid[x2][y2]
            print('total_steps: {}'.format(t))
            print(DP)
        return max(0, DP[n-1][n-1])


def main():
    sol = SolutionII()
    test = [[0, 1, -1],
            [1, 0, -1],
            [1, 1,  1]]
    print(sol.cherry_picks(test))


if __name__ == '__main__':
    main()
