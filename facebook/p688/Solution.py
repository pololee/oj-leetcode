class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K == 0:
            return 1.0
        
        directions = [(2, 1), (1,2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)]

        DP = [[0 for _ in range(N)] for _ in range(N)]
        DP[r][c] = 1

        for step in range(K):
            currentDP = [[0 for _ in range(N)] for _ in range(N)]

            for r in range(N):
                for c in range(N):
                    for dr, dc in directions:
                        new_r = r + dr
                        new_c = c + dc

                        if new_r >= 0 and new_r < N and new_c >= 0 and new_c < N:
                            currentDP[new_r][new_c] += DP[r][c] / 8
            DP = currentDP
        
        prob = 0.0
        for i in range(N):
            for j in range(N):
                prob += DP[i][j]
        return prob

def main():
    sol = Solution()
    print(sol.knightProbability(3, 2, 0, 0))

if __name__ == '__main__':
    main()
