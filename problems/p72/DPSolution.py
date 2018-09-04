class DPSolution:
    def min_edit_distance(self, x, y):
        m = len(x)
        n = len(y)

        DP = [[0 for _ in range(n + 1)]
               for _ in range(m + 1)]
        
        for j in range(n + 1):
            DP[0][j] = j
        
        for i in range(m + 1):
            DP[i][0] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0
                if x[i-1] != y[j-1]:
                    cost += 1
                
                DP[i][j] = min(
                    DP[i-1][j] + 1,
                    DP[i][j-1] + 1,
                    DP[i-1][j-1] + cost
                )
        return DP[m][n]
