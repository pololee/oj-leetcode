import unittest


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = dict()
        return self.isMatchUtil(s, 0, p, 0, memo)

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

        if pIdx + 1 < len(p) and p[pIdx + 1] == '*':
            match = self.isMatchUtil(s, sIdx, p, pIdx + 2, memo) or \
                self.charMatch(sChar, pChar) and self.isMatchUtil(
                    s, sIdx + 1, p, pIdx, memo)
        else:
            match = self.charMatch(sChar, pChar) and self.isMatchUtil(
                s, sIdx + 1, p, pIdx + 1, memo)

        memo[(sIdx, pIdx)] = match
        return match

    def charMatch(self, sChar, pChar):
        return pChar in (sChar, '.')

    def isEmptyPattern(self, p, pIdx):
        size = len(p)
        for i in range(pIdx, size):
            if p[i] != '*' and (i+1 >= size or p[i+1] != '*'):
                return False
        return True


class DpSolution:
    def isMatch(self, s, p):
        sSize = len(s)
        pSize = len(p)

        DP = [[False for _ in range(pSize + 1)]
              for _ in range(sSize + 1)]
        DP[0][0] = True

        if pSize > 0 and p[0] == '*':
            DP[0][1] = True

        for i in range(2, pSize + 1):
            if p[i-1] == '*':
                DP[0][i] = DP[0][i-2]

        for i in range(1, sSize + 1):
            for j in range(1, pSize + 1):
                sChar = s[i-1]
                pChar = p[j-1]

                if pChar == '*' and j >= 2:
                    DP[i][j] = DP[i][j-2] or (p[j-2]
                                              in (sChar, '.') and DP[i-1][j])
                else:
                    if pChar in (sChar, '.'):
                        DP[i][j] = DP[i-1][j-1]
        return DP[sSize][pSize]


class SolutionTest(unittest.TestCase):
    def testIsEmptyPattern(self):
        sol = Solution()
        self.assertTrue(sol.isEmptyPattern('*', 0))
        self.assertTrue(sol.isEmptyPattern('a*.*', 2))

    def testIsMatch(self):
        sol = Solution()
        self.assertFalse(sol.isMatch("aa", 'a'))
        self.assertTrue(sol.isMatch("aa", "a*"))
        self.assertTrue(sol.isMatch("aa", "aa"))
        self.assertTrue(sol.isMatch("ab", ".*"))
        self.assertFalse(sol.isMatch("mississippi", "mis*is*p*."))
        self.assertFalse(sol.isMatch("ab", ".*c"))
        self.assertTrue(sol.isMatch("", "*"))

    def testIsMatchAgain(self):
        sol = DpSolution()
        self.assertFalse(sol.isMatch("aa", 'a'))
        self.assertTrue(sol.isMatch("aa", "a*"))
        self.assertTrue(sol.isMatch("aa", "aa"))
        self.assertTrue(sol.isMatch("ab", ".*"))
        self.assertFalse(sol.isMatch("mississippi", "mis*is*p*."))
        self.assertFalse(sol.isMatch("ab", ".*c"))
        self.assertTrue(sol.isMatch("", "*"))


unittest.main()
