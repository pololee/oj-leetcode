class Solution:
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        if not S or not T:
            return ""

        if len(S) < len(T):
            return ""
        
        m = len(S)
        n = len(T)

        DP = [[-1 for _ in range(n)] for _ in range(m)]
        if S[0] == T[0]:
            DP[0][0] = 0
        
        for i in range(1, m):
            if S[i] == T[0]:
                DP[i][0] = i
            else:
                DP[i][0] = DP[i-1][0]
        
        for j in range(1, n):
            for i in range(j, m):
                if S[i] == T[j]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = DP[i-1][j]
        
        ansStart = 0
        ansLen = m + 1
        for i in range(m):
            if DP[i][n-1] != -1:
                if i - DP[i][n-1] + 1 < ansLen:
                    ansStart = DP[i][n-1]
                    ansLen = i - DP[i][n-1] + 1
        
        if ansLen == m + 1:
            return ""
        return S[ansStart:ansStart + ansLen]
