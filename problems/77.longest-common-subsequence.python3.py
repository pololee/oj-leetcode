class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        
        m = len(A)
        n = len(B)
        DP = [[0 for _ in range(n)]
              for _ in range(m)]
        
        for i in range(m):
            if A[i] == B[0]:
                DP[i][0] = 1
        
        for j in range(n):
            if A[0] == B[j]:
                DP[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if A[i] == B[j]:
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        
        return DP[m-1][n-1]
