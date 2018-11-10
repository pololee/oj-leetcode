import unittest

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        prev = [i for i in range(m + 1)] # target is word1

        for ch in word2:
            curr = [0 for i in range(m + 1)]
            curr[0] = prev[0] + 1

            for j in range(1, m + 1):
                a = word1[j-1]

                if ch == a:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j], prev[j-1], curr[j-1])
            prev = curr
        return prev[m]

class SolutionTest(unittest.TestCase):
    def testMinDistance(self):
        sol = Solution()
        self.assertEqual(3, sol.minDistance('horse', 'ros'))
        self.assertEqual(5, sol.minDistance('intention', 'execution'))

unittest.main()

