import unittest

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.isMatchUtil(s, 0, p, 0, dict())

    def isMatchUtil(self, s, sIdx, p, pIdx, memo):
        if (sIdx, pIdx) in memo:
            return memo[(sIdx, pIdx)]

        if pIdx == len(p):
            return sIdx == len(s)

        if sIdx == len(s):
            return self.isEmptyPattern(p, pIdx)

        sChar = s[sIdx]
        pChar = p[pIdx]
        match = False
        if pChar == '*':
            match = self.isMatchUtil(s, sIdx + 1, p, pIdx, memo) or self.isMatchUtil(s, sIdx, p, pIdx + 1, memo)
        else:
            match = (self.charMatch(sChar, pChar) and self.isMatchUtil(s, sIdx + 1, p, pIdx + 1, memo))

        memo[(sIdx, pIdx)] = match
        return match

    def charMatch(self, sChar, pChar):
        return pChar in (sChar, '?')

    def isEmptyPattern(self, p, pIdx):
        size = len(p)
        for i in range(pIdx, size):
            if p[i] != '*':
                return False
        return True

class DpSolution:
    def isMatch(self, s, p):
        sSize = len(s)
        pSize = len(p)

        dp = [[False for _ in range(pSize + 1)] for _ in range(sSize + 1)]
        dp[0][0] = True

        for i in range(1, pSize + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = False
        
        for i in range(1, sSize + 1):
            for j in range(1, pSize + 1):
                sChar = s[i-1]
                pChar = p[j-1]

                if pChar == '*':
                    # dp[i-1][j] "*" as any sequence
                    # dp[i][j-1] "*" as empty
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = pChar in (sChar, "?") and dp[i-1][j-1]

        return dp[sSize][pSize]


class SolutionTest(unittest.TestCase):
    def testIsMatch(self):
        sol = Solution()
        self.assertFalse(sol.isMatch('acdcb', "a*c?b"))
    
    def testIsMatch(self):
        sol = DpSolution()
        self.assertFalse(sol.isMatch('acdcb', "a*c?b"))

unittest.main()
