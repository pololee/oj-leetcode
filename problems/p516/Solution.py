class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        size = len(s)
        DP = [[0 for _ in range(size)] for _ in range(size)]

        for start in reversed(range(size)):
            DP[start][start] = 1
            for j in range(start + 1, size):
                if s[start] == s[j]:
                    DP[start][j] = DP[start + 1][j - 1] + 2
                else:
                    DP[start][j] = max(DP[start+1][j], DP[start][j-1])
        return DP[0][size-1]
    
    def longestPalindromeSubseqRecursive(self, s):
        if not s:
            return 0
        
        size = len(s)
        DP = [[-1 for _ in range(size)] for _ in range(size)]

        self.compute(0, size - 1, s, DP)

        return DP[0][size - 1]
    
    def compute(self, start, end, s, dp):
        if dp[start][end] != -1:
            return
        
        if start == end:
            dp[start][end] = 1
            return
        
        if start + 1 == end:
            if s[start] == s[end]:
                dp[start][end] = 2
            else:
                dp[start][end] = 1            
            return
        
        self.compute(start + 1, end, s, dp)
        self.compute(start, end - 1, s, dp)
        self.compute(start + 1, end - 1, s, dp)

        if s[start] == s[end]:
            dp[start][end] = dp[start+1][end-1] + 2
        else:
            dp[start][end] = max(dp[start+1][end], dp[start][end-1])

def main():
    sol = Solution()
    print(sol.longestPalindromeSubseq('bbbab'))
    print(sol.longestPalindromeSubseqRecursive('bbbab'))
if __name__ == '__main__':
    main()
